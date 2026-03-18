#!/usr/bin/env python3

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT_DIR = Path(__file__).resolve().parent.parent
SCHEMA_PATH = ROOT_DIR / "schemas" / "entity.schema.json"
REGISTRY_FILES = [
    ROOT_DIR / "registry" / "watchlist.json",
    ROOT_DIR / "registry" / "restricted.json",
    ROOT_DIR / "registry" / "blocked.json",
]
FULL_INDEX_PATH = ROOT_DIR / "registry" / "full-index.json"


def load_json(path: Path) -> Any:
    if not path.exists():
        raise FileNotFoundError(f"Missing file: {path.relative_to(ROOT_DIR)}")

    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"Invalid JSON in {path.relative_to(ROOT_DIR)}: {exc.msg} "
            f"(line {exc.lineno}, column {exc.colno})"
        ) from exc


def format_error_path(error: Any) -> str:
    if not error.path:
        return "<root>"
    return ".".join(str(part) for part in error.path)


def validate_entities(
    entities: list[Any], validator: Draft202012Validator, source_name: str
) -> bool:
    if not isinstance(entities, list):
        print(f"ERROR: {source_name}: expected an array of entities")
        return False

    has_error = False

    for index, entity in enumerate(entities):
        entity_id = "<unknown>"
        if isinstance(entity, dict):
            entity_id = str(entity.get("id", "<unknown>"))

        errors = sorted(validator.iter_errors(entity), key=lambda err: list(err.path))
        for error in errors:
            has_error = True
            path_str = format_error_path(error)
            print(
                f"ERROR: {source_name}: index={index} id={entity_id} "
                f"path={path_str}: {error.message}"
            )

    if not has_error:
        print(f"OK: {source_name}")

    return not has_error


def main() -> int:
    try:
        from jsonschema import Draft202012Validator
    except ImportError:
        print("ERROR: Missing dependency: jsonschema")
        print("Install it with: python3 -m pip install jsonschema")
        return 1

    try:
        schema = load_json(SCHEMA_PATH)
        validator = Draft202012Validator(schema)
    except (FileNotFoundError, ValueError) as exc:
        print(f"ERROR: {exc}")
        return 1

    all_ok = True

    for path in REGISTRY_FILES:
        try:
            entities = load_json(path)
        except (FileNotFoundError, ValueError) as exc:
            print(f"ERROR: {exc}")
            return 1

        all_ok = validate_entities(
            entities, validator, str(path.relative_to(ROOT_DIR))
        ) and all_ok

    try:
        full_index = load_json(FULL_INDEX_PATH)
    except (FileNotFoundError, ValueError) as exc:
        print(f"ERROR: {exc}")
        return 1

    if not isinstance(full_index, dict):
        print("ERROR: registry/full-index.json: expected an object")
        return 1

    entities = full_index.get("entities")
    if not isinstance(entities, list):
        print("ERROR: registry/full-index.json: missing entities array")
        return 1

    all_ok = validate_entities(
        entities, validator, "registry/full-index.json entities"
    ) and all_ok

    if not all_ok:
        print("Validation failed.")
        return 1

    print("All entity registry files passed validation.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

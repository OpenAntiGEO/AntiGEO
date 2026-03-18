#!/usr/bin/env python3

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT_DIR = Path(__file__).resolve().parent.parent
REGISTRY_FILES = [
    ROOT_DIR / "registry" / "watchlist.json",
    ROOT_DIR / "registry" / "restricted.json",
    ROOT_DIR / "registry" / "blocked.json",
]
FULL_INDEX_PATH = ROOT_DIR / "registry" / "full-index.json"
ENTITIES_COMPACT_PATH = ROOT_DIR / "registry" / "entities.compact.json"
MANIFEST_PATH = ROOT_DIR / "registry" / "manifest.json"

VERSION = "0.1.0-dev"
COMPACT_ENTITY_FIELDS = [
    "id",
    "name",
    "entity_type",
    "aliases",
    "domains",
    "current_status",
    "summary",
    "tags_topic",
    "tags_intent",
    "tags_risk",
    "status_reason",
    "related_entities",
]


def load_json_array(path: Path) -> list[Any]:
    if not path.exists():
        raise FileNotFoundError(f"Missing file: {path.relative_to(ROOT_DIR)}")

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"Invalid JSON in {path.relative_to(ROOT_DIR)}: {exc.msg} "
            f"(line {exc.lineno}, column {exc.colno})"
        ) from exc

    if not isinstance(data, list):
        raise ValueError(
            f"{path.relative_to(ROOT_DIR)}: expected a top-level array of entities"
        )

    return data


def require_entity_id(entity: Any, source_name: str, index: int) -> str:
    if not isinstance(entity, dict):
        raise ValueError(
            f"{source_name}: index={index}: expected an object with an 'id' field"
        )

    entity_id = entity.get("id")
    if entity_id is None:
        raise ValueError(f"{source_name}: index={index}: missing required field: id")

    if isinstance(entity_id, str):
        normalized = entity_id.strip()
    else:
        normalized = str(entity_id).strip()

    if not normalized:
        raise ValueError(f"{source_name}: index={index}: invalid id: {entity_id!r}")

    return normalized


def collect_entity_ids(entities: list[Any], source_name: str) -> dict[str, int]:
    id_to_index: dict[str, int] = {}

    for index, entity in enumerate(entities):
        entity_id = require_entity_id(entity, source_name, index)
        id_to_index[entity_id] = index

    return id_to_index


def find_duplicate_ids(sources: list[tuple[str, list[Any]]]) -> list[str]:
    first_seen: dict[str, tuple[str, int]] = {}
    duplicates: list[str] = []

    for source_name, entities in sources:
        for index, entity in enumerate(entities):
            entity_id = require_entity_id(entity, source_name, index)

            prev = first_seen.get(entity_id)
            if prev is None:
                first_seen[entity_id] = (source_name, index)
                continue

            prev_source, prev_index = prev
            duplicates.append(
                f"Duplicate entity id '{entity_id}' found in {prev_source} index={prev_index} "
                f"and {source_name} index={index}"
            )

    return duplicates


def utc_now_iso_z() -> str:
    # Keep it stable and readable: second precision, always 'Z'.
    return (
        datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def compact_entity(entity: dict[str, Any]) -> dict[str, Any]:
    compact = {field: entity.get(field) for field in COMPACT_ENTITY_FIELDS}

    for field in (
        "aliases",
        "domains",
        "tags_topic",
        "tags_intent",
        "tags_risk",
        "related_entities",
    ):
        value = compact.get(field)
        compact[field] = value if isinstance(value, list) else []

    return compact


def build_full_index(entities: list[Any], generated_at: str) -> dict[str, Any]:
    return {
        "version": VERSION,
        "generated_at": generated_at,
        "entities": entities,
    }


def build_compact_entities(entities: list[Any]) -> list[dict[str, Any]]:
    compact_entities: list[dict[str, Any]] = []

    for entity in entities:
        if not isinstance(entity, dict):
            continue
        compact_entities.append(compact_entity(entity))

    return compact_entities


def build_manifest(
    generated_at: str,
    counts_by_status: dict[str, int],
    entity_count: int,
) -> dict[str, Any]:
    return {
        "version": VERSION,
        "generated_at": generated_at,
        "entity_count": entity_count,
        "counts_by_status": counts_by_status,
        "files": {
            "watchlist": "registry/watchlist.json",
            "restricted": "registry/restricted.json",
            "blocked": "registry/blocked.json",
            "full_index": "registry/full-index.json",
            "entities_compact": "registry/entities.compact.json",
        },
    }


def write_json(path: Path, data: Any) -> None:
    text = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    tmp_path = path.with_suffix(path.suffix + ".tmp")
    tmp_path.write_text(text, encoding="utf-8")
    tmp_path.replace(path)


def main() -> int:
    loaded_sources: list[tuple[str, list[Any]]] = []
    merged_entities: list[Any] = []
    counts_by_status: dict[str, int] = {}

    for path in REGISTRY_FILES:
        source_name = str(path.relative_to(ROOT_DIR))
        status_name = path.stem
        try:
            entities = load_json_array(path)
        except (FileNotFoundError, ValueError) as exc:
            print(f"ERROR: {exc}")
            return 1

        # Ensure all entities have an id (error early with a clear location).
        try:
            collect_entity_ids(entities, source_name)
        except ValueError as exc:
            print(f"ERROR: {exc}")
            return 1

        loaded_sources.append((source_name, entities))
        merged_entities.extend(entities)
        counts_by_status[status_name] = len(entities)
        print(f"Loaded {source_name}")

    try:
        duplicates = find_duplicate_ids(loaded_sources)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 1

    if duplicates:
        for message in duplicates:
            print(f"ERROR: {message}")
        return 1

    generated_at = utc_now_iso_z()
    full_index = build_full_index(merged_entities, generated_at)
    compact_entities = build_compact_entities(merged_entities)
    manifest = build_manifest(
        generated_at=generated_at,
        counts_by_status=counts_by_status,
        entity_count=len(merged_entities),
    )

    try:
        write_json(FULL_INDEX_PATH, full_index)
        write_json(ENTITIES_COMPACT_PATH, compact_entities)
        write_json(MANIFEST_PATH, manifest)
    except OSError as exc:
        print(f"ERROR: Failed to write build output: {exc}")
        return 1

    print(f"Wrote {FULL_INDEX_PATH.relative_to(ROOT_DIR)}")
    print(f"Wrote {ENTITIES_COMPACT_PATH.relative_to(ROOT_DIR)}")
    print(f"Wrote {MANIFEST_PATH.relative_to(ROOT_DIR)}")
    print("Build completed successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

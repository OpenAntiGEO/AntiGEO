# Quick Start / 快速开始

[中文](#中文) | [English](#english)

---

## 中文

### 1. 文档目的

本文件用于帮助新用户或新贡献者在一台新机器上快速跑通 AntiGEO 当前已经可执行的最小工作流，包括依赖安装、数据校验与聚合构建。

### 2. 前置条件

开始前，请确认：

- 已安装 Python 3
- 已 clone AntiGEO 项目仓库

### 3. 创建虚拟环境

在仓库根目录运行：

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. 安装依赖

当前项目的 Python 依赖很少，只需安装 `requirements.txt` 中声明的最小依赖：

```bash
python3 -m pip install -r requirements.txt
```

### 5. 运行校验

运行以下命令，检查当前 `registry` 数据是否符合 `schemas/entity.schema.json` 的要求：

```bash
python3 scripts/validate.py
```

如果校验通过，脚本会输出成功信息；如果存在结构或字段问题，脚本会输出对应错误并返回非 0 退出码。

### 6. 运行构建

运行以下命令，根据 `registry/watchlist.json`、`registry/restricted.json` 和 `registry/blocked.json` 重新生成聚合索引 `registry/full-index.json`：

```bash
python3 scripts/build.py
```

构建脚本会执行基础一致性检查，包括输入文件存在性、JSON 可解析性、顶层数组检查，以及 entity `id` 重复检查。

### 7. 当前项目状态

当前 Quick Start 仅覆盖 entity registry 的最小链路：校验状态清单，并生成完整聚合索引。后续随着项目演进，文档会逐步补充提案、证据与治理相关流程。

### 8. 进一步阅读

如需了解项目背景、定义与治理规则，可继续查看：

- [README.md](../README.md)
- [docs/definition.md](./definition.md)
- [docs/governance.md](./governance.md)
- [docs/evidence-policy.md](./evidence-policy.md)
- [docs/voting.md](./voting.md)
- [docs/appeals.md](./appeals.md)
- [CONTRIBUTING.md](../CONTRIBUTING.md)

---

## English

### 1. Purpose

This document helps new users and contributors get the current AntiGEO repository running on a fresh machine with the smallest practical workflow: install dependencies, validate the registry data, and rebuild the aggregate index.

### 2. Prerequisites

Before you begin, make sure:

- Python 3 is installed
- The AntiGEO repository has been cloned locally

### 3. Create a Virtual Environment

From the repository root, run:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install Dependencies

The current Python footprint is intentionally small. Install the minimal dependencies listed in `requirements.txt`:

```bash
python3 -m pip install -r requirements.txt
```

### 5. Run Validation

Run the following command to validate the current `registry` data against `schemas/entity.schema.json`:

```bash
python3 scripts/validate.py
```

If validation passes, the script prints a success message. If the data contains structural or field-level issues, it prints clear errors and exits with a non-zero status code.

### 6. Run the Build Script

Run the following command to regenerate `registry/full-index.json` from `registry/watchlist.json`, `registry/restricted.json`, and `registry/blocked.json`:

```bash
python3 scripts/build.py
```

The build script performs basic consistency checks, including file existence, JSON parsing, top-level array validation, and duplicate entity `id` detection.

### 7. Current Project Status

This Quick Start currently covers only the minimal entity registry workflow: validating the status lists and generating the aggregate full index. Additional workflows for proposals, evidence, and governance will be documented as the project evolves.

### 8. Further Reading

For project context, definitions, and governance rules, see:

- [README.md](../README.md)
- [docs/definition.md](./definition.md)
- [docs/governance.md](./governance.md)
- [docs/evidence-policy.md](./evidence-policy.md)
- [docs/voting.md](./voting.md)
- [docs/appeals.md](./appeals.md)
- [CONTRIBUTING.md](../CONTRIBUTING.md)

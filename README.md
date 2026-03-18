# AntiGEO

[中文](#中文) | [English](#english)

---

## 中文

AntiGEO 是一套面向 provider 发布的 GEO 风险清单数据结构与数据包格式。当前仓库是一个最小 `reference implementation`，用于说明 package 结构、基础 schema、参考数据和最小工具链。

## 当前仓库提供什么

- `schemas/entity.schema.json`：entity 数据结构定义
- `schemas/override.schema.json`：override 数据结构定义
- `registry/`：reference registry data 与当前 package 导出
- `scripts/build.py`：构建脚本
- `scripts/validate.py`：校验脚本
- `docs/quick-start.md`：快速开始说明
- `requirements.txt`：当前最小 Python 依赖

## 基本模型

- provider 发布符合 AntiGEO 格式的数据包
- consumer 加载一个或多个 provider 数据包
- 用户本地白名单、本地 blocklist 与本地 override 的优先级高于外部 provider 数据

当前主仓库不追求维护唯一、中心化的统一名单。它更关注格式、兼容性和最小可消费链路。

## 当前数据包文件

当前 `registry/` 目录中的主要文件类型包括：

- `full-index.json`
- `entities.compact.json`
- `manifest.json`
- topic / intent / risk / domain / name 各类索引文件

这些文件共同构成当前最小 package 形态，用于支持搜索前初筛与搜索后命中场景。

## Quick Start

- [快速开始](./docs/quick-start.md)
- [参考数据包](./docs/reference-package.md)

## 当前状态

项目当前仍处于早期阶段。当前仓库主要承担最小规范与参考实现的角色；后续可以继续演进，但当前重点是保持格式清晰、结构简单、输出可消费。

## 许可

- [LICENSE](./LICENSE)

---

## English

AntiGEO is a GEO risk-registry data structure and package format for providers. This repository is a minimal `reference implementation` that demonstrates the package shape, foundational schemas, reference data, and the smallest useful toolchain.

## What This Repository Provides

- `schemas/entity.schema.json`: the entity schema
- `schemas/override.schema.json`: the override schema
- `registry/`: reference registry data and current package exports
- `scripts/build.py`: the build script
- `scripts/validate.py`: the validation script
- `docs/quick-start.md`: the quick-start guide
- `requirements.txt`: the current minimal Python dependencies

## Basic Model

- providers publish AntiGEO-compatible packages
- consumers load one or more provider packages
- local user allowlists, local blocklists, and local overrides take priority over external provider data

The main repository does not aim to maintain one centralized global registry. Its focus is format clarity, compatibility, and a minimal consumable flow.

## Current Package Files

The main file types currently exported under `registry/` include:

- `full-index.json`
- `entities.compact.json`
- `manifest.json`
- topic / intent / risk / domain / name index files

Together these files form the current minimal package shape for pre-search filtering and post-search matching.

## Quick Start

- [Quick Start](./docs/quick-start.md)
- [Reference Package](./docs/reference-package.md)

## Current Status

The project is still early-stage. At this stage, the repository mainly serves as a minimal specification core and reference implementation. It may continue to evolve, but the current priority is to keep the format clear, simple, and easy to consume.

## License

- [LICENSE](./LICENSE)

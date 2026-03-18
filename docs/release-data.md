# Release Data / Release 数据

[中文](#中文) | [English](#english)

---

## 中文

### 1. 文档目的

本文件用于说明 AntiGEO 当前 release 导出的数据文件、各文件的用途，以及次级项目建议如何理解和消费这些文件。

### 2. 总体设计思路

AntiGEO 当前的 release 数据设计分为两层：

- 完整聚合数据
- 面向次级项目消费的轻量实体集合与轻量索引

前者用于审查、调试和离线分析；后者用于浏览器插件、搜索插件、OpenClaw 插件、本地代理、RAG 中间层等次级项目在运行时做更直接的匹配和治理。

### 3. 当前导出文件

#### `registry/full-index.json`

- 用途：完整聚合数据。
- 结构：顶层为 object，包含 `version`、`generated_at` 和 `entities`。
- 适用阶段：适合调试、人工审查、离线分析与全量检查。

#### `registry/entities.compact.json`

- 用途：轻量实体集合。
- 结构：顶层为 array，每条记录仅保留次级项目常用的核心字段。
- 适用阶段：适合作为次级项目的主加载数据集。

#### `registry/manifest.json`

- 用途：release 元信息文件。
- 结构：顶层为 object，包含版本、生成时间、实体数量、状态计数和文件列表。
- 适用阶段：适合作为次级项目发现当前有哪些导出文件的入口。

#### `registry/tag-topic-to-entities.json`

- 用途：按主题 tag 召回候选 entity。
- 结构：顶层为 object，key 为 topic tag，value 为 entity id 数组。
- 适用阶段：适合搜索前的主题初筛。

#### `registry/tag-intent-to-entities.json`

- 用途：按意图 tag 缩小候选 entity 范围。
- 结构：顶层为 object，key 为 intent tag，value 为 entity id 数组。
- 适用阶段：适合搜索前的意图初筛。

#### `registry/tag-risk-to-entities.json`

- 用途：提供风险解释和治理辅助。
- 结构：顶层为 object，key 为 risk tag，value 为 entity id 数组。
- 适用阶段：适合搜索后解释命中原因，或为治理动作提供辅助上下文。

#### `registry/domain-to-entities.json`

- 用途：按域名精确命中 entity。
- 结构：顶层为 object，key 为 domain，value 为 entity id 数组。
- 适用阶段：适合搜索结果阶段基于 URL 或域名做快速匹配。

#### `registry/name-to-entities.json`

- 用途：按实体主名称和别名命中 entity。
- 结构：顶层为 object，key 为名称字符串，value 为 entity id 数组。
- 适用阶段：适合搜索结果阶段基于标题、摘要或结构化元信息做名称匹配。

### 4. 推荐消费流程

当前推荐采用两阶段消费模型。

第一阶段：搜索前

- 从 query 中识别主题与意图。
- 使用 `tag-topic-to-entities.json` 与 `tag-intent-to-entities.json` 初筛 candidate entities。
- 将筛出的 entity id 与 `entities.compact.json` 结合，形成较小的候选治理范围。

第二阶段：搜索后

- 对结果 URL、域名、标题、摘要或结构化元信息做匹配。
- 使用 `domain-to-entities.json` 与 `name-to-entities.json` 命中 entity。
- 再结合 `entities.compact.json` 中的 `current_status`、`tags_risk`、`summary`、`status_reason` 等字段决定下游治理动作。

### 5. 字段与索引的关系

- `tags_topic` 对应 `registry/tag-topic-to-entities.json`
- `tags_intent` 对应 `registry/tag-intent-to-entities.json`
- `tags_risk` 对应 `registry/tag-risk-to-entities.json`
- `domains` 对应 `registry/domain-to-entities.json`
- `name` 与 `aliases` 对应 `registry/name-to-entities.json`

这些索引都只保存 entity id，而不内嵌完整 entity 数据。次级项目通常应将索引命中的 id 再映射回 `entities.compact.json` 中的对应记录。

### 6. 当前范围说明

当前 release 数据只覆盖 entity registry 的基础导出。当前结构尚未提供 evidence 或 proposal 的消费索引，也不包含更复杂的发布包装机制。

这意味着当前结构仍处于早期阶段，但已经足以支撑一个最小可用的消费链路：

- 搜索前初筛
- 搜索后命中
- 基于状态与风险标签的基础治理

### 7. 给次级项目的建议

- 优先使用 `registry/manifest.json` 发现当前可用产物。
- 优先加载 `registry/entities.compact.json` 作为主消费数据集。
- 将 `registry/full-index.json` 保留给调试、审查和离线分析。
- 一般不建议在每次搜索请求中直接加载 `registry/full-index.json` 全量内容。

本说明文档会随着 AntiGEO release 数据结构的演进而继续公开更新。

---

## English

### 1. Purpose

This document describes the data files currently exported by AntiGEO releases, what each file is for, and how downstream projects are expected to consume them.

### 2. Overall Design

The current AntiGEO release data model has two layers:

- full aggregate data
- lightweight entities and lightweight indexes for downstream consumption

The first layer is useful for review, debugging, and offline analysis. The second layer is intended for browser extensions, search plugins, OpenClaw plugins, local proxies, RAG middleware, and similar downstream systems that need direct runtime matching and governance support.

### 3. Current Exported Files

#### `registry/full-index.json`

- Purpose: full aggregate data.
- Structure: a top-level object containing `version`, `generated_at`, and `entities`.
- Best use: debugging, human review, offline analysis, and full-record inspection.

#### `registry/entities.compact.json`

- Purpose: lightweight entity collection.
- Structure: a top-level array where each record keeps only the core fields commonly needed by downstream systems.
- Best use: the primary runtime dataset for downstream consumers.

#### `registry/manifest.json`

- Purpose: release metadata.
- Structure: a top-level object containing version, generation time, entity counts, status counts, and a file list.
- Best use: the entry point for discovering which exported files are available in the current release.

#### `registry/tag-topic-to-entities.json`

- Purpose: recall candidate entities by topic tag.
- Structure: a top-level object mapping topic tags to arrays of entity ids.
- Best use: topic-level filtering before search or retrieval.

#### `registry/tag-intent-to-entities.json`

- Purpose: narrow candidate entities by intent tag.
- Structure: a top-level object mapping intent tags to arrays of entity ids.
- Best use: intent-level filtering before search or retrieval.

#### `registry/tag-risk-to-entities.json`

- Purpose: provide risk explanation and governance support.
- Structure: a top-level object mapping risk tags to arrays of entity ids.
- Best use: post-search interpretation and governance context.

#### `registry/domain-to-entities.json`

- Purpose: match entities by domain.
- Structure: a top-level object mapping domains to arrays of entity ids.
- Best use: fast matching during result-stage URL or domain processing.

#### `registry/name-to-entities.json`

- Purpose: match entities by primary name and aliases.
- Structure: a top-level object mapping names to arrays of entity ids.
- Best use: result-stage matching against titles, snippets, or structured metadata.

### 4. Recommended Consumption Flow

The current recommendation is a two-stage consumption model.

Stage 1: before search

- Identify topic and intent signals from the query.
- Use `tag-topic-to-entities.json` and `tag-intent-to-entities.json` to narrow the candidate entity set.
- Join the resulting entity ids with `entities.compact.json` to produce a smaller governance candidate set.

Stage 2: after search

- Match against result URLs, domains, titles, snippets, or structured metadata.
- Use `domain-to-entities.json` and `name-to-entities.json` to identify relevant entities.
- Then use fields such as `current_status`, `tags_risk`, `summary`, and `status_reason` from `entities.compact.json` to determine downstream governance behavior.

### 5. Relationship Between Fields and Indexes

- `tags_topic` maps to `registry/tag-topic-to-entities.json`
- `tags_intent` maps to `registry/tag-intent-to-entities.json`
- `tags_risk` maps to `registry/tag-risk-to-entities.json`
- `domains` maps to `registry/domain-to-entities.json`
- `name` and `aliases` map to `registry/name-to-entities.json`

These indexes store only entity ids rather than full entity records. In most cases, downstream systems should map matched ids back to the corresponding records in `entities.compact.json`.

### 6. Current Scope

The current release data covers only the foundational entity registry exports. It does not yet provide consumer indexes for evidence or proposals, and it does not introduce more complex release packaging mechanisms.

That means the structure is still early-stage, but it is already sufficient for a minimal downstream workflow:

- pre-search candidate filtering
- post-search entity matching
- basic governance based on status and risk tags

### 7. Suggestions for Downstream Projects

- Use `registry/manifest.json` first to discover available outputs.
- Prefer `registry/entities.compact.json` as the primary runtime dataset.
- Keep `registry/full-index.json` for debugging, review, and offline analysis.
- In most cases, avoid loading the full contents of `registry/full-index.json` on every search request.

This document will continue to be updated publicly as the AntiGEO release data structure evolves.

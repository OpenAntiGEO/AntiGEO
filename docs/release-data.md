# Release Data / Release 数据

[中文](#中文) | [English](#english)

---

## 中文

### 1. 文档目的

本文件用于说明 AntiGEO 当前 release 数据包会导出哪些文件、这些文件分别承担什么作用，以及 consumer 应如何理解和消费这些文件。

### 2. 当前定位

AntiGEO 当前的 release 数据应理解为 provider package 的一种标准化形态。主项目当前会生成一份 reference package，作为 schema、索引格式、工具链和消费模型的参考实现；其它 provider 也可以按相同格式发布自己的数据包。

因此，这些文件既可以来自主项目，也可以来自任何兼容 AntiGEO 规范的 provider。consumer 面向的是格式兼容的数据源，而不是某一个唯一仓库。

### 3. 总体设计思路

当前 release 数据分为两层：

- 完整聚合数据
- 面向 consumer 的轻量实体集合与轻量索引

完整聚合数据适合调试、审查和离线分析。轻量实体集合与索引更适合浏览器插件、搜索插件、OpenClaw 插件、本地代理、RAG 中间层等 consumer 在运行时加载。

### 4. 当前导出文件

#### `registry/full-index.json`

- 用途：完整聚合数据。
- 结构：顶层 object，包含 `version`、`generated_at`、`entities`。
- 适用阶段：适合调试、人工审查、离线分析与全量回查。

#### `registry/entities.compact.json`

- 用途：轻量实体集合。
- 结构：顶层 array，只保留 consumer 常用核心字段。
- 适用阶段：适合作为运行时主数据集。

#### `registry/manifest.json`

- 用途：release 元信息与文件发现入口。
- 结构：顶层 object，包含版本、生成时间、实体数量、状态计数与文件路径映射。
- 适用阶段：适合作为 consumer 发现当前 provider package 中有哪些产物的入口。

#### `registry/tag-topic-to-entities.json`

- 用途：按主题标签召回候选 entity。
- 结构：顶层 object，key 为 topic tag，value 为 entity id 数组。
- 适用阶段：搜索前初筛。

#### `registry/tag-intent-to-entities.json`

- 用途：按意图标签缩小候选 entity 范围。
- 结构：顶层 object，key 为 intent tag，value 为 entity id 数组。
- 适用阶段：搜索前初筛。

#### `registry/tag-risk-to-entities.json`

- 用途：补充风险解释和治理辅助上下文。
- 结构：顶层 object，key 为 risk tag，value 为 entity id 数组。
- 适用阶段：搜索后治理、解释命中原因、辅助下游动作。

#### `registry/domain-to-entities.json`

- 用途：按域名命中 entity。
- 结构：顶层 object，key 为 domain，value 为 entity id 数组。
- 适用阶段：搜索结果阶段基于 URL 或域名快速命中。

#### `registry/name-to-entities.json`

- 用途：按主名称和别名命中 entity。
- 结构：顶层 object，key 为名称字符串，value 为 entity id 数组。
- 适用阶段：搜索结果阶段基于标题、摘要或结构化元信息做名称匹配。

### 5. 推荐消费流程

当前推荐采用两阶段消费模型。

第一阶段：搜索前初筛

- 从 query 中识别主题与意图信号。
- 使用 `tag-topic-to-entities.json` 与 `tag-intent-to-entities.json` 初筛 candidate entities。
- 将命中的 entity id 映射到 `entities.compact.json`，形成更小的候选治理范围。

第二阶段：搜索后治理

- 对结果 URL、域名、标题、摘要和结构化元信息做匹配。
- 使用 `domain-to-entities.json` 与 `name-to-entities.json` 命中相关 entity。
- 再结合 `entities.compact.json` 中的 `current_status`、`tags_risk`、`summary`、`status_reason` 等字段决定下游治理动作。

`tag-risk-to-entities.json` 更适合作为搜索后解释和治理辅助层，而不是单独替代实体级判断。

### 6. 为什么这些文件适合 provider 模式

这些 release 文件只描述数据格式、索引方式和最小消费模型，不要求数据内容必须由主项目独占维护。任何 provider 只要遵守相同的 schema、索引结构和构建约定，就可以发布自己的 package。

这也是当前主项目的定位重点：提供规范、工具链、reference package 和消费建议，而不是要求所有清单都回流到单一中心仓库。

### 7. 给 consumer 的简短建议

- 优先使用 `registry/manifest.json` 发现 provider package 的可用产物。
- 优先加载 `registry/entities.compact.json` 作为运行时主数据集。
- 将 `registry/full-index.json` 保留给调试、离线分析和审查。
- 一般不建议在每次搜索请求中直接加载 `registry/full-index.json` 全量内容。
- 如果同时订阅多个 provider，建议将主项目或任意 provider 数据都视为输入源，再由本地规则决定最终覆盖结果。

### 8. 当前范围说明

当前 release 数据主要覆盖 entity registry 与其对应的轻量索引导出。evidence 与 proposal 目前已经有 schema 和参考样例数据，但尚未进入当前 release 索引层。

因此，当前结构仍处于早期阶段，但已经足以支撑最小消费链路：

- 搜索前初筛
- 搜索后命中
- 基于状态与风险标签的基础治理

本说明文档会随着 AntiGEO release 数据结构的演进而继续公开更新。

---

## English

### 1. Purpose

This document explains which files are currently exported as AntiGEO release data, what each file is for, and how consumers are expected to interpret and use them.

### 2. Current Positioning

The current AntiGEO release data should be understood as a standardized provider package format. The main repository currently produces a reference package as a reference implementation for schemas, index formats, tooling, and consumption patterns, but other providers may publish their own packages in the same format.

That means these files may come either from the main project or from any AntiGEO-compatible provider. Consumers are designed to work with format-compatible data sources rather than with a single mandatory repository.

### 3. Overall Design

The current release package has two layers:

- full aggregate data
- lightweight entities and lightweight indexes for consumer use

The full aggregate layer is best suited for debugging, review, and offline analysis. The lightweight entity and index layer is better suited for runtime loading by browser extensions, search integrations, OpenClaw plugins, local proxies, RAG middleware, and similar consumers.

### 4. Current Exported Files

#### `registry/full-index.json`

- Purpose: full aggregate data.
- Structure: a top-level object with `version`, `generated_at`, and `entities`.
- Best use: debugging, human review, offline analysis, and full-record inspection.

#### `registry/entities.compact.json`

- Purpose: lightweight entity collection.
- Structure: a top-level array containing only the core fields commonly needed at runtime.
- Best use: the primary runtime dataset.

#### `registry/manifest.json`

- Purpose: release metadata and file discovery.
- Structure: a top-level object containing version, generation time, entity counts, status counts, and a file map.
- Best use: the entry point for discovering what outputs exist in a provider package.

#### `registry/tag-topic-to-entities.json`

- Purpose: recall candidate entities by topic tag.
- Structure: a top-level object mapping topic tags to entity id arrays.
- Best use: pre-search filtering.

#### `registry/tag-intent-to-entities.json`

- Purpose: narrow candidate entities by intent tag.
- Structure: a top-level object mapping intent tags to entity id arrays.
- Best use: pre-search filtering.

#### `registry/tag-risk-to-entities.json`

- Purpose: provide risk explanation and governance context.
- Structure: a top-level object mapping risk tags to entity id arrays.
- Best use: post-search governance and explanation support.

#### `registry/domain-to-entities.json`

- Purpose: match entities by domain.
- Structure: a top-level object mapping domains to entity id arrays.
- Best use: fast result-stage matching based on URL or domain.

#### `registry/name-to-entities.json`

- Purpose: match entities by primary name and aliases.
- Structure: a top-level object mapping names to entity id arrays.
- Best use: result-stage matching against titles, snippets, or structured metadata.

### 5. Recommended Consumption Flow

The current recommendation is a two-stage consumption model.

Stage 1: pre-search filtering

- Identify topic and intent signals from the query.
- Use `tag-topic-to-entities.json` and `tag-intent-to-entities.json` to narrow the candidate set.
- Map the matched entity ids into `entities.compact.json` to form a smaller governance candidate set.

Stage 2: post-search governance

- Match against result URLs, domains, titles, snippets, and structured metadata.
- Use `domain-to-entities.json` and `name-to-entities.json` to identify relevant entities.
- Then use fields such as `current_status`, `tags_risk`, `summary`, and `status_reason` from `entities.compact.json` to decide downstream governance behavior.

`tag-risk-to-entities.json` is better treated as a post-search explanation and governance-support layer than as a replacement for entity-level judgment.

### 6. Why These Files Fit The Provider Model

These release files describe data formats, indexing patterns, and a minimal consumption model. They do not require registry content to be maintained only by the main project. Any provider that follows the same schemas, index structures, and build conventions can publish its own package.

That is also the current emphasis of the main project: provide specifications, tooling, a reference package, and consumption guidance rather than require all registry content to flow through a single central repository.

### 7. Short Guidance For Consumers

- Use `registry/manifest.json` first to discover the outputs in a provider package.
- Prefer `registry/entities.compact.json` as the primary runtime dataset.
- Keep `registry/full-index.json` for debugging, review, and offline analysis.
- In most cases, avoid loading the full contents of `registry/full-index.json` on every search request.
- If you subscribe to multiple providers, treat both the main project and third-party providers as input sources, then let local rules determine the final override outcome.

### 8. Current Scope

The current release layer mainly covers the entity registry and its lightweight indexes. Evidence and proposal data already have schemas and sample records, but they are not yet part of the current release index layer.

The structure is therefore still early-stage, but it is already sufficient for a minimal workflow:

- pre-search filtering
- post-search matching
- basic governance based on status and risk tags

This document will continue to be updated publicly as the AntiGEO release data structure evolves.

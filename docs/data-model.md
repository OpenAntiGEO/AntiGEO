# Data Model / 数据模型

[中文](#中文) | [English](#english)

---

## 中文

### 1. 文档目的

本文件用于说明 AntiGEO 当前的数据模型、核心对象及它们之间的关系。它面向主项目贡献者、provider 开发者和 consumer / 次级项目开发者，用于帮助理解整体设计，而不是替代 schema 文件本身。

### 2. 总体设计思路

AntiGEO 当前的数据模型可以概括为三层：

- 治理对象层
- 治理支持材料层
- 消费与覆盖层

治理对象层主要围绕 entity 展开；治理支持材料层主要包括 evidence 和 proposal；消费与覆盖层主要包括 provider package、consumer 与用户本地规则。主项目当前重点提供的是这三层之间可互操作的数据结构、reference implementation 和最小消费模型。

从当前 provider 模式看，entity、override、provider package 与 consumer 构成核心模型；evidence 与 proposal 更接近可选治理扩展对象。当前 release 数据主链路主要围绕 entity 层展开。

### 3. entity 是什么

entity 是 AntiGEO 当前清单中的核心治理对象。它表示一个可识别的对象，例如品牌、组织、域名、内容网络、站群或其它相关实体。

entity 主要承载以下信息：

- 身份信息
- 当前状态
- 主题标签、意图标签与风险标签
- 面向下游消费所需的核心上下文

当前 release 导出的核心文件主要围绕 entity 组织，例如 full index、compact entities，以及 topic / intent / risk / domain / name 各类索引。

### 4. evidence 是什么

evidence 是支持某个 entity 或某类治理判断的证据记录。它描述的是可复核材料、观察记录或支持性线索，而不是直接等同于最终状态结论。

在当前项目中，evidence 主要服务于治理与审查层，用来支撑对 entity 的评估、提案形成和后续讨论。当前 evidence 在主项目中更多处于 schema + sample data 阶段，尚未进入当前 release 索引层。

这也意味着 evidence 不是所有 provider 的强制要求。provider 可以提供 evidence 来提升透明度、可解释性和信任度，也可以先只提供核心 package。

### 5. proposal 是什么

proposal 是治理动作记录。它用于描述某个对象、状态或相关记录应如何新增、调整、复审、修正或移除。

proposal 通常依赖 entity，也常常引用 evidence。它表达的是治理流程中的建议或动作请求，而不是最终裁定本身。换言之，proposal 是治理过程中的记录对象，而不是终局结论。

在当前模型中，proposal 同样更接近治理扩展层对象，而不是 provider / consumer 互通的最低必需对象。

### 6. override 是什么

override 是消费侧的本地覆盖规则。它不属于主项目治理执行的一部分，也不是 provider 必须统一裁定的对象。

override 的作用是让用户或次级项目在本地控制最终行为，例如本地白名单、本地 blocklist 或其它本地覆盖规则。按照 AntiGEO 当前推荐的优先级思想，本地 override 的优先级高于外部 provider 数据。

### 7. provider package 是什么

provider package 是由某个 provider 发布的一组符合 AntiGEO 规范的数据文件。它是 consumer 实际加载和消费的对象。

当前主项目仓库可以视为一个 reference package / reference implementation。当前典型 provider package 至少包括：

- `manifest`
- `entities.compact`
- 各类索引文件

在更完整的场景中，provider 还可以维护 entity、evidence、proposal 等原始数据或治理记录，但 consumer 在运行时最常直接接触的是 release 数据层。

对于当前最小可消费链路，provider package 不要求必须包含 evidence 或 proposal 导出。

### 8. consumer 是什么

consumer 是消费 AntiGEO 数据的系统，例如浏览器插件、搜索插件、OpenClaw 插件、本地代理、RAG 中间层或其它下游工具。

consumer 主要负责：

- 订阅一个或多个 provider
- 加载 provider package
- 应用用户本地 override
- 在搜索前和搜索后使用相关数据

consumer 并不一定参与主项目治理，但它负责把 provider 数据转化为实际的检索、筛选、解释和治理行为。

### 9. 当前推荐的数据流

当前推荐的数据流可以分为三个阶段。

第一阶段：provider 侧

- 使用 schema 定义数据结构
- 组织 entity、evidence、proposal 等数据
- 通过 build 导出 provider package

第二阶段：consumer 侧

- 加载 provider package
- 搜索前按 topic / intent 索引初筛 candidate entities
- 搜索后按 domain / name 索引命中 entity
- 再结合 entity 的 `current_status`、`tags_risk`、`summary`、`status_reason` 等信息做治理

第三阶段：用户本地控制

- 用户本地白名单
- 用户本地 blocklist
- 用户本地 override
- 本地规则优先于 provider 数据

这三阶段共同构成了当前 AntiGEO 的最小可运行数据流：provider 负责发布兼容数据，consumer 负责加载和应用，最终控制权保留在本地。

### 10. 当前范围说明

当前项目已经完成 entity / evidence / proposal / override 的基础 schema。当前 build / validate 主链路主要围绕 entity registry 与 release 数据层；evidence 与 proposal 目前仍主要作为样例和治理层数据存在。

因此，当前数据模型仍处于早期阶段，但主干结构已经建立：

- 对象层次已经明确
- provider package 形态已经落地
- consumer 的最小消费模型已经明确
- 本地优先级原则已经明确

本数据模型文档会随着 schema、provider package 和 consumer 模式的演进而继续公开更新。

---

## English

### 1. Purpose

This document explains the current AntiGEO data model, its core objects, and the relationships between them. It is intended for main-project contributors, provider authors, and consumer developers. Its role is to explain the overall design rather than replace the schema files themselves.

### 2. Overall Design

The current AntiGEO data model can be understood as three layers:

- a governance object layer
- a governance support-material layer
- a consumption and override layer

The governance object layer is centered on entities. The support-material layer mainly includes evidence and proposals. The consumption and override layer mainly includes provider packages, consumers, and local user rules. The main project currently focuses on providing interoperable structures across these layers, together with a reference implementation and a minimal consumption model.

Within the current provider model, entity, override, provider package, and consumer make up the core model, while evidence and proposals are better understood as optional governance-extension objects. The current release-data path is centered primarily on the entity layer.

### 3. What An Entity Is

An entity is the core governance object in the current AntiGEO registry model. It represents an identifiable object such as a brand, organization, domain, content network, site cluster, or related entity.

An entity mainly carries:

- identity information
- current status
- topic, intent, and risk tags
- core context needed by downstream consumers

The current release exports are organized primarily around entities, including the full index, compact entities, and the topic / intent / risk / domain / name indexes.

### 4. What Evidence Is

Evidence is a record that supports assessment of an entity or a governance-related judgment. It represents verifiable material, observed patterns, or supporting records rather than a final status conclusion by itself.

In the current project, evidence mainly serves the governance and review layer by supporting entity evaluation, proposal formation, and later discussion. At the moment, evidence in the main project is still mostly at the schema + sample-data stage and is not yet part of the current release index layer.

That also means evidence is not mandatory for every provider. A provider may publish evidence to improve transparency, explainability, and trust, but it may also choose to publish only the core package.

### 5. What A Proposal Is

A proposal is a governance-action record. It describes how an entity, status, or related record should be added, adjusted, re-reviewed, corrected, or removed.

A proposal usually depends on entities and often references evidence. It expresses a governance request or action under review rather than a final determination. In that sense, a proposal is a process record, not the final result itself.

In the current model, proposals also belong more naturally to the governance-extension layer than to the minimum provider / consumer interoperability layer.

### 6. What An Override Is

An override is a local consumption-side rule. It is not part of the main project's governance execution model, and it is not something that providers must settle centrally.

Its purpose is to let users or downstream systems control final behavior locally, for example through a local allowlist, local blocklist, or other local override rule. Under AntiGEO's current recommended priority model, local overrides take precedence over external provider data.

### 7. What A Provider Package Is

A provider package is a set of AntiGEO-compatible data files published by a provider. It is the object that consumers actually load and use.

The current main repository can be treated as a reference package / reference implementation. A typical provider package currently includes at least:

- `manifest`
- `entities.compact`
- index files

In more complete scenarios, a provider may also maintain raw entity, evidence, and proposal data or governance records, but the runtime layer most directly consumed by downstream systems is the release-data layer.

For the current minimal consumable flow, a provider package is not required to include evidence or proposal exports.

### 8. What A Consumer Is

A consumer is a system that uses AntiGEO data, such as a browser extension, search plugin, OpenClaw plugin, local proxy, RAG middleware, or another downstream tool.

A consumer is mainly responsible for:

- subscribing to one or more providers
- loading provider packages
- applying local user overrides
- using the data before and after search

A consumer does not need to run the main project's governance process, but it does turn provider data into actual retrieval, filtering, explanation, and governance behavior.

### 9. The Current Recommended Data Flow

The recommended data flow currently has three stages.

Stage 1: provider side

- use schemas to define the structure
- organize entity, evidence, proposal, and related data
- build and export a provider package

Stage 2: consumer side

- load the provider package
- use topic / intent indexes for pre-search candidate filtering
- use domain / name indexes for post-search entity matching
- then apply fields such as `current_status`, `tags_risk`, `summary`, and `status_reason` from entities to drive governance behavior

Stage 3: local user control

- local allowlist
- local blocklist
- local override
- local rules take priority over provider data

Together these three stages form the current minimal operational AntiGEO flow: providers publish compatible data, consumers load and apply it, and final control remains local.

### 10. Current Scope

The project already has foundational schemas for entity, evidence, proposal, and override. The main build / validate workflow is currently centered on the entity registry and release-data layer, while evidence and proposal records still function mainly as sample and governance-layer data.

The model is therefore still early-stage, but its backbone is already in place:

- the object layers are defined
- the provider-package form is implemented
- the minimal consumer model is established
- the local-priority principle is explicit

This data-model document will continue to evolve publicly as the schemas, provider packages, and consumer model mature.

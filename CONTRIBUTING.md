# Contributing / 贡献指南

[中文](#中文) | [English](#english)

---

## 中文

### 1. 欢迎与定位

欢迎参与 AntiGEO。当前主项目首先是一个规范层、reference implementation 与 reference package 项目，因此最重要的贡献方向包括 schema、文档、工具链、参考样例数据，以及 consumer 如何使用这些数据的说明。

主项目欢迎贡献，但不要求所有清单都提交到本仓库。若你希望长期维护自己的清单来源，也完全可以基于 AntiGEO 规范建立独立 provider 仓库或独立数据源。

当前贡献也可以大致分为两类：核心规范层贡献，以及可选治理扩展层贡献。

### 2. 当前最需要的贡献

当前主项目尤其欢迎以下类型的贡献：

- 修订和完善 schema
- 改进 build / validate 脚本
- 改进 release 数据格式与索引说明
- 补充或修正 reference entity / evidence / proposal 样例
- 改进定义、治理、provider 模式与 FAQ 文档
- 提高术语一致性、可读性和项目边界清晰度

其中，entity schema、override schema、release 数据格式、manifest、compact entities、索引和 consumer 优先级模型属于当前核心规范层；evidence、proposal、governance、appeals、voting 则更接近可选治理扩展层。

### 3. 如果你想维护自己的 provider

如果你的目标是维护一份独立风险清单来源，推荐做法通常是：

- 参考 AntiGEO 的 schema 与 release 数据格式
- 参考当前 reference package 的构建与校验方式
- 在自己的仓库或数据源中维护具体 registry 内容
- 自行决定 provider 的审核、更新与发布节奏

换言之，AntiGEO 主项目更像公共规范与参考实现，而不是所有清单内容的唯一汇总点。

如果你想做一个轻量 provider，并不需要一次性实现 evidence、voting、appeals 等全套治理模块；只要核心 package 与 consumer 兼容，就已经可以工作。若你希望提供更高透明度或更强可解释性，则可以进一步采用这些可选扩展。

### 4. 提交前建议阅读

提交前建议先阅读：

- [README.md](./README.md)
- [docs/definition.md](./docs/definition.md)
- [docs/release-data.md](./docs/release-data.md)
- [docs/provider-model.md](./docs/provider-model.md)
- [docs/governance.md](./docs/governance.md)
- [docs/evidence-policy.md](./docs/evidence-policy.md)

### 5. 提交内容的基本要求

提交内容应尽量满足以下要求：

- 内容清楚、范围明确、可复核
- 术语使用与项目文档保持一致
- 不要只提交结论，尽量说明理由与上下文
- 修改 schema、工具或 release 格式时，应尽量考虑兼容性和 consumer 影响
- 提交 reference data 时，应明确其为样例、参考记录或主项目参考内容，而不是要求其自动成为全局唯一名单

### 6. 不鼓励或可能被拒绝的提交

以下内容不鼓励，或可能被拒绝：

- 无证据的指控
- 仅基于品牌偏好或主观印象的要求
- 试图把主项目强行变成所有 provider 的唯一中心名单
- 重复提交且无新增内容
- 骚扰、攻击性或竞争性滥用
- 明显脱离项目范围的内容

### 7. 文档、工具与样例同样重要

在当前阶段，以下贡献同样非常重要：

- 文档澄清
- 术语统一
- release 数据说明优化
- provider 模式说明补充
- 样例数据可读性提升
- build / validate 行为收敛

这些工作直接影响 provider 与 consumer 是否能够稳定对齐。

### 8. 关于参考数据的提醒

当前仓库中的 registry、sample evidence、sample proposals 与 release 导出，都应被理解为 reference data / reference package。它们可以被修订、替换、补充和审查，但不应被理解为所有外部数据源都必须提交到本仓库统一维护。

### 9. 协作方式

协作时请尽量保持：

- 克制
- 透明
- 以证据和上下文为中心
- 尊重项目边界
- 尊重用户与 consumer 的本地控制优先级

### 10. 早期项目说明

AntiGEO 仍处于早期阶段，贡献方式与目录边界仍可能继续公开收敛。若你不确定某项内容应该进入主项目还是独立 provider，更推荐先把问题表述清楚，再围绕“规范层还是数据源本身”这个边界来决定落点。

---

## English

### 1. Welcome and Positioning

Contributions to AntiGEO are welcome. The main repository is currently best understood as a specification layer, reference implementation, and reference package project. That means the most important contribution areas include schemas, documentation, tooling, sample data, and guidance for how consumers should use those outputs.

The main project welcomes contributions, but it does not require all registry content to be submitted here. If you want to maintain your own long-lived registry source, you can build an independent provider repository or data source on top of AntiGEO conventions.

At a high level, contributions can also be understood as belonging either to the core specification layer or to the optional governance-extension layer.

### 2. What Contributions Are Most Useful Right Now

The main project is especially interested in:

- refining and extending schemas
- improving build / validate scripts
- improving release-data formats and index guidance
- adding or correcting reference entity / evidence / proposal samples
- improving definitions, governance, provider-model, and FAQ documentation
- making terminology, readability, and project boundaries clearer

Within that structure, the entity schema, override schema, release-data format, manifest, compact entities, indexes, and consumer priority model belong to the current core specification layer, while evidence, proposals, governance, appeals, and voting belong more naturally to the optional governance-extension layer.

### 3. If You Want To Maintain Your Own Provider

If your goal is to maintain an independent risk-registry source, the usual approach is:

- follow AntiGEO schemas and release-data formats
- use the current reference package as a tooling and structure reference
- maintain your concrete registry content in your own repository or data source
- define your own review, update, and publication cadence

In other words, the main AntiGEO repository is better treated as a public specification and reference implementation than as the single required home for all registry content.

If you want to build a lightweight provider, you do not need to implement the full evidence / voting / appeals stack all at once. As long as the core package is compatible with the current consumer model, it can already work. If you want to offer higher transparency or stronger explainability, you can adopt those optional extensions as well.

### 4. Recommended Reading Before Contributing

Please review the following before contributing:

- [README.md](./README.md)
- [docs/definition.md](./docs/definition.md)
- [docs/release-data.md](./docs/release-data.md)
- [docs/provider-model.md](./docs/provider-model.md)
- [docs/governance.md](./docs/governance.md)
- [docs/evidence-policy.md](./docs/evidence-policy.md)

### 5. Basic Expectations For Submissions

Submissions should be:

- clear in scope and verifiable where applicable
- consistent with project terminology
- supported by rationale and context rather than conclusions alone
- mindful of compatibility and consumer impact when changing schemas, tooling, or release formats
- explicit that reference data in the main repository is sample or reference material rather than an automatic global registry decision

### 6. Disfavored or Potentially Rejected Contributions

The following are disfavored or may be rejected:

- accusations without evidence
- requests based only on brand preference or subjective impression
- attempts to force the main project into becoming the single central registry for every provider
- repetitive submissions without meaningful new content
- harassing, aggressive, or competitively abusive behavior
- content clearly outside project scope

### 7. Documentation, Tooling, and Samples Matter

At the current stage, the following are also high-value contributions:

- documentation clarification
- terminology consistency
- better release-data guidance
- clearer provider-model explanations
- more readable sample data
- tighter build / validate behavior

These directly affect whether providers and consumers can align reliably.

### 8. A Note on Reference Data

The registry data, sample evidence, sample proposals, and release outputs in this repository should all be treated as reference data / a reference package. They may be revised, replaced, expanded, and reviewed, but they should not be read as requiring every external data source to be maintained in this one repository.

### 9. Collaboration Style

Please aim to keep collaboration:

- restrained
- transparent
- evidence and context centered
- respectful of project boundaries
- respectful of user and consumer local-priority control

### 10. Early-Stage Project Note

AntiGEO is still early-stage, and contribution patterns and repository boundaries may continue to evolve publicly. If you are unsure whether something belongs in the main project or in an independent provider, it is usually best to frame the question first and decide based on whether the contribution belongs to the specification layer or to a concrete data source.

# Governance / 治理

[中文](#中文) | [English](#english)

---

## 中文

### 1. 文档目的

本文件用于定义 AntiGEO 主项目的治理框架，以及主项目如何公开维护 schema、reference implementation、reference data 和相关文档。

本文件首先约束主项目自身仓库内容；外部 provider 可以参考这套框架，也可以在兼容 AntiGEO 数据格式的前提下采用自己的治理实践。

### 2. 主项目治理的对象

当前主项目治理的对象主要包括：

- schema 与数据结构约定
- build / validate 工具链
- reference registry
- reference evidence / proposal 样例
- release 数据格式与消费模型文档

主项目不是所有 provider 的唯一治理中心。它治理的是自己的 reference implementation 和参考内容，而不是替所有 provider 统一裁决具体清单。

### 3. 治理原则

AntiGEO 主项目治理应遵循以下原则：

- 证据优先
- 可复核
- 谨慎认定
- 透明与可审计
- 一致性
- 可申诉与可复审
- 尽量避免主观偏好、品牌立场或竞争性滥用

对于 reference data，社区应持续关注**系统性**、**规模化**与**可复核**三个核心维度。对于格式、工具与文档，则应优先关注清晰性、稳定性、可扩展性与兼容性。

### 4. 可以治理哪些事项

主项目治理至少可以处理以下事项：

- 修订 schema
- 修订 release 数据格式
- 修订 build / validate 行为
- 更新 reference registry 样例
- 更新 evidence / proposal 样例
- 修订定义、治理、provider 模式与消费说明文档
- 处理申诉、复审与文档性更正

### 5. 关于 reference data 的理解

当前仓库中的 registry、sample evidence、sample proposals 与 build 导出文件，均应被视为参考样例或 reference package。它们可以帮助 provider 和 consumer 对齐格式与消费方式，但不构成唯一官方名单，也不要求外部 provider 与主项目内容完全一致。

### 6. 基本流程

主项目治理的基本流程通常包括：

1. 提交问题、建议、提案或修订请求。
2. 检查材料是否完整，以及是否属于主项目范围。
3. 讨论其与定义、文档、schema 或 reference package 的一致性。
4. 必要时进入更正式的审核或投票流程。
5. 记录结果并公开保留必要历史。

若事项明显不属于主项目范围，例如要求主项目强制接管外部 provider 的所有清单内容，则可以直接说明边界并不纳入本仓库治理。

### 7. 关于状态与首次提案

当前 reference data 使用 `watchlist`、`restricted` 与 `blocked` 三种状态。对于新对象的首次提案，主项目不预设固定起始状态。首次提案可以直接建议进入其中任一状态；最终进入哪个状态，应由现有证据强度、可复核性与社区判断共同决定。

状态越高强度，审核就越应谨慎。首次提案并不当然只能先进入 `watchlist`，但若直接建议 `restricted` 或 `blocked`，则更需要足够强、可复核且与状态强度相匹配的证据基础。

### 8. 外部 provider 与主项目的关系

外部 provider 可以：

- 直接参考主项目 schema 与 release 数据格式
- 参考主项目 governance 文档中的原则
- 选择维护自己的 evidence、proposal 与 registry 内容
- 选择建立自己的审核、投票、申诉与发布流程

主项目欢迎兼容性与格式层协作，但并不要求所有 provider 接受主项目作为唯一治理中心。

### 9. 申诉、复审与修订

主项目中的 reference data、reference 文档与 reference package 都可以被申诉、复审或公开修订。申诉与复审不自动导致状态变化或文档改写，但会为重新判断提供基础。

当事实更正、新证据、格式问题或更好的文档表达出现时，主项目应允许通过公开流程修订 reference implementation。

### 10. 早期项目说明

AntiGEO 仍处于早期阶段。当前 governance 首先服务于主项目自身的规范层与参考实现建设，而不是试图成为所有 provider 的统一裁决中心。随着实践推进，治理细节仍可能继续公开收敛与调整。

---

## English

### 1. Purpose of This Document

This document defines the governance framework for the AntiGEO main project and explains how the main repository publicly maintains its schemas, reference implementation, reference data, and related documentation.

This document primarily governs the main repository itself. External providers may follow this framework, but they may also adopt their own governance practices as long as they remain compatible with AntiGEO data conventions.

### 2. What The Main Project Governs

The current governance scope of the main project mainly includes:

- schemas and structural conventions
- the build / validate toolchain
- the reference registry
- reference evidence / proposal samples
- release-data formats and consumer guidance

The main project is not the sole governance center for every provider. It governs its own reference implementation and sample contents rather than issuing centralized decisions for all registries everywhere.

### 3. Governance Principles

Governance of the AntiGEO main project should follow these principles:

- evidence first
- verifiability
- cautious determination
- transparency and auditability
- consistency
- appeals and re-review
- avoid subjective preference, brand alignment, or competitive abuse wherever possible

For reference data, the community should continue to focus on **systemic pattern**, **scale**, and **verifiability**. For formats, tools, and documentation, the focus should be on clarity, stability, extensibility, and compatibility.

### 4. What May Be Governed

The main project may govern at least the following:

- schema revisions
- release-data format revisions
- build / validate behavior
- updates to the reference registry
- updates to reference evidence / proposal samples
- revisions to definitions, governance, provider-model, and consumer guidance documents
- appeals, re-review, and documentary corrections

### 5. How To Understand Reference Data

The registry data, sample evidence, sample proposals, and build outputs in this repository should all be understood as sample material or a reference package. They help providers and consumers align on format and usage, but they do not create a single official registry and do not require all external providers to match the main repository exactly.

### 6. Basic Process

The basic governance process for the main project usually includes:

1. Submit an issue, proposal, change request, or revision.
2. Check whether the material is complete and within the scope of the main project.
3. Discuss its consistency with the definitions, documentation, schemas, or reference package.
4. Move to more formal review or voting when needed.
5. Record the outcome and preserve the necessary public history.

If a request is plainly outside the scope of the main project, such as asking the main repository to take over all third-party registry content, the project may simply clarify the boundary and decline to govern it here.

### 7. Statuses and Initial Proposals

The current reference data uses `watchlist`, `restricted`, and `blocked`. For a first proposal involving a new entity, the main project does not assume a fixed entry status. An initial proposal may recommend any of those statuses, and the appropriate outcome should be determined by the available evidence, its verifiability, and community judgment.

The more severe the proposed status, the more cautious the review should be. An initial proposal is therefore not required to begin at `watchlist`, but a proposal that directly seeks `restricted` or `blocked` should rest on evidence that is strong enough, verifiable enough, and proportionate to the severity of the status.

### 8. Relationship Between External Providers and The Main Project

External providers may:

- adopt the project's schemas and release-data formats directly
- use the project's governance documents as guidance
- maintain their own evidence, proposal, and registry contents
- define their own review, voting, appeal, and publication processes

The main project welcomes compatibility and format-level collaboration, but it does not require every provider to accept the main repository as the single governance authority.

### 9. Appeals, Re-Review, and Revisions

Reference data, reference documentation, and the reference package in the main project may all be appealed, re-reviewed, or revised publicly. Appeals and re-review do not automatically change a status or rewrite a document, but they create a basis for reassessment.

Where factual corrections, new evidence, format issues, or better documentation become available, the project should allow the reference implementation to be revised through a public process.

### 10. Early-Stage Project Note

AntiGEO is still early-stage. Its current governance is primarily intended to support the project's specification layer and reference implementation rather than to serve as a universal decision center for every provider. As practice evolves, governance details may continue to be refined publicly.

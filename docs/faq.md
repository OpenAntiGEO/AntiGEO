# FAQ

[中文](#中文) | [English](#english)

---

## 中文

### 1. AntiGEO 是什么？

AntiGEO 是一个开源、可审计、社区治理的 GEO 风险清单规范与参考实现项目。它提供 schema、索引格式、build / validate 工具、参考样例数据，以及 consumer 如何消费这些数据的最小模型。

### 2. AntiGEO 是否维护唯一名单？

不是。AntiGEO 主项目当前不追求维护唯一、中心化、全局权威的名单。具体风险清单可以由不同 provider 独立发布，只要它们遵守兼容的数据格式和消费约定。

### 3. 为什么允许多个 provider？

因为 GEO 风险判断本身可能依赖不同的数据来源、审核节奏、治理偏好和部署场景。允许多个 provider，可以让 consumer 与用户自行选择更适合自己的数据源，而不强制绑定单一中心仓库。

### 4. 主项目中的数据是不是官方最终裁决？

不是。当前仓库中的 registry、sample evidence、sample proposals 和 release 导出，都应理解为 reference implementation / reference package 的一部分。它们用于说明格式、工具链和消费模型，不应被理解为唯一官方最终裁决。

### 5. provider 和 consumer 分别是什么？

provider 是按 AntiGEO 规范发布数据包的开发者、团队或社区维护数据源。consumer 是加载这些数据包并在搜索、检索、代理、RAG 或其它系统中使用它们的工具、插件或服务。

### 5.1 provider 是否必须提供 evidence？

不必须。evidence 是当前的可选治理扩展，而不是所有 provider 的强制要求。provider 可以提供 evidence 来提升可解释性、可复核性和信任度，但 consumer 不应假设所有 provider 都会带 evidence。

### 6. 用户为什么要自己选择信任源？

因为不同 provider 可能维护不同覆盖范围、不同审查标准和不同更新频率。把选择权留给用户或 consumer，可以减少单点判断的风险，也更符合 AntiGEO 当前作为规范层和 reference implementation 的定位。

### 6.1 AntiGEO 是否强制统一投票机制？

不强制。投票、申诉和治理流程当前更适合作为参考治理模块或 optional extension。provider 可以采用社区投票、维护者决定、审核流程或其它治理方式；主项目不要求所有 provider 必须使用统一正式投票机制。

### 7. 为什么用户本地规则优先？

因为最终控制权应保留给用户或 consumer，而不是被外部 provider 或主项目直接夺走。当前建议的优先级是：用户本地白名单、用户本地 blocklist、用户本地 override，高于外部 provider 数据。

### 8. 如果我只想用 AntiGEO 主项目的数据，可以吗？

可以。当前主项目可以被视为一个 reference provider / reference package。你可以只使用主项目导出的 release 数据，也可以同时订阅其它 provider，再由本地规则决定最终覆盖关系。

### 9. provider 是否必须把自己的清单提交到主项目？

不必须。开发者、团队或社区完全可以基于 AntiGEO 的 schema、索引格式和消费模型维护独立 provider 仓库或独立数据源。主项目欢迎规范、工具、样例和文档贡献，但不要求所有清单内容都汇总到主项目。

### 10. 当前 release 数据是用来做什么的？

当前 release 数据主要用于支持两个阶段：

- 搜索前初筛：通过 topic / intent 索引缩小候选 entity 范围
- 搜索后治理：通过 domain / name 索引命中 entity，再结合 compact entity 的状态与风险字段做处理

### 11. evidence 和 proposal 目前处于什么状态？

当前主项目已经提供 evidence / proposal 的 schema 与参考样例数据，但它们目前更多处于治理与审查层样例状态。当前 build / validate 主链路仍主要围绕 entity registry 与 release 数据层。

不同 provider 因此也可以有不同治理深度：有些只提供核心 package；有些会额外提供 evidence、proposal、appeals 或 voting 记录。

### 12. AntiGEO 是否会替代法律、监管或平台结论？

不会。AntiGEO 记录的是风险状态、数据结构与治理模型，不是法律、监管或平台执法结论的替代品。

进一步阅读：

- [README.md](../README.md)
- [docs/quick-start.md](./quick-start.md)
- [docs/release-data.md](./release-data.md)
- [docs/provider-model.md](./provider-model.md)
- [docs/definition.md](./definition.md)
- [docs/governance.md](./governance.md)
- [CONTRIBUTING.md](../CONTRIBUTING.md)

本 FAQ 会随着项目结构和 provider 模式的演进继续公开更新。

---

## English

### 1. What is AntiGEO?

AntiGEO is an open, auditable, community-governed GEO risk registry specification and reference implementation project. It provides schemas, index formats, build / validate tooling, sample reference data, and a minimal consumption model for downstream consumers.

### 2. Does AntiGEO maintain a single authoritative registry?

No. The main project does not currently aim to maintain a single centralized or globally authoritative registry. Concrete risk registries may be published independently by different providers as long as they follow compatible data formats and consumption conventions.

### 3. Why allow multiple providers?

Because GEO risk assessment may depend on different data sources, review cadence, governance preferences, and deployment contexts. Allowing multiple providers lets consumers and users choose the sources that fit their needs rather than forcing everything through one central repository.

### 4. Is the data in the main project an official final ruling?

No. The current registry data, sample evidence, sample proposals, and release exports in this repository should be understood as part of a reference implementation / reference package. They illustrate format, tooling, and consumption behavior rather than serving as a single official final ruling.

### 5. What are providers and consumers?

A provider is a developer, team, or community-maintained data source that publishes AntiGEO-compatible packages. A consumer is any tool, plugin, service, or local system that loads those packages and uses them in search, retrieval, proxying, RAG, or similar workflows.

### 5.1 Must a provider publish evidence?

No. Evidence is currently an optional governance extension rather than a mandatory requirement for every provider. A provider may publish evidence to improve explainability, verifiability, and trust, but consumers should not assume that every provider will include evidence.

### 6. Why should users choose which sources to trust?

Because different providers may maintain different coverage, review standards, and update cadence. Leaving that choice with the user or consumer reduces single-source risk and is more consistent with AntiGEO's current role as a specification layer and reference implementation.

### 6.1 Does AntiGEO require one unified voting mechanism?

No. Voting, appeals, and governance workflows are better treated today as reference governance modules or optional extensions. Providers may use community voting, maintainer decisions, review workflows, or other governance methods; the main project does not require every provider to adopt one formal voting mechanism.

### 7. Why do local rules take priority?

Because final control should remain with the user or consumer rather than being imposed directly by a provider or by the main project. The current recommended priority is: local allowlist, local blocklist, local override, then external provider data.

### 8. Can I use only the main project's data?

Yes. The main repository can be treated as a reference provider / reference package. You may use only the main project's release outputs, or combine them with third-party providers and let local rules determine the final override behavior.

### 9. Must providers submit their registries back to the main project?

No. Developers, teams, and communities can maintain independent provider repositories or data sources using AntiGEO schemas, index formats, and consumption conventions. The main project welcomes contributions to standards, tooling, documentation, and sample data, but it does not require all registry content to be centralized here.

### 10. What is the current release data for?

The current release data mainly supports two stages:

- pre-search filtering, using topic / intent indexes to narrow candidate entities
- post-search governance, using domain / name indexes to match entities and then applying status and risk fields from compact entities

### 11. What is the current role of evidence and proposal data?

The main project already provides schemas and sample data for evidence and proposals, but they are still primarily sample material for governance and review. The current build / validate workflow is still centered on the entity registry and release-data layer.

Different providers can therefore also choose different governance depth: some may publish only the core package, while others may additionally publish evidence, proposals, appeals, or voting records.

### 12. Does AntiGEO replace legal, regulatory, or platform conclusions?

No. AntiGEO records risk status, data structures, and governance models. It is not a substitute for legal, regulatory, or platform enforcement conclusions.

Further reading:

- [README.md](../README.md)
- [docs/quick-start.md](./quick-start.md)
- [docs/release-data.md](./release-data.md)
- [docs/provider-model.md](./provider-model.md)
- [docs/definition.md](./definition.md)
- [docs/governance.md](./governance.md)
- [CONTRIBUTING.md](../CONTRIBUTING.md)

This FAQ will continue to evolve publicly as the project structure and provider model mature.

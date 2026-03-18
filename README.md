# AntiGEO

[中文](#中文) | [English](#english)

---

## 中文

AntiGEO 是一个开源、可审计、社区治理的 GEO 风险清单规范与参考实现项目。主项目当前重点提供数据结构规范、索引与 release 数据格式、校验与构建工具、参考样例数据，以及面向 consumer 的消费模型与覆盖优先级建议。

AntiGEO 主项目并不追求维护唯一、中心化、全局权威的名单。具体风险清单可以由不同 provider 独立发布；consumer 与用户可以自行选择信任并订阅哪些 provider；用户本地白名单、本地 blocklist 和本地 override 的优先级应高于外部 provider 数据。

## 主项目提供什么

- `schemas/`：entity、evidence、proposal 等数据结构规范。
- `scripts/`：当前的构建与校验工具，用于生成和检查 reference package。
- `registry/`：当前 reference package 的 entity 样例与 release 导出。
- `evidence/` 与 `proposals/`：与 entity 关联的参考样例数据。
- `docs/`：定义、治理、provider 模式、release 数据格式和消费建议。

当前仓库中的 registry、sample evidence、sample proposals 以及 build 生成的导出文件，都应理解为 reference implementation / reference package，而不是唯一官方裁决结果。

## Provider 模式

在 AntiGEO 里，provider 指的是按 AntiGEO 规范发布数据包的开发者、团队或社区维护数据源。不同 provider 可以共享同一套 schema、索引格式和消费模型，但维护各自的数据内容、审核节奏和治理实践。

这意味着 consumer 面向的是“符合 AntiGEO 格式的数据源”，而不是必须依赖主项目自身仓库。主项目当前可以被视为一个 reference provider / reference package，但并不垄断具体清单内容。

## 用户控制优先级

AntiGEO 关心的是可互操作的数据格式与消费模型，不替用户夺走最终控制权。当前推荐的优先级思想是：

1. 用户本地白名单
2. 用户本地 blocklist
3. 用户本地 override
4. 外部 provider 数据

主项目和 provider 都只是输入源；最终采用哪份数据、如何合并、如何覆盖，应由 consumer 或终端用户决定。

## 当前仓库内容

```text
AntiGEO/
├── docs/        项目说明、定义、治理、provider 模式、release 数据说明
├── schemas/     entity、evidence、proposal 等数据结构规范
├── registry/    reference registry 与 release 导出
├── evidence/    reference evidence 样例
├── proposals/   reference proposal 样例
└── scripts/     构建与校验工具
```

当前已经建立的主干包括：

- entity / evidence / proposal 的基础 schema
- reference entity registry 与 compact/index/release 导出
- 基础 build / validate 链路
- 搜索前初筛与搜索后治理的最小消费模型

其中 evidence / proposal 当前仍主要处于治理与审查层的参考样例状态；build / validate 目前主要围绕 entity registry 与 release 数据层。

## 从哪里开始

- [快速开始](./docs/quick-start.md)
- [Release 数据说明](./docs/release-data.md)
- [Provider 模式](./docs/provider-model.md)
- [定义说明](./docs/definition.md)
- [治理规则](./docs/governance.md)
- [证据政策](./docs/evidence-policy.md)
- [投票规则](./docs/voting.md)
- [申诉说明](./docs/appeals.md)
- [常见问题](./docs/faq.md)
- [贡献指南](./CONTRIBUTING.md)

## 项目状态

AntiGEO 仍处于早期阶段，但主干框架已经建立。当前主项目更像一个规范层、参考实现和参考数据包，而不是单一中心化名单服务。随着后续实践，schema、reference package、provider model 文档和消费建议都可能继续公开收敛与完善。

## 许可与协作

许可证与贡献方式请分别参见 [LICENSE](./LICENSE) 和 [CONTRIBUTING.md](./CONTRIBUTING.md)。如需理解当前 release 导出与 provider 关系，建议优先阅读 [docs/release-data.md](./docs/release-data.md) 与 [docs/provider-model.md](./docs/provider-model.md)。

---

## English

AntiGEO is an open, auditable, community-governed GEO risk registry specification and reference implementation project. The main repository currently focuses on data schemas, index and release data formats, validation and build tools, sample reference data, and consumption guidance for downstream consumers.

The main project does not aim to maintain a single centralized or globally authoritative list. Concrete risk registries may be published by different providers; consumers and users may choose which providers to trust and subscribe to; and local user allowlists, local blocklists, and local overrides should take precedence over external provider data.

## What The Main Project Provides

- `schemas/`: structural specifications for entities, evidence, proposals, and related records.
- `scripts/`: the current build and validation tools used to produce and check a reference package.
- `registry/`: the current reference entity package and release exports.
- `evidence/` and `proposals/`: sample reference data linked to the entity layer.
- `docs/`: definitions, governance, provider model, release data format, and consumption guidance.

The registry data, sample evidence, sample proposals, and build outputs in this repository should be understood as a reference implementation / reference package rather than as a single official final record.

## Provider Model

Within AntiGEO, a provider is a developer, team, or community-maintained data source that publishes packages in AntiGEO-compatible formats. Different providers may share the same schemas, index formats, and consumption model while maintaining their own record contents, review cadence, and governance practices.

That means consumers are designed to work with any AntiGEO-compatible data source, not only with the main repository. The main repository can currently be treated as a reference provider / reference package, but it does not monopolize registry content.

## User Control Priority

AntiGEO is designed around interoperable formats and consumer control, not around taking final control away from the user. The current recommended priority model is:

1. local user allowlist
2. local user blocklist
3. local user override
4. external provider data

Both the main project and third-party providers are input sources. The final decision about what to load, merge, trust, or override should remain with the consumer or end user.

## Repository Contents

```text
AntiGEO/
├── docs/        project documents, definitions, governance, provider model, release data
├── schemas/     schemas for entities, evidence, proposals, and related records
├── registry/    reference registry and release exports
├── evidence/    reference evidence samples
├── proposals/   reference proposal samples
└── scripts/     build and validation tools
```

The current backbone already includes:

- foundational schemas for entity / evidence / proposal
- a reference entity registry plus compact, indexed, and release-style exports
- a basic build / validate workflow
- a minimal two-stage consumption model for pre-search filtering and post-search governance

At the moment, evidence and proposal data are still primarily sample material for governance and review. The build / validate workflow is currently centered on the entity registry and release-data layer.

## Where To Start

- [Quick Start](./docs/quick-start.md)
- [Release Data](./docs/release-data.md)
- [Provider Model](./docs/provider-model.md)
- [Definitions](./docs/definition.md)
- [Governance](./docs/governance.md)
- [Evidence Policy](./docs/evidence-policy.md)
- [Voting](./docs/voting.md)
- [Appeals](./docs/appeals.md)
- [FAQ](./docs/faq.md)
- [Contributing](./CONTRIBUTING.md)

## Project Status

AntiGEO is still early-stage, but the main structural backbone is now in place. At this stage, the project should be read primarily as a specification layer, reference implementation, and reference package rather than as a single centralized registry service. Schemas, reference package structure, provider-model documentation, and consumption guidance may continue to evolve publicly over time.

## License and Collaboration

For licensing and contribution guidance, see [LICENSE](./LICENSE) and [CONTRIBUTING.md](./CONTRIBUTING.md). For the current relationship between release outputs and providers, start with [docs/release-data.md](./docs/release-data.md) and [docs/provider-model.md](./docs/provider-model.md).

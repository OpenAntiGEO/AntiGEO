# AntiGEO

[中文](#中文) | [English](#english)

---

OpenAntiGEO / AntiGEO

## 中文

AntiGEO 是由 **OpenAntiGEO** 维护的开源、可审计、社区治理的 **GEO 操纵风险注册表**。它用于帮助 AI 搜索、检索增强系统、答案引擎与 Agent 识别可能存在系统性操纵风险的品牌、域名、内容网络与相关实体。

本仓库主项目仅维护规则、名单、证据、提案、投票与申诉，不承载面向终端用户的插件或 SDK 实现。

## 项目范围

本仓库当前包含以下内容：

- 规则与定义
- 风险名单与注册表
- 可复核证据
- 社区提案
- 投票记录
- 申诉材料与处理规则

以下内容不在本仓库内实现，均应作为独立子项目维护：

- 浏览器插件
- 搜索插件 / 搜索适配器
- OpenClaw 插件
- SDK

## 状态定义

仓库当前只使用三种状态：

- `watchlist`：已有一定证据，说明对象存在 GEO 操纵嫌疑，需要继续观察。
- `restricted`：证据较充分，说明对象存在较明显的系统性操纵风险，建议下游系统降权、弱化或显著标记。
- `blocked`：证据强且相对明确，说明对象属于高风险 GEO 操纵源，建议下游系统默认忽略，除非用户本地豁免。

## 治理流程

项目采用基于证据的社区治理流程：

1. 提交可复核证据。
2. 社区审核证据是否真实、是否符合定义。
3. 通过投票决定进入何种状态。

## 仓库结构

```text
AntiGEO/
├── docs/        项目说明、定义、治理、投票、申诉等文档
├── schemas/     注册表、证据、提案等数据结构定义
├── registry/    状态名单与聚合索引
├── proposals/   社区提案
├── evidence/    证据材料
└── scripts/     辅助脚本
```

当前目录用途说明：

- `docs/`：存放定义、治理、证据政策、投票与申诉等说明文档。
- `schemas/`：存放实体、证据、提案等 JSON Schema。
- `registry/`：存放 `watchlist`、`restricted`、`blocked` 及聚合索引。
- `proposals/`：存放待审议或历史提案。
- `evidence/`：存放支撑提案与状态判断的证据材料。
- `scripts/`：存放校验、整理、生成等辅助脚本。

## 项目状态

本项目仍处于**早期初始化阶段**。当前仓库以基础规则、数据结构、注册表约定和治理流程搭建为主；目录、格式与流程在保持可审计性的前提下，仍可能继续收敛和调整。

## 相关文档

- [定义说明](./docs/definition.md)
- [治理规则](./docs/governance.md)
- [证据政策](./docs/evidence-policy.md)
- [投票机制](./docs/voting.md)
- [申诉说明](./docs/appeals.md)
- [常见问题](./docs/faq.md)

## 许可与协作

许可证与贡献流程请分别参见 [LICENSE](./LICENSE) 和 [CONTRIBUTING.md](./CONTRIBUTING.md)。治理相关细则以 `docs/` 目录下正式文档为准。

---

## English

AntiGEO is an open, auditable, community-governed **GEO manipulation risk registry** maintained by **OpenAntiGEO**. It helps AI search, retrieval-augmented systems, answer engines, and agents identify brands, domains, content networks, and related entities that may present systematic manipulation risk.

The main repository is limited to rules, registries, evidence, proposals, voting, and appeals. It does not host end-user extensions or SDK implementations.

## Scope

The main repository is limited to the following:

- Rules and definitions
- Risk registries
- Reviewable evidence
- Community proposals
- Voting records
- Appeals materials and procedures

The following are not implemented in this repository and should be maintained as separate subprojects:

- Browser extension
- Search plugins
- OpenClaw plugin
- SDKs

## Status Definitions

This repository uses only three statuses:

- `watchlist`: there is some evidence indicating possible GEO manipulation risk and the subject requires continued observation.
- `restricted`: the evidence is relatively substantial and indicates a clearer pattern of systematic manipulation risk; downstream systems are advised to downrank, de-emphasize, or clearly label the subject.
- `blocked`: the evidence is strong and comparatively clear; the subject is considered a high-risk GEO manipulation source, and downstream systems are advised to ignore it by default unless a local user override applies.

## Governance Process

The project follows an evidence-based community governance process:

1. Submit reviewable evidence.
2. The community reviews whether the evidence is authentic and whether it meets the project definitions.
3. A vote determines which status, if any, should be assigned.

## Repository Structure

```text
AntiGEO/
├── docs/        Project documents, definitions, governance, voting, appeals
├── schemas/     Data schemas for registries, evidence, and proposals
├── registry/    Status lists and aggregate indexes
├── proposals/   Community proposals
├── evidence/    Evidence materials
└── scripts/     Supporting scripts
```

Directory overview:

- `docs/`: definitions, governance, evidence policy, voting, appeals, and related documentation.
- `schemas/`: JSON Schema files for entities, evidence, proposals, and related data.
- `registry/`: `watchlist`, `restricted`, `blocked`, and aggregate indexes.
- `proposals/`: pending and historical proposals.
- `evidence/`: evidence supporting proposals and status decisions.
- `scripts/`: helper scripts for validation, processing, and generation.

## Project Status

This project is still in the **early initialization stage**. At this stage, the repository is focused on establishing baseline rules, data structures, registry conventions, and governance procedures. Directory layout, formats, and process details may continue to evolve while preserving auditability.

## Documents

- [Definitions](./docs/definition.md)
- [Governance](./docs/governance.md)
- [Evidence Policy](./docs/evidence-policy.md)
- [Voting](./docs/voting.md)
- [Appeals](./docs/appeals.md)
- [FAQ](./docs/faq.md)

## License and Collaboration

For licensing and contribution procedures, see [LICENSE](./LICENSE) and [CONTRIBUTING.md](./CONTRIBUTING.md). Governance-related rules are defined by the formal documents under `docs/`.

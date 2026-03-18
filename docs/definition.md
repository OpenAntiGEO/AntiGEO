# Definition / 定义

[中文](#中文) | [English](#english)

---

## 中文

### 1. 文档目的

本文件用于定义 AntiGEO 的核心术语、适用范围、边界与判断基础。它同时说明 AntiGEO 当前关注的是风险清单的数据与治理模型，而不是由主项目垄断具体清单内容。

本文件中的核心定义适用于 AntiGEO 风险清单模型本身；至于具体治理流程、证据透明度、申诉深度与投票方式，则可以因 provider 而异。

### 2. 什么是 GEO manipulation risk

在 AntiGEO 语境下，**GEO 操纵风险**是指某一对象通过可规模化、可复制、可组织化的方法，影响 AI 搜索、AI 摘要、答案引擎、检索增强系统、智能体或类似下游系统的来源选择、排序、曝光或呈现，从而造成失真曝光、品牌偏置、竞争压制或用户误导的风险。

AntiGEO 特别关注三个核心维度：**系统性**、**规模化**、**可复核**。项目关注的是系统性风险模式，而不是单篇低质量页面、偶发异常结果或一般性的内容优化行为本身。

### 3. AntiGEO 当前定义的对象

AntiGEO 当前使用的核心对象包括但不限于：

- entity
- evidence
- proposal
- release data / provider package

这些对象共同构成一个可被 provider 发布、被 consumer 消费的风险清单数据模型。主项目当前提供 schema、reference data 和 reference package，但不要求所有具体清单内容都由主项目维护。

### 4. AntiGEO 关注的对象类型

被记录的 entity 可以包括但不限于：

- 品牌
- 公司或组织
- 域名
- 内容网络
- 站群
- 代理发布网络
- 其它可识别的相关实体

对象是否进入清单，不取决于类别本身，而取决于是否存在与 GEO manipulation risk 相关的可复核证据。

### 5. 常见风险行为

AntiGEO 当前关注的模式可以包括但不限于：

- 伪媒体网络
- 伪评测网络
- 伪专家背书
- 批量化模板内容投放
- 为 AI 检索或答案系统专门构造的大规模操纵型页面
- 多站点重复或轻改写内容网络
- 以影响 AI 回答为目标的结构化品牌植入
- 其它可复核的系统性操纵模式

这些示例仅用于说明常见模式，本身不自动构成纳入清单的充分理由。

### 6. AntiGEO 不关注什么

以下内容通常不在 AntiGEO 当前关注范围内，除非另有证据显示其已形成可复核的系统性操纵模式：

- 正常官网内容
- 正常 SEO
- 合法 PR
- 明确标注的广告
- 普通用户评价
- 单篇低质量文章但未形成系统性操纵
- 单纯质量差但无证据显示存在组织化操纵的内容

AntiGEO 不把一般性的内容质量问题或正常品牌建设活动直接等同于 GEO manipulation risk。

### 7. 风险认定原则

在审核、投票、申诉与复审时，应遵循以下原则：

- 证据优先
- 可复核
- 谨慎认定
- 重视系统性和重复性
- 避免仅凭主观印象或品牌偏好判断
- 允许申诉与复审

缺乏足够证据时，不应作出过强结论。

### 8. 与 provider 模式的关系

AntiGEO 当前定义的是一套风险清单的数据与治理模型。主项目可以提供参考数据，但不垄断具体清单内容。任何 provider 只要遵守相同的定义框架、schema 和 release 数据格式，都可以发布自己的数据源。

在这一前提下，不同 provider 可以选择不同治理深度。有些 provider 可能公开 evidence、proposal、appeals 或 voting 记录；有些 provider 只提供核心 package。

因此，consumer 使用的是 AntiGEO 兼容格式，而不是必须依附主项目仓库本身。主项目当前更接近 reference implementation / reference provider，而不是唯一来源。

### 9. 与状态模型的关系

当前状态模型仍使用 `watchlist`、`restricted` 与 `blocked`。定义文档负责回答“什么属于 AntiGEO 关注的风险”；具体状态回答“现有证据支持达到何种风险级别”。

是否采用某个 provider 的状态、如何与本地规则合并、是否覆盖，都应由 consumer 或终端用户决定。

### 10. 非目标

AntiGEO 当前不以以下事项为目标：

- 不对产品优劣作价值判断
- 不裁定单条内容真伪
- 不替代法律或监管结论
- 不输出统一、唯一、强制性的全局名单
- 不直接规定所有下游工具必须采用何种执行策略

本定义文档会随着项目公开演进继续修订。

---

## English

### 1. Purpose of This Document

This document defines the core terms, scope, boundaries, and interpretive basis of AntiGEO. It also clarifies that AntiGEO is currently focused on a risk-registry data and governance model rather than on monopolizing concrete registry content through the main repository.

The core definitions in this document apply to the AntiGEO risk-registry model itself. Specific governance flow, evidence transparency, appeal depth, or voting style may still vary from one provider to another.

### 2. What GEO Manipulation Risk Means

Within AntiGEO, **GEO manipulation risk** refers to the risk that an entity uses scalable, repeatable, or organized methods to influence source selection, ranking, exposure, or presentation in AI search, AI summaries, answer engines, retrieval-augmented systems, agents, or similar downstream systems, in ways that may produce distorted exposure, brand bias, competitive suppression, or user misdirection.

AntiGEO pays particular attention to three dimensions: **systemic pattern**, **scale**, and **verifiability**. The project is concerned with systemic risk patterns rather than with a single low-quality page, an isolated abnormal result, or ordinary content optimization by itself.

### 3. Objects Defined by AntiGEO

The current AntiGEO model includes, at minimum:

- entities
- evidence
- proposals
- release data / provider packages

Together these form a risk-registry data model that may be published by providers and consumed by downstream systems. The main repository currently provides schemas, reference data, and a reference package, but it does not require all concrete registry content to be maintained centrally here.

### 4. Types of Objects Within Scope

Recorded entities may include, but are not limited to:

- brands
- companies or organizations
- domains
- content networks
- site clusters
- proxy publishing networks
- other identifiable related entities

Whether something enters a registry depends not on category alone, but on whether there is verifiable evidence relevant to GEO manipulation risk.

### 5. Common Risk Behaviors

Patterns of concern may include, for example:

- pseudo-media networks
- pseudo-review networks
- false or manufactured expert endorsement
- large-scale templated content deployment
- large-scale manipulative pages built specifically for AI retrieval or answer systems
- multi-site duplicate or lightly rewritten content networks
- structured brand insertion intended to influence AI-generated answers
- other verifiable patterns of systemic manipulation

These examples are illustrative only and do not, by themselves, provide a sufficient basis for inclusion in a registry.

### 6. What AntiGEO Is Not Focused On

The following are generally outside AntiGEO's current concern unless additional evidence shows a verifiable systemic pattern:

- normal official website content
- ordinary SEO
- legitimate PR
- clearly disclosed advertising
- ordinary user reviews
- a single low-quality article without systemic manipulation
- content that is poor in quality but unsupported by evidence of organized manipulation

AntiGEO does not treat ordinary quality problems or normal brand-building activity as GEO manipulation risk by default.

### 7. Principles for Risk Determination

Review, voting, appeals, and re-review should follow these principles:

- evidence first
- verifiability
- cautious determination
- attention to systemic and repeated patterns
- avoid judgments based only on subjective impressions or brand preference
- allow appeals and re-review

Where evidence is insufficient, the project should avoid strong conclusions.

### 8. Relationship to the Provider Model

AntiGEO currently defines a risk-registry data and governance model. The main project may provide reference data, but it does not monopolize concrete registry content. Any provider that follows the same definition framework, schemas, and release-data conventions may publish its own data source.

Under that model, providers may choose different governance depth. Some may publish evidence, proposals, appeals, or voting records openly, while others may publish only the core package.

That means consumers use AntiGEO-compatible formats rather than depending on the main repository itself. The main project is better understood today as a reference implementation / reference provider than as the only source of truth.

### 9. Relationship to the Status Model

The current status model still uses `watchlist`, `restricted`, and `blocked`. This definition document answers what kinds of risk fall within AntiGEO's scope; the status process answers what level of risk is supported by the available record.

Whether to adopt a provider's status, how to merge it with local rules, and whether to override it should remain decisions for the consumer or end user.

### 10. Non-Goals

AntiGEO does not currently aim to do the following:

- make value judgments about product quality or merit
- determine the truth or falsity of a single item of content
- replace legal or regulatory conclusions
- produce a single mandatory global registry
- directly require all downstream systems to use one enforcement strategy

This definition document may continue to evolve through the project's public process.

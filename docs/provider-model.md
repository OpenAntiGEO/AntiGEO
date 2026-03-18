# Provider Model / Provider 模式

[中文](#中文) | [English](#english)

---

## 中文

### 1. 文档目的

本文件用于说明 AntiGEO 当前的 provider 模式：provider 是什么、provider 发布什么、consumer 如何使用 provider 数据，以及用户本地规则与 provider 数据之间的优先级关系。

### 2. 什么是 provider

在 AntiGEO 语境下，provider 是按 AntiGEO 兼容格式发布数据包的开发者、团队、社区维护数据源或其它发布主体。

provider 的核心职责不是实现某一种固定产品，而是提供一组可以被 consumer 加载、校验和消费的数据文件，例如：

- entity registry
- compact entity 集合
- topic / intent / risk / domain / name 索引
- manifest
- 与治理相关的 evidence / proposal 记录或参考材料

### 3. provider 发布什么

当前最小 provider package 可以围绕以下内容构建：

- 与 AntiGEO schema 兼容的 entity 数据
- 与当前 release 数据格式兼容的导出文件
- 可被 build / validate 工具检查的数据结构

主项目当前仓库中的 `registry/` 导出文件，就是一个 reference package 的例子。其它 provider 可以发布不同内容，但最好保持格式兼容，以便 consumer 复用相同的加载逻辑。

### 4. provider 与主项目的关系

主项目当前重点提供：

- schema
- release 数据格式
- build / validate 工具
- reference 样例数据
- consumption guidance

因此，主项目与 provider 的关系更接近“规范层与参考实现”对“具体数据源”的关系。主项目可以被视为一个 reference provider / reference package，但不是所有 provider 的唯一上级或唯一内容中心。

### 5. consumer 如何使用 provider

consumer 通常不需要关心 provider 的内部治理细节，而更关心以下问题：

- 这个 provider 是否输出 AntiGEO 兼容格式
- 是否包含 `manifest.json`
- 是否提供 compact entities 和所需索引
- 是否满足自己的更新频率、覆盖范围与审计要求

只要格式兼容，consumer 就可以在同一套加载逻辑下订阅一个或多个 provider。

### 6. 多 provider 订阅

AntiGEO 当前允许 consumer 同时订阅多个 provider。这样做的原因包括：

- 不同 provider 可能覆盖不同领域
- 不同 provider 可能有不同治理风格
- 不同用户可能信任不同数据源
- 单一来源不应成为唯一强制入口

主项目不要求 provider 之间内容一致，也不要求所有 provider 必须回流到主项目仓库统一维护。

### 7. 用户本地规则优先级

当前建议的优先级思想是：

1. 用户本地白名单
2. 用户本地 blocklist
3. 用户本地 override
4. 外部 provider 数据

这意味着 provider 数据只是输入源之一。最终决定是否采纳、如何覆盖、如何冲突合并，应由 consumer 或终端用户控制。

### 8. 为什么当前仓库可以视为 reference provider

当前仓库之所以可以被视为 reference provider / reference package，是因为它已经提供了：

- entity / evidence / proposal 的基础 schema
- reference registry 数据
- compact entities 与多类索引导出
- manifest
- build / validate 工具
- Quick Start、Release Data 和消费模型说明

但这并不意味着当前仓库维护的是唯一权威名单。它更像一份公开、可审计、可复用的参考包。

### 9. 给 provider 开发者的建议

- 尽量复用主项目的 schema 与 release 数据格式。
- 尽量提供 `manifest.json` 作为 package 入口。
- 尽量保持 compact entities 与索引结构稳定。
- 尽量明确自己的治理范围、审核方法和更新节奏。
- 不要假设 consumer 只会订阅你这一家 provider。

### 10. 给 consumer 的建议

- 优先根据 `manifest.json` 发现 provider package 内容。
- 优先加载 `entities.compact.json` 与必要索引，而不是每次都扫描 `full-index.json`。
- 将 provider 数据视为输入源，再结合本地规则决定最终行为。
- 明确记录本地白名单、blocklist 与 override 的覆盖顺序。

本文件会随着 AntiGEO provider 模式和 reference package 的演进继续公开更新。

---

## English

### 1. Purpose

This document explains the current AntiGEO provider model: what a provider is, what a provider publishes, how consumers use provider data, and how local user rules relate to provider data in the final priority model.

### 2. What A Provider Is

Within AntiGEO, a provider is a developer, team, community-maintained data source, or other publishing party that releases AntiGEO-compatible data packages.

The core role of a provider is not to implement one particular product, but to publish a set of data files that consumers can load, validate, and use, such as:

- an entity registry
- a compact entity collection
- topic / intent / risk / domain / name indexes
- a manifest
- evidence / proposal records or reference materials related to governance

### 3. What A Provider Publishes

The current minimal provider package can be built around:

- entity data compatible with AntiGEO schemas
- exported files compatible with the current release-data format
- structures that can be checked by build / validate tooling

The exported files under `registry/` in the main repository are one example of a reference package. Other providers may publish different content, but compatibility is useful because it allows consumers to reuse the same loading logic.

### 4. Relationship Between Providers and The Main Project

The main project currently focuses on:

- schemas
- release-data formats
- build / validate tools
- reference sample data
- consumption guidance

That means the relationship between the main repository and providers is best understood as the relationship between a specification layer / reference implementation and concrete data sources. The main project may be treated as a reference provider / reference package, but it is not the sole parent or sole content center for every provider.

### 5. How Consumers Use Providers

Consumers usually do not need to depend on a provider's internal governance details. Instead, the key questions are:

- does this provider publish AntiGEO-compatible formats?
- does it include `manifest.json`?
- does it provide compact entities and the required indexes?
- does it satisfy the consumer's needs for update cadence, coverage, and auditability?

As long as the format is compatible, a consumer can subscribe to one or many providers using the same loading model.

### 6. Multi-Provider Subscription

AntiGEO currently allows consumers to subscribe to multiple providers at the same time. Reasons include:

- different providers may cover different domains
- different providers may use different governance styles
- different users may trust different data sources
- no single source should become the only mandatory entry point

The main project does not require providers to keep identical content, and it does not require every provider to feed all of its data back into the main repository.

### 7. Local User Priority

The current recommended priority model is:

1. local user allowlist
2. local user blocklist
3. local user override
4. external provider data

This means provider data is only one input source. The final decision about adoption, conflict resolution, and override behavior should remain with the consumer or end user.

### 8. Why The Current Repository Can Be Viewed As A Reference Provider

The current repository can be viewed as a reference provider / reference package because it already provides:

- foundational schemas for entity / evidence / proposal
- reference registry data
- compact entities and multiple index exports
- a manifest
- build / validate tooling
- Quick Start, Release Data, and consumption guidance documents

But that does not mean the repository maintains the only authoritative registry. It is better understood as an open, auditable, reusable reference package.

### 9. Guidance For Provider Authors

- Reuse the project's schemas and release-data formats where possible.
- Provide `manifest.json` as the package entry point where possible.
- Keep compact entities and index structures stable where possible.
- Be explicit about your own governance scope, review method, and publication cadence.
- Do not assume consumers will subscribe to only one provider.

### 10. Guidance For Consumers

- Use `manifest.json` first to discover provider package contents.
- Prefer `entities.compact.json` and the necessary indexes over scanning `full-index.json` on every request.
- Treat provider data as an input source, then combine it with local rules to determine final behavior.
- Make the precedence of local allowlists, blocklists, and overrides explicit in your implementation.

This document will continue to evolve publicly as the AntiGEO provider model and reference package mature.

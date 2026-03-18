# FAQ

[中文](#中文) | [English](#english)

---

## 中文

### 1. AntiGEO 是什么？

AntiGEO 是一个开源、可审计、社区治理的 GEO 操纵风险清单，用于记录可能存在系统性操纵风险的对象及其证据基础。

### 2. AntiGEO 不是什么？

AntiGEO 不是品牌攻击工具，不是产品优劣排行榜，不是单篇内容真假裁定器，也不是法律或监管结论的替代品。

### 3. 为什么需要 AntiGEO？

AI 搜索、摘要和答案系统可能受到系统性操纵影响。AntiGEO 提供一个公开、可审计、可复核的风险登记层，让下游工具可以自主决定如何消费这份清单。

### 4. AntiGEO 如何工作？

AntiGEO 采用三段式流程：先提交可复核证据，再由社区审核，最后在满足条件时进入投票并决定状态。

### 5. watchlist / restricted / blocked 有什么区别？

`watchlist` 表示已有一定证据，需要继续观察；`restricted` 表示证据较充分，存在较明显的系统性操纵风险；`blocked` 表示证据强且相对明确，属于高风险 GEO 操纵源。

### 6. 被列入清单是否等于被“定罪”？

不等于。AntiGEO 记录的是风险状态及其证据基础，不是终局定罪，也不替代法律或监管结论。

### 7. AntiGEO 是不是在反对一切 SEO、广告或 PR？

不是。正常 SEO、官网内容、合法 PR 和明确标注的广告，并不自动属于 AntiGEO 的关注范围。项目关注的是系统性、规模化、可复核的操纵风险。

### 8. 单张截图、主观体验、二手整理材料能直接决定状态吗？

通常不能。这类材料通常只能作为辅助信息，单份辅助材料一般不能自动决定最终状态。

### 9. 为什么需要申诉与复审？

因为状态不是永久的。新证据、反证、事实更正和补充上下文都可能改变判断，公开治理也需要允许纠错。

### 10. 为什么主项目不直接做插件或 SDK 等接入层项目？

主项目聚焦标准、清单、证据与治理。插件和 SDK 属于消费层，应独立演进，这样边界更清楚，也更利于第三方接入。

### 11. 谁可以参与贡献？

社区贡献是欢迎的，但提交仍需符合项目规则、证据要求和协作原则。文档改进、术语统一和结构优化同样是有效贡献。

### 12. 如果我不同意某个状态怎么办？

你可以发起申诉或复审，并提供新证据、反证或事实更正。新的申诉或复审不会自动推翻既有结果，但会为重新判断提供基础。

进一步阅读：

- [README.md](../README.md)
- [docs/definition.md](./definition.md)
- [docs/governance.md](./governance.md)
- [docs/evidence-policy.md](./evidence-policy.md)
- [docs/voting.md](./voting.md)
- [docs/appeals.md](./appeals.md)
- [CONTRIBUTING.md](../CONTRIBUTING.md)

本 FAQ 会随着项目发展通过公开方式持续更新。

---

## English

### 1. What is AntiGEO?

AntiGEO is an open, auditable, community-governed GEO manipulation risk registry that records objects that may present systemic manipulation risk and the evidentiary basis for that risk.

### 2. What is AntiGEO not?

AntiGEO is not a tool for brand attacks, not a ranking of product quality, not a truth arbiter for single pieces of content, and not a substitute for legal or regulatory conclusions.

### 3. Why is AntiGEO needed?

AI search, summaries, and answer systems may be affected by systemic manipulation. AntiGEO provides an open, auditable, and verifiable risk registry layer so that downstream tools can choose how to consume the registry.

### 4. How does AntiGEO work?

AntiGEO follows a three-step process: submit verifiable evidence, conduct community review, and then move to voting when the conditions are met to determine status.

### 5. What is the difference between watchlist, restricted, and blocked?

`watchlist` means there is some evidence and the subject should continue to be observed. `restricted` means the evidence is relatively substantial and indicates a clearer systemic manipulation risk. `blocked` means the evidence is strong and comparatively clear, indicating a high-risk GEO manipulation source.

### 6. Does inclusion in the registry mean someone has been "convicted"?

No. AntiGEO records a risk status and its evidentiary basis. It is not a conviction or final determination, and it does not replace legal or regulatory conclusions.

### 7. Is AntiGEO opposed to all SEO, advertising, or PR?

No. Ordinary SEO, official website content, legitimate PR, and clearly disclosed advertising are not automatically within AntiGEO's scope. The project is concerned with systemic, scalable, and verifiable manipulation risk.

### 8. Can a single screenshot, subjective experience, or secondary compilation determine status directly?

Usually not. Supporting materials usually cannot determine status on their own, and a single supporting material should not automatically set the final status.

### 9. Why are appeals and re-review necessary?

Because statuses are not permanent. New evidence, counter-evidence, factual corrections, and added context may change the assessment, and open governance needs a way to correct the record.

### 10. Why does the main project not directly build plugins or SDKs?

The main project is focused on standards, the registry, evidence, and governance. Plugins and SDKs belong to the consumption layer and should evolve independently. That keeps boundaries clearer and makes third-party integration easier.

### 11. Who can contribute?

Community contributions are welcome, but submissions should still follow the project rules, evidence requirements, and collaboration principles. Documentation, terminology, and structural improvements are also valid contributions.

### 12. What if I disagree with a status?

You can initiate appeals or re-review and provide new evidence, counter-evidence, or factual corrections. A new appeal or re-review does not automatically overturn the existing result, but it can provide grounds for reassessment.

Further reading:

- [README.md](../README.md)
- [docs/definition.md](./definition.md)
- [docs/governance.md](./governance.md)
- [docs/evidence-policy.md](./evidence-policy.md)
- [docs/voting.md](./voting.md)
- [docs/appeals.md](./appeals.md)
- [CONTRIBUTING.md](../CONTRIBUTING.md)

This FAQ may be updated publicly as the project evolves.

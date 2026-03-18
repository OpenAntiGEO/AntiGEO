# Reference Package / 参考数据包

[中文](#中文) | [English](#english)

---

## 中文

### 1. 文档目的

本文件用于说明当前仓库中的 `registry/` 目录如何被理解为一个最小的 reference provider package。

### 2. 什么是 reference provider package

provider package 是一组符合 AntiGEO 格式的数据文件，用于被 provider 发布、被 consumer 加载。

当前仓库中的 `registry/` 目录提供了一个最小 `reference implementation`。它展示了当前 package 的基础结构、主要导出文件以及最小可消费布局。consumer 可以按这套结构理解和消费数据，provider 也可以把它作为参考。

### 3. 当前 package 中的文件

当前 `registry/` 目录中的主要文件包括：

- `manifest.json`：package 入口与文件发现信息
- `entities.compact.json`：面向 consumer 的轻量 entity 集合
- `full-index.json`：完整聚合数据
- `tag-topic-to-entities.json`：topic 索引
- `tag-intent-to-entities.json`：intent 索引
- `tag-risk-to-entities.json`：risk 索引
- `domain-to-entities.json`：domain 索引
- `name-to-entities.json`：name / alias 索引

其中：

- `watchlist.json`、`restricted.json`、`blocked.json` 更接近源数据分层文件
- 其余文件更接近面向 consumer 的导出产物

### 4. 当前 package 的用途

当前 package 的用途主要包括：

- provider 参考这套目录结构发布自己的 package
- consumer 参考这套目录结构加载数据
- 主项目提供一个最小参考布局，帮助不同实现对齐基本格式

当前主项目并不要求所有 provider 完全一致实现，但这套结构可以作为当前最小可用的参考起点。

### 5. 当前范围说明

这是一个最小 reference package。当前重点仍然是 entity registry 与 release data，不包含更复杂的治理、evidence、proposal、voting 等模块要求。

当前仓库中的 `scripts/build.py` 可以重新生成这些导出文件，`scripts/validate.py` 可以校验当前 entity registry 与 release 数据输出。

### 6. 进一步查看

- [README.md](../README.md)
- [docs/quick-start.md](./quick-start.md)

---

## English

### 1. Purpose

This document explains how the `registry/` directory in the current repository can be understood as a minimal reference provider package.

### 2. What A Reference Provider Package Is

A provider package is a set of AntiGEO-compatible data files published by a provider and loaded by a consumer.

The `registry/` directory in this repository provides a minimal `reference implementation`. It shows the current package shape, the main exported files, and the smallest useful consumable layout. Consumers can use this structure as a loading reference, and providers can use it as a publishing reference.

### 3. Files In The Current Package

The main files currently present under `registry/` include:

- `manifest.json`: package entry point and file-discovery metadata
- `entities.compact.json`: lightweight entity collection for consumers
- `full-index.json`: full aggregate data
- `tag-topic-to-entities.json`: topic index
- `tag-intent-to-entities.json`: intent index
- `tag-risk-to-entities.json`: risk index
- `domain-to-entities.json`: domain index
- `name-to-entities.json`: name / alias index

In addition:

- `watchlist.json`, `restricted.json`, and `blocked.json` are closer to layered source data files
- the remaining files are closer to consumer-facing exported outputs

### 4. What The Current Package Is For

The current package is mainly useful as:

- a reference for providers publishing their own package structure
- a reference for consumers loading AntiGEO-compatible data
- a minimal layout that helps different implementations align on the basic format

The main project does not require every provider to implement the package in exactly the same way, but this structure serves as the current minimal practical reference.

### 5. Current Scope

This is a minimal reference package. Its current focus remains the entity registry and release data. It does not introduce requirements for more complex governance, evidence, proposal, or voting modules.

In the current repository, `scripts/build.py` regenerates these exported files, and `scripts/validate.py` validates the current entity registry and release-data outputs.

### 6. Further Reading

- [README.md](../README.md)
- [docs/quick-start.md](./quick-start.md)

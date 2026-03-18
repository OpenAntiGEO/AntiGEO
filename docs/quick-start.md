# Quick Start / 快速开始

[中文](#中文) | [English](#english)

---

## 中文

### 1. 文档目的

本文件提供一个最小 Quick Start，用于帮助用户在本地快速跑通当前 AntiGEO `reference implementation` 的基础链路。

### 2. 前置条件

开始前，请确认：

- 已安装 Python 3
- 已 clone 本项目仓库

### 3. 创建虚拟环境

在仓库根目录运行：

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. 安装依赖

安装当前最小依赖：

```bash
python3 -m pip install -r requirements.txt
```

### 5. 运行校验

运行以下命令：

```bash
python3 scripts/validate.py
```

该脚本会校验当前 `registry` 基础数据以及当前 release 数据输出。

### 6. 运行构建

运行以下命令：

```bash
python3 scripts/build.py
```

该脚本会根据 `registry` 中的基础数据重新生成当前 release 数据文件。

### 7. 当前范围

当前 Quick Start 只覆盖最小的 schema / registry / build / validate 链路。当前仓库本身是一个最小 `reference implementation`，重点在于格式、结构和最小可运行流程。

### 8. 进一步查看

- [README.md](../README.md)
- [LICENSE](../LICENSE)

---

## English

### 1. Purpose

This document provides a minimal Quick Start for running the current AntiGEO `reference implementation` locally.

### 2. Prerequisites

Before you begin, make sure:

- Python 3 is installed
- the repository has been cloned locally

### 3. Create a Virtual Environment

From the repository root, run:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install Dependencies

Install the current minimal dependencies:

```bash
python3 -m pip install -r requirements.txt
```

### 5. Run Validation

Run:

```bash
python3 scripts/validate.py
```

This script validates the current `registry` base data and the current release-data outputs.

### 6. Run Build

Run:

```bash
python3 scripts/build.py
```

This script regenerates the current release-data files from the base data in `registry`.

### 7. Current Scope

This Quick Start covers only the minimal schema / registry / build / validate flow. The current repository is a minimal `reference implementation` focused on format, structure, and the smallest useful runnable path.

### 8. Further Reading

- [README.md](../README.md)
- [LICENSE](../LICENSE)

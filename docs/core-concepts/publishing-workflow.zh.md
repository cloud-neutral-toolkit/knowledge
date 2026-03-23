---
title: 发布流程
description: 在不破坏源目录边界的前提下调整公开文档结构的最小流程。
slug: publishing-workflow
lang: zh
tags:
  - docs
  - workflow
---

# 发布流程

当公开文档结构发生变化时，按这个顺序处理：

1. 在 `docs/**` 下新增或更新源页面。
2. 同步修改中英文导航清单。
3. 保持历史服务文档的链接稳定。
4. 重新加载 `docs.svc.plus`，验证分组导航和语言回退。

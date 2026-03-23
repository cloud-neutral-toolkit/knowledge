---
title: 双语支持
description: 定义英文与中文页面、导航标签如何成对组织。
slug: bilingual-support
lang: zh
tags:
  - docs
  - i18n
---

# 双语支持

文档入口层需要同时支持英文与中文。

## 规则

- 本地化集合页使用 `lang: en` 或 `lang: zh`
- 成对文件可以共享同一个公开 `slug`
- 导航标签分别维护在 `docs/navigation.en.yaml` 和 `docs/navigation.zh.yaml`

## 回退策略

如果某个语言版本不存在，`docs.svc.plus` 应回退到非本地化源页。

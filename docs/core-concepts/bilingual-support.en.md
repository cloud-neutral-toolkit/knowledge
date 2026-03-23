---
title: Bilingual support
description: How localized docs pages and navigation labels are paired for English and Chinese readers.
slug: bilingual-support
lang: en
tags:
  - docs
  - i18n
---

# Bilingual support

The docs entry layer supports both English and Chinese.

## Rules

- localized collection pages use `lang: en` or `lang: zh`
- paired localized files may share the same public `slug`
- navigation labels are defined independently in `docs/navigation.en.yaml` and `docs/navigation.zh.yaml`

## Fallback

If a localized variant does not exist, `docs.svc.plus` should fall back to the non-localized source page.

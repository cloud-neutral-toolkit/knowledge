# Content Schema

This document defines the minimum frontmatter contract expected by `docs.svc.plus`.

## Supported Roots

- `docs/**`
- `content/**`

## Recommended Frontmatter

```yaml
---
title: Example title
description: Short summary used for cards and metadata
date: 2026-03-19T00:00:00Z
author: shenlan
tags:
  - cloud-neutral
  - docs
category: example
---
```

## Minimum Rules

- Every new markdown document should include `title`
- Blog-style content under `content/**` should include `date`
- Use `tags` as a YAML array of strings
- Keep content under the allowlisted trees only; `docs-agent` will refuse writes outside them

## Language Rules

- Localized repository-level docs may live under `docs/zh/**` and `docs/en/**`
- Service collections continue to live under top-level directories like `docs/01-console/**`
- When no localized page exists, `docs.svc.plus` falls back to the non-localized source

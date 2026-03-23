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
slug: overview
lang: en
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
- Collection pages may also use paired files such as `overview.en.md` and `overview.zh.md`
- Use frontmatter `lang: en` or `lang: zh` on localized collection pages
- Use frontmatter `slug` when different localized files should resolve to the same public route
- When no localized page exists, `docs.svc.plus` falls back to the non-localized source

## Navigation Manifest

`docs.svc.plus` may read:

- `docs/navigation.en.yaml`
- `docs/navigation.zh.yaml`

Each manifest defines grouped sidebar navigation for the public docs experience.

```yaml
title: Cloud-Neutral Toolkit Docs
description: Public docs navigation
sections:
  - title: Get started
    items:
      - title: Welcome
        href: /docs/get-started/overview
```

Use the manifest to control section order, labels, and legacy-page placement without moving the source files themselves.

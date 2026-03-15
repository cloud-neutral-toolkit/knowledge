# Design

This repository is content-centric and should document editorial structure, publishing workflow, and knowledge organization.

Use this page to consolidate design decisions, ADR-style tradeoffs, and roadmap-sensitive implementation notes.

## Current code-aligned notes

- Documentation target: `knowledge`
- Repo kind: `content`
- Manifest and build evidence: repository structure and scripts only
- Primary implementation and ops directories: `scripts/`, `content/`
- Package scripts snapshot: No package.json scripts were detected.

## Existing docs to reconcile

- `01-console/CONFIG_SYSTEM_SUMMARY.md`
- `01-console/DESIGN_DOCS_REFACTOR.md`
- `03-rag-server/IMPLEMENTATION_GUIDE.md`
- `03-rag-server/TOKEN_AUTH_SUMMARY.md`
- `04-postgresql/SUMMARY.md`

## What this page should cover next

- Describe the current implementation rather than an aspirational future-only design.
- Keep terminology aligned with the repository root README, manifests, and actual directories.
- Link deeper runbooks, specs, or subsystem notes from the legacy docs listed above.
- Promote one-off implementation notes into reusable design records when behavior, APIs, or deployment contracts change.

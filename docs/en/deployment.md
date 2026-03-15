# Deployment

This repository is content-centric and should document editorial structure, publishing workflow, and knowledge organization.

Use this page to standardize deployment prerequisites, supported topologies, operational checks, and rollback notes.

## Current code-aligned notes

- Documentation target: `knowledge`
- Repo kind: `content`
- Manifest and build evidence: repository structure and scripts only
- Primary implementation and ops directories: `scripts/`, `content/`
- Package scripts snapshot: No package.json scripts were detected.

## Existing docs to reconcile

- `01-console/Runbook/RAG-Server.md`
- `02-accounts/SMTP_GMAIL_SETUP.md`
- `03-rag-server/Runbook/RAG-Server.md`
- `03-rag-server/deployment.md`
- `03-rag-server/google-cloud-run-howto.md`
- `04-postgresql/QUICKSTART.md`
- `04-postgresql/deployments/docker-compose.md`
- `04-postgresql/deployments/helm-chart.md`

## What this page should cover next

- Describe the current implementation rather than an aspirational future-only design.
- Keep terminology aligned with the repository root README, manifests, and actual directories.
- Link deeper runbooks, specs, or subsystem notes from the legacy docs listed above.
- Verify deployment steps against current scripts, manifests, CI/CD flow, and environment contracts before each release.

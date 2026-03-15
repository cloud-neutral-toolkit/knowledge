# Documentation Coverage Matrix

This matrix tracks the bilingual canonical documentation set for `knowledge` and maps it back to the current codebase and older docs.

该矩阵用于跟踪 `knowledge` 的双语规范文档，并将其与当前代码状态和历史文档对应起来。

| Category | EN | ZH | Current status | Existing references | Next check |
| --- | --- | --- | --- | --- | --- |
| Architecture | Yes | Yes | Seeded from current codebase and existing docs. | `04-postgresql/ARCHITECTURE.md`<br>`04-postgresql/PROJECT_STRUCTURE.md`<br>`04-postgresql/overview.md` | Keep diagrams and ownership notes synchronized with actual directories, services, and integration dependencies. |
| Design | Yes | Yes | Seeded from current codebase and existing docs. | `01-console/CONFIG_SYSTEM_SUMMARY.md`<br>`01-console/DESIGN_DOCS_REFACTOR.md`<br>`03-rag-server/IMPLEMENTATION_GUIDE.md`<br>`03-rag-server/TOKEN_AUTH_SUMMARY.md`<br>`04-postgresql/SUMMARY.md` | Promote one-off implementation notes into reusable design records when behavior, APIs, or deployment contracts change. |
| Deployment | Yes | Yes | Seeded from current codebase and existing docs. | `01-console/Runbook/RAG-Server.md`<br>`02-accounts/SMTP_GMAIL_SETUP.md`<br>`03-rag-server/Runbook/RAG-Server.md`<br>`03-rag-server/deployment.md`<br>`03-rag-server/google-cloud-run-howto.md`<br>`04-postgresql/QUICKSTART.md`<br>`04-postgresql/deployments/docker-compose.md`<br>`04-postgresql/deployments/helm-chart.md` | Verify deployment steps against current scripts, manifests, CI/CD flow, and environment contracts before each release. |
| User Guide | Yes | Yes | Seeded from current codebase and existing docs. | `01-console/CONFIG_SYSTEM_SUMMARY.md`<br>`01-console/MIGRATION_GUIDE.md`<br>`03-rag-server/IMPLEMENTATION_GUIDE.md`<br>`03-rag-server/TOKEN_AUTH_MANUAL.md`<br>`03-rag-server/configuration.md`<br>`03-rag-server/getting-started.md`<br>`03-rag-server/google-cloud-run-howto.md`<br>`04-postgresql/QUICKSTART.md` | Prefer workflow-oriented examples and keep screenshots or terminal snippets aligned with the latest UI or CLI behavior. |
| Developer Guide | Yes | Yes | Seeded from current codebase and existing docs. | `03-rag-server/PATH_VERIFICATION.md`<br>`03-rag-server/api-reference.md`<br>`03-rag-server/e2e_test_doc.md`<br>`04-postgresql/PROJECT_STRUCTURE.md` | Keep setup and test commands tied to actual package scripts, Make targets, or language toolchains in this repository. |
| Vibe Coding Reference | Yes | Yes | Seeded from current codebase and existing docs. | `03-rag-server/AGENTS.md`<br>`03-rag-server/api-reference.md` | Review prompt templates and repo rules whenever the project adds new subsystems, protected areas, or mandatory verification steps. |

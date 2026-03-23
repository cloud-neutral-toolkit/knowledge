---
week: 10
dates: "2026-05-18 ~ 2026-05-24"
status: draft
---

# Week 10 发布内容

> 账号：@Cloud_Neutral · 发布后在 [x-publish-queue.md](./x-publish-queue.md) 更新状态

---

## 📅 05-18（周一）· Radar 卡 · Trivy

**发布状态：** ⬜

```
🔍 Cloud-Neutral Radar | Trivy

Layer: Identity & Security — Supply Chain Security

One-line verdict:
Vulnerability scanning for container images, repos, IaC —
one tool, one format, no cloud lock-in.

What it does:
→ Scans container images for CVEs (OS packages + app dependencies)
→ Scans Git repos, filesystems, IaC (Terraform, K8s YAML)
→ SBOM generation (Software Bill of Materials)
→ Secret scanning in code and images
→ K8s-native: scan running clusters, not just images

✅ Strong fit:
– CI/CD pipeline security gate (image scan before push)
– Infrastructure-as-Code misconfiguration detection
– Supply chain security baseline for any team
– Cloud-neutral: runs anywhere, reports to anything

⚠️ Real trade-offs:
– False positive rate requires tuning
– Doesn't replace runtime security (see Falco for that)
– Enterprise features (policy management at scale) need integration work

The key insight:
Security scanning doesn't require a vendor.
Trivy is FOSS, integrates with any CI/CD, produces standard SARIF output.

The pipeline is yours. The security data is yours.

#Security #Trivy #DevSecOps #SupplyChain #CloudNative #SBOM
```

---

## 📅 05-20（周三）· Thread · Milvus vs Qdrant 向量数据库选型（6条）

**发布状态：** ⬜

**第 1 条：**
```
1/6 🧵

You're building a RAG pipeline.
You need a vector database.

Milvus or Qdrant?

Both are open-source. Both are production-ready.
The choice depends on scale and architecture.

Here's the practical comparison 👇

#VectorDB #RAG #AI #MLOps #CloudNeutral
```

**第 2 条：**
```
2/6

Milvus: designed for scale

→ Distributed architecture from day one
→ Handles billions of vectors
→ Cloud-native (K8s native, separate storage/compute)
→ Multiple index types (IVF, HNSW, DiskANN)
→ LF AI & Data Foundation project

Best for: large-scale production RAG, multi-tenant vector search,
enterprise data platform with vector capabilities.

⚠️ Overhead: requires MinIO, etcd, Pulsar — heavy for small deployments.
```

**第 3 条：**
```
3/6

Qdrant: designed for developer experience

→ Written in Rust — high performance, low memory
→ Single binary for development, scales for production
→ Payload filtering (filter by metadata + vector similarity simultaneously)
→ Built-in sparse vector support (hybrid search)
→ Clean REST + gRPC API

Best for: teams building AI products quickly,
hybrid search (keyword + semantic), smaller-to-medium scale.

⚠️ Distributed mode is newer than Milvus — less battle-tested at extreme scale.
```

**第 4 条：**
```
4/6

The decision matrix:

Scale > 100M vectors + enterprise deployment?
→ Milvus

Developer velocity + hybrid search (metadata filter + vector)?
→ Qdrant

Already have PostgreSQL and want to avoid another service?
→ pgvector first (PG extension, no extra infra)

Building proof of concept?
→ Qdrant (single binary, fast start)
```

**第 5 条：**
```
5/6

The pgvector option:

Before choosing either — have you tried pgvector?

If your data is already in PostgreSQL:
→ pgvector adds vector similarity search as an extension
→ No additional infrastructure
→ Same ACID guarantees, same backup strategy
→ Works well up to ~10M vectors (with tuning)

For most product-scale RAG workloads,
pgvector is sufficient and dramatically simpler.
```

**第 6 条：**
```
6/6

Bottom line:

Start here: pgvector (if data is already in PG)
Proof of concept: Qdrant (single binary, fast)
Production scale: Qdrant (up to ~50M vectors) or Milvus (100M+)

Cloud-neutral note:
Both Milvus and Qdrant run on your infra.
Neither requires a cloud-specific service.

Your AI data stack shouldn't be a vendor lock-in point.

#VectorDB #RAG #AI #CloudNeutral #Milvus #Qdrant #pgvector
```

---

## 📅 05-22（周五）· Radar 卡 · Apache Flink

**发布状态：** ⬜

```
🔍 Cloud-Neutral Radar | Apache Flink

Layer: Data & AI — Stream Processing

One-line verdict:
When your data problem is time, not just volume —
Flink processes it as it arrives.

What it does:
→ Stateful stream processing at scale
→ Event-time semantics — handle late-arriving data correctly
→ Exactly-once guarantees — financial-grade correctness
→ Unified batch + stream API
→ K8s native deployment (Flink Kubernetes Operator)

✅ Strong fit:
– Real-time analytics (fraud detection, metrics, alerting)
– Event-driven architectures with complex state
– CDC pipelines (Debezium → Flink → target)
– Replacing Spark for latency-sensitive workloads

⚠️ Real trade-offs:
– Steep learning curve (stateful operators, watermarks, checkpointing)
– Operational complexity — requires real expertise
– Not a batch ETL replacement unless you're already stream-processing

The boundary:
Batch (Spark, dbt): transform historical data
Stream (Flink): react to data as it happens

Both have their place. Don't use Flink if batch is sufficient.
Reach for Flink when latency is the constraint.

#ApacheFlink #StreamProcessing #DataEngineering #CloudNative #RealTime
```

---

## 📅 05-24（周日）· 长文导流 · Solo 独立开发 AI 协作实录

**发布状态：** ⬜

```
Over the past year I've been using AI as a daily collaborator
while building distributed systems solo.

Not a demo. Not a tutorial.
Here's what actually happened:

→ The system grew beyond what I could hold in my head.
   Auth, RAG server, database, frontend — 4 services, 1 person.

→ The bottleneck wasn't code generation.
   It was maintaining context across sessions,
   across debugging sessions that span browser + GitHub + Cloud Run.

→ What changed my workflow:
   Using AI that persists system understanding,
   not just reads files.
   The debugging happens in the real environment.
   Not in an isolated conversation.

The result:
Login, signup, MFA, AI assistant — all restored.
UI is still rough (working on it 😅).

But the loop is closed:
Solo founder. Distributed services. Maintained without a team.

This is what the next generation of solo building looks like.

#SoloDev #IndieDev #AI #Architecture #CloudNative
```

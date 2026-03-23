---
week: 1
dates: "2026-03-16 ~ 2026-03-22"
status: draft
---

# Week 01 发布内容

> 账号：@Cloud_Neutral
> 发帖时间参考：平日 9:00 AM 或 21:00 PM（UTC+8）· 周末 10:00 AM
> 发布后在 [x-publish-queue.md](./x-publish-queue.md) 对应行填写 ✅ 和推文链接

---

## 📅 03-16（周一）· Radar 卡 · Terraform / OpenTofu

**类型：** 单条推文
**字数：** ~260 字符
**发布状态：** ⬜

---

```
🔍 Cloud-Neutral Radar | Terraform / OpenTofu

Layer: IaC & Delivery — Change Control

One-line verdict:
Infrastructure changes should happen in code first.
Not in the console. Not in memory.

What it does:
→ Declares desired state (not steps)
→ Plan before apply — full diff before any change
→ Manages multi-cloud with one model
→ State file = explicit map of what actually exists

✅ Strong fit:
– Full audit trail built in
– Rollback = reverting a commit
– Works across AWS, GCP, Alibaba Cloud, bare metal

⚠️ Real trade-offs:
– State management requires discipline
– Not for high-frequency, fine-grained ops

OpenTofu: OSS fork. Same ecosystem. Community-governed. Neutral.

If scripts "do things to the world",
Terraform defines what the world should look like.

#IaC #Terraform #OpenTofu #CloudNative #DevOps
```

---

## 📅 03-18（周三）· Thread · Serverless DB 迁移 0-1-100（9条）

**类型：** Thread，共 9 条
**发布方式：** 先发第 1 条，之后在自己的回复里依次发 2-9 条
**发布状态：** ⬜

---

**第 1 条（主推文）：**
```
1/9 🧵

Frontend on Vercel. Backend on Cloud Run.
Zero idle cost. Perfect elasticity.

Then there's the database —
the one component that keeps billing you even when nobody's there. 💸

Here's a 0→1→100 migration strategy for indie builders 👇

#Serverless #IndieDev #Architecture
```

**第 2 条（回复到第1条）：**
```
2/9

The core tension:

Frontend/backend: no traffic = no cost. Smooth curve.
Database: running = billing. Always.

Most devs die on "over-engineering":
Spinning up a $30/mo Cloud SQL before a single user exists.

We need to decouple "connectivity" from "where data lives."
```

**第 3 条：**
```
3/9

Stage 0 — Prototype & Validate
Target: < $5/mo (or $0)

Best option: Serverless DB (Neon or Supabase)

They support Scale-to-Zero.
→ No connections = compute sleeps (no charge)
→ Request arrives = milliseconds to wake

Architecture:
Vercel → Cloud Run → Serverless DB (public connection)
```

**第 4 条：**
```
4/9

Stage 0 trade-offs:

✅ Near-zero cost at start
✅ Zero ops burden

⚠️ Cold start: DB wake-up adds ~200–500ms

Rule: Start here. Ship the product loop first.
Don't touch infrastructure until users exist.
```

**第 5 条：**
```
5/9

Stage 1 — Early Production
Target: $10–30/mo, eliminate cold starts

Best option: Budget VPS (Hetzner/Linode) + self-hosted Docker Postgres

Problem: Cloud Run has dynamic IPs.
IP allowlists won't work for the DB connection.
```

**第 6 条：**
```
6/9

Stage 1 — The Connection Problem

Solution: Secure tunnel sidecar

→ Tailscale (recommended): Mesh VPN between Cloud Run and VPS
→ Stunnel: Cloud Run sidecar, encrypted TCP tunnel to VPS

You get cheap VPS compute.
Your data doesn't travel in the open.
```

**第 7 条：**
```
7/9

Stage 100 — Large-Scale Production
Priority: High Availability > Cost

When a single point of failure is unacceptable:

Option A: Managed Cloud SQL — pay for peace of mind
Option B: Cloud-neutral: self-managed HA Postgres on K8s
(CloudNativePG or similar)

Stability is the only metric at this stage.
```

**第 8 条：**
```
8/9

The full route map:

🔹 Stage 0  | Neon/Supabase    | ~$0    | PoC
🔹 Stage 1  | VPS + Tunnel     | ~$10   | Growth
🔹 Stage 100| Cloud SQL/K8s HA | $100+  | Scale

Critical rule:
Don't optimize for Stage 100 when you're in Stage 0.
```

**第 9 条：**
```
9/9

If you're rebuilding an app today:

1. Register a Serverless DB (Neon is fast)
2. Point your Cloud Run env vars at it
3. Ship something

When real traffic arrives, come back for the Stage 1 tunnel setup.

RT if this saves someone from over-engineering too early 🔄

#IndieDev #SaaS #Serverless #CloudNative
```

---

## 📅 03-20（周五）· Radar 卡 · PostgreSQL Extensions

**类型：** 单条推文
**字数：** ~270 字符
**发布状态：** ⬜

---

```
🔍 Cloud-Neutral Radar | PostgreSQL (Extensions)

Layer: Data & AI — Core Data Platform

One-line verdict:
Not a new database. A platform that keeps growing
without swapping its core.

Key extensions:
→ pgvector    — vector search for AI/RAG
→ PostGIS     — geospatial, spatial indexes
→ TimescaleDB — time-series (metrics, events)
→ FDW         — query MySQL, Redis, S3 from inside PG
→ pg_cron     — job scheduling inside the DB

The real question:
Can a single database gain new capabilities
without replacing the engine?

PostgreSQL's answer: yes.
Extensions are first-class citizens.
Not plugins. Not hacks. Same transaction model.

✅ Strong fit:
– Core data hub for product systems
– Reducing moving parts in your stack
– Long-term platform you actually maintain

⚠️ Not the right fit:
– Pure OLAP at massive scale
– When you need extreme single-dimension throughput

"Most databases get replaced. PostgreSQL gets extended."

#PostgreSQL #DataEngineering #CloudNative #OpenSource
```

---

## 📅 03-22（周日）· 观点 · 云不是信仰

**类型：** 单条推文（观点）
**发布状态：** ⬜

---

```
The Xiaohongshu "leaving the cloud" story wasn't about a vendor.

Here's what it actually revealed:

The companies that can even discuss "should we move off cloud"
are the ones who never got locked in.

→ Kubernetes = workloads portable across infrastructure
→ Open-source middleware = no vendor data captivity
→ Hybrid by design = no single point of failure

Most companies don't have this choice.
They were locked in before they knew it mattered.

"The cloud isn't a belief system. It's a tool."

Use its elasticity for what it's good at.
Own the workloads that run 24/7 at scale.

#CloudNeutral #CloudNative #Architecture #Platform
```

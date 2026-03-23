---
week: 7
dates: "2026-04-27 ~ 2026-05-03"
status: draft
---

# Week 07 发布内容

> 账号：@Cloud_Neutral · 发布后在 [x-publish-queue.md](./x-publish-queue.md) 更新状态

---

## 📅 04-27（周一）· Radar 卡 · DuckDB

**发布状态：** ⬜

```
🔍 Cloud-Neutral Radar | DuckDB

Layer: Data & AI — Analytical Query Engine

One-line verdict:
OLAP that runs in-process.
No cluster. No server. Just a file and a query.

What it does:
→ Column-oriented analytical engine — runs inside your application
→ Reads Parquet, CSV, JSON, Arrow natively
→ SQL-first, PostgreSQL-compatible dialect
→ In-memory or persistent file mode
→ Single binary, embeds in Python/Node/Go/Java

✅ Strong fit:
– Data scientists running analytics on laptops (no Spark cluster)
– Log analysis, metrics exploration, ad-hoc queries on files
– Replacing pandas for medium-scale data work
– Edge analytics where a server isn't available

⚠️ Real trade-offs:
– Single-node only — no horizontal scale
– Not designed for concurrent writes or OLTP
– Large datasets eventually need something else (ClickHouse, Databend)

The question DuckDB answers:
Does analytical work always require a cluster?

For datasets under ~100GB: no.
A local process with a Parquet file beats a distributed system
for complexity, cost, and operational overhead.

"OLAP doesn't need to be a service. Sometimes it just needs to be a library."

#DuckDB #DataEngineering #Analytics #OpenSource #CloudNeutral
```

---

## 📅 04-29（周三）· Thread · Pulumi vs Terraform（6条）

**发布状态：** ⬜

**第 1 条：**
```
1/6 🧵

Terraform is the IaC standard.
Pulumi lets you write infrastructure in real code.

Both are cloud-neutral. Both are open-source.
The difference matters more than people admit.

Here's the honest comparison 👇

#IaC #Terraform #Pulumi #CloudNative #DevOps
```

**第 2 条：**
```
2/6

Terraform's model:

HCL (HashiCorp Configuration Language)
→ Declarative: describe what you want
→ Plan/Apply: full diff before any change
→ State file: explicit map of reality
→ 14 years of ecosystem maturity

The strength: everyone can read it.
The limit: HCL isn't Turing-complete. Complex logic gets ugly.
```

**第 3 条：**
```
3/6

Pulumi's model:

Real programming languages (TypeScript, Python, Go, Java, C#)
→ Same declarative intent, real code
→ Loops, conditionals, functions — natural
→ Reusable infrastructure as library packages
→ Same plan/apply model as Terraform

The strength: complex infrastructure logic without workarounds.
The limit: steeper onboarding if your team isn't developers.
```

**第 4 条：**
```
4/6

When to choose Terraform:

→ Team is ops-heavy, not developer-heavy
→ You need maximum ecosystem compatibility (providers, modules)
→ Existing HCL investment is significant
→ You want the "everyone knows this" option

OpenTofu note: if you're on Terraform, consider OpenTofu.
Same HCL, same ecosystem, community-governed, truly neutral.
```

**第 5 条：**
```
5/6

When to choose Pulumi:

→ Infrastructure is complex enough that HCL becomes a limitation
→ Your team writes code daily — IaC should feel like code
→ You want to publish infrastructure as reusable packages
→ You're building an internal platform on top of IaC

The crossover point: when your Terraform modules need
"if the environment is production and the region is X and the team is Y..."
```

**第 6 条：**
```
6/6

Bottom line:

Both are cloud-neutral.
Both have plan-before-apply.
Both manage state.

Terraform: stable, universal, slight HCL ceiling
Pulumi: full programming model, higher DevX ceiling

The worst choice: vendor-specific IaC (AWS CDK, Azure Bicep).
That's not IaC — that's vendor lock-in with extra steps.

#IaC #CloudNeutral #Terraform #Pulumi #OpenTofu
```

---

## 📅 05-01（周五）· Radar 卡 · ClickHouse

**发布状态：** ⬜

```
🔍 Cloud-Neutral Radar | ClickHouse

Layer: Data & AI — Real-time Analytics

One-line verdict:
If you need to scan billions of rows in seconds,
ClickHouse is where the conversation starts.

What it does:
→ Column-oriented OLAP database
→ Real-time inserts + analytical queries on the same system
→ Vectorized query execution — extreme single-query throughput
→ MergeTree engine family — efficient for time-series / event data
→ SQL interface, rich ecosystem

✅ Strong fit:
– Product analytics (events, sessions, funnels)
– Infrastructure monitoring at scale (logs, metrics storage)
– Ad-tech, fintech time-series workloads
– Replacing Elasticsearch for log analytics

⚠️ Real trade-offs:
– Not for OLTP — writes are batched, not row-level
– JOINs are expensive — denormalized schemas work better
– Operational complexity at scale (sharding, replication)
– Schema design requires upfront thought

The comparison:
DuckDB: single-node, in-process, ~100GB scale
ClickHouse: distributed, server, billion-row scale

Same family. Different scope.

#ClickHouse #DataEngineering #Analytics #CloudNeutral #OpenSource
```

---

## 📅 05-03（周日）· 长文导流 · AI 与工程写作实录

**发布状态：** ⬜

```
I've been using AI in my daily engineering work for over a year.

Not for code generation (that's table stakes now).

For something harder: building and maintaining a writing practice
as a solo engineer.

3 things that actually changed how I work:

→ 1. AI doesn't write for me. It helps me not lose the thread.
   Across browser, GitHub, Cloud Run, and Vercel — real system context,
   not sandboxed imagination.

→ 2. Continuity beats speed.
   The most valuable thing isn't writing faster.
   It's having something that stays with the system across weeks.
   Context doesn't reset when I come back on Tuesday.

→ 3. The writing is the thinking.
   Explaining a technical decision in plain language
   is how I find out if I actually understand it.

The blog post from this year that changed how I think:
"AI tools don't save time. They save cognitive load."

That's the right frame.

#AI #Engineering #SoloDev #Writing #IndieDev
```

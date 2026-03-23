---
week: 4
dates: "2026-04-06 ~ 2026-04-12"
status: draft
---

# Week 04 发布内容

> 账号：@Cloud_Neutral
> 发帖时间参考：平日 9:00 AM 或 21:00 PM（UTC+8）· 周末 10:00 AM
> 发布后在 [x-publish-queue.md](./x-publish-queue.md) 对应行填写 ✅ 和推文链接

---

## 📅 04-06（周一）· Radar 卡 · OpenTelemetry

**类型：** 单条推文
**发布状态：** ⬜

---

```
🔍 Cloud-Neutral Radar | OpenTelemetry

Layer: Observability — Neutral Instrumentation Standard

One-line verdict:
Stop choosing between observability vendors.
OTel separates instrumentation from where data goes.

What it does:
→ Unified SDK for traces, metrics, and logs
→ Vendor-agnostic — instrument once, export anywhere
→ Auto-instrumentation for most major frameworks
→ Collector: pipeline, filtering, routing, transformation
→ CNCF graduated project — stable, broad adoption

✅ Strong fit:
– Multi-cloud / cloud-neutral observability stack
– Teams tired of re-instrumenting when changing backends
– Polyglot services (Java, Go, Python, Node all supported)

⚠️ Real trade-offs:
– Spec is complex — not everything is GA across all signals
– Logs support still maturing in some SDKs
– Collector requires its own ops attention

The key insight:
OpenTelemetry doesn't store anything.
It defines the contract for how observability data moves.

Jaeger, Grafana, Datadog, Honeycomb — they all accept OTel.
You decide where data lives. OTel decides the format.

#Observability #OpenTelemetry #CloudNative #CNCF #DevOps
```

---

## 📅 04-08（周三）· Thread · Solo Founder 的分布式服务边界（6条）

**类型：** Thread，共 6 条
**来源：** `threads/2026-01-26-distributed-service-boundaries.md`（改写为英文为主）
**发布方式：** 先发第 1 条，之后 reply 继续
**发布状态：** ⬜

---

**第 1 条（主推文）：**
```
1/6 🧵

Solo building means constantly fixing things that almost work.

After weeks of iteration on a distributed system —
frontend, auth, RAG server, database —
here's what I learned about service boundaries as a single person.

#SoloDev #IndieDev #Architecture #SaaS
```

**第 2 条：**
```
2/6

The temptation: keep everything in one repo, one service.

The problem: one mess is still a mess, just faster to create.

What actually helped:
Clear service boundaries — not for scale, but for thinking.

Frontend / Auth / RAG / Database.
Each has one job. Each fails independently.
When something breaks, you know where to look.
```

**第 3 条：**
```
3/6

The hardest part isn't the split.

It's maintaining context across services when you're alone.

Most tools forget what they helped you build last week.

What I needed wasn't speed.
It was continuity — something that stayed with the system
across refactors instead of resetting every session.
```

**第 4 条：**
```
4/6

Real debugging for solo builders doesn't happen in a sandbox.

It happens across:
browser → GitHub → Cloud Run → Vercel

The system is the debug environment.
You need tools that can follow you there —
not just read the code, but understand what's deployed.
```

**第 5 条：**
```
5/6

After the refactor:

✅ Login works
✅ Signup + MFA works  
✅ AI assistant restored
✅ Core flows back

The UI still isn't pretty (yet 😅).

But here's what matters as a solo builder:
You don't need magic.
You need to get the system back into a stable, shippable state.
```

**第 6 条：**
```
6/6

Distributed services for one person is a choice, not a mistake.

The boundary isn't about team size.
It's about fault isolation and cognitive load.

When auth breaks, it breaks auth — not everything.
When the RAG server needs to be rewritten, everything else keeps running.

Build for maintainability first.
Scale is someone else's problem for now.

#SoloDev #IndieDev #CloudNative #Architecture
```

---

## 📅 04-10（周五）· Radar 卡 · APISIX

**类型：** 单条推文
**发布状态：** ⬜

---

```
🔍 Cloud-Neutral Radar | Apache APISIX

Layer: Runtime & Boundary — API Gateway

One-line verdict:
High-performance API gateway, cloud-neutral by design.
No vendor lock-in baked into the data plane.

What it does:
→ Dynamic routing, load balancing, rate limiting
→ Plugin architecture — extend without forking
→ Multi-protocol: HTTP, gRPC, WebSocket, Dubbo
→ Native Kubernetes ingress + service mesh integration
→ Apache-governed — truly open source

✅ Strong fit:
– Teams escaping cloud-native API gateway vendor lock-in
– High-throughput API traffic (built on Nginx/OpenResty)
– Complex routing logic, custom plugin requirements

⚠️ Real trade-offs:
– Smaller ecosystem than Kong in some enterprise areas
– Lua plugin model has a learning curve
– Observability plugins need deliberate configuration

The comparison that matters:
Kong: established enterprise ecosystem
APISIX: newer, faster, genuinely cloud-neutral architecture

If your API gateway routes are a vendor contract,
APISIX is worth the migration cost.

#APISIX #APIGateway #CloudNative #OpenSource #Kubernetes
```

---

## 📅 04-12（周日）· 长文导流 · 从物理机到云端工程史

**类型：** 长文导流推文
**关联长文：** `essays/IT-Salon_From-Bare-Metal-to-the-Cloud...md`
**发布状态：** ⬜

---

```
I wrote about the real history of infrastructure complexity.

Not "tech got better over time."

It's about how engineers kept moving the boundary
between human control and system control —
one layer at a time.

5 key ideas:

→ VMs didn't solve complexity. They moved it inside a boundary.
→ Containers didn't replace VMs. They changed the unit of delivery.
→ Kubernetes manages intent, not machines.
→ K3s proved the idea compresses to fit constraints.
→ k3k treats clusters as resources — control planes controlling control planes.

The pattern isn't progress.
It's redistribution.

Every generation doesn't eliminate complexity.
It moves it somewhere humans can still reason about.

Full piece in the replies 👇

#Platform #Engineering #Kubernetes #CloudNative #DevOps
```

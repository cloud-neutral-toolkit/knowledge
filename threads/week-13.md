---
week: 13
dates: "2026-03-30 ~ 2026-04-05"
status: draft
---

# Week 13 发布内容

> 账号：@Cloud_Neutral
> 发帖时间参考：平日 9:00 AM 或 21:00 PM（UTC+8）· 周末 10:00 AM
> 发布后在 [x-publish-queue.md](./x-publish-queue.md) 对应行填写 ✅ 和推文链接

---

## 📅 03-30（周一）· Radar 卡 · VictoriaMetrics

**类型：** 单条推文
**发布状态：** ⬜

---

```
🔍 Cloud-Neutral Radar | VictoriaMetrics

Layer: Observability — Long-term Metrics Storage

One-line verdict:
Prometheus wrote the contract.
VictoriaMetrics optimized the storage.

What it does:
→ Drop-in replacement for Prometheus long-term storage
→ Single-node handles millions of samples/sec
→ Clustering for horizontal scale
→ 10x compression vs Prometheus
→ Compatible with PromQL, Grafana, Prometheus alerts

✅ Strong fit:
– Teams outgrowing single-node Prometheus
– Cost-sensitive monitoring at scale
– Need > 30 days retention without 10x storage cost
– Cloud-native: runs anywhere, no vendor lock-in

⚠️ Real trade-offs:
– Not a full Prometheus replacement for all use cases
– Clustering adds operational complexity
– Less mature ecosystem than Thanos/Mimir

The key insight:
Prometheus won because it defined the metrics standard.
VictoriaMetrics wins because it solves the storage cost problem
without breaking that standard.

"Keep the contract. Optimize the implementation."

#Observability #VictoriaMetrics #Prometheus #Monitoring #CloudNative
```

---

## 📅 04-01（周三）· Thread · Pulumi vs Terraform：IaC 选型（6条）

**类型：** Thread，共 6 条
**发布方式：** 先发第 1 条，之后在自己的回复里依次发 2-6 条
**发布状态：** ⬜

---

**第 1 条（主推文）：**
```
1/6 🧵

Terraform or Pulumi?

Both do Infrastructure as Code.
Both manage cloud resources.
But they answer a different fundamental question:

" What is the source of truth for your infrastructure? "

Here's the real difference 👇

#IaC #Terraform #Pulumi #DevOps #CloudNative
```

**第 2 条（回复到第1条）：**
```
2/6

Terraform: declarative configuration (HCL)

You write: "I want an S3 bucket with these properties"
Terraform figures out: "Create, modify, or destroy these resources in this order"

Pros:
→ Language designed for infra (readable, structured)
→ Massive provider ecosystem
→ Plan output is human-readable

Cons:
→ Learning HCL is learning a new language
→ Complex logic requires workaround patterns
→ State management can be painful at scale
```

**第 3 条：**
```
3/6

Pulumi: real programming languages

You write: TypeScript, Python, Go, C# — your infrastructure code
Pulumi reads your code, creates an execution plan, runs it

Pros:
→ Use real languages: loops, conditionals, testing, IDE support
→ Share code via packages
→ Same language for infra and app logic

Cons:
→ Team needs language expertise
→ Smaller community than Terraform
→ Some edge cases in drift detection
```

**第 4 条：**
```
4/6

The real question isn't "which is better."

It's: "Who maintains your infrastructure code?"

Terraform: best when your team includes dedicated infra engineers
who write HCL day-in, day-out

Pulumi: best when your app developers also own infrastructure
and want to use familiar languages
```

**第 5 条：**
```
5/6

Migration reality:

Switching isn't just "translating" the code.
It's changing how your team thinks about infra.

Terraform plan → visual, reviewable, shareable
Pulumi program → testable, composable, programmatic

Both can work. The question is which mental model fits your org.
```

**第 6 条：**
```
6/6

Practical recommendation:

Start small:
→ Terraform if infra is a dedicated team's responsibility
→ Pulumi if developers should own their infra too

The real trap:
Using "infrastructure as code" as a buzzword
without answering: who's actually writing and maintaining it?

That's the decision that matters.

#IaC #Terraform #Pulumi #Platform #Engineering
```

---

## 📅 04-03（周五）· Radar 卡 · Kong

**类型：** 单条推文
**发布状态：** ⬜

---

```
🔍 Cloud-Neutral Radar | Kong

Layer: Runtime & Boundary — API Gateway

One-line verdict:
The API gateway that grew into a service platform.
Battle-tested at massive scale, but not the only answer.

What it does:
→ API gateway: rate limiting, auth, routing, transformation
→ Plugins: 100+ built-in (OAuth, JWT, rate-limit, logging, etc.)
→ Declarative config: Kong declarative config / K8s Ingress
→ Service mesh: Kuma integration
→ Multiple deployment modes: DB-less, traditional, Kubernetes

✅ Strong fit:
– Organizations needing mature, documented API management
– Teams with existing Kong investment
– Complex routing and transformation requirements
– Enterprise features (RBAC, audit logs) out of the box

⚠️ Real trade-offs:
– More complex than simple Nginx reverse proxy
– Plugin ecosystem can create dependency lock-in
– Performance overhead vs bare Nginx/APISIX
– Operational knowledge required

The honest assessment:
Kong is the "enterprise answer" to API gateways.
If you need the features, it's worth it.
If you just need routing + basic auth, simpler options exist.

"Not every gateway needs to be a platform."

#Kong #APIGateway #Microservices #CloudNative #API
```

---

## 📅 04-05（周日）· 长文导流 · 从物理机到 K8s：复杂性管理史

**类型：** 长文导流推文（单条）
**发布状态：** ⬜

---

**主推文：**
```
From bare metal to Kubernetes:

A 40-year history of one thing:
how we manage complexity in computing.

→ Physical machines: one app per server, massive waste
→ Virtualization: KVM/QEMU, share hardware, keep OS isolation
→ Containers: Docker, package the environment not the machine
→ Kubernetes: declare desired state, let the system reconcile
→ k3s/k3k: the same model, compressed for edge

Every layer abstraction didn't eliminate complexity.
It moved it.

The real insight:

We're not delivering applications.
We're delivering replicable computing order.

Full analysis 👇

[Link to essay]

#Engineering #History #Kubernetes #CloudNative #Platform
```

---

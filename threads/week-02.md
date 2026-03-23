---
week: 2
dates: "2026-03-23 ~ 2026-03-29"
status: draft
---

# Week 02 发布内容

> 账号：@Cloud_Neutral
> 发帖时间参考：平日 9:00 AM 或 21:00 PM（UTC+8）· 周末 10:00 AM
> 发布后在 [x-publish-queue.md](./x-publish-queue.md) 对应行填写 ✅ 和推文链接

---

## 📅 03-23（周一）· Radar 卡 · Cilium

**类型：** 单条推文
**发布状态：** ⬜

---

```
🔍 Cloud-Neutral Radar | Cilium

Layer: Runtime & Boundary — Network Policy

One-line verdict:
eBPF brought networking into the kernel.
Cilium made that usable for production Kubernetes.

What it does:
→ Enforces L3/L4/L7 network policy at kernel level
→ Replaces iptables — no more rule explosion at scale
→ Transparent observability via Hubble (no sidecars)
→ Service mesh capabilities without proxy overhead

✅ Strong fit:
– Large-scale Kubernetes clusters (100+ nodes)
– Zero-trust networking requirements
– Teams outgrowing iptables-based CNI

⚠️ Real trade-offs:
– Kernel version requirements (Linux 4.9+, ideally 5.10+)
– Steeper learning curve than Calico/Flannel
– eBPF expertise not yet common

The shift from iptables to eBPF isn't just performance.
It's a fundamentally different model for where policy lives.

#Kubernetes #eBPF #CloudNative #NetworkSecurity #Cilium
```

---

## 📅 03-25（周三）· 长文导流 · 小红书下云：真正的工程启示

**类型：** 长文导流推文（单条 + 可展开 Thread）
**发布状态：** ⬜

---

**主推文（单条发布，可独立存在）：**
```
The "Xiaohongshu leaving Alibaba Cloud" story missed the real point.

3 things it actually teaches us about cloud architecture:

→ 1. Scale changes the math
   Elasticity is cloud's strength.
   Constant high-load workloads? That math flips.

→ 2. Lock-in is a choice made early
   Xiaohongshu could move because they stayed neutral:
   K8s everywhere. Open-source middleware. No vendor data captivity.

→ 3. Hybrid is the destination, not a compromise
   Not anti-cloud. Not pro-self-hosting.
   Use cloud for bursts. Own what runs 24/7.

Most companies don't get to make this choice.
They were locked in before they knew it mattered.

The real story: cloud isn't a religion. It's a tool with a cost curve.

#CloudNeutral #Architecture #Kubernetes #Platform
```

---

## 📅 03-27（周五）· Radar 卡 · Prometheus

**类型：** 单条推文
**发布状态：** ⬜

---

```
🔍 Cloud-Neutral Radar | Prometheus

Layer: Observability — Metrics Foundation

One-line verdict:
The metrics standard. Not because it's perfect —
because the whole ecosystem converged on it.

What it does:
→ Pull-based scraping — services expose /metrics, Prometheus collects
→ PromQL — expressive query language for time-series
→ AlertManager — rule-based alerting with routing
→ Service discovery — dynamic target registration

✅ Strong fit:
– Kubernetes-native monitoring (metrics already exposed)
– Multi-cloud / cloud-neutral observability stack
– Long-term metrics + alerting foundation

⚠️ Real trade-offs:
– Storage doesn't scale horizontally by default
– Long-term retention needs Thanos / VictoriaMetrics / Mimir
– Pull model struggles with ephemeral / serverless targets

The key insight:
Prometheus didn't win because it's the best storage system.
It won because it defined the metrics contract.
Everyone else builds around it.

#Observability #Prometheus #CloudNative #SRE #Monitoring
```

---

## 📅 03-29（周日）· 观点 · Stage 0 / Stage 100

**类型：** 单条推文（观点）
**发布状态：** ⬜

---

```
Most engineering debt starts with a lie:

"We might need this at scale someday."

The $30/mo database before a single user.
The Kubernetes cluster for a 3-page app.
The microservices split before product-market fit.

Here's what actually works:

Stage 0: Prove the loop works. Spend $0.
Stage 1: Handle real traffic. Spend $10-30.
Stage 100: Stability > cost. Spend accordingly.

The rule isn't "don't think about the future."
The rule is: don't build for a stage you haven't reached.

Every premature optimization is a bet on a future
that probably won't look the way you imagined.

Ship first. Architect later.

#IndieDev #SoloDev #Architecture #Engineering
```

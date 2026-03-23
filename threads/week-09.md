---
week: 9
dates: "2026-05-11 ~ 2026-05-17"
status: draft
---

# Week 09 发布内容

> 账号：@Cloud_Neutral · 发布后在 [x-publish-queue.md](./x-publish-queue.md) 更新状态

---

## 📅 05-11（周一）· Radar 卡 · k3s

**发布状态：** ⬜

```
🔍 Cloud-Neutral Radar | k3s

Layer: Platform Foundation — Lightweight Kubernetes

One-line verdict:
Kubernetes, compressed.
Same API. Same declarative model. 60MB binary.

What it does:
→ Fully conformant Kubernetes distribution
→ Replaces etcd with SQLite (or external DB for HA)
→ Bundles containerd, CoreDNS, Traefik, Helm controller
→ ARM and x86 support — IoT/edge to VPS
→ Single binary install, 512MB RAM minimum

✅ Strong fit:
– Edge nodes, IoT devices, resource-constrained environments
– Dev/test clusters (fast spin-up)
– Small production deployments ($5 VPS can run it)
– Multi-site edge with consistent K8s API

⚠️ Real trade-offs:
– Less tested at massive scale than full K8s
– Default config (SQLite) limits HA without external DB
– Some enterprise K8s features require additional setup

The key point:
k3s isn't "K8s for beginners."
It's K8s for environments where full K8s is too heavy.

The idea compresses. The API stays the same.

#k3s #Kubernetes #Edge #CloudNative #OpenSource
```

---

## 📅 05-13（周三）· Thread · k3s + k3k：把集群变成资源（6条）

**发布状态：** ⬜

**第 1 条：**
```
1/6 🧵

Kubernetes manages pods.
k3s made Kubernetes fit constrained environments.
k3k made clusters themselves a resource.

This is the recursion at the edge of cloud-neutral infrastructure.

Let me explain 👇

#Kubernetes #k3s #k3k #Platform #CloudNative
```

**第 2 条：**
```
2/6

K3s: Kubernetes, compressed

Same API. Same declarative model.
But: 60MB binary, 512MB RAM, runs on a $5 VPS.

The insight: the *idea* of Kubernetes (declare intent, reconcile toward it)
doesn't require a multi-node cluster.

K3s proved the abstraction can compress without losing its properties.
```

**第 3 条：**
```
3/6

When k3s appears everywhere, a new problem emerges:

How do you manage 50 k3s clusters across edge sites?

The answer can't be "manually SSH into each one."
The answer has to be: treat clusters the same way K8s treats pods.

Declare what clusters you want.
Let the system reconcile toward that.
```

**第 4 条：**
```
4/6

k3k: Kubernetes clusters inside Kubernetes

k3k runs Kubernetes clusters as workloads on an existing cluster.
Cluster as a Resource.

→ Provision a new K8s cluster: kubectl apply
→ Delete it: kubectl delete
→ Scale the control plane: it's just a deployment

The concept: cluster lifecycle becomes part of your existing GitOps workflow.
```

**第 5 条：**
```
5/6

Why this matters for platform engineering:

Without k3k: each cluster is a snowflake.
Manual provisioning. Manual upgrades. Manual deletion.

With k3k: clusters become declarative, versionable, automatable.

Platform teams stop being "cluster admins"
and start being "cluster operators" —
same shift that happened with app deployments when Docker arrived.
```

**第 6 条：**
```
6/6

The recursion pattern:

Physical machine → managed by KVM (resource pool)
Container → managed by K8s (declared, reconciled)
Cluster → managed by k3k (declared, reconciled)

Every generation: the previous layer becomes a resource
that the next layer can schedule, scale, and recycle.

"You're not delivering apps. You're delivering replicable computing order."

#Platform #k3k #k3s #Kubernetes #CloudNeutral #Engineering
```

---

## 📅 05-15（周五）· Radar 卡 · OpenStack

**发布状态：** ⬜

```
🔍 Cloud-Neutral Radar | OpenStack

Layer: Platform Foundation — Private Cloud IaaS

One-line verdict:
The private cloud standard. Proven, complex,
and exactly right for specific organizations.

What it does:
→ Full IaaS: compute (Nova), networking (Neutron), storage (Cinder/Swift)
→ Multi-tenant, multi-region private cloud
→ OpenStack API compatible with many tools
→ CNCF/Linux Foundation ecosystem integration
→ Enterprise deployment: large banks, telcos, research institutions

✅ Strong fit:
– Organizations with significant on-prem hardware investment
– Regulated industries requiring data sovereignty
– Telecoms / national infrastructure operators
– Environments needing cloud-like APIs on owned hardware

⚠️ Real trade-offs:
– Operational complexity: requires dedicated platform team
– Steep learning curve — not a weekend project
– Upgrade cycles are complex and risky
– Many have migrated to K8s + Harvester for simpler IaaS

The honest assessment:
OpenStack isn't for everyone.
But for large-scale, regulated, hardware-owning organizations —
it remains the most mature open-source IaaS platform.

#OpenStack #PrivateCloud #CloudNeutral #IaaS #Infrastructure
```

---

## 📅 05-17（周日）· 观点 · 边缘计算是工程下沉

**发布状态：** ⬜

```
"Edge computing" sounds like a new concept.

It's not. It's the same problem restated:

Where does the compute need to be
for this workload to work?

Sometimes the answer is: next to the data (edge).
Sometimes: centralized (cloud).
Sometimes: distributed but controlled (k3s + k3k).

The important realization:

Kubernetes at the edge isn't about making K8s "cool."
It's about extending the same declarative model —
the one that works in the data center —
to constrained environments.

Same intent. Different container.

k3s proved: the abstraction compresses.
k3k proved: clusters can be resources too.

The next shift: you stop thinking about where compute runs.
You declare what you need, and the system finds where.

We're not there yet. But the trajectory is clear.

#Edge #Kubernetes #k3s #Platform #CloudNeutral #Engineering
```

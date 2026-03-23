---
week: 3
dates: "2026-03-30 ~ 2026-04-05"
status: draft
---

# Week 03 发布内容

> 账号：@Cloud_Neutral
> 发帖时间参考：平日 9:00 AM 或 21:00 PM（UTC+8）· 周末 10:00 AM
> 发布后在 [x-publish-queue.md](./x-publish-queue.md) 对应行填写 ✅和推文链接

---

## 📅 03-30（周一）· Radar 卡 · Argo CD

**类型：** 单条推文
**发布状态：** ⬜

---

```
🔍 Cloud-Neutral Radar | Argo CD

Layer: IaC & Delivery — GitOps

One-line verdict:
Git becomes the single source of truth.
Argo CD makes sure reality agrees with it — continuously.

What it does:
→ Watches Git repos for desired state (YAML/Helm/Kustomize)
→ Continuously reconciles cluster state toward Git
→ Automatic or manual sync — your call
→ Multi-cluster management from one control plane
→ Full UI + CLI + API

✅ Strong fit:
– Kubernetes-first delivery pipelines
– Teams that need audit trails and rollback
– Multi-env, multi-cluster deployment control

⚠️ Real trade-offs:
– Tightly coupled to Kubernetes
– Requires shift from imperative to declarative thinking
– Limited support for non-K8s deployments

The insight:
Argo CD didn't invent GitOps.
It made GitOps something a team could actually run in production.

Rollback = git revert. That's the whole model.

#GitOps #ArgoCD #Kubernetes #DevOps #CloudNative
```

---

## 📅 04-01（周三）· Thread · 从物理机到 K8s：复杂性管理史（6条）

**类型：** Thread，共 6 条
**来源：** `essays/IT-Salon_From-Bare-Metal-to-the-Cloud...md`
**发布方式：** 先发第 1 条，之后 reply 到自己这条继续
**发布状态：** ⬜

---

**第 1 条（主推文）：**
```
1/6 🧵

From bare metal to Kubernetes, this isn't a "tech upgrade" story.

It's a story about how engineers kept moving the boundary
between what humans control and what systems control.

5 acts. One enemy: unmanaged complexity. 👇

#Kubernetes #CloudNative #Platform #DevOps
```

**第 2 条：**
```
2/6

Act 1: Virtualization

One physical server. One app. Massive waste.

KVM/QEMU changed the math:
split one machine into many "real enough" machines.

The insight wasn't technical — it was economic.
When hardware cost becomes visible, sharing stops being risky.

Complexity moved inside the VM.
Hardware became a resource pool for the first time.
```

**第 3 条：**
```
3/6

Act 2: Containers

VMs solved sharing. But they brought the whole OS.

Containers asked a dangerous question:
"Can we just bring the app, not the operating system?"

namespace = "you can't see mine"
cgroup = "you can't eat mine"
Docker = made this explainable to developers

Once "image = unit of delivery" landed,
apps became portable. Infra stepped back.
```

**第 4 条：**
```
4/6

Act 3: Kubernetes

Containers above 100 units break human cognition.

Kubernetes replaced:
"I understand every step"
with:
"I trust it will keep correcting toward my declared state."

The shift: imperative ops → declarative intent.

You say: "I want 3 replicas."
The system asks: "How many do we actually have?" — forever.
```

**第 5 条：**
```
5/6

Act 4: Edge & Recursion (K3s / k3k)

Kubernetes assumed: stable network, full resources, expert ops.

The edge disagreed.

K3s compressed the idea to fit constrained environments.
k3k went further: treated the cluster itself as a resource.

Control planes controlling control planes.
You're no longer deploying apps.
You're delivering replicable computing order.
```

**第 6 条：**
```
6/6

The pattern across all 5 acts:

Each layer didn't eliminate complexity.
It moved it somewhere humans could still reason about.

VMs → contained per-app chaos
Containers → portable, reproducible units
K8s → declared intent, continuous reconciliation
K3s/k3k → cluster as deployable resource

The next system won't be "smarter."
It'll know when to appear — and when to get out of the way.

#Platform #Engineering #Kubernetes #CloudNative
```

---

## 📅 04-03（周五）· Radar 卡 · Vault

**类型：** 单条推文
**发布状态：** ⬜

---

```
🔍 Cloud-Neutral Radar | HashiCorp Vault

Layer: Identity & Security — Secrets Management

One-line verdict:
Secrets don't belong in env vars, config files, or your head.
Vault puts them in one auditable place.

What it does:
→ Centralized secret storage (API keys, certs, DB passwords)
→ Dynamic secrets — generate credentials on-demand, auto-expire
→ Fine-grained access policies (who can read what, when)
→ Full audit log of every secret access
→ PKI, SSH, cloud IAM integration

✅ Strong fit:
– Multi-service environments with many credentials
– Teams that need audit trails for compliance
– Dynamic DB credentials (major security win)

⚠️ Real trade-offs:
– Operational complexity — Vault itself needs to be highly available
– Learning curve for policy model
– Self-managed Vault requires real ops maturity

The key boundary:
Vault doesn't secure your app.
It defines a clear engineering contract for how secrets move.

"The most dangerous secret is the one nobody knows is there."

#Security #Secrets #Vault #CloudNative #DevSecOps
```

---

## 📅 04-05（周日）· 观点 · Kubernetes 管理期望

**类型：** 单条推文（观点）
**发布状态：** ⬜

---

```
Kubernetes doesn't manage machines.
It doesn't manage containers.

It manages the gap between
what you said you wanted
and what's actually running.

That's the whole model.

You declare intent.
The control loop asks "how far are we from intent?" — forever.
When something breaks, it doesn't page you first.
It tries to fix it first.

This is why K8s feels hard to learn but hard to give up.

You're not learning a deployment tool.
You're learning to think in declared states
instead of executed steps.

That's a different mental model.
Not harder — different.

#Kubernetes #Platform #CloudNative #Engineering
```

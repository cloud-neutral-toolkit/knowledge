---
week: 11
dates: "2026-05-25 ~ 2026-05-31"
status: draft
---

# Week 11 发布内容

> 账号：@Cloud_Neutral · 发布后在 [x-publish-queue.md](./x-publish-queue.md) 更新状态

---

## 📅 05-25（周一）· Radar 卡 · Harvester

**发布状态：** ⬜

```
🔍 Cloud-Neutral Radar | SUSE Harvester

Layer: Platform Foundation — HCI / Virtualization on K8s

One-line verdict:
Hyperconverged infrastructure, K8s-native.
VMs and containers on the same platform, same API.

What it does:
→ KubeVirt-based: runs VMs as Kubernetes workloads
→ Longhorn storage built-in — distributed block storage
→ Rancher integration for multi-cluster management
→ Bare metal provisioning with PXE boot
→ Open-source, Apache 2.0

✅ Strong fit:
– Organizations migrating from VMware looking for OSS HCI
– On-prem environments needing both VMs and containers
– Edge deployments where a single platform manages compute
– Rancher-based platform teams

⚠️ Real trade-offs:
– Newer project — less battle-tested than VMware/Nutanix at enterprise scale
– SUSE ecosystem integration is strong, but standalone use has rougher edges
– Storage (Longhorn) has known limitations for very high IOPS workloads

The cloud-neutral angle:
Harvester + K8s = on-prem private cloud without vendor lock-in.
No vSphere license. No Nutanix contract. Just Linux, KVM, and Kubernetes.

#Harvester #HCI #Kubernetes #PrivateCloud #CloudNeutral #OpenSource
```

---

## 📅 05-27（周三）· Thread · 从 Solo Builder 到平台工程（7条）

**发布状态：** ⬜

**第 1 条：**
```
1/7 🧵

Platform engineering isn't about team size.

It starts the moment you ask:
"Why am I doing this the same way for the third time?"

Here's how the shift happens — from solo builder to platform thinking 👇

#Platform #DevOps #Engineering #SoloDev #CloudNative
```

**第 2 条：**
```
2/7

Stage 1: You build one thing.

Single app. Single deployment script. Single environment.
You hold all the context in your head.
This works. It should work. Don't over-engineer it.

The moment it stops working:
When you copy-paste the same setup for a second project.
```

**第 3 条：**
```
3/7

Stage 2: You notice repetition.

Same CI/CD pattern.
Same secrets management setup.
Same Terraform module structure.
Same monitoring config.

This is the platform signal.
Not "we need a platform team."
Just: "this should be a template, not a ritual."
```

**第 4 条：**
```
4/7

Stage 3: You extract the common layer.

Terraform modules for standard infra patterns.
Helm charts for standard deployment patterns.
Shared Argo CD app templates.
Reusable GitHub Actions workflows.

The platform isn't a product.
It's codified experience — your own accumulated knowledge
made reusable without re-explaining it.
```

**第 5 条：**
```
5/7

Stage 4: The platform becomes a contract.

"To deploy a new service, you fill in this template."
"Standard monitoring comes with the deployment. You don't configure it."
"Secrets management: here's the pattern."

The platform handles the 80% that's the same for every service.
The builder focuses on the 20% that's actually unique.
```

**第 6 条：**
```
6/7

What makes this cloud-neutral:

The platform contract shouldn't be defined by a vendor.
It should be defined by your engineering decisions.

K8s + Argo CD + Prometheus + Vault + PostgreSQL.
Each choice is replaceable. The contract remains.

When the platform is built on open standards,
migrating a component doesn't break the platform.
```

**第 7 条：**
```
7/7

The platform mindset shifts:

Before: "How do I deploy this app?"
After: "What should deploying any app look like?"

Before: "How do I monitor this service?"
After: "What's the monitoring contract for all services?"

This isn't about scale.
It's about moving from solving problems repeatedly
to building a system that solves them once.

#Platform #Engineering #CloudNeutral #DevOps #IaC
```

---

## 📅 05-29（周五）· Radar 卡 · KVM/QEMU

**发布状态：** ⬜

```
🔍 Cloud-Neutral Radar | KVM / QEMU

Layer: Platform Foundation — Virtualization

One-line verdict:
The virtualization layer under almost everything.
Not the tool you interact with — the one everything runs on.

What it does:
→ KVM: Linux kernel module, hardware-accelerated virtualization
→ QEMU: device emulation layer, works with KVM for near-native performance
→ Together: the foundation for most production hypervisors
→ libvirt: management API used by OpenStack, Proxmox, Harvester

✅ Strong fit:
– Foundation for any self-managed virtualization stack
– Private cloud IaaS (OpenStack, Proxmox, Harvester all use it)
– Container-in-VM security isolation (kata containers)
– Any environment where you own the hardware

⚠️ Real trade-offs:
– Not a product — requires management layer (libvirt, Harvester, Proxmox)
– Direct management via qemu-img / virsh requires expertise
– Not a replacement for K8s — different layer

The cloud-neutral angle:
Every major public cloud runs on hypervisors.
KVM/QEMU lets you run the same foundational layer on your own hardware.

Private cloud is not "running your own AWS."
It's choosing where your virtualization boundary lives.

#KVM #QEMU #Virtualization #PrivateCloud #CloudNeutral #Linux
```

---

## 📅 05-31（周日）· 观点 · 平台工程是复杂性归位

**发布状态：** ⬜

```
Platform engineering is not about building an internal cloud.

It's about one specific thing:
putting complexity where it belongs.

Every organization accumulates complexity.
The question is: who carries it?

Without platform thinking:
→ Every team figures out deployment independently
→ Every service has a different monitoring setup
→ Every engineer re-learns the same infrastructure patterns
→ Cognitive load grows with headcount

With platform thinking:
→ Common problems are solved once
→ Teams consume standard contracts, not re-invent them
→ The platform carries the infrastructure complexity
→ Engineers focus on product complexity

This isn't about tooling.
Argo CD, Terraform, Vault, Prometheus can all be part of it.
But the tools are just implementations of the model.

The model: move complexity to where it can be maintained centrally,
so that teams at the edges can operate with minimal cognitive overhead.

"Platform is the org's immune system for complexity."

#Platform #Engineering #DevOps #CloudNative #Architecture
```

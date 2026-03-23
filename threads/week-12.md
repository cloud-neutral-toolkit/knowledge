---
week: 12
dates: "2026-06-01 ~ 2026-06-07"
status: draft
---

# Week 12 发布内容

> 账号：@Cloud_Neutral · 发布后在 [x-publish-queue.md](./x-publish-queue.md) 更新状态

---

## 📅 06-01（周一）· Radar 卡 · Cosign

**发布状态：** ⬜

```
🔍 Cloud-Neutral Radar | Cosign (Sigstore)

Layer: Identity & Security — Supply Chain Trust

One-line verdict:
Signing container images used to require GPG expertise.
Cosign made it a one-line command.

What it does:
→ Signs container images and artifacts with private keys or keyless flow
→ Keyless signing: uses OIDC identity (GitHub Actions, Google, etc.) — no key management
→ Transparency log (Rekor): public, tamper-evident record of signatures
→ Integrates with OPA/Gatekeeper for K8s admission policy
→ Part of Sigstore project — Linux Foundation

✅ Strong fit:
– CI/CD pipelines: sign on build, verify on deploy
– K8s admission control: block unsigned images from running
– Supply chain compliance (SLSA framework adoption)
– Teams concerned about image tampering in registries

⚠️ Real trade-offs:
– Keyless flow requires OIDC setup
– Admission controller integration adds deployment complexity
– Still maturing in enterprise adoption

The key insight:
An unsigned container image is a promise without a signature.
You're trusting the registry, not the builder.

Cosign answers: "Did this image come from where I think it came from?"

#Cosign #Sigstore #SupplyChain #DevSecOps #Kubernetes #CloudNative
```

---

## 📅 06-03（周三）· Thread · Cloud-Neutral 工具图谱总览（6条）

**发布状态：** ⬜

**第 1 条：**
```
1/6 🧵

12 weeks. 24 Radar cards. 8 Threads.

Here's the full Cloud-Neutral infrastructure map —
the tools that let you build without being owned by a vendor.

The complete architecture 👇

#CloudNeutral #CloudNative #Architecture #Platform #DevOps
```

**第 2 条：**
```
2/6

Layer 1: Identity & Security

The first thing that gets locked in is often identity.

→ Keycloak / ZITADEL — auth & SSO (open, portable)
→ Vault — secrets management (no hardcoded credentials)
→ Cosign / Trivy — supply chain security
→ SPIFFE/SPIRE — workload identity (zero-trust)
→ Dex — OIDC federation

If your identity stack is a vendor SaaS:
you don't own the key to your own system.
```

**第 3 条：**
```
3/6

Layer 2: IaC & Delivery

How changes reach production defines how fast you can move.

→ Terraform / OpenTofu — infra state as code
→ Pulumi — infra as real code
→ Argo CD / FluxCD — GitOps delivery
→ Ansible — configuration management
→ Teleport — secure access to infra (audited, cloud-neutral)

The principle: every change should be reviewable, reversible, and traceable.
```

**第 4 条：**
```
4/6

Layer 3: Runtime & Boundary

Where your workloads actually run.

→ Kubernetes — the orchestration standard
→ containerd — the runtime
→ Cilium / Calico — network policy (eBPF / traditional)
→ APISIX / Nginx — API gateway / reverse proxy
→ k3s / k3k — lightweight K8s for edge and platform

The principle: workloads should be portable.
The infra layer should be replaceable.
```

**第 5 条：**
```
5/6

Layer 4: Observability

You can't fix what you can't see.

→ OpenTelemetry — instrumentation standard (vendor-agnostic)
→ Prometheus — metrics collection
→ VictoriaMetrics — long-term storage at scale
→ Grafana — visualization
→ Loki / Vector / VictoriaLogs — log aggregation

The principle: observability data shouldn't be locked in a SaaS.
You should own the pipelines and the storage.
```

**第 6 条：**
```
6/6

Layer 5: Data & AI

The data layer is where lock-in is most dangerous.

→ PostgreSQL (+ extensions) — the data anchor
→ ClickHouse — real-time analytics
→ DuckDB — embedded analytics
→ Milvus / Qdrant — vector search
→ Apache Flink — stream processing

Cloud-neutral principle applied to data:
Your database should run on your terms.
Not on a cloud provider's pricing model.

---

The full stack is documented at:
github.com/cloud-neutral-

#CloudNeutral #Architecture #Platform #Engineering
```

---

## 📅 06-05（周五）· Radar 卡 · SPIFFE/SPIRE

**发布状态：** ⬜

```
🔍 Cloud-Neutral Radar | SPIFFE / SPIRE

Layer: Identity & Security — Workload Identity

One-line verdict:
Every service needs to prove who it is.
SPIFFE defines the standard. SPIRE implements it.

What it does:
→ SPIFFE: open standard for service identity (SVID = X.509 cert)
→ SPIRE: production implementation of SPIFFE
→ Automatically issues and rotates short-lived certificates
→ Works across cloud, on-prem, and hybrid environments
→ Kubernetes-native + multi-platform support

✅ Strong fit:
– Zero-trust architectures (mTLS between every service)
– Multi-cloud / hybrid environments needing consistent identity
– Replacing static credentials with rotating certificates
– Service mesh foundation (Istio, Envoy, Linkerd can use SPIFFE)

⚠️ Real trade-offs:
– Complex to operate and tune
– Requires PKI understanding
– Overkill for small, single-environment deployments

The problem it solves:
In a distributed system, how does Service A prove to Service B
that it's actually Service A — and not an attacker?

IP address: not reliable (dynamic, spoofable)
Shared secret: needs rotation, gets leaked
SPIFFE: short-lived, cryptographically verifiable, automatically rotated

"Zero trust starts with workload identity."

#SPIFFE #SPIRE #ZeroTrust #Security #CloudNative #mTLS
```

---

## 📅 06-07（周日）· 观点 · 12 周之后，什么没变

**发布状态：** ⬜

```
12 weeks of cloud-neutral infrastructure content.
24 Radar cards. 8 Threads.

Here's what didn't change in any of it:

→ The principles hold, not the tools.

Kubernetes may be replaced.
Prometheus may be superseded.
Terraform may give way to something better.

But the principles:
– Declare intent, let systems reconcile.
– Own your data. Own your identity. Own your secrets.
– Avoid lock-in not because vendors are evil,
  but because flexibility is cheaper to build upfront.
– Complexity doesn't disappear — it moves.
  Your job is to put it where you can manage it.

→ The question isn't "which tool."

The question is: which decisions are reversible,
and which ones compound into constraints?

Cloud-neutral isn't a tech choice.
It's a posture: stay movable, stay auditable, stay in control.

Thanks for following along.
The backlog has more.

#CloudNeutral #Engineering #Architecture #Platform #DevOps
```

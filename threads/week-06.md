---
week: 6
dates: "2026-04-20 ~ 2026-04-26"
status: draft
---

# Week 06 发布内容

> 账号：@Cloud_Neutral · 发布后在 [x-publish-queue.md](./x-publish-queue.md) 更新状态

---

## 📅 04-20（周一）· Radar 卡 · FluxCD

**发布状态：** ⬜

```
🔍 Cloud-Neutral Radar | FluxCD

Layer: IaC & Delivery — GitOps (Pull-based)

One-line verdict:
GitOps without the UI.
Pure operator model — Git is truth, cluster pulls toward it.

What it does:
→ Watches Git repos / Helm registries / OCI artifacts
→ Automatic reconciliation — no push pipelines needed
→ Kustomize + Helm native support
→ Multi-tenancy via GitRepository isolation
→ CNCF graduated — production stable

✅ Strong fit:
– Teams preferring operator-pattern over centralized control plane
– Multi-tenant platform engineering
– Integration-first workflows (pairs well with Terraform, Crossplane)

⚠️ Real trade-offs:
– No built-in UI (vs. Argo CD's dashboard)
– Steeper initial configuration vs. Argo CD
– Debugging reconciliation failures requires CLI fluency

FluxCD vs Argo CD:
Not better or worse — different philosophy.
Flux: distributed operator model. Argo: centralized control.

The question: do you want a dashboard or do you want operators all the way down?

#FluxCD #GitOps #Kubernetes #CloudNative #DevOps
```

---

## 📅 04-22（周三）· Thread · VictoriaMetrics vs Prometheus（7条）

**发布状态：** ⬜

**第 1 条：**
```
1/7 🧵

Prometheus is the metrics standard.
VictoriaMetrics is what you run when Prometheus runs out of road.

Here's the honest comparison for production teams 👇

#Prometheus #VictoriaMetrics #Observability #CloudNative
```

**第 2 条：**
```
2/7

Why Prometheus hits limits:

→ Single-node storage — horizontal scaling requires Thanos/Cortex/Mimir
→ Long-term retention gets expensive fast
→ High-cardinality metrics cause memory spikes
→ Federation at scale is operationally complex

None of these are bugs. Prometheus was designed for a different scope.
When you outgrow it, you need to know where to go.
```

**第 3 条：**
```
3/7

VictoriaMetrics: what changes

✅ 5-10x better compression (same data, fraction of disk)
✅ Handles high-cardinality metrics without OOM
✅ Horizontal scaling built in (VM cluster mode)
✅ PromQL compatible — no migration of dashboards/alerts
✅ Single binary for small deployments — simpler than Prometheus + Thanos
```

**第 4 条：**
```
4/7

What stays the same:

Both are open-source.
Both are cloud-neutral — deploy anywhere.
Both speak PromQL (VM has MetricsQL extension).
Both integrate with Grafana natively.

VictoriaMetrics doesn't replace your Prometheus ecosystem.
It replaces the Prometheus storage layer.
```

**第 5 条：**
```
5/7

When to stay on Prometheus:

→ You're below ~500k active time series
→ You don't need long-term retention (30d+ gets expensive)
→ Your team already knows Prometheus well
→ You're running it alongside Thanos and it's working

Don't migrate because VictoriaMetrics is "better."
Migrate when Prometheus is costing you real ops time.
```

**第 6 条：**
```
6/7

When to switch to VictoriaMetrics:

→ Prometheus OOM at high cardinality
→ Long-term retention (90d+) is eating storage budget
→ Multi-cluster metrics aggregation needed
→ You want simpler ops (one VM cluster vs. Prometheus + Thanos + Cortex)

The migration path is clean: VM accepts remote_write from Prometheus.
You can run both in parallel during transition.
```

**第 7 条：**
```
7/7

Bottom line:

Prometheus: instrument everything against the standard
VictoriaMetrics: store and query at scale

They're not competitors. They're complements.

The cloud-neutral observability stack:
→ OpenTelemetry (instrumentation)
→ Prometheus (collection + short-term)
→ VictoriaMetrics (long-term, high-scale storage)
→ Grafana (visualization)

None of them require a vendor. All of them interoperate.

#Observability #VictoriaMetrics #Prometheus #CloudNeutral #SRE
```

---

## 📅 04-24（周五）· Radar 卡 · containerd

**发布状态：** ⬜

```
🔍 Cloud-Neutral Radar | containerd

Layer: Runtime & Boundary — Container Runtime

One-line verdict:
The container runtime that runs your containers.
Not the one you think about — the one that actually does the work.

What it does:
→ Pulls images, manages storage, runs containers
→ CRI (Container Runtime Interface) compliant — K8s talks to it directly
→ OCI-standard image format support
→ Snapshotters, plugins, namespace isolation
→ CNCF graduated — used in almost every K8s distribution

✅ Strong fit:
– Default choice for K8s production deployments
– Teams moving away from Docker-as-runtime (Docker ≠ containerd)
– Stable, minimal surface area runtime

⚠️ Real trade-offs:
– Not user-facing — most engineers never interact with it directly
– Debugging at runtime level requires crictl/ctr
– Image build is not its job (use BuildKit, Kaniko, etc.)

The important distinction:
Docker = developer toolchain (build + run + push)
containerd = production runtime (run only)

Kubernetes deprecated Dockershim because it needed
a direct CRI implementation. containerd is that.

#containerd #Kubernetes #ContainerRuntime #CloudNative #CNCF
```

---

## 📅 04-26（周日）· 观点 · 开源是工程决策

**发布状态：** ⬜

```
Open source isn't a philosophy.
It's an engineering decision.

Here's the actual trade:

You get:
→ No vendor lock-in on the data layer
→ Full control over upgrade timing
→ Ability to patch, fork, contribute
→ Community that outlasts any single company

You give:
→ Ops responsibility (you run it)
→ Support responsibility (you fix it)
→ Engineering time (you maintain it)

The question isn't "open source vs. SaaS."
The question is: which dependencies are you willing to own?

For database, identity, observability, and delivery infrastructure —
owning makes sense. The vendor alternative is a structural dependency.

For payment processing, email deliverability, fraud detection —
SaaS makes sense. Building those is not your competitive advantage.

Know the difference. Choose deliberately.

#CloudNeutral #OpenSource #Engineering #Architecture
```

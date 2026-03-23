---
week: 5
dates: "2026-04-13 ~ 2026-04-19"
status: draft
---

# Week 05 发布内容

> 账号：@Cloud_Neutral · 发布后在 [x-publish-queue.md](./x-publish-queue.md) 更新状态

---

## 📅 04-13（周一）· Radar 卡 · ZITADEL

**发布状态：** ⬜

```
🔍 Cloud-Neutral Radar | ZITADEL

Layer: Identity & Security — AuthN/AuthZ Platform

One-line verdict:
Keycloak for teams who want modern DevX
without the XML configuration archaeology.

What it does:
→ OIDC / OAuth2 / SAML identity provider
→ Built-in multi-tenancy (organizations)
→ Fine-grained RBAC + custom roles
→ Machine-to-machine auth with service accounts
→ Audit log on every identity event

✅ Strong fit:
– B2B SaaS products needing org-level identity
– Teams building auth from scratch (vs. inheriting Keycloak)
– Cloud-neutral identity that runs anywhere

⚠️ Real trade-offs:
– Smaller ecosystem than Keycloak for enterprise integrations
– Less battle-hardened at extreme scale
– Community edition has feature limits vs. Cloud

The comparison:
Keycloak: proven, powerful, steep ops overhead
ZITADEL: modern API-first, better DevX, growing adoption

"The auth system you don't control will eventually control you."

#Identity #ZITADEL #Auth #CloudNative #Security
```

---

## 📅 04-15（周三）· Thread · ZITADEL vs Keycloak 选型（6条）

**发布状态：** ⬜

**第 1 条：**
```
1/6 🧵

Identity is the one system you can't easily replace.

Keycloak or ZITADEL?
Both are open-source. Both are cloud-neutral.
The answer depends on what you're building.

Here's the honest comparison 👇

#Identity #Auth #OpenSource #CloudNative
```

**第 2 条：**
```
2/6

Keycloak — The battle-hardened enterprise choice

✅ 10+ years of production use
✅ Massive ecosystem (LDAP, SAML, every enterprise protocol)
✅ Huge community, extensive docs

⚠️ Painful XML/UI configuration
⚠️ Heavy JVM footprint
⚠️ Multi-tenancy is an afterthought, not a first-class feature
```

**第 3 条：**
```
3/6

ZITADEL — The modern API-first challenger

✅ Multi-tenancy built in (organizations as first-class concept)
✅ Clean Go codebase, lower resource footprint
✅ API-first design — everything is automatable
✅ Better developer experience out of the box

⚠️ Smaller enterprise ecosystem
⚠️ Less battle-tested at Keycloak scale
⚠️ Some enterprise features require paid tier
```

**第 4 条：**
```
4/6

The real decision matrix:

Building a B2B SaaS product?
→ ZITADEL (orgs are core, not bolted on)

Replacing an existing enterprise SSO?
→ Keycloak (protocol support breadth wins)

Greenfield, you control the stack?
→ ZITADEL (developer velocity matters more early)

Legacy LDAP/AD integration required?
→ Keycloak (hands down)
```

**第 5 条：**
```
5/6

Both choices share one property: cloud-neutral.

Neither locks you to AWS Cognito, Azure AD, or Okta.
Both run on your infrastructure.
Both support OIDC/OAuth2 — the open standard.

The identity system is where lock-in is most invisible.
Choosing open-source here is an architectural decision,
not just a cost decision.
```

**第 6 条：**
```
6/6

Bottom line:

If you're starting new → ZITADEL
If you're enterprise/legacy → Keycloak
If you're already on Keycloak → stay unless pain is real

The worst outcome: choosing the managed SaaS option
because "auth is hard."

Auth IS hard. That's why owning it matters.

#Identity #ZITADEL #Keycloak #Auth #CloudNeutral
```

---

## 📅 04-17（周五）· Radar 卡 · Grafana

**发布状态：** ⬜

```
🔍 Cloud-Neutral Radar | Grafana

Layer: Observability — Visualization & Dashboarding

One-line verdict:
The visualization layer for every observability backend.
Not a database — a window into whatever you're running.

What it does:
→ Unified dashboards across Prometheus, Loki, Tempo, and 50+ sources
→ Alerting with notification routing
→ Explore mode — ad-hoc metric/log/trace investigation
→ Plugin ecosystem: new data sources without vendor lock-in

✅ Strong fit:
– Observability stacks with multiple backends (Prometheus + Loki + Tempo)
– Teams that need one UI across cloud and on-prem data
– Anyone who's outgrown vendor dashboards

⚠️ Real trade-offs:
– Dashboard management at scale needs discipline (too easy to have 200 unused dashboards)
– Enterprise features (RBAC, SSO) require paid Grafana Enterprise or Cloud
– Not a replacement for proper alerting infrastructure

The key insight:
Grafana doesn't care where your data lives.
That's what makes it cloud-neutral by design.

#Grafana #Observability #CloudNative #Monitoring #OpenSource
```

---

## 📅 04-19（周日）· 观点 · 身份系统锁死

**发布状态：** ⬜

```
The auth system you don't own
will eventually make decisions for you.

Not dramatically. Just quietly:

→ Price increase at renewal
→ Feature gated behind "enterprise"
→ API changed with 90 days notice
→ Your compliance team suddenly needs a feature that doesn't exist

Identity is the one dependency that touches everything.

Every user. Every service. Every API call.

If your identity layer is a managed SaaS you don't control —
that's not a vendor relationship.
That's a structural dependency.

Open-source identity (Keycloak, ZITADEL, Dex) isn't paranoia.
It's the same logic as owning your database.

#CloudNeutral #Identity #Auth #Architecture #OpenSource
```

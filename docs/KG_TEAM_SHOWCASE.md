# Rackspace Enterprise Knowledge Graph: Team Showcase

**CDAIO Data & AI Engineering**
**Date: March 2026**
**Audience: All CDAIO team members**

---

## Why This Document Exists

Over the past two weeks, we enriched the Rackspace Enterprise Knowledge Graph from a sparse starting point into a structured, queryable map of our enterprise — systems, data assets, regulations, risks, controls, people, and the relationships between all of them.

This document explains:
- What the KG is and why we built it this way
- What we actually did and how
- What you can ask it right now
- What it enables for our data & AI strategy
- How to contribute your own domain knowledge

This is not a finished product. It is a foundation — and its value compounds every time someone on this team adds to it.

---

## The Problem We Were Solving

### Before Enrichment: Relationship Deserts

The KG existed but was largely disconnected. It had entities (systems, data assets, controls) but almost no relationships between them. Specifically:

| Relationship Type | Before | After |
|---|---|---|
| `stores` (system → data asset) | 1 | 157 |
| `hosted_on` (system → site) | 1 | 490 |
| `integrates_with` (system → system) | 1 | 101 |
| `mitigates` (control → risk) | 25 | 29 |

A graph with entities but no edges is just a list. You can't reason over a list. You can't ask "which systems store PII?" or "what controls mitigate our cloud infrastructure risks?" without the edges.

Separately, the entity data itself was sparse — systems existed as IDs with a name and almost nothing else. Data assets had no classification, no regulatory mapping, no storage technology, no lineage.

### The Strategic Stakes

We are building toward a data & AI strategy. That strategy requires a ground-truth map of:
- What data we have and where it lives
- What systems process it
- What regulations apply to it
- What risks it creates
- What controls address those risks

Without that map, any AI model we build for data governance, compliance, or security has no foundation to reason from. The KG is that foundation.

---

## What We Built: The Numbers

```
Total Entities:       2,949
Total Relationships:  7,011
Entity Types:         26
Relationship Types:   42
Graph Density:        0.00081
Systems Cataloged:    164
Data Assets:          164
```

### Entity Breakdown (selected)
- **340 controls** mapped to risks and systems
- **164 systems** with OSINT-validated attributes
- **164 data assets** with classification, regulatory scope, lineage, and storage mapping
- **114 policies** linked to systems and data assets
- **70 regulations** mapped across jurisdictions
- **22 risks** with control mappings
- **378 integrations** documented

---

## How We Enriched It: The Methodology

### Principle 1: One Entity at a Time, With Reasoning

We did not run bulk imports or make mass changes. Every relationship and attribute was added individually, with:
- **Rationale**: why this relationship is logical
- **Assumption**: what we assumed vs. confirmed
- **Confidence**: a score between 0.0 and 1.0
- **Attestation status**: "KG-Analysis-Inferred" for inferred, blank for confirmed

This means every inferred edge in the graph is traceable — you can read exactly why it was added and how confident we were.

Example attestation on a relationship:
```json
{
  "attestation": "KG-Analysis-Inferred",
  "review_required": true,
  "confidence": 0.72,
  "rationale": "Power BI is a Microsoft cloud service within the M365 ecosystem...",
  "assumption": "Power BI Service is included within the Rackspace Microsoft 365 enterprise agreement",
  "inferred_date": "2026-03-02"
}
```

### Principle 2: Confidence Tiers

| Tier | Confidence | Source |
|---|---|---|
| T1–T2 | 0.90–1.00 | Official documentation, confirmed architecture |
| T3–T4 | 0.80–0.89 | OSINT (job postings, vendor pages, GitHub) + inference |
| T5–T6 | 0.70–0.79 | Architectural inference from known patterns |
| T7–T8 | 0.60–0.69 | Domain inference with documented assumptions |
| T9–T10 | 0.55–0.59 | Minimum threshold — speculative but documented |

Anything below T9 (< 0.55 confidence) was not added.

### Principle 3: No Schema Changes

We never modified the data structure of existing entities — only added new relationships between existing entities, and populated fields already defined in the schema. This kept every change reversible and non-destructive.

### Principle 4: OSINT-First for Systems

For system enrichment, we used open-source intelligence:
- Rackspace job postings (Lever ATS) — revealed internal tooling
- GitHub repositories (rackerlabs org) — confirmed architecture decisions
- Vendor documentation and announcements
- RADB AS-SET analysis for network topology
- Rackspace blog and press releases

Each source was documented in sprint ledgers with its confidence contribution.

---

## What We Did: Sprint by Sprint

### Phase 1: System Entity Enrichment (Sprint 0–6)
**Feb 24–28, 2026 | Starting: 62 systems → Final: 164 systems**

Six sprints, each targeting a specific domain:

| Sprint | Domain | Systems Added | Key Finds |
|---|---|---|---|
| 0 | Baseline audit | 0 | Added descriptions to all 62 existing systems |
| 1 | Security & IAM | 16 | CrowdStrike, SailPoint, BeyondTrust, RSA, Palo Alto |
| 2 | Kubernetes & DevOps | 15 | Argo, Helm, cert-manager, GitHub Actions, Harbor |
| 3 | Corporate IT & Finance | 13 | Workday, Lever, ServiceNow, Jira, Billing & Revenue |
| 4 | Platform & Observability | 16 | Datadog, Watchman, VMware NSX, Fluent Bit, DriveClient |
| 5 | OpenStack & AI/ML | 20 | Ceilometer, CloudKitty, Blazar, Run:AI, ICE, RITA |
| 6 | Audit & Consolidation | net +4 | Removed 17 duplicates, 7 unverifiable entities; added Sentinel, MetalLB |

**Sprint 4 is notable**: the first pass was rejected because it used only 2 OSINT sources. The redo used 24 sources and produced entities with 3x higher confidence and specificity.

### Phase 2: Data Asset Enrichment
**Feb 26–28, 2026 | 123 assets → 164 assets**

- **41 new data assets discovered** across 5 tiers:
  - Tier A: Genestack/OpenStack databases (Keystone, Nova, Neutron, etc.)
  - Tier B: Kubernetes infrastructure (etcd, cert-manager TLS, Argo Workflows)
  - Tier C: Observability (OpenSearch logs, Prometheus metrics, Grafana state)
  - Tier D: AI/ML (GPU workload stores, model registries)
  - Tier E: Business analytics (Snowflake, Power BI, NPS/CSAT, Salesforce)

- **164/164 assets at 100% schema coverage** — every field defined in the schema populated
- **Average completeness: 57%** — the remaining 43% represents fields that require runtime access (actual DB size, backup test dates, current user counts) — these are documented as known gaps, not missing data

- **7 critical security gaps flagged** during enrichment:
  - etcd encryption-at-rest unconfirmed (if disabled: all K8s Secrets are plaintext)
  - Memcached Cluster has no encryption
  - Confluence labeling and DLP not configured
  - 4 additional gaps documented with remediation plans

### Phase 3: Relationship Desert Remediation
**Mar 1, 2026 | 3 passes across the full graph**

| Pass | Relationship | Added | Method |
|---|---|---|---|
| 1 | `stores` | 124 | Name/description/format inference matching data assets to systems |
| 2 | `hosted_on` | 490 | All 164 systems mapped to hosting sites; SaaS systems to cloud sites |
| 3 | `integrates_with` | 101 | Directional system-to-system integration flows with data_flow metadata |

This phase transformed the graph from a set of isolated clusters into a connected topology.

---

## What You Can Ask It Right Now

The KG is queryable through MCP tools integrated into Claude Desktop. Here are real questions it can answer today:

### Security & Compliance
```
"Which data assets contain PII and are stored unencrypted?"
"What controls mitigate our cloud infrastructure risk?"
"Which systems are FedRAMP in-scope?"
"What data assets cross EU borders and what transfer mechanisms apply?"
```

### Architecture & Dependency Mapping
```
"What systems does Kubernetes (sys-085) store data assets for?"
"What integrates with Salesforce?"
"Which systems are hosted at site-001 (cloud)?"
"Show me the blast radius if MariaDB Galera goes down"
```

### Data Governance
```
"Which data assets have no backup documented?"
"What data assets are classified as restricted?"
"Which assets are subject to GDPR?"
"What systems have no data assets linked to them?"
```

### Risk & Control
```
"Which risks have zero controls mitigating them?"
"What controls apply to our PCI-scoped systems?"
"Which systems are internet-facing with no control mapped?"
```

### Quick Query Example
To run any of these via Claude Desktop, the MCP server is already connected as `hc-enterprise-kg`. Just ask Claude naturally — the tools resolve against the graph automatically.

---

## Opportunities: What This Enables

### 1. Data & AI Strategy Foundation
The KG is a machine-readable map of our enterprise. This is the prerequisite for:
- **AI-assisted compliance monitoring** — an agent that continuously checks whether new systems are mapped to their regulations
- **Automated risk propagation** — when a new vulnerability is disclosed, trace which systems and data assets are affected automatically
- **Data lineage tracking** — understand where data flows from source to consumption
- **FedRAMP readiness acceleration** — the graph already maps which systems and data assets are in-scope

### 2. Security Posture Intelligence
With 164 systems, 340 controls, and 22 risks all connected, we can now ask:
- Where are our control gaps? (10 risks currently have zero control mitigations)
- Which systems are high-criticality but have no incident history documented?
- Where is our attack surface widest?

### 3. Data Catalog Bootstrapping
The 164 enriched data assets are the starting inventory for a formal data catalog. Every asset has:
- Classification (restricted / confidential / internal)
- Regulatory applicability (GDPR, CCPA, FedRAMP, HIPAA, SOC 2)
- Storage technology and system linkage
- Known gaps with remediation plans

This is the foundation that would otherwise take months to build from scratch.

### 4. Organizational Intelligence
With 250 departments, 427 roles, 100 people, and 109 organizational units connected to systems and capabilities, the graph can answer organizational questions:
- Which team owns which system?
- Who are the data stewards for restricted assets?
- Which capabilities depend on systems that have no documented owner?

---

## How to Contribute Your Domain Knowledge

The KG's value is proportional to the accuracy and completeness of its data. You are the ground truth. Here's how to participate:

### Option 1: Attest or Correct Existing Entities
If you know that an inferred relationship is wrong, or that a `review_required: true` edge needs to be validated, you can:
1. Query the entity via Claude Desktop
2. Note the relationship ID
3. Flag it in a PR with your correction and rationale

### Option 2: Add Missing Relationships
If you know that System X integrates with System Y — and it's not in the graph — that's a contribution. Every relationship needs:
- Source entity ID
- Target entity ID
- Relationship type (from the 42 available types)
- Your confidence level and rationale

### Option 3: Populate Known Gaps
Every data asset has a `known_data_gaps` array documenting fields that need runtime access to populate. If you have access to the actual system, you can fill in:
- Backup test dates
- Actual database sizes
- Current user counts
- Encryption configuration confirmations

### Option 4: Add Your Domain's Systems and Data
If your team owns systems or data assets not yet in the graph, the process is:
1. Add the entity via the MCP `add_entity_tool`
2. Link it to its hosting site, owning team, and data assets
3. Push via `scripts/kg-push.sh`

The sync daemon handles the rest — changes propagate to the graph automatically.

### Git Workflow
```bash
# All changes go through the per-type files, not graph.json directly
# graph.json is rebuilt automatically from:
entities/<type>.json
relationships/<type>.json

# To push changes:
./scripts/kg-push.sh "feat(kg): add [your change description]"
```

---

## What Remains: Known Gaps

These are the documented gaps we know about, in priority order:

| Priority | Gap | Impact |
|---|---|---|
| Critical | etcd encryption-at-rest unconfirmed | All K8s Secrets potentially plaintext |
| High | 10 risks with zero control mitigations | Control coverage blindspot |
| High | AI/GenAI data assets not linked to bc-024 (AI capability) | AI strategy visibility gap |
| High | FedRAMP data assets not fully mapped to bc-036 | FedRAMP readiness gap |
| Medium | Data asset provenance attestation null across most assets | Audit trail gap |
| Medium | Nautobot, OpenSearch, Power BI need dedicated system entities | Accuracy of 3 proxy relationships |
| Low | Average completeness at 57% | Runtime-dependent fields awaiting measurement |

---

## What "Good" Looks Like Going Forward

The goal is not a perfectly complete KG — that's not achievable in a live enterprise. The goal is a **continuously maintained, trustworthy graph** that reflects how the organization actually operates.

**Short-term (Q1 2026):**
- Resolve the 10 risks with zero control mappings
- Attest or correct the `review_required: true` relationships
- Add AI/GenAI data asset linkages for the AI strategy

**Medium-term (Q2–Q3 2026):**
- Implement the data catalog on top of the KG data asset inventory
- Build the first AI agent that queries the graph for compliance gap analysis
- Achieve `is_weakly_connected: true` across the full graph

**Long-term:**
- The KG becomes the authoritative source of truth for data & AI governance decisions
- New systems and data assets are registered at inception, not retrospectively
- Policy, risk, and control changes propagate automatically through the graph

---

## How to Get Started Right Now

1. **Open Claude Desktop** — the `hc-enterprise-kg` MCP server is already configured
2. **Ask a question** — try: *"What data assets are classified as restricted and stored in systems with no encryption?"*
3. **Explore an entity** — try: *"Tell me about sys-085 and everything connected to it"*
4. **Try the blast radius tool** — try: *"What's the blast radius of the MariaDB Galera cluster going down?"*

If you find something wrong, something missing, or something that surprises you — that's valuable signal. Document it and we'll add it.

---

*This document was produced from the enrichment sprint ledgers, cowork session outputs, and the KG_ENRICHMENT_NARRATIVE.md. For the full technical record of decisions made during enrichment, see `docs/KG_ENRICHMENT_NARRATIVE.md`.*

*Questions: reach out to the CDAIO Data & AI Engineering team.*

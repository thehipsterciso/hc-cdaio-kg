# hc-cdaio-kg

**An AI-native enterprise knowledge graph built by the Carnegie Mellon Heinz College Chief Data & AI Officer (CDAIO) program.**

This repository contains a production-grade organizational digital twin — 2,900+ entities and 6,000+ relationships — constructed entirely from public sources using AI-augmented OSINT methodology. It demonstrates that institutional-quality enterprise analysis, historically locked behind six-figure consulting engagements, can be produced transparently, reproducibly, and at a fraction of the cost when humans and AI systems work as peers.

## Why This Matters

Enterprise due diligence has been a black box for decades. A handful of advisory firms charge $250K–$1M to produce opaque reports that boards and investment committees accept on faith. The methodology is proprietary. The evidence chains are buried. The analysis is rarely reproducible.

This project inverts that model:

- **Every claim is traceable.** 401 structured analysis documents with explicit evidence sources, confidence ratings, and claim classifications (FACT / INFERENCE / HYPOTHESIS).
- **Every entity is auditable.** 2,900+ entities across 26 types with provenance metadata linking back to SEC filings, regulatory disclosures, DNS records, BGP tables, and public documentation.
- **Every relationship is defensible.** 6,000+ typed relationships with confidence scores and human-readable descriptions.
- **The methodology is open.** The analytical framework (10-stage due diligence constitution), the quality gates, the OSINT research ledgers — all published. Anyone can audit, reproduce, or extend.

This is what enterprise intelligence looks like when you stop gatekeeping it.

## What's in This Repository

### Knowledge Graph (`entities/` + `relationships/`)

The organizational digital twin — structured, typed, and relationship-mapped:

| Layer | Entity Types | Count | Coverage |
|-------|-------------|-------|----------|
| L00 Geography | geography, jurisdiction, location, site | 223 | Global operations footprint |
| L01 Governance | control, policy, regulation | 524 | Compliance and regulatory landscape |
| L02 Technology | system, network, integration | 636 | Technology estate and dependencies |
| L03 Data | data_asset, data_domain | 211 | Information architecture |
| L04 Organization | department, organizational_unit, role | 786 | Organizational structure |
| L05 People | person | 100 | Leadership and key personnel |
| L06 Capabilities | business_capability | 64 | Business capability map |
| L07 Contracts | contract | 37 | Contractual obligations |
| L08 Products | product, product_portfolio, market_segment | 130 | Product and market positioning |
| L09 Customers | customer | 85 | Customer base |
| L10 Vendors | vendor | 60 | Supply chain and partnerships |

**Relationship types:** 39 types including `depends_on`, `subject_to`, `located_in`, `managed_by`, `enforces`, `implements`, `supports`, `connects_to`, and 31 others.

### Due Diligence Analysis (`due-diligence/`)

401 structured JSON documents across 10 analytical stages — the full evidentiary foundation:

| Stage | Focus | Substages |
|-------|-------|-----------|
| **0** Diligence Governance | Epistemic standards, evidence hierarchy, claim classification | Constitution |
| **1** Corporate & Legal | Legal existence, ownership/control, structural debt, change-of-control, jurisdictional locks | 1.1–1.5 |
| **2** Business Model | Revenue engine, cost/margin physics, value flow, customer segmentation, partner dependency, contradictions | 2.1–2.6 |
| **3** Market & Competition | Market structure, competitive threats, buying behavior, pricing dynamics, platform dependency, shock sensitivity | 3.1–3.6 |
| **4** Operating Model | Decision rights, operating cadence, cross-functional bottlenecks, incentive misalignment, talent constraints | 4.1–4.5 |
| **5** Financial Reality | Revenue quality, margin reality, liquidity runway, debt/covenants, capital allocation, financial contradictions | 5.1–5.6 |
| **6** Technology & Platform | Compute/DC control, hyperscaler dependency, platform fragility, vendor lock-in, technical debt, estate coherence | 6.1–6.6 |
| **7** Data & Information | Data domains, lineage/drift, quality, stewardship, access/privilege, flow latency, epistemic coherence | 7.1–7.7 |
| **8** Risk & Security | Cybersecurity posture, privacy/data rights, regulatory enforcement, data sovereignty, governance power | 8.1–8.5 |
| **9** Resilience & Continuity | ESG materiality, failure sequencing, workforce fragility, ecosystem shock propagation, insurance/risk transfer | 9.1–9.5 |

Each stage includes **validation gates** with pass/fail criteria, contradiction analysis, and uncertainty registers.

### Research Ledgers (`docs/ledgers/`)

Session-by-session OSINT research logs documenting methodology, confidence tiers (T1–T4), source attribution, and analytical decision-making. These provide the audit trail for how raw intelligence was transformed into structured knowledge.

## Architecture

```
hc-cdaio-kg/
├── entities/                  # 26 per-type entity files (JSON arrays)
├── relationships/             # 39 per-type relationship files (JSON arrays)
├── due-diligence/             # 10-stage structured analysis (401 JSON documents)
│   ├── stage-0-diligence-governance/
│   ├── stage-1-corporate-legal-structural/
│   ├── stage-2-business-model-economics/
│   ├── stage-3-market-competitive-force/
│   ├── stage-4-operating-model-execution/
│   ├── stage-5-financial-capital-stress/
│   ├── stage-6-technology-platform/
│   ├── stage-7-data-information-epistemic/
│   ├── stage-8-risk-security-regulatory/
│   └── stage-9-resilience-esg-continuity/
├── docs/
│   ├── ledgers/               # OSINT research session logs
│   └── QUALITY_INFRASTRUCTURE.md
├── scripts/
│   ├── lib/                   # kg-build.py, kg-split.py, kg-merge.py
│   ├── kg-morning.sh          # Daily pull + rebuild (8 AM)
│   ├── kg-sync.sh             # Auto-sync every 30 min
│   └── kg-eod.sh              # End-of-day PR creation (5 PM)
└── graph.json                 # Assembled locally (gitignored)
```

## How It Works

The knowledge graph is maintained as **per-type JSON files** — one file per entity type, one file per relationship type. This prevents merge conflicts when multiple analysts work in parallel on different entity types.

Three shell scripts automate the daily workflow:

| Time | Script | Action |
|------|--------|--------|
| 8:00 AM | `kg-morning.sh` | Pull main, rebuild `graph.json`, reload MCP server |
| Every 30 min | `kg-sync.sh` | Split graph into per-type files, commit, push |
| 5:00 PM | `kg-eod.sh` | Final sync + open PR to main |

The assembled `graph.json` feeds directly into the [hc-enterprise-kg](https://github.com/thehipsterciso/hc-enterprise-kg) MCP server, making the full knowledge graph queryable from Claude Desktop — enabling natural-language traversal, blast radius analysis, dependency mapping, and scenario modeling.

## Quality Gates

Every commit is validated against automated quality checks:

| Check | Blocks Commit | Threshold |
|-------|:------------:|-----------|
| Schema validation | Yes | 100% |
| Required fields | Yes | 100% |
| Relationship integrity | Yes | No dangling references |
| Provenance completeness | Warning | Future: 100% |
| Duplicate detection | Warning | 85%+ name similarity |

See [CONTRIBUTING.md](CONTRIBUTING.md) for full quality standards and [docs/QUALITY_INFRASTRUCTURE.md](docs/QUALITY_INFRASTRUCTURE.md) for implementation details.

## The AI-Native Thesis

This project exists to prove a point: **AI doesn't replace human judgment — it scales it.**

Every entity in this graph was discovered, validated, and contextualized through a human-AI partnership. The AI systems performed the collection, pattern matching, cross-referencing, and structured output. The humans provided the analytical framework, the evidentiary standards, the domain expertise, and the judgment calls on what matters.

The result is a body of work that would have taken a traditional consulting team 6–8 weeks and $500K+. It was produced in a fraction of that time, with full transparency, reproducible methodology, and open access.

This isn't a demo. It's a proof of concept for a new model of enterprise intelligence — one where the methodology is public, the evidence is auditable, and the barrier to entry is expertise rather than budget.

## Program & Attribution

This project was developed as part of the **Carnegie Mellon University Heinz College Chief Data & AI Officer (CDAIO) Program** — an executive education initiative preparing senior leaders to drive data and AI strategy at the enterprise level.

### Team

| Name | Role |
|------|------|
| Thomas Jones | Project Lead, CDAIO Candidate |
| *[Team Member 2]* | *[Role/Focus Area]* |
| *[Team Member 3]* | *[Role/Focus Area]* |
| *[Team Member 4]* | *[Role/Focus Area]* |

### Acknowledgments

- **Carnegie Mellon University, Heinz College of Information Systems and Public Policy** — for building a program that treats data and AI leadership as an operational discipline, not an academic abstraction
- **The CDAIO Program Faculty and Staff** — for the analytical frameworks and rigor standards that shaped this work
- **The CDAIO Cohort** — for the peer pressure, the intellectual honesty, and the shared conviction that executive decision-making deserves better evidence

### Built With

- [hc-enterprise-kg](https://github.com/thehipsterciso/hc-enterprise-kg) — Open-source enterprise knowledge graph platform (30 entity types, 58 relationship types, MCP server integration)
- [Claude](https://claude.ai) — AI partner for OSINT collection, entity extraction, relationship mapping, and structured analysis
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io) — The protocol enabling Claude Desktop to query and modify the knowledge graph directly

## License

This repository contains structured analysis of publicly available information. All entity data is derived from public sources including SEC filings, regulatory disclosures, DNS records, BGP routing tables, PeeringDB, and published documentation. No proprietary or confidential information is included.

---

*"The best diligence isn't the most expensive. It's the most honest."*

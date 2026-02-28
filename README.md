# hc-cdaio-kg

Rapid-evaluation enterprise knowledge graph. Maximum coverage, minimal effort.

Built on the [hc-enterprise-kg](https://github.com/thehipsterciso/hc-enterprise-kg) schema (30 entity types, 58 relationship types) and populated entirely from public sources using AI-augmented OSINT. Not production-grade — this is a time-boxed assessment designed to answer the question: *how much can you learn about an enterprise without anyone handing you a single document?*

The answer turns out to be: enough to make a $500K consulting engagement look like a slow way to get the same thing.

## What This Is

A digital twin of a public technology company — 2,900+ entities, 6,000+ relationships, 401 structured analysis documents — constructed as a practicum deliverable for the Carnegie Mellon Heinz College CDAIO program.

The knowledge graph covers 11 layers of enterprise architecture (geography through vendors), and the due diligence analysis covers 10 stages of structured inquiry (corporate structure through enterprise resilience). Every entity traces to a public source. Every analytical claim carries an explicit confidence rating and evidence citation.

This is not a polished final product. It is a working artifact from a rapid evaluation that prioritized breadth and honest uncertainty over completeness.

## Repository Structure

```
entities/              26 per-type JSON files (2,900+ entities)
relationships/         39 per-type JSON files (6,000+ relationships)
due-diligence/         10-stage structured analysis (401 JSON documents)
docs/ledgers/          OSINT research session logs and methodology
scripts/               Sync, build, and quality automation
```

### Knowledge Graph

| Layer | Entity Types | Count |
|-------|-------------|-------|
| L00 Geography | geography, jurisdiction, location, site | 223 |
| L01 Governance | control, policy, regulation | 524 |
| L02 Technology | system, network, integration | 636 |
| L03 Data | data_asset, data_domain | 211 |
| L04 Organization | department, organizational_unit, role | 786 |
| L05 People | person | 100 |
| L06 Capabilities | business_capability | 64 |
| L07 Contracts | contract | 37 |
| L08 Products | product, product_portfolio, market_segment | 130 |
| L09 Customers | customer | 85 |
| L10 Vendors | vendor | 60 |

39 relationship types. `depends_on`, `subject_to`, `located_in`, `managed_by`, `enforces`, `implements`, `supports`, `connects_to`, and 31 others.

### Due Diligence Analysis

| Stage | Focus |
|-------|-------|
| 0 | Diligence governance — evidence hierarchy, claim classification, epistemic standards |
| 1 | Corporate & legal — legal existence, ownership, structural debt, change-of-control |
| 2 | Business model — revenue engine, cost physics, value flow, contradictions |
| 3 | Market & competition — structure, threats, buying behavior, shock sensitivity |
| 4 | Operating model — decision rights, cadence, bottlenecks, incentive misalignment |
| 5 | Financial reality — revenue quality, margins, liquidity, covenants, contradictions |
| 6 | Technology — compute, hyperscaler dependency, platform fragility, technical debt |
| 7 | Data & information — domains, lineage, quality, stewardship, epistemic coherence |
| 8 | Risk & security — cyber posture, privacy, regulatory enforcement, sovereignty |
| 9 | Resilience — ESG, failure sequencing, workforce fragility, ecosystem shocks |

Each stage includes validation gates, contradiction analysis, and uncertainty registers. Every claim is tagged FACT, INFERENCE, or HYPOTHESIS with source citations.

### Research Ledgers

Session-by-session OSINT logs in `docs/ledgers/`. These track what was searched, what was found, what confidence tier it received (T1–T4), and what analytical decisions were made. The audit trail for how raw intelligence became structured knowledge.

## How It Works

Per-type JSON files — one file per entity type, one per relationship type. Prevents merge conflicts when multiple people work in parallel.

| Time | Script | What it does |
|------|--------|-------------|
| 8 AM | `kg-morning.sh` | Pull main, rebuild `graph.json`, reload MCP server |
| Every 30 min | `kg-sync.sh` | Split graph into per-type files, commit, push |
| 5 PM | `kg-eod.sh` | Final sync, open PR to main |

The assembled `graph.json` feeds into the [hc-enterprise-kg](https://github.com/thehipsterciso/hc-enterprise-kg) MCP server. Load it, and Claude Desktop can traverse the graph — dependency chains, blast radius, centrality analysis, scenario modeling — all through natural language.

## Quality Gates

| Check | Blocks Commit | Threshold |
|-------|:---:|-----------|
| Schema validation | Yes | 100% |
| Required fields | Yes | 100% |
| Relationship integrity | Yes | No dangling references |
| Provenance completeness | Warning | Future: 100% |
| Duplicate detection | Warning | 85%+ name similarity |

Details in [CONTRIBUTING.md](CONTRIBUTING.md) and [docs/QUALITY_INFRASTRUCTURE.md](docs/QUALITY_INFRASTRUCTURE.md).

## The Point

Most enterprise due diligence is theater. Expensive theater. A firm charges half a million dollars, assigns a team for six weeks, and produces a PDF that nobody can reproduce, interrogate, or extend. The methodology is proprietary. The evidence chains are opaque. If you want to ask a question that was not in the original scope, you write another check.

This project took a different approach. AI handled the collection, cross-referencing, and structured output. Humans provided the analytical framework, the evidentiary standards, and the judgment. The result is an open, queryable, auditable knowledge graph — not a PDF that sits in a SharePoint folder until the next deal.

That matters for two reasons:

**For executives and boards:** The cost of understanding your own enterprise just dropped by an order of magnitude. A rapid evaluation like this does not replace deep diligence with data room access, but it tells you whether the deep diligence is worth pursuing — and exactly where to focus it.

**For the profession:** If a CISO with AI tools can produce this level of structural analysis from public sources in a fraction of the traditional timeline, then the advisory model that charges by the hour for opaque work product is on borrowed time. The barrier to enterprise intelligence should be expertise and rigor, not budget.

## Program & Attribution

Developed as part of the **Carnegie Mellon University Heinz College Chief Data & AI Officer (CDAIO) Program**.

### Team

| Name | Role |
|------|------|
| Thomas Jones | Project Lead, CDAIO Candidate |
| *[Team Member]* | *[Role]* |
| *[Team Member]* | *[Role]* |
| *[Team Member]* | *[Role]* |

### Acknowledgments

**Carnegie Mellon University, Heinz College of Information Systems and Public Policy** — a program that treats data and AI leadership as an operational discipline, not an academic exercise.

**CDAIO Program Faculty and Staff** — the analytical frameworks and rigor standards that shaped this work.

**The Cohort** — for the intellectual honesty and the shared expectation that executive decision-making deserves better evidence than it typically gets.

### Built With

- [hc-enterprise-kg](https://github.com/thehipsterciso/hc-enterprise-kg) — Open-source enterprise knowledge graph platform
- [Claude](https://claude.ai) + [Model Context Protocol](https://modelcontextprotocol.io) — AI-augmented OSINT, entity extraction, relationship mapping, and interactive graph analysis

## Data Sources

All entity data derived from public sources: SEC filings, regulatory disclosures, DNS records, BGP routing tables, PeeringDB, ARIN, job postings, press releases, published documentation, and compliance certifications. No proprietary or confidential information is included.

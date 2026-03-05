**DCAM Version 2 Deep-Dive**
Capability 1
**Data Management Strategy & Business Case**
Rackspace Technology, Inc.
Assessment Date: March 2026
Source: Enterprise Knowledge Graph (3,060 entities | 7,614 relationships)
**Overall Capability Score: 2 — Developing**
**Classification: Confidential**

# 1. Executive Context
***This deep-dive examines the first of eight DCAM v2 capabilities assessed for Rackspace Technology: Data Management Strategy & Business Case. At a composite score of 2 (Developing), this capability represents the strategic foundation upon which all other data management capabilities depend. The score signals that while Rackspace has demonstrated awareness of data management as a strategic discipline, the organization has not yet formalized this awareness into a unified strategy document, a quantified business case, or executive-level sponsorship dedicated to enterprise data management.***
***The assessment draws from a knowledge graph containing 3,060 entities and 7,614 relationships, with particular focus on 25 strategic initiatives, 67 business capabilities, 100 key persons, and 123 policies. The confidence level for this capability is Medium, reflecting the availability of initiative and organizational data but the absence of direct evidence of a formalized data management strategy.***
### Maturity Positioning
```
┌─────────────────────────────────────────────────────────────────┐
│  DCAM v2 MATURITY SCALE — CAPABILITY 1 POSITION                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                     │
│   1-Initial    2-Developing    3-Defined    4-Managed    5-Optimized │
│   │            │               │            │            │           │
│   │            ▲               │            │            │           │
│   │        [CURRENT]           │            │            │           │
│   │         Score: 2            │            │            │           │
│   │                  ◄──TARGET──►            │            │           │
│   │            │          12-18 mo.       │            │           │
│                                                                     │
└─────────────────────────────────────────────────────────────────┘
```

# 2. Sub-Capability Score Summary

| Sub-Capability                                   | Score | Level      | Trend Indicator    |
| ------------------------------------------------ | ----- | ---------- | ------------------ |
| 1.1 Data Management Strategy Articulation        | 2     | Developing | ▶ Stagnant         |
```
| 1.2 Business Case for Data Management            | 2     | Developing | ▲ Upward potential |
| 1.3 Executive Sponsorship and Funding            | 2     | Developing | ▼ At risk          |
| 1.4 Strategic Alignment with Business Objectives | 3     | Defined    | ▲ Positive         |

# 3. Sub-Capability 1.1: Data Management Strategy Articulation
### Score: 2 — Developing
***DCAM v2 requires that an organization articulate a formal data management strategy document that defines the vision, scope, objectives, and roadmap for managing data as an enterprise asset. At the Developing level, awareness exists and some directional intent is visible, but no unified strategy document has been published.***
## What the Knowledge Graph Reveals
***The KG provides strong evidence of data management intent distributed across multiple organizational initiatives, but no evidence of a consolidated strategy document. The following entities and relationships are relevant:***
Data Governance Policy (pol-071): Establishes ownership, stewardship, quality standards, and lineage tracking. This is the closest artifact to a strategy document, but it is a policy, not a strategy.
Data Platform and AI Readiness Initiative: Articulates strategic direction toward data and AI enablement, but is services-revenue-focused rather than internal-capability-focused.
Managed Data Lake and Lakehouse Services Launch: Revenue-generating initiative that demonstrates data capability, but oriented toward customers, not enterprise data management.
FAIR (Foundry for AI by Rackspace) (ou-012): 70+ enterprise AI implementations for customers. Demonstrates organizational data maturity in services, not internally.
Internal Data & Analytics Department (dept-011): 20-person team, $3.38M budget. Consolidating 400 dashboards to 20 and 70 data warehouses. This is operational modernization, not strategic articulation.
## The Fragmentation Pattern
┌─────────────────────────────────────────────────────────────────┐
│  STRATEGY FRAGMENTATION — WHERE DATA DIRECTION LIVES TODAY          │
├─────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌───────────────┐   ┌───────────────┐   ┌───────────────┐    │
│  │  FAIR Practice │   │ Internal D&A │   │ Data Platform │    │
│  │  (ou-012)      │   │ Dept (011)  │   │ & AI Readines │    │
│  │  Customer AI   │   │ Dashboards  │   │ Services Rev  │    │
│  │  700+ engage.  │   │ 400→20       │   │ $50M+ ARR     │    │
│  └───────────────┘   └───────────────┘   └───────────────┘    │
│        \                  |                  /               │
│         \                 |                 /                │
│          └─────────────┬─────────────┘                 │
│                          |                                  │
│              ┌─────────────────────┐                    │
│              │  ?? MISSING ARTIFACT ??  │                    │
│              │  Enterprise Data Mgmt    │                    │
│              │  Strategy Document       │                    │
│              └─────────────────────┘                    │
│                                                                     │
│  Gap: No single document unifies these threads into an enterprise    │
│  data management strategy with vision, scope, and roadmap.           │
└─────────────────────────────────────────────────────────────────┘
```

***The fundamental issue is not the absence of data management thinking. Rackspace has significant data capability. The issue is that strategic intent is distributed across at least three organizational vectors (FAIR for customer AI, Internal D&A for operational modernization, and service-line initiatives for revenue) with no unifying strategy document, no stated enterprise data management vision, and no published roadmap that connects these threads into a coherent whole.***
## What Good Looks Like (Score 3 Requirements)
A published Enterprise Data Management Strategy document with executive approval
Defined vision, scope, objectives, and 3-year roadmap
Explicit linkage between data management strategy and corporate strategic priorities
Annual review cycle with version control and distribution

# 4. Sub-Capability 1.2: Business Case for Data Management
### Score: 2 — Developing
***DCAM v2 requires a formal business case that quantifies the value of data management investment and links it to enterprise value creation. At the Developing level, implicit business justification exists but no formal business case document has been produced.***
## What the Knowledge Graph Reveals
***The KG provides several data points that could form the basis of a compelling business case, but no entity or artifact represents a formalized business case document:***
AIDE (AI Data Engineering) services targeting $50M+ ARR: Demonstrates that data and AI services have direct revenue value, but this is customer-facing revenue, not an internal data management ROI argument.
Data services bookings doubled FY2024: Market validation of data capability value, but again externally focused.
Project Eagle (INIT-002): $100M+ annualized cost reduction program. Operational efficiency initiative, not a data management business case. However, data management improvements could amplify Project Eagle outcomes.
Internal D&A Department: $3.38M budget, 20 headcount. Dashboard consolidation from 400 to 20 and data warehouse consolidation from 70 to unified platform. The cost and complexity of this consolidation is itself evidence of the cost of poor data management.
Missing Customer Identity Reconciliation Process: CRM, Billing, and Support systems define customers differently with no systematic reconciliation across 81,000+ customer accounts. This gap alone likely creates quantifiable revenue leakage, billing disputes, and analytics inaccuracy.
## The Unrealized Business Case
```
┌─────────────────────────────────────────────────────────────────┐
│  BUSINESS CASE ELEMENTS — AVAILABLE BUT UNASSEMBLED               │
├─────────────────────────────────────────────────────────────────┤
│                                                                     │
│  REVENUE CASE            COST CASE              RISK CASE            │
│  ────────────            ─────────              ─────────            │
│  $50M+ AIDE ARR         400→20 dashboards      81K customer          │
│  2x data bookings       70→unified DW          identity gap          │
│  Data lakehouse svc     $3.38M D&A spend       PLAY ransomware       │
│  700+ AI engagements    Project Eagle $100M    378 integrations       │
│                                                 790 dependencies       │
│  [✓] Evidence exists    [✓] Evidence exists   [✓] Evidence exists    │
│  [✗] Not quantified     [✗] Not quantified    [✗] Not quantified     │
│  [✗] Not formalized     [✗] Not formalized    [✗] Not formalized     │
│                                                                     │
└─────────────────────────────────────────────────────────────────┘
```

***The irony is that Rackspace possesses all the raw material for a compelling business case. The customer identity reconciliation gap alone, affecting 81,000+ accounts across $2.7B in revenue, could be quantified as revenue leakage risk. The dashboard consolidation effort (400 to 20) quantifies the cost of data management debt. The 378 integration points and 790 dependency relationships represent operational risk that a formal data management program would systematically reduce. What is missing is not the evidence. What is missing is someone assembling it into a document that says: here is what data management costs us today, here is what it could save us, and here is the investment required.***

# 5. Sub-Capability 1.3: Executive Sponsorship and Funding
### Score: 2 — Developing
***DCAM v2 requires visible executive sponsorship of data management at the C-suite or Board level, with dedicated funding for data management programs. At the Developing level, some executive engagement exists but is not formalized or dedicated to data management as a distinct discipline.***
## What the Knowledge Graph Reveals
### Leadership Structure (Relevant Persons)

| Person        | Title                                     | Data Management Relevance                                                                                                                  |
| ------------- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Srini Koushik | President, AI Technology & Sustainability | Closest to a CAIO. Leads FAIR practice. P&L authority over AI services. Cross-functional mandate. Does NOT own enterprise data management. |
| Amar Maletira | CEO                                       | Executive sponsor of Multi-Cloud Transformation and Project Eagle. Data management not explicitly in CEO agenda.                           |
| (Absent)      | Chief Data Officer                        | No CDO or equivalent enterprise data management executive exists in the KG. This is the single most significant gap.                       |

## The Sponsorship Gap
```
┌─────────────────────────────────────────────────────────────────┐
│  EXECUTIVE SPONSORSHIP MAP                                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                     │
│                      ┌───────────┐                              │
│                      │    CEO    │                              │
│                      │ Maletira  │                              │
│                      └────┬──────┘                              │
│              ┌────────┼──────────────┬──────────┐          │
│              |        |              |          |          │
│        ┌─────┴───┐ ┌──┴──────┐ ┌───┴─────┐ ┌───┴────┐     │
│        │   CTO    │ │   CFO    │ │   CAIO    │ │  CIO    │     │
│        │ Mukerji │ │ Marino   │ │ Koushik  │ │ Rojas   │     │
│        └─────────┘ └─────────┘ └────┬─────┘ └───┬────┘     │
│                                    |              |              │
│                               ┌────┴─────┐   ┌────┴─────┐     │
│                               │   FAIR    │   │ Internal  │     │
│                               │ Customer │   │   D&A     │     │
│                               │   AI     │   │ dept-011  │     │
│                               └──────────┘   └──────────┘     │
│                                                                     │
│  MISSING: CDO/VP Data Management with enterprise data mandate        │
│  Internal D&A reports through CIO, not to C-suite directly            │
│  Data governance not visible in CEO/Board agenda                      │
└─────────────────────────────────────────────────────────────────┘
```

***Srini Koushik, as President of AI Technology & Sustainability, is the closest the organization has to a Chief AI Officer with cross-functional authority. FAIR, under his leadership, has executed 70+ enterprise AI implementations and is scaling toward $50M+ AI services ARR. But his mandate is customer-facing AI services delivery, not enterprise data management. The Internal Data & Analytics Department (dept-011), which is the organizational unit most directly responsible for internal data management, reports through the CIO (Juan Rojas), placing it two levels below the C-suite. No entity in the knowledge graph carries the title of Chief Data Officer, VP of Data Management, or equivalent.***
***This is not unusual for a technology services company of Rackspace's size and history. But it creates a structural problem for DCAM advancement: without a dedicated executive sponsor, data management competes for attention against revenue-generating initiatives, security imperatives, and cost reduction programs. The $3.38M budget for Internal D&A, while meaningful, is small relative to Rackspace's $2.7B revenue base and $150M annual investment in multi-cloud transformation.***

# 6. Sub-Capability 1.4: Strategic Alignment with Business Objectives
### Score: 3 — Defined
***This is the strongest sub-capability within Capability 1 and the only one that reaches the Defined maturity level. DCAM v2 requires that data management activities demonstrate clear alignment with business strategic priorities. Rackspace meets this threshold because its data-related initiatives are demonstrably connected to corporate strategic objectives.***
## What the Knowledge Graph Reveals
***The KG maps 25 strategic initiatives, many of which have direct data management implications. Three corporate strategic priorities are documented in the FY2024 10-K: operational turnaround, innovation, and capital structure optimization. Data initiatives align to each:***

| Strategic Priority | Data-Related Initiative                                      | Alignment Evidence                                             |
| ------------------ | ------------------------------------------------------------ | -------------------------------------------------------------- |
| Revenue Growth     | FAIR AI services, Data Lakehouse Launch, AIDE ($50M+ ARR)    | Direct revenue linkage. Data services bookings doubled FY2024. |
| Cost Reduction     | Project Eagle ($100M+), Dashboard consolidation (400→20)     | Operational efficiency through data modernization.             |
| Compliance         | FedRAMP, SOC Modernization, GDPR/privacy programs            | 70 regulations, 527 domain-to-regulation mappings.             |
| Innovation         | Data Platform & AI Readiness, Palantir/Sema4.ai partnerships | AI capability requires data capability as prerequisite.        |

***The gap that prevents a score of 4 (Managed) is that alignment is initiative-driven rather than strategy-driven. Each initiative independently connects to business objectives, but there is no overarching data management strategy that deliberately orchestrates these connections. The alignment is emergent, not designed. This is the difference between initiatives that happen to involve data and a data management program that deliberately enables business strategy.***

# 7. Cross-Cutting Analysis: The Services-vs-Internal Paradox
***The most consequential pattern across all four sub-capabilities is the asymmetry between Rackspace's customer-facing data and AI capability and its internal enterprise data management maturity. This pattern is worth examining in detail because it shapes every recommendation.***
```
┌─────────────────────────────────────────────────────────────────┐
│  THE COBBLER'S CHILDREN PROBLEM                                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                     │
│  CUSTOMER-FACING (Mature)        INTERNAL (Developing)               │
│  ───────────────────────        ──────────────────────────     │
│  ✓ 700+ AI engagements            ✗ No enterprise data strategy       │
│  ✓ $50M+ AIDE ARR target           ✗ No CDO role                       │
│  ✓ 300+ certified DBAs             ✗ No data management business case   │
│  ✓ Palantir/Sema4.ai partnerships  ✗ 400 unmanaged dashboards           │
│  ✓ Data Scientists, Engineers       ✗ No data catalog or MDM             │
│  ✓ Multi-cloud data lakehouse       ✗ Customer identity gap              │
│                                                                     │
│  Score: ~4 (if assessed)             Score: 2 (assessed)              │
│                                                                     │
│  INSIGHT: The talent, tooling, and methodology to build a mature     │
│  internal data management program already exists inside Rackspace.   │
│  The gap is strategic direction, not organizational capacity.        │
└─────────────────────────────────────────────────────────────────┘
```

# 8. Recommendations: Path from Score 2 to Score 3
***Moving Capability 1 from Developing (2) to Defined (3) requires four deliberate actions, each mapped to a specific sub-capability deficit:***
## R1: Publish an Enterprise Data Management Strategy (1.1)
Consolidate the strategic intent currently distributed across FAIR, Internal D&A, and service-line initiatives into a single enterprise data management strategy document.
Define vision, scope, objectives, governance model, and 3-year roadmap.
Explicitly address both internal enterprise data management and customer-facing data services.
Estimated effort: 8-12 weeks with cross-functional working group.
## R2: Formalize the Business Case (1.2)
Quantify the cost of the customer identity reconciliation gap (revenue leakage, billing disputes, analytics inaccuracy).
Quantify the cost of dashboard/warehouse fragmentation (400 dashboards, 70 data warehouses).
Frame data management investment as an accelerant for Project Eagle cost savings and AIDE revenue growth.
Publish a formal business case with NPV/ROI analysis and present to CFO.
## R3: Establish Executive Sponsorship (1.3)
Create a CDO role or elevate data management mandate within existing C-suite (most natural: extend Srini Koushik's scope to include internal data management).
Establish a Data Governance Council with cross-BU representation.
Place data management on the Board's audit or risk committee agenda.
## R4: Formalize Strategic Alignment (1.4)
Embed data management objectives into each strategic initiative's OKRs.
Create a data management scorecard linked to corporate KPIs.
Transition from emergent alignment to designed orchestration.

# 9. Knowledge Graph Evidence Summary
***The following table maps each finding in this deep-dive to specific entities and relationships in the enterprise knowledge graph, providing full traceability for the assessment.***

| Finding                        | KG Entity/Relationship                         | Confidence                                         |
| ------------------------------ | ---------------------------------------------- | -------------------------------------------------- |
| No unified DM strategy         | pol-071, ou-012, dept-011, 25 initiatives      | Medium — Absence confirmed by KG exhaustive search |
| No formal business case        | INIT-002 (Project Eagle), AIDE revenue targets | Medium — Indirect evidence only                    |
| No CDO or equivalent           | person-034 (Koushik), 100 persons searched     | Medium-High — 100 persons mapped, no CDO found     |
| FAIR customer AI maturity      | ou-012 (FAIR), 70+ implementations             | Medium-High — SEC filings confirm                  |
| Internal D&A modernization     | dept-011, ou-106, bc-048                       | Medium-High — Case study confirms 400→20           |
| Strategic initiative alignment | 25 initiatives with business_capability links  | Medium — Initiative-level, not strategy-level      |
| Customer identity gap          | Explicit KG-documented gap entity              | High — Self-identified by organization             |

**End of Capability 1 Deep-Dive**
***This document is the first in a series of eight DCAM v2 capability deep-dives for Rackspace Technology. Subsequent capabilities will be assessed in sequence, each building on the evidence base established here.***
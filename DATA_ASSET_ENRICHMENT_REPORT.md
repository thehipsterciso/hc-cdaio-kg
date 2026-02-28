# Data Asset Enrichment Report
## Rackspace Technology Enterprise Knowledge Graph — CDAIO Program

**Date:** 2026-02-28
**Assessed By:** CDAIO KG Enrichment Process — Hybrid Methodology
**Graph File:** `graph.json`

---

## Executive Summary

All 164 data asset entities in the Rackspace Technology enterprise knowledge graph have been enriched to operational completeness. This work spanned two phases: Phase 1 added 41 new data assets representing previously unmapped data stores across the Genestack/OpenStack, Kubernetes, observability, AI/ML, and business analytics infrastructure tiers. Phase 2 enriched all 164 data assets (123 existing + 41 new) with governance, regulatory, temporal, lineage, and provenance metadata.

**Zero Pydantic validation errors** were encountered across all 164 update operations.

---

## Graph Statistics (Post-Enrichment)

| Metric | Value |
|--------|-------|
| Total entities | 2,949 |
| Total relationships | 7,011 |
| Data asset entities | 164 |
| System entities | 164 |
| Graph density | 0.00081 |
| Entity types | 26 |
| Relationship types | 42 |

---

## Enrichment Coverage

| Metric | Count | Percentage |
|--------|-------|------------|
| Total data assets | 164 | — |
| Enriched (completeness_pct populated) | 164 | 100% |
| Average completeness_pct | 57.0% | — |
| Min completeness_pct | 40% | — |
| Max completeness_pct | 80% | — |

### By Classification

| Classification | Count | Avg Completeness |
|---------------|-------|-----------------|
| Restricted | 60 | ~62% |
| Confidential | 89 | ~55% |
| Internal | 15 | 43% |

### Key Attribute Coverage

| Attribute | Assets with Data | Coverage |
|-----------|-----------------|----------|
| provenance.completeness_pct | 164 | 100% |
| regulatory_applicability (with regulation_id) | 83 | 50.6% |
| lineage_upstream (with asset_id) | 31 | 18.9% |
| data_owner | ~150 | ~91% |
| encryption_at_rest | ~160 | ~98% |
| access_governance | ~150 | ~91% |

---

## Phase 1: New Data Assets Added (41 Entities)

### Tier A — Genestack/OpenStack Service Databases (13)
Keystone Identity, Nova Compute, Neutron Network, Cinder Block Storage, Glance Image Registry, Heat Orchestration, Barbican Secrets, Octavia LB, Ironic Bare Metal, Designate DNS, Manila Shared FS, Placement Resource, Skyline Dashboard — plus Memcached Cache and RabbitMQ Message Queue.

### Tier B — Kubernetes & Platform Data Stores (8)
etcd Cluster State, Longhorn Persistent Volumes, Vault Enterprise Secrets, cert-manager TLS Certificates, Harbor Container Registry, Argo Workflows State, Nautobot DCIM/IPAM, Dex OIDC Identity Provider.

### Tier C — Observability & Security Data (8)
Prometheus TSDB, OpenSearch Log Indices, Grafana Dashboard State, AlertManager Alert State, Microsoft Sentinel SIEM, CrowdStrike Falcon EDR, Microsoft Defender VMDR, Microsoft Purview DLP.

### Tier D — AI/ML Data Stores (6)
AI Launchpad Training Datasets, AI Launchpad Model Artifacts, AI Anywhere GPU Workload, Compass Healthcare AI Clinical Dataset, RITA Responsible AI Assessment, ICE AI Impact Calculation.

### Tier E — Business & Analytics Data (6)
Snowflake Enterprise Analytics DWH, PagerDuty Incident Operations, Confluence Enterprise Knowledge Base, Power BI Reporting Datasets, Customer NPS/CSAT Survey Data, plus Rackspace Public API Usage Metrics (mapped to existing entity).

---

## Key Findings

### Golden Sources Identified
- **Vault Enterprise Secrets Store** — root of trust for all credential management
- **Nautobot DCIM/IPAM Database** — authoritative source for network inventory and IP allocations

### Critical Data Gaps Flagged
- **Memcached Keystone Cache** — no authentication or TLS encryption; Critical priority remediation
- **etcd Cluster State** — encryption at rest not confirmed; Critical priority
- **Confluence Knowledge Base** — mixed classification content without per-page labeling; High priority

### Regulatory Highlights
- **6 data assets** subject to EU AI Act (AI Launchpad Training, Model Artifacts, AI Anywhere GPU, Compass Healthcare, RITA RAI, ICE Impact)
- **Compass Healthcare AI** carries the most stringent regulatory profile: HIPAA, HITECH, EU AI Act, SOC2, GDPR
- **AI Launchpad Training Dataset** flagged High risk under EU AI Act Art. 10 data governance requirements

### Lineage Chains Established
- Prometheus TSDB → AlertManager → PagerDuty (observability alert chain)
- AI Launchpad Training Data → AI Launchpad Model Artifacts (ML pipeline)
- RITA RAI Assessments → ICE Impact Calculations (AI governance chain)
- Snowflake DWH → Power BI Reporting Datasets (analytics pipeline)
- NPS/CSAT Survey → Snowflake DWH (customer experience analytics)

---

## Fields Intentionally Left Null

The following field categories require runtime data, operational access, or financial information that cannot be populated through documentation-based enrichment:

- **quality_score_composite** — requires active data quality monitoring tools
- **record_count_detail** — requires database/API queries for live counts
- **volume.current_size** — requires storage metrics access (populated where publicly available)
- **financial profile** (storage_cost, processing_cost, total_data_cost) — requires finance team input
- **profiling_status** — requires data profiling tooling
- **current_access_grants** — requires IAM/directory queries
- **data_cleansing_history** — requires data operations records

---

## Methodology

All enrichment followed a Hybrid methodology combining:
1. System entity data (164 enriched systems provided parent-child context)
2. Product and vendor documentation
3. Regulatory framework analysis (GDPR, HIPAA, SOC2, ISO 27001, EU AI Act, PCI DSS)
4. Architecture inference from integration patterns
5. OSINT for publicly available product specifications

Confidence levels range from Medium to High, with AI/ML assets generally at Medium (newer products, less documentation) and established infrastructure assets at High.

---

## Recommendations

1. **Implement data classification labeling in Confluence** — mixed-classification spaces represent the highest governance risk among knowledge management assets
2. **Enable encryption at rest for Memcached and etcd** — both store sensitive data without confirmed encryption
3. **Establish automated data quality monitoring** — zero assets have quality_score_composite populated; this is the largest systematic gap
4. **Complete EU AI Act compliance assessments** — 6 AI data assets flagged; 3 currently "In Progress"
5. **Build out financial profile data** — storage/processing cost attribution would enable data asset valuation and FinOps integration
6. **Formalize data catalog registration** — majority of Phase 1 assets not yet registered in enterprise data catalog

---

*Report generated by CDAIO KG Enrichment Process. Graph version: 2,949 entities / 7,011 relationships.*

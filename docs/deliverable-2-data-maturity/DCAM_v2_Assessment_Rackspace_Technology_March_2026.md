
**DCAM Version 2**
Data Management Capability Assessment
**Rackspace Technology, Inc.**

Assessment Date: March 2026
Methodology: EDM Council DCAM v2 Framework
Source: Enterprise Knowledge Graph (3,060 entities | 7,614 relationships)
**Classification: Confidential**

# Executive Summary
This assessment evaluates Rackspace Technology’s data management maturity against the EDM Council’s Data Management Capability Assessment Model (DCAM) version 2 framework. The analysis is derived entirely from an enterprise knowledge graph comprising 3,060 entities and 7,614 relationships, representing the organization’s systems, policies, controls, data domains, personnel, and operational structures as of March 2026.
The overall maturity score is 2.6 on the DCAM 1–5 scale, placing Rackspace Technology at the upper boundary of Developing maturity with pockets of Defined and Managed capability. This score reflects a fundamental asymmetry: Rackspace has built sophisticated data governance, privacy, and security capabilities to serve its customers as a managed cloud services provider, but has underinvested in applying equivalent rigor to its own enterprise data management.
Data Privacy and Protection (4.0) is the strongest capability, driven by multi-framework compliance requirements across 50+ jurisdictions. Data Governance (3.0) benefits from a comprehensive policy framework of 123 policies and 351 controls. At the other end, Master and Reference Data Management (1.0), Self-Service Data Access (1.0), and Data Service Level Management (1.0) represent critical gaps where foundational capabilities do not yet exist.
The most consequential finding is the explicitly documented absence of a Customer Identity Reconciliation Process — the knowledge graph itself identifies that CRM, Billing, and Support systems define customers differently with no systematic reconciliation. For a company managing 81,000+ customer accounts across $2.7B in revenue, this master data gap creates downstream data quality, analytics, and financial reporting risk.

## Overall Maturity Scores by Capability

| Capability                                  | Score | Maturity Level |
| ------------------------------------------- | ----- | -------------- |
| 1. Data Management Strategy & Business Case | 2     | Developing     |
| 2. Data Governance                          | 3     | Defined        |
| 3. Data Quality Management                  | 2     | Developing     |
| 4. Data Architecture and Integration        | 3     | Defined        |
| 5. Data Lifecycle Management                | 3     | Defined        |
| 6. Data Privacy and Protection              | 4     | Managed        |
| 7. Data and Analytics Enablement            | 2     | Developing     |
| 8. Data Management Operations               | 2     | Developing     |

**Overall Composite Score: 2.6 — Developing (upper boundary)**

## DCAM v2 Maturity Scale Reference

| Level | Name       | Description                                                                             |
| ----- | ---------- | --------------------------------------------------------------------------------------- |
| 1     | Initial    | Ad hoc or absent. No repeatable processes or formal capabilities exist.                 |
| 2     | Developing | Awareness exists. Some processes defined but inconsistently applied. Reactive posture.  |
| 3     | Defined    | Policies and standards documented. Processes repeatable. Governance structure in place. |
| 4     | Managed    | Quantitatively measured. Proactive management. Continuous improvement in place.         |
| 5     | Optimized  | Fully integrated. Automated. Data management embedded in culture and strategy.          |

# Detailed Capability Assessments
## 1. Data Management Strategy & Business Case
**Capability Score: **2 — Developing
Rackspace Technology demonstrates nascent but recognizable data management strategic intent. The knowledge graph reveals 25 strategic initiatives, several directly addressing data and AI readiness — notably the Data Platform and AI Readiness initiative and the Managed Data Lake and Lakehouse Services Launch. A Data Governance Policy exists establishing ownership, stewardship, quality standards, and lineage tracking. However, the strategy remains fragmented across business units (Public Cloud, Private Cloud, FAIR) without a unified enterprise data management strategy document or formally articulated business case linking data management investment to measurable business outcomes. The Internal Data & Analytics Department is consolidating from 400 dashboards to a unified platform, which signals strategic awareness, but the effort lacks a published data management strategy with executive sponsorship at the C-suite level. The Chief AI Officer role exists with cross-functional authority, yet there is no Chief Data Officer or equivalent enterprise data management executive.

### Sub-Capability Scores

| Sub-Capability                                   | Score | Maturity Level |
| ------------------------------------------------ | ----- | -------------- |
| 1.1 Data Management Strategy Articulation        | 2     | Developing     |
| 1.2 Business Case for Data Management            | 2     | Developing     |
| 1.3 Executive Sponsorship and Funding            | 2     | Developing     |
| 1.4 Strategic Alignment with Business Objectives | 3     | Defined        |

**1.1 Data Management Strategy Articulation (Score: 2): **Data Governance Policy exists (KG entity: policy). Data Platform and AI Readiness initiative articulates direction. No standalone enterprise data management strategy document. Strategy fragmented across FAIR, Internal Data & Analytics, and BU-specific programs.

**1.2 Business Case for Data Management (Score: 2): **AI services revenue target ($50M+ ARR for AIDE) provides indirect business case. Data services bookings doubled FY2024. No formal business case document quantifying data management ROI or linking it to enterprise value creation. Cost reduction (Project Eagle) is operational, not data-strategic.

**1.3 Executive Sponsorship and Funding (Score: 2): **Chief AI Officer exists with P&L authority. FAIR funded as innovation unit. No CDO or equivalent data management executive. Data governance not visibly sponsored at CEO/Board level. Internal Data & Analytics Dept reports through CIO, not directly to C-suite.

**1.4 Strategic Alignment with Business Objectives (Score: 3): **Data initiatives clearly aligned to revenue growth (AI services, data lakehouse), cost reduction (Project Eagle), and compliance (FedRAMP). 25 initiatives show business alignment. Gap: alignment is initiative-driven, not strategy-driven.

## 2. Data Governance
**Capability Score: **3 — Defined
Data governance is the most mature DCAM capability observed. The knowledge graph reveals a comprehensive policy framework: 123 policies including a dedicated Data Governance Policy, Data Classification Policy, Data Quality Policy, Data Architecture and Modeling Standards Policy, and Data Retention and Disposal Policy. 351 controls enforce these policies through 386 enforcement relationships. 90 data domains are formally defined with managed_by relationships to 63 responsible departments. 70 regulations and 527 data-domain-to-regulation subject_to relationships demonstrate regulatory mapping depth. The Data Classification Policy establishes four tiers (Public, Internal, Confidential, Restricted) with handling requirements. However, confidence scores on managed_by relationships average only 0.77 (the lowest of any relationship type), indicating uncertainty in stewardship assignment. Several data domains, particularly customer-facing operational data, show 0.65 confidence in management ownership, suggesting stewardship roles are inferred rather than formally designated.

### Sub-Capability Scores

| Sub-Capability                           | Score | Maturity Level |
| ---------------------------------------- | ----- | -------------- |
| 2.1 Governance Operating Model           | 3     | Defined        |
| 2.2 Data Stewardship                     | 2     | Developing     |
| 2.3 Data Policy Framework                | 4     | Managed        |
| 2.4 Regulatory and Compliance Mapping    | 4     | Managed        |
| 2.5 Data Domain Definition and Ownership | 3     | Defined        |

**2.1 Governance Operating Model (Score: 3): **Data Governance Policy establishes framework. 63 data domain managed_by relationships define ownership. No formal Data Governance Council or committee visible in KG. Operating model is policy-defined but execution structure unclear.

**2.2 Data Stewardship (Score: 2): **63 managed_by relationships link data domains to departments. Average confidence 0.77 (lowest relationship type). 27 data domains at 0.65 confidence. Data Strategy & Governance Lead role exists but appears services-facing, not internal. No formal steward registry.

**2.3 Data Policy Framework (Score: 4): **23 data-specific policies identified. Coverage spans classification, quality, retention, privacy, architecture, DLP, and cross-border transfer. Policies are detailed with regulatory cross-references. Strong policy framework.

**2.4 Regulatory and Compliance Mapping (Score: 4): **70 regulations mapped. 527 data-domain-to-regulation relationships. 1,117 total subject_to relationships across KG. Coverage includes GDPR, SOX, HIPAA, FedRAMP, ITAR, PCI DSS, and 50+ jurisdictions. Confidence avg 0.91.

**2.5 Data Domain Definition and Ownership (Score: 3): **90 data domains formally defined with rich descriptions. Contains relationships (51) link domains to sub-domains. Ownership assigned via managed_by. Gap: 27 domains have uncertain ownership (0.65 confidence).

## 3. Data Quality Management
**Capability Score: **2 — Developing
Data quality management shows policy-level intent but limited operational evidence. A Data Quality Policy exists establishing dimensions (accuracy, completeness, consistency, timeliness, validity) and a Data Quality Monitoring Controls entity is present in the knowledge graph. However, the control description references automated data quality rules and exception reporting without specifying tooling, coverage metrics, or operational maturity. There is a critical gap explicitly identified in the KG: a missing Customer Identity Reconciliation Process, described as the absence of a systematic process to reconcile customer identity and count across CRM, Billing, and Support systems. This is a direct indicator of data quality issues in master data. The Internal Data & Analytics Department’s consolidation from 400 dashboards to a unified platform suggests historical data quality and consistency problems. No dedicated data quality team or tooling (e.g., Great Expectations, Informatica DQ) is evident.

### Sub-Capability Scores

| Sub-Capability                              | Score | Maturity Level |
| ------------------------------------------- | ----- | -------------- |
| 3.1 Data Quality Strategy and Standards     | 3     | Defined        |
| 3.2 Data Quality Measurement and Monitoring | 2     | Developing     |
| 3.3 Data Quality Remediation                | 2     | Developing     |
| 3.4 Master and Reference Data Management    | 1     | Initial        |

**3.1 Data Quality Strategy and Standards (Score: 3): **Data Quality Policy defines dimensions and processes. Data Architecture and Modeling Standards Policy establishes naming conventions. Policy intent is strong. Gap: no evidence of DQ KPIs, SLAs, or measurement targets.

**3.2 Data Quality Measurement and Monitoring (Score: 2): **Data Quality Monitoring Controls entity exists but lacks specificity on tooling and coverage. No dedicated DQ platform visible. 400-to-1 dashboard consolidation indicates historical inconsistency.

**3.3 Data Quality Remediation (Score: 2): **Exception reporting and remediation tracking referenced in policy. Missing Customer Identity Reconciliation Process is an explicit KG-documented gap. No evidence of systematic root cause analysis or remediation workflows.

**3.4 Master and Reference Data Management (Score: 1): **Explicitly identified gap: no cross-system customer identity reconciliation. CRM, Billing, Support define customers differently. No MDM platform or golden record capability visible. Critical deficiency.

## 4. Data Architecture and Integration
**Capability Score: **3 — Defined
Data architecture is extensive but organically evolved rather than strategically designed. The knowledge graph maps 164 systems, 378 integrations, and 790 depends_on relationships, revealing a complex technology estate. Integration patterns are heavily identity-centric: Cloud Identity Service (Keystone) serves as the primary authentication fabric with 15+ direct integration relationships. A Data Architecture and Modeling Standards Policy exists. The technology stack spans OpenStack-era systems (Nova, Swift, Neutron) through modern cloud platforms (AWS, Azure, GCP partnerships). RackConnect Global provides multi-cloud connectivity via MPLS. However, the 378 integrations suggest significant point-to-point complexity. No enterprise integration platform, API gateway, or event-driven architecture layer is visible as a unifying integration strategy. The 790 depends_on relationships indicate deep coupling that creates blast radius risk.

### Sub-Capability Scores

| Sub-Capability                    | Score | Maturity Level |
| --------------------------------- | ----- | -------------- |
| 4.1 Enterprise Data Architecture  | 3     | Defined        |
| 4.2 Data Integration Strategy     | 2     | Developing     |
| 4.3 Data Modeling and Standards   | 3     | Defined        |
| 4.4 Metadata Management           | 2     | Developing     |
| 4.5 Technology Platform and Tools | 3     | Defined        |

**4.1 Enterprise Data Architecture (Score: 3): **Data Architecture and Modeling Standards Policy exists. 90 data domains provide logical architecture. 164 data assets mapped. Gap: no enterprise data architecture diagram or reference architecture document visible. Architecture is implicit in the system/integration topology.

**4.2 Data Integration Strategy (Score: 2): **378 integrations mapped. Heavy point-to-point pattern. Identity-centric integration via Keystone. RackConnect for multi-cloud. No enterprise integration platform, ESB, or API management layer visible. Integration strategy is tactical.

**4.3 Data Modeling and Standards (Score: 3): **Data Architecture and Modeling Standards Policy establishes methodology. Database Administration and Management Policy governs provisioning. 300+ certified DBAs. Standards exist but enforcement unclear.

**4.4 Metadata Management (Score: 2): **Data Governance Policy references lineage tracking and metadata management. No data catalog, metadata repository, or lineage tool visible in KG systems inventory. Metadata management is policy-aspirational.

**4.5 Technology Platform and Tools (Score: 3): **164 systems mapped. Splunk for SIEM/observability. ServiceNow for ITSM. SailPoint for identity governance. Moogsoft for AIOps. CrowdStrike for EDR. Mature security tooling. Gap: no dedicated data management tooling stack.

## 5. Data Lifecycle Management
**Capability Score: **3 — Defined
Data lifecycle management benefits from strong regulatory drivers. The Data Retention and Disposal Policy, Data Retention and Automated Purge control, and Records Management and Retention Policy collectively establish a lifecycle framework. Retention periods are defined: 7-year SOX, 6-year GDPR, 13-month security logs. Secure Media Disposal follows NIST 800-88. The Document Retention and Destruction Schedule operationalizes retention across corporate document categories. 165 stores relationships map data assets to storage systems. However, lifecycle management is compliance-driven rather than value-driven: no evidence of data archival strategies, tiered storage optimization, or lifecycle-based data monetization. The 9 documented security incidents, including the PLAY ransomware attack, underscore the operational importance of lifecycle controls.

### Sub-Capability Scores

| Sub-Capability                       | Score | Maturity Level |
| ------------------------------------ | ----- | -------------- |
| 5.1 Data Retention and Archival      | 3     | Defined        |
| 5.2 Data Disposal and Destruction    | 4     | Managed        |
| 5.3 Data Lineage and Provenance      | 2     | Developing     |
| 5.4 Data Classification and Handling | 4     | Managed        |

**5.1 Data Retention and Archival (Score: 3): **Data Retention and Disposal Policy defines periods. Automated purge controls exist. Document Retention and Destruction Schedule is operational. Gap: retention is compliance-driven, no value-based tiering.

**5.2 Data Disposal and Destruction (Score: 4): **Secure Media Disposal (NIST 800-88). Media Sanitization (MP-6) control. Cryptographic erasure, degaussing, or physical destruction based on classification. Certificates of destruction. Mature capability.

**5.3 Data Lineage and Provenance (Score: 2): **Data Governance Policy references lineage tracking. No lineage tooling visible. 790 depends_on relationships provide implicit lineage proxy but no end-to-end data flow traceability.

**5.4 Data Classification and Handling (Score: 4): **Data Classification Policy with four tiers. Data Classification Labeling control. Data Tagging for PII (PT-4). Security Categorization (RA-2) per FIPS 199. Handling requirements defined per classification level.

## 6. Data Privacy and Protection
**Capability Score: **4 — Managed
Data privacy and protection is the strongest capability area, driven by Rackspace’s position as a managed cloud services provider handling customer data across 50+ countries. The knowledge graph reveals 70 regulations, 23 data-specific policies, and deep regulatory mapping (527 data-domain-to-regulation relationships). GDPR compliance spans 20 data domains. PCI DSS Level 1 Service Provider certification, HITRUST CSF, FedRAMP Moderate JAB P-ATO, and SOC 1/2/3 attestations demonstrate multi-framework compliance. Privacy-specific capabilities include: Data Privacy Impact Assessment Policy, Data Subject Rights Response Policy, Cross-Border Data Transfer Policy (SCCs, EU-US DPF), Cookie Consent and Tracking Controls, and a Customer Data Processing Addendum. The CISO role is well-defined. Post-PLAY ransomware, security modernization is an active initiative. 351 controls with 386 enforcement relationships demonstrate operational enforcement.

### Sub-Capability Scores

| Sub-Capability                              | Score | Maturity Level |
| ------------------------------------------- | ----- | -------------- |
| 6.1 Privacy Program and Compliance          | 4     | Managed        |
| 6.2 Data Security Controls                  | 4     | Managed        |
| 6.3 Third-Party and Vendor Risk             | 3     | Defined        |
| 6.4 Incident Response and Breach Management | 3     | Defined        |
| 6.5 Regulatory Compliance Monitoring        | 4     | Managed        |

**6.1 Privacy Program and Compliance (Score: 4): **Privacy Notice, DPIA Policy, Data Subject Rights Response Policy, Cross-Border Transfer Policy. GDPR, CCPA/CPRA, UK GDPR, PIPEDA, PDPA coverage. Cookie consent controls. Mature privacy program.

**6.2 Data Security Controls (Score: 4): **351 controls mapped. MFA, RBAC, PAM, encryption, DLP, EDR (CrowdStrike), SIEM (Splunk). Active Directory domain segregation. Bastion host isolation. Comprehensive security architecture.

**6.3 Third-Party and Vendor Risk (Score: 3): **55 vendors mapped. Supplier Data Processing Agreement Policy. 40 contracts. Third-Party Dependency Risk identified. Gap: vendor data handling assessment process not visible beyond contractual DPA.

**6.4 Incident Response and Breach Management (Score: 3): **Incident Response Policy. 9 documented incidents. PLAY ransomware response and SOC modernization initiative. Information Spillage Response (IR-9). Gap: post-breach improvements still in progress. S1-S4 severity classification.

**6.5 Regulatory Compliance Monitoring (Score: 4): **70 regulations tracked. FedRAMP continuous monitoring. SOC attestations. PCI DSS quarterly ASV scans. 1,117 subject_to relationships. Compliance monitoring is operationally mature.

## 7. Data and Analytics Enablement
**Capability Score: **2 — Developing
Data and analytics enablement is emerging but immature relative to Rackspace’s size and complexity. The Internal Data & Analytics Department exists and is consolidating from 400 dashboards to a unified platform, indicating early-stage modernization. The FAIR (Foundry for AI by Rackspace) practice has executed 700+ customer-facing AI engagements but internal data and analytics capability lags the external services capability. Data-related roles are primarily services-facing: Data Scientists, Data Engineers, and Data Architects serve customers through the FAIR framework rather than internal enterprise analytics. The Data Platform and AI Readiness initiative and Managed Data Lake and Lakehouse Services Launch are services-revenue-focused, not internal-capability-focused. No enterprise BI platform, self-service analytics layer, or data democratization program targeting internal Rackspace users is visible.

### Sub-Capability Scores

| Sub-Capability                          | Score | Maturity Level |
| --------------------------------------- | ----- | -------------- |
| 7.1 Business Intelligence and Reporting | 2     | Developing     |
| 7.2 Advanced Analytics and Data Science | 2     | Developing     |
| 7.3 Self-Service Data Access            | 1     | Initial        |
| 7.4 Data Literacy and Training          | 2     | Developing     |

**7.1 Business Intelligence and Reporting (Score: 2): **400 dashboards consolidated to unified platform (in progress). Internal Data & Analytics Department exists. Analytics & BI Developer role present. Gap: no named BI platform. Consolidation implies fragmented baseline.

**7.2 Advanced Analytics and Data Science (Score: 2): **FAIR has 700+ customer AI engagements. Data Scientist, DataOps Engineer, Data Platform Engineer roles exist. Palantir and Sema4.ai partnerships. Gap: internal advanced analytics capability not visible.

**7.3 Self-Service Data Access (Score: 1): **No data catalog, data marketplace, or self-service query tool visible in KG. No data democratization initiative. Data access appears request-based through department-owned dashboards.

**7.4 Data Literacy and Training (Score: 2): **Rackspace University delivers 52+ Learning Hours. Technical Onboarding Program (TOP). 3,800+ AWS accreditations, 500+ GCP certifications. Gap: no data literacy program targeting non-technical staff.

## 8. Data Management Operations
**Capability Score: **2 — Developing
Data management operations are implicitly embedded within IT and security operations rather than existing as a distinct operational function. The knowledge graph reveals strong IT operational maturity: ServiceNow ITSM, SailPoint identity governance, Moogsoft AIOps, and a 24x7x365 operations model across 7,614 managed relationships. However, data management operations as a distinct discipline — data pipeline monitoring, data SLA management, data incident resolution, data change management — is not visible. Change Management Policy exists for production systems but does not specifically address data changes. The 790 depends_on relationships create operational complexity that is managed through general IT operations rather than data-specific operations. No DataOps team, data pipeline monitoring, or data SLA framework is visible for internal enterprise data.

### Sub-Capability Scores

| Sub-Capability                         | Score | Maturity Level |
| -------------------------------------- | ----- | -------------- |
| 8.1 Data Operations Team and Process   | 2     | Developing     |
| 8.2 Data Issue and Incident Management | 2     | Developing     |
| 8.3 Data Change Management             | 2     | Developing     |
| 8.4 Data Service Level Management      | 1     | Initial        |

**8.1 Data Operations Team and Process (Score: 2): **DataOps Engineer role exists but is services-facing. No internal data operations team or process visible. General IT operations (24x7x365) handles infrastructure. Data management piggybacked on IT ops.

**8.2 Data Issue and Incident Management (Score: 2): **ServiceNow ITSM for general incidents. S1-S4 severity classification. No data-specific incident category or resolution SLA visible. Data issues managed through general IT incident process.

**8.3 Data Change Management (Score: 2): **Change Management Policy exists for production systems. Database Administration and Management Policy governs DB changes. Gap: no data-specific change management (schema changes, data migration, DQ rule changes).

**8.4 Data Service Level Management (Score: 1): **No data SLAs, data availability targets, or data freshness commitments visible in KG. SLAs exist for cloud infrastructure (99.9%+) but not for enterprise data services.

# Cross-Cutting Findings
## Finding 1: The Services-vs-Internal Maturity Gap
The most pervasive pattern across the assessment is the gap between Rackspace’s customer-facing data and AI services capability and its internal enterprise data management maturity. FAIR has delivered 700+ AI engagements for customers. 300+ certified DBAs manage customer database environments. Data Scientists, Data Architects, and DataOps Engineers exist in quantity — but overwhelmingly in services delivery roles. The Internal Data & Analytics Department’s 400-dashboard consolidation, the absence of internal self-service analytics, and the missing customer identity reconciliation process all point to the same conclusion: the cobbler’s children have no shoes. This is not unusual for technology services firms, but it is a strategic risk as Rackspace positions itself as an AI and data services leader. Credibility requires demonstrated internal capability.
## Finding 2: Policy Strength Without Operational Tooling
Rackspace’s policy framework is genuinely impressive: 123 policies, 351 controls, 386 enforcement relationships, and deep regulatory mapping. The Data Governance Policy, Data Quality Policy, Data Architecture and Modeling Standards Policy, and Data Classification Policy collectively describe a mature data management program on paper. But the knowledge graph reveals a tooling gap beneath the policy layer. No data catalog. No metadata repository. No data lineage tool. No MDM platform. No dedicated data quality platform. No enterprise integration layer. Policies without tooling create audit risk: the organization can articulate what it should be doing, and compliance auditors will increasingly ask for evidence that it actually is.
## Finding 3: Integration Complexity as a Data Management Risk
378 integrations and 790 depends_on relationships describe an interconnected but organically evolved technology landscape. The identity-centric integration pattern (Cloud Identity/Keystone as the hub) provides authentication coherence but does not address data integration coherence. Point-to-point integration patterns create data consistency risk, make impact analysis difficult, and increase the blast radius of any single system failure. The November 2023 PLAY ransomware attack on Hosted Exchange and the September 2024 ScienceLogic zero-day exploitation both demonstrate how integration density amplifies incident impact. A formal integration architecture and data mesh or data fabric strategy would reduce both operational risk and data management overhead.
## Finding 4: Confidence Erosion at the Stewardship Layer
The knowledge graph’s own confidence scores tell a story. While most relationship types carry confidence averages above 0.85, the managed_by relationship type — which maps data domains to their responsible departments — averages only 0.77. This is the lowest confidence of any relationship type in the graph. The applies_to relationship (0.78) and contains relationship (0.83) also show relatively lower confidence. In DCAM terms, this means the organization has high confidence in what data it has and what regulations apply to it, but lower confidence in who is responsible for managing that data. Stewardship ambiguity is the leading indicator of governance program fragility.
## Finding 5: Strong Compliance Foundation Creates a Path to Maturity
Despite the gaps identified, Rackspace’s compliance-driven data management foundation provides a strong base for maturity advancement. The regulatory mapping (70 regulations, 527 domain-to-regulation relationships), the policy framework, the classification scheme, and the security control architecture do not need to be built — they need to be extended. Moving from Developing to Defined maturity requires operationalizing existing policies with tooling, formalizing stewardship with explicit role assignments, and creating data-specific SLAs and metrics. The incremental effort is significantly lower than building from scratch. The Chief AI Officer’s cross-functional authority, combined with the FAIR organization’s data engineering talent, represents the organizational capacity to drive this maturation if strategic direction is provided.

# Appendix A: Provenance, Confidence, and Assumptions
## A.1 Assessment Methodology and Data Source
This assessment is derived entirely from an enterprise knowledge graph maintained as the hc-cdaio-kg repository. The graph contains 3,060 entities across 26 entity types and 7,614 relationships across 40 relationship types. Entity data was sourced from public SEC filings (10-K, 10-Q, 8-K, DEF 14A), published technical documentation, partner announcements, regulatory filings, job postings, and organizational disclosures. No interviews, surveys, or self-assessments were conducted. This is an observational assessment based on documented evidence.
## A.2 Confidence Level by Capability

| DCAM Capability                             | Score | Confidence | Primary KG Evidence Sources                                                                                                  |
| ------------------------------------------- | ----- | ---------- | ---------------------------------------------------------------------------------------------------------------------------- |
| 1. Data Management Strategy & Business Case | 2     | Medium     | 25 initiatives, business_capability (67), data_domain (90), person (CAIO role)                                               |
| 2. Data Governance                          | 3     | High       | 123 policies, 351 controls, 386 enforces, 90 data_domain, 63 managed_by, 527 subject_to                                      |
| 3. Data Quality Management                  | 2     | Medium-Low | Data Quality Policy, DQ Monitoring Controls, missing reconciliation control (explicit gap). Limited operational evidence.    |
| 4. Data Architecture & Integration          | 3     | High       | 164 systems, 378 integrations, 790 depends_on, Data Architecture Standards Policy                                            |
| 5. Data Lifecycle Management                | 3     | High       | Retention/Disposal Policy, NIST 800-88 controls, 165 stores, classification controls, media sanitization                     |
| 6. Data Privacy & Protection                | 4     | High       | 70 regulations, 23 data policies, 351 controls, 1117 subject_to, 55 vendors, 9 incidents                                     |
| 7. Data & Analytics Enablement              | 2     | Medium     | Internal Data & Analytics Dept, FAIR practice, 400-dashboard reference, role inventory. Limited internal analytics evidence. |
| 8. Data Management Operations               | 2     | Medium-Low | ServiceNow, Change Mgmt Policy, DB Admin Policy. No data-specific ops processes visible in KG.                               |

## A.3 Knowledge Graph Statistics

| Metric                               | Value                 |
| ------------------------------------ | --------------------- |
| Total Entities                       | 3,060                 |
| Total Relationships                  | 7,614                 |
| Entity Types                         | 26                    |
| Relationship Types                   | 40                    |
| Average Relationship Confidence      | 0.89                  |
| Average Relationship Weight          | 0.93                  |
| Relationships with Weight ≥ 0.9      | 5,432 (71.3%)         |
| Relationships with Weight 0.7–0.89   | 2,007 (26.4%)         |
| Relationships with Weight < 0.7      | 175 (2.3%)            |
| Lowest Confidence Relationship Type  | managed_by (avg 0.77) |
| Highest Confidence Relationship Type | regulates (avg 1.00)  |

## A.4 Entity Type Distribution

| Entity Type         | Count | DCAM Relevance                         |
| ------------------- | ----- | -------------------------------------- |
| role                | 430   | Stewardship, organizational capacity   |
| integration         | 378   | Data architecture, system connectivity |
| control             | 351   | Policy enforcement, DQ controls        |
| department          | 250   | Organizational structure, stewardship  |
| data_asset          | 164   | Data inventory, lifecycle              |
| system              | 164   | Technology architecture                |
| policy              | 123   | Governance framework                   |
| organizational_unit | 111   | Governance structure                   |
| person              | 100   | Leadership, sponsorship                |
| risk                | 94    | Risk-driven governance                 |
| data_domain         | 90    | Domain definition, ownership           |
| regulation          | 70    | Compliance mapping                     |
| vendor              | 55    | Third-party data risk                  |
| contract            | 40    | Data processing agreements             |
| initiative          | 25    | Strategic direction                    |
| incident            | 9     | Incident response maturity             |

## A.5 Key Assumptions and Limitations
**Observational methodology: **Scores are based on documented evidence in the knowledge graph. Capabilities that exist but are not documented in the KG may be underscored. This is particularly relevant for Capabilities 7 (Analytics Enablement) and 8 (Data Ops), where informal processes may exist.
**Confidence scoring: **Where the KG provides relationship confidence scores, these are used to qualify findings. Low-confidence relationships (< 0.80) are flagged as uncertain. Capabilities heavily dependent on low-confidence relationships receive Medium-Low assessment confidence.
**Absence vs. non-documentation: **The absence of an entity or relationship in the KG is treated as absence of the capability, not proof it does not exist. For example, the absence of a data catalog system does not prove Rackspace has no data catalog — it proves no data catalog was identified in the documented evidence base.
**Temporal scope: **The KG reflects organizational state as of early 2026. Active initiatives (SOC Modernization, Dashboard Consolidation, Data Platform Readiness) may have progressed beyond what is captured. Scores should be validated against current operational state.
**Public source bias: **KG entities sourced from public filings (SEC, regulatory) carry higher confidence than entities inferred from job postings or partner announcements. This creates a bias toward regulatory/compliance maturity and potentially understates operational maturity.
**Scoring calibration: **DCAM v2 scores are applied using the EDM Council’s five-level maturity scale. Scores represent the assessor’s best judgment mapping KG evidence to DCAM criteria. Half-point increments are not used; each score is a whole integer representing the predominant maturity level.

## A.6 Relationship Confidence by Type (Full Distribution)

| Relationship Type | Count | Avg Conf. | Min Conf. | DCAM Impact               |
| ----------------- | ----- | --------- | --------- | ------------------------- |
| managed_by        | 385   | 0.77      | 0.65      | Stewardship certainty     |
| applies_to        | 601   | 0.78      | 0.75      | Policy coverage           |
| located_at        | 683   | 0.80      | 0.75      | Physical data locality    |
| contains          | 75    | 0.83      | 0.70      | Domain structure          |
| affects           | 76    | 0.83      | 0.80      | Risk propagation          |
| mitigates         | 45    | 0.84      | 0.50      | Control effectiveness     |
| provides_service  | 61    | 0.84      | 0.70      | Service delivery          |
| connects_to       | 140   | 0.85      | 0.75      | Network architecture      |
| stores            | 165   | 0.87      | 0.65      | Data asset mapping        |
| enforces          | 386   | 0.91      | 0.80      | Governance enforcement    |
| subject_to        | 1117  | 0.91      | 0.55      | Regulatory coverage       |
| depends_on        | 790   | 0.91      | 0.60      | Architecture dependencies |
| hosted_on         | 490   | 0.92      | 0.65      | Infrastructure mapping    |
| implements        | 178   | 0.93      | 0.70      | Control implementation    |
| supports          | 193   | 0.95      | 0.67      | Capability enablement     |
| regulates         | 49    | 1.00      | 1.00      | Regulatory authority      |

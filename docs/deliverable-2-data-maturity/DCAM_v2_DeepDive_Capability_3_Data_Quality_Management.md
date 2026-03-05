**DCAM Version 2 Deep-Dive**
Capability 3
**Data Quality Management**
Rackspace Technology, Inc.
Assessment Date: March 2026
Source: Enterprise Knowledge Graph (3,060 entities | 7,614 relationships)
**Overall Capability Score: 2 — Developing**
**Contains Lowest Sub-Capability Score in Entire Assessment (3.4 = 1, Initial)**
**Classification: Confidential**

# 1. Executive Context
***This deep-dive examines Capability 3 of eight DCAM v2 capabilities assessed for Rackspace Technology: Data Quality Management. At a composite score of 2 (Developing), this capability represents one of the most materially underdeveloped domains in the enterprise data management architecture. The score indicates that while Rackspace has articulated a data quality policy (POL-072) and created a detective control (CTL-305), the organization has not yet operationalized data quality management as a continuous, measurable, and systematic discipline across its 90 data domains.***
***The central finding is what this assessment terms the 'Null Quality Pattern': the knowledge graph schema for every data domain includes comprehensive quality management fields—quality_targets, quality_monitoring, profiling_status, quality_score_composite—yet across all 90 domains, these fields are universally unpopulated. No key performance indicators are populated. No data profiling has been conducted. Automated monitoring remains disabled across the entire data domain portfolio. Zero data domains have composite quality scores. The schema represents organizational intention; the null values represent operational reality. The gap between the two is the defining characteristic of Capability 3.***
***The paradox deepens when examined through an organizational lens. Rackspace employs DataOps Engineers (role-125), Lead Data Engineers (role-160), and operates a Data Modernization Department (dept-069, $1.56M budget, 10 headcount) whose explicit mandate includes 'data quality validation' in customer-facing services. These professionals implement data quality frameworks for external customers daily: completeness validation, accuracy checks, timeliness enforcement, and consistency rules across Azure Data Lake, Databricks, Synapse, and Snowflake platforms. Yet those same quality frameworks, methodologies, and technical patterns have not been turned inward to systematically measure and improve the quality of Rackspace's own data estate. The cobbler's children, once again, have no shoes.***
***The assessment draws from a knowledge graph containing 3,060 entities and 7,614 relationships, with particular focus on 90 data domains, 123 policies (of which 1 is quality-specific), 351 controls (of which 1 is quality-monitoring-specific), and the structural absence of quality measurement data across the entire domain portfolio. Sub-Capability 3.4 (Data Profiling & Assessment) scores 1 (Initial)—the lowest sub-capability score in the entire DCAM assessment—indicating a complete operational void in data profiling execution.***
### Maturity Positioning
```
┌─────────────────────────────────────────────────────────────────┐
│  DCAM v2 MATURITY SCALE — CAPABILITY 3 POSITION                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                     │
│   1-Initial    2-Developing    3-Defined    4-Managed    5-Optimized │
│   │            │               │            │            │           │
│   │            ▲               │            │            │           │
│   │        [CURRENT]           │            │            │           │
│   │         Score: 2           │            │            │           │
│   │            ►─TARGET────►         │            │           │
│   │          12-18 mo.         │            │            │           │
│                                                                     │
│   NOTE: Sub-Cap 3.4 scores 1 (Initial) — lowest in entire DCAM     │
└─────────────────────────────────────────────────────────────────┘
```

### Quality Policy and Control Landscape

| Policy ID | Policy Name                        | Type           | Review Freq. | Enforced |
| --------- | ---------------------------------- | -------------- | ------------ | -------- |
| POL-072   | Data Quality Policy                | Administrative | Annual       | Yes      |
| POL-054   | Quality Management Policy          | Administrative | Annual       | Yes      |
| CTL-305   | Data Quality Monitoring Controls   | Detective      | Continuous   | Partial  |
| CTL-292   | Quality Management System Controls | Preventive     | Annual       | Yes      |

***Note: POL-054 and CTL-292 address ISO 9001 service quality management, not data quality specifically. Only POL-072 and CTL-305 are directly relevant to DCAM Capability 3 assessment. The distinction matters: ISO 9001 quality management governs service delivery processes, while data quality management governs the accuracy, completeness, consistency, timeliness, and validity of the data assets themselves. Rackspace has a robust ISO 9001 program; it does not yet have a comparable data quality program.***

# 2. Sub-Capability Score Summary

| Sub-Capability                            | Score | Level      | Trend Indicator                        |
| ----------------------------------------- | ----- | ---------- | -------------------------------------- |
| 3.1 Data Quality Strategy                 | 2     | Developing | Policy exists; no operational strategy |
| 3.2 Data Quality Measurement & Monitoring | 2     | Developing | Control exists; KPIs unpopulated       |
| 3.3 Data Quality Issue Management         | 2     | Developing | No remediation workflow                |
| 3.4 Data Profiling & Assessment           | 1     | Initial    | Zero domains profiled — lowest in DCAM |

***The sub-capability scores reveal a capability that is uniformly underdeveloped across all four dimensions, with Sub-Capability 3.4 representing a complete operational void. Scores of 1-2 indicate that while the organization has identified the concept of data quality and created policy artifacts, it has not yet built the operational capability to measure, enforce, or improve data quality systematically. The scores also reveal a cascading dependency chain that compounds the problem.***
### Cascading Dependency Chain
```
┌─────────────────────────────────────────────────────────────────┐
│  QUALITY MANAGEMENT DEPENDENCY CASCADE                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                     │
│   3.4 PROFILING (Score 1)     │  Without profiling, no baselines   │
│        │                      │  exist for any domain. Zero of    │
│        ▼                      │  90 domains have last_profiled_   │
│   3.1 STRATEGY (Score 2)      │  date populated. No profiling      │
│        │                      │  tool deployed.                    │
│        ▼                      │                                    │
│   3.2 MEASUREMENT (Score 2)   │  Without strategy, no targets.     │
│        │                      │  Without targets, no KPIs.         │
│        ▼                      │  CTL-305 KPIs are entirely null.   │
│   3.3 ISSUE MGMT (Score 2)    │  Without measurement, issues       │
│                               │  cannot be systematically detected  │
│   ▶ ROOT CAUSE: 3.4           │  or prioritized. No SLA defined.   │
│                                                                     │
└─────────────────────────────────────────────────────────────────┘
```

***The cascade illustrates why Sub-Capability 3.4 is the root cause of the entire Capability 3 underperformance. Profiling provides the baselines that inform strategy; strategy defines the targets that drive measurement; measurement surfaces the issues that require management. When the foundation (profiling) is entirely absent, every subsequent layer inherits a structural inability to function. Addressing Capability 3 must therefore begin at 3.4 and flow upward.***

# 3. Sub-Capability 3.1: Data Quality Strategy
### Score: 2 (Developing)
***The Data Quality Strategy sub-capability assesses whether Rackspace has articulated a comprehensive data quality vision, defined quality target levels by domain, identified root causes of quality defects, and established a prioritized roadmap for quality improvement. At a score of 2, the organization has named the concept of data quality in its policy framework but has not operationalized that concept into a strategically coherent program with measurable objectives, accountable owners, and sequenced investments.***
## The Policy Artifact Without Strategy
***POL-072 (Data Quality Policy) exists in the knowledge graph as an Administrative-type policy with Medium severity, marked as Enforced, with an annual review cycle. The policy defines five data quality dimensions: Accuracy, Completeness, Consistency, Timeliness, and Validity. These dimensions are explicitly present in the policy entity's attributes and align with industry-standard frameworks (DAMA DMBOK, ISO 8000). The presence of these dimensions demonstrates that someone within the organization understood the theoretical foundation of data quality management.***
***However, the compliance_measurement object for POL-072 is entirely empty: metric_name is null, target_value is null, current_value is null, measurement_method is null, frequency is null. This structural absence reveals the gap between definition and operationalization. The policy defines WHAT to measure (five dimensions) but provides no framework for HOW to measure, WHO measures, at what FREQUENCY, or AGAINST WHAT TARGETS. The policy is definitional, not operational.***
***An operational data quality strategy would specify, for example, that 'Customer Account Data (DD-001) must achieve 99.5% completeness for critical billing fields, measured monthly through automated record validation against source systems, with exceptions escalated to the Data Strategy & Governance team within 24 hours and root cause analysis completed within 72 hours.' POL-072 says 'completeness shall be measured' but does not specify these operational details for any single data domain across the entire portfolio of 90 domains.***
## Five Dimensions Defined, Zero Operationalized
```
┌─────────────────────────────────────────────────────────────────┐
│  POL-072: FIVE DIMENSIONS vs. OPERATIONAL REALITY                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                     │
│   DIMENSION       POLICY   TARGETS  MEASUREMENT  DOMAINS  AUTOMATED  │
│   ────────────   ──────   ───────  ───────────  ───────  ─────────  │
│   Accuracy        ✓ Yes     ✗ None   ✗ None       0 / 90   ✗ No      │
│   Completeness    ✓ Yes     ✗ None   ✗ None       0 / 90   ✗ No      │
│   Consistency     ✓ Yes     ✗ None   ✗ None       0 / 90   ✗ No      │
│   Timeliness      ✓ Yes     ✗ None   ✗ None       0 / 90   ✗ No      │
│   Validity        ✓ Yes     ✗ None   ✗ None       0 / 90   ✗ No      │
│                                                                     │
│   POLICY COVERAGE: 100%  |  OPERATIONAL COVERAGE: 0%                │
│   Gap: Total (policy exists but zero measurement implemented)       │
│                                                                     │
└─────────────────────────────────────────────────────────────────┘
```

### Quality Dimensions Coverage Matrix

| Quality Dimension | Target Defined | Domains Measured | Automated? | Coverage % |
| ----------------- | -------------- | ---------------- | ---------- | ---------- |
| Accuracy          | No             | 0 / 90           | No         | 0.0%       |
| Completeness      | No             | 0 / 90           | No         | 0.0%       |
| Consistency       | No             | 0 / 90           | No         | 0.0%       |
| Timeliness        | No             | 0 / 90           | No         | 0.0%       |
| Validity          | No             | 0 / 90           | No         | 0.0%       |

***The table above quantifies the complete disconnect between policy articulation and operational implementation. POL-072 defines five quality dimensions. None of those dimensions have target values defined for any data domain. None have measurement methods established. None are monitored through automation. The operational coverage rate across all dimensions, all domains, and all measurement modalities is 0.0%.***
## The Services-Facing Quality Capability
***As with Capability 2's governance disconnect, the quality management gap manifests as a services-internal disconnect. The Data Modernization Department (dept-069, $1.56M budget, 10 headcount) explicitly offers 'data quality validation' as a services deliverable to Rackspace's customer base. DataOps Engineers (role-125) implement quality validation rules as part of customer pipeline development. Lead Data Engineers (role-160) architect data lake quality frameworks on Azure Data Lake, Databricks, Synapse, and Snowflake. These professionals possess the operational data quality discipline that could be systematized internally.***
***The disconnect is worth quantifying: dept-069 has $1.56M in annual budget directed at customer-facing data quality work. The investment required to establish an internal data quality baseline (profiling tool licensing, initial profiling execution, KPI framework population) would likely represent a fraction of that amount, perhaps $200-400K in the first year including tooling and dedicated FTE allocation. The organization already possesses the expertise. The gap is strategic direction, not capability.***
POL-072 compliance_measurement fields are entirely null (metric_name, target_value, current_value, measurement_method, frequency)
Five quality dimensions defined in policy but zero are measured against any baseline across any of the 90 data domains
No data quality strategy document, roadmap, or prioritization framework identified in the knowledge graph
dept-069 DataOps capability ($1.56M, 10 HC) is services-facing; no evidence of internal quality program leverage
No quality dimension targets (completeness_target_pct, accuracy_target_pct, timeliness_target_sla, consistency_target_pct, validity_target_pct) populated for any domain

# 4. Sub-Capability 3.2: Data Quality Measurement & Monitoring
### Score: 2 (Developing)
***The Data Quality Measurement and Monitoring sub-capability assesses whether Rackspace has implemented KPIs, automated quality checks, measurement dashboards, and trending analysis across its data domains. At a score of 2, the organization has created a control artifact (CTL-305) and identified the systems it should apply to, but has not operationalized the control through KPI definition, automation enablement, effectiveness measurement, or systematic evidence collection.***
## CTL-305: The Implemented Control Without Implementation
***CTL-305 (Data Quality Monitoring Controls) exists as a Detective control, marked as 'Implemented' status, with control owner listed as 'Data Governance.' The control explicitly enforces POL-072 at a confidence level of 0.80. The control description references 'automated monitoring across completeness, accuracy, timeliness, and consistency dimensions, applied to enterprise data systems.' Three systems are linked via applies_to relationships: sys-056 (Data Lake and Warehouse), sys-050 (Data Pipeline Orchestration), and sys-031 (Metadata Store), all at confidence 0.75.***
***However, every operational attribute of CTL-305 contradicts its 'Implemented' status designation. The KPI fields (metric_name, target_value, current_value, measurement_method, frequency) are all null. The control_effectiveness rating field is null. The testing_approach field is undefined. Most critically, evidence_collection_automated is set to false, indicating that despite the control's title and description mentioning 'automated monitoring,' the actual monitoring infrastructure is either manual, non-systematized, or absent entirely.***
```
┌─────────────────────────────────────────────────────────────────┐
│  CTL-305: DOCUMENTED vs. OPERATIONAL STATE                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                     │
│   ATTRIBUTE              DOCUMENTED        ACTUAL (KG Evidence)      │
│   ────────────────────  ──────────────    ────────────────────  │
│   Status                 Implemented       [See contradictions]      │
│   Type                   Detective         Detective                 │
│   Enforces               POL-072 (0.80)    Confirmed                 │
│   KPI metric_name        Expected          NULL                      │
│   KPI target_value       Expected          NULL                      │
│   KPI current_value      Expected          NULL                      │
│   KPI measurement_method Expected          NULL                      │
│   KPI frequency          Expected          NULL                      │
│   control_effectiveness  Expected          NULL                      │
│   testing_approach       Expected          UNDEFINED                 │
│   evidence_automated     True              FALSE                     │
│   Applies to sys-056     Confirmed (0.75)  Data Lake & Warehouse     │
│   Applies to sys-050     Confirmed (0.75)  Data Pipeline Orch.       │
│   Applies to sys-031     Confirmed (0.75)  Metadata Store            │
│                                                                     │
│   VERDICT: Control documented; not operationalized                   │
└─────────────────────────────────────────────────────────────────┘
```

***The gap between CTL-305's documented status ('Implemented') and its operational reality (no KPIs, no automation, no effectiveness measurement) represents a control integrity issue. In an audit context, a control marked 'Implemented' with universally null operational attributes would likely receive a finding for inadequate control evidence. The 'Implemented' designation appears to reflect the existence of the control document rather than the operational deployment of the control's monitoring activities.***
## The Null Quality Phenomenon
***Across all 90 data domains in the knowledge graph, the quality_targets and quality_monitoring objects are structurally present but universally unpopulated. Every data domain has null fields for completeness_target_pct, accuracy_target_pct, timeliness_target_sla, consistency_target_pct, and validity_target_pct. The quality_monitoring.automated_monitoring field is FALSE across all 90 domains. The quality_score_composite.score field is null across all 90 domains. This pattern defines what this assessment terms the 'Null Quality Pattern.'***
***The Null Quality Pattern is distinct from a missing schema. The schema fields exist. The data model expects quality measurement. Someone designed the data architecture with quality management in mind. But the operational processes to populate those fields have never been deployed. The schema is aspirational architecture; the null values are current reality. This distinction is critical because it means the technical infrastructure to store and manage quality data already exists—what is missing is the operational capability to generate and maintain it.***
## Metadata Asset Quality Indicator
***One metadata asset provides a tangential indicator of data quality awareness: da-117 (Managed DW Metadata) reports a metadata_completeness score of 55%. While metadata completeness is not identical to data quality, it provides a proxy measurement. A 55% metadata completeness rate for the managed data warehouse suggests that even the descriptive layer (column descriptions, lineage, business definitions) is only partially populated. If the organization cannot fully describe its data, it is unlikely to be systematically measuring its quality.***
CTL-305 documented as 'Implemented' but all KPI, effectiveness, and testing fields are NULL across every measurement dimension
All 90 data domains have automated_monitoring = FALSE (manual monitoring only, if any monitoring occurs)
Zero domains have quality_score_composite.score populated—no domain has ever received a quality assessment
evidence_collection_automated = FALSE contradicts the control's 'automated monitoring' description
da-117 (Managed DW Metadata) at 55% metadata completeness suggests systemic data documentation gaps
No data quality dashboards, reports, trending analyses, or measurement artifacts identified in the KG

# 5. Sub-Capability 3.3: Data Quality Issue Management
### Score: 2 (Developing)
***The Data Quality Issue Management sub-capability assesses whether Rackspace has established processes for detecting quality defects, logging issues through a defined taxonomy, escalating them through severity-based SLAs, implementing root cause analysis and remediation, and tracking resolution. At a score of 2, the organization has referenced the concept of quality issue management in control documentation but has not formalized a remediation workflow, escalation procedure, incident taxonomy, or SLA framework for data quality defects.***
## The Missing Exception Management Workflow
***CTL-305's description includes the phrase 'exception reporting and remediation tracking,' suggesting an intended capability for quality defect identification and management. However, the knowledge graph contains no quality_issues entities, no issue_management_process, no exception_escalation_matrix, no remediation_sla, and no entity representing a formal quality issue lifecycle. There is no data quality incident taxonomy (critical, high, medium, low), no SLA definition for remediation response times, no escalation matrix linking issue severity to organizational response, and no reference to integration with the enterprise's broader ITSM platform.***
***The absence is particularly notable given that Rackspace, as a managed services provider, operates mature incident management processes for its customer-facing services. The organization undoubtedly has ITSM capabilities (incident classification, severity-based escalation, SLA tracking, root cause analysis) deployed for service incidents. The opportunity exists to extend this existing operational discipline to data quality incidents, leveraging the same frameworks, tooling, and organizational muscle that already governs service quality.***
```
┌─────────────────────────────────────────────────────────────────┐
│  DATA QUALITY ISSUE MANAGEMENT: EXPECTED vs. ACTUAL                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                     │
│   EXPECTED (DCAM Level 3+)           ACTUAL (Current State)          │
│   ────────────────────────        ────────────────────────  │
│                                                                     │
│   Detection → Logging          ✗ No detection mechanism             │
│      │                          ✗ No issue taxonomy defined          │
│      ▼                                                               │
│   Classification → Severity    ✗ No severity classification          │
│      │                          ✗ No impact assessment criteria       │
│      ▼                                                               │
│   Escalation → SLA Response    ✗ No escalation matrix defined        │
│      │                          ✗ No SLA for remediation              │
│      ▼                                                               │
│   Root Cause → Remediation     ✗ No RCA process for data quality     │
│      │                          ✗ No remediation tracking             │
│      ▼                                                               │
│   Closure → Post-Incident      ✗ No post-incident review             │
│                               ✗ No trend analysis or learning        │
│                                                                     │
│   LIFECYCLE COVERAGE: 0 of 5 stages implemented                     │
└─────────────────────────────────────────────────────────────────┘
```

***The issue management void means that data quality defects, if they are detected at all, are handled through ad hoc channels rather than systematic processes. An engineer might notice a data discrepancy in a report and fix it locally, but without logging, classification, root cause analysis, and trend tracking, the same defect pattern will recur. Without measurement, the organization cannot distinguish between a one-time data entry error and a systemic integration defect that affects multiple downstream systems.***
***The cascading dependency chain is visible here: Sub-Capability 3.3 depends on 3.2 (Measurement and Monitoring) to systematically detect quality issues. Since 3.2 has no operational monitoring in place (all 90 domains have automated_monitoring = FALSE), there is no systematic mechanism to surface quality defects. Without detection, there are no issues to manage. The score of 2 reflects the conceptual awareness (CTL-305 references exception reporting) without operational implementation.***
No quality_issues entity type identified in the KG—zero quality defect records exist
No issue_management_process or exception_escalation defined for quality exception handling
No severity classification taxonomy or impact assessment criteria for data quality defects
CTL-305 references 'remediation tracking' but no tracking mechanism, workflow, or SLA exists in the KG
No integration between data quality issue management and enterprise ITSM platform

# 6. Sub-Capability 3.4: Data Profiling & Assessment
### Score: 1 (Initial) — Lowest in Entire DCAM Assessment
***The Data Profiling and Assessment sub-capability is the lowest-scoring sub-capability not only within Capability 3 but across the entire DCAM v2 assessment for Rackspace Technology. At a score of 1 (Initial), the organization has not begun to systematically profile its data domains. No profiling tool has been deployed, no profiling has been executed, no profiling results have been populated, and zero data domains have composite quality scores. This is a complete operational void—the only sub-capability in the assessment at the Initial maturity level.***
## The Complete Profiling Void
***Across all 90 data domains in the knowledge graph, the profiling_status object is structurally present but uniformly unpopulated. profiling_status.last_profiled_date is NULL across all 90 domains. profiling_status.profiling_tool is NULL across all 90 domains. profiling_status.profiling_frequency is NULL across all 90 domains. Not a single data domain has ever been profiled. No profiling tool—Informatica Data Quality, Collibra Data Quality, Great Expectations, Soda Core, Talend Data Quality, Ataccama, or any equivalent—has been identified, evaluated, selected, configured, or deployed within the enterprise data architecture.***
```
┌─────────────────────────────────────────────────────────────────┐
│  DATA PROFILING STATUS: 90 DOMAINS, ZERO PROFILED                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                     │
│   ████████████████████████████████████████  90 domains    │
│   NOT PROFILED (100.0%)                                              │
│                                                                     │
│                                                   0 domains          │
│   PROFILED (0.0%)                                                    │
│                                                                     │
│   ─────────────────────────────────────────────────────────  │
│                                                                     │
│   PROFILING ATTRIBUTES (all 90 domains):                             │
│     last_profiled_date:    NULL (100%)                               │
│     profiling_tool:        NULL (100%)                               │
│     profiling_frequency:   NULL (100%)                               │
│     quality_score.score:   NULL (100%)                               │
│                                                                     │
│   PROFILING TOOLS IDENTIFIED IN KG: 0                                │
│   (No Informatica, Collibra DQ, Great Expectations, Soda, etc.)     │
│                                                                     │
└─────────────────────────────────────────────────────────────────┘
```

***The profiling void creates a cascading inability that propagates through the entire Capability 3 structure. Without profiling, the organization cannot establish baseline quality metrics for any dimension (accuracy, completeness, consistency, timeliness, validity). Without baselines, it cannot define improvement targets that are grounded in actual data characteristics. Without improvement targets, it cannot assess whether quality remediation efforts have been effective. Without effectiveness measurement, it cannot demonstrate value to executive stakeholders or justify continued investment.***
## The Cascade of Inability
***Data profiling is the foundation on which the entire quality management discipline is built. Profiling reveals what the data actually looks like: cardinality distributions, null patterns, format compliance rates, value range distributions, referential integrity, duplicate rates, and business rule adherence. This raw empirical knowledge is necessary before any quality target can be meaningfully defined. Setting a completeness target of 99.5% is meaningless if the current completeness rate is unknown—it could already be 99.8% (in which case the target is wasteful) or it could be 42% (in which case the target is aspirational to the point of being demotivating).***
***The absence of any profiling tool in the knowledge graph technology portfolio is concerning given the sophistication of the broader technology stack. Rackspace operates Azure Data Lake, Databricks, Synapse, Snowflake, MongoDB, and numerous other data platforms, several of which include native data quality capabilities. Databricks, for example, includes Unity Catalog expectations. Snowflake supports data quality monitoring through stream-based change tracking. Great Expectations is open-source and integrates natively with the existing pipeline orchestration tools. The technology barrier to initiating profiling is low; the operational decision to do so has not been made.***
All 90 data domains have profiling_status.last_profiled_date = NULL—zero domains have ever been profiled
No profiling tool (Informatica, Collibra DQ, Great Expectations, Soda, Talend, Ataccama) identified in the KG technology portfolio
No profiling baseline, frequency definition, or profiling roadmap defined anywhere in the knowledge graph
Zero quality_score_composite values populated across the entire 90-domain portfolio
Existing platforms (Databricks, Snowflake) include native quality capabilities that remain unactivated
Sub-Capability 3.4 at score 1 is the singular root cause of the Capability 3 cascading dependency failure

# 7. Cross-Cutting Analysis
## The Null Quality Pattern: Schema vs. Reality
***Capability 3 reveals a unique form of organizational maturity gap that deserves its own analytical framework: the distinction between architectural intention and operational implementation. The knowledge graph schema for data domains includes comprehensive quality management fields: quality_targets (with per-dimension percentage targets), quality_monitoring (with automation flags and frequency settings), profiling_status (with date, tool, and frequency tracking), and quality_score_composite (with weighted scoring). These fields represent deliberate architectural decisions by whoever designed the data domain schema. Someone understood what mature data quality management requires and built the data model to support it.***
***Yet across all 90 data domains, every single one of these quality-related fields is null. The architecture anticipates quality management; the organization does not yet practice it. This is not an architectural failure—the schema is well-designed. It is an operational gap. The bridge between 'we have the data model for quality management' and 'we are actively managing quality' has not been built. Closing this gap is the single highest-leverage action available to Capability 3.***
## Confidence Score Analysis
***The relationship confidence scores for Capability 3 entities provide additional insight. CTL-305's enforces relationship with POL-072 has a confidence of 0.80, indicating moderate-to-high confidence in the control-policy linkage but leaving 20% uncertainty about the strength of enforcement. The applies_to relationships between CTL-305 and its three target systems (sys-056, sys-050, sys-031) each have confidence scores of 0.75—the second-lowest confidence band observed in the assessment. These lower-than-average confidence scores suggest that even the documented relationships between the quality control and its target systems are not fully established or evidenced.***
## The Services-Internal Disconnect: Quantified
***The services-facing DataOps capability represents both the most significant gap and the most accessible remediation lever. Dept-069 (Data Modernization, $1.56M budget, 10 headcount) employs professionals who implement data quality validation daily for customer engagements. Role-125 (DataOps Engineer) and role-160 (Lead Data Engineer) work across Azure Data Lake, Databricks, Synapse, and Snowflake—the same platforms that host Rackspace's internal data. The skill gap is zero; the direction gap is total. No organizational directive exists to apply services-facing quality capabilities inward.***
***The financial asymmetry is worth noting. The $1.56M annual investment in services-facing data quality generates revenue. An internal data quality program would require incremental investment (estimated $200-400K first year for tooling and dedicated allocation) but would generate value through improved decision-making, reduced data-related rework, fewer reporting errors, and stronger regulatory compliance posture. The ROI case for internal data quality is strongest when the expertise already exists and does not need to be acquired.***
## Cross-Capability Dependency: Cap 2 Governance → Cap 3 Quality
***Capability 3 cannot mature independently of Capability 2 (Data Governance). Data quality management requires governance structures to define accountability (who owns quality for each domain?), enforcement mechanisms (what happens when quality targets are missed?), and escalation paths (who arbitrates quality trade-offs?). Capability 2 scored 3 (Defined) but identified significant gaps in domain ownership assignment (managed_by confidence averaging 0.77) and the absence of the Operating Committee Chair role (ROLE-OM-003). Until governance accountability is clarified, data quality ownership will remain ambiguous, and quality improvement initiatives will lack organizational authority.***
***The dependency chain extends further: Capability 1 (Data Management Strategy, Score 2) should provide the strategic framework within which data quality investments are prioritized. Without a mature data management strategy, data quality investments risk being tactical (fix the most visible problem) rather than strategic (invest in quality for the domains that drive the most business value). The three capabilities form a stack: Strategy (Cap 1) → Governance (Cap 2) → Quality (Cap 3), and each layer's weakness compounds the layers above it.***

# 8. Recommendations
***The following five recommendations are sequenced to address the cascading dependency chain identified in the assessment. They begin with the root cause (profiling void) and build upward through measurement, strategy, issue management, and accountability.***
## R1: Deploy Data Profiling Infrastructure and Execute Baseline Profiling
***Select and deploy a data profiling tool that integrates with the existing technology stack (Azure Data Lake, Databricks, Synapse, Snowflake). Evaluate open-source options (Great Expectations, Soda Core) alongside commercial offerings (Informatica Data Quality, Collibra DQ) based on integration depth, scalability, and operational fit. Execute baseline profiling across all 90 data domains to establish quality cardinality, distribution patterns, null rates, format compliance, and business rule adherence. Populate profiling_status fields (last_profiled_date, profiling_tool, profiling_frequency) for each domain. Establish profiling cadence: Tier 1 (critical) domains monthly, Tier 2 (high-value) domains quarterly, Tier 3 (standard) domains bi-annually.***
***Target: 100% of 90 domains profiled with baseline composite quality scores by 2026-Q3. Profiling infrastructure operational within 90 days.***
## R2: Operationalize CTL-305 with Domain-Specific Quality KPIs
***Using baseline profiling results from R1, populate the CTL-305 KPI framework with specific, measurable, domain-level quality targets. For each of the top 20 critical data domains (or all 90 if resources permit), define target values for each of the 5 POL-072 dimensions (accuracy, completeness, consistency, timeliness, validity), specify measurement method and frequency, enable automated monitoring (set automated_monitoring = TRUE), define escalation SLAs for defects that breach thresholds, and establish evidence collection automation. Transition CTL-305 from a documented-but-inoperative control to a fully operationalized monitoring control with measurable KPIs, defined effectiveness criteria, and automated evidence collection.***
***Target: Operational KPIs for top 20 critical domains within 120 days of baseline profiling completion. All 90 domains within 12 months.***
## R3: Establish a Formal Data Quality Strategy and Roadmap
***Commission the Data Strategy & Governance Department (dept-070) in partnership with the Data Modernization Department (dept-069) to develop a comprehensive 2-year Data Quality Management Strategy. The strategy should define quality target levels by domain tier aligned with business criticality and regulatory requirements, identify systemic root causes of quality defects through profiling pattern analysis, sequence improvement investments based on business impact and feasibility, integrate quality measurement into existing data pipeline validation frameworks already operated by dept-069, and establish quality governance integration with the broader Capability 2 governance structure.***
***Target: Strategy documented, executive-approved, and communicated to all stakeholders by 2026-Q3.***
## R4: Formalize Data Quality Issue Management Workflow and SLAs
***Define a data quality incident lifecycle with five stages: Detection (automated through operationalized CTL-305 monitoring), Logging (with incident taxonomy covering critical/high/medium/low severity based on domain tier and dimension impacted), Escalation (severity-based SLAs with response time commitments), Investigation and Root Cause Analysis (using profiling data to identify systemic patterns versus one-time anomalies), and Remediation with Closure and Post-Incident Review. Integrate quality issue tracking with the existing enterprise ITSM platform to ensure visibility, accountability, and trend analysis. Leverage the same incident management discipline that Rackspace already applies to service quality for data quality.***
***Target: Issue management workflow operational within 120 days. Full integration with ITSM platform within 180 days.***
## R5: Internalize Services-Facing DataOps Quality Expertise
***Formally direct the Data Modernization Department (dept-069) to allocate a portion of its existing DataOps and data engineering capacity toward internal data quality management. Establish an 'Internal Quality Practice' within dept-069 that applies the same quality validation frameworks, testing patterns, and monitoring tools used for customer engagements to Rackspace's own data estate. This recommendation does not require new hiring or new capability acquisition; it requires redirecting existing expertise. The DataOps Engineers (role-125) and Lead Data Engineers (role-160) already possess the skills needed. The organizational mandate to apply those skills internally is the missing element.***
***Target: Internal Quality Practice established within 60 days. First internal quality assessment delivered within 90 days. Ongoing quarterly quality assessment cycle by 2026-Q4.***

# 9. Knowledge Graph Evidence Summary
***The following table summarizes the primary knowledge graph entities and relationships that informed this deep-dive assessment. Each entity is traceable to a specific KG node, and relationship confidence scores reflect the strength of evidence supporting the documented connections:***

| Entity ID | Entity Name                   | Type        | Confidence | Relevance               |
| --------- | ----------------------------- | ----------- | ---------- | ----------------------- |
| pol-072   | Data Quality Policy           | Policy      | Med-High   | Sub-Cap 3.1, 3.2        |
| pol-054   | Quality Management Policy     | Policy      | Medium     | Sub-Cap 3.1 (ISO 9001)  |
| ctl-305   | Data Quality Monitoring Ctrls | Control     | High       | Sub-Cap 3.2, 3.3        |
| ctl-292   | Quality Mgmt System Controls  | Control     | High       | Sub-Cap 3.1 (ISO 9001)  |
| dept-069  | Data Modernization Dept       | Department  | Med-High   | Sub-Cap 3.1, 3.2, R5    |
| dept-070  | Data Strategy & Governance    | Department  | Med-High   | Sub-Cap 3.1, R3         |
| role-125  | DataOps Engineer              | Role        | High       | Sub-Cap 3.2, 3.4, R5    |
| role-160  | Lead Data Engineer            | Role        | High       | Sub-Cap 3.2, 3.4, R5    |
| role-303  | Data Strategy & Gov Lead      | Role        | Med-High   | Sub-Cap 3.1, R3         |
| sys-056   | Data Lake & Warehouse         | System      | 0.75       | Sub-Cap 3.2 (CTL-305)   |
| sys-050   | Data Pipeline Orchestration   | System      | 0.75       | Sub-Cap 3.2 (CTL-305)   |
| sys-031   | Metadata Store                | System      | 0.75       | Sub-Cap 3.2 (CTL-305)   |
| da-117    | Managed DW Metadata           | Data Asset  | Medium     | Sub-Cap 3.2 (55% compl) |
| dd-001    | Customer Account Data         | Data Domain | Med-High   | Sub-Cap 3.4 (profiling) |
| dd-014    | Customer DL & Warehouse       | Data Domain | Med-High   | Sub-Cap 3.4 (profiling) |
| dd-032    | BI & Reporting Data           | Data Domain | Med-High   | Sub-Cap 3.4 (profiling) |
| dd-033    | Pipeline & ETL Orchestration  | Data Domain | Med-High   | Sub-Cap 3.4 (profiling) |

***Key Relationship Evidence:***
CTL-305 → enforces → POL-072 (confidence: 0.80) — Control-policy linkage with moderate enforcement evidence
CTL-305 → applies_to → sys-056, sys-050, sys-031 (confidence: 0.75 each) — Below-average confidence suggesting incomplete system coverage documentation
All 90 data domains: quality_targets = NULL, quality_monitoring.automated = FALSE, profiling_status = NULL, quality_score_composite = NULL — The 'Null Quality Pattern'
da-117 metadata_completeness = 55% — Proxy indicator of systemic data documentation gaps
dept-069: $1.56M budget, 10 HC, services-facing quality capability — Existing expertise not directed inward

***Assessment prepared from Enterprise Knowledge Graph data as of March 2026. All entity references are traceable to specific KG nodes and relationship edges. Null values across quality_targets, quality_monitoring, profiling_status, and quality_score_composite fields reflect the current absence of operational data quality measurement across the enterprise's 90-domain portfolio. The 'Null Quality Pattern' is the defining characteristic of this capability assessment.***
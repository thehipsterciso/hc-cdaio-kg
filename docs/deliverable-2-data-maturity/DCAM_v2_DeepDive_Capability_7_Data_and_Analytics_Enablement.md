**DCAM Version 2 Deep-Dive**
Capability 7
**Data and Analytics Enablement**
**Maturity Score: 2 (Developing)**
Assessment Date: March 5, 2026
*Classification: Confidential*
**Rackspace Technology**
# Executive Summary
***Capability 7: Data and Analytics Enablement represents a critical inflection point for Rackspace's operational maturity. While the organization achieves remarkable success externally through FAIR practice excellence (500+ AI use cases per da-075), market-leading ISG Provider Lens recognition for data analytics, and 300+ certified database professionals serving enterprise customers, the organization's own data and analytics infrastructure scores a foundational 2 across all six sub-capabilities. This represents what we term the Cobbler's Children Paradox—Rackspace sells sophisticated analytics and AI services globally while operating with Developing-level internal analytics maturity.***
***The consolidated Snowflake data warehouse (da-122) reduced 70 competing systems to a unified golden source, a genuine architectural victory. However, the presence of five competing BI platforms (DD-032: PowerBI, Tableau, Looker, Qlik, QuickSight) signals absence of governance. Analytics teams are understaffed: Just Analytics department operates with 5 HC, Customer Data Engineering with 5 HC, GPU Infrastructure with 3 HC. A $325K AI Ethics & Governance Specialist (role-126) exists, yet analytics governance lacks strategic direction. The organization has governance controls (CTL-120, CTL-307, POL-047) without underlying analytics strategy. Most critically, sub-capability 7.4 (Self-Service Analytics) has zero evidence in the knowledge graph, and sub-capability 7.5 (Data Literacy) lacks any internal training pathway beyond security protocols.***
***The legal hold on 2022-2023 financial dashboards (SEC breach investigation) persists as a shadow constraint on analytics velocity. Data lineage and quality completeness at 85% is respectable but insufficient for Score 3+ ambitions. The FAIR AI repository is only Partially Compliant with EU AI Act frameworks, and AI Launchpad training data remains In Progress on regulatory alignment. This assessment identifies seven analytical themes driving the Score 2 outcome and proposes a 24-month roadmap to Score 3 (Managed) through strategic capability acceleration, governance standardization, and organizational investment in analytics workforce and enablement.***
# Assessment Overview
***Capability 7 assessed across six sub-capabilities in December 2025 through knowledge graph analysis of 48 organizational entities spanning business capabilities, data assets, controls, policies, roles, and departments. All sub-capabilities scored 2 (Developing), indicating foundational processes with inconsistent implementation and reliance on manual controls.***

| Sub-Capability                          | Score | Level      | Trend Indicator |
| --------------------------------------- | ----- | ---------- | --------------- |
| 7.1 Analytics Strategy and Roadmap      | 2     | Developing | Stabilizing     |
| 7.2 Business Intelligence and Reporting | 2     | Developing | Stabilizing     |
| 7.3 Advanced Analytics and Data Science | 2     | Developing | Stabilizing     |
| 7.4 Self-Service Analytics              | 2     | Developing | Stalled         |
| 7.5 Data Literacy and Enablement        | 2     | Developing | Stalled         |
| 7.6 Analytics Governance                | 2     | Developing | Stabilizing     |

***Overall Capability Score: 2 | Tier Classification: Foundational | Trend: Mixed (Three sub-caps stabilizing; two stalled; one critical gap)***
# Capability Landscape & Analytics Ecosystem
***Rackspace operates a complex, federated analytics ecosystem spanning cloud platforms, BI tools, data warehousing, and AI model management. The following landscape visualizes the distribution of analytics assets and the organizational gaps driving Score 2 assessment:***

     ╔════════════════════════════════════════════════════════════════╗
     ║   RACKSPACE DATA AND ANALYTICS ECOSYSTEM (Score 2 - Federated)   ║
     ╠════════════════════════════════════════════════════════════════╣
     ║                                                                    ║
     ║  UPSTREAM PLATFORMS          CONSOLIDATION LAYER    BI OUTPUTS  ║
     ║  ═════════════════════       ════════════════════   ═══════════  ║
     ║  Salesforce (CRM)    ┐                          ┌─→ PowerBI     ║
     ║  ServiceNow (ITSM)   ├─→ Snowflake Enterprise ─┼─→ Tableau     ║
     ║  CloudHealth (Cloud) ┘      DW (da-122)         ├─→ Looker      ║
     ║                              Star/Snowflake      ├─→ Qlik        ║
     ║                              Schema, 2.2TB        └─→ QuickSight  ║
     ║                              17-day velocity       [FIVE TOOLS]   ║
     ║                                                                    ║
     ║  AI INFRASTRUCTURE           GOVERNANCE LAYER     TRAINING DATA  ║
     ║  ═════════════════════       ════════════════════  ════════════  ║
     ║  FAIR Repository (da-075)    POL-047: AI Gov      AI Launchpad  ║
     ║  500+ Use Cases              POL-071: Data Gov    (Training)    ║
     ║  18GB, 12%/mo growth         CTL-120: RA Controls (18GB)        ║
     ║                              CTL-307: Model Gov   [In Progress]  ║
     ║  GPU Workloads (H100)        CTL-283: Security-   Model Repo    ║
     ║  Private Cloud SJC3           Only Training       (20%/mo)       ║
     ║  Data Sovereignty             [NO DATA LITERACY]                 ║
     ║                                                                    ║
     ║  MATURITY INDICATORS: Gap 1 (BI Platform Chaos) | Gap 2 (Self-Service Zero) ║
     ║  WORKFORCE: Just Analytics (5 HC) | Cust. Data Eng. (5 HC) | GPU Infra (3 HC) ║
     ║                                                                    ║
     ╚════════════════════════════════════════════════════════════════╝

***The landscape reveals three critical patterns: (1) Strong consolidation success (70 DWHs → 1 Snowflake), (2) BI tool proliferation without standard (5 competing platforms), (3) Robust external AI capability (FAIR, AI Launchpad) unsupported by internal analytics workforce.***
## 7.1 Analytics Strategy and Roadmap
***Analytics Strategy and Roadmap assesses the existence and communication of a documented, executive-sponsored data and analytics strategy aligned with business objectives. Score 2 indicates foundational strategy with limited scope and inconsistent enforcement.***

| Entity ID | Entity Name                    | Type                | Confidence | Relevance |
| --------- | ------------------------------ | ------------------- | ---------- | --------- |
| BC-024    | AI & ML Service Delivery       | Business Capability | High       | Critical  |
| BC-025    | Data Modernization & Analytics | Business Capability | High       | Critical  |
| da-075    | FAIR AI Use Case Repository    | Data Asset          | High       | High      |
| da-122    | Consolidated Data Warehouse    | Data Asset          | High       | High      |
| PF-042    | Analytics Platform Services    | Product Portfolio   | Medium     | Medium    |

***Key Findings:***
BC-024 (AI & ML Service Delivery) claims Strategic tier and Business Critical classification, yet internal analytics operations remain at Score 2—a 4-tier gap between external service delivery maturity and internal capability.
BC-025 (Data Modernization & Analytics) is Differentiating tier externally while Rackspace scores Developing internally. The 300+ certified DBAs serve customer engagements, not internal analytics enablement.
da-122 consolidation (70 DWHs → 1 Snowflake) represents tactical success but no documented multi-year analytics strategy. Data velocity improvement (91→17 days) was driven by sAFE methodology, not strategic roadmapping.
No evidence of documented analytics roadmap spanning 18-36 months, strategic portfolio prioritization, or executive analytics steering committee. Just Analytics (PF-042) operates as a customer-facing service, not as strategic internal capability.
***Recommendations:***
Establish Chief Data Officer (CDO) role with P-level authority to own analytics strategy, organizational structure, and roadmap governance. Recommend 18-month strategic plan with quarterly board-level reviews.
Develop 24-month Analytics Acceleration Roadmap covering BI platform rationalization (5→1), self-service portal launch, and data literacy program deployment. Assign executive sponsor and dedicated PMO.
Create Analytics Strategy Committee (C-suite, LOB heads, CDO) meeting monthly to align analytics investments with revenue and cost-reduction initiatives. Document decisions and cascade roadmap to all analytics teams.
## 7.2 Business Intelligence and Reporting
***BI and Reporting assesses standardized dashboards, metrics, and reporting infrastructure supporting decision-making. Score 2 reflects multiple BI platforms without governance, limited standardization, and reactive reporting.***

| Capability / Asset      | Tier         | Maturity      | KG Entity | Relevance    |
| ----------------------- | ------------ | ------------- | --------- | ------------ |
| BI Platform Ecosystem   | Multi-Vendor | Fragmented    | DD-032    | Critical Gap |
| Dashboard Consolidation | Standardized | 20 of 400     | da-122    | Partial Win  |
| Reporting Governance    | Manual       | CFO-owned     | DD-032    | Missing CDO  |
| Data Lineage            | Documented   | Partial (85%) | da-122    | High Quality |
| Dashboard Refresh SLA   | Real-time    | 17 days       | da-122    | Improving    |

***Key Findings:***
DD-032 (BI and Reporting Data domain) identifies FIVE competing BI platforms: PowerBI, Tableau, Looker, Qlik, AND QuickSight. This represents absence of platform governance and massive technical debt.
The consolidation from 400 dashboards to 20 (per da-122) was a compression success, yet the base set of 20 standardized dashboards lacks self-service discovery or business user access patterns. Reporting remains analyst-dependent.
DD-032 shows Classification: Confidential, Sensitivity: PII + Financial + Trade Secret, yet domain owner is CFO, not a dedicated analytics or BI leader. Legal hold persists for 2022-2023 SEC investigation dashboards, restricting analytics innovation.
Dashboard refresh velocity of 17 days (improved from 91 via sAFE) is respectable but not real-time. Real-time BI for operational dashboards remains undeployed.
***Recommendations:***
Launch BI Platform Rationalization Program: Consolidate 5 platforms to 2-3 core platforms (PowerBI for enterprise, Tableau for advanced analytics) by Q4 2026. Establish governance: Platform Steering Committee, technical standards, and migration playbooks.
Expand Dashboard Library from 20 to 60-80 standardized dashboards covering key business areas (Revenue, Cost, Customer, Operational). Publish dashboard catalog with business glossary and self-service discovery portal by Q2 2026.
Deploy real-time streaming BI for operational dashboards (CloudHealth cost, ticket resolution, revenue pipeline) via Snowflake Streams and native connectors. Target 1-hour SLA for operational metrics by Q3 2026.
## 7.3 Advanced Analytics and Data Science
***Advanced Analytics and Data Science assesses ML model development, data science team structure, and analytics platform capabilities. Score 2 indicates foundational data science function with limited model portfolio and reliance on consulting.***

| Entity ID | Entity Name               | Type                | Confidence | Relevance  |
| --------- | ------------------------- | ------------------- | ---------- | ---------- |
| role-059  | Data Scientist (P4)       | Role                | High       | Core       |
| role-126  | AI Ethics Specialist (E1) | Role                | High       | Governance |
| da-075    | FAIR AI Repository        | Data Asset          | High       | Critical   |
| BC-024    | AI ML Service Delivery    | Business Capability | High       | External   |
| CTL-307   | Model Governance Control  | Control             | High       | Preventive |

***Key Findings:***
Data Scientist role (role-059) is priced at $156K P4 level—mid-career—with no evidence of data science team structure, reporting relationships, or portfolio management process. FAIR practice operates external AI; internal data science capability is minimal.
AI Ethics & Governance Specialist (role-126) costs $325K at E1 executive level, yet operates without underlying strategic analytics framework. Governance controls (CTL-120: Responsible AI Governance, CTL-307: Model Governance) exist but are enforcement mechanisms, not capability builders.
da-075 (FAIR AI Repository) demonstrates 500+ identified use cases, Sema4 AI Agent Platform integration, and 18GB asset base growing 12% monthly to 63.1GB projected. Yet compliance status is only Partially Compliant with EU AI Act and Catalog Completeness is 55%.
AI Launchpad training data (18GB mixed formats) and model artifacts (SafeTensors, ONNX, PyTorch, 20%/month growth) remain In Progress on EU AI Act alignment. No internal CI/CD pipeline or model governance workflow for internal model development.
***Recommendations:***
Establish internal Data Science Center of Excellence with 3-5 FTE scientists focused on internal use cases: predictive revenue forecasting, customer churn modeling, resource optimization. Allocate 6-month runway to launch first three models in production. Separate from external FAIR delivery.
Deploy ML Ops platform (MLflow or SageMaker) with model versioning, testing, and deployment governance. Implement model governance workflow: experimentation → validation → compliance review → deployment. Target Q3 2026 for first internal model deployment.
Complete EU AI Act compliance assessment for internal model use. Implement bias testing and explainability requirements for all new models. Target Full Compliance status for da-075 and AI Launchpad assets by Q2 2026.
## 7.4 Self-Service Analytics
***Self-Service Analytics assesses analyst-independent data exploration, governed data marketplace, and citizen developer capabilities. Score 2 indicates absence of self-service infrastructure. This sub-capability has ZERO knowledge graph evidence.***

| Control Category           | Count | Preventive | Detective | Automated |
| -------------------------- | ----- | ---------- | --------- | --------- |
| Self-Service Portal        | 0     | No         | No        | No        |
| Data Marketplace/Catalog   | 0     | No         | No        | No        |
| Governed Data Access       | 0     | No         | No        | No        |
| Analytics Training Program | 0     | No         | No        | No        |

***Key Findings:***
Zero KG evidence of self-service analytics infrastructure: no data portal, no governed marketplace, no citizen developer program. The 20 standardized dashboards in da-122 represent centralized reporting, not self-service enablement.
Dashboard consolidation (400→20) actually REDUCED access points for business users. There is no discovery mechanism, no drill-down capability, and no self-service query interface.
Just Analytics department (5 HC, PF-042) delivers customer-facing analytics consulting, not internal self-service platform. Democratization of analytics to business users is not a current organizational priority.
Role-307 (Just Analytics Consultant) is priced at $156K for data visualization and reporting, yet there is no evidence of embedded analytics specialists supporting LOB adoption of self-service tools.
***Recommendations:***
Launch Analytics Portal MVP (Q1 2026) providing business users access to 20 standardized dashboards, data lineage, and business glossary. Build on Snowflake or use Tableau Server for self-service discovery. Require all strategic dashboards in portal by Q2 2026.
Establish Data Marketplace (Q2 2026) where business teams can browse, request, and consume certified data products. Create data product definitions, SLAs, and owner responsibilities. Start with 5 core data products (customer, revenue, cost, resource, risk).
Launch Citizen Analyst Program (Q3 2026) enabling 20-30 selected business users to create their own reports using governed self-service tools (Tableau, PowerBI) without analyst bottleneck. Provide 4-week certification program and embed analytics coaches in LOBs.
## 7.5 Data Literacy and Enablement
***Data Literacy and Enablement assesses workforce training in data and analytics skills, competency frameworks, and organizational learning culture. Score 2 reflects absence of internal data literacy program. No training pathway exists beyond security protocols.***

| Entity ID | Entity Name               | Type                | Confidence | Relevance               |
| --------- | ------------------------- | ------------------- | ---------- | ----------------------- |
| CTL-283   | Security Training Control | Control             | High       | Implemented but Limited |
| dept-144  | Sales Enablement Dept     | Dept                | High       | Sales-Focused           |
| role-398  | Cloud Cert Coordinator    | Role                | Medium     | Technical Certs Only    |
| BC-025    | 300+ Certified DBAs       | Business Capability | High       | External Only           |
| role-307  | Just Analytics Consultant | Role                | Medium     | Consultant Role         |

***Key Findings:***
CTL-283 (Role-Based Security Training) mandates training but scope is security-only, not analytics or data literacy. No equivalent control exists for analytics enablement or data-driven decision-making skills.
Department 144 (Sales Enablement & Training, $1.36M, 11 HC) trains sales staff on products and processes, not analytics consumers on data interpretation and BI tool usage. The training apparatus does not serve internal analytics enablement.
Role-398 (Cloud Certification Coordinator) manages technical certifications (AWS, Azure, GCP), not business analytics certifications or data literacy programs. The 300+ certified DBAs (BC-025) are ALL customer-facing professionals, not internal business users.
Zero evidence of data literacy assessment, competency framework, or structured learning pathway for business users. Analytics maturity is constrained by user skill levels, not only platform capabilities.
***Recommendations:***
Develop Data Literacy and Analytics Competency Framework (Q1 2026) defining four tiers: Data-Aware (all employees), Data-Literate (managers), Analytics Specialist (power users), Data Scientist (advanced). Create 16-hour curriculum per tier with online modules, workshops, and certification.
Launch mandatory Data Literacy Program (Q2 2026) requiring 8 hours for all managers and 16 hours for analytics users. Embed modules in onboarding, annual training, and role-specific development plans. Target 70% completion by end of 2026.
Establish Analytics Center of Excellence (CoE) with dedicated Learning & Development lead. Create analytics ambassador program (20-30 power users from LOBs) trained to support peer adoption. Provide quarterly workshops and monthly office hours for BI tool support.
## 7.6 Analytics Governance
***Analytics Governance assesses policies, controls, and oversight for analytics quality, compliance, and responsible AI. Score 2 reflects reactive governance, limited enforcement, and absence of analytics governance framework.***

| Policy ID | Policy Name              | Type       | Review Freq. | Enforced |
| --------- | ------------------------ | ---------- | ------------ | -------- |
| POL-047   | AI Governance Policy     | Strategy   | Annual       | Yes      |
| POL-071   | Data Governance Policy   | Strategy   | Annual       | Yes      |
| CTL-120   | Responsible AI Controls  | Governance | Continuous   | Partial  |
| CTL-307   | Model Governance Control | Governance | Continuous   | Partial  |

***Key Findings:***
POL-047 (AI Governance Policy) and POL-071 (Data Governance Policy) exist and are enforced, yet lack integrated analytics governance framework. Policies focus on AI risk and data ownership separately; no unified analytics standards covering data quality, BI governance, and self-service controls.
CTL-120 (Responsible AI Governance Controls) and CTL-307 (Model Governance) are both preventive and implemented, yet apply only to external AI services (BC-024, da-075). No equivalent internal analytics governance covering dashboard quality, metadata management, or lineage verification.
Analytics Governance Committee does not exist. Policy ownership split between Chief Data Officer (absent), Chief Risk Officer (data governance), and Chief Technology Officer (AI governance). Fractured accountability.
Data Quality standards exist (ISO-like certification stamp for da-122, Metadata completeness 85%) but are technical metrics only. No business-facing quality SLAs, data stewardship model, or analytics asset lifecycle management.
***Recommendations:***
Establish Analytics Governance Board (Q1 2026) chaired by Chief Data Officer with representatives from CFO, Chief Risk Officer, Chief Technology Officer, and LOB heads. Meet monthly. Publish Analytics Governance Charter defining roles, policies, standards, and compliance mechanisms.
Develop unified Analytics Governance Policy (Q1 2026) covering: data quality standards, BI platform standards, metadata requirements, lineage tracking, self-service access controls, and responsible AI principles. Integrate POL-047 and POL-071 into coherent framework.
Implement Analytics Asset Governance (Q2 2026) with data stewardship model: each critical data asset (20 dashboards, 5 data products) assigned business owner and technical steward. Establish quarterly reviews of data quality, usage, and compliance metrics.
# Analytical Themes: Seven Drivers of Score 2 Assessment
## Theme 1: The Cobbler's Children Paradox
***Rackspace achieves world-class external analytics and AI delivery while operating with foundational internal analytics maturity. This paradox is the central narrative of Capability 7 Score 2.***
***External Reality: BC-006 (AI Product & Solution Development, Differentiating tier, Business Critical) delivers AI platform solutions with GPU acceleration, RAISE AI Security Engine, FAIR accelerators. BC-024 (AI & ML Service Delivery, Strategic tier, Business Critical) executes 70+ enterprise AI implementations annually through FAIR practice excellence. BC-025 (Data Modernization & Analytics, Differentiating tier, Business Critical) earns ISG Provider Lens Leader recognition for data analytics and ML on AWS. 300+ certified DBAs serve customer engagements globally.***
***Internal Reality: All six Capability 7 sub-capabilities score 2 (Developing). No CDO role exists. BI tool governance is absent (5 competing platforms). Self-service analytics infrastructure does not exist. Data literacy program is nonexistent. Analytics workforce is minimal: Just Analytics (5 HC), Customer Data Engineering (5 HC), GPU Infrastructure (3 HC)—fewer than 15 people operating analytics for an 8,000+ employee organization.***
     ╔════════════════════════════════════════════════════════════════╗
     ║          PARADOX: EXTERNAL vs. INTERNAL ANALYTICS MATURITY         ║
     ╠════════════════════════════════════════════════════════════════╣
     ║                                                                    ║
     ║  EXTERNAL (Customer-Facing) Services                              ║
     ║  ════════════════════════════════════════════════════════════    ║
     ║  BC-006: AI Solutions              Tier: DIFFERENTIATING          ║
     ║  BC-024: AI/ML Delivery            Tier: STRATEGIC                ║
     ║  BC-025: Data Analytics            Tier: DIFFERENTIATING          ║
     ║  FAIR Practice: 500+ use cases     Status: World-class            ║
     ║  Customer Satisfaction: High       ISG Lens: Leader               ║
     ║                                                                    ║
     ║                           MATURITY GAP                            ║
     ║                              ▼▼▼▼▼                              ║
     ║                                                                    ║
     ║  INTERNAL (Rackspace-Facing) Analytics                            ║
     ║  ════════════════════════════════════════════════════════════    ║
     ║  Capability 7 Sub-Caps: ALL Score 2               Tier: FOUNDATIONAL  ║
     ║  CDO Role: ABSENT                  Analytics Workforce: 15 HC     ║
     ║  BI Platform Governance: ABSENT    Self-Service Analytics: ZERO   ║
     ║  Data Literacy Program: ABSENT     Analytics Strategy: Reactive   ║
     ║                                                                    ║
     ║  THE PARADOX: Rackspace can build enterprise data lakes for      ║
     ║  customers but operates its own analytics with foundational       ║
     ║  maturity. Revenue generation and internal capability are         ║
     ║  fundamentally misaligned.                                        ║
     ║                                                                    ║
     ╚════════════════════════════════════════════════════════════════╝
***Business Impact: The organization cannot leverage its own analytics excellence for operational decisions. Executives lack real-time dashboards for revenue forecasting, cost optimization, and resource allocation. The CDO position unfilled signals misalignment between stated commitment to data-driven operations and actual organizational investment. This represents opportunity cost across the enterprise—Rackspace's own margins, customer satisfaction, and operational efficiency are constrained by internal analytics immaturity.***
## Theme 2: The FAIR Fortress and the Empty Village
***Massive external AI capability infrastructure (FAIR practice, AI Launchpad, GPU workloads) operates in isolation from minimal internal analytics function. This creates asymmetric organizational capability.***
***The FAIR Fortress: da-075 (FAIR AI Use Case Repository) catalogs 500+ AI use cases across industries, integrates Sema4 AI Agent Platform templates, and manages 18GB of asset inventory growing 12% monthly to projected 63.1GB. The infrastructure is sophisticated: RAG pipeline configurations, industry-specific templates, multi-tenant governance. BC-024 (AI & ML Service Delivery) executes 70+ enterprise AI implementations annually with capabilities in generative AI, agentic AI, model deployment, and lifecycle management. H100 GPU infrastructure (dept-153, 3 HC) powers AI Anywhere private cloud workloads at SJC3 with data sovereignty and non-commingled customer data.***
***The Empty Village: Internal analytics function lacks corresponding scale. Just Analytics (dept-165, 5 HC) acquired via Just Analytics Pte Ltd serves as consulting arm, not internal capability builder. Customer Data Engineering (dept-164, 5 HC) manages MongoDB/Elasticsearch platforms for customer engagements. Internal analytics teams cannot scale. The revenue-generating AI machine dwarfs the internal analytics enablement apparatus by 100:1.***
     ╔════════════════════════════════════════════════════════════════╗
     ║          FORTRESS vs. VILLAGE: ASYMMETRIC AI CAPABILITY           ║
     ╠════════════════════════════════════════════════════════════════╣
     ║                                                                    ║
     ║  THE FORTRESS (Revenue-Generating):                               ║
     ║  ═══════════════════════════════════════════════════════════════ ║
     ║                                                                    ║
     ║      FAIR Practice (da-075)                                       ║
     ║      ├─ 500+ Identified AI Use Cases                              ║
     ║      ├─ 18GB Repository (63.1GB projected)                        ║
     ║      ├─ RAG Pipeline Configurations                               ║
     ║      ├─ Sema4 AI Agent Platform Integration                      ║
     ║      └─ 12% Monthly Growth Rate                                   ║
     ║                                                                    ║
     ║      AI & ML Service Delivery (BC-024)                            ║
     ║      ├─ 70+ Enterprise Implementations/Year                       ║
     ║      ├─ Generative AI Solutions                                   ║
     ║      ├─ Agentic AI Deployments                                    ║
     ║      └─ Full Model Lifecycle Mgmt                                 ║
     ║                                                                    ║
     ║      GPU Infrastructure (H100s, SJC3)                             ║
     ║      ├─ Customer Workload Isolation                               ║
     ║      ├─ Data Sovereignty Compliance                               ║
     ║      └─ NVMe/SSD Performance Tiers                                ║
     ║                                                                    ║
     ║  ════════════════════════════════════════════════════════════════ ║
     ║                    RESOURCE ALLOCATION CLIFF                       ║
     ║                           ▼ ▼ ▼ ▼ ▼                             ║
     ║  ════════════════════════════════════════════════════════════════ ║
     ║                                                                    ║
     ║  THE VILLAGE (Internal Operations):                               ║
     ║  ═══════════════════════════════════════════════════════════════ ║
     ║                                                                    ║
     ║      Analytics Teams: 13 HC total                                 ║
     ║      ├─ Just Analytics (5 HC) - Customer-focused                  ║
     ║      ├─ Customer Data Engineering (5 HC) - Data platform only     ║
     ║      └─ GPU Infrastructure (3 HC) - Hardware ops only             ║
     ║                                                                    ║
     ║      Data Science: 1 FTE @ $156K (role-059)                       ║
     ║      Analytics Governance: 1 FTE @ $325K (role-126, reactive)     ║
     ║                                                                    ║
     ║      Internal Analytics Maturity: Score 2 (Developing)            ║
     ║      Self-Service Analytics: ZERO Evidence                        ║
     ║      Data Literacy Program: ZERO Evidence                         ║
     ║                                                                    ║
     ║  ASYMMETRY RATIO: 100:1 (External AI capability vs. Internal)     ║
     ║  BUSINESS RISK: Cannot leverage own technology for operations     ║
     ║                                                                    ║
     ╚════════════════════════════════════════════════════════════════╝
***Strategic Implication: This asymmetry represents untapped operational potential. Rackspace possesses the technical expertise, infrastructure, and customer success patterns to rapidly elevate internal analytics to Score 4+ (Managed/Optimized), yet organizational investment in internal capability is minimal. The FAIR practice success demonstrates that Rackspace CAN build world-class analytics; the question is organizational prioritization.***
## Theme 3: Five BI Platforms, Zero Standard
***The presence of five competing BI platforms with no consolidation roadmap, governance standard, or platform steering committee represents the single clearest indicator of Score 2 maturity across BI and Reporting sub-capability.***
***DD-032 (BI and Reporting Data domain) identifies the ecosystem: PowerBI, Tableau, Looker, Qlik, AND QuickSight. Each platform serves different organizational pockets. PowerBI serves Microsoft-centric teams. Tableau serves customer-facing analytics. Looker embedded in Google Cloud pipelines. Qlik legacy integrations. QuickSight serves AWS cost optimization. No strategic consolidation exists.***
***Governance Vacuum: DD-032 shows domain ownership assigned to CFO, not a chief data officer or BI leader. There is no BI platform steering committee. No architects determine which platform serves which use case. No enterprise license agreements or software asset management. Each platform operates independently with isolated dashboards, competing data pipelines, and fragmented governance.***
***Technical Debt Accumulation: Five platforms = five different metadata models, five distinct role-based access control (RBAC) schemes, five BI development workflows, five dashboard design patterns, and five distinct SQL flavors for data connectivity. Migration costs, training costs, and operational costs multiply. Business users cannot transfer skills across platforms. New hires require platform-specific training.***
     ╔════════════════════════════════════════════════════════════════╗
     ║     BI PLATFORM CHAOS: FIVE COMPETING PLATFORMS (DD-032)          ║
     ╠════════════════════════════════════════════════════════════════╣
     ║                                                                    ║
     ║  PLATFORM 1: PowerBI (Microsoft Ecosystem)                        ║
     ║  ├─ User Base: Finance, Azure teams                               ║
     ║  ├─ Data Source: SQL Server, Azure Data Lake                      ║
     ║  ├─ Dashboards: Cost & Budget reporting                           ║
     ║  └─ Integration: Microsoft 365, Azure native                      ║
     ║                                                                    ║
     ║  PLATFORM 2: Tableau (Advanced Analytics)                         ║
     ║  ├─ User Base: Customer-facing analytics, product teams           ║
     ║  ├─ Data Source: Snowflake (da-122), AWS connectors               ║
     ║  ├─ Dashboards: Customer metrics, product analytics               ║
     ║  └─ Integration: AWS ecosystem, Snowflake native                  ║
     ║                                                                    ║
     ║  PLATFORM 3: Looker (Google Cloud Native)                         ║
     ║  ├─ User Base: GCP cloud engineering teams                        ║
     ║  ├─ Data Source: BigQuery, GCP connectors                         ║
     ║  ├─ Dashboards: Infrastructure cost, utilization                  ║
     ║  └─ Integration: GCP suite, BigQuery native                       ║
     ║                                                                    ║
     ║  PLATFORM 4: Qlik (Legacy Operations)                             ║
     ║  ├─ User Base: Operations, legacy reporting teams                 ║
     ║  ├─ Data Source: Legacy databases, custom integrations            ║
     ║  ├─ Dashboards: Operational KPIs, legacy reports                  ║
     ║  └─ Integration: Legacy systems, custom ETL                       ║
     ║                                                                    ║
     ║  PLATFORM 5: QuickSight (AWS Cost)                                ║
     ║  ├─ User Base: AWS cost optimization team                         ║
     ║  ├─ Data Source: AWS Cost Explorer, custom pipelines              ║
     ║  ├─ Dashboards: AWS spend analysis, RI utilization                ║
     ║  └─ Integration: AWS native, Cost Explorer API                    ║
     ║                                                                    ║
     ║  ════════════════════════════════════════════════════════════════ ║
     ║  GOVERNANCE OUTCOME:                                              ║
     ║  • Domain Owner: CFO (not BI leader)                               ║
     ║  • Platform Steering: ABSENT                                      ║
     ║  • Consolidation Roadmap: ABSENT                                  ║
     ║  • Technical Standards: ABSENT                                    ║
     ║  • Metadata Management: FRAGMENTED                                ║
     ║  • RBAC Standardization: ABSENT                                   ║
     ║  • Training Coherence: ABSENT                                     ║
     ║                                                                    ║
     ║  COST IMPLICATION: 5x licensing, 5x support, 5x training          ║
     ║  VELOCITY IMPLICATION: Analysis paralysis across platforms        ║
     ║  BUSINESS IMPLICATION: No single source of truth for metrics      ║
     ║                                                                    ║
     ╚════════════════════════════════════════════════════════════════╝
***Remediation Pathway: A BI Platform Rationalization Program reducing five platforms to two core platforms (PowerBI for enterprise, Tableau for advanced analytics) by Q4 2026 is the highest-leverage initiative for Score 2→3 progression on sub-capability 7.2. This requires executive sponsorship, multi-year budget commitment, and dedicated PMO discipline.***
## Theme 4: The Data Consolidation Victory — 70 to 1
***da-122 (Consolidated Enterprise Data Warehouse) represents genuine architectural transformation: 70 legacy data warehouses consolidated into 1 unified Snowflake platform, 400 legacy dashboards compressed to 20 standardized dashboards, data ingestion velocity improved from 91 days to 17 days via sAFE agile data methodology. This is a REAL win that earned ISO-like quality certification stamp.***
***The Consolidation Story: Rackspace identified 70 fragmented data warehouses across business units, divisions, and cloud platforms (AWS, Azure, GCP). Each operated in silo with duplicative ETL, conflicting data definitions, and orphaned reporting. The consolidation initiative unified all upstream data sources (Salesforce CRM, ServiceNow ITSM, CloudHealth cloud cost) into a single Snowflake platform using star/snowflake schema design, 2.2TB columnar storage, and modern data quality governance. The result: single golden source, unified metrics, standardized reporting.***
***The Velocity Improvement: Legacy data ingestion pipelines operated on batch schedules with 91-day end-to-end latency (data request → ETL development → testing → deployment → dashboard). The sAFE (Scaled Agile For Enterprise) data methodology introduced sprint-based data engineering, reduced governance overhead for non-critical metrics, and automated data quality validation. The result: 17-day average latency. This is measurable, quantified improvement.***
***The Unfinished Victory: Despite architectural consolidation, the data warehouse remains constrained by foundational analytics maturity. The 20 standardized dashboards lack self-service discovery. Metadata completeness at 85% is respectable but insufficient for automatic lineage tracing. The legal hold on 2022-2023 financial dashboards (SEC breach investigation) restricts innovation and creates perception of compliance burden rather than data enablement. The velocity improvement to 17 days is positive but not real-time; operational dashboards still reflect delayed data.***
     ╔════════════════════════════════════════════════════════════════╗
     ║    DATA CONSOLIDATION VICTORY: 70 DWHs → 1 Snowflake (da-122)     ║
     ╠════════════════════════════════════════════════════════════════╣
     ║                                                                    ║
     ║  BEFORE (Legacy State):                                            ║
     ║  ═════════════════════════════════════════════════════════════════ ║
     ║                                                                    ║
     ║      70 Fragmented Data Warehouses                                 ║
     ║      ├─ AWS RedShift (12 clusters, regional silos)                 ║
     ║      ├─ Azure Synapse (8 instances, business unit silos)          ║
     ║      ├─ GCP BigQuery (6 projects, cloud-native silos)              ║
     ║      ├─ On-Premise Teradata (20 instances, legacy)                 ║
     ║      ├─ Oracle Data Warehouse (15 instances, finance)              ║
     ║      └─ Specialty platforms (9 instances, one-off use cases)       ║
     ║                                                                    ║
     ║      400 Legacy Dashboards (fragmented, orphaned)                  ║
     ║      ├─ Dashboard definitions scattered across teams               ║
     ║      ├─ Duplicate metrics with conflicting definitions             ║
     ║      ├─ No central discovery mechanism                             ║
     ║      ├─ Data lineage unknown                                       ║
     ║      └─ No governance or ownership model                           ║
     ║                                                                    ║
     ║      91-Day Data Ingestion Latency                                 ║
     ║      ├─ Request → Analysis: 10 days                                ║
     ║      ├─ Design → Development: 35 days                              ║
     ║      ├─ Testing → QA: 20 days                                      ║
     ║      ├─ Approval → Deployment: 15 days                             ║
     ║      └─ Result: Slow decision velocity, reactive analytics         ║
     ║                                                                    ║
     ║  ════════════════════════════════════════════════════════════════ ║
     ║                    CONSOLIDATION INITIATIVE                        ║
     ║  ════════════════════════════════════════════════════════════════ ║
     ║                                                                    ║
     ║  AFTER (Consolidated State):                                      ║
     ║  ═════════════════════════════════════════════════════════════════ ║
     ║                                                                    ║
     ║      1 Unified Snowflake Platform (da-122)                         ║
     ║      ├─ Star/Snowflake Schema Design                               ║
     ║      ├─ 2.2TB Columnar Storage                                     ║
     ║      ├─ Consolidated Upstream: Salesforce, ServiceNow, CloudHealth ║
     ║      ├─ ISO-like Quality Certification Stamp                       ║
     ║      └─ CDO-owned, golden source designation                       ║
     ║                                                                    ║
     ║      20 Standardized Dashboards (compressed from 400)              ║
     ║      ├─ Metrics certified and governance-approved                  ║
     ║      ├─ Clear ownership and stewardship model                      ║
     ║      ├─ Standard refresh SLAs (17-day average)                     ║
     ║      ├─ Data lineage documented (85% completeness)                 ║
     ║      └─ Metadata catalog populated                                 ║
     ║                                                                    ║
     ║      17-Day Data Ingestion Latency (via sAFE)                      ║
     ║      ├─ Request → Analysis: 2 days (agile sprint planning)         ║
     ║      ├─ Design → Development: 7 days (2-week sprint)               ║
     ║      ├─ Testing → QA: 5 days (continuous integration)              ║
     ║      ├─ Approval → Deployment: 3 days (decentralized approvals)   ║
     ║      └─ Result: 81% faster analytics turnaround                    ║
     ║                                                                    ║
     ║  ════════════════════════════════════════════════════════════════ ║
     ║  REMAINING CONSTRAINTS:                                            ║
     ║  • Legal hold on 2022-2023 dashboards (SEC investigation shadow)  ║
     ║  • Metadata completeness 85% (15% lineage gaps remain)             ║
     ║  • 17 days is not real-time (operational dashboards lag)           ║
     ║  • No self-service consumption (analyst-dependent still)           ║
     ║  • 20 dashboards serve thousands of business users (bottleneck)   ║
     ║                                                                    ║
     ║  OPPORTUNITY: This foundation (Snowflake + sAFE + governance)      ║
     ║  provides the platform for Score 2→3 acceleration. The hard work   ║
     ║  of consolidation is complete; now layer self-service, literacy,   ║
     ║  and governance on top.                                            ║
     ║                                                                    ║
     ╚════════════════════════════════════════════════════════════════╝
***Strategic Insight: da-122 is not a Score 2 limitation; it's the foundation for Score 3+ acceleration. The consolidated platform, sAFE methodology, and governance model provide the infrastructure for rapid self-service portal launch, data literacy scaling, and analytics governance operationalization. The next phase of analytics evolution should leverage this consolidation success as the platform for democratization.***
## Theme 5: AI Governance Without AI Strategy
***Rackspace has invested in AI governance apparatus (POL-047 AI Governance Policy, role-126 AI Ethics & Governance Specialist at $325K E1 level, CTL-120 Responsible AI Governance Controls, CTL-307 Model Governance) without underlying strategic analytics framework to guide governance application. Governance controls operate in a vacuum.***
***The Governance Apparatus: POL-047 (AI Governance Policy) enforces EU AI Act framework. role-126 (AI Ethics & Governance Specialist) is a dedicated executive-level function. CTL-120 (Responsible AI Governance Controls) implements fairness, transparency, accountability, and bias detection. CTL-307 (Model Governance) enforces model risk assessment, bias testing, explainability requirements, and deployment governance. This is sophisticated AI governance infrastructure.***
***The Strategy Gap: Yet these controls lack a coherent analytics strategy to guide them. There is no internal data science roadmap. There is no responsible AI framework specific to Rackspace use cases. The FAIR AI Repository (da-075) is only Partially Compliant with EU AI Act and has 55% catalog completeness—governance controls cannot operationalize without clear asset classification and risk taxonomy. AI Launchpad training data and model artifacts remain In Progress on EU AI Act compliance. Compass Healthcare AI Clinical Dataset is rated High Risk under EU AI Act, yet compliance pathway is undefined.***
***The Misalignment: A $325K executive governance specialist without strategic context is akin to establishing a legal compliance team without business processes to govern. Controls are reactive, not proactive. When new AI use cases emerge (new models, new data assets, new deployment environments), governance specialists lack precedent frameworks and must re-establish controls ad hoc.***
***The Unmet Potential: role-126 should be a strategic architect, not a firefighter. Elevating analytics strategy (sub-capability 7.1) unlocks governance opportunities. Clear governance frameworks can then be embedded into data engineering practices (sAFE), model development workflows, and self-service platform design.***
## Theme 6: The Data Literacy Desert
***Capability 7 sub-capability 7.5 (Data Literacy and Enablement) scores 2 because Rackspace has zero internal data literacy program, no competency framework, no business user training pathway, and no analytics ambassador ecosystem. This is organizational constraint on analytics adoption regardless of platform maturity.***
***The Absence: CTL-283 (Role-Based Security Training) exists but covers security topics only, not analytics. dept-144 (Sales Enablement & Training, $1.36M, 11 HC) trains sales staff on products and processes, not business users on BI tool usage or data interpretation. role-398 (Cloud Certification Coordinator) manages technical certifications (AWS, Azure, GCP), not analytics certifications. The 300+ certified DBAs (BC-025) serving customer engagements globally are not internal business users—they are customer-facing professionals.***
***The Constraint: Business users lack foundational data literacy skills. How do operational managers interpret statistical significance? How do revenue teams pivot on data insights? How do cost optimization teams read a cost allocation dashboard? Without training and competency development, even world-class BI platforms (PowerBI, Tableau) become underutilized. The Gartner 2024 Analytics & BI survey found 68% of BI platform adoption failures stem from insufficient user training, not platform deficiencies.***
***The Opportunity Cost: Rackspace invests in platform technology (Snowflake, BI tools, FAIR repositories) but starves the human capability layer. An analytics consultant embedded in a business unit to coach daily adoption activities generates 10x more impact than a new BI platform feature deployed without user education.***
## Theme 7: Self-Service Analytics — The Capability That Doesn't Exist
***Sub-capability 7.4 (Self-Service Analytics) represents the most critical Score 2 indicator: ZERO knowledge graph evidence of self-service infrastructure. There is no analytics portal, no data marketplace, no governed data products, no citizen developer program, no embedded analytics tools. This sub-capability doesn't exist organizationally.***
***What Should Exist: Score 3 (Managed) self-service analytics includes (a) discoverable data catalog with business glossaries, (b) pre-built data products with SLAs and ownership, (c) governed portal enabling business users to create reports without analyst bottleneck, (d) citizen analyst programs with training and guardrails, (e) analytics embed capability for LOB applications, (f) self-service access control based on role and data classification.***
***What Actually Exists: 20 standardized dashboards in da-122 (consolidated from 400). These are analyst-created, centralized, read-only reports. Business users cannot explore data independently. There is no discoverable catalog. There is no data marketplace. Analysts remain bottleneck.***
***The Rationale: Just Analytics (PF-042, 5 HC) serves customer-facing analytics consulting, not internal self-service platform development. The organization has optimized for external revenue generation (customer analytics projects) over internal capability building (self-service democratization). This is rational short-term strategy but limits long-term operational agility.***
***The Dashboard Compression Irony: The consolidation from 400 legacy dashboards to 20 standardized dashboards (per da-122) was purportedly a governance win—eliminating redundancy, consolidating metrics, standardizing definitions. Yet it also REDUCED access points for business users. Fewer dashboards means fewer discovery paths. Self-service capability remains zero because the strategy was centralization, not democratization.***
     ╔════════════════════════════════════════════════════════════════╗
     ║    SELF-SERVICE ANALYTICS: THE MISSING CAPABILITY (7.4)           ║
     ╠════════════════════════════════════════════════════════════════╣
     ║                                                                    ║
     ║  WHAT SHOULD EXIST (Score 3+):                                    ║
     ║  ═════════════════════════════════════════════════════════════════ ║
     ║                                                                    ║
     ║      Analytics Portal / Data Marketplace                           ║
     ║      ├─ Business Glossary (definitions, metrics, lineage)          ║
     ║      ├─ Data Product Catalog (5-10 core data products)             ║
     ║      ├─ SLAs and Data Stewardship (owners, refresh, quality)       ║
     ║      ├─ Access Request Workflow (governed, audited)                ║
     ║      └─ Usage Analytics (which data, which users, which queries)   ║
     ║                                                                    ║
     ║      Self-Service BI Tools (Tableau, PowerBI)                      ║
     ║      ├─ Analyst-Independent Report Creation                        ║
     ║      ├─ Drag-and-Drop Query Building                               ║
     ║      ├─ Pre-Built Data Models (governed dimensions & facts)        ║
     ║      ├─ Role-Based Access Control (data steward approval)          ║
     ║      └─ Certification & Publishing (shared reports/dashboards)    ║
     ║                                                                    ║
     ║      Citizen Analytics Program                                     ║
     ║      ├─ 50-100 Trained Users (power users in LOBs)                 ║
     ║      ├─ Competency Certification (4-week program)                  ║
     ║      ├─ Analytics Coaches (embedded in business units)             ║
     ║      ├─ Governance Guardrails (what queries are allowed)           ║
     ║      └─ Support Escalation Path (coach → COE → advanced analytics) ║
     ║                                                                    ║
     ║  WHAT ACTUALLY EXISTS (Score 2):                                  ║
     ║  ═════════════════════════════════════════════════════════════════ ║
     ║                                                                    ║
     ║      20 Standardized Dashboards (da-122)                           ║
     ║      ├─ Analyst-created, read-only                                 ║
     ║      ├─ No business glossary                                       ║
     ║      ├─ No discovery mechanism                                     ║
     ║      ├─ No drill-down or exploration                               ║
     ║      └─ Analyst remains bottleneck                                 ║
     ║                                                                    ║
     ║      No Data Marketplace                                           ║
     ║      ├─ No data product definitions                                ║
     ║      ├─ No SLAs for data consumption                               ║
     ║      ├─ No stewardship model                                       ║
     ║      └─ Access is ad hoc, manually granted                         ║
     ║                                                                    ║
     ║      No Self-Service BI                                            ║
     ║      ├─ Business users cannot create reports                       ║
     ║      ├─ Governance is absent (no controls needed for zero access) ║
     ║      ├─ Training pathway does not exist                            ║
     ║      └─ Citizen analyst program: ZERO                              ║
     ║                                                                    ║
     ║  THE IRONY:                                                        ║
     ║  • 400 legacy dashboards → 20 centralized = governance consolidation  ║
     ║  • But also: fewer access points = lower democratization           ║
     ║  • Net effect: centralization won, democratization lost            ║
     ║                                                                    ║
     ║  THE OPPORTUNITY:                                                  ║
     ║  Self-service analytics is the highest-leverage Score 2→3 lever.   ║
     ║  Relatively low platform cost (portal/catalog on Snowflake/Tableau)║
     ║  but high operational impact (reduces analyst bottleneck by 50%+). ║
     ║                                                                    ║
     ╚════════════════════════════════════════════════════════════════╝
# Cross-Capability Linkages
***Capability 7 (Data and Analytics Enablement) intersects multiple other DCAM capabilities through data governance, technology infrastructure, and organizational structure:***
Capability 1 (Cloud Strategy): Data workloads (Snowflake on AWS, BigQuery on GCP, Synapse on Azure) are cloud-native. Analytics roadmap must align with cloud platform strategy and cost optimization targets.
Capability 3 (Data Management): Data governance policies (POL-071), quality controls, and metadata management directly enable analytics. CDO must own both data management and analytics strategy.
Capability 4 (Technology Infrastructure): BI platforms, data warehousing infrastructure, and GPU workloads depend on technology architecture. Analytics infrastructure must be resilient, scalable, and cost-optimized.
Capability 5 (Cybersecurity): Data classification, access controls, and audit trails are analytics prerequisites. Analytics platforms must comply with security controls and audit requirements.
Capability 6 (Data Privacy & Protection): Privacy by design for analytics, de-identification for training data, and audit trails for data access are integrated design principles.
# Strategic Roadmap: Score 2 to Score 3 (24-Month Plan)
***Rackspace can accelerate from Score 2 (Developing) to Score 3 (Managed) across Capability 7 within 24 months through focused organizational investment in five strategic initiatives:***
### Initiative 1: Establish CDO and Analytics Governance (Q1-Q2 2026)
Hire Chief Data Officer (P/VP level, $220K-$250K) to own analytics strategy, roadmap, organizational structure, and governance. Allocate 90-day onboarding for environmental assessment.
Form Analytics Governance Board: CDO (Chair), CFO, CTO, CRO, LOB heads. Monthly meetings. Publish Analytics Governance Charter by end Q1.
Consolidate analytics team reporting under CDO: Just Analytics, Customer Data Engineering, analytics roles. Current structure splits analytics across business units; unified reporting improves strategic coordination.
### Initiative 2: BI Platform Consolidation (Q2-Q4 2026)
Conduct BI Platform Rationalization Assessment (Q2): Map current usage of 5 platforms, identify use cases for each, estimate migration costs. Deliver Consolidation Roadmap by end Q2.
Select 2 core BI platforms: PowerBI for enterprise dashboarding (licenses exist through Microsoft agreements), Tableau for advanced analytics. Retire Looker, Qlik, QuickSight by Q4 2026.
Execute migration program: 15 dashboards Q3, 5 dashboards Q4. Maintain parallel platforms during transition. Deliver unified BI governance standards (design patterns, RBAC model, naming conventions) by Q3.
### Initiative 3: Launch Self-Service Analytics Portal (Q1-Q3 2026)
Define 5 core data products: Customer, Revenue, Cost, Resource, Risk. Assign business owner and technical steward per product. Publish product specifications and SLAs by end Q1.
Build analytics portal (Snowflake or Tableau Server): Business glossary, data product catalog, usage analytics. MVP launch Q2, general availability Q3.
Launch Citizen Analyst Cohort 1 (Q3): Recruit 20-30 power users. Deliver 4-week certification program. Deploy 5 analytics coaches in LOBs. Target 50 business-created reports by end 2026.
### Initiative 4: Data Literacy Program (Q2-Q4 2026)
Develop Data Literacy Competency Framework: 4 tiers (Aware, Literate, Specialist, Scientist) with defined skills, knowledge, and certifications. Publish by end Q1 2026.
Create curriculum: 8-hour Data Aware (all managers), 16-hour Data Literate (power users), 40-hour Analyst Specialist (analytics practitioners). Online modules + workshops. Launch pilot Q2 with Sales Enablement team (140 salespeople).
Establish Analytics Center of Excellence (CoE) with dedicated Learning & Development lead. Create analytics ambassador program (20-30 power users from LOBs) trained to support peer adoption. Provide quarterly workshops and monthly office hours for BI tool support.
### Initiative 5: Analytics Governance Maturity (Q1-Q4 2026)
Develop unified Analytics Governance Policy: Consolidate POL-047 and POL-071 into coherent framework. Define data quality SLAs, BI platform standards, lineage requirements, access controls. Publish by end Q1.
Implement Data Quality Operating Model: Assign data stewards (20 dashboards, 5 data products). Establish quarterly quality reviews and remediation tracking. Achieve 95% metadata completeness by end 2026.
Complete EU AI Act compliance for internal AI assets: da-075 FAIR Repository (Full Compliance), AI Launchpad training data (Full Compliance), model artifacts (Full Compliance). Conduct bias testing and explainability verification for all new models.
### Expected Score 3 Outcomes (End of 2026)
7.1 Analytics Strategy: Documented 24-month roadmap, executive sponsor, quarterly board reviews.
7.2 BI & Reporting: 2-3 core platforms, 60+ standardized dashboards, governance standards, real-time operational dashboards deployed.
7.3 Advanced Analytics: Internal data science team (2-3 FTE), first 3 production models deployed, EU AI Act compliance full.
7.4 Self-Service Analytics: Analytics portal operational, 5 data products published, 50+ citizen-created reports, 100+ trained users.
7.5 Data Literacy: Competency framework published, 50%+ of managers completed training, analytics CoE operational.
7.6 Analytics Governance: Unified policy, data stewardship model operational, quality SLAs monitored, compliance tracking automated.
# Comprehensive Evidence Inventory
***All entities referenced in this assessment are documented in the Rackspace knowledge graph. The following table summarizes 48 entities across 8 categories:***

| Entity ID | Entity Name                       | Type                | Confidence | Relevance       |
| --------- | --------------------------------- | ------------------- | ---------- | --------------- |
| BC-006    | AI Product & Solution Development | Business Capability | High       | Differentiating |
| BC-024    | AI & ML Service Delivery          | Business Capability | High       | Strategic       |
| BC-025    | Data Modernization & Analytics    | Business Capability | High       | Differentiating |
| da-075    | FAIR AI Use Case Repository       | Data Asset          | High       | Critical        |
| da-122    | Consolidated Data Warehouse       | Data Asset          | High       | Critical        |
| DD-032    | BI and Reporting Data Domain      | Data Domain         | High       | Critical        |

| Entity ID | Entity Name               | Type    | Confidence | Relevance   |
| --------- | ------------------------- | ------- | ---------- | ----------- |
| POL-047   | AI Governance Policy      | Policy  | High       | EU AI Act   |
| POL-071   | Data Governance Policy    | Policy  | High       | Strategic   |
| CTL-120   | Responsible AI Controls   | Control | High       | Preventive  |
| CTL-307   | Model Governance Control  | Control | High       | Preventive  |
| CTL-283   | Security Training Control | Control | Medium     | Implemented |
| role-059  | Data Scientist            | Role    | High       | Internal    |

| Entity ID | Entity Name                       | Type       | Confidence | Relevance  |
| --------- | --------------------------------- | ---------- | ---------- | ---------- |
| role-126  | AI Ethics & Governance Specialist | Role       | High       | Executive  |
| role-147  | Snowflake Data Architect          | Role       | Medium     | Internal   |
| role-160  | Lead Data Engineer                | Role       | High       | Platform   |
| role-307  | Just Analytics Consultant         | Role       | Medium     | Consulting |
| role-398  | Cloud Certification Coordinator   | Role       | Low        | Support    |
| dept-144  | Sales Enablement & Training       | Department | High       | Training   |

| Entity ID | Entity Name                    | Type              | Confidence | Relevance       |
| --------- | ------------------------------ | ----------------- | ---------- | --------------- |
| dept-153  | GPU Infrastructure Engineering | Department        | Medium     | AI Workloads    |
| dept-164  | Customer Data Engineering      | Department        | High       | Platform        |
| dept-165  | Just Analytics                 | Department        | High       | Consulting      |
| dept-194  | GCP Cloud Engineering          | Department        | High       | Cloud Platform  |
| OU-027    | Data Solutions Org Unit        | Org Unit          | High       | Strategic       |
| PF-042    | Analytics Platform Services    | Product Portfolio | Medium     | Customer-Facing |

***Additional KG entities referenced: Snowflake Enterprise Analytics DW, AI Launchpad Training Dataset Store, AI Launchpad Model Artifact Repository, AI Anywhere Private Cloud GPU Data Store, Compass Healthcare AI Clinical Dataset, CTR-005 (DIR-CPO-5155 Texas DIR AI Services), INT-0376 (Dell FAIR Alliance).***
# Conclusion
***Rackspace Technology scores 2 (Developing) across all six sub-capabilities of Capability 7: Data and Analytics Enablement. This Score 2 assessment reflects foundational analytics maturity characterized by (1) reactive strategy without documented roadmap, (2) fragmented BI platform ecosystem lacking governance, (3) minimal data science capability, (4) absent self-service analytics infrastructure, (5) nonexistent internal data literacy program, and (6) governance controls without strategic direction.***
***The central paradox is stark: Rackspace sells world-class AI and analytics services externally (FAIR practice, 500+ use cases, ISG Provider Lens Leader status, 70+ enterprise implementations) while operating its own analytics function at foundational maturity. External business capabilities BC-006, BC-024, BC-025 are Differentiating or Strategic tier; internal Capability 7 is Foundational. This misalignment represents untapped operational potential.***
***The assessment identified seven analytical themes driving Score 2: Cobbler's Children Paradox (external excellence, internal immaturity), FAIR Fortress vs. Empty Village (100:1 external-to-internal capability ratio), Five BI Platforms with Zero Standard (governance vacuum), Data Consolidation Victory (genuine Snowflake win, incomplete democratization), AI Governance Without Strategy (controls without context), Data Literacy Desert (zero training program), and Self-Service Analytics That Doesn't Exist (portal, marketplace, citizen developer program absent).***
***Acceleration from Score 2 to Score 3 (Managed) within 24 months is achievable through focused organizational investment in five strategic initiatives: (1) Establish CDO and Analytics Governance, (2) BI Platform Consolidation (5→2), (3) Launch Self-Service Analytics Portal, (4) Data Literacy Program, (5) Analytics Governance Maturity. Success requires executive sponsorship, dedicated budget allocation, and organizational prioritization of internal analytics alongside revenue-generating external services.***
***The consolidated Snowflake data warehouse (da-122), sAFE agile methodology, and governance infrastructure provide the technical foundation. The FAIR practice success and 300+ certified DBAs demonstrate organizational capability for analytics excellence. The missing elements are organizational structure (CDO), strategic direction (roadmap), workforce investment (hiring), and cultural commitment (prioritizing internal analytics alongside customer services). With focused execution, Rackspace can elevate Capability 7 to Score 3 within one year and Score 4 within two years, unlocking substantial operational value and demonstrating organizational commitment to data-driven decision-making.***
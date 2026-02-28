# L02-SYSTEM.JSON EXPANSION: ENTERPRISE SYSTEM INVENTORY

## Authorization Document — Sprint Plan & Execution Framework

**Target:** Rackspace Technology (NASDAQ: RXT)
**File:** L02-system.json
**Current State:** 62 entities, 166 relationships
**Target State:** 180–220 entities, ~600+ relationships
**Date:** 2026-02-24

---

## 1. COMPANY PROFILE

| Attribute | Value | Source |
|-----------|-------|--------|
| Revenue | $2,737M FY2024 | 10-K Annual Report, Feb 2025 |
| Private Cloud Revenue | $1,055M (down 13% YoY) | 10-K Annual Report |
| Public Cloud Revenue | $1,683M (down 3% YoY) | 10-K Annual Report |
| Employees | ~7,200 | 2025 Sustainability Report |
| Data Centers | 27+ | rackspace.com/about/data-centers |
| Operational Sites | 58 (per L00-site.json) | Validated project file |
| Countries | 15+ | 10-K Annual Report |
| Certifications | ISO 27001, SOC 1/2/3, PCI DSS L1, FedRAMP Moderate, HITRUST, ISO 14001/45001/9001 | rackspace.com/compliance |
| Business Model | Managed cloud services (not pure SaaS) | SEC filings |
| Public Company | NASDAQ listed, SEC reporting, SOX compliant | ir.rackspace.com |
| CSO | Karen O'Reilly-Smith (confirmed Dec 2022) | L05-person.json |
| CEO | Amar Maletira | 10-K Annual Report |

---

## 2. CURRENT STATE ANALYSIS

### 2.1 Schema Definition

The L02-system.json schema provides 10 fields per entity:

```
id, entity_type, name, system_type, hostname, ip_address, os,
criticality, environment, is_internet_facing
```

**Critical observation:** No `description` field exists. This means source documentation, confidence rationale, and OSINT provenance cannot be encoded per-entity within the current schema. The network.json schema DOES include description. This is a schema gap we need to address before build.

### 2.2 Distribution Analysis (Current 62 Entities)

**System Type:**
- infrastructure: 31 (50%)
- application: 23 (37%)
- security: 8 (13%)

**Criticality:**
- critical: 21 (34%)
- high: 35 (56%)
- medium: 6 (10%)
- low: 0 (0%)

**Environment:**
- production: 62 (100%) — NO dev, staging, DR, or test environments modeled

**Internet-Facing:**
- True: 37 (60%)
- False: 25 (40%)

**Hostname Quality:**
- Real/observable: 43 (69%)
- N/A (unknown): 7 (11%)
- Inferred: 12 (19%)

**IP Address Quality:**
- Real IPs: 16 (26%)
- N/A: 46 (74%)

**Relationship Types:**
- depends_on: 38
- hosted_on: 1
- located_at: 30
- owned_by: 62
- managed_by: 35

**Cross-File Targets:**
- dept-*: 62 (every system has owned_by → department)
- sys-*: 39 (internal system dependencies)
- person-*: 35 (managed_by → person)
- site-*: 30 (located_at → site)

**Referential Integrity:** ZERO dangling references confirmed.

### 2.3 Category Inventory (Current 62 Entities)

| Category | Count | Entity IDs | Status |
|----------|-------|-----------|--------|
| Customer-Facing Portals | 6 | sys-001 thru sys-004, sys-035, sys-036 | GAP |
| Cloud Infrastructure APIs | 6 | sys-006, sys-008 thru sys-011, sys-034 | GAP |
| Email & Messaging | 2 | sys-013, sys-033 | GAP |
| BGP Edge Routers | 5 | sys-016 thru sys-020 | ADEQUATE |
| DNS Infrastructure | 6 | sys-021 thru sys-023, sys-039, sys-047, sys-048 | ADEQUATE |
| Security Appliances | 9 | sys-028, sys-043 thru sys-046, sys-051, sys-054, sys-055, sys-057 | GAP |
| Network Interconnect | 3 | sys-024 thru sys-026 | ADEQUATE |
| DC Infrastructure Mgmt | 3 | sys-027, sys-029, sys-052 | GAP |
| Monitoring & Observability | 5 | sys-012, sys-031, sys-049, sys-050, sys-056 | GAP |
| Database & Storage | 7 | sys-007, sys-014, sys-037 thru sys-041, sys-053 | ADEQUATE |
| AI & Cloud Management | 5 | sys-058 thru sys-062 | ADEQUATE |
| DevOps & Automation | 1 | sys-030 | **CRITICAL GAP** |
| Corporate SaaS / Internal IT | 3 | sys-015, sys-032, sys-042 | **CRITICAL GAP** |
| Identity & Access Mgmt | 0 | — | **CRITICAL GAP** |
| Collaboration & Productivity | 0 | — | **CRITICAL GAP** |
| CRM & Customer Success | 0 | — | **CRITICAL GAP** |
| HR/Talent/Workforce | 0 | — | **CRITICAL GAP** |
| Financial Systems | 0 | — | **CRITICAL GAP** |
| Backup/DR/BC | 0 | — | **CRITICAL GAP** |
| Telephony & Comms | 0 | — | **CRITICAL GAP** |
| Endpoint & Fleet Mgmt | 0 | — | **CRITICAL GAP** |

---

## 3. BENCHMARK ANALYSIS

### 3.1 Expected System Count by Category

For a NASDAQ-listed managed cloud provider with $2.7B revenue, ~7,200 employees, FedRAMP Moderate ATO, and the certification portfolio listed above:

| Category | Current | Expected (Low) | Expected (High) | Gap Status |
|----------|---------|----------------|-----------------|------------|
| Customer Portals | 6 | 8 | 15 | GAP |
| Cloud APIs | 6 | 8 | 12 | GAP |
| Security Stack | 9 | 15 | 25 | GAP |
| Identity & Access | 0 | 4 | 8 | CRITICAL |
| Network Infra | 8 | 8 | 12 | ADEQUATE |
| DNS | 6 | 5 | 8 | ADEQUATE |
| DC Infra Mgmt | 3 | 5 | 10 | GAP |
| Monitoring/AIOps | 5 | 8 | 14 | GAP |
| Email/Messaging | 2 | 4 | 6 | GAP |
| Database/Storage | 7 | 6 | 10 | ADEQUATE |
| Corporate IT/Back Office | 3 | 15 | 25 | CRITICAL |
| DevOps/CI-CD | 1 | 8 | 15 | CRITICAL |
| AI/Cloud Mgmt | 5 | 5 | 8 | ADEQUATE |
| Collaboration | 0 | 4 | 8 | CRITICAL |
| CRM/Customer Success | 0 | 3 | 6 | CRITICAL |
| HR/Talent | 0 | 3 | 6 | CRITICAL |
| Financial Systems | 0 | 4 | 8 | CRITICAL |
| Backup/DR | 0 | 3 | 6 | CRITICAL |
| Telephony | 0 | 2 | 4 | CRITICAL |
| Endpoint/Fleet | 0 | 2 | 4 | CRITICAL |
| **TOTALS** | **61** | **120** | **210** | |

**Current coverage: 51% of minimum, 29% of maximum.**

### 3.2 Endpoint & Hardware Fleet Estimation

For a company with ~7,200 employees in the managed cloud/technology services sector:

| Asset Class | Estimation Method | Estimated Count | Confidence |
|-------------|-------------------|----------------|------------|
| Laptops/Desktops | 1.1 per employee (tech company standard) | ~7,920 | 0.80 |
| Monitors | 1.5 per employee (dual-monitor standard) | ~10,800 | 0.70 |
| Mobile Devices (managed) | 0.3 per employee (corporate mobile) | ~2,160 | 0.65 |
| Printers/MFDs | 1 per 50 employees | ~144 | 0.60 |
| Conference Room Systems | 1 per 20 employees (tech company) | ~360 | 0.55 |
| Servers (owned, data center) | Based on 27+ DCs, est. 500-2000/DC | ~20,000-50,000 | 0.50 |
| Network Devices (switches, routers) | Based on 27+ DCs + offices | ~5,000-15,000 | 0.50 |

**Note:** These are fleet-level estimates, not individual system entities. They inform the CMDB context but are not modeled as discrete entities in the KG. They would be captured as attributes or metadata on the endpoint management and DC infrastructure system entities.

---

## 4. OSINT EVIDENCE LEDGER

### 4.1 OSINT Source Hierarchy (Confidence Tiers)

| Tier | Source Category | Confidence Range | Examples |
|------|----------------|-----------------|----------|
| T1 | SEC Filings | 0.95–1.00 | 10-K, 10-Q, 8-K, DEF 14A |
| T2 | SOC 2/3 Reports | 0.90–0.95 | Technology stack references in audit reports |
| T3 | Product Documentation | 0.85–0.95 | docs.rackspace.com, API docs, hostnames |
| T4 | Compliance/Legal Pages | 0.85–0.90 | rackspace.com/compliance, DPA, AUP |
| T5 | Press Releases / IR | 0.85–0.90 | ir.rackspace.com, partnership announcements |
| T6 | GitHub Repositories | 0.80–0.90 | rackspace, rackerlabs, Rackspace-DOT orgs |
| T7 | Job Postings | 0.70–0.85 | Lever, LinkedIn, ZipRecruiter listings |
| T8 | Employee LinkedIn | 0.65–0.80 | Technology stack mentions in profiles |
| T9 | DNS/WHOIS/BGP | 0.85–0.95 | ARIN, PeeringDB, DNS records |
| T10 | Sector Inference | 0.45–0.70 | Industry norms for company of this profile |

### 4.2 Confirmed Systems NOT Yet Modeled

**SOC 2/3 Confirmed (T2 — Confidence 0.90+):**

| System | Source | Current Status | Confidence |
|--------|--------|---------------|------------|
| SailPoint IdentityIQ | SOC 3 FY2024 | MISSING | 0.95 |
| CrowdStrike Falcon | SOC 3 FY2024 | MISSING | 0.95 |
| Splunk SIEM | SOC 3 FY2024 | Bundled in sys-032 | 0.95 |
| Palo Alto IDS | SOC 2/3 FY2020-24 | MISSING | 0.95 |
| RSA Authentication Manager | SOC 3 FY2024 | MISSING | 0.90 |
| Balabit Shell Control Box | SOC 3 FY2024 | MISSING | 0.90 |
| Trend Micro Cloud One (FIM) | SOC 3 FY2024 | MISSING | 0.90 |
| Active Directory (3-forest) | SOC 2/3 FY2020-24 | MISSING | 0.95 |
| ADFS (Federated Identity) | SOC 2/3 FY2020-24 | MISSING | 0.90 |

**Vendor File Cross-Reference (T5 — Confidence 0.80+):**

| Vendor Entity | System Implied | Current Status | Confidence |
|---------------|---------------|---------------|------------|
| vnd-019: Atlassian | Jira + Confluence | Bundled in sys-032 | 0.85 |
| vnd-020: Salesforce | CRM Platform | Bundled in sys-032 | 0.90 |
| vnd-021: Datadog | Monitoring SaaS | MISSING | 0.80 |
| vnd-022: Snowflake | Data Warehouse | MISSING | 0.75 |
| vnd-023: Databricks | Data/ML Platform | MISSING | 0.75 |
| vnd-031: ScienceLogic | AIOps Monitoring | MISSING | 0.80 |
| vnd-032: Platform9 | Kubernetes Mgmt | MISSING | 0.85 |
| vnd-033: Workday | HRIS/Finance | MISSING | 0.85 |
| vnd-034: Moogsoft (IBM) | AIOps | MISSING | 0.75 |
| vnd-035: Everbridge | Mass Notification | MISSING | 0.80 |

**GitHub OSINT Confirmed (T6 — Confidence 0.80+):**

| System | Evidence | Current Status | Confidence |
|--------|----------|---------------|------------|
| GitHub Enterprise | 4 orgs: rackspace, rackerlabs (119 repos), Rackspace-DOT, rackspace-infrastructure-automation | MISSING | 0.90 |
| Terraform | rackspace-toolbox container (gcr.io/rs-public-containers/rackspace-toolbox) | MISSING | 0.90 |
| Ansible | Rackspace-DOT/ansible-roles repo | MISSING | 0.85 |
| Jenkins | docs.rackspace.com security automation blog | MISSING | 0.75 |
| CircleCI | .circleci/config.yml in IaC repo structure | MISSING | 0.80 |
| Docker/GCR | gcr.io/rs-public-containers, ObjectRocket registry | MISSING | 0.85 |
| Kubernetes | Rackspace-DOT/kubectl, MPK product, understack project | MISSING | 0.85 |
| OpenStack Control Plane | Co-founded 2010, Platinum OpenInfra, skyline-rxt/genestack repos | MISSING | 0.95 |

**Job Posting / LinkedIn Confirmed (T7-T8 — Confidence 0.65-0.80):**

| System | Evidence | Current Status | Confidence |
|--------|----------|---------------|------------|
| Avaya Telecom | Job posting: "Strong knowledge of Avaya Telecom System" | MISSING | 0.75 |
| Microsoft Teams | Multiple employee LinkedIn profiles | MISSING | 0.80 |
| Slack | Employee LinkedIn profiles | MISSING | 0.75 |
| Confluence | Employee LinkedIn profiles | Bundled in sys-032 | 0.80 |
| Jira | Job postings + LinkedIn profiles | Bundled in sys-032 | 0.85 |
| Gainsight | CSM LinkedIn profile | MISSING | 0.70 |
| CloudHealth/CloudCheckr | CSM LinkedIn profile | MISSING | 0.70 |
| Microsoft 365 | Job postings: "Windows Desktops, Office 365" | MISSING | 0.80 |

**Press / IR Confirmed (T5 — Confidence 0.85+):**

| System | Evidence | Current Status | Confidence |
|--------|----------|---------------|------------|
| Rubrik (Cyber Recovery) | April 2025 RSAC joint announcement | MISSING | 0.85 |
| Sema4.ai Platform | June 2025 agentic AI partnership | MISSING | 0.85 |
| Rackspace Lab Services | Aug 2024 VMware Explore launch on SDDC Flex | MISSING | 0.85 |
| OpenStack Flex (Genestack) | April 2025 launch announcement | MISSING | 0.90 |

---

## 5. SCHEMA DECISION

### 5.1 The Description Field Problem

The current L02-system.json schema has NO `description` field. However:
- L02-network.json DOES have a `description` field
- Every other validated project file uses description for source documentation
- Without description, we cannot encode OSINT provenance, confidence rationale, or distinguish factual from inferred entities

**Recommendation:** Add `description` field to the system entity schema, consistent with the pattern established in L02-network.json and all other project files. This is the field where we encode:
- What the system does (scoped to system.json topic only)
- OSINT source citations
- Confidence rationale (confirmed vs. inferred)
- Evidence trail for later analysis

### 5.2 Factual vs. Inferred Marking Convention

Every system description will begin with a confidence tag:

- `[CONFIRMED - T1/T2]` — Directly referenced in SEC filings or SOC audit reports
- `[CONFIRMED - T3/T4]` — Observable via product docs, DNS, compliance pages
- `[CONFIRMED - T5/T6]` — Referenced in press releases or GitHub repositories
- `[CONFIRMED - T7/T8]` — Referenced in job postings or employee LinkedIn profiles
- `[INFERRED - SECTOR]` — Not directly observed, but required for company of this sector/size/profile
- `[INFERRED - VENDOR]` — Vendor relationship confirmed (L10-vendor.json) but specific system deployment not directly observed

---

## 6. SPRINT EXECUTION PLAN

### Sprint 0: Foundation (Pre-Build)
**Objective:** Prepare the file for expansion.
**Tasks:**
1. Add `description` field to all 62 existing entities with source documentation
2. Decompose sys-032 "Internal Tooling Stack (JIRA/Splunk/Salesforce)" into discrete entities
3. Validate existing hostname/IP data is still current
4. Establish ID allocation scheme: sys-063 through sys-XXX
5. Run baseline referential integrity check

**Deliverable:** Updated 62-entity file with descriptions, sys-032 decomposed into 3+ entities
**Expected entity count after Sprint 0:** ~65

### Sprint 1: SOC-Confirmed Security & IAM Stack
**Objective:** Model every system explicitly named in SOC 2/3 audit reports.
**Scope:**
- SailPoint IdentityIQ (IAM governance)
- CrowdStrike Falcon (EDR/NGAV)
- Splunk Enterprise Security (SIEM) — extracted from sys-032
- Palo Alto Networks (IDS/IPS)
- RSA Authentication Manager (MFA)
- Balabit/BeyondTrust Shell Control Box (PAM session recording)
- Trend Micro Cloud One (FIM)
- Active Directory (3-forest: Corporate, Intensive, Global RS)
- ADFS (Federated Identity)
- Inferred: SOAR platform, vulnerability scanner, GRC/compliance platform, PKI/certificate management, DLP, WAF

**Confidence range:** 0.90–0.95 for SOC-confirmed, 0.60–0.75 for inferred
**Expected new entities:** 15–20
**Expected entity count after Sprint 1:** ~80–85

### Sprint 2: DevOps, CI/CD & Container Orchestration
**Objective:** Model the development and automation toolchain confirmed via GitHub and product documentation.
**Scope:**
- GitHub Enterprise (source code management)
- Terraform (IaC, confirmed via toolbox container)
- Ansible (configuration management, confirmed via Rackspace-DOT)
- Jenkins (CI/CD, confirmed via blog)
- CircleCI (CI/CD, confirmed via IaC repo config)
- Docker / Container Registry (GCR confirmed)
- Kubernetes Clusters (kubectl confirmed, MPK product, understack/genestack)
- OpenStack Control Plane (co-founded, Platinum member, dedicated repos)
- Artifact repository (Nexus/Artifactory — inferred)
- Code quality (SonarQube — inferred)
- Secrets management (HashiCorp Vault — inferred)

**Confidence range:** 0.75–0.95 for GitHub-confirmed, 0.55–0.70 for inferred
**Expected new entities:** 10–14
**Expected entity count after Sprint 2:** ~90–99

### Sprint 3: Corporate IT & Back Office
**Objective:** Model the corporate IT systems required for a $2.7B NASDAQ-listed company with 7,200 employees.
**Scope:**

*Confirmed:*
- Salesforce CRM (RelationEdge acquisition 2018, employee profiles) — extracted from sys-032
- Jira (project management) — extracted from sys-032
- Confluence (knowledge management) — extracted from sys-032/LinkedIn
- Workday (HRIS/Finance, confirmed via vendor file vnd-033)
- Microsoft 365 (collaboration, confirmed via job postings)
- Slack (messaging, confirmed via LinkedIn)
- Gainsight (customer success, confirmed via LinkedIn)

*Inferred (required for company profile):*
- ERP/General Ledger (financial reporting, SOX ICFR)
- Accounts Payable/Receivable
- Billing & Revenue Recognition (ASC 606)
- Treasury Management
- Procurement System
- Legal/Contract Lifecycle Management
- Board Portal (NASDAQ governance)
- Expense Management
- Travel Booking
- Learning Management System
- Compensation & Benefits Administration
- Tax Compliance
- Audit Management / GRC Platform
- Investor Relations Platform
- Corporate Communications / Intranet

**Confidence range:** 0.70–0.90 for confirmed, 0.45–0.65 for inferred
**Expected new entities:** 20–28
**Expected entity count after Sprint 3:** ~110–127

### Sprint 4: Monitoring, Backup/DR, Telephony & Endpoint
**Objective:** Fill remaining operational gaps.
**Scope:**

*Confirmed:*
- Datadog (monitoring, vendor vnd-021)
- ScienceLogic (AIOps, vendor vnd-031)
- Moogsoft/IBM AIOps (vendor vnd-034)
- Everbridge (mass notification, vendor vnd-035)
- Rubrik (backup/cyber recovery, RSAC 2025 press release)
- Avaya (telephony, job posting)
- CloudHealth/CloudCheckr (cloud cost management, LinkedIn)

*Inferred:*
- APM platform
- Synthetic monitoring
- Log analytics (distinct from SIEM)
- Status page infrastructure
- Enterprise backup infrastructure
- DR orchestration platform
- Data replication platform
- ACD/IVR (contact center)
- Call recording / quality management
- MDM/UEM (endpoint management)
- Patch management platform
- IPAM/DDI (Infoblox or similar)
- Network management system (NMS)

**Confidence range:** 0.75–0.85 for confirmed, 0.50–0.65 for inferred
**Expected new entities:** 15–22
**Expected entity count after Sprint 4:** ~125–149

### Sprint 5: Expanded Platforms, Portals & Additional Infrastructure
**Objective:** Fill remaining coverage gaps with customer-facing platforms, additional infrastructure, and edge cases.
**Scope:**
- Additional customer portals (partner portal, developer portal, status page, billing portal)
- Additional OpenStack services (Cinder block storage, Glance image service, Heat orchestration)
- Rackspace Lab Services platform
- OpenStack Flex / Genestack
- Sema4.ai agentic AI platform
- VMware management plane (vSphere/vCenter for SDDC)
- Platform9 Kubernetes management
- Internal database infrastructure
- Legacy systems from acquisitions (Datapipe, HostCentric, Onica)
- Geographic redundancy / DR instances of critical systems

**Confidence range:** 0.70–0.90 for confirmed, 0.50–0.65 for inferred
**Expected new entities:** 15–25
**Expected entity count after Sprint 5:** ~140–174

### Sprint 6: Validation, Relationships & Quality Gates
**Objective:** Final validation, relationship wiring, and quality assurance.
**Tasks:**
1. Mechanical schema validation (all fields populated, correct types)
2. ID uniqueness check across entire KG (2,636+ entities)
3. Referential integrity check (zero dangling references)
4. Relationship wiring: depends_on, hosted_on, located_at, owned_by, managed_by for all new entities
5. Weight/confidence scoring on all relationships (0.6–1.0)
6. Distribution sanity check (system_type, criticality, environment, internet-facing)
7. Cross-reference against L01-control.json (every SOC-confirmed tool should map to controls that reference it)
8. Cross-reference against L02-integration.json (every system should participate in integrations)
9. Cross-reference against L10-vendor.json (vendor relationships properly reflected)
10. Entity count benchmarked: confirm we hit 120+ minimum threshold

**Deliverable:** Final validated L02-system.json

---

## 7. QUALITY GATES (Applied Per Sprint)

- [ ] All required schema fields populated (no empty values)
- [ ] All entity IDs unique within file AND across entire KG
- [ ] All relationship UUIDs valid v4
- [ ] All weight values in [0.6, 1.0]
- [ ] All confidence values in [0.45, 1.0] — lower bound reflects inferred entities
- [ ] Zero dangling references across entire KG
- [ ] Cross-file relationship chain intact
- [ ] Source citations in description fields (every entity)
- [ ] Confidence tag at start of every description
- [ ] Distribution sanity check per sprint
- [ ] Factual/inferred ratio tracked in sprint ledger

---

## 8. SPRINT LEDGER FORMAT

Each sprint will produce a ledger entry:

```
SPRINT N LEDGER
===============
Entities added: XX
Entities modified: XX
Total entities: XXX
Relationships added: XX
Total relationships: XXX

Factual entities (T1-T8): XX (XX%)
Inferred entities (SECTOR/VENDOR): XX (XX%)

New entity ID range: sys-XXX through sys-XXX
Dangling references: 0
Schema violations: 0

OSINT sources consumed:
  - [source URL or description, tier, confidence]
  - ...
```

---

## 9. RISK REGISTER

| Risk | Impact | Mitigation |
|------|--------|------------|
| Schema alteration (adding description field) | Breaks template compliance | Description field exists in L02-network.json; consistent with project convention |
| Inferred entities reduce KG credibility | Lower overall confidence | Clear tagging convention, distinct confidence ranges, rationale in descriptions |
| sys-032 decomposition breaks existing relationships | Dangling references | Re-wire all relationships that target sys-032 to appropriate successor entities |
| Vendor file references may be aspirational (not deployed) | Overcount | Conservative confidence scoring (0.75 for vendor-only, vs 0.90 for SOC-confirmed) |
| Employee count may have changed (7,200 vs prior 9,600) | Fleet estimates off | Use current 7,200 figure from 2025 sustainability report |
| Redundant modeling with L02-integration.json | Double-counting | Systems are discrete deployable units; integrations are data flows between them. Different entity types. |

---

## 10. AUTHORIZATION REQUEST

**Requesting authorization to execute Sprints 0 through 6 as defined above.**

Expected outcome: L02-system.json expanded from 62 to 180–220 entities with:
- ~80–100 OSINT-confirmed systems (confidence 0.70–1.00)
- ~60–80 sector-inferred systems (confidence 0.45–0.70)
- ~40–60 confirmed endpoint fleet estimates encoded in descriptions
- Full relationship wiring to existing KG entities (dept, site, person, vendor)
- Clear factual vs. inferred demarcation in every description
- Zero dangling references
- Zero schema violations

**Awaiting go-ahead.**

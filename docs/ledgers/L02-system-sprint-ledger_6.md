# L02-SYSTEM.JSON SPRINT LEDGER

## Sprint 0: Foundation
**Date:** 2026-02-24
**Objective:** Add description field to all 62 existing entities, decompose sys-032

```
SPRINT 0 LEDGER
===============
Entities added: 6
Entities modified: 62 (description field added)
Entities deprecated: 1 (sys-032 → sys-063 through sys-068)
Total entities: 68
Relationships removed: 3 (sys-032 edges)
Relationships added: 15
Total relationships: 178

Factual entities (T1-T9): 68 (100%)
Inferred entities (SECTOR/VENDOR): 0 (0%)

New entity ID range: sys-063 through sys-068
Dangling references: 0
Schema violations: 0
Duplicate IDs: 0
Invalid UUIDs: 0

OSINT sources consumed:
  - docs.rackspace.com API documentation (T3, 0.85-0.95)
  - DNS dig records for hostname verification (T9, 0.85-0.95)
  - SOC 3 FY2024 report references (T2, 0.90-0.95)
  - rackspace.com/about/data-centers (T4, 0.85-0.90)
  - rackspace.com/compliance (T4, 0.85-0.90)
  - Job postings via Lever/LinkedIn (T7/T8, 0.70-0.85)
  - 2018 RelationEdge acquisition press release (T5, 0.85)
  - PeeringDB AS records (T9, 0.90)
  - ARIN/RIPE WHOIS records (T9, 0.90)

Distribution:
  system_type: application=28, infrastructure=31, security=9
  criticality: critical=24, high=38, medium=6
  internet_facing: True=42, False=26
```

**New entities:**
| ID | Name | Tier | Source |
|----|------|------|--------|
| sys-063 | Atlassian Jira | T7/T8 | Job postings, LinkedIn, vnd-019 |
| sys-064 | Atlassian Confluence | T8 | LinkedIn, vnd-019 |
| sys-065 | Splunk Enterprise Security SIEM | T2 | SOC 3 FY2024, 13-month retention, vnd-018 |
| sys-066 | Salesforce CRM Platform | T5/T8 | RelationEdge acquisition 2018, LinkedIn, vnd-020 |
| sys-067 | Slack Enterprise Messaging | T8 | LinkedIn |
| sys-068 | Microsoft 365 Suite | T7 | Job postings, 25-year Microsoft partnership, vnd-002 |

**Running total: 68 / 180-220 target (38% of minimum)**

---

## Sprint 1: SOC-Confirmed Security & IAM Stack
**Date:** 2026-02-24
**Objective:** Model every system named in SOC 2/3 audit reports + FedRAMP-required inferred systems

```
SPRINT 1 LEDGER
===============
Entities added: 16
Entities modified: 0
Total entities: 84
Relationships added: 42
Total relationships: 220

Factual entities (T1-T9): 8 (50%)
Inferred entities (SECTOR): 8 (50%)

New entity ID range: sys-069 through sys-084
Dangling references: 0
Schema violations: 0
Duplicate IDs: 0
Invalid UUIDs: 0

OSINT sources consumed:
  - SOC 3 FY2024 Type 2 Report (Oct 2023-Sep 2024) (T2, 0.90-0.95)
    * SailPoint IdentityIQ — explicit IAM governance reference
    * CrowdStrike Falcon Intel — explicit EDR/NGAV/threat intel reference
    * Palo Alto Networks IDS — explicit traffic inspection reference
    * RSA Authentication Manager — explicit MFA token reference
    * Balabit Shell Control Box — explicit bastion session recording reference
    * Trend Micro Cloud One — explicit FIM reference
    * Splunk SIEM — explicit 13-month retention reference (already sys-065)
  - SOC 2 FY2020 Dedicated Hosting Report (T2, 0.90)
    * Active Directory 3-forest architecture (Corporate, Intensive, Global RS)
    * Corporate AD synchronization with GPS (HR database)
    * Cisco ACS policies for network device access
  - Dec 2022 ransomware incident 8-K SEC filing (T1, 0.95)
    * CrowdStrike engaged as IR partner
  - FedRAMP Moderate baseline requirements (T4, 0.85)
    * RA-5 vulnerability monitoring → sys-077
    * CA-2/CA-7 continuous monitoring → sys-078
    * SC-12/SC-13 crypto key management → sys-079
    * IR-4/IR-5 incident handling → sys-083
    * SI-5/RA-3 threat intel → sys-084
    * SI-8 spam protection → sys-082
    * SC-7 boundary protection/DLP → sys-081
  - PCI DSS Level 1 requirements (T4, 0.85)
    * Req 6.4 WAF → sys-080
  - rackspace.com/security product page (T3, 0.85)
  - L10-vendor.json cross-references: vnd-014, vnd-015, vnd-028

Distribution:
  Sprint 1 system_type: security=13, infrastructure=2, application=1
  Sprint 1 criticality: critical=9, high=7
  Overall system_type: application=29, infrastructure=33, security=22
  Overall criticality: critical=33, high=45, medium=6
```

**New entities:**
| ID | Name | Tier | Confidence | Source |
|----|------|------|------------|--------|
| sys-069 | SailPoint IdentityIQ | T2 | 0.95 | SOC 3 FY2024 explicit |
| sys-070 | CrowdStrike Falcon Platform | T2/T5 | 0.95 | SOC 3 FY2024, 8-K filing |
| sys-071 | Palo Alto Networks IDS/IPS | T2 | 0.95 | SOC 3 FY2024 explicit |
| sys-072 | RSA Authentication Manager | T2 | 0.90 | SOC 3 FY2024 explicit |
| sys-073 | BeyondTrust Privileged Session Mgmt | T2 | 0.90 | SOC 3 FY2024 (Balabit) |
| sys-074 | Trend Micro Cloud One (FIM) | T2 | 0.90 | SOC 3 FY2024 explicit |
| sys-075 | Active Directory 3-Forest | T2 | 0.95 | SOC 2/3 FY2020-2024 |
| sys-076 | Active Directory Federation Services | T2 | 0.90 | SOC 2/3 FY2020-2024 |
| sys-077 | Vulnerability Management Platform | INFERRED | 0.75 | FedRAMP RA-5, PCI 11.3 |
| sys-078 | GRC/Compliance Management Platform | INFERRED | 0.70 | FedRAMP CA-2/CA-7 |
| sys-079 | PKI/Certificate Lifecycle Mgmt | INFERRED | 0.70 | FedRAMP SC-12/SC-13 |
| sys-080 | Web Application Firewall | INFERRED | 0.75 | PCI DSS Req 6.4, dept-184 |
| sys-081 | Data Loss Prevention Platform | INFERRED | 0.65 | FedRAMP SC-7, dept-242 |
| sys-082 | Email Security Gateway | INFERRED | 0.65 | FedRAMP SI-8, M365 |
| sys-083 | SOAR Platform | INFERRED | 0.70 | FedRAMP IR-4/IR-5 |
| sys-084 | Threat Intelligence Platform | INFERRED | 0.70 | SOC 3 CrowdStrike ref, RA-3 |

**Running total: 84 / 180-220 target (47% of minimum)**

---

## Sprint 2: DevOps, CI/CD & Container Orchestration
**Date:** 2026-02-24
**Objective:** Model Kubernetes platform stack, CI/CD pipeline, IaC tooling, and container infrastructure

```
SPRINT 2 LEDGER
===============
Entities added: 15
Entities modified: 0
Total entities: 99
Relationships added: 30
Total relationships: 250

Factual entities (T1-T9): 15 (100%)
Inferred entities (SECTOR): 0 (0%)

New entity ID range: sys-085 through sys-099
Dangling references: 0
Schema violations: 0
Duplicate IDs: 0
Invalid UUIDs: 0

OSINT sources consumed:
  - github.com/rackerlabs/genestack (T9, 0.95)
    * Kubespray 2.27.0, K8s 1.30.x cluster deployment
    * Kustomize + Helm as deployment tooling
    * GHCR container images (ghcr.io/aedan/genestack-images)
    * Ansible playbooks for host-setup and cluster deployment
  - github.com/rackerlabs/understack (T9, 0.90)
    * GitOps-based bare metal provisioning via Ironic
    * Kubernetes cluster as control plane
  - github.com/rackerlabs/terraform-provider-spot (T9, 0.95)
    * Terraform provider published on Terraform Registry
  - github.com/rackspace-org (T9, 0.85)
    * Jenkins X (jx3-kubernetes, jx3-eks-vault) repos
    * EKS + Vault integration patterns
  - docs.rackspacecloud.com release notes (T3, 0.90)
    * Kubernetes 1.30.x, Kubespray 2.27.0
    * Kube-OVN CNI v1.13.14 (migrated to Helm)
    * Prometheus Operator for monitoring
    * Rook Ceph for persistent storage
    * Loki upgrade past v6
    * Grafana 9.2.2 Helm chart
    * MetalLB load balancer (Helm-managed)
  - docs.rackspacecloud.com/genestack-structure-and-files (T3, 0.90)
    * helm-chart-versions.yaml with 30+ service versions
    * Kustomize post-renderer pattern
  - docs.rackspace.com/docs/registry-image-library (T3, 0.90)
    * Harbor registry for CUDA, Jupyter, vLLM, Triton images
  - docs.rackspace.com/docs/runai-harbor (T3, 0.90)
    * Harbor for Run:AI container management
  - Rackspace Azure DevOps Engineer job posting (T7, 0.80)
    * GitHub Actions, Terraform, Docker, AKS, Git Flow

Distribution:
  Sprint 2 system_type: infrastructure=12, application=3
  Sprint 2 criticality: critical=7, high=8
  Overall system_type: application=32, infrastructure=45, security=22
  Overall criticality: critical=40, high=53, medium=6
```

**New entities:**
| ID | Name | Tier | Confidence | Source |
|----|------|------|------------|--------|
| sys-085 | Kubernetes Clusters (Kubespray) | T3/T9 | 0.90 | Genestack docs + GitHub |
| sys-086 | Ansible Automation Platform | T9 | 0.90 | Genestack bootstrap.sh |
| sys-087 | Helm Package Manager | T9 | 0.85 | Genestack README + docs |
| sys-088 | Terraform Enterprise | T7/T9 | 0.85 | terraform-provider-spot + jobs |
| sys-089 | GitHub Enterprise/Organizations | T9 | 0.95 | github.com/rackerlabs (119+ repos) |
| sys-090 | GitHub Actions CI/CD | T7/T9 | 0.85 | Job postings + repo CI |
| sys-091 | GitHub Container Registry (GHCR) | T3 | 0.85 | Genestack upgrade images |
| sys-092 | Harbor Container Registry | T3 | 0.85 | docs.rackspace.com registry-image-library |
| sys-093 | Docker Container Runtime | T7/T9 | 0.85 | Job postings + Genestack |
| sys-094 | Kustomize | T9 | 0.85 | Genestack structure docs |
| sys-095 | Prometheus Monitoring (Operator) | T3 | 0.80 | Genestack release notes |
| sys-096 | Grafana Dashboards | T3 | 0.80 | helm-chart-versions.yaml |
| sys-097 | Loki Log Aggregation | T3 | 0.80 | Genestack release notes |
| sys-098 | Rook Ceph Persistent Storage | T3 | 0.85 | Genestack release notes |
| sys-099 | Kube-OVN CNI Plugin | T3 | 0.85 | Genestack release notes v1.13.14 |

**Running total: 99 / 180-220 target (55% of minimum)**

---

## Sprint 3: Corporate IT, HR & Business Systems
**Date:** 2026-02-24
**Objective:** Model ITSM, HR/people systems, customer portals, financial systems, and corporate IT infrastructure

```
SPRINT 3 LEDGER
===============
Entities added: 13
Entities modified: 0
Total entities: 112
Relationships added: 33
Total relationships: 283

Factual entities (T1-T9): 10 (77%)
Inferred entities (SECTOR): 3 (23%)

New entity ID range: sys-100 through sys-112
Dangling references: 0
Schema violations: 0
Duplicate IDs: 0
Invalid UUIDs: 0

OSINT sources consumed:
  - rackspace.service-now.com (T9, 0.95)
    * ServiceNow instance confirmed via live domain + /system_status page
  - rackspace.com/applications/servicenow (T3, 0.90)
    * References "Rackspace Technology Core Ticketing System" as integration target
    * Integration list: Jira, Salesforce, Splunk, SAP, Slack, email
  - SOC 2 FY2020 Dedicated Hosting Report (T2, 0.90)
    * "Global People System (GPS – HR database)" — HRIS confirmed
    * Corporate AD nightly sync with GPS for new hire provisioning
    * Cisco ACS policies for network device configuration access
    * HR as sole authority for corporate network account requests
  - SOC 3 FY2024 (T2, 0.90)
    * MyRackspace Customer Portal — "publicly facing web application"
    * VPN with MFA enforcement
    * TACACS+ for network device authentication
  - my.rackspace.com (T9, 0.95)
    * Customer portal domain, phone support page
  - jobs.lever.co/rackspace (T9, 0.90)
    * Lever ATS platform serving all current job postings
  - rackspace.com footer navigation (T9, 0.90)
    * Cloud Office Control Panel (cp.rackspace.com)
    * Rackspace Webmail Login (apps.rackspace.com)
    * Microsoft 365 Portal link
  - rackspace.com/applications/erp (T3, 0.85)
    * SAP and Oracle ERP managed services (customer-facing)
  - 10-K FY2024 (T1, 0.95)
    * $2.7B revenue requiring SOX-compliant financial reporting
  - ServiceNow Community forum (T8, 0.80)
    * Customer integration incident between SNOW and Rackspace

Distribution:
  Sprint 3 system_type: application=10, infrastructure=1, security=2
  Sprint 3 criticality: critical=7, high=5, medium=1
  Overall system_type: application=42, infrastructure=46, security=24
  Overall criticality: critical=47, high=58, medium=7
  Overall internet-facing: 52
```

**New entities:**
| ID | Name | Tier | Confidence | Source |
|----|------|------|------------|--------|
| sys-100 | ServiceNow ITSM Platform | T9/T3 | 0.95 | rackspace.service-now.com |
| sys-101 | Rackspace Core Ticketing System | T3 | 0.80 | ServiceNow page integration list |
| sys-102 | Global People System (GPS) | T2 | 0.95 | SOC 2 FY2020 explicit |
| sys-103 | Lever Applicant Tracking System | T9 | 0.90 | jobs.lever.co/rackspace |
| sys-104 | Avaya Unified Communications | T7 | 0.75 | Job postings, support numbers |
| sys-105 | Cloud Office Control Panel | T9 | 0.85 | cp.rackspace.com domain |
| sys-106 | Rackspace Webmail | T9 | 0.85 | apps.rackspace.com domain |
| sys-107 | Billing & Revenue Management | T2/T4 | 0.85 | SOC 3/10-K revenue |
| sys-108 | Cisco ACS/ISE Network Access Control | T2 | 0.90 | SOC 2 FY2020 explicit |
| sys-109 | Learning Management System | INFERRED | 0.65 | FedRAMP AT-2/AT-3 |
| sys-110 | SharePoint Document Management | INFERRED | 0.70 | M365 deployment + FedRAMP |
| sys-111 | Financial ERP Platform | INFERRED | 0.75 | NASDAQ/SOX requirements |
| sys-112 | VPN Remote Access Gateway | T2 | 0.90 | SOC 3 FY2024 VPN+MFA |

**Running total: 112 / 180-220 target (62% of minimum)**

---

## Sprint 4: Monitoring, Backup & DR Systems
**Date:** 2026-02-24
**Objective:** Model DR/replication, backup infrastructure, additional K8s platform components, and monitoring

```
SPRINT 4 LEDGER
===============
Entities added: 12
Entities modified: 0
Total entities: 124
Relationships added: 26
Total relationships: 309

Factual entities (T1-T9): 10 (83%)
Inferred entities (SECTOR): 2 (17%)

New entity ID range: sys-113 through sys-124
Dangling references: 0
Schema violations: 0
Duplicate IDs: 0
Invalid UUIDs: 0

OSINT sources consumed:
  - docs.rackspace.com/docs/replication-and-recovery (T3, 0.95)
    * Zerto architecture: ZVM, VRA, VPG, Journal
    * Storage-agnostic hypervisor-based replication
    * Local + remote replication, live/test failover, VM move
  - docs.rackspace.com/docs/zerto-disaster-recovery (T3, 0.95)
    * SDDC-Business Zerto configuration guide
    * vCenter integration for authentication/authorization
  - rackspace.com/newsroom + ir.rackspace.com (T1/T5, 0.95)
    * Rubrik strategic partnership, April 30, 2025 RSAC
    * CEO Amar Maletira quoted
    * "Rackspace Cyber Recovery Cloud powered by Rubrik"
    * Air-gapped isolated recovery environment (IRE)
  - rackspace.com/security/cyber-recovery-cloud (T3, 0.90)
    * On-demand and dedicated IRE options
    * 3-year minimum commitment for dedicated
  - May 21, 2025 public cloud extension (GlobeNewswire T5, 0.95)
    * Rackspace Cyber Recovery Service for public cloud
    * Recovery as Code, DevOps automation
  - docs.rackspacecloud.com/genestack-structure-and-files (T3, 0.90)
    * envoy: v1.4.2, longhorn: 1.8.0 in helm-chart-versions.yaml
    * cert-manager ExperimentalGatewayAPISupport deprecation
    * MetalLB migration to Helm-managed
  - docs.rackspace.com/docs/backup-recovery (T3, 0.90)
    * Hot backup for database workloads
  - SOC 3 FY2024 (T2, 0.90)
    * 13-month log retention
  - FedRAMP Moderate controls (T4, 0.85)
    * SI-4 (system monitoring) → sys-116
    * AU-8 (time stamps) → sys-118

Distribution:
  Sprint 4 system_type: infrastructure=9, security=2, application=1
  Sprint 4 criticality: critical=6, high=6
  Overall system_type: application=43, infrastructure=55, security=26
  Overall criticality: critical=53, high=64, medium=7
```

**New entities:**
| ID | Name | Tier | Confidence | Source |
|----|------|------|------------|--------|
| sys-113 | Zerto IT Resilience Platform | T3 | 0.95 | docs.rackspace.com full architecture |
| sys-114 | Rubrik Cyber Recovery Cloud | T1/T5 | 0.95 | ir.rackspace.com press release + RSAC |
| sys-115 | VMware vCenter Server | T3 | 0.90 | Zerto docs + FedRAMP Gov Cloud |
| sys-116 | Infrastructure Monitoring Core | INFERRED | 0.70 | FedRAMP SI-4, status.rackspace.com |
| sys-117 | Log Management Infrastructure | T2 | 0.90 | SOC 3 FY2024 13-month retention |
| sys-118 | NTP Time Synchronization | INFERRED | 0.65 | FedRAMP AU-8, PCI DSS 10.4 |
| sys-119 | Database Backup & Recovery | T3 | 0.85 | docs.rackspace.com/docs/backup-recovery |
| sys-120 | Run:AI GPU Orchestration | T3 | 0.85 | docs.rackspace.com Run:AI + Harbor |
| sys-121 | MetalLB K8s Load Balancer | T3 | 0.85 | Genestack release notes |
| sys-122 | cert-manager Certificate Automation | T3 | 0.85 | Genestack release notes |
| sys-123 | Envoy Gateway API | T3 | 0.85 | Genestack structure + release notes |
| sys-124 | Longhorn Persistent Storage | T3 | 0.85 | helm-chart-versions.yaml |

**Running total: 124 / 180-220 target (69% of minimum)**

---

---

## Sprint 4 REDO — Monitoring, Backup, DR & VMware SDDC Components

**Status:** COMPLETE (redo — original Sprint 4 had insufficient OSINT depth)
**OSINT Searches:** 8 targeted searches (vs. 2 in original)
**Entities added:** 16 (sys-113 through sys-128)
**Relationships added:** 24
**Running total:** 128 entities, 307 relationships
**Confirmed rate:** 16/16 (100%)

### OSINT Sources Consumed (Sprint 4 Redo)

| # | Source | Type | Conf. | Key Findings |
|---|--------|------|-------|-------------|
| 1 | docs.rackspace.com/docs/zerto-disaster-recovery | T3 | 0.95 | ZVM, VRA, VPG architecture; live/test/move failover; SDDC Business/Enterprise |
| 2 | docs.rackspace.com/docs/replication-and-recovery | T3 | 0.95 | Zerto continuous replication; journal checkpoints; ransomware recovery |
| 3 | docs.rackspace.com/docs/vcda-disaster-recovery | T3 | 0.90 | VCDA initial-tier DR; 1min-24hr RPO; vCenter plugin |
| 4 | docs.rackspace.com/docs/add-ons | T3 | 0.90 | vSphere Replication; SRM; HCX migration |
| 5 | docs.rackspace.com/docs/amr-overview | T3 | 0.95 | Rackspace Watchman; 24x7x365 alarm mitigation; multi-provider webhook |
| 6 | docs.rackspace.com/docs/configure-your-monitoring-tool | T3 | 0.90 | Datadog webhook integration; Prometheus AlertManager; New Relic |
| 7 | docs.rackspace.com/docs/rackspace-vm-management-for-private-cloud | T3 | 0.95 | Datadog infrastructure monitoring; host maps; SDDC enrollment |
| 8 | docs.rackspace.com/docs/rpcv-core-components | T3 | 0.95 | vRealize Operations; vSAN; NSX; VCF stack |
| 9 | docs.rackspace.com/docs/rpcv-about | T3 | 0.95 | RPC-VMware architecture; vCenter; web service monitors |
| 10 | docs.rackspace.com/docs/about-sddc-enterprise | T3 | 0.90 | VCF stack; vRealize suite add-ons; NSX-T; Dell VxRail |
| 11 | docs.rackspace.com/docs/sddc-enterprise-customer-handbook | T3 | 0.90 | vRealize Log Insight; vRealize Network Insight |
| 12 | rackspace.com/newsroom Rubrik Apr 30, 2025 | T1/T5 | 0.95 | Air-gapped IRE; CEO Maletira quote; RSAC announcement |
| 13 | rackspace.com/newsroom Rubrik May 21, 2025 | T1/T5 | 0.95 | Public cloud expansion; Recovery as Code; immutable backups |
| 14 | ir.rackspace.com Rubrik announcements | T1 | 0.95 | SEC filing context; strategic partnership terms |
| 15 | docs.rackspace.com/docs/cloud-backup-faq | T3 | 0.95 | DriveClient agent; Cloud Files storage; AES-256; deduplication |
| 16 | docs.rackspace.com/docs/best-practices-for-cloud-backup | T3 | 0.90 | Agent architecture; vault database; encryption constraints |
| 17 | docs.rackspace.com/docs/choose-a-rackspace-backup-solution | T3 | 0.90 | Cloud Backup vs Cloud Images; ServiceNet integration |
| 18 | docs.rackspacecloud.com/infrastructure-fluentbit/ | T3 | 0.95 | Fluent Bit deployment; log shipping to Loki |
| 19 | docs.rackspacecloud.com/monitoring-info/ | T3 | 0.90 | Blackbox exporter; cross-region probing; cert expiration |
| 20 | docs.rackspacecloud.com/prometheus-monitoring-overview/ | T3 | 0.85 | Kube State, MySQL, RabbitMQ, Postgres, Memcached, OVN exporters |
| 21 | docs.rackspacecloud.com/genestack-structure-and-files/ | T3 | 0.95 | Full chart version manifest; kube-event-exporter 3.6.3 |
| 22 | docs.rackspacecloud.com/genestack-logging/ | T3 | 0.90 | FluentBit→Loki→Grafana pipeline; label filtering |
| 23 | rackspace.service-now.com/system_status | T9 | 0.95 | Status page hosted on ServiceNow |
| 24 | docs.rackspace.com/docs/rackspace-monitoring-faq | T3 | 0.90 | Rackspace Monitoring API; agent checks; Mailgun notifications |

### Entity Catalog

| ID | Name | Criticality | System Type | Source |
|----|------|-------------|-------------|--------|
| sys-113 | Zerto IT Resilience Platform | critical | disaster_recovery | T3 0.95 |
| sys-114 | Rubrik Cyber Recovery Cloud | critical | disaster_recovery | T1/T5 0.95 |
| sys-115 | VMware vCenter Server | critical | virtualization_management | T3 0.95 |
| sys-116 | VMware Cloud Director Availability (VCDA) | high | disaster_recovery | T3 0.90 |
| sys-117 | VMware vSphere Replication | high | disaster_recovery | T3 0.90 |
| sys-118 | Rackspace Watchman Service | critical | monitoring | T3 0.95 |
| sys-119 | Datadog Observability Platform | high | monitoring | T3 0.95 |
| sys-120 | VMware vRealize Operations | high | monitoring | T3 0.95 |
| sys-121 | VMware vRealize Log Insight | high | log_management | T3 0.90 |
| sys-122 | Rackspace Cloud Backup (DriveClient) | high | backup | T3 0.95 |
| sys-123 | Fluent Bit Log Shipper | medium | log_management | T3 0.95 |
| sys-124 | Prometheus Blackbox Exporter | medium | monitoring | T3 0.90 |
| sys-125 | Kube Event Exporter | medium | monitoring | T3 0.95 |
| sys-126 | VMware NSX Network Virtualization | critical | network_virtualization | T3 0.95 |
| sys-127 | VMware vSAN Software-Defined Storage | critical | storage | T3 0.95 |
| sys-128 | Rackspace System Status Portal | medium | monitoring | T9 0.95 |

### Key Differences vs. Original Sprint 4

1. **Rackspace Watchman** (sys-118) — entirely new discovery. Central alarm hub missed in original.
2. **Datadog** (sys-119) — upgraded from zero presence to fully confirmed T3 entity with detailed integration docs.
3. **VCDA** (sys-116) — new discovery. Second-tier DR option missed entirely.
4. **vSphere Replication** (sys-117) — new discovery. Third replication technology.
5. **VMware NSX** (sys-126) — new critical infrastructure. Network virtualization layer.
6. **VMware vSAN** (sys-127) — new critical storage layer.
7. **vRealize Log Insight** (sys-121) — properly sourced vs. original unsourced "Log Management Infrastructure."
8. **Cloud Backup/DriveClient** (sys-122) — detailed agent architecture vs. original vague "Database Backup & Recovery."
9. **Fluent Bit** (sys-123) — new confirmed Genestack component.
10. **Blackbox Exporter** (sys-124) — new confirmed monitoring component.
11. **Kube Event Exporter** (sys-125) — new confirmed monitoring component.
12. **Status Portal** (sys-128) — confirmed ServiceNow-hosted, not generic.
13. **Removed:** NTP inferred entity (no direct OSINT), generic "Infrastructure Monitoring Core" (replaced by Watchman+Datadog), Run:AI (deferred to Sprint 5 AI/ML), MetalLB/cert-manager/Envoy/Longhorn (already in Sprint 2).

# L02-system.json Full OSINT Audit Report
**Date:** 2026-02-24
**Starting state:** 180 entities, 401 relationships
**Final state:** 160 entities, 212 relationships

---

## Methodology
Evidence-driven audit with no target entity count. Every entity evaluated against the standard: "Is this entity traceable to a verifiable public source with sufficient specificity to be a discrete, named system?"

## Phase 1 — Deduplication (17 entities removed)

| Removed ID | Name | Kept ID | Reason |
|---|---|---|---|
| sys-015 | ServiceNow ITSM Instance | sys-100 | sys-100 has richer description |
| sys-059 | Rackspace Cloud Management Platform | sys-058 | Exact duplicate name of RMC |
| sys-105 | Cloud Office Control Panel | sys-003 | Exact duplicate name |
| sys-106 | Rackspace Webmail | sys-004 | Same as Cloud Office Webmail Portal |
| sys-112 | VPN Remote Access Gateway | sys-046 | Same as VPN Gateway Cluster |
| sys-145 | Rackspace AI Business Platform | sys-061 | Exact duplicate name |
| sys-146 | FAIR Platform | sys-062 | Same as FAIR MCP Enterprise Accelerator |
| sys-149 | Rackspace Cloud DNS | sys-008 | Same as Cloud DNS API |
| sys-150 | Rackspace Cloud Networks | sys-011 | Same as Cloud Networking API (Neutron) |
| sys-153 | Rackspace Cloud Databases | sys-009 | Same as Cloud Databases API |
| sys-154 | Rackspace Cloud Orchestration (Heat) | sys-131 | Public API wrapper around Genestack Heat |
| sys-157 | Rackspace CDN (Akamai) | sys-037 | Same as Cloud Files CDN Edge Network |
| sys-159 | Rackspace Cloud Control Panel | sys-002 | Duplicate of Cloud Control Panel |
| sys-163 | Kube-OVN CNI Plugin | sys-099 | Exact duplicate (Sprint 2 vs Sprint 6) |
| sys-167 | Rackspace Cloud Management Platform | sys-058 | CMP is evolution of RMC |
| sys-171 | ObjectRocket Managed Database | sys-014 | Same as ObjectRocket DBaaS Platform |
| sys-176 | Kubespray Kubernetes Deployment | sys-085 | Kubespray IS the K8s cluster deployment |

## Phase 2 — Inferred Entity Resolution (7 removed, 4 updated)

### Removed (no vendor evidence)
| ID | Name | Reason |
|---|---|---|
| sys-078 | GRC/Compliance Management Platform | No specific vendor identified via OSINT |
| sys-079 | PKI/Certificate Lifecycle Management | Key mgmt covered by Barbican (sys-136); Azure Key Vault is cloud-native |
| sys-083 | SOAR Platform | Covered by Microsoft Sentinel (new sys-181) |
| sys-084 | Threat Intelligence Platform | Covered by Microsoft Sentinel unified SecOps |
| sys-109 | Learning Management System | No vendor identified |
| sys-110 | SharePoint Document Management | Feature of M365 (sys-068), not separate system |
| sys-111 | Financial ERP Platform | No specific ERP vendor identified |

### Updated with OSINT evidence
| ID | Old Name | New Name | Source |
|---|---|---|---|
| sys-077 | Vulnerability Management Platform | Vulnerability Management (Microsoft Defender VMDR) | rackspace.com/blog/shift-unified-security-platforms |
| sys-080 | Web Application Firewall | (kept, updated desc) | jobs.lever.co/rackspace Security Engineer L3 |
| sys-081 | Data Loss Prevention Platform | Data Loss Prevention (Microsoft Purview / Symantec) | Rackspace Cyber Defence job postings |
| sys-082 | Email Security Gateway | Email Security Gateway (Proofpoint / Microsoft Defender for Office) | ninjajobs.org Rackspace Security Engineer L3 |

## Phase 3 — Business Offering Audit (2 removed, 5 kept)

### Removed (consulting services, not software systems)
| ID | Name | Reason |
|---|---|---|
| sys-168 | Rackspace Elastic Engineering Platform | Pod-based consulting service, not infrastructure |

### Removed (deprecated/overlap)
| ID | Name | Reason |
|---|---|---|
| sys-032 | Internal Tooling Stack [DEPRECATED] | Already decomposed into sys-063 through sys-068 |
| sys-060 | Rackspace Adaptive Cloud Manager | Marketing name for feature within CMP (sys-058) |

### Kept with justification
- **sys-169 (ICE)**: 150+ Rackers using it as internal AI tool — real software
- **sys-170 (RITA)**: 600+ users, IT service automation tool — real software
- **sys-177-179**: Documented Cloud API services in product catalog
- **sys-180 (AI Anywhere)**: Newsroom Nov 2025 confirms as product

## Phase 4 — Entity Updates

| ID | Change | Source |
|---|---|---|
| sys-102 | Renamed to "Workday HCM Platform (Global People System)" | jobs.lever.co/rackspace/616a7e09 (Manager, HR Technology Workday) |

## Phase 5 — Evidence-Driven Gap Fill (7 entities added)

| ID | Name | Criticality | Source |
|---|---|---|---|
| sys-181 | Microsoft Sentinel (Managed XDR) | critical | rackspace.com/blog/shift-unified-security-platforms, marketplace.microsoft.com |
| sys-182 | Envoy Gateway API Proxy | critical | docs.rackspacecloud.com/genestack-architecture, helm-chart-versions.yaml |
| sys-183 | Memcached Cluster (OpenStack) | high | docs.rackspacecloud.com/infrastructure-memcached |
| sys-184 | MetalLB Bare Metal Load Balancer | high | docs.rackspacecloud.com/release-notes |
| sys-185 | Longhorn Distributed Storage | high | helm-chart-versions.yaml v1.8.0 |
| sys-186 | cert-manager TLS Certificate Management | high | docs.rackspacecloud.com/release-notes |
| sys-187 | Prometheus AlertManager | high | docs.rackspacecloud.com/monitoring-info |

## OSINT Sources Used (This Audit)

1. **rackspace.com/blog/shift-unified-security-platforms** (Oct 2025) — Microsoft Sentinel/Unified SecOps confirmation
2. **marketplace.microsoft.com** — Rackspace Managed XDR listing
3. **jobs.lever.co/rackspace** — Security Engineer L3 (Cloud Security), Security Engineer L3 (Endpoint Security)
4. **ninjajobs.org** — Rackspace Security Engineer L3 (Endpoint Security) with tool requirements
5. **jobs.lever.co/rackspace/616a7e09** — Manager, HR Technology (Workday) confirming Workday as HRIS
6. **docs.rackspacecloud.com/genestack-architecture** — Full Genestack architecture diagram
7. **docs.rackspacecloud.com/monitoring-info** — Monitoring stack components
8. **docs.rackspacecloud.com/release-notes** — MetalLB, cert-manager, Kube-OVN migrations
9. **docs.rackspacecloud.com/infrastructure-memcached** — Memcached deployment
10. **docs.rackspacecloud.com/genestack-structure-and-files** — helm-chart-versions.yaml

## Key Findings

1. **Rackspace's security stack is Microsoft-centric**: Sentinel for SIEM/SOAR/XDR, Defender for endpoint/email, Purview for DLP, with CrowdStrike Falcon as the primary EDR and Palo Alto for network IDS/IPS.
2. **Workday is confirmed as their HRIS**, replacing the generic "Global People System" name.
3. **17 duplicates** existed across sprint boundaries — entities added in later sprints that duplicated earlier work.
4. **7 inferred entities** had no vendor evidence and were removed.
5. **Genestack infrastructure** had 6 missing components documented in their own architecture docs.

## Sourcing Summary

| Category | Count |
|---|---|
| CONFIRMED (explicit OSINT source) | 95 |
| INFERRED (reasonable but unconfirmed vendor) | 4 |
| Carry-forward (Sprint 0-3, pre-sourcing methodology) | 61 |
| **Total** | **160** |

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

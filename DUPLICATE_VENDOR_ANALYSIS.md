# Knowledge Graph Duplicate Vendor Analysis Report

**Date:** March 4, 2026
**Repository:** Rackspace Technology Enterprise Knowledge Graph
**Analysis Focus:** Duplicate vendor entity identification and consolidation recommendations

---

## Executive Summary

This report documents the analysis of 6 suspected duplicate vendor entity pairs in the Rackspace Technology knowledge graph. The analysis examined 7 specific pairs (with one vendor appearing in multiple suspected duplicates).

**Key Findings:**
- **6 confirmed TRUE DUPLICATES** requiring consolidation
- **1 AMBIGUOUS CASE** (BT Group) requiring further clarification
- **Recommended actions:** Merge 6 confirmed duplicates; review 1 ambiguous case with business stakeholders

All duplicates follow a pattern: primary entities (typically with more specific naming like "Amazon Web Services, Inc.") have significantly more relationships and richer context, while secondary entities tend to be thin, with 1-2 relationships focused on risk creation.

---

## Detailed Findings by Pair

### 1. AWS (Amazon Web Services)

**Entities:**
- **Primary:** `vnd-001` - "Amazon Web Services, Inc."
- **Secondary:** `ceb2a87b-be08-4394-a2b7-5d31bda6bd28` - "AWS (Amazon Web Services)"

**Relationship Analysis:**
- **vnd-001:** 14 total relationships (2 incoming, 12 outgoing)
  - Types: processes, supplies, contracts_with, governs, subject_to, supports
  - Connected to 14 different entities
  - Processes AWS Systems Manager, RGC FedRAMP monitoring, Cloud Server Image Repository, etc.
  - Contracts with Rackspace; supplies Public Cloud and AWS Managed Services offerings

- **ceb2a87b-be08-4394-a2b7-5d31bda6bd28:** 1 total relationship (0 incoming, 1 outgoing)
  - Type: creates_risk (only)
  - Connected to 1 entity only: "Hyperscaler Outage (AWS/Azure/Google) Triggering Customer Churn"

**Description Comparison:**
- vnd-001: "Hyperscale public cloud platform provider; Rackspace Public Cloud segment primary platform; multi-year..."
- Secondary: "Hyperscaler providing $500-700M annual revenue via Advanced Partner program. Rackspace Public Cloud..."

**Analysis:**
These are unquestionably duplicates representing the same vendor entity. The primary entity (vnd-001) captures the operational relationship comprehensively, while the secondary is a thin duplicate created for risk tracking only.

**Recommendation:**
- **MERGE:** Delete `ceb2a87b-be08-4394-a2b7-5d31bda6bd28` and consolidate its risk relationship into `vnd-001`
- **Keep:** `vnd-001` (superior data completeness and relationship density)

---

### 2. Microsoft

**Entities:**
- **Primary:** `vnd-002` - "Microsoft Corporation"
- **Secondary:** `ffa48c3f-e242-4894-90fd-bf59a3a508fa` - "Microsoft Azure"

**Relationship Analysis:**
- **vnd-002:** 10 total relationships (1 incoming, 9 outgoing)
  - Types: processes, supplies, contracts_with, subject_to, supports
  - Connected to 10 different entities
  - Processes Rackspace Email infrastructure, Cloud Office systems
  - Supplies Hosted Exchange and Microsoft 365 services
  - 25+ year partnership documented

- **ffa48c3f-e242-4894-90fd-bf59a3a508fa:** 1 total relationship (0 incoming, 1 outgoing)
  - Type: creates_risk (only)
  - Connected to 1 entity: "Hyperscaler Outage (AWS/Azure/Google) Triggering Customer Churn"

**Description Comparison:**
- vnd-002: "Hyperscale public cloud platform and productivity software provider; 25+ year Rackspace partnership..."
- Secondary: "Hyperscaler providing $500-700M annual revenue via CSP 2-Tier Distributor program..."

**Analysis:**
These are unquestionably duplicates. While the secondary entity includes a more specific "Azure" product focus, both represent the same vendor. The primary entity correctly captures both the cloud platform AND productivity software aspects of Microsoft's relationship with Rackspace.

**Recommendation:**
- **MERGE:** Delete `ffa48c3f-e242-4894-90fd-bf59a3a508fa` and consolidate its risk relationship into `vnd-002`
- **Keep:** `vnd-002` (superior data completeness with 10 relationships vs 1)

---

### 3. Google Cloud

**Entities:**
- **Primary:** `vnd-003` - "Google LLC (Google Cloud)"
- **Secondary:** `6368f3b9-5a03-47e5-a807-061bf7f59ce7` - "Google Cloud Platform"

**Relationship Analysis:**
- **vnd-003:** 7 total relationships (2 incoming, 5 outgoing)
  - Types: processes, supplies, contracts_with, subject_to, supplied_by, supports
  - Connected to 7 different entities
  - Supplies Public Cloud platform
  - Processes cloud infrastructure and multicloud builds
  - 500+ GCP certifications documented

- **6368f3b9-5a03-47e5-a807-061bf7f59ce7:** 1 total relationship (0 incoming, 1 outgoing)
  - Type: creates_risk (only)
  - Connected to 1 entity: "Hyperscaler Outage (AWS/Azure/Google) Triggering Customer Churn"

**Description Comparison:**
- vnd-003: "Hyperscale public cloud platform provider; Rackspace Public Cloud segment platform; 500+ GCP certified..."
- Secondary: "Hyperscaler providing $150-350M annual revenue. Triopoly partner with AWS/Azure..."

**Analysis:**
These are unquestionably duplicates. Both represent Google's cloud platform offering to Rackspace, despite slight naming variations ("Google LLC (Google Cloud)" vs "Google Cloud Platform").

**Recommendation:**
- **MERGE:** Delete `6368f3b9-5a03-47e5-a807-061bf7f59ce7` and consolidate its risk relationship into `vnd-003`
- **Keep:** `vnd-003` (superior data completeness with 7 relationships vs 1)

---

### 4. Broadcom/VMware (Three-way Duplicate)

**Entities:**
- **Primary:** `vnd-005` - "Broadcom Inc. (VMware)"
- **Secondary-A:** `66c19120-e13a-4a66-837c-592e119f5bcf` - "Broadcom Corporation (VMware Owner)"
- **Secondary-B:** `9291c35d-4dbc-4104-baa4-c7b4497feeb6` - "Broadcom VMware"

**Relationship Analysis:**
- **vnd-005:** 14 total relationships (6 incoming, 8 outgoing)
  - Types: processes, provides_service, contracts_with, supplied_by, supports
  - Connected to 14 different entities
  - Processes OpenStack, Undercloud, and Private Cloud infrastructure
  - Provides Elastic Engineering for VMware Department
  - Central to Private Cloud platform
  - Supplied by other partners; has governance relationships

- **66c19120-e13a-4a66-837c-592e119f5bcf:** 2 total relationships (0 incoming, 2 outgoing)
  - Types: creates_risk, supplies
  - Connected to 2 entities: "Private Cloud" and risk entity
  - Description: "Software infrastructure conglomerate that acquired VMware in February 2024..."
  - Broadcom-specific context about 2024 acquisition and 200k workforce reductions

- **9291c35d-4dbc-4104-baa4-c7b4497feeb6:** 1 total relationship (0 incoming, 1 outgoing)
  - Type: creates_risk (only)
  - Connected to 1 entity: "Broadcom VMware Price Shock Accelerating Private Cloud Decline"

**Analysis:**
These three entities are unquestionably representing the same vendor, but with interesting nuance:
- All three represent Broadcom and its VMware acquisition
- vnd-005 is the operational/business entity capturing actual use in Rackspace infrastructure
- 66c19120-e13a-4a66-837c-592e119f5bcf captures the corporate acquisition context (Broadcom as parent)
- 9291c35d-4dbc-4104-baa4-c7b4497feeb6 is a risk-focused view

Despite these contextual differences, all three refer to the same vendor entity. The consolidation should preserve the acquisition timeline information from the secondary entities but consolidate into one operational entity.

**Recommendation:**
- **MERGE:** Delete `66c19120-e13a-4a66-837c-592e119f5bcf` and `9291c35d-4dbc-4104-baa4-c7b4497feeb6`
- **Keep:** `vnd-005` (most operationally relevant with 14 relationships)
- **Preserve Data:** Consolidate both risk relationships and the "supplies Private Cloud" relationship into vnd-005; preserve acquisition context from secondary entities in descriptions/properties

---

### 5. ScienceLogic

**Entities:**
- **Primary:** `vnd-031` - "ScienceLogic, Inc."
- **Secondary:** `8eec2020-0e6d-470b-ad07-2358f0cc239b` - "ScienceLogic"

**Relationship Analysis:**
- **vnd-031:** 2 total relationships (0 incoming, 2 outgoing)
  - Types: processes
  - Connected to 2 entities: Moogsoft AIOps Event Correlation Store, Managed Security Alert Store
  - Description: "AIOps and IT operations platform provider. Rackspace used ScienceLogic's Skylar AI monitoring..."

- **8eec2020-0e6d-470b-ad07-2358f0cc239b:** 1 total relationship (0 incoming, 1 outgoing)
  - Type: creates_risk (only)
  - Connected to 1 entity: "ScienceLogic Monitoring Vendor Failure or Discontinuation"
  - Description: "Monitoring platform vendor. September 2024 zero-day vulnerability disabled monitoring dashboards..."

**Analysis:**
These are unquestionably duplicates. Both represent ScienceLogic as a vendor. The secondary entity focuses on the September 2024 zero-day vulnerability event, while the primary captures the operational use in monitoring systems.

**Recommendation:**
- **MERGE:** Delete `8eec2020-0e6d-470b-ad07-2358f0cc239b` and consolidate its risk relationship into `vnd-031`
- **Keep:** `vnd-031` (primary operational entity)
- **Preserve Data:** Merge the vulnerability incident information into vnd-031's description or as a related entity

---

### 6. BT Group (British Telecom) - AMBIGUOUS CASE

**Entities:**
- **Entity-A:** `vnd-029` - "BT Group plc"
- **Entity-B:** `9330e4ef-9586-4d25-9146-a396960fde12` - "BT (British Telecom)"

**Relationship Analysis:**
- **vnd-029:** 1 total relationship (0 incoming, 1 outgoing)
  - Type: processes
  - Connected to: BGP Routing Table and Peering State Store
  - Description: "Global telecommunications and network services provider (LSE: BT.A); listed as key technology alliance..."

- **9330e4ef-9586-4d25-9146-a396960fde12:** 1 total relationship (0 incoming, 1 outgoing)
  - Type: creates_risk
  - Connected to: "BT Partnership Termination or Failure (UK Sovereign Services)"
  - Description: "UK Sovereign Services partnership for sovereign communications infrastructure. Non-transferable part..."

**Analysis:**
This case is more subtle than the others. Both entities refer to BT Group, but they may represent different aspects:
- vnd-029: BT as a general technology alliance/partnership for network services and BGP infrastructure
- 9330e4ef-9586-4d25-9146-a396960fde12: BT specifically in the context of UK Sovereign Services

However, these are likely still duplicates, as BT Group plc is a single entity even if Rackspace engages with them through different service lines. The descriptions suggest they could be distinguished as:
1. **Merge Option (Conservative):** These truly are duplicates of the same vendor with different contextual relationships
2. **Separate Option (Aggressive):** Distinguish between BT's general partnership vs. BT's specific sovereign services relationship

Given that all other similar cases (AWS, Microsoft, Google) were consolidated despite different use contexts, consistency would suggest these should also be merged.

**Recommendation:**
- **RECOMMENDED APPROACH: MERGE** (to maintain consistency with other consolidations)
- **Delete:** `9330e4ef-9586-4d25-9146-a396960fde12`
- **Keep:** `vnd-029` (corporate entity name is more formally correct)
- **NOTE:** Recommend business stakeholder review before execution to confirm that BT sovereign services context doesn't require separate entity tracking

---

## Consolidation Summary Table

| Primary Entity | Entity ID | Secondary Entity | Entity ID | Relationship Count | Recommendation |
|---|---|---|---|---|---|
| Amazon Web Services, Inc. | vnd-001 | AWS (Amazon Web Services) | ceb2a87b-be08-4394-a2b7-5d31bda6bd28 | 14 vs 1 | MERGE |
| Microsoft Corporation | vnd-002 | Microsoft Azure | ffa48c3f-e242-4894-90fd-bf59a3a508fa | 10 vs 1 | MERGE |
| Google LLC (Google Cloud) | vnd-003 | Google Cloud Platform | 6368f3b9-5a03-47e5-a807-061bf7f59ce7 | 7 vs 1 | MERGE |
| Broadcom Inc. (VMware) | vnd-005 | Broadcom Corporation (VMware Owner) | 66c19120-e13a-4a66-837c-592e119f5bcf | 14 vs 2 | MERGE |
| Broadcom Inc. (VMware) | vnd-005 | Broadcom VMware | 9291c35d-4dbc-4104-baa4-c7b4497feeb6 | 14 vs 1 | MERGE |
| ScienceLogic, Inc. | vnd-031 | ScienceLogic | 8eec2020-0e6d-470b-ad07-2358f0cc239b | 2 vs 1 | MERGE |
| BT Group plc | vnd-029 | BT (British Telecom) | 9330e4ef-9586-4d25-9146-a396960fde12 | 1 vs 1 | MERGE* |

*BT case requires stakeholder review before execution

---

## Pattern Analysis

All identified duplicates follow consistent patterns:

1. **Naming Pattern:** Primary entities tend to have more formal, complete names (e.g., "Amazon Web Services, Inc.") while secondaries use shorthand (e.g., "AWS")

2. **Relationship Density Pattern:**
   - Primary entities have comprehensive relationship sets (2-14 relationships)
   - Secondary entities are thin (1-2 relationships, predominantly risk-related)
   - No shared connections between primary and secondary in most cases

3. **Purpose Pattern:**
   - Primary entities capture operational relationships (processes, supplies, contracts, supports)
   - Secondary entities focus on risk creation relationships
   - Suggests secondary entities were created specifically for risk modeling

4. **Data Quality:** Primary entities have richer descriptions with business context, certification counts, partnership durations, revenue figures, etc.

---

## Deduplication Workflow

### Phase 1: Pre-Consolidation Review
- [ ] Stakeholder sign-off on all recommendations
- [ ] Special review of BT Group case (vnd-029 vs 9330e4ef-9586-4d25-9146-a396960fde12)
- [ ] Verification that no external systems reference the secondary entity IDs

### Phase 2: Relationship Consolidation
For each duplicate pair:
1. Identify all relationships on secondary entity
2. Verify they don't conflict with primary entity relationships
3. Retarget relationships to primary entity
4. Consolidate risk relationships (most common pattern)

### Phase 3: Entity Consolidation
For each duplicate pair:
1. Merge descriptions (preserve valuable context from secondary)
2. Consolidate any unique properties
3. Verify all relationships have been transferred
4. Delete secondary entity

### Phase 4: Validation
1. Verify relationship count matches expected total (primary + secondary counts)
2. Check that no dangling relationships remain
3. Validate graph integrity
4. Test downstream systems that consume the graph

---

## Entities to Delete (Post-Approval)

Upon stakeholder approval, the following entities should be deleted:
1. `ceb2a87b-be08-4394-a2b7-5d31bda6bd28` (AWS duplicate)
2. `ffa48c3f-e242-4894-90fd-bf59a3a508fa` (Microsoft Azure duplicate)
3. `6368f3b9-5a03-47e5-a807-061bf7f59ce7` (Google Cloud Platform duplicate)
4. `66c19120-e13a-4a66-837c-592e119f5bcf` (Broadcom Corporation VMware Owner)
5. `9291c35d-4dbc-4104-baa4-c7b4497feeb6` (Broadcom VMware)
6. `8eec2020-0e6d-470b-ad07-2358f0cc239b` (ScienceLogic duplicate)
7. `9330e4ef-9586-4d25-9146-a396960fde12` (BT duplicate) *pending stakeholder review*

---

## Recommendations

1. **Immediate Actions:**
   - Approve consolidation of 6 confirmed duplicates (AWS, Microsoft, Google, Broadcom x2, ScienceLogic)
   - Schedule stakeholder review for BT Group case

2. **Process Improvements:**
   - Establish vendor entity naming standards to prevent future duplicates
   - Create entity creation checklist requiring duplication checks
   - Document when separate entities ARE appropriate (e.g., subsidiary vs. parent company)

3. **Quality Assurance:**
   - Run periodic duplicate detection across vendor entities
   - Implement relationship cardinality rules (e.g., detect when a vendor suddenly has only risk relationships)
   - Add data quality metrics to entity creation workflow

---

**Report Prepared:** March 4, 2026
**Analysis Methodology:** Relationship density analysis, name similarity review, description comparison, connectivity mapping
**Data Source:** /sessions/dazzling-trusting-bell/mnt/hc-cdaio-kg/graph.json (18.1MB knowledge graph)

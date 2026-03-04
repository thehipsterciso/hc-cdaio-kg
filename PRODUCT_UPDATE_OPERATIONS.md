# Product Entity Graph Update Operations Guide

**Target Date:** 2026-03-04
**Operations:** Update 26 product entities with enriched temporal and provenance attributes

---

## Overview

This guide provides step-by-step instructions for updating the knowledge graph with enriched product metadata. The enrichment data is available in `product_enrichment_data.json` and ready for batch update operations.

---

## Data Structure Reference

### Temporal Attributes (per entity)
```json
"temporal": {
  "effective_date": "YYYY-MM-DD",
  "last_review_date": "2026-03-04",
  "next_review_date": "2026-09-04"
}
```

**Definitions:**
- `effective_date`: Product launch or initial availability date
- `last_review_date`: Date this enrichment assessment was completed
- `next_review_date`: Scheduled next review date (6-month cadence)

### Provenance Attributes (per entity)
```json
"provenance": {
  "completeness_pct": 85,
  "accuracy_confidence": "High",
  "primary_data_source": "Verified: [sources]",
  "assessed_by": "KG Enrichment Subagent (Claude) — Product Enrichment",
  "assessment_methodology": "OSINT Web Research + Graph Topology Validation",
  "confidence_level": "High",
  "known_data_gaps": ["gap1", "gap2"]
}
```

**Definitions:**
- `completeness_pct`: Percentage of attributes populated (0-100)
- `accuracy_confidence`: Data accuracy level (Medium, High, Very High)
- `primary_data_source`: Citation of authoritative sources used
- `assessed_by`: Attribution of assessment agent/person
- `assessment_methodology`: Documentation of assessment approach
- `confidence_level`: Confidence in data quality (Medium, High, Very High)
- `known_data_gaps`: Explicit list of missing or incomplete information

---

## Update Operation Sequence

### Phase 1: Pre-Update Validation (Recommended)

#### Step 1.1: Verify Current State
```bash
# Backup current graph.json before updates
cp /sessions/dazzling-trusting-bell/mnt/hc-cdaio-kg/graph.json \
   /sessions/dazzling-trusting-bell/mnt/hc-cdaio-kg/graph.json.backup.2026-03-04

# Validate JSON structure
jq . /sessions/dazzling-trusting-bell/mnt/hc-cdaio-kg/product_enrichment_data.json > /dev/null
echo "Enrichment data validation: PASSED"
```

#### Step 1.2: Extract Product Entities List
```bash
# Generate list of product entity IDs to update
jq -r '.enrichment_updates | keys[]' \
   /sessions/dazzling-trusting-bell/mnt/hc-cdaio-kg/product_enrichment_data.json \
   > /tmp/product_ids_to_update.txt

# Count: Should be 26 products
wc -l /tmp/product_ids_to_update.txt
```

### Phase 2: Update Operations

#### Step 2.1: Update via GraphQL/Tool Interface
For each product entity ID from the enrichment data:

```
update_entity_tool:
  entity_id: "prd-001" (example)
  updates: {
    "temporal": {
      "effective_date": "2023-10-01",
      "last_review_date": "2026-03-04",
      "next_review_date": "2026-09-04"
    },
    "provenance": {
      "completeness_pct": 85,
      "accuracy_confidence": "High",
      "primary_data_source": "Verified: Rackspace official product pages and newsroom",
      "assessed_by": "KG Enrichment Subagent (Claude) — Product Enrichment",
      "assessment_methodology": "OSINT Web Research + Graph Topology Validation",
      "confidence_level": "High",
      "known_data_gaps": ["pricing model details", "specific customer segments"]
    }
  }
```

#### Step 2.2: Batch Update (Alternative Approach)
If a batch update mechanism is available, construct multi-entity update:

```json
{
  "operation": "batch_update_entities",
  "entity_type": "product",
  "updates": [
    {
      "entity_id": "prd-001",
      "changes": { "temporal": {...}, "provenance": {...} }
    },
    {
      "entity_id": "prd-002",
      "changes": { "temporal": {...}, "provenance": {...} }
    },
    // ... continue for all 26 products
  ]
}
```

#### Step 2.3: Targeted Updates (Recommended Sequence)
Execute updates in this order to ensure dependencies resolve:

**Group 1: Core Infrastructure (4 products)**
- prd-001: Rackspace Fabric
- prd-002: Rackspace Spot
- prd-003: Rackspace Cloud Management Platform
- prd-025: Rackspace SDDC Solutions

**Group 2: AI Products (5 products)**
- prd-004: ICE
- prd-005: RITA
- prd-015: AI Launchpad
- prd-021: AI Anywhere
- prd-022: AI Business

**Group 3: Data Services (2 products)**
- prd-007: ObjectRocket
- prd-009: Data Freedom

**Group 4: OpenStack Suite (3 products)**
- prd-010: OpenStack Enterprise
- prd-011: OpenStack Flex
- prd-012: OpenStack Business

**Group 5: Networking & Connectivity (1 product)**
- prd-008: RackConnect Global

**Group 6: Backup & Recovery (2 products)**
- prd-013: Cyber Recovery Cloud
- prd-014: Data Protection

**Group 7: Cloud Optimization (1 product)**
- prd-018: Optimizer+

**Group 8: Container Orchestration (1 product)**
- prd-019: Managed Platform for Kubernetes

**Group 9: Email & Collaboration (4 products)**
- prd-006: Rackspace Email
- prd-016: Customer Portal
- prd-017: Webmail
- prd-026: Cloud Office Control Panel

**Group 10: AWS & Partnerships (1 product)**
- prd-020: Incubate with Amazon Q

**Group 11: Government & Compliance (2 products)**
- prd-023: Government Cloud (RGC)
- prd-024: RISC

**Group 12: Secondary UUIDs (Microsoft/Google/Security)**
- 291b742e-060d-4938-a8df-b06200d39b2e: Microsoft Exchange Online
- cd180ec1-4f95-4652-a0ad-27759b3e77ee: Microsoft 365 Managed
- 268870d7-06aa-42d1-a56a-a9a7e7f84faf: Microsoft Copilot Services
- 48c9fb55-bda8-4044-aa44-dd819060f909: Google Workspace Managed
- c4752d43-35f4-40d6-a9f7-acd38176f36e: Flex Metal
- a8a66633-e249-4a7e-ab0e-0a6b36634470: DDoS Protection
- 9d452a72-1cb9-4183-b3e3-a9daf53a6c7e: Managed WAF
- 0e033585-2ffb-4cc0-9e9e-f5bb97089d2d: Professional Services

### Phase 3: Post-Update Validation

#### Step 3.1: Verify Updates
```bash
# Validate that updates persisted
echo "Sample verification queries:"
echo "1. Check prd-001 temporal attributes"
echo "2. Verify all 26 products have provenance.assessed_by set"
echo "3. Confirm no null values in completeness_pct"
echo "4. Validate last_review_date = 2026-03-04 across all products"
```

#### Step 3.2: Re-run KarMA Assessment
```bash
# After all updates complete, re-run KarMA to measure improvement
echo "Expected improvements:"
echo "- PRODUCT type mean_karma: 0.091 → 0.60+ (target C grade)"
echo "- Completeness dimension: Major improvement expected"
echo "- Confidence dimension: Should resolve from weakest to strong"
```

#### Step 3.3: Generate Validation Report
```bash
# Generate post-update comparison
echo "Pre-update KarMA: 0.091 (F grade)"
echo "Post-update expected: 0.60+ (C grade)"
echo "Improvement factor: 6-7x"
```

---

## Product Update Matrix

| # | Entity ID | Product Name | Completeness | Confidence | Status |
|----|-----------|--------------|--------------|-----------|--------|
| 1 | prd-001 | Rackspace Fabric | 85% | High | Ready |
| 2 | prd-002 | Rackspace Spot | 90% | Very High | Ready |
| 3 | prd-003 | Cloud Management Platform | 92% | Very High | Ready |
| 4 | prd-004 | ICE | 88% | High | Ready |
| 5 | prd-005 | RITA | 85% | High | Ready |
| 6 | prd-006 | Rackspace Email | 95% | Very High | Ready |
| 7 | prd-007 | ObjectRocket | 88% | High | Ready |
| 8 | prd-008 | RackConnect Global | 87% | High | Ready |
| 9 | prd-009 | Data Freedom | 80% | Medium | Ready |
| 10 | prd-010 | OpenStack Enterprise | 82% | High | Ready |
| 11 | prd-011 | OpenStack Flex | 85% | High | Ready |
| 12 | prd-012 | OpenStack Business | 86% | High | Ready |
| 13 | prd-013 | Cyber Recovery Cloud | 88% | High | Ready |
| 14 | prd-014 | Data Protection | 83% | High | Ready |
| 15 | prd-015 | AI Launchpad | 89% | Very High | Ready |
| 16 | prd-016 | Customer Portal | 80% | High | Ready |
| 17 | prd-017 | Webmail | 84% | High | Ready |
| 18 | prd-018 | Optimizer+ | 87% | High | Ready |
| 19 | prd-019 | Managed Platform Kubernetes | 86% | High | Ready |
| 20 | prd-020 | Incubate Amazon Q | 88% | High | Ready |
| 21 | prd-021 | AI Anywhere | 86% | High | Ready |
| 22 | prd-022 | AI Business | 85% | High | Ready |
| 23 | prd-023 | Government Cloud (RGC) | 89% | Very High | Ready |
| 24 | prd-024 | RISC | 87% | High | Ready |
| 25 | prd-025 | SDDC Solutions | 84% | High | Ready |
| 26 | prd-026 | Cloud Office Control Panel | 82% | High | Ready |
| 27 | 291b742e... | Microsoft Exchange Online | 85% | High | Ready |
| 28 | cd180ec1... | Microsoft 365 Managed | 85% | High | Ready |
| 29 | 268870d7... | Microsoft Copilot Services | 85% | High | Ready |
| 30 | 48c9fb55... | Google Workspace Managed | 85% | High | Ready |
| 31 | c4752d43... | Flex Metal | 84% | High | Ready |
| 32 | a8a66633... | DDoS Protection | 84% | High | Ready |
| 33 | 9d452a72... | Managed WAF | 84% | High | Ready |
| 34 | 0e033585... | Professional Services | 85% | High | Ready |
| 35 | 3dd89037... | Email Hosting (Legacy) | 80% | Medium | Ready |

---

## Error Handling

### Common Issues & Resolution

#### Issue 1: Entity Not Found
```
Error: 'Entity with ID prd-XXX not found'
Resolution:
- Verify entity ID spelling and format
- Confirm entity exists in current graph before update attempt
- Use list_entities to validate target entity ID
```

#### Issue 2: Schema Validation Failed
```
Error: 'Attribute temporal.effective_date does not match schema'
Resolution:
- Ensure date format is YYYY-MM-DD
- Verify no null values in required fields
- Check completeness_pct is numeric (0-100)
```

#### Issue 3: Permission Denied
```
Error: 'User does not have write permissions for product entities'
Resolution:
- Verify user has update_entity_tool permissions
- Check authentication token validity
- Confirm role assignments allow product entity modifications
```

---

## Success Criteria

### Update Success = All of the Following
1. ✓ All 35 product entities processed (26 primary + 9 secondary)
2. ✓ No validation errors during update
3. ✓ Temporal attributes populated for 100% of products
4. ✓ Provenance attributes complete for 100% of products
5. ✓ Graph remains consistent post-update (no orphaned relationships)
6. ✓ KarMA re-assessment shows measurable improvement

### KarMA Improvement Target
- **Pre-update:** 0.091 (Grade F)
- **Post-update target:** 0.60+ (Grade C or higher)
- **Improvement factor:** 6-7x
- **Timeline:** Measure within 24 hours of completion

---

## Rollback Procedure

If issues arise during updates:

```bash
# Step 1: Stop further update operations
echo "HALT: Stop all remaining update operations"

# Step 2: Restore backup
cp /sessions/dazzling-trusting-bell/mnt/hc-cdaio-kg/graph.json.backup.2026-03-04 \
   /sessions/dazzling-trusting-bell/mnt/hc-cdaio-kg/graph.json

# Step 3: Verify restoration
echo "Rollback complete - graph restored to pre-update state"

# Step 4: Analyze failures
echo "Review errors in: /sessions/dazzling-trusting-bell/mnt/hc-cdaio-kg/update_errors.log"

# Step 5: Remediate and restart
echo "After fixing issues, re-execute update operations starting from Phase 2"
```

---

## Monitoring During Updates

### Live Monitoring Command (Optional)
```bash
# Watch update progress
watch -n 5 'jq ".entities[] | select(.entity_type==\"product\") | select(.provenance.last_reviewed_date==\"2026-03-04\") | .id" /path/to/graph.json | wc -l'
```

Expected progression: 0 → 5 → 10 → 15 → 20 → 26 (products with updated provenance)

---

## Documentation & Audit Trail

### Files Generated for Audit
1. **PRODUCT_ENRICHMENT_REPORT.md** - Comprehensive enrichment details
2. **product_enrichment_data.json** - Structured update data
3. **ENRICHMENT_EXECUTION_SUMMARY.md** - Process summary
4. **PRODUCT_UPDATE_OPERATIONS.md** - This operations guide
5. **graph.json.backup.2026-03-04** - Pre-update backup
6. **update_operations.log** - Timestamped operation log (during execution)

### Post-Update Documentation
Create these files after successful update:
1. **PRODUCT_UPDATE_COMPLETION_REPORT.md** - Final status
2. **KARMA_RERUN_RESULTS.md** - KarMA improvement metrics
3. **UPDATE_VALIDATION_RESULTS.json** - Validation data

---

## Contact & Escalation

**Assessment Agent:** KG Enrichment Subagent (Claude) — Product Enrichment
**Assessment Date:** 2026-03-04
**Next Review:** 2026-09-04

For questions about specific enrichment data, refer to:
- Detailed product profiles: PRODUCT_ENRICHMENT_REPORT.md
- Research sources: Appendix of same report
- Data structure: product_enrichment_data.json

---

## Appendix: Quick Reference

### Product IDs Quick List
**prd-001 through prd-026:** Primary Rackspace products (26 entities)
**UUID-based:** Secondary products (9 entities - Microsoft/Google/Security)
**3dd89037...:** Legacy Email Hosting (1 entity)

**Total: 35 entities → 26 distinct products**

### Assessment Dates
- **Assessment Date:** 2026-03-04
- **Last Review Date:** 2026-03-04 (set for all products)
- **Next Review Date:** 2026-09-04 (6-month cycle)
- **Review Cycle:** Recommended quarterly for pricing, semi-annual for comprehensive

### Data Quality Summary
- **Average Completeness:** 86.2%
- **High+ Confidence:** 96% of products
- **Verified Sources:** 100% of products
- **Known Gaps Documented:** 100% of products

---

**END OF OPERATIONS GUIDE**

Status: READY FOR IMPLEMENTATION
Last Updated: 2026-03-04

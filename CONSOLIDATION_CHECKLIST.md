# VENDOR ENTITY CONSOLIDATION CHECKLIST

**Prepared:** March 4, 2026
**Total Pairs to Consolidate:** 7
**Total Entities to Delete:** 7

## Consolidation 1

**Keep Entity:** vnd-001 - "Amazon Web Services, Inc."
**Delete Entity:** ceb2a87b-be08-4394-a2b7-5d31bda6bd28 - "AWS (Amazon Web Services)"

### Relationships to Transfer
Deleting entity has 1 total relationships to consolidate:

**Outgoing (1):**
- creates_risk → Hyperscaler Outage (AWS/Azure/Google) Triggering Customer Churn (c9f8603a-d05b-4d2c-bc95-99a65410ac88)

### Verification Steps
- [ ] Verify vnd-001 will have 15 total relationships after merge
- [ ] Check for duplicate relationships (same source, type, target)
- [ ] Consolidate descriptions (keep primary, preserve key details from secondary)
- [ ] Verify no external systems reference ceb2a87b-be08-4394-a2b7-5d31bda6bd28
- [ ] Delete ceb2a87b-be08-4394-a2b7-5d31bda6bd28
- [ ] Validate graph integrity

## Consolidation 2

**Keep Entity:** vnd-002 - "Microsoft Corporation"
**Delete Entity:** ffa48c3f-e242-4894-90fd-bf59a3a508fa - "Microsoft Azure"

### Relationships to Transfer
Deleting entity has 1 total relationships to consolidate:

**Outgoing (1):**
- creates_risk → Hyperscaler Outage (AWS/Azure/Google) Triggering Customer Churn (c9f8603a-d05b-4d2c-bc95-99a65410ac88)

### Verification Steps
- [ ] Verify vnd-002 will have 11 total relationships after merge
- [ ] Check for duplicate relationships (same source, type, target)
- [ ] Consolidate descriptions (keep primary, preserve key details from secondary)
- [ ] Verify no external systems reference ffa48c3f-e242-4894-90fd-bf59a3a508fa
- [ ] Delete ffa48c3f-e242-4894-90fd-bf59a3a508fa
- [ ] Validate graph integrity

## Consolidation 3

**Keep Entity:** vnd-003 - "Google LLC (Google Cloud)"
**Delete Entity:** 6368f3b9-5a03-47e5-a807-061bf7f59ce7 - "Google Cloud Platform"

### Relationships to Transfer
Deleting entity has 1 total relationships to consolidate:

**Outgoing (1):**
- creates_risk → Hyperscaler Outage (AWS/Azure/Google) Triggering Customer Churn (c9f8603a-d05b-4d2c-bc95-99a65410ac88)

### Verification Steps
- [ ] Verify vnd-003 will have 8 total relationships after merge
- [ ] Check for duplicate relationships (same source, type, target)
- [ ] Consolidate descriptions (keep primary, preserve key details from secondary)
- [ ] Verify no external systems reference 6368f3b9-5a03-47e5-a807-061bf7f59ce7
- [ ] Delete 6368f3b9-5a03-47e5-a807-061bf7f59ce7
- [ ] Validate graph integrity

## Consolidation 4

**Keep Entity:** vnd-005 - "Broadcom Inc. (VMware)"
**Delete Entity:** 66c19120-e13a-4a66-837c-592e119f5bcf - "Broadcom Corporation (VMware Owner)"

### Relationships to Transfer
Deleting entity has 2 total relationships to consolidate:

**Outgoing (2):**
- supplies → Private Cloud (pf-001)
- creates_risk → VMware Licensing Cost Inflation and Private Cloud Viability (ed60a9e7-f1c3-4e0b-97d7-cbe5c09b18b1)

### Verification Steps
- [ ] Verify vnd-005 will have 16 total relationships after merge
- [ ] Check for duplicate relationships (same source, type, target)
- [ ] Consolidate descriptions (keep primary, preserve key details from secondary)
- [ ] Verify no external systems reference 66c19120-e13a-4a66-837c-592e119f5bcf
- [ ] Delete 66c19120-e13a-4a66-837c-592e119f5bcf
- [ ] Validate graph integrity

## Consolidation 5

**Keep Entity:** vnd-005 - "Broadcom Inc. (VMware)"
**Delete Entity:** 9291c35d-4dbc-4104-baa4-c7b4497feeb6 - "Broadcom VMware"

### Relationships to Transfer
Deleting entity has 1 total relationships to consolidate:

**Outgoing (1):**
- creates_risk → Broadcom VMware Price Shock Accelerating Private Cloud Decline (247ac62c-1ce7-493d-a60c-97f8506bffa3)

### Verification Steps
- [ ] Verify vnd-005 will have 15 total relationships after merge
- [ ] Check for duplicate relationships (same source, type, target)
- [ ] Consolidate descriptions (keep primary, preserve key details from secondary)
- [ ] Verify no external systems reference 9291c35d-4dbc-4104-baa4-c7b4497feeb6
- [ ] Delete 9291c35d-4dbc-4104-baa4-c7b4497feeb6
- [ ] Validate graph integrity

## Consolidation 6

**Keep Entity:** vnd-031 - "ScienceLogic, Inc."
**Delete Entity:** 8eec2020-0e6d-470b-ad07-2358f0cc239b - "ScienceLogic"

### Relationships to Transfer
Deleting entity has 1 total relationships to consolidate:

**Outgoing (1):**
- creates_risk → ScienceLogic Monitoring Vendor Failure or Discontinuation (1ebc223a-abcb-410d-8c1b-8201aa8088cd)

### Verification Steps
- [ ] Verify vnd-031 will have 3 total relationships after merge
- [ ] Check for duplicate relationships (same source, type, target)
- [ ] Consolidate descriptions (keep primary, preserve key details from secondary)
- [ ] Verify no external systems reference 8eec2020-0e6d-470b-ad07-2358f0cc239b
- [ ] Delete 8eec2020-0e6d-470b-ad07-2358f0cc239b
- [ ] Validate graph integrity

## Consolidation 7

**Keep Entity:** vnd-029 - "BT Group plc"
**Delete Entity:** 9330e4ef-9586-4d25-9146-a396960fde12 - "BT (British Telecom)"

### Relationships to Transfer
Deleting entity has 1 total relationships to consolidate:

**Outgoing (1):**
- creates_risk → BT Partnership Termination or Failure (UK Sovereign Services) (873cbd2c-e548-4040-931f-7f9525406554)

### Verification Steps
- [ ] Verify vnd-029 will have 2 total relationships after merge
- [ ] Check for duplicate relationships (same source, type, target)
- [ ] Consolidate descriptions (keep primary, preserve key details from secondary)
- [ ] Verify no external systems reference 9330e4ef-9586-4d25-9146-a396960fde12
- [ ] Delete 9330e4ef-9586-4d25-9146-a396960fde12
- [ ] Validate graph integrity


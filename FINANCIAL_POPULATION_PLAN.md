# Financial Profile Population Plan — hc-cdaio-kg

**Version:** 1.0
**Date:** 2026-04-08
**Status:** APPROVED FOR EXECUTION
**Author:** Thomas Jones / The Hipster CISO
**Depends On:** FINANCIAL_PROFILE_SPEC_v2.md, SEC_FINANCIAL_DATA.md, T1_POPULATION_AUDIT.md

---

## 1. Objective

Populate every field on every entity's financial_profile across all 3,071 entities in the knowledge graph. Four fiscal years per entity (FY2023, FY2024, FY2025, FY2026). Every FieldValue fully constructed with value, confidence_tier, and derivation. No nulls without explicit REFERENCE derivation explaining why. No field left empty. No templates. Every value produced through LLM reasoning grounded in entity context, graph relationships, and traceable source data.

---

## 2. Current State (Post-Cleanup)

As of commit `53992c3` (2026-04-08):

- 3,071 entities carry an empty financial_profile skeleton: `{currency: "USD", fx_rate: null, fx_rate_date: null, last_updated: null, updated_by: null, fiscal_years: {}}`
- No fiscal year data exists on any entity
- No residual non-standard keys remain
- Financial figures previously embedded in descriptions have been redacted
- The graph is clean and ready for population

---

## 3. Source Data Hierarchy

Population flows from high-confidence anchors downward. Every value at a lower level traces back to an anchor at a higher level.

### Layer 0 — SEC Consolidated (1 entity)

**Entity:** ou-029 (Rackspace Technology, Inc.)
**Source:** SEC_FINANCIAL_DATA.md (10-K filings, earnings releases)
**Confidence:** T1 for direct line items, T2 for derived/estimated values

This entity carries the consolidated income statement, balance sheet, and cash flow data. It is the ceiling that all allocations below must sum to. Every value populated here comes directly from SEC_FINANCIAL_DATA.md with source_document referencing the specific filing accession number.

**Available T1 data points (per SEC_FINANCIAL_DATA.md):**

| Field | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|
| recurring_revenue | $2,957M | $2,737M | $2,686M | — |
| cost_of_revenue | $2,328M | $2,204M | $2,179.3M | — |
| opex (SG&A) | ~$767M | $708M | $607.1M | — |
| capex | $181M | $136M | $139M | — |
| depreciation_amortization | $369.7M | $295.4M | ~$298.3M | — |
| fte_count | ~5,800 | ~5,100 | ~7,200 | — |
| balance_sheet.cash | $197M | $144M | $106M | — |
| balance_sheet.accounts_receivable | $339.7M | $298.8M | $266.5M | — |
| balance_sheet.fixed_assets (PP&E) | $608.8M | $601.0M | $596.3M | — |
| balance_sheet.debt | ~$2.7B | ~$2.7B | ~$2.7B | — |
| balance_sheet.equity | $(154.5M) | $(1,004.2M) | $(1,219.5M) | — |
| forecast_revenue (FY2026) | — | — | — | $2,650M (mid) |
| Non-GAAP OP | $157M | $106M | $126M | $160-170M |
| Adjusted EBITDA | — | ~$96M | $230M | $305-315M |
| OCF | $375M | $40M | $151M | — |
| FCF | ~$194M | $(71M) | $91M | — |

**Fields requiring LLM reasoning at L0:** interest_expense (derivable from debt load × blended rate), stock_based_compensation (back-derivable from Non-GAAP reconciliation), restructuring_charges (back-derivable from GAAP-to-Non-GAAP delta), impairment_charges (same), transaction_costs (same), tax_paid (derivable from OCF reconciliation), headcount_cost (derivable from FTE × industry benchmarks), deferred_revenue ($94.6M FY2025 from 10-K), accounts_payable ($413.9M FY2025 from 10-K), goodwill and intangible_assets (derivable from total assets minus identified components).

### Layer 1 — SEC Segments (4 entities)

**Entities:** pf-001 / ou-002 (Private Cloud), pf-002 / ou-001 (Public Cloud)
**Source:** SEC_FINANCIAL_DATA.md segment detail
**Confidence:** T1 for segment revenue, T2 for segment operating profit, T3 for allocated balance sheet items

T1 segment revenue is directly available. Segment operating profit available for FY2025 (PC $252.4M, PuC $67.6M). Segment depreciation available from 10-K Note 16. Cost of revenue derivable from revenue minus operating profit. All other fields allocated from L0 using revenue-weighting or headcount-weighting per FINANCIAL_PROFILE_SPEC_v2.md allocation rules.

**Allocation basis for L1:**
- Revenue-weighted: opex, balance_sheet items, capex
- Segment-specific: depreciation (from Note 16), operating profit
- Corporate bucket: costs not attributable to segments (captured as negative on ou-029's corporate unallocated line)

### Layer 2 — Sub-Portfolios and Business Units (~25 entities)

**Entities:** Product portfolios (pf-013 through pf-025, pf-033), OUs below segments
**Source:** OSINT-anchored estimates allocated from L1 parents
**Confidence:** T3-T4
**Method:** ALLOCATED from L1 parent using CUSTOM allocation_pct derived from OSINT signals (job postings, partner tier status, product descriptions, press releases)

### Layer 3 — Departments (250 entities)

**Entities:** dept-001 through dept-250
**Source:** Entity-level headcount and budget fields (anchors), parent OU relationship, department function classification (revenue-generating vs. cost center)
**Confidence:** T3-T4

This is the most complex layer. Each department requires individual reasoning based on:
- Its headcount and budget (top-level entity fields, available on all 250 departments)
- Its parent OU and that OU's financial profile (graph traversal)
- Whether it is a revenue-generating department or a cost center
- Its functional domain (engineering, sales, finance, HR, security, etc.)
- The Rackspace restructuring narrative arc (FY2023 stable → FY2024 restructuring → FY2025 stabilization → FY2026 AI growth)
- Connected roles, persons, systems, and capabilities (graph neighbors)

**Department classification rules:**
- **Revenue-generating:** Departments whose work directly produces billable services (e.g., Elastic Engineering, Professional Services, Cloud Optimization, managed services delivery). Carry recurring_revenue, bookings, backlog, contract_value, unit_economics, dso_days.
- **Cost centers:** Departments that support the business but do not directly bill (e.g., Finance, HR, Legal, Security, IT). Revenue fields set to null with REFERENCE derivation explaining cost center classification. Carry opex, headcount_cost, budget, compliance_costs.
- **Hybrid:** Departments with partial revenue attribution (e.g., Solutions Architecture does pre-sales solutioning that enables bookings but doesn't bill directly). Revenue fields use DERIVED method with formula referencing influenced pipeline.

### Layer 4 — All Other Entity Types (~2,821 entities)

Each entity type has a natural field subset. Fields outside that subset get null FieldValues with REFERENCE derivation.

| Entity Type | Count | Primary Financial Fields | Null With Reasoning |
|---|---|---|---|
| role | 430 | headcount_cost (loaded annual comp), fte_count (1.0), budget (role-level budget if applicable) | Revenue fields, balance_sheet, contract_detail, unit_economics |
| integration | 378 | fully_loaded_cost (TCO), opex (annual license/maintenance), capex (implementation) | Revenue fields, headcount, balance_sheet |
| control | 351 | compliance_costs (implementation + monitoring cost), opex (ongoing operational cost) | Revenue fields, headcount, balance_sheet, contract_detail |
| system | 164 | fully_loaded_cost (TCO), opex (license + support), capex (acquisition), depreciation_amortization | Revenue fields (unless revenue-generating system), headcount |
| data_asset | 164 | fully_loaded_cost (storage + governance), opex (ongoing cost) | Revenue, headcount, balance_sheet |
| person | 100 | headcount_cost (total comp), fte_count (1.0) | Revenue, balance_sheet, contract_detail |
| customer | 85 | recurring_revenue, contract_value, deferred_revenue, dso_days, bookings, unit_economics | Cost fields (captured on serving departments), headcount |
| product_portfolio | 69 | recurring_revenue, cost_of_revenue, opex, capex, depreciation_amortization, balance_sheet | Headcount (on departments), compliance_costs |
| business_capability | 67 | fully_loaded_cost (sum of enabling departments/systems), budget | Revenue (unless revenue capability), headcount (on departments) |
| vendor | 64 | contract_value, opex (annual spend), cost_of_revenue_detail | Revenue, headcount, balance_sheet |
| site | 58 | opex (facility operating cost), capex (improvements), balance_sheet.fixed_assets, depreciation_amortization | Revenue, headcount_cost, contract_detail |
| jurisdiction | 61 | compliance_costs (regulatory burden), opex (in-jurisdiction operating cost) | Revenue, headcount, balance_sheet |
| geography | 57 | recurring_revenue (geographic revenue attribution), opex, fte_count | balance_sheet (consolidated only), contract_detail |
| location | 46 | opex (facility cost), capex, balance_sheet.fixed_assets | Revenue, headcount_cost |
| contract | 40 | contract_value, contract_detail (all fields), deferred_revenue | Most P&L fields |
| product | 35 | recurring_revenue, cost_of_revenue, unit_economics, bookings | Headcount, balance_sheet |
| market_segment | 32 | recurring_revenue (segment revenue), bookings, unit_economics (segment-level) | Cost fields, headcount, balance_sheet |
| initiative | 25 | budget, spend_to_date, capex, forecast_cost | Revenue, balance_sheet, headcount |
| policy | 123 | compliance_costs (enforcement cost), opex (policy administration) | Revenue, headcount, balance_sheet |
| network | 94 | opex (network operating cost), capex (network infrastructure), fully_loaded_cost | Revenue, headcount, contract_detail |
| risk | 94 | compliance_costs (mitigation cost), opex (risk management cost) | Revenue, headcount, balance_sheet |
| data_domain | 90 | fully_loaded_cost (governance cost), opex | Revenue, headcount, balance_sheet |
| regulation | 70 | compliance_costs (compliance burden estimate) | Revenue, headcount, balance_sheet |
| incident | 9 | opex (incident response cost), compliance_costs (remediation + regulatory), fully_loaded_cost | Revenue, headcount |

---

## 4. FieldValue Construction Rules

### Rule 1: Every Field Gets a FieldValue

No field in the schema is skipped. If a field applies to the entity, it gets a populated FieldValue with a reasoned value. If a field does not apply, it gets:

```yaml
field_name:
  value: null
  confidence_tier: null
  derivation:
    method: REFERENCE
    source: "[Entity-specific explanation of why this field does not apply]"
    source_document: null
```

The source string in REFERENCE derivations must be unique to the entity. "Not applicable" is not acceptable. The string must name the entity, its type, and the specific reason. Examples:
- "Finance Department (dept-001) is a corporate G&A cost center under the CFO organization; it does not generate direct revenue"
- "Corporate Controller role (role-135) is an individual contributor position with no direct budget authority beyond expense approval limits"
- "Rackspace internal DNS infrastructure (net-012) is a shared service network segment with no revenue attribution; costs are allocated to IT Operations department"

### Rule 2: Derivation Chain Must Be Complete

Per FINANCIAL_PROFILE_SPEC_v2.md Validation Rule 3:
- Every ALLOCATED field must specify parent_field, allocation_pct, and allocation_basis
- The referenced parent_field on the graph-traversed parent must exist and have a non-null value
- Every DERIVED field must specify formula and input_fields
- Every HYBRID field must list components with individual confidence_tier and method

### Rule 3: Confidence Tier Follows Inheritance Rules

Per FINANCIAL_PROFILE_SPEC_v2.md:

| Parent Tier | Method | Child Tier |
|---|---|---|
| T1 | DIRECT | T1 |
| T1 | ALLOCATED | T3 |
| T1 | DERIVED | T2 |
| T2 | ALLOCATED | T3 |
| T3 | ALLOCATED | T4 |
| Any mix | HYBRID | Lowest tier among components |

### Rule 4: All Values Must Be Populated

This is the critical departure from the prior T1 population pass (which left most fields null). The requirement now: if a field applies to the entity, it must have a non-null value. If the value cannot be sourced from SEC filings or OSINT, it must be reasoned from:

1. **Entity context** — headcount, budget, description, functional domain
2. **Graph relationships** — parent OU financials, connected systems/vendors, role compensation bands
3. **Industry benchmarks** — cost ratios, compensation benchmarks, technology cost benchmarks
4. **Rackspace narrative arc** — the restructuring timeline drives FY-over-FY trajectories
5. **Due diligence analysis** — Stage 5 financial reality files provide analytical context on margin physics, liquidity constraints, pricing power, and structural limitations

The confidence_tier will be T3 or T4 for most of these reasoned values. That is acceptable. A T4 value with documented reasoning is infinitely more useful than a null field.

### Rule 5: FY-over-FY Trajectories Must Be Narratively Coherent

Each entity's four fiscal years tell a story consistent with Rackspace's documented trajectory:

- **FY2023 (AUDITED):** Baseline year. Stable operations pre-restructuring. Revenue $2,957M, ~5,800 FTE.
- **FY2024 (AUDITED):** Major restructuring. Revenue decline to $2,737M. Headcount cut to ~5,100 (-12%). Elevated restructuring charges, severance, and impairments. OCF collapsed to $40M. Debt refinanced March 2024.
- **FY2025 (PRELIMINARY):** Stabilization and recovery. Revenue $2,686M (slower decline). Headcount rebounded to ~7,200 (+41%, AI/cloud hiring). SG&A dropped to $607M. Adjusted EBITDA jumped to $230M. FCF recovered to $91M.
- **FY2026 (FORECAST):** AI-driven growth pivot. Private Cloud revenue grows for first time (+6%). Public Cloud declines on paper (-6%) due to government contract exit, but underlying services grow mid-to-high teens. EBITDA guidance $305-315M. Debt load ($2.7B) remains the defining constraint.

Every department, system, role, vendor, and other entity must reflect this arc at its own level. A Finance Department that shows flat headcount across all four years contradicts the restructuring narrative. An AI engineering department that doesn't show FY2025-2026 growth contradicts the pivot. The LLM must reason about each entity's position in this arc.

---

## 5. Execution Protocol

### 5.1 Method: Direct graph.json Edit

Population writes directly to graph.json using Python as a delivery mechanism. This avoids the token cost of MCP update_entity_tool responses (which exceeded 116K characters per entity in prior sessions). The MCP server auto-reloads from graph.json on mtime change.

Python constructs the financial_profile object with LLM-reasoned values and writes it to the entity's position in graph.json. The values come from LLM reasoning performed in the conversation context — Python is the delivery vehicle, not the reasoning engine.

### 5.2 Batch Size and Commit Cadence

- **Batch size:** Up to 10 entities per reasoning cycle
- **Commit cadence:** Every 10 entities, commit graph.json to git via Desktop Commander on the host machine
- **Commit message format:** `fin-pop: [entity type] [id range] — [count] entities, [field count] fields × 4 FYs`
- **Example:** `fin-pop: department dept-001 through dept-010 — 10 entities, 36 fields × 4 FYs`

### 5.3 Per-Entity Reasoning Process

For each entity:

1. **Fetch entity** via MCP `get_entity` — read id, type, name, description, headcount, budget, code, all available context fields
2. **Fetch neighbors** via MCP `get_neighbors` — understand parent OU, connected roles/persons/systems/vendors, hierarchy position
3. **Classify entity** — revenue-generating, cost center, or hybrid; determine which of the 36 fields apply vs. get REFERENCE nulls
4. **Identify parent financial context** — read the parent entity's financial_profile (already populated at a higher layer) to establish allocation ceilings
5. **Reason through each field × each FY:**
   - What is the value? How was it derived? What source or logic supports it?
   - How does FY2024 differ from FY2023 given restructuring? How does FY2025 differ given recovery? FY2026 given AI pivot?
   - Does this value make sense relative to the entity's headcount, budget, and functional domain?
   - Does this value roll up correctly to the parent?
6. **Construct the full financial_profile object** with all FieldValues
7. **Write to graph.json** via Python

### 5.4 Layer Execution Order

Execution follows the hierarchy strictly. You cannot populate a child before its parent, because child values derive from parent values.

| Phase | Layer | Entity Count | Dependencies |
|---|---|---|---|
| Phase 1 | L0: Consolidated (ou-029) | 1 | SEC_FINANCIAL_DATA.md only |
| Phase 2 | L1: Segments (pf-001, ou-002, pf-002, ou-001) | 4 | L0 populated |
| Phase 3 | L2: Sub-portfolios and BU sub-units | ~25 | L1 populated |
| Phase 4 | L3: Departments (dept-001 through dept-250) | 250 | L1/L2 populated (parent OUs) |
| Phase 5 | L4a: Revenue-facing entities (customers, products, market_segments, contracts) | ~192 | L1/L2 populated |
| Phase 6 | L4b: People entities (persons, roles) | ~530 | L3 populated (departments) |
| Phase 7 | L4c: Technology entities (systems, integrations, networks) | ~636 | L3 populated (owning departments) |
| Phase 8 | L4d: Governance entities (controls, policies, regulations, risks) | ~638 | L3 populated |
| Phase 9 | L4e: Location entities (sites, geographies, jurisdictions, locations) | ~222 | L0/L1 populated |
| Phase 10 | L4f: Remaining (data_assets, data_domains, business_capabilities, vendors, initiatives, incidents) | ~573 | Various parent layers |

Estimated total: 3,071 entities × ~10 minutes reasoning per entity = ~512 hours of LLM reasoning time. At 10 entities per session batch, this is ~307 batches across multiple sessions.

---

## 6. LLM Reasoning Enforcement Mechanisms

### Mechanism 1: Derivation Source Uniqueness Check

After each 10-entity commit, run a validation that checks derivation.source strings across the batch. No two entities of different types should have identical source strings. Source strings must reference the specific entity by name and context.

**Failure signal:** If `derivation.source` on dept-001's opex field is identical to dept-002's opex field, the reasoning was templated, not individualized.

### Mechanism 2: Entity Context Anchoring

Every entity's financial_profile must reference at least one of:
- The entity's own headcount or budget fields
- A specific graph neighbor (by name, not just ID)
- A specific fact from the entity's description
- A specific characteristic of its functional domain

This prevents "generic finance department" reasoning. The values must be anchored to THIS entity's actual context.

### Mechanism 3: Narrative Coherence Across FYs

For any field that changes across fiscal years, the derivation.source on FY2024, FY2025, and FY2026 must explain WHY it changed relative to the prior year. Generic "restructuring impact" is not sufficient. The explanation must be entity-specific:
- "Finance Department headcount reduced from 46 to 40 in FY2024 as junior AP/AR roles were automated via ERP workflow improvements during the restructuring cycle"
- NOT: "Reduced due to FY2024 restructuring"

### Mechanism 4: Roll-Up Spot Checks

After each phase completes, run arithmetic validation:
- Sum all child entity values for each field
- Compare to parent entity's value for that field
- Tolerance: 0.1% per FINANCIAL_PROFILE_SPEC_v2.md Validation Rule 1
- Document any variance as intercompany_adjustment on the parent

### Mechanism 5: updated_by Tagging

Every populated entity gets:
```yaml
financial_profile:
  last_updated: [ISO timestamp of population]
  updated_by: "llm_reasoning_v2"
```

Any entity with a different updated_by value after a population phase indicates it was missed or overwritten.

### Mechanism 6: Post-Batch Verification

After each 10-entity batch is committed, fetch one random entity from the batch via MCP `get_entity` and verify:
- fiscal_years contains FY2023, FY2024, FY2025, FY2026
- All 36 fields per FY are present (none missing from the schema)
- All FieldValues have non-null derivation.method
- All REFERENCE-method fields have entity-specific source strings
- updated_by = "llm_reasoning_v2"

---

## 7. Git Persistence Protocol

This is what failed in the prior session. MCP updates modified graph.json in memory, but the auto-sync system overwrote the file before changes were committed. The fix:

1. All writes go directly to graph.json on disk (not through MCP update_entity_tool)
2. After every 10 entities, commit via Desktop Commander on the host machine:
   ```
   cd ~/hc-cdaio-kg && git add graph.json && git commit -m "[commit message]"
   ```
3. Push to remote after each phase completes (not after each batch — pushes are heavier)
4. Before starting any new session, verify the last commit contains the expected data by checking a sample entity

**If the auto-sync system fires during a batch:** The commit after the batch will capture the current state. If auto-sync overwrites uncommitted in-progress edits, re-apply from the last committed state. Maximum data loss: 10 entities (one batch).

---

## 8. Reference Documents

| Document | Path | Purpose |
|---|---|---|
| Financial Profile Spec v2 | FINANCIAL_PROFILE_SPEC_v2.md | Schema definition, FieldValue structure, derivation methods, validation rules |
| SEC Financial Data | SEC_FINANCIAL_DATA.md | T1 anchor data for L0 and L1 population |
| T1 Population Audit | T1_POPULATION_AUDIT.md.bak | Prior audit trail — template for documentation approach |
| Structural Constraints Register | docs/deliverable-1-due-diligence/stage-5-financial-capital-stress/validation/5.structural_financial_constraints_register.json | Analytical context on margin physics, liquidity, debt structure |
| Financial Reality Truth Map | docs/deliverable-1-due-diligence/stage-5-financial-capital-stress/validation/5.financial_reality_truth_map.json | High-confidence facts vs. uncertainty zones |
| Financial Contradictions | docs/deliverable-1-due-diligence/stage-5-financial-capital-stress/5.6-financial-coherence-contradictions/5.6.financial_contradictions.json | Known contradictions in financial narrative |
| hc-enterprise-kg Skill | .claude/skills/hc-enterprise-kg/ | Entity model, relationship taxonomy, confidence tier system |

---

## 9. Success Criteria

Population is complete when:

1. All 3,071 entities have `updated_by: "llm_reasoning_v2"`
2. All 3,071 entities have fiscal_years containing FY2023, FY2024, FY2025, FY2026
3. Every fiscal year contains all fields defined in FINANCIAL_PROFILE_SPEC_v2.md (no missing keys)
4. Every FieldValue has a non-null derivation.method
5. Every REFERENCE derivation has an entity-specific source string (no generic "not applicable")
6. Every ALLOCATED derivation has parent_field, allocation_pct, and allocation_basis
7. Every DERIVED derivation has formula and input_fields
8. Roll-up validation passes: children sum to parent within 0.1% tolerance for all populated parent fields
9. All changes are committed to git and pushed to remote
10. No two entities of different types share identical derivation.source strings on the same field

---

## Change Log

| Date | Version | Change |
|---|---|---|
| 2026-04-08 | 1.0 | Initial plan. Covers full 3,071-entity population scope, 10-phase execution order, 6 enforcement mechanisms, persistence protocol, and success criteria. |

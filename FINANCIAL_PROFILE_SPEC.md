# Financial Profile Specification — hc-enterprise-kg

**Version:** 1.0
**Date:** 2026-04-03
**Status:** APPROVED DESIGN — Pending Implementation
**Author:** Thomas Jones / The Hipster CISO

---

## Design Principles

1. **One universal schema** across all 13 financial entity types. Same fields everywhere. Nulls where fields don't apply.
2. **No derived values stored.** Margins, percentages, ROI, variance, totals — all calculated at query time by the consuming agent.
3. **Confidence-tiered data.** T1 (SEC filings), T2 (multiple corroborating sources), T3 (single source), T4 (analytical judgment with documented rationale).
4. **Fiscal year keyed.** Historical capture across multiple fiscal years. Each FY entry carries its own confidence and period type.
5. **Parent-child rollups via graph relationships.** The KG relationship structure determines what sums to what. No rollup logic embedded in the schema.
6. **No new entity types.** Financial data lives on existing entities. The 13 non-financial entity types derive financial relevance through graph traversal.

---

## Entity Types That Carry financial_profile (13)

| Entity Type | Count | Primary Financial Concept |
|---|---|---|
| ProductPortfolio | 71 | Revenue, cost, margins |
| Product | 35 | Revenue, cost to deliver |
| OrganizationalUnit | 111 | P&L, cost structure |
| Department | 250 | Budget, headcount cost |
| Customer | 85 | Revenue, contract value |
| Vendor | 64 | Spend, contract value |
| BusinessCapability | 67 | Cost to operate |
| Initiative | 25 | Budget, spend, forecast |
| System | 164 | TCO, cost breakdown |
| Site | 58 | Operating cost |
| Contract | 40 | Contract value |
| MarketSegment | 32 | Segment revenue |
| DataAsset | 164 | Maintenance cost, value |

## Entity Types That Derive Financial Relevance via Relationships (13)

Person, Role, Policy, Control, Risk, Regulation, Geography, Jurisdiction, Location, Network, Integration, Data Domain, Incident

These entities have NO financial_profile. Their financial impact is computed at query time by traversing the graph to entities that do carry financial data.

---

## Schema Definition

```yaml
financial_profile:
  currency: "USD"
  fx_rate: null                        # Exchange rate to USD if local currency differs
  fx_rate_date: ""                     # Date of FX rate capture
  last_updated: ""                     # ISO timestamp of last value update
  updated_by: ""                       # User or system that last updated values

  fiscal_years:
    FY2024:

      # --- Period Classification ---
      period_type: ""                  # AUDITED | PRELIMINARY | ESTIMATED | FORECAST

      # --- What It Brings In ---
      recurring_revenue: null
      non_recurring_revenue: null
      revenue_recognition_method: ""   # UPFRONT | OVER_CONTRACT_LIFE | UPON_DELIVERY

      # --- What It Costs ---
      cost_of_revenue: null
      operating_expense: null
      capex: null
      depreciation_amortization: null
      headcount_cost: null
      budget: null
      spend_to_date: null
      run_rate: null
      run_rate_basis: ""               # ANNUALIZED_CURRENT_MONTH | ROLLING_12M | FORWARD_COMMITTED
      intercompany_adjustment: null
      fully_loaded_cost: null          # DEFERRED — populate after base values complete

      # --- How Many People ---
      fte_count: null
      contractor_count: null

      # --- What's Committed ---
      contract_value: null
      debt_obligations: null
      deferred_revenue: null

      # --- Cash Timing ---
      dso_days: null
      dpo_days: null

      # --- Where It's Headed ---
      forecast_revenue: null
      forecast_cost: null

      # --- How Confident Are We ---
      confidence_tier: "T4"            # T1 = SEC | T2 = Multiple Sources | T3 = Single Source | T4 = Analytical Judgment
      confidence_rationale: ""         # Required. Plain text explaining why this tier was assigned.
      allocation_method: ""            # How this number was derived (e.g., "proportional by headcount from parent OU")
      fully_loaded_cost_method: null   # DEFERRED

      # --- Consolidation ---
      consolidation_method: ""         # STANDALONE | CONSOLIDATED | EQUITY_METHOD
      consolidation_scope: ""          # ENTITY_ONLY | DIRECT_CHILDREN | ALL_DESCENDANTS

      # --- Confidence Propagation ---
      derived_confidence_tier: null    # Computed tier when rolling up mixed-confidence children

      # --- Balance Sheet (Grouped) ---
      balance_sheet:
        cash: null
        accounts_receivable: null
        ar_aging_0_30: null
        ar_aging_31_60: null
        ar_aging_61_90: null
        ar_aging_90_plus: null
        accounts_payable: null
        inventory: null
        fixed_assets: null
        debt: null
        equity: null

      # --- Contract Detail (Grouped) ---
      contract_detail:
        start_date: ""
        end_date: ""
        contract_currency: ""
        contract_type: ""              # RECURRING | ONE_TIME | HYBRID
        payment_schedule: ""           # UPFRONT_ANNUAL | QUARTERLY | MONTHLY | MILESTONE
        auto_renewal: null
        renewal_probability_pct: null

      # --- Unit Economics (Grouped) ---
      unit_economics:
        units: null
        revenue_per_unit: null
        cost_per_unit: null
        cac: null
        ltv: null
        monthly_churn_rate: null
        nrr_pct: null

      # --- Allocation Detail (Grouped) ---
      allocation_detail:
        basis: ""                      # HEADCOUNT | REVENUE | SQUARE_FOOTAGE | CUSTOM
        parent_entity_id: ""
        allocation_pct: null
        allocation_rationale: ""

      # --- Cost of Revenue Breakdown (Grouped) ---
      cost_of_revenue_detail:
        hardware: null
        cloud_infrastructure: null
        support_labor: null
        third_party_licenses: null
        other: null

      # --- Compliance Costs (Grouped) ---
      compliance_costs:
        tax_provision: null
        regulatory_cost: null
        audit_cost: null
        compliance_cost: null
```

---

## Derived Values — Calculated at Query Time, Never Stored

| Derived Value | Formula |
|---|---|
| total_revenue | recurring_revenue + non_recurring_revenue |
| gross_profit | total_revenue - cost_of_revenue |
| gross_margin_pct | gross_profit / total_revenue |
| operating_income | total_revenue - operating_expense |
| operating_margin_pct | operating_income / total_revenue |
| total_headcount | fte_count + contractor_count |
| budget_variance | spend_to_date - budget |
| roi | (total_revenue - total_cost) / total_cost |
| payback_period_months | total_cost / (total_revenue / 12) |
| risk_adjusted_value | financial_value × probability (from linked Risk entity) |
| cost_per_fte | headcount_cost / fte_count |
| contractor_concentration_pct | contractor_count / total_headcount |

---

## Confidence Tier Definitions

| Tier | Source | Example |
|---|---|---|
| T1 | SEC filings, audited financials | 10-K revenue, gross profit |
| T2 | Multiple corroborating sources | Analyst consensus + job postings + press releases |
| T3 | Single source | One analyst estimate, one benchmark report |
| T4 | Analytical judgment | Industry median comp × headcount, proportional allocation |

### Confidence Propagation Rule

When rolling up values from children with mixed confidence tiers, the resulting confidence tier equals the **lowest confidence tier among the contributing values**. A sum of T1 + T3 + T4 values produces a T4 result.

---

## Consolidation Rules

- **STANDALONE**: Entity's own values only. No children included.
- **CONSOLIDATED**: Entity values + all children, with intercompany_adjustment applied to eliminate double-counting.
- **EQUITY_METHOD**: Entity shows proportional share of subsidiary values.

When querying rollups, the consuming agent must check consolidation_method and consolidation_scope to determine traversal behavior.

---

## Population Order (Top-Down Waterfall)

1. **T1 entities first.** SEC-reportable segments (pf-001, pf-002) and corporate-level OUs (ou-001, ou-002). Values come directly from SEC filings.
2. **T2 children of T1.** Sub-portfolios and products with multiple corroborating sources.
3. **T3 entities.** Single-source estimates.
4. **T4 entities.** Analytical judgment — industry benchmarks, proportional allocation, documented rationale.
5. **Verify at each level.** Children must sum to parent. If they don't, investigate and adjust before moving down.
6. **fully_loaded_cost last.** Populated only after all base values are verified across the tree.

---

## What This Spec Does NOT Cover

- Pydantic model implementation (separate engineering task)
- Migration strategy for existing KG data (separate planning task)
- Specific entity values (separate population task)
- Validation rules and automated sanity checks (deferred to implementation)

---

## Change Log

| Date | Version | Change |
|---|---|---|
| 2026-04-03 | 1.0 | Initial specification. Universal schema with 25 core fields + 6 grouped containers. |

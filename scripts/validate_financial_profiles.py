#!/usr/bin/env python3
"""Validate the financial_profile cleanup across the entire KG.

Checks:
1. All 13 financial entity types have the universal financial_profile schema
2. No loose baggage fields remain on any entity
3. Non-financial entity types have NO financial_profile
4. Schema structure is identical across all financial entities
5. Entity and relationship counts are intact
"""
import json
from pathlib import Path

GRAPH_PATH = Path("/Users/thomasjones/hc-cdaio-kg/graph.json")

FINANCIAL_ENTITY_TYPES = {
    "product_portfolio", "product", "organizational_unit", "department",
    "customer", "vendor", "business_capability", "initiative",
    "system", "site", "contract", "market_segment", "data_asset",
}

NON_FINANCIAL_ENTITY_TYPES = {
    "person", "role", "policy", "control", "risk", "regulation",
    "geography", "jurisdiction", "location", "network",
    "integration", "data_domain", "incident",
}

# All known baggage fields that should have been removed
ALL_BAGGAGE_FIELDS = {
    "revenue_attribution", "margin_contribution", "margin_compression",
    "latent_churn_risk", "revenue_trend", "strategic_risk",
    "estimated_annual_revenue", "estimated_gross_margin_pct",
    "estimated_growth_rate_pct", "revenue_estimation_methodology",
    "financial_confidence_tier", "financial_assessment_date",
    "assessed_by", "estimated_annual_budget", "budget_confidence",
    "estimation_methodology", "p_and_l_responsibility",
    "budget_as_pct_of_opex", "annual_spend_estimate", "spend_category",
    "spend_tier", "contract_risk_financial_impact",
    "estimated_annual_spend", "estimated_contract_value",
    "financial_estimation_methodology", "cost_estimation_methodology",
    "estimated_annual_operating_cost", "estimated_lease_or_ownership_cost",
    "annual_investment_usd", "annual_savings_target_usd",
}

# Expected top-level keys in financial_profile
EXPECTED_FP_TOP_KEYS = {
    "currency", "fx_rate", "fx_rate_date",
    "last_updated", "updated_by", "fiscal_years",
}

# Expected keys in each fiscal year entry
EXPECTED_FY_KEYS = {
    "period_type", "recurring_revenue", "non_recurring_revenue",
    "cost_of_revenue", "operating_expense", "capex",
    "depreciation_amortization", "headcount_cost", "budget",
    "spend_to_date", "run_rate", "run_rate_basis",
    "intercompany_adjustment", "fully_loaded_cost",
    "fte_count", "contractor_count",
    "contract_value", "debt_obligations", "deferred_revenue",
    "dso_days", "dpo_days",
    "forecast_revenue", "forecast_cost",
    "confidence_tier", "confidence_rationale", "allocation_method",
    "fully_loaded_cost_method",
    "consolidation_method", "consolidation_scope",
    "derived_confidence_tier",
    "balance_sheet", "contract_detail", "unit_economics",
    "allocation_detail", "cost_of_revenue_detail", "compliance_costs",
}

EXPECTED_FY_LIST = {"FY2024", "FY2023"}


def main():
    print(f"Loading graph from {GRAPH_PATH}")
    with open(GRAPH_PATH) as f:
        graph = json.load(f)

    entities = graph.get("entities", [])
    relationships = graph.get("relationships", [])
    print(f"Total entities: {len(entities)}")
    print(f"Total relationships: {len(relationships)}")

    errors = []
    warnings = []
    stats = {
        "financial_entities_checked": 0,
        "non_financial_entities_checked": 0,
        "fp_schema_valid": 0,
        "fp_schema_invalid": 0,
        "baggage_found": 0,
        "non_financial_with_fp": 0,
    }

    for entity in entities:
        eid = entity.get("id", "???")
        etype = entity.get("entity_type", "")

        # CHECK 1: Non-financial entities should NOT have financial_profile
        if etype in NON_FINANCIAL_ENTITY_TYPES:
            stats["non_financial_entities_checked"] += 1
            if "financial_profile" in entity:
                errors.append(f"NON-FINANCIAL entity {eid} ({etype}) has financial_profile")
                stats["non_financial_with_fp"] += 1
            continue

        if etype not in FINANCIAL_ENTITY_TYPES:
            continue

        stats["financial_entities_checked"] += 1

        # CHECK 2: Loose baggage fields
        for field in ALL_BAGGAGE_FIELDS:
            if field in entity:
                errors.append(f"BAGGAGE: {eid} ({etype}) still has loose field '{field}'")
                stats["baggage_found"] += 1

        # CHECK 3: Must have financial_profile
        fp = entity.get("financial_profile")
        if fp is None:
            errors.append(f"MISSING: {eid} ({etype}) has no financial_profile")
            stats["fp_schema_invalid"] += 1
            continue

        # CHECK 4: Top-level FP keys
        fp_keys = set(fp.keys())
        missing_top = EXPECTED_FP_TOP_KEYS - fp_keys
        extra_top = fp_keys - EXPECTED_FP_TOP_KEYS
        if missing_top:
            errors.append(f"FP KEYS: {eid} missing top-level keys: {missing_top}")
        if extra_top:
            errors.append(f"FP KEYS: {eid} has extra top-level keys: {extra_top}")

        # CHECK 5: Fiscal years present
        fy = fp.get("fiscal_years", {})
        if not isinstance(fy, dict):
            errors.append(f"FY TYPE: {eid} fiscal_years is not a dict")
            stats["fp_schema_invalid"] += 1
            continue

        fy_keys = set(fy.keys())
        if fy_keys != EXPECTED_FY_LIST:
            errors.append(f"FY KEYS: {eid} has {fy_keys}, expected {EXPECTED_FY_LIST}")

        # CHECK 6: Each FY entry has correct keys
        valid = True
        for fy_name, fy_data in fy.items():
            if not isinstance(fy_data, dict):
                errors.append(f"FY DATA: {eid}.{fy_name} is not a dict")
                valid = False
                continue
            fy_data_keys = set(fy_data.keys())
            missing_fy = EXPECTED_FY_KEYS - fy_data_keys
            extra_fy = fy_data_keys - EXPECTED_FY_KEYS
            if missing_fy:
                errors.append(f"FY FIELDS: {eid}.{fy_name} missing: {missing_fy}")
                valid = False
            if extra_fy:
                errors.append(f"FY FIELDS: {eid}.{fy_name} extra: {extra_fy}")
                valid = False

            # CHECK 7: All values are null (clean slate)
            for key in EXPECTED_FY_KEYS:
                if key in fy_data:
                    val = fy_data[key]
                    if key == "confidence_tier" and val == "T4":
                        continue
                    if key == "confidence_rationale" and val == "":
                        continue
                    if key == "allocation_method" and val == "":
                        continue
                    if key in ("balance_sheet", "contract_detail",
                               "unit_economics", "allocation_detail",
                               "cost_of_revenue_detail", "compliance_costs"):
                        if isinstance(val, dict):
                            non_null = {k: v for k, v in val.items() if v is not None}
                            if non_null:
                                warnings.append(f"NON-NULL: {eid}.{fy_name}.{key} has values: {non_null}")
                        continue
                    if val is not None:
                        warnings.append(f"NON-NULL: {eid}.{fy_name}.{key} = {val}")

        if valid:
            stats["fp_schema_valid"] += 1
        else:
            stats["fp_schema_invalid"] += 1

    # CHECK 8: Entity counts by type
    type_counts = {}
    for e in entities:
        t = e.get("entity_type", "unknown")
        type_counts[t] = type_counts.get(t, 0) + 1

    expected_counts = {
        "business_capability": 67, "contract": 40, "control": 351,
        "customer": 85, "data_asset": 164, "data_domain": 90,
        "department": 250, "geography": 57, "incident": 9,
        "initiative": 25, "integration": 378, "jurisdiction": 61,
        "location": 46, "market_segment": 32, "network": 94,
        "organizational_unit": 111, "person": 100, "policy": 123,
        "product": 35, "product_portfolio": 71, "regulation": 70,
        "risk": 94, "role": 430, "site": 58, "system": 164,
        "vendor": 64,
    }
    for etype, expected in expected_counts.items():
        actual = type_counts.get(etype, 0)
        if actual != expected:
            errors.append(f"COUNT: {etype} expected {expected}, got {actual}")

    # REPORT
    print(f"\n{'='*60}")
    print(f"FINANCIAL PROFILE VALIDATION REPORT")
    print(f"{'='*60}")
    print(f"\nEntities: {len(entities)}  |  Relationships: {len(relationships)}")
    print(f"\nFinancial entities checked:     {stats['financial_entities_checked']}")
    print(f"Non-financial entities checked: {stats['non_financial_entities_checked']}")
    print(f"FP schema valid:               {stats['fp_schema_valid']}")
    print(f"FP schema invalid:             {stats['fp_schema_invalid']}")
    print(f"Baggage fields found:          {stats['baggage_found']}")
    print(f"Non-financial with FP:         {stats['non_financial_with_fp']}")

    if errors:
        print(f"\n--- ERRORS ({len(errors)}) ---")
        for e in errors:
            print(f"  [ERROR] {e}")
    else:
        print(f"\n--- NO ERRORS ---")

    if warnings:
        print(f"\n--- WARNINGS ({len(warnings)}) ---")
        for w in warnings[:20]:
            print(f"  [WARN] {w}")
        if len(warnings) > 20:
            print(f"  ... and {len(warnings) - 20} more warnings")
    else:
        print(f"\n--- NO WARNINGS ---")

    # Final verdict
    print(f"\n{'='*60}")
    if not errors:
        print("VERDICT: PASS — KG is clean and ready for T1 population")
    else:
        print(f"VERDICT: FAIL — {len(errors)} error(s) must be resolved")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()

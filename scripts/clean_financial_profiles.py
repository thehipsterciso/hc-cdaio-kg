#!/usr/bin/env python3
"""Clean all financial_profile variations and loose financial baggage fields.

Replaces every financial_profile on the 13 financial entity types with the
new universal schema (all nulls). Removes loose financial fields that were
scattered by the enrichment pipeline.

Creates a backup at graph.json.pre-financial-clean before modifying.
"""
import json
import shutil
from pathlib import Path
from datetime import datetime

GRAPH_PATH = Path("/Users/thomasjones/hc-cdaio-kg/graph.json")
BACKUP_PATH = GRAPH_PATH.with_suffix(".pre-financial-clean")

# The 13 entity types that carry financial_profile
FINANCIAL_ENTITY_TYPES = {
    "product_portfolio", "product", "organizational_unit", "department",
    "customer", "vendor", "business_capability", "initiative",
    "system", "site", "contract", "market_segment", "data_asset",
}

# Loose financial baggage fields to REMOVE (by entity type)
# These are top-level fields added by the enrichment pipeline
BAGGAGE_FIELDS_BY_TYPE = {
    "product_portfolio": {
        "revenue_attribution", "margin_contribution", "margin_compression",
        "latent_churn_risk", "revenue_trend", "strategic_risk",
    },
    "product": {
        "estimated_annual_revenue", "estimated_gross_margin_pct",
        "estimated_growth_rate_pct", "revenue_estimation_methodology",
        "financial_confidence_tier", "financial_assessment_date",
        "assessed_by",
    },
    "organizational_unit": {
        "estimated_annual_budget", "budget_confidence",
        "estimation_methodology", "p_and_l_responsibility",
    },
    "department": {
        "budget_as_pct_of_opex",
    },
    "vendor": {
        "annual_spend_estimate", "spend_category", "spend_tier",
        "contract_risk_financial_impact", "estimated_annual_spend",
        "estimated_contract_value", "financial_estimation_methodology",
        "financial_confidence_tier", "financial_assessment_date",
        "assessed_by",
    },
    "site": {
        "estimated_annual_operating_cost", "estimated_lease_or_ownership_cost",
        "cost_estimation_methodology", "financial_confidence_tier",
        "financial_assessment_date", "assessed_by",
    },
    "initiative": {
        "annual_investment_usd", "annual_savings_target_usd",
    },
    "system": {
        "financial_confidence_tier", "financial_assessment_date",
        "assessed_by",
    },
    "customer": {
        "financial_confidence_tier", "financial_assessment_date",
        "assessed_by",
    },
    "business_capability": set(),
    "contract": set(),
    "market_segment": set(),
    "data_asset": set(),
}

# Universal fields to check and remove from ALL financial entity types
UNIVERSAL_BAGGAGE = {
    "financial_confidence_tier", "financial_assessment_date",
    "assessed_by", "estimation_methodology", "cost_estimation_methodology",
    "financial_estimation_methodology", "revenue_estimation_methodology",
}

def new_fiscal_year_template():
    """Return the universal fiscal year entry with all nulls."""
    return {
        "period_type": None,
        "recurring_revenue": None,
        "non_recurring_revenue": None,
        "cost_of_revenue": None,
        "operating_expense": None,
        "capex": None,
        "depreciation_amortization": None,
        "headcount_cost": None,
        "budget": None,
        "spend_to_date": None,
        "run_rate": None,
        "run_rate_basis": None,
        "intercompany_adjustment": None,
        "fully_loaded_cost": None,
        "fte_count": None,
        "contractor_count": None,
        "contract_value": None,
        "debt_obligations": None,
        "deferred_revenue": None,
        "dso_days": None,
        "dpo_days": None,
        "forecast_revenue": None,
        "forecast_cost": None,
        "confidence_tier": "T4",
        "confidence_rationale": "",
        "allocation_method": "",
        "fully_loaded_cost_method": None,
        "consolidation_method": None,
        "consolidation_scope": None,
        "derived_confidence_tier": None,
        "balance_sheet": {
            "cash": None,
            "accounts_receivable": None,
            "ar_aging_0_30": None,
            "ar_aging_31_60": None,
            "ar_aging_61_90": None,
            "ar_aging_90_plus": None,
            "accounts_payable": None,
            "inventory": None,
            "fixed_assets": None,
            "debt": None,
            "equity": None,
        },
        "contract_detail": {
            "start_date": None,
            "end_date": None,
            "contract_currency": None,
            "contract_type": None,
            "payment_schedule": None,
            "auto_renewal": None,
            "renewal_probability_pct": None,
        },
        "unit_economics": {
            "units": None,
            "revenue_per_unit": None,
            "cost_per_unit": None,
            "cac": None,
            "ltv": None,
            "monthly_churn_rate": None,
            "nrr_pct": None,
        },
        "allocation_detail": {
            "basis": None,
            "parent_entity_id": None,
            "allocation_pct": None,
            "allocation_rationale": None,
        },
        "cost_of_revenue_detail": {
            "hardware": None,
            "cloud_infrastructure": None,
            "support_labor": None,
            "third_party_licenses": None,
            "other": None,
        },
        "compliance_costs": {
            "tax_provision": None,
            "regulatory_cost": None,
            "audit_cost": None,
            "compliance_cost": None,
        },
    }

def new_financial_profile():
    """Return the universal financial_profile with FY2024 and FY2023."""
    return {
        "currency": "USD",
        "fx_rate": None,
        "fx_rate_date": None,
        "last_updated": datetime.now().isoformat(),
        "updated_by": "financial_profile_clean_v1",
        "fiscal_years": {
            "FY2024": new_fiscal_year_template(),
            "FY2023": new_fiscal_year_template(),
        },
    }


def clean_entity(entity: dict) -> tuple[int, int]:
    """Clean one entity. Returns (baggage_fields_removed, had_old_fp)."""
    etype = entity.get("entity_type", "")
    if etype not in FINANCIAL_ENTITY_TYPES:
        return 0, 0

    removed = 0

    # Remove type-specific baggage fields
    type_baggage = BAGGAGE_FIELDS_BY_TYPE.get(etype, set())
    all_baggage = type_baggage | UNIVERSAL_BAGGAGE
    for field in list(all_baggage):
        if field in entity:
            del entity[field]
            removed += 1

    # Replace financial_profile with new universal schema
    had_old = "financial_profile" in entity
    entity["financial_profile"] = new_financial_profile()

    return removed, int(had_old)


def main():
    print(f"Loading graph from {GRAPH_PATH}")
    with open(GRAPH_PATH) as f:
        graph = json.load(f)

    # Create backup
    print(f"Creating backup at {BACKUP_PATH}")
    shutil.copy2(GRAPH_PATH, BACKUP_PATH)

    entities = graph.get("entities", [])
    print(f"Total entities: {len(entities)}")

    total_cleaned = 0
    total_baggage_removed = 0
    total_old_fp_replaced = 0
    by_type = {}

    for entity in entities:
        etype = entity.get("entity_type", "")
        if etype not in FINANCIAL_ENTITY_TYPES:
            continue

        baggage, had_old = clean_entity(entity)
        total_cleaned += 1
        total_baggage_removed += baggage
        total_old_fp_replaced += had_old

        if etype not in by_type:
            by_type[etype] = {"count": 0, "baggage": 0, "old_fp": 0}
        by_type[etype]["count"] += 1
        by_type[etype]["baggage"] += baggage
        by_type[etype]["old_fp"] += had_old

    # Save cleaned graph
    print(f"\nSaving cleaned graph to {GRAPH_PATH}")
    with open(GRAPH_PATH, "w") as f:
        json.dump(graph, f, indent=2)

    # Report
    print(f"\n{'='*60}")
    print(f"FINANCIAL PROFILE CLEANUP REPORT")
    print(f"{'='*60}")
    print(f"Entities cleaned:        {total_cleaned}")
    print(f"Baggage fields removed:  {total_baggage_removed}")
    print(f"Old FPs replaced:        {total_old_fp_replaced}")
    print(f"\nBreakdown by type:")
    for etype, stats in sorted(by_type.items()):
        print(f"  {etype:25s}  cleaned={stats['count']:4d}  "
              f"baggage={stats['baggage']:3d}  old_fp={stats['old_fp']:3d}")
    print(f"\nBackup saved to: {BACKUP_PATH}")
    print("Done.")


if __name__ == "__main__":
    main()

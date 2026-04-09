"""
Financial Profile v2 schema construction.

Single source of truth for the empty financial_profile skeleton. Every entity
in the graph must conform to this shape before population begins. Every batch
payload must fill every field defined here.

The schema matches FINANCIAL_PROFILE_SPEC_v2.md. If the spec changes, this
module is the canonical update point.
"""

from __future__ import annotations

from typing import Any

# ─── Fiscal years always populated ────────────────────────────────────────────
FISCAL_YEARS = ["FY2023", "FY2024", "FY2025", "FY2026"]

# ─── Scalar FieldValue fields at the root of each fiscal_year ──────────────
SCALAR_FIELDS = [
    # Revenue
    "recurring_revenue",
    "non_recurring_revenue",
    # Cost
    "cost_of_revenue",
    "opex",
    "capex",
    "depreciation_amortization",
    "interest_expense",
    "stock_based_compensation",
    "restructuring_charges",
    "impairment_charges",
    "transaction_costs",
    "tax_paid",
    "headcount_cost",
    "budget",
    "spend_to_date",
    "run_rate",
    "intercompany_adjustment",
    "fully_loaded_cost",
    # People
    "fte_count",
    "contractor_count",
    # Commitments
    "contract_value",
    "debt_obligations",
    "deferred_revenue",
    # Cash timing
    "dso_days",
    "dpo_days",
    # Leading indicators
    "bookings",
    "backlog",
    # Forward
    "forecast_revenue",
    "forecast_cost",
]

# ─── Grouped containers ──────────────────────────────────────────────────────
BALANCE_SHEET_FIELDS = [
    "cash",
    "accounts_receivable",
    "ar_aging_0_30",
    "ar_aging_31_60",
    "ar_aging_61_90",
    "ar_aging_90_plus",
    "accounts_payable",
    "inventory",
    "fixed_assets",
    "goodwill",
    "intangible_assets",
    "debt",
    "equity",
]

UNIT_ECONOMICS_FIELDS = [
    "units",
    "revenue_per_unit",
    "cost_per_unit",
    "cac",
    "ltv",
    "monthly_churn_rate",
    "nrr_pct",
]

COST_OF_REVENUE_DETAIL_FIELDS = [
    "hardware",
    "cloud_infrastructure",
    "support_labor",
    "third_party_licenses",
    "other",
]

COMPLIANCE_COSTS_FIELDS = [
    "tax_provision",
    "regulatory_cost",
    "audit_cost",
    "compliance_cost",
]

# ─── Non-FieldValue literals kept on the fiscal_year object ──────────────────
# contract_detail is a dict of literal values (dates, booleans, strings), not
# FieldValue-wrapped. Kept separate.
CONTRACT_DETAIL_FIELDS = [
    "start_date",
    "end_date",
    "contract_currency",
    "contract_type",
    "payment_schedule",
    "auto_renewal",
    "renewal_probability_pct",
]


def empty_field_value() -> dict[str, Any]:
    """A FieldValue with no data — used for skeleton construction."""
    return {
        "value": None,
        "confidence_tier": None,
        "derivation": {
            "method": None,
            "source": None,
            "source_document": None,
            "parent_field": None,
            "allocation_pct": None,
            "allocation_basis": None,
            "formula": None,
            "input_fields": None,
            "components": None,
        },
    }


def empty_contract_detail() -> dict[str, Any]:
    return {k: None for k in CONTRACT_DETAIL_FIELDS}


def empty_fiscal_year() -> dict[str, Any]:
    fy: dict[str, Any] = {
        "period_type": None,
        "run_rate_basis": None,
        "confidence_tier": None,
        "confidence_rationale": None,
        "allocation_method": None,
        "fully_loaded_cost_method": None,
        "consolidation_method": None,
        "consolidation_scope": None,
        "derived_confidence_tier": None,
    }
    for f in SCALAR_FIELDS:
        fy[f] = empty_field_value()
    fy["balance_sheet"] = {f: empty_field_value() for f in BALANCE_SHEET_FIELDS}
    fy["contract_detail"] = empty_contract_detail()
    fy["unit_economics"] = {f: empty_field_value() for f in UNIT_ECONOMICS_FIELDS}
    fy["cost_of_revenue_detail"] = {
        f: empty_field_value() for f in COST_OF_REVENUE_DETAIL_FIELDS
    }
    fy["compliance_costs"] = {f: empty_field_value() for f in COMPLIANCE_COSTS_FIELDS}
    fy["allocation_detail"] = {
        "basis": None,
        "parent_entity_id": None,
        "allocation_pct": None,
        "allocation_rationale": None,
    }
    return fy


def empty_financial_profile() -> dict[str, Any]:
    return {
        "currency": "USD",
        "fx_rate": None,
        "fx_rate_date": None,
        "last_updated": None,
        "updated_by": None,
        "hierarchy": {
            "level": None,
            "consolidation_method": None,
            "consolidation_scope": None,
        },
        "fiscal_years": {fy: empty_fiscal_year() for fy in FISCAL_YEARS},
    }


# ─── Field enumeration for validators ────────────────────────────────────────
def all_field_paths() -> list[str]:
    """All FieldValue paths inside a fiscal_year. Used for completeness checks."""
    paths: list[str] = list(SCALAR_FIELDS)
    paths += [f"balance_sheet.{f}" for f in BALANCE_SHEET_FIELDS]
    paths += [f"unit_economics.{f}" for f in UNIT_ECONOMICS_FIELDS]
    paths += [f"cost_of_revenue_detail.{f}" for f in COST_OF_REVENUE_DETAIL_FIELDS]
    paths += [f"compliance_costs.{f}" for f in COMPLIANCE_COSTS_FIELDS]
    return paths


def total_field_count_per_fy() -> int:
    return len(all_field_paths())

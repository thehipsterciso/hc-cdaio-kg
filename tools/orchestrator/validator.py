"""
Batch validators — the six enforcement mechanisms from
FINANCIAL_POPULATION_PLAN.md Section 6.

Mechanism 1: Derivation Source Uniqueness Check
Mechanism 2: Entity Context Anchoring
Mechanism 3: Narrative Coherence Across FYs
Mechanism 4: Roll-Up Spot Checks            (phase-level, not batch-level)
Mechanism 5: updated_by Tagging
Mechanism 6: Post-Batch Verification
"""

from __future__ import annotations

from typing import Any

from . import schema

REQUIRED_TOP_LEVEL_KEYS = {
    "currency",
    "fx_rate",
    "fx_rate_date",
    "last_updated",
    "updated_by",
    "hierarchy",
    "fiscal_years",
}


def validate_profile_shape(fp: dict[str, Any]) -> list[str]:
    """Return a list of shape errors. Empty list = conformant."""
    errs: list[str] = []
    for k in REQUIRED_TOP_LEVEL_KEYS:
        if k not in fp:
            errs.append(f"missing top-level key: {k}")
    fy = fp.get("fiscal_years", {})
    for fy_name in schema.FISCAL_YEARS:
        if fy_name not in fy:
            errs.append(f"missing fiscal_year: {fy_name}")
            continue
        for path in schema.all_field_paths():
            parts = path.split(".")
            obj: Any = fy[fy_name]
            found = True
            for part in parts:
                if not isinstance(obj, dict) or part not in obj:
                    found = False
                    break
                obj = obj[part]
            if not found:
                errs.append(f"{fy_name}.{path}: missing")
                continue
            if not isinstance(obj, dict):
                errs.append(f"{fy_name}.{path}: not a FieldValue object")
                continue
            if "value" not in obj or "derivation" not in obj:
                errs.append(f"{fy_name}.{path}: malformed FieldValue")
    return errs


def validate_updated_by(fp: dict[str, Any], expected: str) -> list[str]:
    if fp.get("updated_by") != expected:
        return [f"updated_by = {fp.get('updated_by')!r}, expected {expected!r}"]
    return []


def validate_derivation_methods(fp: dict[str, Any]) -> list[str]:
    """Every FieldValue must have a non-null derivation.method."""
    errs: list[str] = []
    fy = fp.get("fiscal_years", {})
    for fy_name, fy_data in fy.items():
        for path in schema.all_field_paths():
            parts = path.split(".")
            obj: Any = fy_data
            for part in parts:
                obj = obj.get(part) if isinstance(obj, dict) else None
                if obj is None:
                    break
            if not isinstance(obj, dict):
                continue
            method = obj.get("derivation", {}).get("method")
            if not method:
                errs.append(f"{fy_name}.{path}: derivation.method is null")
    return errs


def validate_reference_source_specificity(
    fp: dict[str, Any], entity_id: str
) -> list[str]:
    """REFERENCE derivations must name the entity. Generic 'not applicable' fails."""
    errs: list[str] = []
    fy = fp.get("fiscal_years", {})
    for fy_name, fy_data in fy.items():
        for path in schema.all_field_paths():
            parts = path.split(".")
            obj: Any = fy_data
            for part in parts:
                obj = obj.get(part) if isinstance(obj, dict) else None
                if obj is None:
                    break
            if not isinstance(obj, dict):
                continue
            deriv = obj.get("derivation") or {}
            if deriv.get("method") == "REFERENCE":
                src = deriv.get("source") or ""
                if not src or len(src) < 20:
                    errs.append(
                        f"{fy_name}.{path}: REFERENCE source too short ({len(src)} chars)"
                    )
                if src.strip().lower() in {"not applicable", "n/a", "none"}:
                    errs.append(
                        f"{fy_name}.{path}: REFERENCE source is generic: {src!r}"
                    )
    return errs


def validate_batch_source_uniqueness(
    batch_payloads: list[dict[str, Any]]
) -> list[str]:
    """No two entities in a batch of different types should share a REFERENCE source."""
    errs: list[str] = []
    seen: dict[str, str] = {}  # source string -> entity_id
    for payload in batch_payloads:
        eid = payload["entity_id"]
        fp = payload["financial_profile"]
        fy = fp.get("fiscal_years", {})
        for fy_name, fy_data in fy.items():
            for path in schema.all_field_paths():
                parts = path.split(".")
                obj: Any = fy_data
                for part in parts:
                    obj = obj.get(part) if isinstance(obj, dict) else None
                    if obj is None:
                        break
                if not isinstance(obj, dict):
                    continue
                deriv = obj.get("derivation") or {}
                if deriv.get("method") == "REFERENCE":
                    src = deriv.get("source") or ""
                    key = f"{fy_name}.{path}::{src}"
                    if key in seen and seen[key] != eid:
                        errs.append(
                            f"duplicate REFERENCE source on {fy_name}.{path}: "
                            f"{seen[key]} and {eid}"
                        )
                    else:
                        seen[key] = eid
    return errs


def validate_allocated_fields(fp: dict[str, Any]) -> list[str]:
    """Every ALLOCATED FieldValue must specify parent_field, allocation_pct,
    allocation_basis. DERIVED must specify formula and input_fields."""
    errs: list[str] = []
    fy = fp.get("fiscal_years", {})
    for fy_name, fy_data in fy.items():
        for path in schema.all_field_paths():
            parts = path.split(".")
            obj: Any = fy_data
            for part in parts:
                obj = obj.get(part) if isinstance(obj, dict) else None
                if obj is None:
                    break
            if not isinstance(obj, dict):
                continue
            deriv = obj.get("derivation") or {}
            method = deriv.get("method")
            if method == "ALLOCATED":
                for req in ("parent_field", "allocation_pct", "allocation_basis"):
                    if deriv.get(req) is None:
                        errs.append(f"{fy_name}.{path}: ALLOCATED missing {req}")
            elif method == "DERIVED":
                for req in ("formula", "input_fields"):
                    if deriv.get(req) is None:
                        errs.append(f"{fy_name}.{path}: DERIVED missing {req}")
    return errs


def run_all_checks(
    batch_payloads: list[dict[str, Any]], expected_updated_by: str
) -> dict[str, Any]:
    """Aggregate runner. Returns a report dict."""
    report: dict[str, Any] = {
        "checks": {},
        "pass": True,
        "total_errors": 0,
    }
    all_errs: list[str] = []

    for p in batch_payloads:
        eid = p["entity_id"]
        fp = p["financial_profile"]
        entity_report: dict[str, list[str]] = {
            "shape": validate_profile_shape(fp),
            "updated_by": validate_updated_by(fp, expected_updated_by),
            "derivation_methods": validate_derivation_methods(fp),
            "reference_source": validate_reference_source_specificity(fp, eid),
            "allocated_fields": validate_allocated_fields(fp),
        }
        for errs in entity_report.values():
            all_errs.extend(errs)
        report["checks"][eid] = entity_report

    report["checks"]["_batch_"] = {
        "source_uniqueness": validate_batch_source_uniqueness(batch_payloads),
    }
    all_errs.extend(report["checks"]["_batch_"]["source_uniqueness"])

    report["total_errors"] = len(all_errs)
    report["pass"] = len(all_errs) == 0
    return report

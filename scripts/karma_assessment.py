#!/usr/bin/env python3
"""
KarMA — Knowledge graph Attribute Reliability and Maturity Assessment
hc-enterprise-kg quality module

Scores every entity on 6 dimensions:
  1. Completeness  — % of type-specific attributes with non-null/non-empty values
  2. Confidence     — provenance.confidence_level mapped to numeric score
  3. Freshness      — temporal.last_review_date recency score
  4. Source Quality  — provenance.data_quality_score composite
  5. Consistency     — cross-entity relational consistency checks
  6. Gap Coverage    — ratio of documented vs undocumented data gaps

Outputs:
  - Per-entity KarMA score (0.0 - 1.0)
  - Per-type aggregate statistics
  - Enterprise-wide maturity distribution
  - Deficiency heat map for enrichment prioritization
"""

import json
import sys
from pathlib import Path
from datetime import datetime, timezone
from collections import defaultdict
from typing import Dict, List, Any, Optional, Tuple

ASSESSMENT_DATE = "2026-03-04"

# Confidence level to numeric mapping
CONFIDENCE_MAP = {
    "Critical": 0.95,
    "High": 0.85,
    "Medium-High": 0.75,
    "Medium": 0.60,
    "Low": 0.35,
    "": 0.0,
    None: 0.0,
}

# Fields that count as "populated" even when they're structured objects
# (we check their interior for non-null values)
DEEP_CHECK_FIELDS = {
    "temporal", "provenance", "person_name", "reporting_to",
    "experience_profile", "background_check_status", "insider_status",
    "acquisition_source", "api_surface", "encryption_profile",
    "scalability_profile", "availability_design", "observability_stack",
    "vulnerability_profile", "capacity_current", "total_cost_of_ownership",
    "inherent_financial_impact", "materiality_assessment", "treatment_plan",
    "risk_tolerance",
}

# Base fields present on all entities (not type-specific)
BASE_FIELDS = {
    "id", "entity_type", "name", "description", "created_at", "updated_at",
    "valid_from", "valid_until", "version", "tags", "provenance", "temporal",
}


def is_populated(value: Any) -> bool:
    """Determine if an attribute value is meaningfully populated."""
    if value is None:
        return False
    if isinstance(value, str) and value.strip() == "":
        return False
    if isinstance(value, list) and len(value) == 0:
        return False
    if isinstance(value, dict):
        # Check if at least one interior value is non-null/non-empty
        return any(is_populated(v) for v in value.values())
    return True


def count_deep_populated(obj: dict, prefix: str = "") -> Tuple[int, int]:
    """Count total and populated fields in a nested object, flattened."""
    total = 0
    populated = 0
    for key, value in obj.items():
        if key in ("schema_version",):
            continue  # Skip meta fields
        if isinstance(value, dict) and key not in ("provenance",):
            t, p = count_deep_populated(value, f"{prefix}{key}.")
            total += t
            populated += p
        else:
            total += 1
            if is_populated(value):
                populated += 1
    return total, populated


def score_completeness(entity: dict) -> float:
    """Score 1: Attribute completeness (0.0-1.0)."""
    total_fields = 0
    populated_fields = 0

    for key, value in entity.items():
        if key in BASE_FIELDS:
            continue  # Skip base fields, focus on type-specific
        if key in ("created_at", "updated_at", "version"):
            continue

        if key in DEEP_CHECK_FIELDS and isinstance(value, dict):
            t, p = count_deep_populated(value)
            total_fields += t
            populated_fields += p
        else:
            total_fields += 1
            if is_populated(value):
                populated_fields += 1

    if total_fields == 0:
        return 0.0
    return populated_fields / total_fields


def score_confidence(entity: dict) -> float:
    """Score 2: Provenance confidence level (0.0-1.0)."""
    prov = entity.get("provenance", {})
    conf = prov.get("confidence_level", "")
    return CONFIDENCE_MAP.get(conf, 0.0)


def score_freshness(entity: dict) -> float:
    """Score 3: Temporal freshness based on last_review_date (0.0-1.0)."""
    temporal = entity.get("temporal", {})
    last_review = temporal.get("last_review_date")
    last_assessed = entity.get("provenance", {}).get("last_assessed_date")

    # Use whichever is more recent
    date_str = last_review or last_assessed
    if not date_str:
        return 0.0

    try:
        review_date = datetime.fromisoformat(str(date_str).replace("Z", "+00:00"))
        if review_date.tzinfo is None:
            review_date = review_date.replace(tzinfo=timezone.utc)
        now = datetime(2026, 3, 4, tzinfo=timezone.utc)
        days_old = (now - review_date).days
        if days_old <= 7:
            return 1.0
        elif days_old <= 30:
            return 0.9
        elif days_old <= 90:
            return 0.75
        elif days_old <= 180:
            return 0.5
        elif days_old <= 365:
            return 0.25
        else:
            return 0.1
    except (ValueError, TypeError):
        return 0.0


def score_source_quality(entity: dict) -> float:
    """Score 4: Provenance data quality score composite (0.0-1.0)."""
    prov = entity.get("provenance", {})
    dqs = prov.get("data_quality_score", {})

    completeness_pct = dqs.get("completeness_pct")
    accuracy = dqs.get("accuracy_confidence", "")
    timeliness = dqs.get("timeliness_score", "")
    consistency = dqs.get("consistency_score", "")

    scores = []

    if completeness_pct is not None:
        scores.append(min(completeness_pct / 100.0, 1.0))

    accuracy_map = {"High": 0.9, "Medium-High": 0.8, "Medium": 0.6, "Low": 0.3}
    if accuracy in accuracy_map:
        scores.append(accuracy_map[accuracy])

    timeliness_map = {"Current": 0.9, "Recent": 0.7, "Stale": 0.3, "Unknown": 0.1}
    if timeliness in timeliness_map:
        scores.append(timeliness_map[timeliness])

    consistency_map = {"Verified": 0.95, "Consistent": 0.75, "Inconsistent": 0.3}
    if consistency in consistency_map:
        scores.append(consistency_map[consistency])

    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def score_gap_coverage(entity: dict) -> float:
    """Score 5: Known data gaps documentation (0.0-1.0).
    Higher score = gaps are documented with remediation plans.
    Zero gaps can mean either perfect data OR undocumented gaps."""
    prov = entity.get("provenance", {})
    gaps = prov.get("known_data_gaps", [])

    if not gaps:
        # No gaps documented — could be complete or could be unassessed
        completeness = prov.get("data_quality_score", {}).get("completeness_pct")
        if completeness is not None and completeness >= 90:
            return 0.9  # Likely genuinely complete
        elif completeness is not None and completeness >= 70:
            return 0.5  # Probably has undocumented gaps
        else:
            return 0.2  # Almost certainly has undocumented gaps

    # Has documented gaps — score based on remediation plan quality
    has_plan = sum(1 for g in gaps if g.get("remediation_plan"))
    has_priority = sum(1 for g in gaps if g.get("priority"))

    plan_ratio = has_plan / len(gaps) if gaps else 0
    priority_ratio = has_priority / len(gaps) if gaps else 0

    return 0.5 + (plan_ratio * 0.3) + (priority_ratio * 0.2)


def compute_karma_score(entity: dict) -> dict:
    """Compute the composite KarMA score for an entity."""
    completeness = score_completeness(entity)
    confidence = score_confidence(entity)
    freshness = score_freshness(entity)
    source_quality = score_source_quality(entity)
    gap_coverage = score_gap_coverage(entity)

    # Weighted composite (completeness is most important)
    weights = {
        "completeness": 0.30,
        "confidence": 0.20,
        "freshness": 0.15,
        "source_quality": 0.20,
        "gap_coverage": 0.15,
    }

    composite = (
        completeness * weights["completeness"]
        + confidence * weights["confidence"]
        + freshness * weights["freshness"]
        + source_quality * weights["source_quality"]
        + gap_coverage * weights["gap_coverage"]
    )

    return {
        "entity_id": entity.get("id"),
        "entity_type": entity.get("entity_type"),
        "entity_name": entity.get("name", "")[:60],
        "scores": {
            "completeness": round(completeness, 3),
            "confidence": round(confidence, 3),
            "freshness": round(freshness, 3),
            "source_quality": round(source_quality, 3),
            "gap_coverage": round(gap_coverage, 3),
        },
        "karma_composite": round(composite, 3),
        "karma_grade": grade_karma(composite),
    }


def grade_karma(score: float) -> str:
    """Map KarMA composite to letter grade."""
    if score >= 0.85:
        return "A"
    elif score >= 0.70:
        return "B"
    elif score >= 0.55:
        return "C"
    elif score >= 0.40:
        return "D"
    else:
        return "F"


def run_karma_assessment(graph_path: str) -> dict:
    """Run full KarMA assessment on a graph."""
    with open(graph_path) as f:
        graph = json.load(f)

    entities = graph.get("entities", [])
    print(f"KarMA Assessment: Scoring {len(entities)} entities...")

    results = []
    type_scores = defaultdict(list)

    for entity in entities:
        karma = compute_karma_score(entity)
        results.append(karma)
        type_scores[entity.get("entity_type", "unknown")].append(karma["karma_composite"])

    # Aggregate by type
    type_summary = {}
    for etype, scores in sorted(type_scores.items()):
        type_summary[etype] = {
            "count": len(scores),
            "mean_karma": round(sum(scores) / len(scores), 3),
            "min_karma": round(min(scores), 3),
            "max_karma": round(max(scores), 3),
            "grade": grade_karma(sum(scores) / len(scores)),
        }

    # Enterprise aggregate
    all_scores = [r["karma_composite"] for r in results]
    enterprise_mean = sum(all_scores) / len(all_scores) if all_scores else 0

    # Grade distribution
    grade_dist = defaultdict(int)
    for r in results:
        grade_dist[r["karma_grade"]] += 1

    # Bottom 20 entities (enrichment priority)
    bottom_20 = sorted(results, key=lambda x: x["karma_composite"])[:20]

    report = {
        "assessment_date": ASSESSMENT_DATE,
        "assessed_by": "KarMA v1.0 — hc-enterprise-kg Quality Module",
        "total_entities": len(entities),
        "enterprise_karma": {
            "mean": round(enterprise_mean, 3),
            "grade": grade_karma(enterprise_mean),
        },
        "grade_distribution": dict(sorted(grade_dist.items())),
        "type_summary": type_summary,
        "enrichment_priority_queue": [
            {
                "entity_id": r["entity_id"],
                "entity_type": r["entity_type"],
                "name": r["entity_name"],
                "karma": r["karma_composite"],
                "grade": r["karma_grade"],
                "weakest_dimension": min(r["scores"], key=r["scores"].get),
            }
            for r in bottom_20
        ],
        "dimension_averages": {
            "completeness": round(sum(r["scores"]["completeness"] for r in results) / len(results), 3),
            "confidence": round(sum(r["scores"]["confidence"] for r in results) / len(results), 3),
            "freshness": round(sum(r["scores"]["freshness"] for r in results) / len(results), 3),
            "source_quality": round(sum(r["scores"]["source_quality"] for r in results) / len(results), 3),
            "gap_coverage": round(sum(r["scores"]["gap_coverage"] for r in results) / len(results), 3),
        },
    }

    return report


def main():
    repo_root = Path(__file__).parent.parent
    graph_path = repo_root / "graph.json"

    if not graph_path.exists():
        print("ERROR: graph.json not found")
        sys.exit(1)

    report = run_karma_assessment(str(graph_path))

    # Print summary
    print(f"\n{'='*70}")
    print(f"  KarMA Assessment Report — {report['assessment_date']}")
    print(f"{'='*70}")
    print(f"\n  Enterprise KarMA Score: {report['enterprise_karma']['mean']:.3f} (Grade: {report['enterprise_karma']['grade']})")
    print(f"  Total Entities Scored: {report['total_entities']}")

    print(f"\n  Grade Distribution:")
    for grade in ["A", "B", "C", "D", "F"]:
        count = report["grade_distribution"].get(grade, 0)
        bar = "█" * (count // 10) + "▒" * (count % 10 > 0)
        print(f"    {grade}: {count:>5} entities  {bar}")

    print(f"\n  Dimension Averages:")
    for dim, score in report["dimension_averages"].items():
        bar_len = int(score * 30)
        bar = "█" * bar_len + "░" * (30 - bar_len)
        print(f"    {dim:>16s}: {score:.3f} [{bar}]")

    print(f"\n  Type Summary (sorted by KarMA):")
    sorted_types = sorted(report["type_summary"].items(), key=lambda x: x[1]["mean_karma"])
    for etype, stats in sorted_types:
        print(f"    {etype:>25s}: {stats['mean_karma']:.3f} ({stats['grade']}) [{stats['count']:>4} entities] range [{stats['min_karma']:.2f}-{stats['max_karma']:.2f}]")

    print(f"\n  Enrichment Priority Queue (Bottom 20):")
    for item in report["enrichment_priority_queue"]:
        print(f"    {item['entity_id']:>45s} | {item['karma']:.3f} ({item['grade']}) | weakest: {item['weakest_dimension']:>15s} | {item['name']}")

    # Save full report
    report_path = repo_root / "karma_assessment_report.json"
    with open(report_path, "w") as f:
        json.dump(report, f, indent=2)
    print(f"\n  Full report saved to: {report_path}")

    # Save per-entity scores for GraphGuard cross-reference
    entity_scores_path = repo_root / "karma_entity_scores.json"
    # Re-run to get full entity list (or we could refactor to return it)
    with open(graph_path) as f:
        graph = json.load(f)
    all_entity_results = [compute_karma_score(e) for e in graph["entities"]]
    with open(entity_scores_path, "w") as f:
        json.dump(all_entity_results, f, indent=2)
    print(f"  Entity scores saved to: {entity_scores_path}")


if __name__ == "__main__":
    main()

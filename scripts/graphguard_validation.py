#!/usr/bin/env python3
"""
GraphGuard — Graph Integrity and Consistency Validation
hc-enterprise-kg quality module

Validates the knowledge graph across 8 integrity dimensions:
  1. Referential Integrity   — no dangling relationship references
  2. Duplicate Detection     — fuzzy name matching within types
  3. Orphan Detection        — entities with zero relationships
  4. Hierarchical Consistency — parent-child value propagation checks
  5. Provenance Completeness — required provenance fields populated
  6. Temporal Coherence      — date field logical consistency
  7. Schema Conformance      — entity_type field alignment
  8. Relational Density       — relationship count vs expected range

Outputs:
  - Per-check pass/fail with finding details
  - Severity-graded findings (CRITICAL, HIGH, MEDIUM, LOW, INFO)
  - Cross-entity consistency violations
  - Remediation recommendations
"""

import json
import sys
from pathlib import Path
from datetime import datetime
from collections import defaultdict
from typing import Dict, List, Any, Tuple

try:
    from rapidfuzz import fuzz
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "rapidfuzz", "--break-system-packages", "-q"])
    from rapidfuzz import fuzz

ASSESSMENT_DATE = "2026-03-04"

# Expected relationship density ranges by entity type (min, typical, max)
EXPECTED_DENSITY = {
    "system": (2, 8, 25),
    "data_asset": (2, 6, 20),
    "vendor": (1, 4, 15),
    "person": (1, 3, 12),
    "risk": (1, 4, 15),
    "control": (1, 3, 10),
    "policy": (1, 3, 12),
    "department": (1, 5, 20),
    "role": (1, 3, 10),
    "regulation": (1, 5, 20),
    "data_domain": (2, 5, 15),
    "customer": (1, 4, 12),
    "product": (1, 4, 15),
    "initiative": (2, 5, 15),
    "site": (2, 6, 20),
    "network": (1, 3, 10),
    "integration": (2, 3, 8),
    "contract": (1, 3, 10),
    "business_capability": (1, 4, 15),
    "organizational_unit": (1, 4, 15),
    "geography": (1, 3, 10),
    "jurisdiction": (1, 3, 10),
    "location": (1, 3, 10),
    "product_portfolio": (1, 3, 10),
    "market_segment": (1, 3, 10),
    "incident": (1, 3, 8),
}

# Valid relationship schemas (source_type -> relationship_type -> target_type)
# Not exhaustive; used for spot-checking
VALID_PATTERNS = {
    ("system", "depends_on", "system"),
    ("system", "hosted_on", "system"),
    ("system", "hosted_on", "site"),
    ("system", "stores", "data_asset"),
    ("system", "integrates_with", "system"),
    ("data_asset", "hosted_on", "system"),
    ("person", "has_role", "role"),
    ("person", "works_in", "department"),
    ("person", "reports_to", "person"),
    ("vendor", "supplies", "system"),
    ("vendor", "contracts_with", "department"),
    ("risk", "mitigates", "control"),
    ("control", "mitigates", "risk"),
    ("control", "enforces", "policy"),
    ("policy", "applies_to", "data_domain"),
    ("policy", "governs", "data_asset"),
    ("regulation", "subject_to", "jurisdiction"),
    ("department", "managed_by", "person"),
    ("department", "located_in", "geography"),
    ("role", "belongs_to", "department"),
}


class Finding:
    """A single GraphGuard finding."""
    def __init__(self, check: str, severity: str, message: str, entity_ids: list = None, recommendation: str = ""):
        self.check = check
        self.severity = severity
        self.message = message
        self.entity_ids = entity_ids or []
        self.recommendation = recommendation

    def to_dict(self):
        return {
            "check": self.check,
            "severity": self.severity,
            "message": self.message,
            "entity_ids": self.entity_ids,
            "recommendation": self.recommendation,
        }


class GraphGuard:
    def __init__(self, graph: dict):
        self.entities = graph.get("entities", [])
        self.relationships = graph.get("relationships", [])
        self.entity_map = {e["id"]: e for e in self.entities}
        self.findings: List[Finding] = []

        # Build adjacency
        self.outgoing = defaultdict(list)
        self.incoming = defaultdict(list)
        for rel in self.relationships:
            sid = rel.get("source_id")
            tid = rel.get("target_id")
            self.outgoing[sid].append(rel)
            self.incoming[tid].append(rel)

    def check_referential_integrity(self):
        """Check 1: No dangling references in relationships."""
        entity_ids = set(self.entity_map.keys())
        dangling_source = 0
        dangling_target = 0
        examples = []

        for rel in self.relationships:
            sid = rel.get("source_id")
            tid = rel.get("target_id")
            if sid not in entity_ids:
                dangling_source += 1
                if len(examples) < 5:
                    examples.append(f"  source '{sid}' in rel {rel.get('id','?')}")
            if tid not in entity_ids:
                dangling_target += 1
                if len(examples) < 5:
                    examples.append(f"  target '{tid}' in rel {rel.get('id','?')}")

        total_dangling = dangling_source + dangling_target
        if total_dangling > 0:
            self.findings.append(Finding(
                "referential_integrity", "CRITICAL",
                f"{total_dangling} dangling references found ({dangling_source} source, {dangling_target} target)",
                recommendation="Remove or reconnect dangling relationships"
            ))
        else:
            self.findings.append(Finding(
                "referential_integrity", "PASS",
                f"All {len(self.relationships)} relationships have valid source and target entities"
            ))

    def check_duplicates(self, threshold: float = 0.85):
        """Check 2: Fuzzy duplicate detection within entity types."""
        by_type = defaultdict(list)
        for e in self.entities:
            by_type[e.get("entity_type", "unknown")].append(e)

        duplicates = []
        for etype, elist in by_type.items():
            for i, e1 in enumerate(elist):
                for e2 in elist[i + 1:]:
                    n1 = e1.get("name", "")
                    n2 = e2.get("name", "")
                    if not n1 or not n2:
                        continue
                    sim = fuzz.ratio(n1.lower(), n2.lower()) / 100.0
                    if sim >= threshold:
                        duplicates.append({
                            "id1": e1["id"], "name1": n1,
                            "id2": e2["id"], "name2": n2,
                            "similarity": round(sim, 3),
                            "type": etype,
                        })

        if duplicates:
            severity = "HIGH" if len(duplicates) > 5 else "MEDIUM"
            self.findings.append(Finding(
                "duplicate_detection", severity,
                f"{len(duplicates)} potential duplicate pairs found (≥{threshold*100:.0f}% similarity)",
                entity_ids=[d["id1"] for d in duplicates] + [d["id2"] for d in duplicates],
                recommendation="Consolidate duplicates, migrate relationships to primary entity"
            ))
            for d in duplicates[:10]:
                self.findings.append(Finding(
                    "duplicate_detection", "INFO",
                    f"  [{d['type']}] '{d['name1']}' ({d['id1']}) ↔ '{d['name2']}' ({d['id2']}) — {d['similarity']:.0%}"
                ))
        else:
            self.findings.append(Finding(
                "duplicate_detection", "PASS",
                "No duplicates detected above threshold"
            ))

    def check_orphans(self):
        """Check 3: Entities with zero relationships."""
        connected = set()
        for rel in self.relationships:
            connected.add(rel.get("source_id"))
            connected.add(rel.get("target_id"))

        orphans = []
        for e in self.entities:
            if e["id"] not in connected:
                orphans.append({"id": e["id"], "type": e.get("entity_type"), "name": e.get("name", "")[:50]})

        if orphans:
            severity = "HIGH" if len(orphans) > 20 else "MEDIUM"
            self.findings.append(Finding(
                "orphan_detection", severity,
                f"{len(orphans)} orphan entities (no relationships) found",
                entity_ids=[o["id"] for o in orphans],
                recommendation="Connect orphans to related entities or remove if invalid"
            ))
            by_type = defaultdict(int)
            for o in orphans:
                by_type[o["type"]] += 1
            for etype, count in sorted(by_type.items(), key=lambda x: -x[1]):
                self.findings.append(Finding(
                    "orphan_detection", "INFO",
                    f"  {etype}: {count} orphans"
                ))
        else:
            self.findings.append(Finding(
                "orphan_detection", "PASS",
                "All entities have at least one relationship"
            ))

    def check_hierarchical_consistency(self):
        """Check 4: Parent-child relational value consistency.
        Examples: department budget should not exceed parent org_unit budget.
        Risk residual_risk_level should not exceed inherent_risk_level."""
        inconsistencies = []

        # Check risk: residual should not be worse than inherent
        risk_level_order = {"Low": 1, "Medium": 2, "Moderate": 2, "High": 3, "Major": 3, "Critical": 4, "Catastrophic": 5}
        for e in self.entities:
            if e.get("entity_type") != "risk":
                continue
            inherent = e.get("inherent_risk_level", "")
            residual = e.get("residual_risk_level", "")
            if inherent and residual:
                i_val = risk_level_order.get(inherent, 0)
                r_val = risk_level_order.get(residual, 0)
                if r_val > i_val:
                    inconsistencies.append({
                        "entity_id": e["id"],
                        "issue": f"Residual risk ({residual}) exceeds inherent risk ({inherent})",
                        "type": "risk_hierarchy"
                    })

        # Check: entities with depends_on should not have higher availability than their dependency
        for rel in self.relationships:
            if rel.get("relationship_type") != "depends_on":
                continue
            source = self.entity_map.get(rel.get("source_id"), {})
            target = self.entity_map.get(rel.get("target_id"), {})
            if source.get("entity_type") == "system" and target.get("entity_type") == "system":
                s_uptime = (source.get("availability_design") or {}).get("designed_uptime_pct")
                t_uptime = (target.get("availability_design") or {}).get("designed_uptime_pct")
                if s_uptime and t_uptime and s_uptime > t_uptime:
                    inconsistencies.append({
                        "entity_id": source["id"],
                        "issue": f"System '{source.get('name','')}' claims {s_uptime}% uptime but depends on '{target.get('name','')}' with only {t_uptime}% uptime",
                        "type": "availability_hierarchy"
                    })

        if inconsistencies:
            self.findings.append(Finding(
                "hierarchical_consistency", "HIGH",
                f"{len(inconsistencies)} hierarchical consistency violations found",
                entity_ids=[i["entity_id"] for i in inconsistencies],
                recommendation="Review parent-child value propagation logic"
            ))
            for inc in inconsistencies[:10]:
                self.findings.append(Finding(
                    "hierarchical_consistency", "INFO",
                    f"  [{inc['type']}] {inc['entity_id']}: {inc['issue']}"
                ))
        else:
            self.findings.append(Finding(
                "hierarchical_consistency", "PASS",
                "No hierarchical consistency violations detected"
            ))

    def check_provenance_completeness(self):
        """Check 5: Required provenance fields populated."""
        required_prov_fields = ["primary_data_source", "last_assessed_date", "assessed_by", "confidence_level"]
        missing_counts = defaultdict(int)
        incomplete_entities = 0

        for e in self.entities:
            prov = e.get("provenance", {})
            entity_incomplete = False
            for field in required_prov_fields:
                val = prov.get(field)
                if not val or (isinstance(val, str) and val.strip() == ""):
                    missing_counts[field] += 1
                    entity_incomplete = True
            if entity_incomplete:
                incomplete_entities += 1

        total = len(self.entities)
        completeness_pct = ((total - incomplete_entities) / total * 100) if total > 0 else 0

        severity = "CRITICAL" if completeness_pct < 50 else "HIGH" if completeness_pct < 75 else "MEDIUM" if completeness_pct < 90 else "LOW"
        self.findings.append(Finding(
            "provenance_completeness", severity,
            f"Provenance completeness: {completeness_pct:.1f}% ({total - incomplete_entities}/{total} entities fully documented)",
            recommendation="Populate missing provenance fields during enrichment passes"
        ))
        for field, count in sorted(missing_counts.items(), key=lambda x: -x[1]):
            pct = count / total * 100
            self.findings.append(Finding(
                "provenance_completeness", "INFO",
                f"  {field}: missing on {count} entities ({pct:.1f}%)"
            ))

    def check_temporal_coherence(self):
        """Check 6: Date field logical consistency."""
        incoherent = []

        for e in self.entities:
            temporal = e.get("temporal", {})
            eff = temporal.get("effective_date")
            exp = temporal.get("expiration_date")
            last_rev = temporal.get("last_review_date")
            next_rev = temporal.get("next_review_date")

            try:
                if eff and exp:
                    if str(eff) > str(exp):
                        incoherent.append({"id": e["id"], "issue": f"effective_date ({eff}) > expiration_date ({exp})"})
                if last_rev and next_rev:
                    if str(last_rev) > str(next_rev):
                        incoherent.append({"id": e["id"], "issue": f"last_review_date ({last_rev}) > next_review_date ({next_rev})"})
            except (TypeError, ValueError):
                pass

        if incoherent:
            self.findings.append(Finding(
                "temporal_coherence", "MEDIUM",
                f"{len(incoherent)} temporal coherence violations found",
                entity_ids=[i["id"] for i in incoherent],
                recommendation="Correct date ordering: effective < expiration, last_review < next_review"
            ))
        else:
            self.findings.append(Finding(
                "temporal_coherence", "PASS",
                "All temporal fields are logically consistent"
            ))

    def check_relational_density(self):
        """Check 7: Relationship count per entity vs expected range."""
        # Count relationships per entity
        rel_count = defaultdict(int)
        for rel in self.relationships:
            rel_count[rel.get("source_id")] += 1
            rel_count[rel.get("target_id")] += 1

        under_connected = []
        over_connected = []

        for e in self.entities:
            etype = e.get("entity_type", "unknown")
            eid = e["id"]
            count = rel_count.get(eid, 0)
            expected = EXPECTED_DENSITY.get(etype, (0, 2, 50))
            min_exp, _, max_exp = expected

            if count < min_exp:
                under_connected.append({"id": eid, "type": etype, "count": count, "expected_min": min_exp, "name": e.get("name","")[:40]})
            elif count > max_exp * 2:  # Only flag extreme over-connection
                over_connected.append({"id": eid, "type": etype, "count": count, "expected_max": max_exp, "name": e.get("name","")[:40]})

        if under_connected:
            self.findings.append(Finding(
                "relational_density", "MEDIUM",
                f"{len(under_connected)} under-connected entities (below minimum expected relationships)",
                entity_ids=[u["id"] for u in under_connected[:20]],
                recommendation="Add missing relationships during enrichment"
            ))
            by_type = defaultdict(int)
            for u in under_connected:
                by_type[u["type"]] += 1
            for etype, count in sorted(by_type.items(), key=lambda x: -x[1])[:10]:
                self.findings.append(Finding("relational_density", "INFO", f"  {etype}: {count} under-connected"))

        if over_connected:
            self.findings.append(Finding(
                "relational_density", "LOW",
                f"{len(over_connected)} highly-connected entities (may indicate hub entities or data quality issues)",
                entity_ids=[o["id"] for o in over_connected[:10]],
                recommendation="Review hub entities for correctness"
            ))

        if not under_connected and not over_connected:
            self.findings.append(Finding(
                "relational_density", "PASS",
                "All entities within expected relationship density range"
            ))

    def check_schema_conformance(self):
        """Check 8: Entity types match known schema types."""
        known_types = set(EXPECTED_DENSITY.keys())
        unknown_types = defaultdict(int)

        for e in self.entities:
            etype = e.get("entity_type", "")
            if etype and etype not in known_types:
                unknown_types[etype] += 1

        if unknown_types:
            self.findings.append(Finding(
                "schema_conformance", "MEDIUM",
                f"{len(unknown_types)} unknown entity types found",
                recommendation="Verify these types exist in hc-enterprise-kg schema"
            ))
            for etype, count in sorted(unknown_types.items(), key=lambda x: -x[1]):
                self.findings.append(Finding("schema_conformance", "INFO", f"  {etype}: {count} entities"))
        else:
            self.findings.append(Finding(
                "schema_conformance", "PASS",
                f"All {len(self.entities)} entities use valid schema types"
            ))

    def run_all_checks(self) -> dict:
        """Execute all GraphGuard checks and return structured report."""
        print("GraphGuard Validation: Running 8 integrity checks...")

        self.check_referential_integrity()
        self.check_duplicates()
        self.check_orphans()
        self.check_hierarchical_consistency()
        self.check_provenance_completeness()
        self.check_temporal_coherence()
        self.check_relational_density()
        self.check_schema_conformance()

        # Summarize
        severity_counts = defaultdict(int)
        for f in self.findings:
            if f.severity != "INFO":
                severity_counts[f.severity] += 1

        checks_passed = severity_counts.get("PASS", 0)
        total_checks = sum(v for k, v in severity_counts.items() if k != "INFO")

        report = {
            "assessment_date": ASSESSMENT_DATE,
            "assessed_by": "GraphGuard v1.0 — hc-enterprise-kg Integrity Module",
            "total_entities": len(self.entities),
            "total_relationships": len(self.relationships),
            "checks_passed": checks_passed,
            "total_checks": total_checks,
            "severity_summary": dict(severity_counts),
            "overall_integrity": "HEALTHY" if severity_counts.get("CRITICAL", 0) == 0 and severity_counts.get("HIGH", 0) <= 2
                else "AT_RISK" if severity_counts.get("CRITICAL", 0) == 0
                else "CRITICAL",
            "findings": [f.to_dict() for f in self.findings],
        }

        return report


def main():
    repo_root = Path(__file__).parent.parent
    graph_path = repo_root / "graph.json"

    if not graph_path.exists():
        print("ERROR: graph.json not found")
        sys.exit(1)

    with open(graph_path) as f:
        graph = json.load(f)

    guard = GraphGuard(graph)
    report = guard.run_all_checks()

    # Print summary
    print(f"\n{'='*70}")
    print(f"  GraphGuard Integrity Report — {report['assessment_date']}")
    print(f"{'='*70}")
    print(f"\n  Overall Status: {report['overall_integrity']}")
    print(f"  Entities: {report['total_entities']} | Relationships: {report['total_relationships']}")
    print(f"\n  Severity Distribution:")
    for sev in ["CRITICAL", "HIGH", "MEDIUM", "LOW", "PASS"]:
        count = report["severity_summary"].get(sev, 0)
        icon = {"CRITICAL": "🔴", "HIGH": "🟠", "MEDIUM": "🟡", "LOW": "🔵", "PASS": "🟢"}.get(sev, "⚪")
        print(f"    {icon} {sev}: {count}")

    print(f"\n  Findings Detail:")
    for f in report["findings"]:
        if f["severity"] == "INFO":
            print(f"       {f['message']}")
        else:
            icon = {"CRITICAL": "🔴", "HIGH": "🟠", "MEDIUM": "🟡", "LOW": "🔵", "PASS": "🟢"}.get(f["severity"], "⚪")
            print(f"    {icon} [{f['check']}] {f['message']}")
            if f.get("recommendation"):
                print(f"       → {f['recommendation']}")

    # Save report
    report_path = repo_root / "graphguard_report.json"
    with open(report_path, "w") as f:
        json.dump(report, f, indent=2)
    print(f"\n  Full report saved to: {report_path}")

    # Exit code based on findings
    if report["overall_integrity"] == "CRITICAL":
        sys.exit(2)
    elif report["overall_integrity"] == "AT_RISK":
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()

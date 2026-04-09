"""
Phase planner.

Reads graph.json and builds the entity queues for all 10 population phases
described in FINANCIAL_POPULATION_PLAN.md Section 5.4. Each phase queue is
written to audit/orchestrator/queue/phase_NN.json as a list of entity IDs.

Phases:
    0  normalize_skeletons     all 3,071 entities → v2 empty skeleton
    1  consolidated            ou-029
    2  segments                pf-001, pf-002, ou-001, ou-002
    3  sub_portfolios          L2 product_portfolio and sub-segment OUs
    4  departments             all 250 departments
    5  revenue_facing          customers, products, market_segments, contracts
    6  people                  persons, roles
    7  technology              systems, integrations, networks
    8  governance              controls, policies, regulations, risks
    9  locations               sites, geographies, jurisdictions, locations
    10 remaining               data_assets, data_domains, business_capabilities,
                               vendors, initiatives, incidents
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
GRAPH_PATH = REPO_ROOT / "graph.json"
QUEUE_DIR = REPO_ROOT / "audit" / "orchestrator" / "queue"

# ── Phase definitions ───────────────────────────────────────────────────────
PHASE_SEGMENTS = {"pf-001", "pf-002", "ou-001", "ou-002"}
PHASE_CONSOLIDATED = {"ou-029"}

# L2 sub-portfolios and business unit sub-OUs. These are the entities that
# sit one level below Private Cloud / Public Cloud / FAIR (Apps/Multicloud
# Services / Intelligent Services). The list below is built dynamically by
# walking the graph hierarchy, but this seed set handles product_portfolios
# already known from prior population work.
KNOWN_L2_PF = {
    "pf-013", "pf-014", "pf-015", "pf-016", "pf-017", "pf-018", "pf-019",
    "pf-020", "pf-021", "pf-022", "pf-023", "pf-024", "pf-025", "pf-033",
}


def load_graph() -> dict[str, Any]:
    with GRAPH_PATH.open() as f:
        return json.load(f)


def all_entities() -> list[dict[str, Any]]:
    return load_graph().get("entities", [])


def _by_type(entities: list[dict[str, Any]], t: str) -> list[str]:
    return sorted(e["id"] for e in entities if e.get("entity_type") == t)


def build_phase_queues() -> dict[int, list[str]]:
    entities = all_entities()
    by_id = {e["id"]: e for e in entities}

    queues: dict[int, list[str]] = {}

    # Phase 0: normalize everyone
    queues[0] = sorted(e["id"] for e in entities)

    # Phase 1: consolidated
    queues[1] = sorted(e["id"] for e in entities if e["id"] in PHASE_CONSOLIDATED)

    # Phase 2: segments
    queues[2] = sorted(e["id"] for e in entities if e["id"] in PHASE_SEGMENTS)

    # Phase 3: sub-portfolios (product_portfolio entities minus segment parents
    # plus any OU sub-units below segments). Conservative: all product_portfolio
    # entities that are not pf-001 or pf-002, plus KNOWN_L2_PF.
    l3_ids: set[str] = set()
    for e in entities:
        if e.get("entity_type") == "product_portfolio":
            if e["id"] not in PHASE_SEGMENTS:
                l3_ids.add(e["id"])
    queues[3] = sorted(l3_ids)

    # Phase 4: departments
    queues[4] = _by_type(entities, "department")

    # Phase 5: revenue-facing
    rev_types = {"customer", "product", "market_segment", "contract"}
    queues[5] = sorted(
        e["id"] for e in entities if e.get("entity_type") in rev_types
    )

    # Phase 6: people
    queues[6] = sorted(
        e["id"] for e in entities if e.get("entity_type") in {"person", "role"}
    )

    # Phase 7: technology
    tech_types = {"system", "integration", "network"}
    queues[7] = sorted(
        e["id"] for e in entities if e.get("entity_type") in tech_types
    )

    # Phase 8: governance
    gov_types = {"control", "policy", "regulation", "risk"}
    queues[8] = sorted(
        e["id"] for e in entities if e.get("entity_type") in gov_types
    )

    # Phase 9: locations
    loc_types = {"site", "geography", "jurisdiction", "location"}
    queues[9] = sorted(
        e["id"] for e in entities if e.get("entity_type") in loc_types
    )

    # Phase 10: remaining
    remaining_types = {
        "data_asset",
        "data_domain",
        "business_capability",
        "vendor",
        "initiative",
        "incident",
    }
    queues[10] = sorted(
        e["id"] for e in entities if e.get("entity_type") in remaining_types
    )

    # Residual OUs not captured anywhere (organizational_unit entities that are
    # not L0/L1 and did not appear in Phase 3): slot into Phase 3 as L2-like
    # carriers so they are not orphaned. This is a safety net.
    already_placed = set()
    for i in (1, 2, 3):
        already_placed.update(queues[i])
    for e in entities:
        if e.get("entity_type") == "organizational_unit" and e["id"] not in already_placed:
            queues[3].append(e["id"])
    queues[3] = sorted(set(queues[3]))

    return queues


def write_queues(queues: dict[int, list[str]]) -> dict[int, int]:
    QUEUE_DIR.mkdir(parents=True, exist_ok=True)
    counts: dict[int, int] = {}
    for phase, ids in queues.items():
        p = QUEUE_DIR / f"phase_{phase:02d}.json"
        with p.open("w") as f:
            json.dump({"phase": phase, "count": len(ids), "entity_ids": ids}, f, indent=2)
        counts[phase] = len(ids)
    return counts


def phase_summary(queues: dict[int, list[str]]) -> list[dict[str, Any]]:
    names = {
        0: "normalize_skeletons",
        1: "consolidated",
        2: "segments",
        3: "sub_portfolios",
        4: "departments",
        5: "revenue_facing",
        6: "people",
        7: "technology",
        8: "governance",
        9: "locations",
        10: "remaining",
    }
    return [
        {"phase": p, "name": names[p], "count": len(queues[p])}
        for p in sorted(queues.keys())
    ]


def load_queue(phase: int) -> list[str]:
    p = QUEUE_DIR / f"phase_{phase:02d}.json"
    if not p.exists():
        return []
    with p.open() as f:
        return json.load(f)["entity_ids"]


if __name__ == "__main__":
    q = build_phase_queues()
    counts = write_queues(q)
    print("Phase queues written:")
    for phase, count in sorted(counts.items()):
        print(f"  phase_{phase:02d}: {count}")
    total = sum(counts.values()) - counts[0]  # phase 0 is same entities as rest
    print(f"Total entities (phases 1-10): {total}")
    print(f"Phase 0 (normalize): {counts[0]}")

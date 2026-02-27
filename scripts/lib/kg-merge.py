#!/usr/bin/env python3
"""
kg-merge.py — Union-merge two graph data directories (branch wins on conflict).

Usage:
    python3 kg-merge.py <base-dir> <branch-dir> <output-dir>

    base-dir:   data directory from main branch
    branch-dir: data directory from team member's branch
    output-dir: merged result written as per-type files

Merge strategy:
    Entities:      union by ID — branch version wins when same ID exists in both
    Relationships: union by (source_id, target_id, relationship_type) — branch wins

"Branch wins" means the team member's additions/edits are always preserved.
Conflicts are reported but never block the merge.
"""

import json
import sys
from collections import defaultdict
from pathlib import Path


def load_dir(data_dir: Path) -> tuple[dict[str, dict], list[dict]]:
    """Return entities keyed by id, and flat relationship list."""
    entities: dict[str, dict] = {}
    relationships: list[dict] = []

    entities_dir = data_dir / "entities"
    if entities_dir.exists():
        for f in sorted(entities_dir.glob("*.json")):
            for entity in json.loads(f.read_text()):
                entities[entity["id"]] = entity

    rels_dir = data_dir / "relationships"
    if rels_dir.exists():
        for f in sorted(rels_dir.glob("*.json")):
            relationships.extend(json.loads(f.read_text()))

    return entities, relationships


def merge(base_dir: Path, branch_dir: Path, output_dir: Path) -> None:
    base_entities, base_rels = load_dir(base_dir)
    branch_entities, branch_rels = load_dir(branch_dir)

    # ── Entity merge ────────────────────────────────────────────────────────
    # Start with base, overwrite with branch (branch wins on any conflict)
    merged_entities = {**base_entities, **branch_entities}

    conflicts = [
        eid for eid in branch_entities
        if eid in base_entities and base_entities[eid] != branch_entities[eid]
    ]
    new_in_branch = [eid for eid in branch_entities if eid not in base_entities]
    new_in_base   = [eid for eid in base_entities   if eid not in branch_entities]

    # ── Relationship merge ──────────────────────────────────────────────────
    rel_index: dict[tuple, dict] = {}
    for rel in base_rels:
        key = (rel["source_id"], rel["target_id"], rel["relationship_type"])
        rel_index[key] = rel
    for rel in branch_rels:
        key = (rel["source_id"], rel["target_id"], rel["relationship_type"])
        rel_index[key] = rel  # branch wins

    # ── Write output ────────────────────────────────────────────────────────
    output_dir.mkdir(parents=True, exist_ok=True)

    by_type: dict[str, list] = defaultdict(list)
    for entity in merged_entities.values():
        by_type[entity["entity_type"]].append(entity)

    entities_out = output_dir / "entities"
    entities_out.mkdir(exist_ok=True)
    for etype, ents in sorted(by_type.items()):
        (entities_out / f"{etype}.json").write_text(json.dumps(ents, indent=2) + "\n")

    by_rel: dict[str, list] = defaultdict(list)
    for rel in rel_index.values():
        by_rel[rel["relationship_type"]].append(rel)

    rels_out = output_dir / "relationships"
    rels_out.mkdir(exist_ok=True)
    for rtype, rels in sorted(by_rel.items()):
        (rels_out / f"{rtype}.json").write_text(json.dumps(rels, indent=2) + "\n")

    # ── Summary ──────────────────────────────────────────────────────────────
    print(f"Merged: {len(merged_entities)} entities, {len(rel_index)} relationships")
    print(f"  New from branch : {len(new_in_branch)} entities")
    print(f"  New from base   : {len(new_in_base)} entities")
    if conflicts:
        print(f"  Conflicts (branch won): {len(conflicts)}")
        for eid in conflicts[:10]:
            name = branch_entities[eid].get("name", eid)
            print(f"    {eid[:8]}…  {name}")
        if len(conflicts) > 10:
            print(f"    … and {len(conflicts) - 10} more")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: kg-merge.py <base-dir> <branch-dir> <output-dir>", file=sys.stderr)
        sys.exit(1)
    merge(Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]))

#!/usr/bin/env python3
"""
kg-split.py — Decompose graph.json into per-entity-type and per-relationship-type files.

Usage:
    python3 kg-split.py <graph.json> <output-dir>

Output structure:
    <output-dir>/
        entities/
            person.json
            system.json
            ...
        relationships/
            works_in.json
            depends_on.json
            ...

Each output file is a JSON array of objects of that type.
git diffs are now per-type, so two people editing different types never conflict.
"""

import json
import sys
from collections import defaultdict
from pathlib import Path


def split(graph_path: Path, output_dir: Path) -> None:
    try:
        with open(graph_path) as f:
            graph = json.load(f)
    except json.JSONDecodeError as e:
        print(f"ERROR: {graph_path} is not valid JSON: {e}", file=sys.stderr)
        sys.exit(1)
    except OSError as e:
        print(f"ERROR: Cannot read {graph_path}: {e}", file=sys.stderr)
        sys.exit(1)

    if not isinstance(graph, dict):
        print("ERROR: graph.json root must be a JSON object.", file=sys.stderr)
        sys.exit(1)

    # ── Entities ──────────────────────────────────────────────────────────
    by_type: dict[str, list] = defaultdict(list)
    for entity in graph.get("entities", []):
        etype = entity.get("entity_type", "unknown")
        by_type[etype].append(entity)

    entities_dir = output_dir / "entities"
    entities_dir.mkdir(parents=True, exist_ok=True)

    for etype, entities in sorted(by_type.items()):
        out = entities_dir / f"{etype}.json"
        out.write_text(json.dumps(entities, indent=2) + "\n")

    # ── Relationships ──────────────────────────────────────────────────────
    by_rel: dict[str, list] = defaultdict(list)
    for rel in graph.get("relationships", []):
        rtype = rel.get("relationship_type", "unknown")
        by_rel[rtype].append(rel)

    rels_dir = output_dir / "relationships"
    rels_dir.mkdir(parents=True, exist_ok=True)

    for rtype, rels in sorted(by_rel.items()):
        out = rels_dir / f"{rtype}.json"
        out.write_text(json.dumps(rels, indent=2) + "\n")

    n_entities = sum(len(v) for v in by_type.values())
    n_rels = sum(len(v) for v in by_rel.values())
    print(
        f"Split: {n_entities} entities ({len(by_type)} types), "
        f"{n_rels} relationships ({len(by_rel)} types)"
    )


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: kg-split.py <graph.json> <output-dir>", file=sys.stderr)
        sys.exit(1)
    split(Path(sys.argv[1]), Path(sys.argv[2]))

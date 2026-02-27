#!/usr/bin/env python3
"""
kg-build.py — Assemble per-type files into a single graph.json for the MCP server.

Usage:
    python3 kg-build.py <data-dir> <graph.json>

Reads:
    <data-dir>/entities/*.json       — arrays of entities by type
    <data-dir>/relationships/*.json  — arrays of relationships by type

Writes:
    <graph.json>  — single combined graph file (gitignored in data repo)

The MCP server reads this file and auto-reloads when its mtime changes.
"""

import json
import sys
from pathlib import Path


def build(data_dir: Path, output_path: Path) -> None:
    entities: list[dict] = []
    relationships: list[dict] = []

    entities_dir = data_dir / "entities"
    if entities_dir.exists():
        for f in sorted(entities_dir.glob("*.json")):
            try:
                data = json.loads(f.read_text())
                if not isinstance(data, list):
                    print(f"WARNING: {f} is not a JSON array — skipping", file=sys.stderr)
                    continue
                entities.extend(data)
            except json.JSONDecodeError as e:
                print(f"WARNING: {f} has invalid JSON: {e} — skipping", file=sys.stderr)

    rels_dir = data_dir / "relationships"
    if rels_dir.exists():
        for f in sorted(rels_dir.glob("*.json")):
            try:
                data = json.loads(f.read_text())
                if not isinstance(data, list):
                    print(f"WARNING: {f} is not a JSON array — skipping", file=sys.stderr)
                    continue
                relationships.extend(data)
            except json.JSONDecodeError as e:
                print(f"WARNING: {f} has invalid JSON: {e} — skipping", file=sys.stderr)

    graph = {"entities": entities, "relationships": relationships}
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(graph, indent=2) + "\n")

    print(
        f"Built: {len(entities)} entities, {len(relationships)} relationships"
        f" → {output_path}"
    )


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: kg-build.py <data-dir> <graph.json>", file=sys.stderr)
        sys.exit(1)
    build(Path(sys.argv[1]), Path(sys.argv[2]))

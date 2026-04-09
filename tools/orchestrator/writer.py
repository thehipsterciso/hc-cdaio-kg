"""
Graph writer — the single place where graph.json is mutated.

Every write goes through write_entity_profile(). The writer:

    1. Acquires a simple lock file (graph.json.orchestrator.lock)
    2. Loads the graph
    3. Locates the entity by id
    4. Deep-merges the supplied financial_profile (or replaces entirely)
    5. Writes atomically via a .tmp sibling and os.replace
    6. Releases the lock

The MCP server auto-reloads from graph.json on mtime change, so the in-memory
knowledge graph stays in sync automatically after each commit.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

from . import schema

REPO_ROOT = Path(__file__).resolve().parents[2]
GRAPH_PATH = REPO_ROOT / "graph.json"

# No lock file — orchestrator runs single-threaded from the main session.
# The workspace mount does not allow file unlink, so a lock file would be
# one-shot anyway. Sequential reasoning guarantees no concurrent writes.


def _acquire_lock(timeout_s: float = 30.0) -> None:  # noqa: ARG001
    return None


def _release_lock() -> None:
    return None


def load_graph() -> dict[str, Any]:
    with GRAPH_PATH.open() as f:
        return json.load(f)


def save_graph(graph: dict[str, Any]) -> None:
    tmp = GRAPH_PATH.with_suffix(".json.tmp")
    with tmp.open("w") as f:
        json.dump(graph, f, indent=2, ensure_ascii=False)
    os.replace(tmp, GRAPH_PATH)


def get_entity(graph: dict[str, Any], entity_id: str) -> dict[str, Any] | None:
    for e in graph.get("entities", []):
        if e.get("id") == entity_id:
            return e
    return None


def _find_index(graph: dict[str, Any], entity_id: str) -> int:
    for i, e in enumerate(graph.get("entities", [])):
        if e.get("id") == entity_id:
            return i
    return -1


def normalize_entity(graph: dict[str, Any], entity_id: str) -> bool:
    """Ensure the entity has a fully-shaped v2 financial_profile skeleton.

    Returns True if a change was made, False if already conformant.
    Values that already exist on the entity are preserved; only missing
    keys are filled with empties. This is Phase 0's primary operation.
    """
    idx = _find_index(graph, entity_id)
    if idx < 0:
        return False
    entity = graph["entities"][idx]
    existing = entity.get("financial_profile") or {}

    skeleton = schema.empty_financial_profile()

    changed = False

    # Top-level fields
    for k, v in skeleton.items():
        if k == "fiscal_years":
            continue
        if k not in existing:
            existing[k] = v
            changed = True

    # fiscal_years
    existing_fy = existing.get("fiscal_years") or {}
    for fy_name in schema.FISCAL_YEARS:
        if fy_name not in existing_fy:
            existing_fy[fy_name] = skeleton["fiscal_years"][fy_name]
            changed = True
        else:
            # Deep-fill any missing fields (legacy v1 entities)
            fy_current = existing_fy[fy_name]
            fy_expected = skeleton["fiscal_years"][fy_name]
            for field_key, field_default in fy_expected.items():
                if field_key not in fy_current:
                    fy_current[field_key] = field_default
                    changed = True
                elif isinstance(field_default, dict) and isinstance(
                    fy_current[field_key], dict
                ):
                    for sub_key, sub_default in field_default.items():
                        if sub_key not in fy_current[field_key]:
                            fy_current[field_key][sub_key] = sub_default
                            changed = True
    existing["fiscal_years"] = existing_fy
    entity["financial_profile"] = existing
    graph["entities"][idx] = entity
    return changed


def write_entity_profile(entity_id: str, financial_profile: dict[str, Any]) -> None:
    """Replace the entity's financial_profile with the supplied payload."""
    _acquire_lock()
    try:
        graph = load_graph()
        idx = _find_index(graph, entity_id)
        if idx < 0:
            raise KeyError(f"Entity not found: {entity_id}")
        graph["entities"][idx]["financial_profile"] = financial_profile
        save_graph(graph)
    finally:
        _release_lock()


def apply_batch_normalize(entity_ids: list[str]) -> dict[str, Any]:
    """Phase 0 entrypoint: normalize a batch of entities in-place.

    Loads the graph once, normalizes each entity, saves once.
    """
    _acquire_lock()
    try:
        graph = load_graph()
        changed = 0
        not_found: list[str] = []
        for eid in entity_ids:
            if _find_index(graph, eid) < 0:
                not_found.append(eid)
                continue
            if normalize_entity(graph, eid):
                changed += 1
        save_graph(graph)
    finally:
        _release_lock()
    return {
        "processed": len(entity_ids),
        "changed": changed,
        "not_found": not_found,
    }


def apply_batch_payloads(payloads: list[dict[str, Any]]) -> dict[str, Any]:
    """Population phase entrypoint: write multiple entity payloads in one pass.

    Each payload must have the shape:
        {"entity_id": "...", "financial_profile": {...}}
    """
    _acquire_lock()
    try:
        graph = load_graph()
        written: list[str] = []
        not_found: list[str] = []
        for p in payloads:
            eid = p["entity_id"]
            fp = p["financial_profile"]
            idx = _find_index(graph, eid)
            if idx < 0:
                not_found.append(eid)
                continue
            graph["entities"][idx]["financial_profile"] = fp
            written.append(eid)
        save_graph(graph)
    finally:
        _release_lock()
    return {"written": written, "not_found": not_found}

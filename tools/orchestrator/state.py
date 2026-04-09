"""
Orchestrator state management.

State lives at audit/orchestrator/state.json. It is the single source of
truth for "where are we". Every action that changes progress must call
`save()`. Every session resume begins with `load()`.

The state machine has these moving parts:

    phase_index          current 0-10 phase number (0 = normalization, 1-10 = population phases)
    phase_name           human-readable phase label
    batch_index          which 10-entity batch within the phase we are on
    completed_entities   set of entity IDs fully populated and committed
    failed_entities      set of entity IDs that errored and need human review
    skipped_entities     set of entity IDs intentionally skipped (with reason)
    last_commit_sha      git SHA after the most recent batch commit
    last_checkpoint      ISO timestamp of the most recent checkpoint write
    session_log          append-only log of session boundaries (start, pause, resume)
    validation_log       append-only log of validation runs
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
STATE_DIR = REPO_ROOT / "audit" / "orchestrator"
STATE_PATH = STATE_DIR / "state.json"
PROGRESS_PATH = STATE_DIR / "phase_progress.json"
ERRORS_LOG = STATE_DIR / "errors" / "errors.log"


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _default_state() -> dict[str, Any]:
    return {
        "version": "0.1.0",
        "created_at": now_iso(),
        "updated_at": now_iso(),
        "phase_index": 0,
        "phase_name": "normalize_skeletons",
        "batch_index": 0,
        "current_batch_ids": [],
        "completed_entities": [],
        "failed_entities": [],
        "skipped_entities": [],
        "last_commit_sha": None,
        "last_checkpoint": None,
        "session_log": [],
        "validation_log": [],
        "totals": {
            "entities_total": 0,
            "entities_done": 0,
            "batches_committed": 0,
        },
    }


def load() -> dict[str, Any]:
    if not STATE_PATH.exists():
        s = _default_state()
        save(s)
        return s
    with STATE_PATH.open() as f:
        return json.load(f)


def save(state: dict[str, Any]) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    state["updated_at"] = now_iso()
    tmp = STATE_PATH.with_suffix(".json.tmp")
    with tmp.open("w") as f:
        json.dump(state, f, indent=2, sort_keys=False)
    os.replace(tmp, STATE_PATH)


def log_session_event(state: dict[str, Any], event: str, detail: str = "") -> None:
    state["session_log"].append(
        {"ts": now_iso(), "event": event, "detail": detail}
    )


def log_validation(state: dict[str, Any], batch_id: str, result: dict[str, Any]) -> None:
    state["validation_log"].append(
        {"ts": now_iso(), "batch_id": batch_id, "result": result}
    )


def log_error(message: str) -> None:
    ERRORS_LOG.parent.mkdir(parents=True, exist_ok=True)
    with ERRORS_LOG.open("a") as f:
        f.write(f"[{now_iso()}] {message}\n")


def mark_completed(state: dict[str, Any], entity_ids: list[str]) -> None:
    done = set(state["completed_entities"])
    done.update(entity_ids)
    state["completed_entities"] = sorted(done)
    state["totals"]["entities_done"] = len(done)


def write_progress_summary(state: dict[str, Any], phases: list[dict[str, Any]]) -> None:
    """Write a lightweight phase_progress.json for dispatch viewing."""
    summary = {
        "updated_at": now_iso(),
        "phase_index": state["phase_index"],
        "phase_name": state["phase_name"],
        "batch_index": state["batch_index"],
        "entities_done": state["totals"]["entities_done"],
        "entities_total": state["totals"]["entities_total"],
        "last_commit_sha": state["last_commit_sha"],
        "last_checkpoint": state["last_checkpoint"],
        "phases": phases,
    }
    PROGRESS_PATH.parent.mkdir(parents=True, exist_ok=True)
    with PROGRESS_PATH.open("w") as f:
        json.dump(summary, f, indent=2)

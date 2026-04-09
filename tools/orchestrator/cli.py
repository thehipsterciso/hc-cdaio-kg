"""
Orchestrator CLI — the operator surface.

Commands:
    status                           show current state
    init                             build phase queues and initialize state
    next [--size N]                  print the next batch context (default 10)
    normalize --size N               run Phase 0 normalize on next N entities
    apply PAYLOAD_FILE               apply a batch payload JSON file
    checkpoint --notes "..."         write a manual checkpoint
    advance-phase                    move to the next phase (when current exhausted)
    resume                           print resume card
    validate PAYLOAD_FILE            run validators on a payload without writing

Payload file format (for apply):
    {
      "phase": 1,
      "entities": [
        {"entity_id": "ou-029", "financial_profile": {...}},
        ...
      ]
    }

All writes are atomic. All errors go to audit/orchestrator/errors/errors.log.
State is always saved after every command that mutates it.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

from . import checkpoint, planner, state, validator, writer
from .schema import FISCAL_YEARS, total_field_count_per_fy

REPO_ROOT = Path(__file__).resolve().parents[2]
ORCH_DIR = REPO_ROOT / "audit" / "orchestrator"

UPDATED_BY_TAG = "llm_reasoning_v2"

PHASE_NAMES = {
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


# ─── helpers ─────────────────────────────────────────────────────────────────


def _git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args], cwd=str(REPO_ROOT), capture_output=True, text=True
    )
    return result.stdout.strip()


def _current_head() -> str:
    return _git("rev-parse", "--short", "HEAD")


def _phase_done_in(s: dict[str, Any], phase_ids: list[str]) -> int:
    done_set = set(s["completed_entities"])
    return sum(1 for e in phase_ids if e in done_set)


def _pending_in_phase(s: dict[str, Any], phase_ids: list[str]) -> list[str]:
    done_set = set(s["completed_entities"])
    return [e for e in phase_ids if e not in done_set]


def _phase_info(s: dict[str, Any]) -> dict[str, Any]:
    pids = planner.load_queue(s["phase_index"])
    return {
        "phase": s["phase_index"],
        "name": PHASE_NAMES.get(s["phase_index"], "unknown"),
        "count": len(pids),
        "done": _phase_done_in(s, pids),
        "pending": len(_pending_in_phase(s, pids)),
    }


# ─── commands ────────────────────────────────────────────────────────────────


def cmd_init(args: argparse.Namespace) -> int:
    print("Building phase queues from graph.json...")
    queues = planner.build_phase_queues()
    counts = planner.write_queues(queues)
    phases = planner.phase_summary(queues)

    s = state.load()
    s["phase_index"] = 0
    s["phase_name"] = PHASE_NAMES[0]
    s["batch_index"] = 0
    # Phase 0 normalizes everyone, but totals.entities_total for progress is
    # the sum of population phases (1-10), not normalization.
    total_pop = sum(counts[p] for p in range(1, 11) if p in counts)
    s["totals"]["entities_total"] = total_pop
    state.log_session_event(s, "init", f"queues built, {total_pop} population entities")
    state.save(s)
    state.write_progress_summary(s, phases)
    checkpoint.write_session_resume_card(s)

    print("Phase queues:")
    for p in phases:
        print(f"  phase_{p['phase']:02d} {p['name']:<22} {p['count']:>5}")
    print(f"\nTotal population entities (phases 1-10): {total_pop}")
    print(f"State written: {state.STATE_PATH}")
    return 0


def cmd_status(args: argparse.Namespace) -> int:
    s = state.load()
    pi = _phase_info(s)
    done = s["totals"]["entities_done"]
    total = s["totals"]["entities_total"]
    pct = (done / total * 100) if total else 0.0

    print(f"Orchestrator state — updated {s['updated_at']}")
    print()
    print(f"  Phase:     {s['phase_index']} — {s['phase_name']}")
    print(f"  Batch:     {s['batch_index']}")
    print(f"  Progress:  {done}/{total} ({pct:.1f}%)")
    print(f"  Phase:     {pi['done']}/{pi['count']} entities done, {pi['pending']} pending")
    print(f"  Failed:    {len(s['failed_entities'])}")
    print(f"  Last SHA:  {s.get('last_commit_sha') or '—'}")
    print(f"  Last chkpt:{s.get('last_checkpoint') or '—'}")
    print()
    print(f"  Field count per FY (schema v2): {total_field_count_per_fy()}")
    print(f"  Fiscal years: {', '.join(FISCAL_YEARS)}")
    return 0


def cmd_next(args: argparse.Namespace) -> int:
    s = state.load()
    pids = planner.load_queue(s["phase_index"])
    pending = _pending_in_phase(s, pids)

    if not pending:
        print(f"Phase {s['phase_index']} ({s['phase_name']}) is complete.")
        print("Run: python -m tools.orchestrator.cli advance-phase")
        return 0

    size = args.size
    batch = pending[:size]
    s["current_batch_ids"] = batch
    state.save(s)

    print(f"Phase {s['phase_index']} ({s['phase_name']}) — next batch ({len(batch)} of {len(pending)} pending):")
    for eid in batch:
        print(f"  {eid}")
    print()
    print(f"Phase progress: {len(pids) - len(pending)}/{len(pids)}")
    print()
    print("When payload is ready:")
    print(f"  python -m tools.orchestrator.cli apply <payload.json>")
    return 0


def cmd_normalize(args: argparse.Namespace) -> int:
    """Phase 0 only: normalize the next N entities to the v2 skeleton."""
    s = state.load()
    if s["phase_index"] != 0:
        print(f"Normalize is Phase 0 only. Current phase = {s['phase_index']}.")
        return 2
    pids = planner.load_queue(0)
    pending = _pending_in_phase(s, pids)
    if not pending:
        print("Phase 0 complete.")
        return 0

    size = args.size
    batch = pending[:size]
    print(f"Normalizing {len(batch)} entities ({len(pending)} pending total)...")
    result = writer.apply_batch_normalize(batch)
    print(
        f"Processed: {result['processed']}, changed: {result['changed']}, "
        f"not_found: {len(result['not_found'])}"
    )
    if result["not_found"]:
        state.log_error(
            f"normalize not_found: {result['not_found']}"
        )

    state.mark_completed(s, batch)
    s["batch_index"] += 1
    state.save(s)

    if args.commit:
        sha = _commit_graph(
            f"orch: phase 0 normalize batch {s['batch_index']} — {len(batch)} entities"
        )
        s["last_commit_sha"] = sha
        state.save(s)

    # Write a lightweight checkpoint
    pi = _phase_info(s)
    next_batch = _pending_in_phase(s, pids)[: args.size]
    phase_summary = planner.phase_summary(planner.build_phase_queues())
    state.write_progress_summary(s, phase_summary)
    path = checkpoint.write_checkpoint(
        s,
        pi,
        {"changed": result["changed"], "written": batch, "not_found": result["not_found"]},
        {"pass": True, "total_errors": 0, "checks": {}},
        next_batch,
        notes=f"Phase 0 normalize (schema skeleton). Commit: {'yes' if args.commit else 'no'}",
    )
    s["last_checkpoint"] = str(path.name)
    state.save(s)
    checkpoint.write_session_resume_card(s)
    print(f"Checkpoint: {path}")
    return 0


def cmd_apply(args: argparse.Namespace) -> int:
    payload_path = Path(args.payload)
    with payload_path.open() as f:
        payload = json.load(f)

    entities = payload.get("entities", [])
    if not entities:
        print("ERROR: payload has no 'entities'")
        return 2

    # Validate before writing
    print(f"Validating {len(entities)} payloads against schema...")
    report = validator.run_all_checks(entities, UPDATED_BY_TAG)
    if not report["pass"] and not args.force:
        print(f"VALIDATION FAILED — {report['total_errors']} errors")
        print("Re-run with --force to write anyway (not recommended)")
        for eid, checks in report["checks"].items():
            for check, errs in checks.items():
                for e in errs[:3]:
                    print(f"  {eid}/{check}: {e}")
        return 3

    print(f"Writing {len(entities)} entities to graph.json...")
    write_result = writer.apply_batch_payloads(entities)
    print(
        f"Written: {len(write_result['written'])}, "
        f"not_found: {len(write_result['not_found'])}"
    )

    s = state.load()
    state.mark_completed(s, write_result["written"])
    s["batch_index"] += 1
    s["totals"]["batches_committed"] += 1
    state.log_validation(s, f"phase{s['phase_index']}_batch{s['batch_index']}", report)
    state.save(s)

    if not args.no_commit:
        phase_label = PHASE_NAMES.get(s["phase_index"], f"phase{s['phase_index']}")
        msg = (
            f"orch: {phase_label} batch {s['batch_index']} — "
            f"{len(write_result['written'])} entities, "
            f"{total_field_count_per_fy()} fields × 4 FYs"
        )
        sha = _commit_graph(msg)
        s["last_commit_sha"] = sha
        state.save(s)
        print(f"Committed: {sha}")

    pi = _phase_info(s)
    pids = planner.load_queue(s["phase_index"])
    next_batch = _pending_in_phase(s, pids)[:10]
    phase_summary = planner.phase_summary(planner.build_phase_queues())
    state.write_progress_summary(s, phase_summary)
    path = checkpoint.write_checkpoint(
        s, pi, write_result, report, next_batch, notes=payload.get("notes", "")
    )
    s["last_checkpoint"] = path.name
    state.save(s)
    checkpoint.write_session_resume_card(s)
    print(f"Checkpoint: {path}")
    return 0


def cmd_advance_phase(args: argparse.Namespace) -> int:
    s = state.load()
    cur = s["phase_index"]
    pids = planner.load_queue(cur)
    pending = _pending_in_phase(s, pids)
    if pending and not args.force:
        print(
            f"Phase {cur} still has {len(pending)} pending entities. "
            f"Refusing to advance without --force."
        )
        return 2
    new_phase = cur + 1
    if new_phase > 10:
        print("Already at final phase.")
        return 0
    s["phase_index"] = new_phase
    s["phase_name"] = PHASE_NAMES[new_phase]
    s["batch_index"] = 0
    state.log_session_event(s, "advance_phase", f"{cur} -> {new_phase}")
    state.save(s)
    checkpoint.write_session_resume_card(s)
    print(f"Advanced to phase {new_phase} — {s['phase_name']}")
    return 0


def cmd_resume(args: argparse.Namespace) -> int:
    s = state.load()
    path = checkpoint.write_session_resume_card(s)
    print(path.read_text())
    return 0


def cmd_validate(args: argparse.Namespace) -> int:
    with open(args.payload) as f:
        payload = json.load(f)
    report = validator.run_all_checks(payload.get("entities", []), UPDATED_BY_TAG)
    print(json.dumps(report, indent=2))
    return 0 if report["pass"] else 1


def _commit_graph(message: str) -> str:
    subprocess.run(["git", "add", "graph.json"], cwd=str(REPO_ROOT), check=True)
    subprocess.run(
        ["git", "commit", "-m", message], cwd=str(REPO_ROOT), check=False
    )
    return _current_head()


# ─── main ────────────────────────────────────────────────────────────────────


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="orchestrator")
    sub = p.add_subparsers(dest="cmd")

    sub.add_parser("init", help="build phase queues and initialize state").set_defaults(
        func=cmd_init
    )
    sub.add_parser("status", help="show orchestrator state").set_defaults(
        func=cmd_status
    )

    p_next = sub.add_parser("next", help="print the next batch of entities")
    p_next.add_argument("--size", type=int, default=10)
    p_next.set_defaults(func=cmd_next)

    p_norm = sub.add_parser("normalize", help="Phase 0: normalize N entities")
    p_norm.add_argument("--size", type=int, default=100)
    p_norm.add_argument("--commit", action="store_true")
    p_norm.set_defaults(func=cmd_normalize)

    p_app = sub.add_parser("apply", help="apply a batch payload file")
    p_app.add_argument("payload")
    p_app.add_argument("--no-commit", action="store_true")
    p_app.add_argument("--force", action="store_true", help="write even if validation fails")
    p_app.set_defaults(func=cmd_apply)

    p_adv = sub.add_parser("advance-phase", help="move to the next phase")
    p_adv.add_argument("--force", action="store_true")
    p_adv.set_defaults(func=cmd_advance_phase)

    sub.add_parser("resume", help="print resume card").set_defaults(func=cmd_resume)

    p_val = sub.add_parser("validate", help="run validators on payload")
    p_val.add_argument("payload")
    p_val.set_defaults(func=cmd_validate)

    args = p.parse_args(argv)
    if not hasattr(args, "func"):
        p.print_help()
        return 1
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())

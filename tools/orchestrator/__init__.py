"""
hc-cdaio-kg Financial Population Orchestrator

A state-machine orchestrator driving the 10-phase financial profile population
effort described in FINANCIAL_POPULATION_PLAN.md. The orchestrator itself does
not reason about financial values — the main Claude session is the reasoning
engine. This package provides:

    - State management (resumable across sessions)
    - Phase planning (entity queues per phase)
    - Schema construction (v2 FieldValue skeleton)
    - Graph writer (direct graph.json edit)
    - Per-batch validators (enforcement mechanisms 1-6)
    - Checkpoint reporters (markdown for dispatch monitoring)

Workflow per batch:

    1. orchestrator.py status       → show where we are
    2. orchestrator.py next         → print the next batch context
    3. [main session reasons through each entity, writes JSON payloads]
    4. orchestrator.py apply        → validate + write + commit + checkpoint
    5. loop until phase complete
"""

__version__ = "0.1.0"

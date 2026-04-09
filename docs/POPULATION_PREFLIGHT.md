# Population Preflight — Mandatory Checklist

**Status:** Enforced gate. All seven gates must pass before any financial profile population work in hc-cdaio-kg.

**Purpose:** Prevent the three failure patterns that have recurred in this repo:
1. Carrying numbers forward from prior context without verifying against the graph.
2. Expanding a narrow fix into a documentation or planning exercise.
3. Template math dressed up as reasoning (e.g. `capex = revenue * 0.02`).

This file exists because those three patterns cost Thomas more time and frustration than doing it right the first time would. The gates are mechanical. If a gate fails, stop and report. Do not work around it.

---

## When this triggers

Any work in hc-cdaio-kg that involves:
- Populating or modifying `financial_profile` on any entity
- Writing, running, or editing a `phase<N>_payload.py` or `apply_phase<N>.py` script
- Any statement about entity counts, portfolio hierarchy, or phase scope
- Any change to `graph.json`

If the user's message touches any of the above, run this checklist before the first tool call that writes anything.

---

## Gate 1 — Verify scope against the actual graph

**Before stating any entity count, running any script, or agreeing to any scope:**

1. Query `graph.json` directly for the real entity counts.
2. If prior conversation context or the user message references a number (e.g. "177 sub_portfolios"), verify it against the query.
3. If the numbers do not match, STOP. Report the delta to the user. Do not proceed.

**Failure mode this prevents:** Phase Plan v1 referenced "177 sub_portfolios." The graph had 71. Nobody caught it until execution was attempted.

**Minimum verification query:**

```python
import json
from collections import Counter
with open('/sessions/gracious-laughing-gauss/mnt/hc-cdaio-kg/graph.json') as f:
    g = json.load(f)
print(Counter(e.get('entity_type') for e in g['entities']))
```

---

## Gate 2 — Confirm the minimum viable ask

**Before writing any code or any document:**

1. State the user's ask in one sentence.
2. State the minimum executable version of that ask in one sentence.
3. If those two differ, or if scope is ambiguous, use AskUserQuestion. Do not guess.
4. Do NOT write a planning document, a phase plan, a spec, or any .md file unless the user explicitly asked for one.

**Failure mode this prevents:** "Fix Phase 3" became a 380-line phase plan rewrite. The fix was one line.

**Heuristic:** If the diff between "what they asked" and "what I'm about to do" is more than a factor of 3× in scope, stop and ask.

---

## Gate 3 — Per-field reasoning, not template math

**Before writing any payload dict:**

For each entity × each fiscal year × each field, answer this question: *what specific fact about this business in this year justifies this value?*

**Forbidden patterns:**
- `capex = revenue * 0.02` — without a cited reason 0.02 is the right number
- `opex_exhc = revenue * 0.12` — same
- `sbc = revenue * 0.03` — same
- `bookings = revenue * 1.3` — same
- Any multiplier applied uniformly across years without reasoning about how the business changed year to year

**Required pattern:**
Each value has a one- to three-sentence justification captured in the `source` field of the FieldValue. The justification references a specific fact (SEC filing line, press release date, partnership announcement, industry compensation data, etc.) OR a reasoning chain from already-anchored facts.

If you catch yourself writing a parameterized `year_payload(entity, year)` function with shared multipliers, STOP. Write per-year dicts instead. The DRY principle does not apply when each year is a different business state.

**Failure mode this prevents:** First Phase 3 payload attempt was full of `rev * 0.XX` template math with no per-year reasoning. Scrapped and rewritten.

---

## Gate 4 — Tier honesty

**For every FieldValue, default to the lower tier, not the higher one:**

| Tier | What qualifies |
|---|---|
| T1 | SEC filing line item OR schema structural default (e.g. `period_type = "fiscal_year"`) OR hard conceptual zero (e.g. hardware = $0 on a software portfolio) |
| T2 | Strong public inference — 10-K commentary, well-documented industry cost structure, press releases with financial detail |
| T3 | Reasoned inference from multiple public facts, BLS data, partnership disclosures, named-segment commentary |
| T4 | Working hypothesis, forecast, uncited industry heuristic |

Do not inflate tiers to make a profile look more confident than it is. If you cannot name a document in `source_document`, it is not T1 or T2.

**Failure mode this prevents:** FAIR values were originally labeled T3 in places they should have been T4 — there is no SEC disclosure of FAIR at all.

---

## Gate 5 — NULL bar confirmation

**Before populating any balance sheet or below-the-line field:**

1. Confirm the entity's perspective: STANDALONE or CONSOLIDATED?
2. If STANDALONE (product_portfolio): the six NULL-bar fields stay NULL with `method=REFERENCE`:
   - `interest_expense`
   - `debt_obligations`
   - `balance_sheet.cash`
   - `balance_sheet.accounts_receivable` (and all four aging buckets)
   - `balance_sheet.accounts_payable`
   - `balance_sheet.equity`
   - Plus `balance_sheet.debt`
3. Plus the seven `contract_detail` fields are REF_NULL at root segment level.
4. If CONSOLIDATED (organizational_unit at root or segment BU): populate the NULL-bar fields — consolidation brings them into scope.

Do NOT default to populating everything. Do NOT default to NULL for fields that *are* applicable.

**Failure mode this prevents:** Before the NULL bar was locked, every iteration had inconsistent NULL treatment across STANDALONE vs CONSOLIDATED. The locked rule exists because it was a repeated friction point.

---

## Gate 6 — Proof plan before merge

**Before running any `apply_phase<N>.py` script:**

1. State which 2 random entities × years will be dumped to a proof file.
2. Use a seeded random selection so the choice is reproducible and honest.
3. Proof file must include, for every field: `value`, `confidence_tier`, `method`, `source`, `source_document`, `parent_field`, `allocation_pct`, `allocation_basis`, `formula`, `input_fields`.
4. Write the proof file to `phase<N>_proof_<entities>.txt` in the repo root.
5. Halt for user review before advancing to the next phase.

**Do not** present summary tables instead of field dumps. The user has stated this explicitly: "sumamring them does not help me."

---

## Gate 7 — Document creation gate

**Before creating any new `.md` file in this repo:**

1. Did the user explicitly ask for a document? If not, STOP.
2. Is the content going to exceed 50 lines? If yes and the user did not explicitly ask, STOP.
3. Would a one-sentence report to the user serve the same purpose? If yes, do that instead.

**Failure mode this prevents:** "Fix the phase plan" became `PHASE_PLAN_v2.md` — a 380-line document that was never asked for. The instinct to document is often procrastination dressed up as thoroughness.

---

## How to run this checklist

At the start of any qualifying task:

1. Read this file in full (required — do not skim).
2. State in the reply: "Preflight: Gates 1–7 loaded." This is the explicit acknowledgment that the checklist is live for this task.
3. Work through the gates in order. Each gate is a decision point, not a formality.
4. If any gate fails, report the failure and stop.
5. On completion, state which gates were cleared and which were not applicable.

The gates are mechanical, not aesthetic. The user does not care about the justification for skipping them. If a gate is skipped, the work does not ship.

---

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-04-09 | Initial version. Written after three successive failure modes in a single session: scope fabrication, document over-reach, template math. |

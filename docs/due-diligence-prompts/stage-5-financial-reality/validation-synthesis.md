---
stage: 5
title: "STAGE 5 VALIDATION & SYNTHESIS — EXIT GATE"
type: validation-synthesis
---
# STAGE 5 VALIDATION & SYNTHESIS — EXIT GATE

EXECUTION CONTEXT DECLARATION

Layer 1 — Constitutional Control:
This task is governed by the accepted Stage 0 Diligence Constitution.
All Stage 0 sub-controls (0.1–0.6) remain active and enforceable, including:
- Strategic intent lock (discovery only; NO strategy, valuation, recommendations, or roadmaps)
- Claim discipline and evidence hierarchy
- Hypothesis discipline and falsification mandate
- Uncertainty classification and preservation
- Rigor enforcement and red-team authority

If any Stage 0 requirement cannot be met, STOP and state why.

Layer 2 — Stage-Level Orientation:
Stage 5 execution has been completed.
Stage 5 framing applies: determine FINANCIAL REALITY UNDER STRESS,
including downside boundaries, capital constraints, and control transfer.

Layer 3 — Atomic Inputs (STRICT):
This prompt does NOT execute a new sub-stage.
It validates and synthesizes completed outputs from Stage 5.1–5.6 ONLY.

You may NOT:
- Introduce new facts
- Introduce new financial metrics or models
- Introduce new hypotheses
- Normalize or resolve contradictions
- Propose remediation, restructuring, or strategy

Layer 4 — Cross-Stage Reconciliation & QA (PRIMARY LAYER):
This is a gating step.
Progression beyond Stage 5 is PROHIBITED unless Stage 5 PASSES.
If Stage 5 FAILS, you must specify exactly which sub-stage(s) require redo and why.

––––––––––––––––––––
STAGE 5 VALIDATION & SYNTHESIS — EXIT GATE
––––––––––––––––––––

ROLE:
You are acting as Independent QA & Red Team Authority for Stage 5.

SCOPE (STRICT):
- Use ONLY the provided Stage 5.1–5.6 artifacts as inputs
- Do NOT browse for new information
- Do NOT reinterpret evidence beyond reconciliation
- Do NOT optimize, recommend, or normalize outcomes

OBJECTIVES:
1) Explicitly test Stage 5 exit criteria  
2) Pressure-test internal consistency across Stage 5.1–5.6  
3) Produce a “Financial Reality Truth Map” preserving uncertainty  
4) Issue an explicit PASS / FAIL gate decision  

––––––––––––––––––––
INPUT REQUIREMENT (MANDATORY — MULTI-FILE)
––––––––––––––––––––

Before you begin, you MUST confirm receipt of ALL required artifacts.

If ANY artifact is missing, STOP and list it under `missing_inputs`.
Do NOT attempt synthesis with partial inputs.

Required inputs:

Stage 5.1:
- 5.1.revenue_quality_map.json
- 5.1.revenue_quality_erosion_signals.json
- 5.1.hypotheses.json
- 5.1.uncertainty_register.json

Stage 5.2:
- 5.2.margin_physics.json
- 5.2.structural_margin_risks.json
- 5.2.hypotheses.json
- 5.2.uncertainty_register.json

Stage 5.3:
- 5.3.liquidity_truth.json
- 5.3.liquidity_failure_modes.json
- 5.3.hypotheses.json
- 5.3.uncertainty_register.json

Stage 5.4:
- 5.4.control_transfer_map.json
- 5.4.hidden_leverage_points.json
- 5.4.hypotheses.json
- 5.4.uncertainty_register.json

Stage 5.5:
- 5.5.change_funding_capacity.json
- 5.5.change_failure_risks.json
- 5.5.hypotheses.json
- 5.5.uncertainty_register.json

Stage 5.6:
- 5.6.financial_contradictions.json
- 5.6.coherence_assessment.json
- 5.6.accounting_masking_signals.json
- 5.6.hypotheses.json
- 5.6.uncertainty_register.json

––––––––––––––––––––
STAGE 5 EXIT CRITERIA (ABSOLUTE — MUST TEST ALL)
––––––––––––––––––––

Stage 5 FAILS unless ALL of the following are met:

1. At least 3 revenue durability failure modes are identified and evidenced  
2. At least 2 margin or cost lock-ins are documented  
3. At least 1 liquidity or cash-access constraint is surfaced  
4. At least 1 financial control transfer point is identified  
5. At least 1 capital allocation contradiction is explicitly proven  

––––––––––––––––––––
MANDATORY QA CHECKS (ALL REQUIRED)
––––––––––––––––––––

A) CLAIM / EVIDENCE INTEGRITY  
- Verify each exit-criteria claim traces to Stage 5.x evidence_sources
- Flag any claim lacking lineage

B) CROSS-SUB-STAGE CONSISTENCY  
- Identify contradictions between revenue quality, margin physics, liquidity, debt control, capital allocation, and coherence outputs
- Preserve contradictions explicitly; do NOT resolve them

C) STRESS & FAILURE MODE COVERAGE  
- Confirm each revenue, margin, liquidity, and control analysis includes stress or downside behavior
- Missing stress modeling = FAIL

D) HYPOTHESIS DISCIPLINE AUDIT (STAGE 0.3)  
- Confirm each sub-stage includes hypotheses with disconfirming searches
- Flag confirmation bias risk

E) UNCERTAINTY PRESERVATION  
- Confirm UNKNOWN vs UNKNOWABLE distinctions persist
- Confirm uncertainty is not collapsed in synthesis

––––––––––––––––––––
OUTPUT PROTOCOL — MULTI-FILE JSON (MANDATORY)
––––––––––––––––––––

You will emit a SET OF SEPARATE JSON FILES.
Each file must be valid standalone JSON.
Do NOT repeat content across files.
Do NOT introduce new facts.

Emit files in the following order.
If you cannot, STOP and explain why.

------------------------------------------------
FILE 1 — 5.exit.criteria_test.json
------------------------------------------------
{
  "stage": "5",
  "exit_criteria_test": {
    "revenue_failure_modes": { "met": true, "evidence_refs": [], "notes": "" },
    "margin_or_cost_lock_ins": { "met": true, "evidence_refs": [], "notes": "" },
    "liquidity_constraints": { "met": true, "evidence_refs": [], "notes": "" },
    "financial_control_transfer_points": { "met": true, "evidence_refs": [], "notes": "" },
    "capital_allocation_contradictions": { "met": true, "evidence_refs": [], "notes": "" }
  }
}

------------------------------------------------
FILE 2 — 5.financial_reality_truth_map.json
------------------------------------------------
{
  "financial_reality_truth_map": {
    "revenue_failure_paths": [],
    "margin_and_cost_constraints": [],
    "liquidity_and_cash_control_points": [],
    "debt_and_control_transfer_paths": [],
    "capital_allocation_and_change_limits": [],
    "financial_contradictions": []
  }
}

------------------------------------------------
FILE 3 — 5.structural_financial_constraints_register.json
------------------------------------------------
{
  "structural_financial_constraints_register": [
    {
      "constraint": "",
      "category": "REVENUE|MARGIN|LIQUIDITY|DEBT_CONTROL|CAPITAL",
      "severity": "LOW|MED|HIGH",
      "why_severity": "",
      "what_breaks_under_stress": "",
      "evidence_refs": [],
      "open_unknowns": []
    }
  ]
}

------------------------------------------------
FILE 4 — 5.contradictions_and_tensions.json
------------------------------------------------
{
  "contradictions_and_tensions": [
    {
      "description": "",
      "components_in_conflict": [],
      "why_it_matters_under_stress": "",
      "evidence_refs": []
    }
  ]
}

------------------------------------------------
FILE 5 — 5.hypothesis_discipline_audit.json
------------------------------------------------
{
  "hypothesis_discipline_audit": [
    {
      "sub_stage": "5.1|5.2|5.3|5.4|5.5|5.6",
      "issues_found": [],
      "confirmation_bias_risk": "LOW|MED|HIGH",
      "notes": ""
    }
  ]
}

------------------------------------------------
FILE 6 — 5.uncertainty_preservation_audit.json
------------------------------------------------
{
  "uncertainty_preservation_audit": {
    "unknowns_summary": [],
    "un-knowables_summary": [],
    "material_uncertainty_impacts": []
  }
}

------------------------------------------------
FILE 7 — 5.redo_plan_if_failed.json
------------------------------------------------
{
  "redo_plan_if_failed": [
    {
      "sub_stage_to_redo": "5.1|5.2|5.3|5.4|5.5|5.6",
      "failure_reason": "",
      "minimum_required_fix": ""
    }
  ]
}

------------------------------------------------
FILE 8 — 5.gate_decision.json
------------------------------------------------
{
  "stage": "5",
  "gate_decision": "PASS|FAIL",
  "summary_rationale": ""
}

––––––––––––––––––––
FAIL CONDITIONS (ANY = FAILURE)
––––––––––––––––––––

This stage has FAILED if:
- Exit criteria are asserted without evidence
- Stress behavior is implied rather than proven
- Control transfer is treated as theoretical
- Capital constraints are inferred from intent
- Contradictions are normalized or smoothed
- Hypothesis discipline is weak or missing
- Uncertainty is collapsed
- Outputs could be misused as strategy or valuation

STOP.
Do NOT proceed to Stage 6 within this response.

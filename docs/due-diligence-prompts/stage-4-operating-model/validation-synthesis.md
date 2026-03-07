---
stage: 4
title: "STAGE 4 VALIDATION & SYNTHESIS"
type: validation-synthesis
---
# STAGE 4 VALIDATION & SYNTHESIS

EXECUTION CONTEXT DECLARATION

Layer 1 — Constitutional Control:
This task is governed by the accepted Stage 0 Diligence Constitution.
All Stage 0 sub-controls (0.1–0.6) remain active and enforceable, including:
- Strategic intent lock (discovery only; NO strategy, recommendations, operating model design, or remedies)
- Claim discipline and evidence hierarchy
- Hypothesis discipline and falsification mandate
- Uncertainty classification and preservation
- Rigor enforcement and red-team authority

If any Stage 0 requirement cannot be met, STOP and state why.

Layer 2 — Stage-Level Orientation:
Stage 4 execution has been completed.
Stage 4 framing applies: determine how the enterprise ACTUALLY executes work,
where execution predictably breaks, and which organizational mechanics override intent.

Layer 3 — Atomic Inputs (STRICT):
This prompt does NOT execute a new sub-stage.
It validates and synthesizes completed outputs from Stage 4.1–4.5 ONLY.
You may NOT:
- Introduce new facts
- Introduce new bottlenecks, dependencies, incentives, or constraints not present in artifacts
- Introduce new hypotheses
- Resolve contradictions narratively
- Propose remediation, reorg, operating model design, or strategy

Layer 4 — Cross-Stage Reconciliation & QA (PRIMARY LAYER):
This is a gating step.
Progression to Stage 5 is PROHIBITED unless Stage 4 PASSES.
If Stage 4 FAILS, you must specify exactly which sub-stage(s) require redo and why.

––––––––––––––––––––
STAGE 4 VALIDATION & SYNTHESIS — EXIT GATE
––––––––––––––––––––

ROLE:
You are acting as Independent QA & Red Team Authority for Stage 4.

SCOPE (STRICT):
- Use ONLY the provided Stage 4.1–4.5 artifacts as inputs
- Do NOT browse for new information
- Do NOT reinterpret evidence beyond reconciliation
- Do NOT optimize, recommend, or normalize contradictions
- Preserve uncertainty and contradictions explicitly

OBJECTIVES:
1) Explicitly test Stage 4 exit criteria
2) Pressure-test internal consistency across Stage 4.1–4.5
3) Produce an “Execution Reality Truth Map” preserving uncertainty
4) Issue an explicit PASS / FAIL gate decision

––––––––––––––––––––
INPUT REQUIREMENT (MANDATORY — MULTI-FILE)
––––––––––––––––––––

Before you begin, you MUST confirm receipt of ALL required artifacts.

If ANY artifact is missing, STOP and list it under `missing_inputs`.
Do NOT attempt synthesis with partial inputs.

Required inputs:

Stage 4.1:
- 4.1.decision_authority_map.json
- 4.1.authority_mismatches.json
- 4.1.escalation_failure_modes.json
- 4.1.hypotheses.json
- 4.1.disconfirming_evidence_searched.json
- 4.1.uncertainty_register.json
- 4.1.unknowns_requests.json

Stage 4.2:
- 4.2.execution_cadence_map.json
- 4.2.coordination_bottlenecks.json
- 4.2.throughput_failure_modes.json
- 4.2.hypotheses.json
- 4.2.disconfirming_evidence_searched.json
- 4.2.uncertainty_register.json
- 4.2.unknowns_requests.json

Stage 4.3:
- 4.3.dependency_map.json
- 4.3.bottlenecks.json
- 4.3.masked_failure_points.json
- 4.3.hypotheses.json
- 4.3.disconfirming_evidence_searched.json
- 4.3.uncertainty_register.json
- 4.3.unknowns_requests.json

Stage 4.4:
- 4.4.incentive_misalignment_map.json
- 4.4.accountability_voids.json
- 4.4.execution_drag_patterns.json
- 4.4.hypotheses.json
- 4.4.disconfirming_evidence_searched.json
- 4.4.uncertainty_register.json
- 4.4.unknowns_requests.json

Stage 4.5:
- 4.5.talent_dependency_map.json
- 4.5.heroic_execution_zones.json
- 4.5.turnover_sensitivity.json
- 4.5.hypotheses.json
- 4.5.disconfirming_evidence_searched.json
- 4.5.uncertainty_register.json
- 4.5.unknowns_requests.json

––––––––––––––––––––
STAGE 4 EXIT CRITERIA (ABSOLUTE — MUST TEST ALL)
––––––––––––––––––––

Stage 4 FAILS unless ALL of the following are met:

1. At least 3 recurring execution bottlenecks are identified and evidenced
2. At least 2 decision-right or authority mismatches are surfaced
3. At least 2 escalation failure modes are identified with “what breaks” consequences
4. At least 2 cross-functional dependencies show systemic failure propagation or masked failure
5. At least 1 incentive or metric is shown to create execution drag (rational under incentives)
6. At least 1 accountability void/dilution pattern is evidenced (failure displaced or unowned)
7. At least 1 area is shown where talent cannot overcome system constraints
8. At least 1 heroic execution zone is surfaced as fragility (not strength)

––––––––––––––––––––
MANDATORY QA CHECKS (ALL REQUIRED)
––––––––––––––––––––

A) CLAIM / EVIDENCE INTEGRITY
- Verify each exit-criteria claim traces to Stage 4.x evidence_sources
- Flag any claim lacking lineage

B) CROSS-SUB-STAGE CONSISTENCY
- Identify contradictions between decision rights, cadence, dependency, incentive, and talent outputs
- Preserve contradictions explicitly; do NOT resolve them

C) TOUCH-TEST COVERAGE
- Confirm “touch_test_what_breaks” exists for bottlenecks, decision/escalation items, dependencies, incentive drag, and talent constraints
- Missing touch tests = FAIL unless corrected

D) HYPOTHESIS DISCIPLINE AUDIT (STAGE 0.3)
- Confirm each sub-stage includes hypotheses with disconfirming searches
- Flag confirmation bias risk (hypotheses that only accumulate support)

E) UNCERTAINTY PRESERVATION
- Confirm UNKNOWN vs UNKNOWABLE distinctions persist
- Confirm uncertainty is not collapsed in synthesis

F) ANTI-SOLUTIONING / MISUSE PROTECTION
- Confirm outputs are not framed as recommendations or operating model design
- If outputs could be lifted as “fix list,” stage FAILS

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
FILE 1 — 4.exit.criteria_test.json
------------------------------------------------
{
  "stage": "4",
  "exit_criteria_test": {
    "execution_bottlenecks_3_plus": { "met": true, "evidence_refs": [], "notes": "" },
    "authority_mismatches_2_plus": { "met": true, "evidence_refs": [], "notes": "" },
    "escalation_failure_modes_2_plus": { "met": true, "evidence_refs": [], "notes": "" },
    "dependencies_with_propagation_2_plus": { "met": true, "evidence_refs": [], "notes": "" },
    "incentive_creates_execution_drag": { "met": true, "evidence_refs": [], "notes": "" },
    "accountability_voids_evidenced": { "met": true, "evidence_refs": [], "notes": "" },
    "talent_cannot_overcome_structure": { "met": true, "evidence_refs": [], "notes": "" },
    "heroic_execution_zone_identified": { "met": true, "evidence_refs": [], "notes": "" }
  }
}

------------------------------------------------
FILE 2 — 4.execution_reality_truth_map.json
------------------------------------------------
{
  "execution_reality_truth_map": {
    "decision_rights_and_authority_failures": [],
    "escalation_mechanics_and_breakage": [],
    "operating_cadence_and_throughput_limits": [],
    "cross_functional_dependency_and_propagation": [],
    "bottlenecks_and_masked_failures": [],
    "incentive_and_accountability_drag": [],
    "talent_vs_system_constraints": [],
    "heroics_as_fragility": []
  }
}

------------------------------------------------
FILE 3 — 4.execution_constraints_register.json
------------------------------------------------
{
  "execution_constraints_register": [
    {
      "constraint": "",
      "category": "DECISION|ESCALATION|CADENCE|DEPENDENCY|BOTTLENECK|INCENTIVE|ACCOUNTABILITY|TALENT|HEROICS",
      "severity": "LOW|MED|HIGH",
      "why_severity": "",
      "what_breaks_if_touched_or_under_stress": "",
      "evidence_refs": [],
      "open_unknowns": []
    }
  ]
}

------------------------------------------------
FILE 4 — 4.contradictions_and_tensions.json
------------------------------------------------
{
  "contradictions_and_tensions": [
    {
      "description": "",
      "components_in_conflict": [],
      "why_it_matters": "",
      "evidence_refs": []
    }
  ]
}

------------------------------------------------
FILE 5 — 4.false_execution_assumptions_invalidated.json
------------------------------------------------
{
  "false_execution_assumptions_invalidated": [
    {
      "assumption": "",
      "explicit_invalidation_statement": "",
      "evidence_refs": []
    }
  ]
}

------------------------------------------------
FILE 6 — 4.hypothesis_discipline_audit.json
------------------------------------------------
{
  "hypothesis_discipline_audit": [
    {
      "sub_stage": "4.1|4.2|4.3|4.4|4.5",
      "issues_found": [],
      "confirmation_bias_risk": "LOW|MED|HIGH",
      "notes": ""
    }
  ]
}

------------------------------------------------
FILE 7 — 4.uncertainty_preservation_audit.json
------------------------------------------------
{
  "uncertainty_preservation_audit": {
    "unknowns_summary": [],
    "un-knowables_summary": [],
    "material_execution_impacts": []
  }
}

------------------------------------------------
FILE 8 — 4.redo_plan_and_gate_decision.json
------------------------------------------------
{
  "stage": "4",
  "gate_decision": "PASS|FAIL",
  "summary_rationale": "",
  "redo_plan_if_failed": [
    {
      "sub_stage_to_redo": "4.1|4.2|4.3|4.4|4.5",
      "failure_reason": "",
      "minimum_required_fix": ""
    }
  ]
}

––––––––––––––––––––
FAIL CONDITIONS (ANY = FAILURE)
––––––––––––––––––––

This stage has FAILED if:
- Exit criteria are asserted without evidence lineage
- Contradictions are normalized or resolved narratively
- Touch-test coverage is missing for key items
- Hypothesis discipline is weak or confirmation-biased
- Uncertainty is collapsed
- Outputs could be misused as recommendations or operating model design

STOP.
Do NOT proceed to Stage 5 within this response.

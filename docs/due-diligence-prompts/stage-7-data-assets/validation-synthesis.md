---
stage: 7
title: "STAGE 7 VALIDATION & SYNTHESIS — EXIT GATE"
type: validation-synthesis
---
# STAGE 7 VALIDATION & SYNTHESIS — EXIT GATE

EXECUTION CONTEXT DECLARATION

Layer 1 — Constitutional Control (PERSISTENT):
This task is governed by the accepted Stage 0 Diligence Constitution.
All Stage 0 sub-controls (0.1–0.6) remain active and enforceable, including:
- Strategic intent lock (discovery only; NO strategy, recommendations, or governance design)
- Claim discipline and evidence hierarchy
- Hypothesis discipline and falsification mandate
- Uncertainty classification and preservation
- Rigor enforcement and red-team authority

If any Stage 0 requirement cannot be met, STOP and state why.

Layer 2 — Stage-Level Orientation:
Stage 7 execution has been completed.
Stage 7 framing applies: determine how the enterprise constructs truth,
where it loses it, and who controls it.
If this stage cannot explain why two executives see different “truths,” Stage 7 fails.

Layer 3 — Atomic Inputs (STRICT):
This prompt does NOT execute a new sub-stage.
It validates and synthesizes completed outputs from Stage 7.1–7.7 ONLY.
You may NOT:
- Introduce new facts
- Introduce new data domains, systems, teams, or actors
- Introduce new hypotheses
- Resolve contradictions narratively
- Propose remediation, governance, operating model, or strategy

Layer 4 — Cross-Stage Reconciliation & QA (PRIMARY LAYER):
This is a gating step.
Progression beyond Stage 7 is PROHIBITED unless Stage 7 PASSES.
If Stage 7 FAILS, you must specify exactly which sub-stage(s) require redo and why.

––––––––––––––––––––
STAGE 7 VALIDATION & SYNTHESIS — EXIT GATE
––––––––––––––––––––

ROLE:
You are acting as Independent QA & Red Team Authority for Stage 7.

SCOPE (STRICT):
- Use ONLY the provided Stage 7.1–7.7 artifacts as inputs
- Do NOT browse for new information
- Do NOT reinterpret evidence beyond reconciliation
- Do NOT optimize, recommend, normalize, or reconcile contradictions

OBJECTIVES:
1) Explicitly test Stage 7 exit criteria
2) Pressure-test internal consistency across Stage 7.1–7.7
3) Produce an “Epistemic Control Truth Map” that preserves uncertainty
4) Issue an explicit PASS / FAIL gate decision

––––––––––––––––––––
INPUT REQUIREMENT (MANDATORY — MULTI-FILE)
––––––––––––––––––––

Before you begin, you MUST confirm receipt of ALL required artifacts.
If ANY artifact is missing, STOP and list it under `missing_inputs`.
Do NOT attempt synthesis with partial inputs.

Required inputs:

Stage 7.1:
- 7.1.authoritative_truth_map.json
- 7.1.contested_domains.json
- 7.1.epistemic_power_centers.json
- 7.1.hypotheses.json
- 7.1.uncertainty_register.json
- 7.1.disconfirming_evidence_not_found.json

Stage 7.2:
- 7.2.meaning_drift_map.json
- 7.2.semantic_fragility_patterns.json
- 7.2.hypotheses.json
- 7.2.uncertainty_register.json
- 7.2.disconfirming_evidence_not_found.json

Stage 7.3:
- 7.3.error_tolerance_map.json
- 7.3.selective_quality_enforcement.json
- 7.3.hypotheses.json
- 7.3.uncertainty_register.json
- 7.3.disconfirming_evidence_not_found.json

Stage 7.4:
- 7.4.blame_flow_map.json
- 7.4.orphaned_data_domains.json
- 7.4.hypotheses.json
- 7.4.uncertainty_register.json
- 7.4.disconfirming_evidence_not_found.json

Stage 7.5:
- 7.5.information_asymmetry_map.json
- 7.5.epistemic_gatekeepers.json
- 7.5.hypotheses.json
- 7.5.uncertainty_register.json
- 7.5.disconfirming_evidence_not_found.json

Stage 7.6:
- 7.6.latency_map.json
- 7.6.systemic_timeliness_failures.json
- 7.6.hypotheses.json
- 7.6.uncertainty_register.json
- 7.6.disconfirming_evidence_not_found.json

Stage 7.7:
- 7.7.epistemic_contradictions.json
- 7.7.coherence_assessment.json
- 7.7.hypotheses.json
- 7.7.uncertainty_register.json
- 7.7.disconfirming_evidence_not_found.json

––––––––––––––––––––
STAGE 7 EXIT CRITERIA (ABSOLUTE — MUST TEST ALL)
––––––––––––––––––––

Stage 7 FAILS unless ALL of the following are met:

1) At least 2 contested or politically sensitive data domains are identified
2) At least 3 data transformations are shown to change meaning materially
3) At least 1 chronic data error is tolerated due to convenience or power
4) At least 1 epistemic gatekeeper is identified
5) At least 1 contradiction in executive “truth” is documented

––––––––––––––––––––
MANDATORY QA CHECKS (ALL REQUIRED)
––––––––––––––––––––

A) CLAIM / EVIDENCE INTEGRITY
- Verify each exit-criteria claim traces to evidence_sources in Stage 7.x artifacts.
- Flag any claim lacking lineage.

B) CROSS-SUB-STAGE CONSISTENCY
- Identify contradictions across 7.1–7.7 (e.g., “system of truth” conflicts with blame flow or access reality).
- Preserve contradictions explicitly; do NOT resolve them.

C) EPISTEMIC MECHANISM COVERAGE
- Confirm the synthesis explicitly covers:
  - Truth authority (7.1)
  - Meaning drift (7.2)
  - Error tolerance (7.3)
  - Accountability/blame flow (7.4)
  - Access asymmetry/gatekeeping (7.5)
  - Latency/timeliness distortion (7.6)
  - Coherence/contradiction (7.7)
- Missing any mechanism = FAIL.

D) HYPOTHESIS DISCIPLINE AUDIT (STAGE 0.3)
- Confirm each sub-stage includes hypotheses AND disconfirming evidence sought.
- Flag confirmation bias where hypotheses only accumulate support.

E) UNCERTAINTY PRESERVATION
- Confirm UNKNOWN vs UNKNOWABLE distinctions persist where used.
- Confirm uncertainty is not collapsed in synthesis or severity scoring.

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
FILE 1 — 7.exit.criteria_test.json
------------------------------------------------
{
  "stage": "7",
  "missing_inputs": [],
  "exit_criteria_test": {
    "contested_domains_2_plus": { "met": true, "evidence_refs": [], "notes": "" },
    "meaning_drift_transformations_3_plus": { "met": true, "evidence_refs": [], "notes": "" },
    "chronic_error_tolerated": { "met": true, "evidence_refs": [], "notes": "" },
    "epistemic_gatekeeper_identified": { "met": true, "evidence_refs": [], "notes": "" },
    "executive_truth_contradiction_documented": { "met": true, "evidence_refs": [], "notes": "" }
  }
}

------------------------------------------------
FILE 2 — 7.epistemic_control_truth_map.json
------------------------------------------------
{
  "epistemic_control_truth_map": {
    "truth_authority_nodes": [],
    "contested_domains": [],
    "meaning_drift_paths": [],
    "error_tolerance_and_selective_enforcement": [],
    "accountability_and_blame_routes": [],
    "access_asymmetry_and_gatekeepers": [],
    "latency_distortion_points": [],
    "executive_truth_contradictions": []
  }
}

------------------------------------------------
FILE 3 — 7.epistemic_constraints_register.json
------------------------------------------------
{
  "epistemic_constraints_register": [
    {
      "constraint": "",
      "category": "AUTHORITY|MEANING_DRIFT|QUALITY|ACCOUNTABILITY|ACCESS|LATENCY|CONTRADICTION",
      "severity": "LOW|MED|HIGH",
      "why_severity": "",
      "what_breaks_if_touched": "",
      "evidence_refs": [],
      "open_unknowns": []
    }
  ]
}

------------------------------------------------
FILE 4 — 7.contradictions_and_tensions.json
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
FILE 5 — 7.hypothesis_discipline_audit.json
------------------------------------------------
{
  "hypothesis_discipline_audit": [
    {
      "sub_stage": "7.1|7.2|7.3|7.4|7.5|7.6|7.7",
      "issues_found": [],
      "confirmation_bias_risk": "LOW|MED|HIGH",
      "notes": ""
    }
  ]
}

------------------------------------------------
FILE 6 — 7.uncertainty_preservation_audit.json
------------------------------------------------
{
  "uncertainty_preservation_audit": {
    "unknowns_summary": [],
    "un-knowables_summary": [],
    "material_uncertainty_impacts": []
  }
}

------------------------------------------------
FILE 7 — 7.redo_plan_if_failed.json
------------------------------------------------
{
  "redo_plan_if_failed": [
    {
      "sub_stage_to_redo": "7.1|7.2|7.3|7.4|7.5|7.6|7.7",
      "failure_reason": "",
      "minimum_required_fix": ""
    }
  ]
}

------------------------------------------------
FILE 8 — 7.gate_decision.json
------------------------------------------------
{
  "stage": "7",
  "gate_decision": "PASS|FAIL",
  "summary_rationale": ""
}

––––––––––––––––––––
FAIL CONDITIONS (ANY = FAILURE)
––––––––––––––––––––

This stage has FAILED if:
- Exit criteria are asserted without evidence lineage
- Contradictions are normalized, reconciled, or explained away
- Epistemic mechanisms are incomplete or missing
- Hypothesis discipline is weak or missing
- Uncertainty is collapsed in synthesis or severity scoring
- Outputs drift into strategy, governance design, or recommendations

STOP.
Do NOT proceed to Stage 8 within this response.

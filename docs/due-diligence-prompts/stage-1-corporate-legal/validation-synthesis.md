---
stage: 1
title: "STAGE 1 VALIDATION & SYNTHESIS — LAYER 4 ENFORCEMENT"
type: validation-synthesis
---
# STAGE 1 VALIDATION & SYNTHESIS — LAYER 4 ENFORCEMENT

EXECUTION CONTEXT DECLARATION

Layer 1 — Constitutional Control:
This task is governed by the accepted Stage 0 Diligence Constitution.
All Stage 0 sub-controls (0.1–0.6) are active and enforceable, including:
- Strategic intent lock (discovery only; no strategy or recommendations)
- Claim discipline and evidence hierarchy
- Hypothesis discipline and falsification mandate
- Uncertainty classification and preservation
- Rigor enforcement and red-team authority
If any Stage 0 requirement cannot be met, STOP and state why.

Layer 2 — Stage-Level Orientation:
Stage 1 Orientation has been completed and approved.
Stage 1 framing applies: determine what the enterprise legally is, who controls what,
and where structural constraints exist.
If you cannot answer “what breaks if we touch this?”, Stage 1 fails.

Layer 3 — Atomic Inputs:
This prompt does NOT execute a new sub-stage.
It validates and synthesizes completed outputs from Stage 1.1–1.5 ONLY.
You may not introduce new facts, new entities, new contracts, or new regimes.
You may only reconcile, cross-check, and synthesize what already exists
in the Stage 1.1–1.5 artifacts.

Layer 4 — Cross-Stage Reconciliation & QA (PRIMARY LAYER):
This is a gating step. Progression to Stage 2 is prohibited unless Stage 1 passes.
You must explicitly test Stage 1 exit criteria, identify gaps, and either PASS or FAIL Stage 1.
If Stage 1 fails, you must specify exactly which sub-stage(s) require redo and why.

––––––––––––––––––––
STAGE 1 VALIDATION & SYNTHESIS
––––––––––––––––––––

ROLE:
You are acting as Independent QA & Red Team Authority for Stage 1.

SCOPE (STRICT):
- Use ONLY the provided Stage 1.1–1.5 artifacts as inputs
- Do NOT browse for new information
- Do NOT add new claims beyond reconciliation/inference strictly supported by existing artifacts
- Do NOT propose remedies, restructuring, or strategy

OBJECTIVE:
1) Validate Stage 1 against absolute exit criteria
2) Pressure-test internal consistency across 1.1–1.5
3) Produce a Stage 1 “Legal-Operational Truth Map” synthesis that preserves uncertainty
4) Output an explicit PASS/FAIL gate decision

––––––––––––––––––––
INPUT REQUIREMENT (MANDATORY — MULTI-FILE)
––––––––––––––––––––

Before you begin, you MUST confirm receipt of ALL the following artifacts.

If ANY artifact is missing, STOP and list it under "missing_inputs".
Do NOT attempt synthesis with partial inputs.

Required inputs:

Stage 1.1:
- 1.1.entities.json
- 1.1.control_constraints.json
- 1.1.hypotheses.json
- 1.1.uncertainties.json
- 1.1.disconfirming_evidence_not_found.json

Stage 1.2:
- 1.2.control_reality.json
- 1.2.misalignment_risks.json
- 1.2.hypotheses.json
- 1.2.disconfirming_evidence_searched.json
- 1.2.unknowns_requests.json

Stage 1.3:
- 1.3.structural_debt_map.json
- 1.3.path_dependency_risks.json
- 1.3.hypotheses.json
- 1.3.disconfirming_evidence_searched.json
- 1.3.unknowns_requests.json

Stage 1.4:
- 1.4.contractual_constraints.json
- 1.4.change_of_control_risk_summary.json
- 1.4.hypotheses.json
- 1.4.disconfirming_evidence_searched.json
- 1.4.unknowns_requests.json

Stage 1.5:
- 1.5.structural_lock_ins.json
- 1.5.false_mobility_assumptions.json
- 1.5.hypotheses.json
- 1.5.disconfirming_evidence_searched.json
- 1.5.unknowns_requests.json

––––––––––––––––––––
STAGE 1 EXIT CRITERIA (ABSOLUTE — MUST TEST EXPLICITLY)
––––––––––––––––––––

Stage 1 is FAILED unless ALL of the following are true:
1. At least 5 structurally relevant entities are identified and explained
2. At least 3 control or veto points are surfaced
3. At least 2 historical decisions are shown to constrain current options
4. At least 1 contract or license is identified that would materially block change
5. At least 1 false assumption about flexibility is explicitly invalidated

––––––––––––––––––––
MANDATORY QA CHECKS (ALL REQUIRED)
––––––––––––––––––––

A) CLAIM / EVIDENCE INTEGRITY CHECK
- Verify each exit-criteria-supporting claim traces to evidence_sources in Stage 1.x artifacts.
- Flag any claim that lacks lineage.

B) CROSS-SUB-STAGE CONSISTENCY CHECK
- Identify contradictions across 1.1–1.5 (e.g., control actor implies rights not reflected elsewhere).
- Do NOT resolve contradictions narratively; preserve them as explicit tensions.

C) TOUCH-TEST COVERAGE CHECK
- Confirm “what breaks if touched” exists for entities, control points, contracts, and lock-ins.
- Missing touch tests = FAIL unless corrected.

D) HYPOTHESIS DISCIPLINE CHECK (STAGE 0.3)
- Confirm each sub-stage includes hypotheses with disconfirming evidence sought.
- Flag confirmation bias where hypotheses only accumulate support.

E) UNCERTAINTY PRESERVATION CHECK
- Confirm unknowns are explicitly recorded and not smoothed.
- Confirm UNKNOWN vs UNKNOWABLE distinctions are respected.

––––––––––––––––––––
SYNTHESIS OUTPUT REQUIREMENTS
––––––––––––––––––––

Your synthesis must produce:
1) A Legal-Operational Truth Map consolidating:
   - Structurally relevant entities
   - Control / veto points
   - Structural debt paths
   - Contractual change friction
   - Jurisdictional / licensing lock-ins

2) A Structural Constraint Register with severity rationale
3) A False Flexibility Assumptions list with explicit invalidations
4) A Redo Plan if failed (exact sub-stage(s) and minimum fixes)

––––––––––––––––––––
OUTPUT PROTOCOL — MULTI-FILE JSON (MANDATORY)
––––––––––––––––––––

You will NOT emit a single monolithic JSON object. It is known to lock up.

Instead, you will emit the Stage 1 validation + synthesis as a SET OF SEPARATE JSON FILES.
Each file must be valid standalone JSON.
Do NOT repeat the same data across files.
Do NOT introduce new facts in later files.

You MUST produce files in the following order. If you cannot, STOP and state why.

FILE 1 — 1.V.missing_inputs.json
{
  "stage": "1",
  "missing_inputs": [],
  "validation_status": "READY|BLOCKED",
  "notes": ""
}

Rule: If validation_status = BLOCKED, STOP immediately (no further files).

FILE 2 — 1.V.gate_decision.json
{
  "stage": "1",
  "gate_decision": "PASS|FAIL",
  "gate_rationale": "A short, constraint-based statement. No recommendations."
}

FILE 3 — 1.V.exit_criteria_test.json
{
  "exit_criteria_test": {
    "criterion_1_entities_5_plus": { "met": true, "evidence_refs": [], "notes": "" },
    "criterion_2_control_veto_3_plus": { "met": true, "evidence_refs": [], "notes": "" },
    "criterion_3_history_constraints_2_plus": { "met": true, "evidence_refs": [], "notes": "" },
    "criterion_4_contract_or_license_blocks_change": { "met": true, "evidence_refs": [], "notes": "" },
    "criterion_5_false_flexibility_invalidated": { "met": true, "evidence_refs": [], "notes": "" }
  }
}

FILE 4 — 1.V.truth_map.entities.json
{
  "legal_operational_truth_map": {
    "structurally_relevant_entities": [
      {
        "entity_or_construct": "",
        "why_structurally_relevant": "",
        "touch_test_what_breaks": "",
        "evidence_refs": []
      }
    ]
  }
}

FILE 5 — 1.V.truth_map.control_veto_points.json
{
  "legal_operational_truth_map": {
    "control_and_veto_points": [
      {
        "actor": "",
        "type": "SHAREHOLDER|CREDITOR|PARTNER|REGULATOR",
        "what_they_can_block_or_force": "",
        "touch_test_what_breaks": "",
        "evidence_refs": []
      }
    ]
  }
}

FILE 6 — 1.V.truth_map.structural_debt_paths.json
{
  "legal_operational_truth_map": {
    "structural_debt_paths": [
      {
        "historical_event": "",
        "structural_artifact_created": "",
        "current_constraint": "",
        "why_it_persists": "",
        "touch_test_what_breaks": "",
        "evidence_refs": []
      }
    ]
  }
}

FILE 7 — 1.V.truth_map.contractual_change_friction.json
{
  "legal_operational_truth_map": {
    "contractual_change_friction": [
      {
        "contract_or_class": "",
        "trigger_event": "",
        "what_breaks": "",
        "severity": "LOW|MED|HIGH",
        "evidence_refs": []
      }
    ]
  }
}

FILE 8 — 1.V.truth_map.jurisdiction_and_licensing_lock_ins.json
{
  "legal_operational_truth_map": {
    "jurisdiction_and_licensing_lock_ins": [
      {
        "activity_or_asset": "",
        "locked_to": "",
        "operational_constraint": "",
        "touch_test_what_breaks": "",
        "evidence_refs": []
      }
    ]
  }
}

FILE 9 — 1.V.structural_constraint_register.json
{
  "structural_constraint_register": [
    {
      "constraint": "",
      "category": "ENTITY|CONTROL|HISTORY|CONTRACT|JURISDICTION_LICENSE",
      "severity": "LOW|MED|HIGH",
      "why_severity": "",
      "touch_test_what_breaks": "",
      "evidence_refs": [],
      "open_unknowns": []
    }
  ]
}

FILE 10 — 1.V.false_flexibility_assumptions_invalidated.json
{
  "false_flexibility_assumptions_invalidated": [
    {
      "assumption": "",
      "explicit_invalidation_statement": "",
      "evidence_refs": []
    }
  ]
}

FILE 11 — 1.V.contradictions_and_tensions.json
{
  "contradictions_and_tensions": [
    {
      "description": "",
      "why_it_matters": "",
      "evidence_refs": []
    }
  ]
}

FILE 12 — 1.V.hypothesis_discipline_audit.json
{
  "hypothesis_discipline_audit": [
    {
      "sub_stage": "1.1|1.2|1.3|1.4|1.5",
      "issues_found": [],
      "confirmation_bias_risk": "LOW|MED|HIGH",
      "notes": ""
    }
  ]
}

FILE 13 — 1.V.uncertainty_preservation_audit.json
{
  "uncertainty_preservation_audit": {
    "unknowns_summary": [],
    "un-knowables_summary": [],
    "material_uncertainty_impacts": []
  }
}

FILE 14 — 1.V.redo_plan_if_failed.json
{
  "redo_plan_if_failed": [
    {
      "sub_stage_to_redo": "1.1|1.2|1.3|1.4|1.5",
      "failure_reason": "",
      "minimum_required_fix": ""
    }
  ]
}

––––––––––––––––––––
STOP CONDITION
––––––––––––––––––––

STOP.
Do NOT proceed to Stage 2 within this response.

---
stage: 2
title: "STAGE 2 VALIDATION & SYNTHESIS — EXIT GATE"
type: validation-synthesis
---
# STAGE 2 VALIDATION & SYNTHESIS — EXIT GATE

EXECUTION CONTEXT DECLARATION

Layer 1 — Constitutional Control:
This task is governed by the accepted Stage 0 Diligence Constitution.
All Stage 0 sub-controls (0.1–0.6) remain active and enforceable, including:
- Strategic intent lock (discovery only; NO strategy, recommendations, or roadmaps)
- Claim discipline and evidence hierarchy
- Hypothesis discipline and falsification mandate
- Uncertainty classification and preservation
- Rigor enforcement and red-team authority

If any Stage 0 requirement cannot be met, STOP and state why.

Layer 2 — Stage-Level Orientation:
Stage 2 execution has been completed.
Stage 2 framing applies: determine how the enterprise ACTUALLY creates,
flows, captures, and contradicts business value under real constraints.

Layer 3 — Atomic Inputs (STRICT):
This prompt does NOT execute a new sub-stage.
It validates and synthesizes completed outputs from Stage 2.1–2.6 ONLY.
You may NOT:
- Introduce new facts
- Introduce new entities, customers, partners, or capabilities
- Introduce new hypotheses
- Resolve contradictions narratively
- Propose remediation or strategy

Layer 4 — Cross-Stage Reconciliation & QA (PRIMARY LAYER):
This is a gating step.
Progression to Stage 3 is PROHIBITED unless Stage 2 PASSES.
If Stage 2 FAILS, you must specify exactly which sub-stage(s) require redo and why.

––––––––––––––––––––
STAGE 2 VALIDATION & SYNTHESIS — EXIT GATE
––––––––––––––––––––

ROLE:
You are acting as Independent QA & Red Team Authority for Stage 2.

SCOPE (STRICT):
- Use ONLY the provided Stage 2.1–2.6 artifacts as inputs
- Do NOT browse for new information
- Do NOT reinterpret evidence beyond reconciliation
- Do NOT optimize, recommend, or normalize contradictions

OBJECTIVES:
1) Explicitly test Stage 2 exit criteria  
2) Pressure-test internal consistency across Stage 2.1–2.6  
3) Produce a “Value Reality Truth Map” preserving uncertainty  
4) Issue an explicit PASS / FAIL gate decision  

––––––––––––––––––––
INPUT REQUIREMENT (MANDATORY — MULTI-FILE)
––––––––––––––––––––

Before you begin, you MUST confirm receipt of ALL required artifacts.

If ANY artifact is missing, STOP and list it under `missing_inputs`.
Do NOT attempt synthesis with partial inputs.

Required inputs:

Stage 2.1:
- 2.1.revenue_engines.json
- 2.1.revenue_mechanics.json
- 2.1.hypotheses.json
- 2.1.uncertainty_register.json

Stage 2.2:
- 2.2.cost_structures.json
- 2.2.margin_drivers.json
- 2.2.hypotheses.json
- 2.2.uncertainty_register.json

Stage 2.3:
- 2.3.value_flows.json
- 2.3.value_transformation_points.json
- 2.3.value_frictions_and_leakage.json
- 2.3.friction_classification_summary.json
- 2.3.hypotheses.json
- 2.3.uncertainty_register.json

Stage 2.4:
- 2.4.customer_segments.json
- 2.4.economic_dependence_and_concentration.json
- 2.4.customer_contract_and_lock_in_dynamics.json
- 2.4.hypotheses.json
- 2.4.uncertainty_register.json

Stage 2.5:
- 2.5.material_partners_and_channels.json
- 2.5.value_capture_and_asymmetry.json
- 2.5.dependency_and_leverage.json
- 2.5.hypotheses.json
- 2.5.uncertainty_register.json

Stage 2.6:
- 2.6.identified_contradictions.json
- 2.6.contradiction_impact_analysis.json
- 2.6.coherence_assessment_summary.json
- 2.6.hypotheses.json
- 2.6.uncertainty_register.json

––––––––––––––––––––
STAGE 2 EXIT CRITERIA (ABSOLUTE — MUST TEST ALL)
––––––––––––––––––––

Stage 2 FAILS unless ALL of the following are met:

1. At least 3 distinct revenue engines are identified and grounded in evidence  
2. At least 2 material cost or margin drivers materially constrain value capture  
3. At least 2 systemic value frictions or leakage points are surfaced  
4. At least 1 customer concentration or dependency risk is explicitly identified  
5. At least 1 partner or channel exhibits value capture asymmetry  
6. At least 1 internal business model contradiction is surfaced and evidenced  

––––––––––––––––––––
MANDATORY QA CHECKS (ALL REQUIRED)
––––––––––––––––––––

A) CLAIM / EVIDENCE INTEGRITY  
- Verify each exit-criteria claim traces to Stage 2.x evidence_sources
- Flag any claim lacking lineage

B) CROSS-SUB-STAGE CONSISTENCY  
- Identify contradictions between revenue, cost, flow, customer, partner, and coherence outputs
- Preserve contradictions explicitly; do NOT resolve them

C) VALUE FLOW COVERAGE  
- Confirm revenue engines map through value flows to realization
- Missing end-to-end flow = FAIL

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
FILE 1 — 2.exit.criteria_test.json
------------------------------------------------
{
  "stage": "2",
  "exit_criteria_test": {
    "revenue_engines_identified": { "met": true, "evidence_refs": [], "notes": "" },
    "material_cost_or_margin_constraints": { "met": true, "evidence_refs": [], "notes": "" },
    "systemic_value_frictions": { "met": true, "evidence_refs": [], "notes": "" },
    "customer_dependency_risk": { "met": true, "evidence_refs": [], "notes": "" },
    "partner_value_capture_asymmetry": { "met": true, "evidence_refs": [], "notes": "" },
    "business_model_contradiction": { "met": true, "evidence_refs": [], "notes": "" }
  }
}

------------------------------------------------
FILE 2 — 2.value_reality_truth_map.json
------------------------------------------------
{
  "value_reality_truth_map": {
    "revenue_engines": [],
    "cost_and_margin_constraints": [],
    "value_flow_and_friction_points": [],
    "customer_dependency_nodes": [],
    "partner_and_channel_leverage_points": [],
    "internal_contradictions": []
  }
}

------------------------------------------------
FILE 3 — 2.structural_value_constraints_register.json
------------------------------------------------
{
  "structural_value_constraints_register": [
    {
      "constraint": "",
      "category": "REVENUE|COST|FLOW|CUSTOMER|PARTNER|CONTRADICTION",
      "severity": "LOW|MED|HIGH",
      "why_severity": "",
      "what_breaks_if_touched": "",
      "evidence_refs": [],
      "open_unknowns": []
    }
  ]
}

------------------------------------------------
FILE 4 — 2.contradictions_and_tensions.json
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
FILE 5 — 2.hypothesis_discipline_audit.json
------------------------------------------------
{
  "hypothesis_discipline_audit": [
    {
      "sub_stage": "2.1|2.2|2.3|2.4|2.5|2.6",
      "issues_found": [],
      "confirmation_bias_risk": "LOW|MED|HIGH",
      "notes": ""
    }
  ]
}

------------------------------------------------
FILE 6 — 2.uncertainty_preservation_audit.json
------------------------------------------------
{
  "uncertainty_preservation_audit": {
    "unknowns_summary": [],
    "un-knowables_summary": [],
    "material_uncertainty_impacts": []
  }
}

------------------------------------------------
FILE 7 — 2.redo_plan_if_failed.json
------------------------------------------------
{
  "redo_plan_if_failed": [
    {
      "sub_stage_to_redo": "2.1|2.2|2.3|2.4|2.5|2.6",
      "failure_reason": "",
      "minimum_required_fix": ""
    }
  ]
}

------------------------------------------------
FILE 8 — 2.gate_decision.json
------------------------------------------------
{
  "stage": "2",
  "gate_decision": "PASS|FAIL",
  "summary_rationale": ""
}

––––––––––––––––––––
FAIL CONDITIONS (ANY = FAILURE)
––––––––––––––––––––

This stage has FAILED if:
- Exit criteria are asserted without evidence
- Contradictions are normalized or resolved
- Value flow is incomplete
- Hypothesis discipline is weak or missing
- Uncertainty is collapsed
- Outputs could be misused as strategy

STOP.
Do NOT proceed to Stage 3 within this response.

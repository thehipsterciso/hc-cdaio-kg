---
stage: 6
title: "STAGE 6 VALIDATION & SYNTHESIS — EXIT GATE"
type: validation-synthesis
---
# STAGE 6 VALIDATION & SYNTHESIS — EXIT GATE

EXECUTION CONTEXT DECLARATION

Layer 1 — Constitutional Control (PERSISTENT):
This task is governed by the accepted Stage 0 Diligence Constitution.
All Stage 0 sub-controls (0.1–0.6) remain active and enforceable, including:
- Strategic intent lock (discovery only; NO strategy, architecture, or remediation)
- Claim discipline and evidence hierarchy
- Hypothesis discipline and falsification mandate
- Uncertainty classification and preservation
- Rigor enforcement and red-team authority

If any Stage 0 requirement cannot be met, STOP and state why.

Layer 2 — Stage-Level Orientation:
Stage 6 execution has been completed.
Stage 6 framing applies: determine where TECHNOLOGY, COMPUTE, AND PLATFORMS
impose non-negotiable operational constraints regardless of intent.

Layer 3 — Atomic Inputs (STRICT):
This prompt does NOT execute a new sub-stage.
It validates and synthesizes completed outputs from Stage 6.1–6.6 ONLY.

You may NOT:
- Introduce new facts, systems, vendors, or platforms
- Introduce new hypotheses
- Resolve contradictions narratively
- Normalize fragility or immobility
- Propose modernization, consolidation, or strategy

Layer 4 — Cross-Stage Reconciliation & QA (PRIMARY LAYER):
This is a HARD GATE.
Progression to Stage 7 is PROHIBITED unless Stage 6 PASSES.
If Stage 6 FAILS, you must specify exactly which sub-stage(s) require redo and why.

––––––––––––––––––––
STAGE 6 VALIDATION & SYNTHESIS — EXIT GATE
––––––––––––––––––––

ROLE:
You are acting as Independent QA & Red Team Authority for Stage 6.

SCOPE (STRICT):
- Use ONLY the provided Stage 6.1–6.6 artifacts as inputs
- Do NOT browse for new information
- Do NOT reinterpret evidence beyond reconciliation
- Do NOT optimize, recommend, or normalize contradictions

OBJECTIVES:
1) Explicitly test Stage 6 exit criteria  
2) Pressure-test internal consistency across Stage 6.1–6.6  
3) Produce a “Technology Control & Fragility Truth Map” preserving uncertainty  
4) Issue an explicit PASS / FAIL gate decision  

––––––––––––––––––––
INPUT REQUIREMENT (MANDATORY — MULTI-FILE)
––––––––––––––––––––

Before you begin, you MUST confirm receipt of ALL required artifacts.

If ANY artifact is missing, STOP and list it under `missing_inputs`.
Do NOT attempt synthesis with partial inputs.

Required inputs:

Stage 6.1:
- 6.1.compute_control_map.json
- 6.1.facility_lock_in_risks.json
- 6.1.hypotheses.json
- 6.1.uncertainty_register.json

Stage 6.2:
- 6.2.cloud_dependency_map.json
- 6.2.multi_cloud_fiction_flags.json
- 6.2.hyperscaler_power_asymmetries.json
- 6.2.hypotheses.json
- 6.2.uncertainty_register.json

Stage 6.3:
- 6.3.platform_fragility_map.json
- 6.3.untouchable_systems.json
- 6.3.hypotheses.json
- 6.3.uncertainty_register.json

Stage 6.4:
- 6.4.vendor_control_map.json
- 6.4.vendor_power_concentration.json
- 6.4.hypotheses.json
- 6.4.uncertainty_register.json

Stage 6.5:
- 6.5.technical_constraint_map.json
- 6.5.compound_debt_risks.json
- 6.5.hypotheses.json
- 6.5.uncertainty_register.json

Stage 6.6:
- 6.6.estate_contradictions.json
- 6.6.coherence_assessment.json
- 6.6.hypotheses.json
- 6.6.uncertainty_register.json

––––––––––––––––––––
STAGE 6 EXIT CRITERIA (ABSOLUTE — MUST TEST ALL)
––––––––––––––––––––

Stage 6 FAILS unless ALL of the following are met:

1. At least 3 immovable or hard-to-exit compute dependencies are identified  
2. At least 2 cloud or platform “exit fictions” are explicitly invalidated  
3. At least 2 platforms are identified as high blast-radius systems  
4. At least 1 vendor is shown to exert structural leverage  
5. At least 1 technical debt area is shown to constrain business outcomes  

––––––––––––––––––––
MANDATORY QA CHECKS (ALL REQUIRED)
––––––––––––––––––––

A) CLAIM / EVIDENCE INTEGRITY  
- Verify each exit-criteria claim traces to Stage 6.x evidence_sources
- Flag any claim lacking lineage

B) CROSS-SUB-STAGE CONSISTENCY  
- Identify contradictions across compute, cloud, platform, vendor, and debt analyses
- Preserve contradictions explicitly; do NOT resolve them

C) CONTROL & IMMOBILITY COVERAGE  
- Confirm “what breaks if touched” exists for compute, platforms, vendors, and debt
- Missing immobility logic = FAIL

D) HYPOTHESIS DISCIPLINE AUDIT (STAGE 0.3)  
- Confirm each sub-stage includes hypotheses with disconfirming searches
- Flag confirmation bias risk

E) UNCERTAINTY PRESERVATION  
- Confirm UNKNOWN vs UNKNOWABLE distinctions persist
- Confirm uncertainty is not collapsed during synthesis

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
FILE 1 — 6.exit.criteria_test.json
------------------------------------------------
{
  "stage": "6",
  "exit_criteria_test": {
    "compute_immobility_dependencies": { "met": true, "evidence_refs": [], "notes": "" },
    "cloud_exit_fictions_invalidated": { "met": true, "evidence_refs": [], "notes": "" },
    "high_blast_radius_platforms": { "met": true, "evidence_refs": [], "notes": "" },
    "vendor_structural_leverage": { "met": true, "evidence_refs": [], "notes": "" },
    "technical_debt_business_constraint": { "met": true, "evidence_refs": [], "notes": "" }
  }
}

------------------------------------------------
FILE 2 — 6.technology_control_and_fragility_truth_map.json
------------------------------------------------
{
  "technology_control_and_fragility_truth_map": {
    "compute_and_facility_lock_ins": [],
    "cloud_and_hyperscaler_dependencies": [],
    "platform_blast_radius_nodes": [],
    "vendor_leverage_points": [],
    "technical_debt_constraints": [],
    "estate_contradictions": []
  }
}

------------------------------------------------
FILE 3 — 6.structural_technology_constraints_register.json
------------------------------------------------
{
  "structural_technology_constraints_register": [
    {
      "constraint": "",
      "category": "COMPUTE|CLOUD|PLATFORM|VENDOR|DEBT|CONTRADICTION",
      "severity": "LOW|MED|HIGH",
      "why_severity": "",
      "what_breaks_if_touched": "",
      "evidence_refs": [],
      "open_unknowns": []
    }
  ]
}

------------------------------------------------
FILE 4 — 6.contradictions_and_tensions.json
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
FILE 5 — 6.hypothesis_discipline_audit.json
------------------------------------------------
{
  "hypothesis_discipline_audit": [
    {
      "sub_stage": "6.1|6.2|6.3|6.4|6.5|6.6",
      "issues_found": [],
      "confirmation_bias_risk": "LOW|MED|HIGH",
      "notes": ""
    }
  ]
}

------------------------------------------------
FILE 6 — 6.uncertainty_preservation_audit.json
------------------------------------------------
{
  "uncertainty_preservation_audit": {
    "unknowns_summary": [],
    "un-knowables_summary": [],
    "material_uncertainty_impacts": []
  }
}

------------------------------------------------
FILE 7 — 6.redo_plan_if_failed.json
------------------------------------------------
{
  "redo_plan_if_failed": [
    {
      "sub_stage_to_redo": "6.1|6.2|6.3|6.4|6.5|6.6",
      "failure_reason": "",
      "minimum_required_fix": ""
    }
  ]
}

------------------------------------------------
FILE 8 — 6.gate_decision.json
------------------------------------------------
{
  "stage": "6",
  "gate_decision": "PASS|FAIL",
  "summary_rationale": ""
}

––––––––––––––––––––
FAIL CONDITIONS (ANY = FAILURE)
––––––––––––––––––––

This stage has FAILED if:
- Exit criteria are asserted without evidence
- Compute, cloud, or platform immobility is normalized
- Vendor leverage is described without power transfer
- Technical debt lacks business consequence
- Hypothesis discipline is weak or missing
- Uncertainty is collapsed
- Outputs could be misused as architecture or strategy

STOP.
Do NOT proceed to Stage 7 within this response.

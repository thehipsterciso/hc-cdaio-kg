---
stage: 3
title: "STAGE 3 VALIDATION & SYNTHESIS — EXIT GATE"
type: validation-synthesis
---
# STAGE 3 VALIDATION & SYNTHESIS — EXIT GATE

EXECUTION CONTEXT DECLARATION

Layer 1 — Constitutional Control (PERSISTENT):
This task is governed by the accepted Stage 0 Diligence Constitution.
All Stage 0 sub-controls (0.1–0.6) remain active and enforceable, including:
- Strategic intent lock (discovery only; NO strategy, recommendations, or positioning)
- Claim discipline and evidence hierarchy
- Hypothesis discipline and falsification mandate
- Uncertainty classification and preservation
- Rigor enforcement and red-team authority

If any Stage 0 requirement cannot be met, STOP and state why.

Layer 2 — Stage-Level Orientation:
Stage 3 Orientation has been completed and approved.
Stage 3 framing applies: determine how external forces constrain
revenue durability, margins, control, and optionality.
If external pressure cannot be shown to materially matter, Stage 3 fails.

Layer 3 — Atomic Inputs:
This prompt does NOT execute a new sub-stage.
It validates and synthesizes completed outputs from Stage 3.1–3.6 ONLY.
You may NOT introduce new facts, competitors, shocks, or interpretations.
You may ONLY reconcile, cross-check, and synthesize existing artifacts.

Layer 4 — Cross-Stage Reconciliation & QA (PRIMARY LAYER):
This is a gating step.
Progression to Stage 4 is prohibited unless Stage 3 passes.
If Stage 3 fails, you must specify exactly which sub-stage(s) require redo and why.

––––––––––––––––––––
STAGE 3 VALIDATION & SYNTHESIS
––––––––––––––––––––

ROLE:
You are acting as Independent QA & Red Team Authority for Stage 3.

SCOPE (STRICT):
- Use ONLY the provided Stage 3.1–3.6 artifacts as inputs
- Do NOT browse for new information
- Do NOT smooth, normalize, or narratively reconcile conflicts
- Do NOT propose mitigation, differentiation, or strategy
- Do NOT soften conclusions for coherence

OBJECTIVE:
1) Validate Stage 3 against absolute exit criteria  
2) Pressure-test internal consistency across 3.1–3.6  
3) Produce an **External Pressure & Survivability Map**
   that preserves uncertainty and adversarial tension  
4) Output an explicit PASS / FAIL gate decision  

––––––––––––––––––––
INPUT REQUIREMENT (MANDATORY — MULTI-FILE)
––––––––––––––––––––

Before you begin, you MUST confirm receipt of ALL artifacts below.

If ANY artifact is missing, STOP and list it under `missing_inputs`.
Do NOT attempt synthesis with partial inputs.

Required inputs:

Stage 3.1:
- 3.1.market_power_map.json
- 3.1.value_migration_trends.json
- 3.1.inevitable_margin_pressures.json
- 3.1.hypotheses.json
- 3.1.disconfirming_evidence_searched.json
- 3.1.unknowns_requests.json

Stage 3.2:
- 3.2.competitive_threats.json
- 3.2.asymmetric_threats.json
- 3.2.false_competitor_focuses.json
- 3.2.hypotheses.json
- 3.2.disconfirming_evidence_searched.json
- 3.2.unknowns_requests.json

Stage 3.3:
- 3.3.switching_dynamics.json
- 3.3.false_loyalty_signals.json
- 3.3.latent_churn_risks.json
- 3.3.hypotheses.json
- 3.3.disconfirming_evidence_searched.json
- 3.3.unknowns_requests.json

Stage 3.4:
- 3.4.pricing_reality.json
- 3.4.silent_price_erosion.json
- 3.4.pricing_power_misreads.json
- 3.4.hypotheses.json
- 3.4.disconfirming_evidence_searched.json
- 3.4.unknowns_requests.json

Stage 3.5:
- 3.5.channel_force_map.json
- 3.5.platform_rent_extraction.json
- 3.5.dependency_trends.json
- 3.5.hypotheses.json
- 3.5.disconfirming_evidence_searched.json
- 3.5.uncertainty_register.json
- 3.5.unknowns_requests.json

Stage 3.6:
- 3.6.shock_response_profiles.json
- 3.6.structural_exposure.json
- 3.6.irreversibility_flags.json
- 3.6.hypotheses.json
- 3.6.disconfirming_evidence_searched.json
- 3.6.uncertainty_register.json
- 3.6.unknowns_requests.json

––––––––––––––––––––
STAGE 3 EXIT CRITERIA (ABSOLUTE — MUST TEST EXPLICITLY)
––––––––––––––––––––

Stage 3 is FAILED unless ALL of the following are true:

1. At least 3 external pressure forces are identified and evidenced  
2. At least 2 power asymmetries unfavorable to the company are documented  
3. At least 1 competitive threat is shown to damage economics
   without head-to-head competition  
4. At least 1 false belief about customer loyalty or pricing power is invalidated  
5. At least 1 external shock is shown to cause irreversible damage
   or permanent power transfer  

––––––––––––––––––––
MANDATORY QA CHECKS (ALL REQUIRED)
––––––––––––––––––––

A) CLAIM / EVIDENCE INTEGRITY  
- Verify each exit-criteria claim traces to evidence_sources
- Flag any unsupported claims

B) CROSS-SUB-STAGE CONSISTENCY  
- Identify contradictions between:
  - Market power vs pricing behavior
  - Competitive threats vs churn dynamics
  - Partner power vs shock exposure
- Preserve contradictions explicitly

C) TOUCH-TEST COVERAGE  
- Confirm “what breaks if touched” exists for:
  - Market power
  - Competitive threats
  - Pricing dynamics
  - Channel dependency
  - Shock scenarios
- Missing touch tests = FAIL

D) HYPOTHESIS DISCIPLINE (STAGE 0.3)  
- Confirm each sub-stage contains falsifiable hypotheses
- Flag confirmation bias or hypothesis drift

E) UNCERTAINTY PRESERVATION  
- Confirm unknowns are not smoothed or collapsed
- Confirm UNKNOWN vs UNKNOWABLE distinctions persist

––––––––––––––––––––
OUTPUT PROTOCOL — MULTI-FILE JSON (MANDATORY)
––––––––––––––––––––

You MUST emit the following JSON files in order.
Each file must be standalone valid JSON.
Do NOT combine files.
Do NOT repeat content across files.

------------------------------------------------
FILE 1 — 3.V.missing_inputs.json
------------------------------------------------
{
  "missing_inputs": [],
  "validation_status": "READY|BLOCKED",
  "notes": ""
}

------------------------------------------------
FILE 2 — 3.V.exit_criteria_test.json
------------------------------------------------
{
  "exit_criteria_test": {
    "criterion_1_external_forces_3_plus": { "met": true, "evidence_refs": [], "notes": "" },
    "criterion_2_power_asymmetries_2_plus": { "met": true, "evidence_refs": [], "notes": "" },
    "criterion_3_non_head_to_head_threat": { "met": true, "evidence_refs": [], "notes": "" },
    "criterion_4_false_belief_invalidated": { "met": true, "evidence_refs": [], "notes": "" },
    "criterion_5_irreversible_shock": { "met": true, "evidence_refs": [], "notes": "" }
  }
}

------------------------------------------------
FILE 3 — 3.V.external_pressure_map.json
------------------------------------------------
{
  "external_pressure_map": {
    "pressure_forces": [],
    "power_transfers": [],
    "economic_fragility_points": [],
    "where_optionality_collapses": []
  }
}

------------------------------------------------
FILE 4 — 3.V.survivability_assessment.json
------------------------------------------------
{
  "survivability_assessment": [
    {
      "pressure_or_shock": "",
      "what_breaks": "",
      "reversibility": "REVERSIBLE|IRREVERSIBLE",
      "who_gains_power": "",
      "evidence_refs": [],
      "open_unknowns": []
    }
  ]
}

------------------------------------------------
FILE 5 — 3.V.false_beliefs_invalidated.json
------------------------------------------------
{
  "false_beliefs_invalidated": [
    {
      "belief": "",
      "explicit_invalidation": "",
      "evidence_refs": []
    }
  ]
}

------------------------------------------------
FILE 6 — 3.V.contradictions_and_tensions.json
------------------------------------------------
{
  "contradictions_and_tensions": [
    {
      "description": "",
      "why_it_matters": "",
      "evidence_refs": []
    }
  ]
}

------------------------------------------------
FILE 7 — 3.V.hypothesis_discipline_audit.json
------------------------------------------------
{
  "hypothesis_discipline_audit": [
    {
      "sub_stage": "3.1|3.2|3.3|3.4|3.5|3.6",
      "issues_found": [],
      "confirmation_bias_risk": "LOW|MED|HIGH",
      "notes": ""
    }
  ]
}

------------------------------------------------
FILE 8 — 3.V.uncertainty_preservation_audit.json
------------------------------------------------
{
  "uncertainty_preservation_audit": {
    "unknowns_summary": [],
    "un-knowables_summary": [],
    "material_uncertainty_impacts": []
  }
}

------------------------------------------------
FILE 9 — 3.V.gate_decision.json
------------------------------------------------
{
  "stage": "3",
  "gate_decision": "PASS|FAIL",
  "redo_plan_if_failed": [
    {
      "sub_stage_to_redo": "3.1|3.2|3.3|3.4|3.5|3.6",
      "failure_reason": "",
      "minimum_required_fix": ""
    }
  ]
}

STOP.
Do NOT proceed to Stage 4 within this response.

---
stage: 9
title: "STAGE 9 VALIDATION & SYNTHESIS — EXIT GATE"
type: validation-synthesis
---
# STAGE 9 VALIDATION & SYNTHESIS — EXIT GATE

and proceed with the Stage 9 exit validation and synthesis.

EXECUTION CONTEXT DECLARATION

Layer 1 — Constitutional Control (PERSISTENT):
This task is governed by the accepted Stage 0 Diligence Constitution.
All Stage 0 sub-controls (0.1–0.6) remain active and enforceable, including:
- Strategic intent lock (discovery only; NO strategy, recommendations, remediation, or assurance)
- Claim discipline and evidence hierarchy
- Hypothesis discipline and falsification mandate
- Uncertainty classification and preservation
- Rigor enforcement and independent red-team authority

If any Stage 0 requirement cannot be met, STOP and state why.

Layer 2 — Stage-Level Orientation:
Stage 9 execution has been completed.
Stage 9 framing applies: determine whether the enterprise can withstand shock
without destroying value.
This is a FAILURE DISCOVERY stage, not resilience affirmation.

Layer 3 — Atomic Inputs (STRICT):
This prompt does NOT execute a new sub-stage.
It validates and synthesizes completed outputs from Stage 9.1–9.5 ONLY.

You MUST NOT:
- Introduce new facts, risks, shocks, or scenarios
- Introduce new hypotheses
- Normalize or resolve contradictions
- Propose remediation, mitigation, or resilience strategy
- Reframe failure as “acceptable risk”

Layer 4 — Cross-Stage Reconciliation & QA (PRIMARY LAYER):
This is a hard exit gate.
Progression beyond Stage 9 is PROHIBITED unless Stage 9 PASSES.
If Stage 9 FAILS, you must specify exactly which sub-stage(s) require redo and why.

––––––––––––––––––––
STAGE 9 VALIDATION & SYNTHESIS — EXIT GATE
––––––––––––––––––––

ROLE:
You are acting as Independent QA & Red Team Authority for Stage 9.

SCOPE (STRICT):
- Use ONLY the provided Stage 9.1–9.5 artifacts as inputs
- Do NOT browse for new information
- Do NOT reinterpret evidence beyond reconciliation
- Do NOT collapse uncertainty
- Do NOT soften failure language

OBJECTIVES (ALL REQUIRED):
1) Explicitly test Stage 9 exit criteria
2) Pressure-test internal consistency across Stage 9.1–9.5
3) Produce a consolidated Enterprise Failure & Fragility Map
4) Preserve contradictions, fragilities, and unknowns
5) Issue an explicit PASS / FAIL gate decision

––––––––––––––––––––
INPUT REQUIREMENT (MANDATORY — MULTI-FILE)
––––––––––––––––––––

Before you begin, you MUST confirm receipt of ALL required artifacts.
If ANY artifact is missing, STOP and list it under `missing_inputs`.
Do NOT attempt synthesis with partial inputs.

Required inputs:

Stage 9.1:
- 9.1.esg_operating_constraints.json
- 9.1.capital_and_deal_blockers.json
- 9.1.esg_accountability_gaps.json
- 9.1.hypotheses.json
- 9.1.uncertainty_register.json

Stage 9.2:
- 9.2.failure_sequences.json
- 9.2.false_resilience_assumptions.json
- 9.2.single_points_of_operational_failure.json
- 9.2.hypotheses.json
- 9.2.uncertainty_register.json

Stage 9.3:
- 9.3.human_fragility_map.json
- 9.3.organizational_single_points_of_failure.json
- 9.3.hypotheses.json
- 9.3.uncertainty_register.json

Stage 9.4:
- 9.4.shock_propagation_paths.json
- 9.4.ecosystem_concentration_risks.json
- 9.4.hypotheses.json
- 9.4.uncertainty_register.json

Stage 9.5:
- 9.5.risk_transfer_reality.json
- 9.5.false_safety_nets.json
- 9.5.residual_risk_owners.json
- 9.5.hypotheses.json
- 9.5.uncertainty_register.json

––––––––––––––––––––
STAGE 9 EXIT CRITERIA (ABSOLUTE — MUST TEST ALL)
––––––––––––––––––––

Stage 9 FAILS unless ALL of the following are met:

1. At least 3 concrete failure sequences are articulated and evidenced
2. At least 1 ESG issue is shown to materially constrain capital, customers, or regulators
3. At least 1 human or organizational single point of failure is identified
4. At least 1 third-party shock propagation path is mapped
5. At least 1 false resilience or risk-transfer assumption is explicitly invalidated

––––––––––––––––––––
MANDATORY QA CHECKS (ALL REQUIRED)
––––––––––––––––––––

A) CLAIM / EVIDENCE INTEGRITY CHECK
- Verify each exit-criteria-supporting claim traces to Stage 9.x evidence_refs
- Flag any claim lacking lineage

B) CROSS-SUB-STAGE CONSISTENCY CHECK
- Identify contradictions between ESG, continuity, human fragility, ecosystem shock, and insurance reality
- Preserve contradictions explicitly; do NOT resolve them

C) FAILURE SEQUENCING COVERAGE CHECK
- Confirm failures are sequenced (first, second, third order)
- Missing cascade logic = FAIL

D) HYPOTHESIS DISCIPLINE AUDIT (STAGE 0.3)
- Confirm each sub-stage includes hypotheses with disconfirming searches
- Flag confirmation bias risk explicitly

E) UNCERTAINTY PRESERVATION CHECK
- Confirm UNKNOWN vs UNKNOWABLE distinctions persist
- Confirm uncertainty is not collapsed into reassurance

––––––––––––––––––––
OUTPUT PROTOCOL — MULTI-FILE JSON (MANDATORY)
––––––––––––––––––––

Emit the following files IN ORDER.
Each file must be valid standalone JSON.
Do NOT repeat content.
Do NOT introduce new facts.

------------------------------------------------
FILE 1 — 9.exit_criteria_test.json
------------------------------------------------
{
  "stage": "9",
  "exit_criteria_test": {
    "failure_sequences_identified": { "met": true, "evidence_refs": [], "notes": "" },
    "esg_material_constraint": { "met": true, "evidence_refs": [], "notes": "" },
    "human_or_org_spof": { "met": true, "evidence_refs": [], "notes": "" },
    "third_party_shock_path": { "met": true, "evidence_refs": [], "notes": "" },
    "false_resilience_invalidated": { "met": true, "evidence_refs": [], "notes": "" }
  }
}

------------------------------------------------
FILE 2 — 9.enterprise_failure_map.json
------------------------------------------------
{
  "enterprise_failure_map": {
    "failure_sequences": [],
    "esg_operating_constraints": [],
    "human_and_org_fragilities": [],
    "ecosystem_shock_paths": [],
    "risk_transfer_failures": []
  }
}

------------------------------------------------
FILE 3 — 9.structural_fragility_register.json
------------------------------------------------
{
  "structural_fragility_register": [
    {
      "fragility": "",
      "category": "ESG|CONTINUITY|HUMAN|ECOSYSTEM|INSURANCE",
      "severity": "LOW|MED|HIGH",
      "failure_trigger": "",
      "what_breaks": "",
      "evidence_refs": [],
      "open_unknowns": []
    }
  ]
}

------------------------------------------------
FILE 4 — 9.contradictions_and_tensions.json
------------------------------------------------
{
  "contradictions_and_tensions": [
    {
      "description": "",
      "domains_in_conflict": [],
      "why_it_matters_under_stress": "",
      "evidence_refs": []
    }
  ]
}

------------------------------------------------
FILE 5 — 9.hypothesis_discipline_audit.json
------------------------------------------------
{
  "hypothesis_discipline_audit": [
    {
      "sub_stage": "9.1|9.2|9.3|9.4|9.5",
      "issues_found": [],
      "confirmation_bias_risk": "LOW|MED|HIGH",
      "notes": ""
    }
  ]
}

------------------------------------------------
FILE 6 — 9.uncertainty_preservation_audit.json
------------------------------------------------
{
  "uncertainty_preservation_audit": {
    "unknowns_summary": [],
    "un-knowables_summary": [],
    "material_decision_risks": []
  }
}

------------------------------------------------
FILE 7 — 9.redo_plan_if_failed.json
------------------------------------------------
{
  "redo_plan_if_failed": [
    {
      "sub_stage_to_redo": "9.1|9.2|9.3|9.4|9.5",
      "failure_reason": "",
      "minimum_required_fix": ""
    }
  ]
}

------------------------------------------------
FILE 8 — 9.gate_decision.json
------------------------------------------------
{
  "stage": "9",
  "gate_decision": "PASS|FAIL",
  "summary_rationale": ""
}

––––––––––––––––––––
FAIL CONDITIONS (ANY = FAILURE)
––––––––––––––––––––

Stage 9 has FAILED if:
- Failure is softened into “risk”
- ESG is reduced to reporting rather than constraint
- Human fragility is abstracted
- Third-party shock is treated as isolated
- Insurance is treated as protection without residual risk
- Uncertainty is collapsed
- Outputs could be misused as assurance

STOP.
Do NOT proceed to any subsequent stage within this response.

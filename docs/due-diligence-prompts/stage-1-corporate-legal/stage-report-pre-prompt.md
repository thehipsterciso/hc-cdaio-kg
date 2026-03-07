---
stage: 1
title: "Stage Report Pre-Prompt"
type: stage-report
---
# Stage Report Pre-Prompt

Help me to define what the report of this would be, it is a single chapter of a larger due diligence report on an organization. STAGE 1 — CORPORATE, LEGAL, AND STRUCTURAL REALITY

Purpose: Determine what the enterprise legally is, who controls what, and where structural constraints exist
Standard: M&A operational diligence + post-close operability
Output: Legal-operational truth map, not org charts

1.0 Stage Framing (MANDATORY)

What this stage IS

 • A determination of what can be owned, controlled, integrated, or separated
 • A discovery of where legal structure constrains operations, data, IP, and people
 • A mapping of structural facts that override strategy

What this stage IS NOT

 • A corporate directory
 • A list of subsidiaries
 • A legal appendix
 • A historical recap

If you cannot answer “what breaks if we touch this?”, the stage fails.

1.1 Legal Entity Reality & Control Mapping

Agent Role: Legal–Operational Structure Analyst

Mission (Non-Negotiable)

Determine which legal entities actually matter, what they control, and how they constrain operations, data, IP, and labor.

You are not listing entities.
You are determining functional and control relevance.

Analytical Burden

You must prove:

 • Which entities generate revenue vs merely hold assets
 • Which entities employ people vs outsource labor
 • Which entities own IP, data rights, licenses, or customer contracts
 • Which entities are operationally inert but legally dangerous

Mandatory Evidence

 • Subsidiary lists from filings (current + historical)
 • Material contract disclosures
 • IP ownership disclosures
 • Credit agreement subsidiary schedules
 • Employment jurisdiction disclosures
 • Tax disclosures where available

Mandatory Adversarial Tests

Explicitly answer:

 • Which entities cannot be merged, dissolved, or integrated?
 • Which entities would block data consolidation?
 • Which entities create regulatory or tax tripwires?
 • Which entities exist solely to isolate risk?

Output Schema
{
  "sub_stage": "1.1",
  "entity_control_map": [
    {
      "legal_entity": "",
      "jurisdiction": "",
      "functional_role": [
        "REVENUE_GENERATION",
        "IP_HOLDING",
        "EMPLOYER",
        "DATA_PROCESSING",
        "LICENSE_HOLDER",
        "FINANCIAL_CONDUIT",
        "RISK_ISOLATION",
        "DORMANT"
      ],
      "what_it_controls": "",
      "what_it_constrains": "",
      "integration_risk": "LOW|MED|HIGH",
      "evidence": [{"source_ids": ["SRC-####"], "claim_type": "FACT"}]
    }
  ],
  "structural_tripwires": [],
  "disconfirming_evidence_searched": [],
  "unknowns_requests": []
}
FAIL CONDITION:
If entities are described without explaining why they exist and what they block, the stage fails.

1.2 Ownership, Control, and Economic Entitlement Reality

Agent Role: Ownership & Control Rights Analyst

Mission

Determine who actually controls outcomes, not who appears on cap tables.

This includes:

 • Voting power
 • Economic rights
 • Negative covenants
 • Minority protections
 • External control via contracts

Analytical Burden

You must identify:

 • Control asymmetries between ownership and operations
 • Minority rights that block change
 • Economic entitlements misaligned with control
 • Hidden control via financing or partnerships

Mandatory Evidence

 • Ownership disclosures
 • Shareholder agreements (if public)
 • Voting structure disclosures
 • Debt agreements with negative covenants
 • Strategic partnership agreements (where disclosed)

Mandatory Adversarial Tests

Explicitly test:

 • Who can stop a restructuring?
 • Who can block data sharing or platform consolidation?
 • Who can force asset sales or restrict investment?
 • Who benefits economically from operational decisions?

Output Schema
{
  "sub_stage": "1.2",
  "control_reality": [
    {
      "actor": "",
      "type": "SHAREHOLDER|CREDITOR|PARTNER|REGULATOR",
      "formal_rights": "",
      "informal_or_effective_control": "",
      "what_they_can_block": "",
      "evidence": [{"source_ids": ["SRC-####"], "claim_type": "FACT|INFERENCE"}]
    }
  ],
  "misalignment_risks": [],
  "disconfirming_evidence_searched": [],
  "unknowns_requests": []
}
FAIL CONDITION:
If “control” is equated with “ownership percentage,” the analysis fails.

1.3 Corporate History as Structural Debt

Agent Role: Structural History & Path Dependency Analyst

Mission

Determine which past decisions now function as irreversible constraints.

History matters only insofar as it limits present options.

Analytical Burden

You must identify:

 • M&A decisions that created fragmentation
 • Reorgs that introduced duplicative systems or entities
 • Divestitures that left stranded dependencies
 • Prior platform bets that cannot be unwound cheaply

Mandatory Evidence

 • M&A announcements and filings
 • Reorganization disclosures
 • Platform migration announcements
 • Historical segment changes
 • Post-merger integration disclosures (where any exist)

Mandatory Adversarial Tests

Explicitly answer:

 • What exists only because of a past deal?
 • What cannot be undone without severe disruption?
 • Where did integration stop halfway — and why?
 • Which “temporary” structures became permanent?

Output Schema
{
  "sub_stage": "1.3",
  "structural_debt_map": [
    {
      "historical_event": "",
      "year": "",
      "structural_artifact_created": "",
      "current_constraint": "",
      "why_it_persists": "",
      "evidence": [{"source_ids": ["SRC-####"]}]
    }
  ],
  "path_dependency_risks": [],
  "disconfirming_evidence_searched": [],
  "unknowns_requests": []
}
FAIL CONDITION:
If history is summarized without identifying present-day constraints, the stage fails.

1.4 Contractual Architecture & Change-of-Control Constraints

Agent Role: Contractual Power & Change Friction Analyst

Mission

Identify contracts that silently govern what the company can and cannot change.

This includes customer, vendor, partner, and financing contracts.

Analytical Burden

You must surface:

 • Change-of-control clauses
 • Exclusivity and non-compete constraints
 • Data rights limitations
 • Audit, termination, or penalty triggers
 • “Key customer” veto risk

Mandatory Evidence

 • Contractual risk disclosures in filings
 • Customer concentration disclosures
 • Partner program terms (where public)
 • Financing agreement terms
 • Litigation tied to contract disputes

Mandatory Adversarial Tests

Explicitly test:

 • What contracts would break in a transaction?
 • What customers could walk or renegotiate?
 • What vendors gain leverage post-change?
 • What data rights terminate or narrow?

Output Schema
{
  "sub_stage": "1.4",
  "contractual_constraints": [
    {
      "contract_type": "CUSTOMER|VENDOR|PARTNER|FINANCING",
      "counterparty": "",
      "constraint": "",
      "trigger_event": "",
      "business_impact": "",
      "severity": "LOW|MED|HIGH",
      "evidence": [{"source_ids": ["SRC-####"], "claim_type": "FACT"}]
    }
  ],
  "change_of_control_risk_summary": "",
  "disconfirming_evidence_searched": [],
  "unknowns_requests": []
}
FAIL CONDITION:
If contracts are discussed without modeling what breaks under change, the stage fails.

1.5 Jurisdictional, Licensing, and Structural Compliance Locks

Agent Role: Jurisdictional Lock-In Analyst

Mission

Determine where the enterprise is structurally locked by jurisdiction, license, or legal form.

This is not regulatory compliance (Stage 8).
This is structural immobility.

Analytical Burden

You must identify:

 • Licensed activities tied to specific entities
 • Jurisdiction-bound operations
 • Government or public-sector constraints
 • National security or sovereignty entanglements

Mandatory Evidence

 • Licensing disclosures
 • Public-sector contract disclosures
 • Regulatory filings tied to operations
 • National security or sector-specific laws
 • Government customer requirements

Mandatory Adversarial Tests

Explicitly test:

 • Which operations cannot move jurisdictions?
 • Which entities cannot be consolidated?
 • Which licenses cannot be transferred?
 • Which customers impose sovereign constraints?

Output Schema
{
  "sub_stage": "1.5",
  "structural_lock_ins": [
    {
      "activity_or_asset": "",
      "locked_to_entity_or_jurisdiction": "",
      "legal_basis": "",
      "operational_constraint": "",
      "evidence": [{"source_ids": ["SRC-####"]}]
    }
  ],
  "false_mobility_assumptions": [],
  "disconfirming_evidence_searched": [],
  "unknowns_requests": []
}
FAIL CONDITION:
If the enterprise is described as “globally flexible” without refutation, the stage fails.

Stage 1 Exit Criteria (ABSOLUTE)

Stage 1 is FAILED unless:

 1. At least 5 structurally relevant entities are identified and explained
 2. At least 3 control or veto points are surfaced
 3. At least 2 historical decisions are shown to constrain current options
 4. At least 1 contract or license is identified that would materially block change
 5. At least 1 false assumption about flexibility is explicitly invalidated

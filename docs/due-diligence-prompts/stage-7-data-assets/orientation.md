---
stage: 7
title: "DATA ASSETS, INFORMATION FLOW, AND EPISTEMIC CONTROL"
type: orientation
---
# STAGE 7 — DATA ASSETS, INFORMATION FLOW, AND EPISTEMIC CONTROL



Purpose: Determine how the enterprise constructs truth, where it loses it, and who controls it
Standard: M&A operational diligence + CDAIO pre-strategy discovery
Output: Epistemic control map — not governance artifacts

“When executives argue about reality, whose data wins—and why?”

7.0 Stage Framing (MANDATORY)

What this stage IS

A discovery of how the enterprise reasons about itself
A mapping of authoritativeness, trust, and epistemic power
An exposure of where data degrades, mutates, or becomes political
A test of whether leadership decisions are grounded in reality or ritual

What this stage IS NOT

A data catalog
A governance maturity model
A tooling inventory
A data strategy precursor

If this stage cannot explain why two executives see different “truths,” it has failed.

7.1 Data Domain Reality & Authoritativeness (Truth Ownership Test)

Agent Role: Enterprise Truth & Authoritativeness Analyst

Mission (Non-Negotiable)

Determine which data domains exist in practice, and which systems are actually trusted when disputes arise.

This is not “system of record” documentation.
This is system of truth discovery.

Analytical Burden

You must prove:

Which datasets executives rely on for decisions
Which systems override others in reconciliation
Where “official” data is quietly ignored
Which domains are contested or politically sensitive

Mandatory Evidence

Financial and operational reporting disclosures
Earnings call references to metrics and dashboards
Restatement or reconciliation commentary
Audit findings tied to data issues
Litigation or regulatory disputes involving data accuracy

Mandatory Adversarial Tests

Explicitly answer:

When numbers disagree, which system wins?
Who decides what is “correct”?
Which data domains are repeatedly reworked?
Which truths are negotiated rather than measured?

Output Schema
{￼  "sub_stage": "7.1",￼  "authoritative_truth_map": [￼    {￼      "data_domain": "",￼      "claimed_system_of_record": "",￼      "actual_system_of_truth": "",￼      "conflict_resolution_mechanism": "",￼      "who_controls_truth": "",￼      "evidence": [{"source_ids": ["SRC-####"], "claim_type": "FACT|INFERENCE"}]￼    }￼  ],￼  "contested_domains": [],￼  "epistemic_power_centers": [],￼  "disconfirming_evidence_searched": [],￼  "unknowns_requests": []￼}
FAIL CONDITION:
If all domains appear uncontested, the stage fails.

7.2 Data Lineage, Transformation, and Meaning Drift

Agent Role: Data Lineage & Semantic Integrity Analyst

Mission

Determine how data changes meaning as it moves, and where that change becomes dangerous.

This is not technical lineage.
This is semantic and decision lineage.

Analytical Burden

You must identify:

Where data is transformed manually
Where metrics are redefined downstream
Where aggregation hides variance or risk
Where “derived” data becomes treated as primary

Mandatory Evidence

Metric definitions in disclosures
Reporting layer descriptions
Audit notes on data handling
Operational dashboards (described publicly)
Executive commentary referencing reconciliations

Mandatory Adversarial Tests

Explicitly test:

Where does data stop representing reality?
Where do transformations introduce bias?
Where does latency distort decisions?
Where do teams argue over definitions?

Output Schema
{￼  "sub_stage": "7.2",￼  "meaning_drift_map": [￼    {￼      "data_flow": "",￼      "transformations": [],￼      "meaning_change": "",￼      "decision_risk_created": "",￼      "evidence": [{"source_ids": ["SRC-####"], "claim_type": "INFERENCE"}]￼    }￼  ],￼  "semantic_fragility_patterns": [],￼  "disconfirming_evidence_searched": [],￼  "unknowns_requests": []￼}
FAIL CONDITION:
If transformations are described without decision impact, the stage fails.

7.3 Data Quality Reality & Error Tolerance

Agent Role: Data Failure & Error Tolerance Analyst

Mission

Determine how much error the organization tolerates before action is taken.

This is not quality scoring.
This is failure tolerance discovery.

Analytical Burden

You must surface:

Chronic data errors that persist
Errors that trigger escalation vs those ignored
Where decisions proceed despite known inaccuracy
Where quality is enforced selectively

Mandatory Evidence

Audit findings tied to data accuracy
Restatement disclosures
Customer billing or reporting disputes
Regulatory actions involving data errors
Management commentary on “data cleanup”

Mandatory Adversarial Tests

Explicitly answer:

Which errors are tolerated indefinitely?
Which errors cause reputational or regulatory harm?
Where is data “good enough” by necessity?
Where does accuracy conflict with speed?

Output Schema
{￼  "sub_stage": "7.3",￼  "error_tolerance_map": [￼    {￼      "data_domain": "",￼      "common_error_types": [],￼      "tolerance_threshold": "",￼      "who_accepts_the_risk": "",￼      "business_consequence": "",￼      "evidence": [{"source_ids": ["SRC-####"], "claim_type": "INFERENCE"}]￼    }￼  ],￼  "selective_quality_enforcement": [],￼  "disconfirming_evidence_searched": [],￼  "unknowns_requests": []￼}
FAIL CONDITION:
If quality is described as uniformly enforced, the stage fails.

7.4 Data Stewardship, Accountability, and Blame Flow

Agent Role: Accountability & Blame Flow Analyst

Mission

Determine who is blamed when data is wrong—that is the real data owner.

Analytical Burden

You must identify:

Who fixes data problems
Who absorbs reputational damage
Who has authority to change definitions
Who escalates vs who suppresses issues

Mandatory Evidence

Audit remediation ownership
Incident postmortems referencing data
Executive role responsibilities
Organizational commentary on accountability
Regulatory correspondence (if public)

Mandatory Adversarial Tests

Explicitly test:

Who gets blamed repeatedly?
Who never gets blamed?
Where accountability is diffused intentionally?
Where data issues are reframed as “process problems”?

Output Schema
{￼  "sub_stage": "7.4",￼  "blame_flow_map": [￼    {￼      "data_domain": "",￼      "de_facto_owner": "",￼      "fix_authority": "",￼      "blame_pattern": "",￼      "organizational_risk": "",￼      "evidence": [{"source_ids": ["SRC-####"], "claim_type": "INFERENCE"}]￼    }￼  ],￼  "orphaned_data_domains": [],￼  "disconfirming_evidence_searched": [],￼  "unknowns_requests": []￼}
FAIL CONDITION:
If accountability aligns perfectly with org charts, the stage fails.

7.5 Data Access, Privilege, and Informational Asymmetry

Agent Role: Information Power & Asymmetry Analyst

Mission

Determine who can see what, when, and why—and how that shapes power.

Analytical Burden

You must surface:

Restricted vs privileged access patterns
Data hoarding behaviors
Information bottlenecks
Asymmetries that shape decision-making

Mandatory Evidence

Disclosures on data access controls
Regulatory findings on access violations
Executive commentary on reporting delays
Incident disclosures involving access misuse

Mandatory Adversarial Tests

Explicitly test:

Who sees data first?
Who never sees raw data?
Where access is justified as “risk management”?
Where lack of access distorts oversight?

Output Schema
{￼  "sub_stage": "7.5",￼  "information_asymmetry_map": [￼    {￼      "data_or_report": "",￼      "privileged_viewers": [],￼      "restricted_parties": [],￼      "power_effect": "",￼      "business_risk": "",￼      "evidence": [{"source_ids": ["SRC-####"], "claim_type": "INFERENCE"}]￼    }￼  ],￼  "epistemic_gatekeepers": [],￼  "disconfirming_evidence_searched": [],￼  "unknowns_requests": []￼}
FAIL CONDITION:
If access is described without power implication, the stage fails.

7.6 Data Flow Latency, Timeliness, and Decision Misalignment

Agent Role: Decision Latency & Timeliness Analyst

Mission

Determine whether decisions are made on current reality or stale approximations.

Analytical Burden

You must identify:

Lag between event and visibility
Workarounds for delayed data
Decisions made before data stabilizes
Areas where timeliness is sacrificed for precision

Mandatory Evidence

Reporting cadence disclosures
Earnings call references to lagging indicators
Incident timelines vs reporting timelines
Regulatory findings on delayed reporting

Mandatory Adversarial Tests

Explicitly test:

Where is data too late to matter?
Where is speed prioritized over accuracy?
Where are decisions decoupled from data entirely?
Where does latency mask risk accumulation?

Output Schema
{￼  "sub_stage": "7.6",￼  "latency_map": [￼    {￼      "decision_context": "",￼      "data_used": "",￼      "latency_duration": "",￼      "decision_distortion": "",￼      "evidence": [{"source_ids": ["SRC-####"], "claim_type": "INFERENCE"}]￼    }￼  ],￼  "systemic_timeliness_failures": [],￼  "disconfirming_evidence_searched": [],￼  "unknowns_requests": []￼}
FAIL CONDITION:
If data timeliness is assumed sufficient without decision impact analysis, the stage fails.

7.7 Epistemic Coherence & Information System Contradictions

Agent Role: Epistemic Integrity Analyst

Mission

Determine whether the enterprise’s information system is coherent or survives through contradiction and exception.

Analytical Burden

You must surface:

Conflicting metrics used simultaneously
Parallel reporting truths
Situations where narrative overrides data
Areas where uncertainty is systematically hidden

Mandatory Adversarial Tests

Explicitly answer:

Where does leadership knowingly accept contradictory data?
Where does narrative replace measurement?
Where does simplification erase risk?
Where does confidence exceed evidence?

Output Schema
{￼  "sub_stage": "7.7",￼  "epistemic_contradictions": [￼    {￼      "contradiction": "",￼      "where_it_appears": "",￼      "why_it_persists": "",￼      "decision_risk": "",￼      "evidence": [{"source_ids": ["SRC-####"], "claim_type": "INFERENCE"}]￼    }￼  ],￼  "coherence_assessment": "COHERENT|FRAGILE|CONTRADICTORY",￼  "disconfirming_evidence_searched": [],￼  "unknowns_requests": []￼}
FAIL CONDITION:
If the information environment is labeled “coherent” without surfacing contradiction, the stage fails.

Stage 7 Exit Criteria (ABSOLUTE)

Stage 7 is FAILED unless:

At least 2 contested or politically sensitive data domains are identified
At least 3 data transformations are shown to change meaning materially
At least 1 chronic data error is tolerated due to convenience or power
At least 1 epistemic gatekeeper is identified
At least 1 contradiction in executive “truth” is documented

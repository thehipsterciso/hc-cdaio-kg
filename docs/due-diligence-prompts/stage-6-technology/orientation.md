---
stage: 6
title: "TECHNOLOGY, COMPUTE, AND PLATFORM REALITY"
type: orientation
---
# STAGE 6 — TECHNOLOGY, COMPUTE, AND PLATFORM REALITY



Purpose: Determine where compute, platforms, and systems impose non-negotiable operational constraints
Standard: M&A operational diligence + post-close operability
Output: Control, fragility, and immobility map — not architecture review

“Where does operational control, fragility, and immobility actually live in the technology and compute estate?”

6.0 Stage Framing (MANDATORY)

What this stage IS

A discovery of where the business is technically trapped
A mapping of control points, fragility, and irreversible dependencies
An exposure of where technology prevents change regardless of intent
A test of operational survivability under technical stress

What this stage IS NOT

An architecture assessment
A modernization roadmap
A cloud maturity review
A tooling inventory

If the output could be mistaken for a “current-state architecture,” this stage has failed.

6.1 Compute & Data Center Control Reality

Agent Role: Compute Control & Physical Dependency Analyst

Mission (Non-Negotiable)

Determine where compute physically lives, who controls it, and what breaks if it moves.

This is not a footprint listing.
This is physical and contractual immobility analysis.

Analytical Burden

You must prove:

Which data centers are revenue-critical vs supportive
Which workloads are customer-contractually bound to location
Which facilities are single points of failure
Which teams can actually operate each environment

Mandatory Evidence

Data center disclosures (owned / leased / colo / customer-dedicated)
Customer contract locality requirements (where public)
Regulatory residency references
Outage disclosures tied to facilities
Infrastructure org disclosures
Public sector / regulated customer requirements

Mandatory Adversarial Tests

Explicitly answer:

What happens if this facility is unavailable for 72 hours?
Which customers would immediately breach contracts?
Which environments cannot be failed over?
Which facilities exist solely because exit is impossible?

Output Schema
{￼  "sub_stage": "6.1",￼  "compute_control_map": [￼    {￼      "facility_or_region": "",￼      "compute_type": "OWNED_DC|LEASED_DC|COLO|CLOUD_REGION|CUSTOMER_DEDICATED",￼      "primary_workloads": [],￼      "teams_with_operational_control": [],￼      "immobility_reason": "",￼      "single_point_of_failure": true,￼      "evidence": [{"source_ids": ["SRC-####"], "claim_type": "FACT|INFERENCE"}]￼    }￼  ],￼  "facility_lock_in_risks": [],￼  "disconfirming_evidence_searched": [],￼  "unknowns_requests": []￼}
FAIL CONDITION:
If facilities are described without stating why they cannot be exited or failed over, the stage fails.

6.2 Cloud Dependency, Hyperscaler Power, and Exit Fiction

Agent Role: Cloud Dependency & Exit Reality Analyst

Mission

Determine whether cloud usage represents flexibility or dependency.

This is not “cloud strategy.”
This is dependency asymmetry analysis.

Analytical Burden

You must identify:

Which workloads are technically portable vs trapped
Which contracts create commercial lock-in
Which architectures rely on proprietary services
Where “multi-cloud” is narrative, not reality

Mandatory Evidence

Hyperscaler partnership disclosures
Cloud service certifications and badges
Job postings indicating service-specific expertise
Cost-of-revenue commentary tied to cloud
Incident disclosures involving cloud providers
Public statements on migration or consolidation

Mandatory Adversarial Tests

Explicitly test:

What happens if pricing increases materially?
What happens if a hyperscaler changes terms?
Which workloads cannot move in <24 months?
Where cloud exit costs exceed business value?

Output Schema
{￼  "sub_stage": "6.2",￼  "cloud_dependency_map": [￼    {￼      "provider": "",￼      "workloads_bound": [],￼      "dependency_type": "TECHNICAL|COMMERCIAL|ORGANIZATIONAL",￼      "exit_feasibility": "LOW|MED|HIGH",￼      "exit_cost_signal": "",￼      "evidence": [{"source_ids": ["SRC-####"], "claim_type": "INFERENCE"}]￼    }￼  ],￼  "multi_cloud_fiction_flags": [],￼  "hyperscaler_power_asymmetries": [],￼  "disconfirming_evidence_searched": [],￼  "unknowns_requests": []￼}
FAIL CONDITION:
If cloud is described as “flexible” without exit analysis, the stage fails.

6.3 Platform Criticality, Coupling, and Change Fragility

Agent Role: Platform Fragility & Coupling Analyst

Mission

Determine which platforms the business cannot afford to touch.

This is not system inventory.
This is blast-radius mapping.

Analytical Burden

You must surface:

Platforms that couple multiple LoBs
Platforms that embed business logic deeply
Customizations that block standardization
Platforms whose failure halts revenue

Mandatory Evidence

Platform references in filings
Incident disclosures tied to systems
Product or service descriptions referencing platforms
Hiring for legacy skill sets
Customer documentation referencing system behavior

Mandatory Adversarial Tests

Explicitly test:

What breaks if this platform changes?
Who relies on undocumented behavior?
Where does technical debt become revenue risk?
Which systems cannot be replaced incrementally?

Output Schema
{￼  "sub_stage": "6.3",￼  "platform_fragility_map": [￼    {￼      "platform": "",￼      "business_capabilities_supported": [],￼      "coupling_strength": "LOOSE|MODERATE|TIGHT",￼      "change_risk": "LOW|MED|HIGH",￼      "blast_radius": "",￼      "evidence": [{"source_ids": ["SRC-####"], "claim_type": "INFERENCE"}]￼    }￼  ],￼  "untouchable_systems": [],￼  "disconfirming_evidence_searched": [],￼  "unknowns_requests": []￼}
FAIL CONDITION:
If all platforms appear “manageable,” the stage fails.

6.4 Vendor Lock-In, Licensing, and Commercial Constraint

Agent Role: Technology Vendor Power Analyst

Mission

Determine where vendors exert operational or economic control.

This is not vendor management.
This is power asymmetry analysis.

Analytical Burden

You must identify:

Licensing models that penalize change
Vendors embedded in core operations
Audit or usage enforcement risk
Substitution timelines vs reality

Mandatory Evidence

Licensing disclosures
Vendor concentration disclosures
Litigation or audit disputes
Renewal or renegotiation commentary
Pricing or cost escalation disclosures

Mandatory Adversarial Tests

Explicitly test:

Which vendors can halt operations?
Which vendors gain leverage post-acquisition?
Which licenses punish consolidation?
Which vendors cannot be replaced in <36 months?

Output Schema
{￼  "sub_stage": "6.4",￼  "vendor_control_map": [￼    {￼      "vendor": "",￼      "technology_or_service": "",￼      "control_mechanism": "LICENSING|AUDIT|EXCLUSIVITY|INTEGRATION",￼      "exit_reality": "",￼      "business_risk": "",￼      "evidence": [{"source_ids": ["SRC-####"], "claim_type": "INFERENCE"}]￼    }￼  ],￼  "vendor_power_concentration": [],￼  "disconfirming_evidence_searched": [],￼  "unknowns_requests": []￼}
FAIL CONDITION:
If vendors are described without identifying leverage, the stage fails.

6.5 Technical Debt as Economic and Operational Constraint

Agent Role: Technical Debt & Operational Drag Analyst

Mission

Determine where accumulated technical debt constrains execution and economics.

This is not debt quantification.
This is constraint discovery.

Analytical Burden

You must surface:

Areas where change requires disproportionate effort
Repeated workarounds
Deferred modernization with visible symptoms
Operational incidents linked to aging systems

Mandatory Evidence

Incident and outage disclosures
Repeated remediation commentary
Hiring patterns for legacy technologies
Restructuring tied to “simplification”
Customer complaints referencing reliability

Mandatory Adversarial Tests

Explicitly test:

Where does the business rely on heroics?
Where does debt compound?
Where does fixing one thing break another?
Where is modernization riskier than stagnation?

Output Schema
{￼  "sub_stage": "6.5",￼  "technical_constraint_map": [￼    {￼      "area": "",￼      "debt_manifestation": "",￼      "operational_symptom": "",￼      "economic_impact": "",￼      "why_it_persists": "",￼      "evidence": [{"source_ids": ["SRC-####"], "claim_type": "INFERENCE"}]￼    }￼  ],￼  "compound_debt_risks": [],￼  "disconfirming_evidence_searched": [],￼  "unknowns_requests": []￼}
FAIL CONDITION:
If technical debt is described without business consequence, the stage fails.

6.6 Technology Estate Coherence & Contradiction

Agent Role: Technology Coherence & Integrity Analyst

Mission

Determine whether the technology estate is internally coherent or sustained through contradiction and exception.

Analytical Burden

You must identify:

Conflicting architectural patterns
Parallel stacks doing the same work
Centralization vs decentralization tension
Platforms that exist solely to compensate for others

Mandatory Adversarial Tests

Explicitly answer:

Where does the estate violate its own principles?
Where does scale increase complexity?
Where do exceptions dominate the norm?
Where does technology undermine operating model coherence?

Output Schema
{￼  "sub_stage": "6.6",￼  "estate_contradictions": [￼    {￼      "contradiction": "",￼      "how_it_manifests": "",￼      "why_it_persists": "",￼      "business_risk": "",￼      "evidence": [{"source_ids": ["SRC-####"], "claim_type": "INFERENCE"}]￼    }￼  ],￼  "coherence_assessment": "COHERENT|FRAGILE|CONTRADICTORY",￼  "disconfirming_evidence_searched": [],￼  "unknowns_requests": []￼}
FAIL CONDITION:
If the estate is labeled “coherent” without surfacing tension, the stage fails.

Stage 6 Exit Criteria (ABSOLUTE)

Stage 6 is FAILED unless:

At least 3 immovable or hard-to-exit compute dependencies are identified
At least 2 cloud or platform exit fictions are invalidated
At least 2 platforms are identified as high blast-radius systems
At least 1 vendor is shown to exert structural leverage
At least 1 technical debt area is shown to constrain business outcomes

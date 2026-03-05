# 4.3 Cross Functional Bottlenecks Failure

*Part of [Stage 4: Operating Model Execution](../README.md)*


## Bottlenecks

> **Structural Bottlenecks - Rackspace Technology, Inc.**


### Sub Stage

4.3

### Bottlenecks

**Bottleneck Location:** CEO as sole cross-functional coordinator  

**Why It Is Structural:** Per Stage 4.1: BU Presidents lack authority (Lillie departure, CEO backfill), no standing governance forums (no operating committee, deal review board, risk committee). All cross-functional conflicts, customer escalations, major deals, risk decisions route to CEO for adjudication. Three CEOs in three years indicates role overload persists across leadership changes—not personality-dependent but structurally embedded. Attempts to fix through CEO hiring failed—pattern recurs. Root cause: Authority concentrated at CEO level upward (Apollo controls strategic decisions) and cannot delegate downward (BU Presidents/VPs lack cross-functional authority).

**Failure Symptoms:** Decision delays (issues queue for CEO availability), Throughput ceiling (organizational volume limited by CEO coordination capacity per Stage 4.2), Strategic distraction (CEO consumed by operational escalations), Inconsistent decisions (no governance forum precedents), Customer escalations stall ('cannot reach senior management' per BBB), Major deals require CEO (healthcare $100M+ TCV), Executive turnover (three CEOs suggests overload)

**Systemic Impact:** Organizational unscalability—cannot add volume/complexity without overwhelming CEO. Post-close integration risk—if CEO changes, coordination collapses. Competitive disadvantage—decision velocity slower than competitors with federated authority. Revenue ceiling—large deal throughput limited by CEO capacity. Customer churn—escalations cannot reach decision-maker.
**Claim Type:** `INFERENCE`  

**Evidence Sources:**
  - Stage 4.1: CEO authority concentration
  - Stage 4.2: CEO serial bottleneck
  - Three CEOs three years
  - Healthcare deal CEO involvement
  - BBB: cannot escalate

---

**Bottleneck Location:** CFO capital allocation under debt covenant and Apollo constraints  

**Why It Is Structural:** Debt service ($1.3B First Lien) mandatory and non-discretionary. Apollo performance targets enforced through board oversight. CFO allocates RESIDUAL capital after external obligations met. Not CFO discretion problem—capital shortage problem. Layoffs 2021, 2023 executed quickly (Stage 4.2) but operational investments deferred (AI strategy unfunded Stage 4.2). Root cause: Capital structure (debt burden) and ownership structure (Apollo control with stranded capital) constrain available capital regardless of CFO allocation decisions.

**Failure Symptoms:** Customer support degradation (complaints increasing 2024), Technology investment lag (AI strategy unfunded), Security investments reactive only (post-incident), Repeated layoffs without resolving cost structure (2021, 2023), Revenue decline (-7% FY2024), Competitive gap widening (hyperscalers outpacing investment)

**Systemic Impact:** Operational underinvestment spiral—customer satisfaction degrades, technology lags, security reactive, creating customer churn, revenue decline, financial pressure, requiring more cuts. Competitive disadvantage permanent—cannot invest at pace to differentiate. Post-close value creation impossible—no capital for improvements.
**Claim Type:** `INFERENCE`  

**Evidence Sources:**
  - Stage 4.1: Debt/Apollo constraints
  - Stage 4.2: Budget fast cuts, slow investments
  - $1.3B First Lien
  - Customer complaints 2024
  - AI unfunded
  - FY2024 -7%

---

**Bottleneck Location:** Sales-delivery handoff without profitability enforcement  

**Why It Is Structural:** Per Stage 4.1: Sales has authority to book deals, delivery has accountability for profitability without pre-sale veto authority. Sales organization 400+ reps operate semi-autonomously. CEO 'walk away' policy Q4 2024 attempts centralized profitability discipline but enforcement mechanism unclear at scale. Sales 'refresh' Q3 2024 indicates personnel changes attempted but structural authority gap remains. Root cause: Incentive misalignment (sales rewarded for bookings, delivery accountable for profitability) plus authority mismatch (sales can commit, delivery cannot refuse).

**Failure Symptoms:** Margin erosion (Private Cloud -13%, Public Cloud -3%), Customer execution failures (deals sold delivery cannot profitably execute), Revenue sacrifice (CEO walking away from unprofitable renewals), Sales force turnover/refresh (Q3 2024), FY2024 revenue decline (-7%)

**Systemic Impact:** Negative-value throughput—sales books deals that destroy rather than create value. Delivery capacity consumed serving unprofitable customers. Customer churn from execution failures. Revenue decline as CEO exits unprofitable business. Financial deterioration accelerates despite sales activity.
**Claim Type:** `INFERENCE`  

**Evidence Sources:**
  - Stage 4.1: Sales/delivery authority mismatch
  - Stage 4.2: Negative-value cascade
  - Q4 2024: walk away policy
  - Q3 2024: sales refresh
  - Margins -13%/-3%
  - FY2024 -7%

---

**Bottleneck Location:** Customer support multi-tier escalation without empowered cross-functional coordinator  

**Why It Is Structural:** Per Stage 4.1: No VP Customer Support or Chief Customer Officer disclosed. BU Presidents lack operational authority (Lillie departure suggests). Support tiers have functional authority (process tickets) but lack cross-functional authority (cannot compel billing waiver, delivery prioritization, engineering expedite). Issues requiring cross-functional coordination have no empowered owner below CEO, but CEO cannot scale to individual customer issues. Root cause: Organizational authority gap—coordinator role needed but doesn't exist or lacks authority.

**Failure Symptoms:** Customer complaints: 'multiple tickets, dozens of engineers, no ownership, cannot escalate' (BBB), 'consistently getting worse' (Trustpilot 2024), 'conflicting advice from multiple engineers' (Gartner), Resolution time unbounded for complex issues, SLA gaming (response times met, resolution ignored)

**Systemic Impact:** Customer churn—unresolved issues force migration. Brand damage—public complaints accumulate. Support staff burnout—accountable without authority. Competitive vulnerability—customers experience degrading service. Revenue risk—churn from support failures.
**Claim Type:** `INFERENCE`  

**Evidence Sources:**
  - Stage 4.1: No VP Support/CCO, escalation authority gap
  - Stage 4.2: Coordination overhead exceeds productive work
  - BBB complaints 2024
  - Trustpilot: consistently worse
  - Gartner: conflicting advice

---

**Bottleneck Location:** Multi-jurisdictional deployment requiring separate execution per jurisdiction  

**Why It Is Structural:** Per Stage 1: Regulatory regimes MANDATE isolation—FedRAMP entity-specific, UK Sovereign architecturally isolated, China in-country requirements. Not coordination issue but legal/regulatory ABSOLUTE CONSTRAINT. Cannot consolidate operations without compliance violations. Cannot create shared services across jurisdictions. Every enterprise initiative must be decomposed and executed 5-6 times separately. Root cause: Regulatory frameworks are unchangeable—cannot negotiate with FedRAMP, UK sovereignty requirements, China Cybersecurity Law.

**Failure Symptoms:** 5-6x deployment multiplier (Stage 4.2), Persistent high cost structure despite layoffs (2021, 2023), Technology deployment delays, Security patch coordination overhead, Talent deployment inflexibility (US Government US citizens only, UK Sovereign UK-isolated), M&A integration barriers (acquired entities potentially jurisdictionally fragmented)

**Systemic Impact:** Permanent competitive disadvantage—deployment speed, technology investment pace slower than unified competitors. Permanent cost penalty—cannot achieve economies of scale. Operational complexity—every initiative multiplied 5-6x. Stage 1 conclusion: 'Portfolio of separate businesses, not unified operation'—fundamentally unintegrable.
**Claim Type:** STRUCTURAL_INFERENCE  

**Evidence Sources:**
  - Stage 1: FedRAMP/UK Sovereign/China isolation requirements
  - Stage 4.2: 5-6x deployment multiplier
  - Stage 1: Portfolio not unified operation
  - Layoffs 2021, 2023: costs remain high

---


## Dependency Map

> **Cross-Functional Dependency Map - Rackspace Technology, Inc.**


### Sub Stage

4.3

### Dependency Map

**Upstream Function:** CEO (sole cross-functional decision authority per Stage 4.1)  

**Downstream Function:** All functions requiring cross-functional coordination: Sales-Delivery conflicts, Customer escalations, Technology investments, Risk decisions, Strategic initiatives, BU resource allocation

**Dependency Type:** APPROVAL + ENABLEMENT - CEO must adjudicate all cross-functional disputes and approve all material cross-functional initiatives

**Load Characteristic:** SERIAL BOTTLENECK - CEO can process N decisions per unit time. Load scales with organizational volume and complexity. BU Presidents lack authority (Stage 4.1: Lillie departure, CEO backfill), no standing governance forums exist. All cross-functional coordination routes through single person creating serial dependency. Load increases non-linearly with complexity—simple issues resolve at functional level, complex issues escalate to CEO.

**Failure Propagation Pattern:** SYSTEMIC PARALYSIS - If CEO unavailable/overloaded: (1) Cross-functional decisions queue, (2) Execution stalls awaiting CEO availability, (3) Urgent matters displace important matters in CEO calendar, (4) Decisions made hastily under time pressure or deferred creating cascading delays. Customer escalations cannot reach CEO (per BBB complaints 'cannot escalate to senior management')—queue indefinitely without resolution. Major deals require CEO involvement (healthcare $100M+ TCV example)—large deal throughput limited by CEO capacity. Three CEOs in three years suggests role overloaded—each CEO transition creates 3-6 month coordination disruption as new CEO learns dependencies. Failure propagates SYSTEMICALLY because CEO dependency affects ALL cross-functional work.

**Touch Test What Breaks:** OPERATIONAL + STRATEGIC: If CEO dependency removed (empower BU Presidents, create governance forums), current CEOs may resist authority dilution or organization lacks management capacity for federated structure. If CEO dependency increased (more escalations, more complexity), CEO becomes saturated—throughput plateaus, decisions delay, execution stalls. Current state: CEO already bottleneck (Stage 4.2 finding), adding volume/complexity worsens paralysis. Breakage is SYSTEMIC—all cross-functional work depends on single coordinator who cannot scale.
**Claim Type:** `INFERENCE`  

**Evidence Sources:**
  - Stage 4.1: CEO sole cross-functional decision-maker, no governance forums
  - Stage 4.1: BU Presidents lack authority (Lillie departure, CEO backfill)
  - Stage 4.2: CEO serial bottleneck limits throughput
  - Three CEOs three years: Jones, Maletira, Kandiah
  - Healthcare deal $100M+ TCV: CEO involved
  - Customer complaints: 'cannot escalate to senior management'

---

**Upstream Function:** Sales organization (400+ quota-bearing reps)  
**Downstream Function:** Delivery/Operations teams (provisioning, customer onboarding, ongoing service delivery)  

**Dependency Type:** HANDOFF + CAPACITY - Sales books deals, delivery must execute within sold scope/price/timeline. Delivery dependent on sales for accurate scoping, realistic commitments, profitability review.

**Load Characteristic:** ASYNCHRONOUS WITH AUTHORITY MISMATCH - Sales operates independently (400+ reps), delivery reacts to completed deals. Load on delivery determined by sales booking pace and deal complexity. Sales organization 'refresh' Q3 2024 indicates prior sales team booked without delivery coordination. CEO 'walk away from unprofitable deals' Q4 2024 attempts to insert profitability discipline but enforcement mechanism unclear at 400+ rep scale (Stage 4.1 finding). Load scales with sales volume but VALUE scales negatively when deals unprofitable (margin erosion Private Cloud -13%, Public Cloud -3%).

**Failure Propagation Pattern:** NEGATIVE-VALUE CASCADE - Sales books deal delivery cannot execute profitably → Delivery attempts execution → Discovers unprofitability/unbuildability → Cannot veto (deal signed per Stage 4.1 authority gap) → Executes poorly consuming capacity → Customer complains → Margin erodes → Delivery capacity consumed serving unprofitable customer → Less capacity for profitable customers → Revenue declines as CEO walks away from renewals. Failure originates in sales-delivery authority mismatch (Stage 4.1), propagates through delivery execution failure, cascades to customer churn and financial deterioration. Pattern persisted until sales 'refresh' Q3 2024 and CEO policy Q4 2024—indicates systemic not isolated failure. FY2024 revenue -7% as CEO sacrifices revenue to stop margin bleed demonstrates failure propagation to financial outcomes.

**Touch Test What Breaks:** FINANCIAL + OPERATIONAL: If sales-delivery dependency strengthened (delivery pre-approval required), sales throughput drops, revenue declines further. If dependency weakened (sales continues booking without delivery input), margin erosion accelerates, customer execution failures multiply, churn increases. Current state: Dependency already broken (Stage 4.1 authority mismatch, Stage 4.2 handoff failure). Repair requires either (1) Delivery veto authority pre-sale, OR (2) Sales compensation tied to delivered profitability not bookings, OR (3) Deal review board with profitability enforcement. None disclosed—dependency remains structurally broken.
**Claim Type:** `INFERENCE`  

**Evidence Sources:**
  - Stage 4.1: Sales authority vs delivery accountability mismatch
  - Stage 4.2: Sales-delivery handoff negative-value throughput
  - Q4 2024: CEO 'walk away from unprofitable deals'
  - Q3 2024: Sales organization refresh
  - FY2024 revenue -7%, margin erosion -13%/-3%
  - 400+ quota-bearing reps (SEC filings)

---

**Upstream Function:** Customer support tiers (Tier 1 → Tier 2/3 technical → Billing/Delivery/Engineering as needed)  
**Downstream Function:** Customer satisfaction, retention, renewal revenue  

**Dependency Type:** SERIAL ESCALATION + CROSS-FUNCTIONAL COORDINATION - Customer issues requiring multiple functions (billing + technical + service) must coordinate across support tiers and functional boundaries without empowered coordinator.

**Load Characteristic:** COORDINATION OVERHEAD SCALES EXPONENTIALLY WITH COMPLEXITY - Simple single-function issues resolve at appropriate tier. Complex cross-functional issues create combinatorial coordination requirements: 'dozens of engineers' per BBB complaint, 'multiple tickets' per customer, re-explanation required at each handoff. Load measured as ticket volume appears manageable (SLA response times 15min/1hr/4hr met), but load measured as coordination effort for complex issues unbounded. No single owner (Stage 4.1: no VP Customer Support/CCO), cannot escalate to empowered decision-maker. Coordination load consumes capacity without producing resolution (Stage 4.2 finding).

**Failure Propagation Pattern:** INFINITE LOOP WITH CUSTOMER LOSS - Customer issue requires cross-functional coordination → Opens ticket Tier 1 → Tier 1 cannot resolve, escalates Tier 2 → Tier 2 identifies need for billing/delivery/engineering → No coordination mechanism exists (Stage 4.1 authority gap) → Ticket bounces between functions → Customer opens multiple tickets, re-explains to 'dozens of engineers' → No single owner emerges → Customer complains publicly (BBB, Trustpilot) → Issue remains unresolved → Customer churns. Failure originates in coordination authority gap (Stage 4.1), propagates through support tier inability to coordinate, cascades to customer churn and revenue loss. Pattern spans multiple complaint platforms and time periods (BBB, Trustpilot, Gartner 2024)—indicates systemic not isolated failure. Trustpilot: 'consistently getting worse' 2024 indicates failure propagation accelerating not stabilizing.

**Touch Test What Breaks:** OPERATIONAL + RISK: If support dependency structure maintained (multi-tier without empowered coordinator), customer churn accelerates as complex issues multiply. If support tiers eliminated or consolidated, coordination may worsen as specialized expertise removed without addressing root cause (authority gap). Current state: Dependency structure creates failure propagation mechanism—complex issues CANNOT resolve within current structure regardless of support capacity or process improvements. Requires organizational authority redesign (Stage 4.1 finding) not process optimization. Breakage is STRUCTURAL—dependency architecture itself creates failure, not execution within architecture.
**Claim Type:** `INFERENCE`  

**Evidence Sources:**
  - Stage 4.1: Customer escalation authority gap, no VP Support/CCO
  - Stage 4.2: Support coordination overhead exceeds productive work
  - BBB: 'multiple tickets, dozens of engineers, no ownership'
  - Trustpilot: 'consistently getting worse' 2024
  - SLA: 15min/1hr/4hr response, resolution time undefined
  - Gartner Peer Insights: conflicting advice from multiple engineers

---

**Upstream Function:** Multi-jurisdictional regulatory regimes (FedRAMP, UK Sovereignty, China Cybersecurity Law, GDPR, etc.)  
**Downstream Function:** Operations, Technology deployment, Talent deployment, Cost structure optimization, M&A integration  

**Dependency Type:** ABSOLUTE CONSTRAINT - Regulatory requirements mandate entity isolation, infrastructure separation, personnel restrictions. Not coordination issue—legal/regulatory VETO authority.

**Load Characteristic:** STRUCTURAL MULTIPLIER - Every enterprise-wide initiative must be decomposed and executed separately across 5-6 jurisdictions: US Government (FedRAMP-isolated), UK Sovereign (architecturally isolated), China (in-country isolated), EU Commercial, US Commercial, APAC. Technology updates, security patches, process improvements require separate planning, testing, deployment, validation per jurisdiction. Load multiplies linearly with jurisdiction count (5-6x) but coordination complexity multiplies combinatorially. Cannot consolidate operations (cost reduction) without violating compliance. Cannot offshore talent flexibly (US Government requires US citizens, UK Sovereign requires UK-isolated teams). Cannot integrate acquisitions fully if customers span jurisdictions.

**Failure Propagation Pattern:** PERMANENT FRAGMENTATION - Operations attempts cost optimization → Identifies consolidation opportunity → Realizes cannot consolidate without violating FedRAMP/UK Sovereignty/China requirements → Must maintain duplicate infrastructure/support/compliance per jurisdiction → Layoffs (2021, 2023) reduce headcount but cannot eliminate structural cost drivers → Cost structure remains high despite cuts → Financial pressure persists → Next layoff cycle required. Technology team plans deployment → Realizes must deploy separately to each jurisdiction → Deployment duration and cost multiply 5-6x → Competitive disadvantage vs hyperscalers deploying unified infrastructure → Technology gap widens. Failure originates in regulatory mandates (Stage 1 structural constraints), propagates through operational inability to consolidate, cascades to persistent high costs and competitive disadvantage. Not fixable—regulatory constraints are absolute and cannot be negotiated (Stage 1 finding).

**Touch Test What Breaks:** OPERATIONAL + COMPETITIVE: If regulatory dependencies removed (attempt consolidation), immediate compliance violations: FedRAMP authorizations invalidate, UK Sovereign customers lose compliant provider, China operations violate Cybersecurity Law. If regulatory dependencies maintained, permanent cost structure penalty (cannot achieve economies of scale), permanent competitive disadvantage (deployment speed, technology investment pace), permanent M&A integration barriers. Current state: Dependency is STRUCTURAL CONSTRAINT not coordination issue. Stage 1 conclusion: 'Portfolio of separate businesses, not unified operation.' Breakage is STRUCTURAL—regulatory dependencies create absolute barriers to operational optimization.
**Claim Type:** STRUCTURAL_INFERENCE  

**Evidence Sources:**
  - Stage 1: FedRAMP entity-specific, invalidates on change of control
  - Stage 1: UK Sovereign architecturally isolated by design
  - Stage 1: China Cybersecurity Law in-country requirements
  - Stage 1: 'Portfolio of separate businesses'
  - Stage 4.2: Multi-jurisdictional 5-6x deployment multiplier
  - Layoffs 2021, 2023: Cost structure remains high despite cuts

---

**Upstream Function:** CFO/Finance (capital allocation, budget approval)  
**Downstream Function:** Technology investment, Customer support capacity, Sales capacity, Security investments, M&A, Strategic initiatives  

**Dependency Type:** APPROVAL + CAPACITY ALLOCATION - All discretionary spending requires CFO/Finance approval. Budget priorities set by external constraints (debt service mandatory, Apollo performance targets) not operational needs.

**Load Characteristic:** EXTERNALLY CONSTRAINED ALLOCATION - Debt service ($1.3B First Lien) takes absolute priority, reducing discretionary capital. Apollo performance requirements enforce margin discipline. Load on downstream functions determined by capital availability AFTER external obligations met. Budget allocation fast for CUTS (layoffs 2021, 2023 announced and executed within quarter per Stage 4.2), slow or never for INVESTMENTS (AI strategy Q3 2024, capital allocation still unclear Q4 2024 per Stage 4.2). Revealed priority order: Debt service > Apollo targets > Cost reduction > Revenue growth > Customer satisfaction > Technology differentiation.

**Failure Propagation Pattern:** OPERATIONAL UNDERINVESTMENT SPIRAL - Operational function requests budget (support needs capacity, technology needs infrastructure, security needs proactive controls) → CFO evaluates capital availability → Debt service and Apollo targets consume available capital → Operational investment deferred or denied → Customer support quality degrades (complaints increasing 2024 per Stage 4.2), technology investment lags (AI strategy unfunded per Stage 4.2), security investments reactive only (post-incident spending per Stage 4.2) → Operational degradation creates customer churn → Revenue declines (-7% FY2024) → Financial pressure intensifies → Next budget cycle repeats with less capital available. Failure originates in capital structure (debt burden) and ownership structure (Apollo control per Stage 4.1), propagates through CFO capital allocation priorities, cascades to operational underinvestment, customer dissatisfaction, revenue decline. Pattern self-reinforcing—financial deterioration begets underinvestment begets further deterioration.

**Touch Test What Breaks:** FINANCIAL + COMPETITIVE: If CFO dependency eliminated (unrestricted capital access), debt covenant violations trigger default, Apollo intervention likely. If CFO dependency maintained with current capital constraints, operational underinvestment continues, competitive gap widens, customer churn accelerates. Current state: Dependency structurally constrained by external obligations (debt, Apollo) not CFO discretion. CFO allocates LIMITED capital, cannot create additional capital. Breakage is STRUCTURAL—capital shortage not allocation process creates failure. Fixing requires either debt restructuring (difficult given valuation) or Apollo capital injection (unlikely given stranded capital per Stage 4.1).
**Claim Type:** `INFERENCE`  

**Evidence Sources:**
  - Stage 4.1: Debt covenants and Apollo control constrain capital allocation
  - Stage 4.2: Budget allocation fast for cuts, slow for investments
  - Debt service: $1.3B First Lien (Stage 1)
  - Customer support degrading: BBB, Trustpilot 2024
  - Technology investment constrained: AI strategy unfunded
  - FY2024 revenue -7%
  - Layoffs 2021, 2023: Quick execution

---

**Upstream Function:** Security/Operations teams (incident detection, response, remediation)  
**Downstream Function:** Customer trust, Regulatory compliance (FedRAMP, HIPAA/HITRUST), Service availability, Operational monitoring  

**Dependency Type:** REACTIVE RESPONSE + VENDOR DEPENDENCY - Security incidents require coordinating: Operations, Security, Engineering (patches), Legal/Compliance (regulatory reporting), Communications (customer notification), External vendors (ScienceLogic monitoring platform, security consultants).

**Load Characteristic:** EVENT-DRIVEN CRISIS WITH VENDOR DEPENDENCY - No proactive risk governance (Stage 4.1: no CRO, reactive only). Load spikes when incidents occur (ransomware Dec 2022, zero-day Sept 2024). Coordination must occur across multiple functions without standing incident response process. Sept 2024 zero-day in ScienceLogic EM7 monitoring platform created VENDOR DEPENDENCY—Rackspace cannot remediate without vendor patch, remediation timeline controlled externally. Incident response duration: Dec 2022 ransomware 'multi-month customer impact,' Sept 2024 zero-day duration unclear but monitoring offline during remediation creates operational blind spot.

**Failure Propagation Pattern:** INCIDENT TRIGGERS CAPACITY DISPLACEMENT - Incident detected → Operations/Security/Engineering mobilized → Regular work deprioritized → Incident response coordination without standing process → Extended remediation (multi-month for ransomware) → Reactive spending authorized crowding out strategic investment (Stage 4.2) → Monitoring/security infrastructure degraded during incident (Sept 2024 dashboards offline) → Increased vulnerability during remediation → Incident response completes → Organization returns to reactive posture → Next incident recurs. Failure originates in absence of proactive risk governance (Stage 4.1), propagates through crisis response displacing operational execution, cascades to strategic project delays, customer trust erosion, regulatory risk. Customer complaint: 'no apology, compensation, or solution' (BBB) indicates incident response doesn't include customer remediation protocol—failure propagates to customer relationships.

**Touch Test What Breaks:** RISK + OPERATIONAL: If security dependency strengthened (proactive security governance), requires capital investment Rackspace cannot fund (constrained by debt/Apollo per above). If security dependency maintained (reactive only), incidents recur, customer trust erodes, regulatory authorizations at risk (FedRAMP requires timely incident management). Current state: Dependency on reactive security response creates recurring failure pattern. Vendor dependency (ScienceLogic) creates external bottleneck—Rackspace cannot control remediation pace for platform-level vulnerabilities. Breakage is SYSTEMIC—reactive posture guarantees incident recurrence, each incident displaces operational capacity creating vulnerability to next incident.
**Claim Type:** `INFERENCE`  

**Evidence Sources:**
  - Stage 4.1: No CRO, reactive risk governance
  - Stage 4.2: Security incidents displace proactive execution
  - Dec 2022 ransomware: multi-month customer impact
  - Sept 2024 zero-day ScienceLogic EM7: monitoring offline
  - BBB: 'no apology, compensation, or solution'
  - Vendor dependency: ScienceLogic monitoring platform

---

**Upstream Function:** Apollo Global Management (57% owner, board representation)  

**Downstream Function:** Strategic direction (M&A, divestitures, go-private review), CEO appointments, Capital structure decisions, Business model strategy (requiring board approval)

**Dependency Type:** ABSOLUTE CONTROL - Apollo 57% voting majority provides veto authority over all shareholder decisions. Board includes Apollo representatives (Vikram Mahidhar currently, David Sambur historically per Stage 4.1).

**Load Characteristic:** STRATEGIC VETO WITH MISALIGNED INCENTIVES - Apollo's stranded capital position (paid $4.3B 2016, current stake worth ~$68M per Stage 4.1) creates misalignment with public shareholders (43-47% ownership). Apollo decisions optimize for capital recovery from stranded position, not growth/market cap appreciation. Strategic review (2022-2023) initiated by Apollo-controlled board, abandoned mid-2023 when no acceptable buyer found—consumed 12-18 months organizational capacity with zero output (Stage 4.2). CEO transitions (Jones exit 2022, Maletira to Kandiah 2025) Apollo-directed. Load on downstream functions determined by Apollo's capital recovery strategy not operational effectiveness requirements.

**Failure Propagation Pattern:** STRATEGIC PARALYSIS WITH FINANCIAL CONSTRAINTS - Management proposes growth strategy requiring capital investment → Apollo evaluates against capital recovery objectives → Investment denied or constrained → Strategy execution capital-starved → Competitive positioning erodes → Financial performance deteriorates → Management proposes cost cuts to satisfy Apollo → Operational quality degrades → Customer churn accelerates → Revenue declines → Apollo maintains control seeking capital recovery → Cycle repeats. Failure originates in ownership structure (Apollo control with stranded capital per Stage 4.1), propagates through strategic decision constraints and capital starvation, cascades to competitive disadvantage and operational underinvestment. Three CEOs in three years suggests management inability to execute turnaround under Apollo constraints—each CEO attempts strategy, encounters capital/strategic constraints, exits or transitions. Pattern: Strategies announced (services-led, AI positioning) but execution capital-constrained.

**Touch Test What Breaks:** STRATEGIC + FINANCIAL: If Apollo dependency removed (Apollo exits position), requires buyer willing to pay Apollo's recovery price OR Apollo accepts massive loss. Market unwilling at Apollo's price (strategic review 2022-2023 failed), Apollo unwilling to accept loss (still holding after 8+ years since 2016 acquisition). If Apollo dependency maintained, strategic options constrained by Apollo's capital recovery objectives, growth strategies underfunded, operational investments deferred. Current state: Dependency is STRUCTURAL OWNERSHIP CONSTRAINT. Public shareholders (43-47%) have economic exposure without decision authority. Breakage is STRUCTURAL—ownership structure creates misaligned decision-making that cannot be fixed without ownership change.
**Claim Type:** FACT + INFERENCE  

**Evidence Sources:**
  - Stage 4.1: Apollo 57% voting control, stranded capital $4.3B cost vs $68M value
  - Stage 4.2: Strategic review 2022-2023, 12-18 months, abandoned
  - Three CEOs three years: Jones, Maletira, Kandiah
  - Apollo board representation: Mahidhar current, Sambur historical
  - AI strategy articulated but capital allocation unclear
  - FY2024 revenue -7%

---


## Disconfirming Evidence Searched

> **Disconfirming Evidence Search Log - Dependencies & Failure Propagation**


### Sub Stage

4.3

### Disconfirming Evidence Searched

**Hypothesis Tested:** H4.3-A: Dependency density drives execution failure more than functional capacity/skill  

**Disconfirming Evidence Sought:** Execution failures attributed to skill/capacity deficits, Successful cross-functional coordination examples, Throughput improvements from capacity additions

**Search Conducted:** Reviewed customer complaints for skill deficit mentions, Examined reorganization rationale for capacity vs coordination focus, Analyzed layoff patterns (if capacity problem, adding headcount would help), Searched for successful cross-functional project examples

**Evidence Found:** NONE disconfirming. Customer complaints cite coordination ('dozens of engineers, no ownership') not skill. Layoffs 2021, 2023 reduced capacity but throughput worsened—confirms coordination not capacity is constraint. No successful cross-functional coordination examples found. Reorganization 2023 created BU structure but authority gaps persist.
**Conclusion:** Disconfirming evidence NOT FOUND. Hypothesis remains supported.  

---

**Hypothesis Tested:** H4.3-B: Bottlenecks are structural not incidental  

**Disconfirming Evidence Sought:** Bottlenecks resolved through process improvements, Leadership changes resolving bottlenecks, Temporary resource constraints (not persistent structural)

**Search Conducted:** Tracked bottleneck persistence across leadership changes (three CEOs), Examined process change outcomes (strategic review, reorganization, layoffs), Searched for bottleneck resolution evidence, Analyzed whether constraints temporary or permanent

**Evidence Found:** NONE disconfirming. CEO bottleneck persists across three CEOs. Sales-delivery bottleneck persists despite sales refresh. Capital bottleneck rooted in debt/Apollo (structural). Multi-jurisdictional bottleneck rooted in regulations (unchangeable). Process changes (review, reorganization, layoffs) didn't resolve bottlenecks.

**Conclusion:** Disconfirming evidence NOT FOUND. All bottlenecks persist, are rooted in structural constraints. Hypothesis remains supported.

---

**Hypothesis Tested:** H4.3-C: Heroics mask systemic failures until crisis  

**Disconfirming Evidence Sought:** Proactive failure recognition, Activity/outcome metrics aligned, Management visibility into masked failures before crisis

**Search Conducted:** Examined timing of corrective actions (walk away, sales refresh—reactive or proactive?), Compared activity metrics (SLA, bookings, tickets) vs outcomes (satisfaction, margins, revenue), Searched for early warning indicators management acted on proactively

**Evidence Found:** NONE disconfirming. Corrective actions crisis-driven: Walk away policy Q4 2024 after margins eroded severely, Sales refresh Q3 2024 after pattern established. Activity/outcome divergence clear: SLA met but satisfaction declining, Sales bookings stable but margins eroding. No proactive recognition evidence.

**Conclusion:** Disconfirming evidence NOT FOUND. Pattern confirms heroics mask failures until crisis forces recognition. Hypothesis remains supported.

---


## Hypotheses

> **Dependency & Failure Propagation Hypotheses**


### Sub Stage

4.3

### Hypothesis Framework


#### Dependency density (number and complexity of cross-functional dependencies) is primary driver of execution failure—not functional capacity or skill deficits

**Hypothesis Id:** H4.3-A  
**Type:** STRUCTURAL  

**Supporting Evidence Sought:**
  - Customer issues requiring cross-functional coordination stalling despite functional expertise available
  - Sales-delivery handoff failures despite both functions having capacity
  - Security incident response delays from coordination not technical capability
  - CEO bottleneck from coordination load not decision quality

**Disconfirming Evidence Sought:**
  - Evidence of execution failures from functional skill/capacity deficits rather than coordination
  - Successful cross-functional coordination examples
  - Throughput improvements from adding functional capacity without addressing coordination

**Evidence Found:**

**Supporting:**
    - BBB: dozens of engineers (capacity exists) but coordination fails
    - Sales 400+ reps, delivery has capacity, but handoff creates margin erosion
    - Security incidents require multi-function coordination creating extended remediation
    - CEO coordination load limits throughput despite functional teams having capacity

**Disconfirming:**
    - No evidence of functional skill deficits as primary constraint
    - No successful cross-functional coordination examples found
    - Layoffs reduced capacity but throughput worsened—suggests coordination not capacity is constraint
**Status:** ✅ SUPPORTED  

**Notes:** Multiple failure patterns indicate coordination, not functional capacity/skill, drives failure. Adding capacity (sales reps, support staff) doesn't improve throughput when coordination constrains.

---


#### Bottlenecks are structural (authority architecture, regulatory constraints, capital structure) not incidental (temporary resource constraints or process inefficiencies)—cannot be resolved through process improvement or temporary capacity additions

**Hypothesis Id:** H4.3-B  
**Type:** STRUCTURAL  

**Supporting Evidence Sought:**
  - Bottlenecks persisting across leadership changes (three CEOs)
  - Bottlenecks persisting despite process changes (reorganization, layoffs)
  - Bottlenecks rooted in external constraints (debt, Apollo, regulations)
  - Attempted fixes failing (sales refresh, walk away policy—symptoms addressed not root causes)

**Disconfirming Evidence Sought:**
  - Bottlenecks resolved through process improvements
  - Bottlenecks eliminated by capacity additions
  - Temporary resource constraints causing bottlenecks
  - Leadership changes resolving bottlenecks

**Evidence Found:**

**Supporting:**
    - CEO bottleneck persists across three CEOs—Jones, Maletira, Kandiah
    - Sales-delivery bottleneck persists despite sales refresh Q3 2024
    - Capital allocation bottleneck rooted in debt structure ($1.3B) and Apollo control
    - Multi-jurisdictional bottleneck rooted in regulatory mandates (FedRAMP, UK, China)
    - Strategic review 2022-2023, reorganization 2023, layoffs 2021/2023—none resolved bottlenecks

**Disconfirming:**
    - No evidence of bottlenecks resolved through process/capacity fixes
    - No evidence of temporary constraints—all persist over years
**Status:** ✅ SUPPORTED  

**Notes:** Bottlenecks persist despite leadership changes, reorganizations, process improvements—indicates structural not incidental. Rooted in authority architecture, regulatory constraints, capital structure—cannot fix without structural redesign.

---


#### Failure absorption through heroics masks systemic fragility—creates illusion of operational stability while structural failures accumulate invisibly until crisis forces recognition

**Hypothesis Id:** H4.3-C  
**Type:** STRUCTURAL  

**Supporting Evidence Sought:**
  - Support staff heroics masking coordination authority gap
  - Delivery absorbing sales failures through margin erosion
  - CEO absorbing all cross-functional coordination personally
  - Operations absorbing security governance absence through reactive crisis management
  - Activity metrics stable while outcome metrics degrade

**Disconfirming Evidence Sought:**
  - Failure surfacing promptly without heroics masking
  - Outcome metrics aligned with activity metrics
  - Management visibility into masked failures
  - Proactive problem recognition before crisis

**Evidence Found:**

**Supporting:**
    - SLA response times met (activity) while customer satisfaction declining (outcome)
    - Sales bookings stable (activity) while margins eroding (outcome)
    - Support processing tickets (activity) while customers complaining unresolved (outcome)
    - CEO intervention masking governance absence until three CEOs in three years indicates unsustainable
    - Failure recognition delayed until crisis: FY2024 -7%, CEO walk away policy, sales refresh

**Disconfirming:**
    - No evidence of proactive failure recognition
    - No evidence of activity/outcome alignment
    - Crisis-driven recognition pattern (walk away, sales refresh) confirms masking until severe
**Status:** ✅ SUPPORTED  

**Notes:** Multiple failure absorption mechanisms identified. Heroics create stability illusion—activity metrics stable, outcome metrics degrading. Recognition delayed until crisis (revenue decline, margin erosion, CEO intervention required). Dangerous pattern—post-close integration will disrupt heroics, exposing masked failures suddenly.

---


## Masked Failure Points

> **Masked Failure Points - Rackspace Technology, Inc.**


### Sub Stage

4.3

### Masked Failure Points

**Area:** Support staff absorbing customer coordination failures through heroics  

**How Failure Is Absorbed:** Support engineers attempt to resolve cross-functional customer issues despite lacking authority to compel billing, delivery, engineering action. Engineers work across multiple tickets, communicate with 'dozens' of colleagues (per BBB), manually coordinate without formal process or authority. Support staff absorbs coordination failure through overtime, informal relationships, personal intervention—masking organizational authority gap. SLA response times met (15min/1hr/4hr) masking that resolution times unbounded for complex issues. Activity metrics (tickets processed) mask outcome metrics (customer satisfaction plummeting).

**Why It Is Dangerous:** Support staff burnout inevitable—cannot sustain heroics indefinitely. Informal coordination non-scalable—dependent on individual relationships not process. Failure masked from management—SLA metrics show 'green' while customer satisfaction degrades. When support staff churn/burnout occurs, informal coordination breaks completely—no process to fall back on. Customer complaints indicate pattern worsening ('consistently getting worse' Trustpilot 2024)—suggesting heroics failing to mask failure adequately.

**Downstream Risk:** Support staff attrition creates coordination collapse—informal networks dissolve. Customer churn accelerates as heroics capacity depleted. Management unaware of severity—SLA metrics misleading. Crisis emerges suddenly when heroics capacity exhausted—appears as sudden degradation but actually long-masked structural failure. Post-close integration amplifies risk—integration disrupts informal networks, heroics cannot scale to increased load.
**Claim Type:** `INFERENCE`  

**Evidence Sources:**
  - Stage 4.2: Support coordination overhead
  - BBB: dozens of engineers involved
  - SLA response times vs resolution failures
  - Trustpilot: consistently worse 2024
  - Stage 4.1: No VP Support/empowered coordinator

---

**Area:** Delivery teams absorbing sales-delivery coordination failures through rework and margin erosion  

**How Failure Is Absorbed:** Delivery teams attempt to execute deals sales booked without profitability review. When unprofitability/unbuildability discovered, delivery absorbs failure through: Margin erosion (executing unprofitably), Rework (post-signature deal modifications), Customer execution failures (poor delivery), Capacity consumption (unprofitable customers consume resources). Delivery absorbs sales authority failure rather than refusing execution—masks coordination breakdown until financial deterioration severe (margins -13%/-3%, revenue -7% FY2024) forcing CEO intervention Q4 2024.

**Why It Is Dangerous:** Margin erosion compounds—each unprofitable deal destroys value. Delivery capacity consumed by unprofitable customers—less available for profitable ones. Customer execution failures create churn—compounds revenue decline. Failure masked from sales organization—sales continues booking unprofitable deals until CEO intervenes. Sales 'refresh' Q3 2024 indicates personnel changes required—suggests masking allowed misaligned behavior to persist. Financial deterioration accelerates invisibly until crisis forcing drastic action (walk away from business, sacrifice revenue).

**Downstream Risk:** Financial deterioration accelerates—margins compress, revenue declines. Delivery capacity exhausted serving unprofitable customers—profitable growth impossible. Customer churn from execution failures. Sales force misalignment persists until personnel changes—cultural/incentive issue entrenched. CEO forced to choose between revenue and profitability—walked away from unprofitable renewals sacrificing FY2024 -7% revenue. Competitive position erodes—cannot grow profitably, cannot invest in differentiation. Post-close acquirer inherits margin destruction pattern—unless sales-delivery authority realigned, acquisition value destroyed.
**Claim Type:** `INFERENCE`  

**Evidence Sources:**
  - Stage 4.1: Sales/delivery authority mismatch
  - Stage 4.2: Negative-value cascade
  - Margins -13%/-3%
  - FY2024 -7%
  - Q3 2024: sales refresh
  - Q4 2024: walk away policy

---

**Area:** CEO absorbing cross-functional coordination failures through escalation processing  

**How Failure Is Absorbed:** CEO adjudicates all cross-functional conflicts because no governance layer exists (Stage 4.1: no operating committee, deal review board). BU Presidents lack authority so issues escalate to CEO. CEO absorbs coordination failure through personal intervention: Major deals (healthcare $100M+ TCV), Customer escalations (though many cannot reach CEO per BBB), Strategic decisions, Risk decisions during incidents. CEO serial processing (Stage 4.2) masks parallel coordination requirement—creates illusion organization can coordinate when actually CEO doing all coordination personally. Three CEOs in three years suggests heroics unsustainable—role overloaded.

**Why It Is Dangerous:** CEO capacity finite—throughput plateaus at CEO coordination limit regardless of functional capacity additions. CEO becomes bottleneck not leader—consumed by coordination not strategy. Coordination non-scalable—adding organizational volume/complexity overwhelms CEO. Each CEO transition creates coordination collapse—new CEO must rebuild informal coordination patterns. Three CEOs three years indicates pattern unsustainable—suggests CEO heroics failing to mask coordination gaps adequately. Customer complaints 'cannot escalate to senior management' indicates CEO heroics already failing for customer escalations—CEO coordination capacity exceeded.

**Downstream Risk:** Organizational unscalability—cannot grow beyond CEO coordination capacity. CEO turnover creates coordination crisis—each transition disrupts. Strategic focus impossible—CEO consumed by operational coordination. Decision delays accumulate—CEO queue lengthens, execution stalls. Post-close integration amplifies—additional coordination load overwhelms CEO heroics. Acquirer cannot rely on CEO coordination—structural governance required but doesn't exist. If CEO leaves post-close, coordination collapses completely—no governance infrastructure to sustain coordination.
**Claim Type:** `INFERENCE`  

**Evidence Sources:**
  - Stage 4.1: CEO sole cross-functional authority
  - Stage 4.2: CEO serial bottleneck
  - Three CEOs three years
  - Healthcare deal: CEO involvement
  - BBB: cannot escalate to CEO
  - BU Presidents lack authority

---

**Area:** Operations teams absorbing security/risk failures through reactive crisis management  

**How Failure Is Absorbed:** No proactive risk governance (Stage 4.1: no CRO, no risk committee). Security incidents handled through ad hoc crisis mobilization. Operations/security/engineering teams absorb risk governance failure by: Responding reactively to incidents, Working extended hours during crises (ransomware multi-month impact, zero-day remediation), Deprioritizing regular work to handle incidents (Stage 4.2: reactive crisis displaces proactive execution), Coordinating informally across functions without standing process. Teams absorb risk governance absence through heroics—masking that proactive controls unfunded, incident response process non-existent, vendor dependencies (ScienceLogic) create external constraints.

**Why It Is Dangerous:** Incident response heroics non-repeatable—each incident requires re-mobilization. Team burnout from crisis cycles—extended incident response hours unsustainable. Regular work displaced—strategic projects delayed, proactive security investments deferred. Vendor dependencies create external bottlenecks—ScienceLogic zero-day remediation timeline controlled externally, Rackspace dependent. Reactive spending crowds out proactive investment—each incident forces spending that could have prevented incident if allocated proactively (Stage 4.2). Regulatory risk increases—FedRAMP, HIPAA/HITRUST require proactive controls, reactive-only posture creates authorization risk.

**Downstream Risk:** Incident recurrence inevitable—reactive posture doesn't prevent, only responds. Customer trust erosion—multi-month impacts, 'no apology or solution' per BBB. Regulatory authorization risk—FedRAMP, UK Sovereign, HIPAA/HITRUST require timely incident management. Team attrition from crisis burnout. Monitoring degradation during incidents (Sept 2024 dashboards offline)—creates operational blind spots. Post-close integration amplifies—additional systems/customers increase incident risk, reactive posture cannot scale. Acquirer inherits reactive security posture—requires proactive governance investment but capital constrained.
**Claim Type:** `INFERENCE`  

**Evidence Sources:**
  - Stage 4.1: No CRO, reactive only
  - Stage 4.2: Incidents displace execution
  - Ransomware multi-month impact
  - Zero-day: monitoring offline
  - BBB: no apology/solution
  - Reactive spending pattern

---

**Area:** Financial planning masking operational underinvestment through activity metrics optimization  

**How Failure Is Absorbed:** Budget process prioritizes measurable activity metrics: SLA response times (not resolution times), Sales bookings (not delivered profitability), Ticket processing (not customer satisfaction), Headcount (not productivity). Operations absorb underinvestment by optimizing activity metrics while outcome metrics degrade: Support meets SLA response but customers report worsening experience, Sales maintains 400+ reps but revenue declines -7%, Tickets processed but customers complain unresolved. Financial planning masks underinvestment severity by reporting activity metrics that appear stable while business deteriorates.

**Why It Is Dangerous:** Management visibility distorted—activity metrics show 'green' while business declining. Resource allocation misguided—invest in maintaining activity metrics (SLA compliance, sales headcount) while starving outcome drivers (resolution quality, delivery profitability, customer satisfaction). Corrective action delayed—problems invisible until financial crisis forces recognition. CEO 'walk away' policy Q4 2024 indicates realization unprofitable despite activity metrics appearing healthy. Sales 'refresh' Q3 2024 indicates recognition sales activity not producing value. Trustpilot 'consistently getting worse' 2024 indicates customer experience declining despite presumably stable support activity metrics.

**Downstream Risk:** Business deterioration invisible until severe—activity metrics mask until financial crisis. Corrective action too late—by time recognized (FY2024 -7% revenue), damage severe. Investment decisions wrong—allocate to activity metrics not outcome drivers. Competitive position erodes invisibly—activity metrics stable while competitors gaining share. Post-close acquirer misled—activity metrics suggest operational health masking outcome degradation. Acquirer must reorient metrics to outcomes—requires operational overhaul, data systems changes. Due diligence misled if relies on activity metrics—true performance much worse than metrics suggest.
**Claim Type:** `INFERENCE`  

**Evidence Sources:**
  - Stage 4.2: Activity vs outcome metric divergence
  - SLA response times vs resolution failures
  - Sales bookings vs margin erosion
  - Ticket processing vs customer complaints
  - FY2024 -7%
  - Trustpilot: consistently worse

---


## Uncertainty Register

> **Uncertainty Register - Dependencies & Failure Propagation**


### Sub Stage

4.3

### Uncertainty Register

**Unknown:** Dependency mapping completeness—which dependencies undisclosed or underestimated  
**Type:** UNKNOWN  

**Decision Impact:** May have missed critical dependencies that will surface post-close. Vendor dependencies partially known (ScienceLogic monitoring) but complete vendor landscape unknown. Technology platform dependencies (shared services, central infrastructure) unknown. Data dependencies (which teams depend on which data sources) unknown. Cannot fully assess failure propagation without complete dependency map.

**What Would Reduce Uncertainty:** Complete dependency mapping: Vendor relationships and contracts, Shared services utilization, Technology platform architecture (central vs distributed), Data flow dependencies, Critical path analysis for major workflows

---

**Unknown:** Failure absorption capacity quantification—how much heroics capacity remains before collapse  
**Type:** UNKNOWN  

**Decision Impact:** Heroics masking failures, but unknown how close to capacity exhaustion. Support staff burnout timeline unknown. CEO coordination capacity utilization unknown (50%? 90%? 150%?). Delivery team margin absorption capacity unknown. Cannot predict when masking fails and crisis emerges. Post-close integration will stress heroics capacity—unknown if capacity exists to absorb integration load.

**What Would Reduce Uncertainty:** Heroics capacity assessment: Employee burnout indicators (turnover rates, engagement scores), CEO time allocation analysis (coordination load percentage), Delivery margin absorption history (how much erosion sustainable), Support escalation queue depth trends (growing or stable), Operations team incident response capacity (number of concurrent incidents manageable)

---

**Unknown:** Failure propagation velocity—how quickly localized failures cascade systemically  
**Type:** UNKNOWN  

**Decision Impact:** Some failures cascade quickly (security incidents), others slowly (margin erosion). Cannot predict crisis timing without understanding propagation velocity. Customer churn from support failures—how quickly does individual churn aggregate to material revenue impact? Sales-delivery failures—at what volume do unprofitable deals overwhelm profitable ones? Cannot assess urgency of corrective actions without velocity understanding.

**What Would Reduce Uncertainty:** Failure velocity metrics: Customer churn acceleration patterns, Margin erosion rates and tipping points, Support quality degradation trends (linear or exponential), Sales-delivery failure accumulation rate, Security incident frequency trends

---

**Unknown:** Post-close integration impact on dependencies and heroics  
**Type:** UNKNOWABLE  

**Decision Impact:** Integration will stress dependencies (additional coordination load) and disrupt heroics (informal networks broken, personnel changes). Cannot predict severity without knowing acquirer integration approach. CEO coordination capacity already constrained—integration load may overwhelm completely. Support heroics dependent on informal relationships—integration disrupts, failures surface. Cannot model integration risk without knowing acquirer strategy.

**What Would Reduce Uncertainty:** UNKNOWABLE—depends on future acquirer integration strategy. Can model scenarios (light touch vs full integration) but cannot predict which approach taken until transaction negotiated.

---


## Unknowns Requests

> **Information Requests - Dependencies & Failure Propagation Unknowns**


### Sub Stage

4.3

### Unknowns Requests

**Request Id:** 4.3-REQ-01  
**Priority:** CRITICAL  
**Unknown Addressed:** Complete cross-functional dependency mapping  

**Specific Request:** (1) Vendor dependency inventory: Critical vendors, contract terms, integration dependencies, single-source risks, (2) Shared services utilization: Which functions depend on which central services (IT, security, legal, finance, HR), capacity constraints, (3) Technology platform architecture: Central infrastructure vs distributed, critical paths, single points of failure, (4) Data flow dependencies: Which teams depend on which data sources, data pipelines, critical data dependencies

**Why Material:** Partial dependency visibility creates integration risk. Unknown dependencies will surface post-close creating surprises. Critical for failure propagation analysis—cannot map cascades without complete dependency understanding. Vendor dependencies create external bottlenecks (ScienceLogic example)—need complete inventory to assess risk.

---

**Request Id:** 4.3-REQ-02  
**Priority:** HIGH  
**Unknown Addressed:** Heroics capacity utilization and failure absorption limits  

**Specific Request:** (1) Employee burnout indicators: Voluntary turnover rates by function/role, engagement survey results, overtime/weekend work patterns, (2) CEO coordination load quantification: Time allocation analysis, decision queue depth, approval bottleneck metrics, (3) Delivery margin absorption: Historical margin erosion rates, profitability distribution by customer, capacity allocation between profitable/unprofitable, (4) Support escalation patterns: Queue depth trends, aging analysis, escalation success rates

**Why Material:** Heroics masking failures but capacity limits unknown. Need to assess how close to exhaustion—determines urgency of structural fixes. Post-close integration will stress heroics capacity—need baseline to assess integration load absorbability. Critical for determining whether business stabilizable or approaching collapse.

---

**Request Id:** 4.3-REQ-03  
**Priority:** MEDIUM  
**Unknown Addressed:** Failure propagation velocity and cascading patterns  

**Specific Request:** (1) Customer churn analysis: Churn acceleration patterns, time from first complaint to churn, churn prediction indicators, (2) Margin erosion velocity: Monthly margin trends, rate of change, tipping point analysis, (3) Support quality degradation: Trend analysis (linear/exponential), correlation with volume/complexity, (4) Security incident frequency: Historical incident rates, mean time between incidents, trend analysis

**Why Material:** Need to assess crisis timing—how quickly do masked failures surface? Determines urgency of corrective actions. Some failures may cascade slowly (margin erosion), others quickly (security incidents, customer churn). Cannot prioritize interventions without understanding propagation velocity.

---

# 7.1 Data Domain Authoritativeness

*Part of [Stage 7: Data Information Epistemic](../README.md)*


## Authoritative Truth Map

> **Authoritative Truth Map - Rackspace Technology, Inc.**


### Sub Stage

7.1

### Authoritative Truth Map

**Data Domain:** Deal profitability by customer—whether signed deals are actually profitable  

**Claimed System Of Record:** INFERENCE: Finance system likely claims profitability truth—general ledger, cost accounting, margin analysis systems. Sales CRM (Salesforce inference) claims bookings truth. No unified deal profitability system visible.

**Actual System Of Truth:** CEO personal judgment becomes system of truth by default when profitability disputed. Walk away policy Q4 2024 indicates CEO must personally assess and reject unprofitable deals/renewals—no systematic profitability validation pre-signature. CEO arbitrates sales (booking) vs delivery (cost) vs finance (margin) conflicts. Truth determined by CEO intervention not system calculation.

**Conflict Resolution Mechanism:** Reactive CEO arbitration AFTER deals signed and profitability questioned. Walk away policy Q4 2024 reactive—established after margin erosion severe (Private Cloud -13%, Public Cloud -3%). Sales refresh Q3 2024 suggests personnel blamed rather than data system inadequacy addressed. No deal review board or systematic profitability gate (Stage 4.1). Conflict resolution: Sales books optimistically, delivery discovers cost reality post-signature, finance reports margin erosion quarterly, CEO intervenes reactively when deterioration visible.

**Who Controls Truth:** CEO controls profitability truth reactively. Sales controls bookings truth proactively (autonomous booking authority Stage 4.1). Delivery has cost reality but lacks authority to establish profitability truth pre-signature. Finance reports historical profitability but cannot prevent unprofitable deals prospectively. Power asymmetry: Sales establishes revenue truth immediately upon booking, but profitability truth only established months later when CEO forces reconciliation.

**Touch Test What Breaks If Challenged:** If deal profitability data challenged publicly: Investor/Board confidence collapses—'walk away' policy admits prior deals unprofitable but magnitude unknown. If sales bookings authority challenged internally: Sales argues velocity/competitive necessity, revenue growth stalls (already -7% FY2024). If CEO profitability judgment challenged: No alternative arbitration mechanism exists—authority void. Challenging profitability truth reveals accountability void (Stage 4.4): No unified owner, split between sales/delivery/finance, CEO forced to arbitrate every dispute creating bottleneck.
**Claim Type:** `INFERENCE`  

**Evidence Sources:**
  - Q4 2024: CEO walk away policy established—reject unprofitable deals/renewals
  - Q3 2024: Sales refresh—personnel change suggests performance/data disputes
  - Margin erosion: Private Cloud -13%, Public Cloud -3% FY2024
  - Stage 4.1: Sales has booking authority, delivery lacks veto, no deal review board
  - Stage 4.4: Deal profitability accountability void—split sales/delivery/finance
  - FY2024: Revenue -7%—walk away policy sacrifices revenue for profitability discipline

---

**Data Domain:** Customer counts and churn rate—who is a 'customer' and when they leave  

**Claimed System Of Record:** INFERENCE: CRM system (Salesforce likely) claims customer count truth. Finance/billing system claims active revenue-generating customer truth. Customer success/support systems claim engagement/satisfaction truth. No unified customer definition visible across systems.

**Actual System Of Truth:** CONTESTED without clear winner. Customer definition varies by audience: Sales counts 'customers' as any signed contract (maximizes customer count metric). Finance counts 'customers' as active revenue generators (excludes non-paying, disputed, or churned-but-contracted). Support counts 'customers' as active ticket generators. Investor communications likely use finance definition (conservative) while sales performance uses CRM definition (optimistic). Churn calculation depends on customer definition—numerator and denominator both contested.

**Conflict Resolution Mechanism:** Definition changes by reporting context—no single truth enforced. Investor/regulatory reporting uses conservative definition (finance system, revenue-generating only). Internal sales performance uses optimistic definition (CRM, all signed contracts). Customer success uses engagement-based definition (support activity). Conflict unresolved—parallel truths coexist. Reconciliation avoided not addressed—reporting presents whichever definition favors narrative.

**Who Controls Truth:** Finance controls external truth (investor/regulatory reporting—SEC filings, earnings calls). Sales controls internal truth (performance management, quotas, territories). Customer success lacks authority to establish truth despite operational proximity (Stage 4.1: no VP Customer Success visible). CEO likely arbitrates investor-facing truth but parallel internal truths persist. Power fragmentation: Each function controls truth within domain, no enterprise-wide customer truth enforced.

**Touch Test What Breaks If Challenged:** If customer count/churn challenged by investors: Requires reconciliation between CRM (sales) and billing (finance) definitions—exposes customer definition ambiguity, potential churn understatement if using optimistic denominator. If churn calculation challenged internally: Reveals incentive misalignment—sales prefers optimistic customer count (denominator inflated, churn% appears lower), finance prefers conservative (denominator realistic, churn% accurate). Customer success likely has highest-fidelity engagement data (support activity) but lacks authority to challenge sales or finance definitions. Challenging customer truth reveals measurement theater (Stage 4.4): Activity metrics (customer counts) optimized while outcome metrics (satisfaction, retention) degrade.
**Claim Type:** `INFERENCE`  

**Evidence Sources:**
  - Stage 4.2: Activity vs outcome metric divergence pattern
  - Customer satisfaction declining: Trustpilot 'consistently worse' 2024, BBB complaints
  - Stage 4.1: No VP Customer Success, support lacks cross-functional authority
  - FY2024: Revenue -7%—suggests customer/churn dynamics material
  - CRM system inference from sales organization structure (400+ reps requires CRM)
  - Finance/billing system separate from CRM standard in enterprise software

---

**Data Domain:** Service delivery performance—SLA compliance vs customer satisfaction reality  

**Claimed System Of Record:** Support ticketing system claims SLA truth (response times: 15min critical, 1hr urgent, 4hr normal). Customer satisfaction surveys claim satisfaction truth if collected. Support activity metrics (tickets processed, SLA compliance%) reported as performance reality.

**Actual System Of Truth:** Support ticketing system wins internally—SLA compliance metrics reported, performance managed, compensation tied to activity metrics (Stage 4.4). Customer satisfaction truth external and lagging—surfaces through complaints (BBB, Trustpilot, Gartner) not systematic measurement. Internal truth (SLA met) contradicts external truth (satisfaction declining). Support activity system of internal truth, customer complaint platforms system of external truth. Contradiction unreconciled—activity metrics continue optimization while satisfaction degrades.

**Conflict Resolution Mechanism:** Internal vs external truth coexist unreconciled. Support performance management uses activity metrics (SLA compliance)—objective, measurable, directly controllable. Customer satisfaction uses external complaint platforms—subjective, lagging, indirectly influenced. When contradiction surfaces (customer complaints despite SLA compliance), resolution reactive: Individual issue escalation, support heroics ('dozens of engineers' coordination BBB), but no systematic reconciliation of activity vs satisfaction misalignment. CEO intervention for severe escalations (BBB: customers attempting CEO contact) but CEO capacity insufficient (Stage 4.2).

**Who Controls Truth:** Support management controls activity truth internally—SLA metrics, ticket processing throughput, team performance dashboards. Customers control satisfaction truth externally—complaints, reviews, survey responses if conducted. Finance controls 'Fanatical Support' brand promise externally (investor communications, competitive differentiation claims). Power asymmetry: Support optimizes internal measurable (SLA), customer dissatisfaction external and diffuse (no single authoritative satisfaction metric), finance claims 'Fanatical' truth without systematic validation. Customer truth lacks internal authority—complaints inform individual escalations not systemic measurement.

**Touch Test What Breaks If Challenged:** If SLA compliance challenged as misleading: Exposes activity-outcome divergence—SLA met but satisfaction declining reveals measurement theater. If 'Fanatical Support' brand promise challenged: Customer complaints (BBB, Trustpilot) directly contradict promise—brand erosion, competitive differentiation lost. If customer satisfaction data demanded systematically: Reveals measurement absence or suppression—systematic satisfaction tracking may not exist or data too negative to report. Challenging support truth reveals incentive misalignment (Stage 4.4): Support compensated on activity, satisfaction unmeasured/unrewarded, rational to optimize measurable (SLA) over unmeasurable (satisfaction).
**Claim Type:** `INFERENCE`  

**Evidence Sources:**
  - Stage 4.2: SLA response times met (activity metric stable)
  - Customer satisfaction declining: Trustpilot 'consistently worse' 2024
  - BBB complaints: Unresolved issues, 'dozens of engineers' coordination
  - Stage 4.4: Support incentive on SLA response not resolution quality
  - Stage 4.1: No VP Support, support lacks resolution authority
  - 'Fanatical Support' brand promise (public/investor communications)

---

**Data Domain:** Incident frequency and security posture—operational stability reality  

**Claimed System Of Record:** Security/operations monitoring systems claim incident truth (SIEM, monitoring dashboards, incident ticketing). ScienceLogic monitoring system cited (Stage 4.3: zero-day Sept 2024 vendor dependency). Incident response metrics (MTTD, MTTR, severity) claimed as operational stability truth.

**Actual System Of Truth:** Incident response metrics system of internal truth—MTTD/MTTR measurable, reportable, performance managed. Incident frequency/recurrence system of external truth—surfaces through customer impact, regulatory disclosure requirements (FedRAMP, HIPAA incident reporting), public incidents (ransomware multi-month, zero-day Sept 2024). Internal truth (response capable) contradicts external reality (incidents recurring). Monitoring system degradation (Sept 2024 dashboards offline during zero-day) indicates internal truth unreliable during crisis—when most needed, least trustworthy.

**Conflict Resolution Mechanism:** Reactive incident-by-incident resolution—each incident generates response metrics (internal truth: we responded), but incident frequency truth external and accumulative (pattern of recurrence). No systematic incident frequency reduction measurement (Stage 4.4: operations incentive on response not prevention). When monitoring fails (Sept 2024), truth determined by customer complaints and regulatory disclosure requirements not internal systems. Conflict between capability truth (operations can respond) and effectiveness truth (incidents recurring) unresolved—response metrics optimized, prevention metrics absent.

**Who Controls Truth:** Operations controls incident response truth internally—MTTD/MTTR metrics, crisis management capability demonstrations. Regulators control compliance truth externally—FedRAM, HIPAA require timely incident disclosure, controls maintenance. Customers control impact truth—experience outages, judge stability independently of operations metrics. No CRO to control enterprise risk truth (Stage 4.1)—operations reactive, no proactive prevention authority. Power fragmentation: Operations controls 'we responded' truth, but lacks authority to establish 'we prevented' truth or 'we're secure' truth.

**Touch Test What Breaks If Challenged:** If incident frequency challenged publicly: Ransomware multi-month impact, zero-day Sept 2024 public—recurrence pattern evident, contradicts stability claims if made. If monitoring reliability challenged: Sept 2024 dashboards offline during incident exposes visibility gap—cannot claim incident truth when monitoring fails during crisis. If security posture challenged by regulators: FedRAMP, HIPAA authorization at risk—reactive-only posture (Stage 4.4: no CRO, no proactive investment) creates compliance jeopardy. Challenging incident truth reveals prevention accountability void (Stage 4.4): Operations accountable for response not prevention, no owner of incident frequency reduction, CEO forced to intervene reactively.
**Claim Type:** `INFERENCE`  

**Evidence Sources:**
  - Ransomware: Multi-month impact (public incident)
  - Sept 2024: Zero-day vulnerability, monitoring dashboards offline during incident
  - Stage 4.1: No CRO, reactive risk posture only
  - Stage 4.4: Operations incentive on incident response not prevention
  - ScienceLogic vendor dependency (monitoring system)
  - FedRAMP, HIPAA/HITRUST compliance requirements (regulatory disclosure)

---

**Data Domain:** Multi-jurisdictional operational metrics—utilization, capacity, performance across FedRAMP/UK/HIPAA/China  

**Claimed System Of Record:** INFERENCE: Central operations dashboard likely claims consolidated operational truth. ScienceLogic monitoring per jurisdiction. Individual jurisdiction systems (FedRAMP-specific, UK-specific, etc.) claim local operational truth. Central technology/operations team claims enterprise-wide operational visibility.

**Actual System Of Truth:** FRAGMENTED without enterprise truth. Each jurisdiction (FedRAMP, UK Sovereign, HIPAA/HITRUST, China) separate operational systems due to regulatory isolation (Stage 4.2: 5-6x operational multiplier, data sovereignty mandates). Utilization truth jurisdiction-specific—cannot aggregate across regulatory boundaries. Capacity truth local not global—each jurisdiction separate capacity pool. Performance truth varies by jurisdiction—different infrastructure, different vendor dependencies (ScienceLogic per jurisdiction), different compliance regimes. No single operational truth—parallel jurisdiction truths coexist, enterprise aggregation impossible or misleading.

**Conflict Resolution Mechanism:** Jurisdictional isolation prevents conflict—each jurisdiction separate truth, aggregation avoided not reconciled. When enterprise-wide operational view needed (investor communications, Board reporting), aggregation methodology contested: Simple sum misleading (ignores jurisdiction isolation, capacity non-fungibility), weighted average arbitrary (weights determined politically not technically). Conflict resolution through aggregation methodology selection—finance/investor relations controls methodology, operations provides jurisdiction data, methodology debate determines enterprise truth. CEO likely arbitrates methodology disputes but expertise insufficient (operational complexity exceeds CEO bandwidth Stage 4.2).

**Who Controls Truth:** Operations controls jurisdiction-specific truth locally—each jurisdiction operations team owns local metrics. Finance/investor relations controls enterprise aggregation methodology—determines how jurisdiction truths combine into investor-facing enterprise truth. Regulators control jurisdiction definition and isolation—data sovereignty mandates prevent consolidation (external constraint). No central operations authority to unify truth (Stage 4.1: operations distributed, no COO visible with cross-jurisdiction authority). Power fragmentation across jurisdictions—no enterprise operational truth owner, jurisdiction specialists control local truth (Stage 4.5: jurisdiction specialists non-fungible, scarce expertise).

**Touch Test What Breaks If Challenged:** If utilization metrics challenged: Reveals jurisdiction fragmentation—'enterprise utilization' meaningless when capacity non-fungible across jurisdictions. If capacity planning challenged: Exposes 5-6x operational multiplier—cannot reallocate capacity across FedRAMP/UK/HIPAA/China boundaries, enterprise capacity truth misleading. If operational performance compared across jurisdictions: Different infrastructure, different vendor dependencies (ScienceLogic configurations), different regulatory overhead creates non-comparable metrics—aggregation methodology determines perceived performance ranking. Challenging operational truth reveals multi-jurisdictional accountability void (Stage 4.4): No central operations owner, distributed across jurisdictions, enterprise truth negotiated not measured.
**Claim Type:** `INFERENCE`  

**Evidence Sources:**
  - Stage 4.2: Multi-jurisdictional 5-6x operational multiplier
  - FedRAMP, UK Sovereign, HIPAA/HITRUST, China compliance (separate jurisdictions)
  - Stage 4.4: No central compliance coordination, distributed accountability
  - Data sovereignty mandates prevent infrastructure consolidation
  - ScienceLogic vendor dependency per jurisdiction (Stage 4.3)
  - Stage 4.5: Jurisdiction specialists non-fungible, expertise isolated

---

**Data Domain:** Sales performance and pipeline health—bookings forecast, pipeline quality, deal velocity  

**Claimed System Of Record:** CRM system (Salesforce inference) claims sales pipeline truth. Sales forecasts, deal stages, opportunity values, close probabilities managed in CRM. Sales management dashboards claim performance truth. Finance consolidates CRM data for revenue forecasting.

**Actual System Of Truth:** Sales CRM wins on pipeline quantity truth (opportunity counts, pipeline value at each stage). Finance establishes revenue forecast truth externally (investor guidance, Board commitments)—may override CRM-based forecast with conservative adjustments. Deal quality truth contested: Sales claims pipeline 'qualified' and 'winnable', delivery discovers post-signature many deals unbuildable or unprofitable (Stage 4.1: sales-delivery authority gap). CEO walk away policy Q4 2024 establishes quality truth reactively—overrides CRM opportunity value with profitability assessment. Sales refresh Q3 2024 suggests CRM truth challenged—if pipeline/performance data reliable, personnel change wouldn't be necessary.

**Conflict Resolution Mechanism:** Pipeline quantity truth uncontested—CRM system single source. Pipeline quality truth contested between sales (optimistic), delivery (realistic post-signature), finance (conservative for forecasting), CEO (profitability-disciplined post-Q4 2024). Conflict resolution: Sales CRM truth used for internal performance management and territory planning. Finance conservative adjustment used for external commitments (investor guidance). CEO profitability filter applied reactively to prevent unprofitable deals (walk away policy). No proactive quality validation pre-CRM entry—optimistic pipeline truth enters system, gets filtered reactively downstream causing margin erosion (Private Cloud -13%, Public Cloud -3%).

**Who Controls Truth:** Sales controls pipeline entry truth—determines what opportunities enter CRM, qualification criteria, stage progression. Sales management controls internal performance truth—quota attainment, territory rankings, compensation calculations based on CRM. Finance controls external forecast truth—adjusts CRM data for investor commitments, Board reporting. CEO controls deal approval truth reactively post-Q4 2024—can reject CRM opportunities via walk away policy. Power asymmetry: Sales establishes opportunity truth proactively and optimistically, finance adjusts conservatively for external consumption, CEO filters reactively for profitability, delivery discovers quality truth too late (post-signature).

**Touch Test What Breaks If Challenged:** If pipeline quality challenged internally: Exposes sales-delivery disconnect—CRM 'qualified' opportunities may be unbuildable, sales-delivery coordination gap (Stage 4.1). If forecast accuracy challenged by investors: Reveals conservative adjustment necessity—CRM optimistic, finance must discount for external credibility. If deal profitability challenged at CRM entry: Sales velocity stalls (fewer opportunities pass profitability screen), revenue growth at risk (already -7% FY2024), sales compensation declines (fewer bookings if quality required). Challenging sales truth reveals incentive misalignment (Stage 4.4): Sales compensated on bookings volume encourages optimistic CRM entry, quality filtering downstream reactive and costly.
**Claim Type:** `INFERENCE`  

**Evidence Sources:**
  - Q4 2024: CEO walk away policy—rejects unprofitable deals/renewals
  - Q3 2024: Sales refresh—suggests performance/pipeline data disputed
  - Stage 4.1: Sales booking authority, delivery lacks veto, no deal review board
  - Margin erosion: Private Cloud -13%, Public Cloud -3%—sales quality issue
  - FY2024: Revenue -7%—forecast accuracy challenged
  - CRM system inference from sales organization scale (400+ reps)

---


### Synthesis Notes

Truth ownership fragmented and contested across all material domains. Pattern: Proactive truth established optimistically by operational functions (sales CRM, support SLA), reactive truth established conservatively by finance/CEO after deterioration visible. No unified data authority—each function controls truth within domain, enterprise truth negotiated not measured. CEO forced to arbitrate truth disputes reactively (walk away policy, sales refresh, customer escalations) creating bottleneck (Stage 4.2). Power over truth correlates with decision authority not data proximity: Finance controls external truth (investor-facing), operations controls internal truth (performance management), CEO arbitrates conflicts. Contested domains systematically those where authority-accountability misaligned (Stage 4.1): Deal profitability (sales/delivery split), customer resolution (support/cross-functional split), operational stability (engineering/operations split). Truth contestation symptom of structural coordination failures not data quality issues.

## Contested Domains

> **Contested Data Domains - Rackspace Technology, Inc.**


### Sub Stage

7.1

### Contested Domains

**Data Domain:** Deal profitability by customer—whether booked revenue profitable when delivered  

**Nature Of Contestation:** Sales claims deals profitable at booking (based on pricing, revenue projections). Delivery discovers actual delivery cost exceeds pricing post-signature. Finance reports margin erosion quarterly but cannot prevent unprofitable bookings proactively. CEO forced to arbitrate via walk away policy Q4 2024—rejects deals/renewals retroactively. Contestation: Sales optimistic profitability assumptions vs delivery actual cost reality vs finance conservative margin reporting. No systematic profitability validation pre-signature reconciles views—conflict emerges only after margin deterioration severe (Private Cloud -13%, Public Cloud -3%).

**Why It Persists:** Authority-accountability mismatch (Stage 4.1): Sales has booking authority without profitability accountability, delivery has margin accountability without deal veto authority, finance reports historically without prospective control. No deal review board to force reconciliation pre-signature. Sales refresh Q3 2024 changed personnel not data reconciliation process—suggests organizational avoidance of systematic profitability truth. Walk away policy Q4 2024 CEO intervention reactive—addresses symptoms (reject bad deals individually) not cause (no proactive profitability validation system). Contestation persists because resolving requires authority reallocation: Sales loses autonomy if profitability veto created, delivery gains authority over revenue if veto granted. Political cost of resolution higher than operational cost of persistent contestation.

**Decision Risk:** Revenue forecasting unreliable—if profitability unknowable pre-signature, revenue quality uncertain. Margin guidance at risk—unpredictable margin erosion from unvalidated deals. Walk away policy application inconsistent—depends on CEO bandwidth and judgment (Stage 4.2: CEO bottleneck) not systematic criteria. Investor confidence at risk if profitability contestation revealed—demonstrates execution control absence. M&A valuation risk—if acquirer demands profitability data by customer/deal and reconciliation infeasible, due diligence failure or valuation discount.

**Evidence Sources:**
  - Q4 2024 walk away policy
  - Q3 2024 sales refresh
  - Margins: -13%/-3%
  - Stage 4.1 authority gaps
  - Stage 4.4 accountability voids

---

**Data Domain:** Customer satisfaction vs support performance—whether 'Fanatical Support' brand promise real  

**Nature Of Contestation:** Support claims SLA compliance proves performance (15min/1hr/4hr response times met). Customers claim satisfaction declining (Trustpilot 'consistently worse' 2024, BBB unresolved complaints). Finance/marketing claims 'Fanatical Support' competitive differentiation. Contestation: Internal activity truth (SLA met) vs external outcome truth (satisfaction down). Support argues metric compliance demonstrates capability. Customers experience unresolved issues despite SLA compliance. Brand promise vs operational reality diverging.

**Why It Persists:** Measurement misalignment (Stage 4.4): Support incentivized on SLA response not resolution quality, rational to optimize measurable (activity) over unmeasurable (satisfaction). Customer satisfaction measurement absent or suppressed internally—external complaint platforms (BBB, Trustpilot) surface truth support metrics don't capture. Support lacks authority to change measurement (no VP Support Stage 4.1). Finance/marketing invested in 'Fanatical Support' brand narrative—acknowledging satisfaction decline contradicts investor/competitive positioning. Contestation persists because internal measurement optimized for controllability (SLA objective, measurable) not validity (satisfaction subjective, lagging). Admitting contestation requires brand promise revision or support measurement overhaul—both costly.

**Decision Risk:** Brand erosion from satisfaction-promise gap—'Fanatical Support' becomes liability if gap widens or surfaces publicly. Customer retention at risk—declining satisfaction predicts churn. Support capacity planning misguided—if optimizing SLA not satisfaction, resource allocation misaligned with customer needs. Competitive differentiation lost—'Fanatical Support' claim unsustainable if satisfaction data contradicts. Investor communications risk—if satisfaction data demanded and reveals brand-reality gap, credibility damaged.

**Evidence Sources:**
  - Stage 4.2 SLA met
  - Trustpilot 'consistently worse' 2024
  - BBB complaints unresolved
  - Stage 4.4 support incentives
  - 'Fanatical Support' brand claims

---

**Data Domain:** Incident frequency and security posture—whether operational stability improving or recurring failures masked  

**Nature Of Contestation:** Operations claims incident response capability (MTTD/MTTR metrics, crisis management demonstrations). Incident recurrence indicates prevention gaps (ransomware multi-month, zero-day Sept 2024). Customers/regulators experience impact frequency, judge stability independently. Contestation: Response capability truth (operations) vs prevention effectiveness truth (external). Operations argues 'we responded' proves competence. Customers/regulators observe 'incidents recurring' indicates inadequacy. Monitoring degradation (Sept 2024 dashboards offline) undermines operations truth claims during crisis.

**Why It Persists:** Incentive misalignment (Stage 4.4): Operations rewarded on response speed not incident frequency reduction, rational to optimize reactive not proactive. No CRO to own prevention truth (Stage 4.1)—operations accountable for response, no one accountable for prevention. Proactive prevention investment perpetually deferred (capital constrained $1.3B debt, incidents consume budget reactively). Incident frequency truth measurement absent—no systematic tracking of recurrence patterns, root cause analysis, prevention effectiveness. Contestation persists because operations controls internal truth (response metrics), external parties control impact truth (incident experience), no reconciliation mechanism. Acknowledging frequency truth requires admitting prevention failure and funding prevention (capital unavailable or allocated elsewhere).

**Decision Risk:** Regulatory authorization at risk—FedRAMP, HIPAA require proactive controls, reactive-only posture creates jeopardy. Customer trust erosion from recurring incidents—stability perception declining. Operational cost inefficiency—reactive spending exceeds prevention cost (Stage 4.2) but prevention investment unavailable. Insurance implications—incident frequency may affect cyber insurance premiums, coverage. M&A risk—acquirer due diligence on incident history may reveal frequency pattern operations metrics don't disclose, valuation impact or deal failure.

**Evidence Sources:**
  - Ransomware multi-month
  - Zero-day Sept 2024
  - Monitoring offline Sept 2024
  - Stage 4.4 ops incentives
  - Stage 4.1 no CRO

---

**Data Domain:** Sales pipeline quality—whether CRM opportunities actually closeable and profitable  

**Nature Of Contestation:** Sales claims CRM pipeline 'qualified' and forecast-able based on stage progression, close probability. Delivery discovers post-signature many deals unbuildable or unprofitable. Finance applies conservative discount to CRM forecast for investor guidance. CEO walk away policy Q4 2024 overrides CRM opportunity values with profitability filter. Contestation: Sales optimistic CRM truth vs delivery post-signature quality reality vs finance conservative external forecast vs CEO profitability discipline. Pipeline enters CRM optimistically, quality discovered reactively downstream.

**Why It Persists:** Incentive to inflate pipeline (Stage 4.4): Sales compensated on bookings encourages optimistic opportunity entry and qualification. No proactive quality validation—deal review board absent (Stage 4.1), delivery lacks veto over CRM opportunities, profitability assessment post-signature only. Sales refresh Q3 2024 suggests pipeline quality disputed but process unchanged—personnel change treats symptom not cause. Finance learns to discount CRM data for external commitments but doesn't force upstream quality improvement. Contestation persists because sales controls CRM entry truth, downstream functions lack authority to challenge proactively, quality discovered reactively creates margin erosion but sales incentive unchanged.

**Decision Risk:** Forecast accuracy unreliable—if pipeline quality contested, revenue projections uncertain. Resource allocation misguided—if optimistic pipeline drives hiring/capacity planning, over-investment in unwinnable opportunities. Sales performance management distorted—if CRM metrics (pipeline value, stage progression) don't predict actual bookings quality, quotas and compensation misaligned. CEO walk away policy bandwidth insufficient (Stage 4.2)—cannot review all opportunities personally, sampling creates inconsistency. M&A due diligence risk—if acquirer audits CRM pipeline quality and discovers inflation, revenue projections challenged, valuation impacted.

**Evidence Sources:**
  - Q4 2024 walk away policy
  - Q3 2024 sales refresh
  - Stage 4.1 no deal review board
  - Stage 4.4 sales incentives
  - Margins: -13%/-3% suggest quality issues

---


### Synthesis Notes

Contestation pattern: Internal operational metrics optimistic (sales CRM pipeline, support SLA compliance, operations incident response), external reality pessimistic (delivery profitability, customer satisfaction, incident recurrence). Contestation emerges when internal activity truth contradicts external outcome truth. Persistence mechanism: Authority-accountability misalignment prevents reconciliation (Stage 4.1 coordination gaps), incentive optimization favors internal measurable over external outcome (Stage 4.4 activity-outcome divergence), capital constraints limit systematic resolution (Stage 5 liquidity), political cost of truth reconciliation exceeds operational cost of continued contestation. Decision risk concentration: Contested domains are material—deal profitability affects revenue quality, satisfaction affects retention, incidents affect regulatory authorization, pipeline quality affects forecast reliability. Acquirer diligence likely to surface contestations—valuation risk if reconciliation forced or infeasible.

## Disconfirming Evidence Not Found

> **Disconfirming Evidence Not Found - Data Domain Authoritativeness**


### Sub Stage

7.1

### Disconfirming Evidence Not Found

**Hypothesis Tested:** H7.1-A: Truth is centralized in single authoritative source per domain  

**Disconfirming Evidence Sought:** Evidence that single system definitively resolves disputes per domain, conflicts resolved systematically by designated authority, executive decisions reference consistent authoritative sources

**Search Conducted:** Examined all material domains for unified truth source: Deal profitability (searched for deal review board, unified profitability system), Customer metrics (searched for master customer database, unified customer definition), Support performance (searched for integrated satisfaction-SLA measurement), Incidents (searched for unified incident management with prevention), Operations (searched for enterprise operational system spanning jurisdictions), Pipeline (searched for quality-validated CRM with downstream integration). Examined governance structure for designated arbiters (Stage 4.1 authority analysis). Examined CEO interventions for systematic vs case-by-case patterns (walk away policy, sales refresh).

**Evidence Found:** NONE disconfirming hypothesis. Every domain exhibits parallel or contested truths. No unified authoritative source identified for any material domain. No systematic conflict resolution found—CEO reactive arbitration only (walk away policy Q4 2024, sales refresh Q3 2024, customer escalations). No data governance infrastructure visible (Stage 4.1: no deal review board, no operating committee, no data stewardship roles). Pattern: System of record exists per domain (CRM, support ticketing, monitoring) but does not equal system of truth—routinely bypassed, overridden, or contradicted by external reality.

**Conclusion:** Hypothesis H7.1-A REFUTED. Disconfirming evidence not found. Truth fragmentation pervasive across all tested domains. Centralized truth hypothesis contradicted by: CEO must personally arbitrate profitability disputes (indicates no systematic resolution), Finance must discount operational data for external reporting (indicates operational truth unreliable), Customers establish satisfaction truth on external platforms (indicates internal metrics don't capture reality), Operations incident response metrics contradicted by recurrence (indicates response truth doesn't reflect prevention truth).

---

**Hypothesis Tested:** H7.1-B: Data conflicts resolved through systematic governance processes  

**Disconfirming Evidence Sought:** Evidence of data governance committee, documented resolution protocols, conflicts resolved at working level not executive, resolution based on methodology not politics

**Search Conducted:** Searched Stage 4.1 authority analysis for governance infrastructure: Data governance committee, data council, data quality working groups, Chief Data Officer or equivalent, Deal review board for profitability validation, Operating committee for cross-functional conflicts, Customer success governance for satisfaction-SLA reconciliation. Searched CEO intervention patterns for systematic vs reactive: Walk away policy Q4 2024 criteria-based or case-by-case, Sales refresh Q3 2024 data-driven or political, Customer escalations systematic routing or ad-hoc. Searched finance adjustment for methodology documentation vs judgment.

**Evidence Found:** NONE disconfirming hypothesis. No data governance infrastructure identified. Stage 4.1 documents: No deal review board, no operating committee, no empowered coordinators, no data stewardship roles visible. CEO interventions reactive and case-by-case: Walk away policy requires CEO personal assessment (not systematic criteria), sales refresh Q3 2024 personnel change (not data reconciliation process), customer escalations attempt CEO contact (BBB: 'cannot reach CEO'—indicates no systematic escalation path). Three CEOs in three years indicates reactive arbitration unsustainable (Stage 4.2 bottleneck, Stage 4.5 role defeats individuals).

**Conclusion:** Hypothesis H7.1-B REFUTED. Disconfirming evidence not found. Governance void comprehensive. Conflicts escalate to CEO for personal reactive arbitration not systematic resolution. Absence of governance infrastructure persistent across: Three CEO transitions (governance void survives leadership changes), 2023 reorganization (created BU structure but not governance layer Stage 4.1), Sales refresh Q3 2024 (treated symptom with personnel change not cause with governance). CEO bottleneck (Stage 4.2) prevents governance infrastructure building—no bandwidth to design/implement systematic resolution while reactively arbitrating every dispute.

---

**Hypothesis Tested:** H7.1-C: Internal operational metrics reliably predict external outcomes  

**Disconfirming Evidence Sought:** Evidence that SLA compliance predicts satisfaction, CRM pipeline predicts quality, incident response predicts stability, internal-external alignment demonstrated

**Search Conducted:** Examined internal-external metric pairs across domains: Support (SLA compliance internal vs customer satisfaction external—Trustpilot, BBB), Sales (CRM pipeline internal vs deal profitability external—margin erosion, walk away policy), Operations (incident response metrics internal vs incident recurrence external—ransomware, zero-day), Customer counts (CRM internal vs churn reality external), Utilization (operations dashboards internal vs capacity reality external—multi-jurisdictional constraints). Searched for leading-lagging indicator validation: Do internal activities predict external outcomes over time? Does optimizing internal metrics improve external results?

**Evidence Found:** NONE disconfirming hypothesis. Systematic internal-external divergence found across all tested domains. Support: SLA met (internal activity stable Stage 4.2) but satisfaction declining (external outcome Trustpilot 'consistently worse' 2024). Sales: Bookings maintained (CRM activity) but margins eroding (profitability outcome Private Cloud -13%, Public Cloud -3%). Operations: Incident response capable (MTTD/MTTR internal) but incidents recurring (stability outcome ransomware multi-month, zero-day Sept 2024). Pipeline: CRM opportunities (internal entry) but quality contested (external walk away policy Q4 2024 needed). Pattern persistent not episodic—divergence documented across Stages 4.2, 4.4 as structural measurement theater.

**Conclusion:** Hypothesis H7.1-C REFUTED decisively. Disconfirming evidence not found—alignment not demonstrated anywhere. Internal-external divergence systematic indicates: Incentive optimization on measurable internal activities (Stage 4.4: support on SLA, sales on bookings, operations on response), Outcome measurement absent or suppressed (satisfaction not tracked systematically, profitability by deal contested, prevention not measured), Activity metrics create measurement theater—reports green while business deteriorates (Stage 4.4 activity-outcome divergence pattern). Walk away policy Q4 2024 reactive recognition after margin erosion severe—internal metrics failed to predict external deterioration.

---

**Hypothesis Tested:** H7.1-D: Data quality and authoritativeness improve over time through learning  

**Disconfirming Evidence Sought:** Evidence of data quality improvements, investment in data systems, disputed domains resolved, maturation from chaos to systematization

**Search Conducted:** Examined longitudinal patterns for improvement: Three CEO transitions—did data disputes resolve with any CEO? 2023 reorganization—did BU structure improve data alignment? Sales refresh Q3 2024—did margin erosion stop post-refresh indicating data quality improved? Walk away policy Q4 2024—proactive improvement or reactive damage control after deterioration? Customer satisfaction trend—improving or declining (Trustpilot 'consistently worse' 2024)? Searched for data infrastructure investment: Capital allocation to data systems, governance, measurement (Stage 5 capital constraints $1.3B debt). Searched for capability building: Chief Data Officer hired, data governance initiated, data quality programs launched.

**Evidence Found:** NONE disconfirming hypothesis. Quality not improving, potentially degrading. Three CEOs—data disputes persist across all transitions (deal profitability, customer metrics, satisfaction-SLA gap, incident truth all unresolved). 2023 reorganization—created BU accountability but not authority, disputes persist (Stage 4.1 authority-accountability mismatch continues). Sales refresh Q3 2024—margin erosion continues post-refresh (Private Cloud -13%, Public Cloud -3% after refresh), indicates personnel change insufficient. Walk away policy Q4 2024—reactive after severe deterioration not proactive improvement. Satisfaction declining 2024 (Trustpilot 'consistently worse')—measurement-reality gap widening not narrowing. No data infrastructure investment visible—capital constrained, CEO bandwidth exhausted on reactive firefighting (Stage 4.2 bottleneck prevents governance building).

**Conclusion:** Hypothesis H7.1-D WEAKENED/REFUTED. Disconfirming evidence (improvement) not found. Quality likely degrading: Activity-outcome divergence widening (satisfaction 'consistently worse'), margin erosion accelerating (necessitated walk away policy Q4 2024), CEO intervention frequency increasing (walk away, sales refresh, customer escalations). No improvement despite repeated interventions indicates: Interventions treat symptoms not causes (personnel changes, reactive policies vs structural reform), Data disputes symptomatic of authority-accountability-incentive misalignments (Stages 4.1, 4.4) not data management deficits, Structural causes unchanged across interventions—disputes persist and intensify.

---


### Synthesis Notes

Comprehensive search for disconfirming evidence (truth centralization, systematic governance, internal-external alignment, quality improvement) found NONE. All hypotheses testing positive data governance patterns refuted. Evidence convergent: Truth fragmented not centralized, governance reactive/political not systematic, internal metrics diverge from external reality, quality not improving potentially degrading. Refutations not isolated—interconnected through structural root causes: Authority-accountability misalignment (Stage 4.1) prevents unified truth ownership, Incentive misalignment (Stage 4.4) drives activity optimization while outcomes degrade, CEO bottleneck (Stage 4.2) prevents governance infrastructure building, Capital constraints (Stage 5 $1.3B debt) limit data system investment. Data disputes symptomatic of execution constraints not causal—resolving requires structural reform (authority reallocation, incentive realignment, governance creation) not data management improvement. Three CEOs, sales refresh, walk away policy, 2023 reorganization all insufficient because structural causes unchanged.

## Epistemic Power Centers

> **Epistemic Power Centers - Rackspace Technology, Inc.**


### Sub Stage

7.1

### Epistemic Power Centers

**Actor Or Role:** CEO—ultimate arbiter of contested truth, controls profitability/quality truth reactively  

**Domains Controlled:**
  - Deal profitability (walk away policy Q4 2024)
  - Sales pipeline quality (override CRM valuations)
  - Customer escalation truth (when reaches CEO level)
  - Performance metric disputes (sales refresh Q3 2024 authority)
  - Investment priorities (allocates constrained capital)

**Mechanism Of Power:** Formal authority: CEO has ultimate decision rights, Board accountability. Reactive arbitration: Intervenes when conflicts surface (walk away policy, sales refresh, customer escalations Stage 4.1). Bottleneck power: All cross-functional truth conflicts escalate to CEO creating dependency (Stage 4.2 serial processing). Three CEOs in three years indicates power without sustainability—role defeats individuals, truth arbitration load exceeds capacity. CEO controls truth by personal judgment not systematic process—walk away policy requires CEO assess each deal profitability, sales refresh CEO-driven personnel decision.

**Organizational Risk:** CEO truth arbitration bottleneck: Organizational truth-seeking stalls when CEO overloaded (Stage 4.2 throughput ceiling). Truth inconsistency: CEO reactive arbitration creates case-by-case truth not systematic—walk away policy application depends on CEO bandwidth. CEO transitions destroy institutional truth: Three CEOs in three years, each transition resets truth arbitration patterns, coordination collapses (Stage 4.5 turnover sensitivity). Successor CEO inherits truth conflicts without resolution infrastructure—operating committee absent (Stage 4.1), deal review board absent, governance void forces CEO personal arbitration perpetuating bottleneck.

**Evidence Sources:**
  - Q4 2024 walk away policy CEO-established
  - Q3 2024 sales refresh CEO-driven
  - Stage 4.1 CEO sole coordinator
  - Stage 4.2 CEO bottleneck
  - Three CEOs three years

---

**Actor Or Role:** Finance/CFO—controls external truth (investor-facing), conservative adjustment authority  

**Domains Controlled:**
  - Revenue forecasts (investor guidance)
  - Margin reporting (quarterly earnings)
  - Customer metrics external (SEC filings)
  - Cash flow and capital allocation truth
  - Cost structure and utilization rates external

**Mechanism Of Power:** Regulatory authority: SEC reporting requirements, audit compliance create finance gatekeeping power. External credibility: Investor relations, Board reporting require finance sign-off—conservative adjustments override operational optimism. Conservative bias: Finance discounts operational data (CRM pipeline, customer counts, utilization) for external consumption creating parallel truths—internal operational vs external financial. Audit backing: External auditors validate finance truth, operational metrics lack external validation. Capital control: Finance controls budget allocation ($1.3B debt constraint), determines which operational truths get funded.

**Organizational Risk:** Internal-external truth divergence: Finance external truth conservative, operations internal truth optimistic, gap widens creating coordination failures—operations plan using internal truth, finance commits using external truth, misalignment creates missed targets. Truth suppression risk: Finance conservative adjustment may suppress operational reality investors need to understand—optimistic operations metrics don't reach investors, deterioration invisible until severe. Capital misallocation: Finance controls investment based on external truth (conservative), operations needs based on internal truth (optimistic), mismatch starves operational execution or creates over-commitment.

**Evidence Sources:**
  - SEC filings finance-controlled
  - Margin reporting: -13%/-3%
  - Stage 5 capital constraints $1.3B debt
  - Finance budget authority inference
  - Conservative forecasting practice inference

---

**Actor Or Role:** Sales leadership—controls pipeline entry truth, CRM data, opportunity qualification  

**Domains Controlled:**
  - Sales pipeline (CRM opportunity entry, qualification, stage progression)
  - Customer counts internal (signed contracts, CRM accounts)
  - Bookings forecasts internal (quota setting, territory planning)
  - Deal terms and pricing (what enters contracts)
  - Competitive win/loss narratives

**Mechanism Of Power:** CRM control: Sales manages CRM data entry, qualification criteria, stage definitions—determines what opportunities 'exist' systemically. Performance metrics: Sales quotas, compensation, territory rankings based on CRM truth—sales controls performance measurement system. First-mover advantage: Sales establishes opportunity and customer truth proactively at CRM entry, downstream functions (delivery, finance) discover quality issues reactively post-signature—temporal power. Volume optimization: Sales incentive on bookings (Stage 4.4) encourages optimistic CRM entry, quality filtering downstream sales externalizes cost to delivery.

**Organizational Risk:** Pipeline inflation: CRM truth optimistic encourages resource misallocation (hiring, capacity planning based on inflated pipeline). Downstream surprise: Delivery discovers deal quality post-signature when correction costly (contracts signed, customer expectations set). Forecast unreliability: Finance learns to discount CRM data but methodology contested, investor guidance uncertainty. Authority-accountability gap: Sales controls CRM truth but lacks profitability accountability (Stage 4.1), creates moral hazard—optimistic truth benefits sales (compensation, performance ratings) while costs borne by delivery (margin erosion) and finance (forecast misses).

**Evidence Sources:**
  - CRM system inference Salesforce
  - Stage 4.4 sales incentive bookings
  - Q3 2024 sales refresh
  - Stage 4.1 sales booking authority
  - Margin erosion: -13%/-3% quality impact

---

**Actor Or Role:** Operations/Security—controls internal operational truth, incident narratives, stability claims  

**Domains Controlled:**
  - Incident response metrics (MTTD, MTTR)
  - Operational stability internal (uptime, availability dashboards)
  - Security posture internal (controls, compliance status)
  - Infrastructure utilization
  - Vendor relationship truth (ScienceLogic, others)

**Mechanism Of Power:** Technical expertise: Operations possesses specialized knowledge others lack—creates information asymmetry, operational claims difficult to challenge by non-technical stakeholders. Monitoring control: Operations manages monitoring systems (ScienceLogic), controls what incidents reported and how measured—monitoring offline Sept 2024 indicates selective visibility. Crisis response: Operations gains power during incidents—all-hands mobilization, executive attention, budget exceptions for reactive spending—incident response validates operations importance. Regulatory interface: Operations manages FedRAMP, HIPAA compliance truth, controls what regulators see—compliance reporting power.

**Organizational Risk:** Incident truth selective: Operations controls what incidents reported, how severity classified, what root causes disclosed—creates incident understatement risk. Prevention truth absence: Operations lacks authority/incentive to report prevention gaps (Stage 4.4 reactive incentive, Stage 4.1 no CRO)—incident frequency truth suppressed or unmeasured. Monitoring reliability contested: Sept 2024 dashboards offline during incident undermines operations truth claims—when monitoring fails during crisis, truth most uncertain when most needed. Regulatory exposure: If operations-controlled compliance truth incomplete or misleading, FedRAMP/HIPAA authorization jeopardy, regulatory investigation risk.

**Evidence Sources:**
  - Stage 4.4 ops incentive response
  - Ransomware multi-month, zero-day Sept 2024
  - ScienceLogic monitoring
  - Monitoring offline Sept 2024
  - Stage 4.1 no CRO

---

**Actor Or Role:** Customers (external)—control satisfaction truth, incident impact truth, brand reality  

**Domains Controlled:**
  - Customer satisfaction (complaint platforms: BBB, Trustpilot, Gartner)
  - Incident impact reality (experience outages, judge stability)
  - 'Fanatical Support' brand truth (gap between promise and experience)
  - Churn decisions (ultimate truth about value delivered)
  - Public reputation (reviews, social media, analyst reports)

**Mechanism Of Power:** External platform power: Customers control truth on platforms Rackspace doesn't manage—BBB, Trustpilot, Gartner Peer Insights create permanent public record. Experience authority: Customers experience service delivery reality directly—support resolution, incident impact, satisfaction—operational metrics can't override customer experience. Churn action: Customer retention/churn ultimate truth validation—'voting with feet' mechanism. Analyst influence: Customer feedback to Gartner, Forrester, others shapes competitive positioning, market perception. Regulatory complaints: Customers can escalate to regulators (FCC, FTC, state AGs) creating external investigation trigger.

**Organizational Risk:** Internal-external truth gap: Rackspace internal metrics (SLA compliance, response times) contradict customer external truth (satisfaction declining, issues unresolved)—gap creates brand erosion. Satisfaction truth lagging: Customer complaints surface after deterioration established—Trustpilot 'consistently worse' 2024 indicates prolonged degradation. Reputational damage persistent: Customer truth on external platforms permanent, public, discoverable—cannot be retracted or managed, damages competitive position and M&A attractiveness. Churn prediction failure: If internal satisfaction metrics don't capture customer truth, churn unpredictable—revenue forecast risk, customer lifetime value miscalculation.

**Evidence Sources:**
  - Trustpilot 'consistently worse' 2024
  - BBB complaints unresolved
  - Gartner Peer Insights reviews
  - Stage 4.2 SLA met/satisfaction down
  - 'Fanatical Support' brand claims

---


### Synthesis Notes

Epistemic power fragmented across CEO (reactive arbiter), finance (external conservative truth), sales (pipeline optimistic truth), operations (incident response truth), customers (satisfaction external truth). No unified truth authority—creates parallel truths coexisting unreconciled. Power correlates with decision authority not data proximity: Finance controls external truth through reporting authority, sales controls pipeline through CRM authority, CEO arbitrates through ultimate decision authority—but support/delivery closest to operational reality lack authority to establish truth (Stage 4.1 coordination gaps). Customer external truth lacks internal authority—complaints inform escalations not systematic measurement changes. Three CEOs in three years indicates CEO truth arbitration power unsustainable—bottleneck (Stage 4.2), role defeats individuals (Stage 4.5 talent constraints). Truth power fragmentation creates execution risk: Parallel truths drive misaligned decisions, contested domains remain unresolved creating margin erosion/satisfaction decline/incident recurrence, M&A diligence may force truth reconciliation impossible or value-destructive.

## Hypotheses

> **Data Domain Authoritativeness Hypotheses - Rackspace Technology**


### Sub Stage

7.1

### Hypotheses


#### H7.1-A: Truth is centralized in single authoritative source per domain—'system of record' equals 'system of truth'


**Supporting Evidence Sought:**
  - Single system definitively resolves disputes per domain
  - Conflicts rare or resolved systematically by designated authority
  - Consistent data usage across functions from single source
  - Executive decisions reference same authoritative system

**Disconfirming Evidence Sought:**
  - Multiple parallel truths coexist per domain
  - System of record bypassed or overridden in decisions
  - Disputes resolved politically not systematically
  - Different functions use different data sources for same domain

**Evidence Found:**
**Supporting:** NONE. No domain has unified authoritative truth.  

**Disconfirming:**
    - Deal profitability: Sales CRM vs delivery cost vs finance margin—no unified system
    - Customer metrics: CRM counts vs billing active vs support engagement—parallel truths
    - Support: SLA system vs customer satisfaction platforms—contradictory
    - Incidents: Operations MTTD/MTTR vs customer impact vs regulator disclosure—fragmented
    - Pipeline: Sales CRM optimistic vs finance conservative vs CEO profitability filter—contested
    - Operations: Jurisdiction-specific systems, no enterprise aggregation trusted
**Status:** ❌ REFUTED  

**Notes:** Hypothesis refuted comprehensively. Every material domain exhibits parallel or contested truths. System of record ≠ system of truth pattern pervasive. CRM is system of record for sales but CEO walk away policy overrides CRM opportunity values. Support ticketing system of record for SLA but customer complaint platforms establish satisfaction truth externally. Finance general ledger system of record for margins but profitability by deal/customer contested between sales and delivery. Refutation indicates structural pattern: Authority-accountability misalignment (Stage 4.1) prevents unified truth—each function controls truth within domain, cross-functional truth negotiated or imposed by CEO reactively.

---


#### H7.1-B: Data conflicts resolved through systematic governance processes—not political negotiation or executive intervention


**Supporting Evidence Sought:**
  - Data governance committee resolves disputes
  - Documented resolution protocols by domain
  - Conflicts resolved at working level not executive escalation
  - Resolution based on data quality or methodology not politics

**Disconfirming Evidence Sought:**
  - CEO arbitrates data disputes personally
  - Conflicts resolved through political negotiation
  - Resolution inconsistent case-by-case not systematic
  - Data governance infrastructure absent or ineffective

**Evidence Found:**
**Supporting:** NONE. No systematic governance process identified.  

**Disconfirming:**
    - CEO walk away policy Q4 2024—CEO personal arbitration of deal profitability
    - Sales refresh Q3 2024—CEO intervention on performance/pipeline disputes
    - Customer escalations reach CEO—no systematic resolution (BBB: 'cannot reach CEO')
    - Stage 4.1: No deal review board, no operating committee, no data governance visible
    - Finance conservative adjustment methodology—not governed, determined case-by-case
    - Multi-jurisdictional aggregation—methodology contested, no governance standard
**Status:** ❌ REFUTED  

**Notes:** Hypothesis refuted. Conflicts escalate to CEO for reactive personal arbitration (walk away policy, sales refresh, customer escalations)—not resolved systematically. No data governance committee visible (Stage 4.1 governance infrastructure absent). Resolution political: CEO has authority not methodology, walk away policy case-by-case not criteria-based, sales refresh personnel change not data reconciliation. Three CEOs in three years indicates personal arbitration unsustainable (Stage 4.2 bottleneck, Stage 4.5 talent constraints). Refutation indicates governance void: Data conflicts symptom of authority-accountability misalignment (Stage 4.4), resolved reactively through CEO heroics not systematically through governance infrastructure.

---


#### H7.1-C: Internal operational metrics reliably predict external outcomes—activity truth aligns with outcome truth


**Supporting Evidence Sought:**
  - SLA compliance predicts customer satisfaction
  - CRM pipeline predicts bookings quality
  - Incident response metrics predict stability perception
  - Utilization metrics predict capacity needs accurately

**Disconfirming Evidence Sought:**
  - Internal activity stable while external outcomes degrade
  - Leading internal indicators fail to predict lagging external results
  - Operational metrics optimized while customer/financial reality deteriorates
  - Divergence pattern persistent not episodic

**Evidence Found:**
**Supporting:** NONE. Internal-external alignment not found.  

**Disconfirming:**
    - Support SLA met (internal activity) but satisfaction declining (external outcome)—Trustpilot 'consistently worse' 2024
    - Sales bookings maintained (CRM activity) but margins eroding (profitability outcome)—Private Cloud -13%, Public Cloud -3%
    - Incident response capable (operations activity) but incidents recurring (stability outcome)—ransomware, zero-day
    - CRM pipeline (sales activity) but quality contested (delivery outcome)—walk away policy needed
    - Activity-outcome divergence pattern systematic not episodic (Stage 4.2, 4.4)
**Status:** ❌ REFUTED  

**Notes:** Hypothesis decisively refuted. Internal activity truth systematically diverges from external outcome truth across all tested domains. Pattern: Incentive optimization favors measurable internal activities (SLA response, CRM entry, incident response, bookings volume) over hard-to-measure external outcomes (satisfaction, profitability, stability, quality). Divergence creates measurement theater (Stage 4.4): Internal metrics reported green while business deteriorates. Refutation indicates structural misalignment: Internal measurement systems designed for controllability (objective, immediate, directly influenced) not validity (predicting customer/financial outcomes). Activity-outcome divergence symptom of incentive misalignment—individuals rationally optimize measured activities while unmeasured outcomes degrade.

---


#### H7.1-D: Data quality and authoritativeness improve over time through learning and investment


**Supporting Evidence Sought:**
  - Historical data quality improvements documented
  - Investment in data systems, governance, measurement
  - Disputed domains resolved through infrastructure building
  - Maturation pattern: Early chaos, later systematization

**Disconfirming Evidence Sought:**
  - Data disputes persistent or worsening
  - No improvement despite CEO transitions, reorganizations
  - Reactive interventions don't resolve structural issues
  - Deterioration pattern: Quality degrades over time

**Evidence Found:**
**Supporting:** Walk away policy Q4 2024, sales refresh Q3 2024 could indicate attempted improvement—but reactive not proactive.  

**Disconfirming:**
    - Three CEOs three years—data disputes persist across CEO transitions
    - 2023 reorganization created BU structure—authority-accountability misalignment persists (Stage 4.1)
    - Sales refresh Q3 2024—margin erosion continues post-refresh
    - Walk away policy Q4 2024—reactive after severe deterioration, not proactive improvement
    - Satisfaction declining 2024 (Trustpilot 'consistently worse')—measurement-reality gap widening
    - No data governance infrastructure visible despite repeated failures
**Status:** WEAKENED/REFUTED  

**Notes:** Hypothesis weakened significantly, likely refuted. Data quality and authoritativeness not improving—disputes persistent despite CEO transitions (three in three years), reorganizations (2023 BU structure), personnel changes (sales refresh Q3 2024). Reactive interventions (walk away policy, sales refresh) address symptoms not causes—authority-accountability misalignment (Stage 4.1), incentive misalignment (Stage 4.4), governance void persist. No systematic data infrastructure investment visible—capital constrained ($1.3B debt Stage 5), CEO bottleneck (Stage 4.2) prevents governance building bandwidth. Pattern suggests degradation not improvement: Activity-outcome divergence widening (satisfaction 'consistently worse' 2024), margin erosion accelerating, CEO intervention necessity increasing. Refutation indicates: Data disputes symptom of structural execution constraints (authority gaps, incentive misalignments, coordination bottlenecks)—not improving because underlying structure unchanged.

---


### Synthesis Notes

All hypotheses testing truth centralization, systematic governance, internal-external alignment, quality improvement either refuted or weakened. Pattern: Truth fragmented not centralized, governance reactive/political not systematic, internal activity diverges from external outcome, quality not improving potentially degrading. Refutations convergent: Point to structural root cause—authority-accountability misalignment (Stage 4.1), incentive misalignment (Stage 4.4), coordination bottlenecks (Stage 4.2), capital constraints (Stage 5). Data disputes symptomatic not causal—resolving data conflicts requires structural reform (authority reallocation, incentive realignment, governance infrastructure) not data management improvement. Three CEOs, sales refresh, walk away policy all fail to resolve data contestation because structural causes unchanged.

## Uncertainty Register

> **Data Domain Authoritativeness Uncertainty Register**


### Sub Stage

7.1

### Uncertainty Register


**Unknown:** Specific data systems and platforms—CRM (Salesforce inference), ERP/financial system, support ticketing, monitoring (ScienceLogic known), BI/analytics tools
**Type:** UNKNOWN  

**Decision Impact:** Cannot precisely map data flow, system integration points, where transformation occurs. Cannot assess technical vs political causes of contestation—if systems don't integrate, contestation may be technical limitation not political choice. Cannot evaluate data quality at system level—if systems unknown, data accuracy/completeness/timeliness assessment incomplete. Inference from organizational structure (400+ sales reps requires CRM, financial reporting requires ERP) and vendor citations (ScienceLogic monitoring Stage 4.3) but specific platforms, versions, integration architecture unknown.

**What Would Reduce Uncertainty:** IT architecture documentation: System inventory with business domain mapping, Data flow diagrams showing system-to-system integration or manual transfer, Platform vendor contracts and SKUs, Data warehouse/lake architecture if exists, BI tool stack and user access patterns, API integration map or ETL process documentation. Would clarify whether contestation caused by system fragmentation (technical) or authority fragmentation (political) or both.

---

**Unknown:** Data governance maturity and investment history—whether data governance attempted and failed vs never attempted  
**Type:** UNKNOWN  

**Decision Impact:** Cannot determine whether current state result of governance failure (attempted, didn't work) or governance absence (never tried). If attempted, why failed? Organizational resistance, capability deficit, executive support withdrawn, budget cut? If never attempted, why not? Prioritization (other initiatives took precedence), awareness (problem not recognized), capability (no expertise to design governance)? Cannot assess feasibility of governance solution—if tried and failed, repeating unlikely to succeed without addressing root failure causes. If never tried, may be feasible but requires capability/budget assessment.

**What Would Reduce Uncertainty:** Governance initiative history: Any data governance committees, councils, working groups created? When, charter, outcomes? Data quality initiatives past 5 years—tools procured, processes designed, success/failure? Chief Data Officer or equivalent role—ever existed, when eliminated if so? Data management consulting engagements—firms hired, recommendations, implementation? Budget allocated to data governance/quality—historical trend shows prioritization or deprioritization?

---


**Unknown:** Systematic customer satisfaction measurement—whether satisfaction data collected internally and suppressed or not collected at all
**Type:** UNKNOWN  

**Decision Impact:** Cannot determine whether satisfaction truth absence deliberate (data exists but suppressed) or structural (data not collected). If collected and suppressed, indicates political sensitivity—satisfaction data so negative reporting would damage brand/investor confidence. If not collected, indicates measurement gap—support optimizing SLA without knowing customer impact. Cannot assess remediation approach—if data exists, making visible requires political will; if data absent, creating requires measurement infrastructure investment. External platforms (BBB, Trustpilot, Gartner) only source visible—may understate or overstate actual satisfaction depending on sample bias.

**What Would Reduce Uncertainty:** Customer satisfaction measurement practices: NPS/CSAT surveys conducted? Frequency, sample size, response rate? Survey data analyzed and reported? To whom (executive team, Board, investors)? Historical satisfaction trends if measured? Satisfaction by customer segment, product, jurisdiction? Correlation analysis satisfaction vs churn? If not measured systematically, why not? Budget, capability, political resistance?

---

**Unknown:** Deal-level profitability visibility—whether finance can calculate profitability by customer/deal or only aggregate  
**Type:** UNKNOWN  

**Decision Impact:** Cannot assess walk away policy effectiveness—if CEO lacks deal-level profitability data, policy implementation inconsistent or arbitrary. Cannot determine whether profitability contestation solvable through better data or structural (sales-delivery coordination gap insurmountable). If profitability calculable, contestation political (sales/delivery/finance won't reconcile despite data). If profitability incalculable, contestation technical (cost allocation, delivery attribution, overhead assignment unsolved). Cannot evaluate M&A risk—if acquirer demands customer profitability data and Rackspace cannot produce, due diligence failure or valuation penalty.

**What Would Reduce Uncertainty:** Cost accounting and profitability analysis capabilities: Can finance calculate fully-loaded cost by customer? What allocation methodology (direct, activity-based, other)? Customer profitability P&Ls produced? Frequency, granularity, confidence level? Profitability by deal, customer segment, product line, jurisdiction? Walk away policy implementation process—what data CEO reviews when assessing deal profitability? If customer profitability not calculable, why not? Technical limitation (cost allocation complexity), system limitation (data not integrated), political resistance (delivery doesn't want visibility)?

---

**Unknown:** Finance conservative adjustment methodology—how finance discounts operational data for external reporting  
**Type:** UNKNOWN  

**Decision Impact:** Cannot assess internal-external truth gap magnitude—if finance adjustment methodology unknown, cannot quantify difference between operational optimism and financial conservatism. Cannot evaluate forecast reliability—if methodology inconsistent or judgmental, forecast accuracy uncertain. Cannot determine whether adjustment appropriate (corrects operational bias toward accuracy) or excessive (creates pessimism bias). Finance credibility with investors depends on adjustment producing accurate forecasts—methodology opacity creates verification impossibility.

**What Would Reduce Uncertainty:** Finance forecasting and adjustment processes: How does finance adjust CRM pipeline for revenue forecast? Discount factors by stage, product, jurisdiction? Historical accuracy of CRM-based forecast vs actual? How does finance adjust customer counts? Active revenue generators only, or includes contracted-but-not-paying? Margin forecast methodology—aggregates BU projections, applies corporate adjustments? Adjustment rationale documented and auditable? CFO judgment involved—qualitative overlays on quantitative models?

---

**Unknown:** Multi-jurisdictional operational data aggregation methodology—how jurisdiction truths combine into enterprise truth  
**Type:** UNKNOWN  

**Decision Impact:** Cannot assess whether enterprise operational metrics (utilization, capacity, performance) meaningful or misleading. If aggregation methodology flawed (ignores jurisdiction isolation, capacity non-fungibility), enterprise truth meaningless and decisions misguided. Cannot evaluate investor communications accuracy—if operational metrics presented without jurisdiction caveat, investors may misunderstand operational reality. Cannot determine infrastructure investment decisions—if enterprise utilization calculated but capacity not fungible across jurisdictions, investment may be misallocated.

**What Would Reduce Uncertainty:** Operations reporting and aggregation practices: How are jurisdiction-specific metrics aggregated for enterprise view? Simple sum, weighted average, consolidated? What weights if applicable? Capacity reported enterprise-wide—does reporting note capacity non-fungibility across jurisdictions? Utilization calculation—denominators account for jurisdiction isolation or assume fungible capacity? Investor/Board reporting—are multi-jurisdictional complexities disclosed or aggregated metrics presented without caveat? Operations dashboards—show jurisdictions separately or consolidated?

---


### Synthesis Notes

Uncertainties cluster around: (1) Technical infrastructure—systems, integration, data flow, (2) Governance history—whether tried and failed vs never attempted, (3) Measurement practices—customer satisfaction, deal profitability, operational aggregation, (4) Methodologies—finance adjustment, cost allocation, aggregation. Decision impact: Cannot distinguish technical from political contestation causes without system knowledge, cannot assess governance solution feasibility without history, cannot quantify truth gaps without methodology visibility. Uncertainties material to M&A—acquirer diligence likely to demand customer profitability, satisfaction data, operational metrics with methodology transparency. If Rackspace cannot produce or methodology defensibility weak, valuation risk or deal failure. Reducing uncertainty requires: IT architecture documentation, governance initiative history, measurement practice disclosure, methodology documentation—all likely exist internally but not publicly disclosed, require diligence access.
# 1.1 Corporate Legal Existence

*Part of [Stage 1: Corporate Legal Structural](../README.md)*


## Control Constraints


### Control Constraints


**Constraint Description:** First Lien Credit Agreement dated March 12, 2024: $1.3B term loan with springing financial maintenance covenant (5.0x super-priority net senior secured leverage ratio) applicable to revolving credit facility when utilization exceeds 35% of commitments.
**Constraint Type:** CONTRACTUAL  

**Affected Entities:**
  - Rackspace Finance, LLC (borrower)
  - Rackspace Finance Holdings, LLC (guarantor)
  - Rackspace Technology, Inc. (ultimate parent)
  - All subsidiary guarantors

**What Breaks If Touched:** Altering ownership or control of Rackspace Technology, Inc. or borrower entity triggers change-of-control provisions requiring: (1) Mandatory offer to repay debt in full, or (2) Lender consent to ownership change. Failure to comply = immediate event of default and debt acceleration. Leverage covenant violation (if triggered) results in default, acceleration, and potential foreclosure on pledged collateral (substantially all assets). Interest rate: Term SOFR + 2.75% (floor 0.75%). Prepayment subject to make-whole premium until September 12, 2025. Maturity May 15, 2028.
**Claim Type:** `FACT`  

**Evidence Sources:**
  - First Lien Credit Agreement terms disclosed in Rackspace IR press release dated March 12, 2024
  - Form 8-K filed March 7, 2024 with credit agreement as Exhibit 10.1
  - Globenewswire and Yahoo Finance coverage of March 2024 refinancing

---


**Constraint Description:** Negative covenants under First Lien Credit Agreement restricting borrower and guarantors from: (1) incurring additional debt beyond specified baskets, (2) paying dividends or making restricted payments, (3) consolidating, merging, or selling substantially all assets, (4) creating additional liens beyond permitted liens.
**Constraint Type:** CONTRACTUAL  

**Affected Entities:**
  - Rackspace Finance, LLC
  - All subsidiary guarantors

**What Breaks If Touched:** Attempting to: (1) Raise additional debt at operating subsidiary level without lender consent, (2) Pay dividends to Rackspace Technology, Inc. shareholders, (3) Sell material subsidiaries or asset portfolios (customer contracts, data centers, IP), or (4) Grant security interests to other creditors - all constitute covenant violations resulting in default and acceleration. Operating flexibility is constrained by these covenants until debt is repaid or refinanced.
**Claim Type:** `FACT`  

**Evidence Sources:**
  - Negative covenants described in Rackspace IR press release March 12, 2024
  - Standard first lien credit agreement structure (typical for leveraged loans)

---


**Constraint Description:** Apollo Global Management majority ownership (53-57% of equity) provides effective control over shareholder decisions requiring simple majority, including: board elections, bylaw amendments, certain merger approvals, and other ordinary course matters.
**Constraint Type:** LEGAL  

**Affected Entities:**
  - Rackspace Technology, Inc.

**What Breaks If Touched:** Actions requiring shareholder approval cannot proceed without Apollo consent. Apollo can block or approve: (1) Board composition changes, (2) Executive compensation plans, (3) Equity incentive plans, (4) Certain M&A transactions. Dilutive equity issuances or secondary offerings could reduce Apollo's stake below majority, altering control dynamics and potentially triggering Apollo's contractual rights under investor agreements (if any exist - not disclosed publicly).
**Claim Type:** `FACT`  

**Evidence Sources:**
  - Apollo ownership percentage: 53-57% per Yahoo Finance (Nov 2024) and ainvest.com (Jul 2025)
  - Standard Delaware corporate law majority voting thresholds

---


**Constraint Description:** Board composition includes Apollo-affiliated directors (Aaron Sobel and Vikram Mahidhar), providing Apollo with direct governance participation and information rights. Board decisions require director votes; Apollo-affiliated directors can influence or veto board-level decisions.
**Constraint Type:** LEGAL  

**Affected Entities:**
  - Rackspace Technology, Inc.

**What Breaks If Touched:** Removing Apollo directors without Apollo consent would violate investor rights agreements (if any exist - typical for PE-backed public companies). Apollo representatives have access to board-level strategic discussions, financial information, and veto rights over material transactions. Diminishing Apollo board representation would require either: (1) Apollo voluntarily relinquishing seats, (2) Apollo's ownership falling below contractual thresholds (if specified in investor agreements), or (3) Shareholder vote to remove directors (which Apollo controls via majority stake).
**Claim Type:** `FACT`  

**Evidence Sources:**
  - Board composition per Rackspace IR press release January 17, 2025
  - Apollo affiliations: Aaron Sobel (Principal, Apollo since 2011), Vikram Mahidhar (Operating Partner, Apollo since 2021)

---


**Constraint Description:** NASDAQ listing requirements impose ongoing disclosure, governance, and financial compliance obligations. Delisting would require voluntary delisting application or going-private transaction complying with SEC Rule 13e-3.
**Constraint Type:** REGULATORY  

**Affected Entities:**
  - Rackspace Technology, Inc.

**What Breaks If Touched:** Taking company private or delisting requires: (1) Tender offer for all public shares, (2) Fairness opinion, (3) SEC Schedule 13E-3 filing, (4) Shareholder vote, (5) Compliance with appraisal rights. Maintaining listing requires: minimum bid price ($1.00), minimum market cap, audit committee, independent directors, annual meetings. Current stock price ($0.48 as of Feb 4, 2026) is below NASDAQ minimum - company may be at risk of delisting notice, which would trigger either price recovery plan or voluntary delisting.
**Claim Type:** `FACT`  

**Evidence Sources:**
  - NASDAQ listing confirmed via public market data (RXT ticker)
  - Stock price $0.4757 per Yahoo Finance February 4, 2026
  - NASDAQ listing rules (publicly available)
  - SEC Rule 13e-3 going-private requirements (publicly available)

---


**Constraint Description:** Subsidiary guarantee structure: multiple operating subsidiaries guarantee debt obligations. Release of guarantors requires lender consent or full debt repayment.
**Constraint Type:** CONTRACTUAL  

**Affected Entities:**
  - Rackspace Technology Global, Inc.
  - Rackspace US, Inc.
  - Other subsidiary guarantors (not fully enumerated in public sources)

**What Breaks If Touched:** Selling, spinning off, or divesting any subsidiary guarantor requires: (1) Release from guarantee (lender consent required), or (2) Substitution of replacement guarantor with equivalent creditworthiness, or (3) Full repayment of debt. Operating subsidiaries cannot be separated from parent without addressing guarantee obligations. This constraint prevents asset sales, carve-outs, or restructurings that would diminish collateral pool securing lenders.
**Claim Type:** `FACT`  

**Evidence Sources:**
  - Guarantee structure described in March 12, 2024 press release: 'guaranteed on a senior secured basis, jointly and severally, by New Holdings and by certain of the New Borrower's subsidiaries'
  - Subsidiary guarantors comprise same entities that guaranteed prior credit facilities

---


**Constraint Description:** Active litigation: Alpha Modus Ventures patent infringement lawsuit filed June 2024 in Western District of Texas against Rackspace US, Inc. Pending class action related to 2022 ransomware attack (most other suits resolved via arbitration/settlement).
**Constraint Type:** LEGAL  

**Affected Entities:**
  - Rackspace US, Inc. (patent defendant)
  - Rackspace Technology, Inc. (potential indemnitor or ultimate liability holder)

**What Breaks If Touched:** Sale or transfer of Rackspace US, Inc. during pending litigation could: (1) Complicate litigation posture, (2) Trigger successor liability analysis, (3) Be perceived by court as attempt to evade judgment, (4) Require litigation stay or refiling against new owner. Material adverse judgment could create contingent liability affecting valuation or requiring disclosure in M&A transaction. Patent infringement involves FCoE technology potentially core to service offerings - adverse judgment could require licensing, design-around, or service discontinuation.
**Claim Type:** `FACT`  

**Evidence Sources:**
  - Alpha Modus lawsuit: Globenewswire June 24, 2025 and Stock Titan coverage
  - Ransomware litigation: SecurityWeek, Law Street Media, and San Antonio Express-News coverage (2022-2023)
  - Litigation status: most suits sent to arbitration or settled per San Antonio Express-News May 2023

---


**Constraint Description:** Compliance certifications (ISO, SOC 2, HIPAA/HITRUST, FedRAMP) are entity-specific and likely held by operating subsidiaries. These certifications are contractually required by enterprise customers and government clients.
**Constraint Type:** OPERATIONAL  

**Affected Entities:**
  - Operating subsidiaries (likely Rackspace Technology Global, Inc. and Rackspace US, Inc.)

**What Breaks If Touched:** Transferring assets or restructuring entities holding compliance certifications triggers recertification requirements. Customers with HIPAA BAAs, FedRAMP authorizations, or SOC 2 contractual requirements would need to re-approve new entity or certificate holder. Recertification timelines: SOC 2 (6-12 months), HITRUST (6-9 months), FedRAMP (12-18 months). During recertification gap, company cannot serve regulated customers (healthcare, government) - representing material revenue risk. Certifications likely cannot be 'transferred' but must be re-earned by successor entity.
**Claim Type:** `INFERENCE`  

**Evidence Sources:**
  - Compliance certifications listed on Rackspace.com/compliance: ISO 27001, SOC 2, HIPAA/HITRUST, FedRAMP, FISMA, PCI
  - Certification entity-specificity and recertification requirements are standard in industry (ISO 27001 standard, FedRAMP guidelines, HITRUST CSF requirements)

---


## Disconfirming Evidence Not Found


### Disconfirming Evidence Not Found

**Description:** Evidence of covenant-lite debt structure or unencumbered balance sheet  

**Why Expected:** If H2 (material debt covenants) were false, would expect to find: (1) Loan agreements described as 'covenant-lite' in press releases, (2) Absence of financial maintenance covenants, (3) Minimal or no negative covenants, (4) Public statements about financial flexibility or unencumbered assets, (5) Credit rating agency reports describing minimal covenant protection.

**Impact Of Absence:** Absence of covenant-lite evidence SUPPORTS H2. Presence of springing leverage covenant, negative covenants, change-of-control provisions, and make-whole premiums confirms debt is RESTRICTIVE, not permissive. Company's corporate actions are materially constrained by debt covenants.

---

**Description:** Evidence of simple single-entity corporate structure  

**Why Expected:** If H1 (multi-tiered structure) were false, would expect to find: (1) Single entity listed in SEC filings with no subsidiaries, (2) Exhibit 21 stating 'no subsidiaries', (3) Credit agreements with single borrower and no guarantors, (4) All contracts, employment agreements, and litigation naming same entity, (5) No intercompany transactions in financial statements.

**Impact Of Absence:** Absence of single-entity evidence SUPPORTS H1. Multiple distinct entities identified across credit agreements, employment contracts, litigation, and subsidiary disclosures. Structure is multi-tiered with separate finance vehicles, operating entities, and legacy acquisition vehicles.

---

**Description:** Evidence of dispersed public ownership without controlling shareholder  

**Why Expected:** If H5 (concentrated ownership) were false, would expect to find: (1) Proxy statements showing no >10% shareholders, (2) All directors identified as 'independent' with no sponsor affiliations, (3) Press coverage describing 'widely held' company, (4) Absence of PE investor in company description, (5) No Schedule 13D/13G filings showing large blocks.

**Impact Of Absence:** Absence of dispersed ownership evidence SUPPORTS H5. Apollo's 53-57% majority stake is consistently reported across multiple sources. Board includes Apollo affiliates. Company is controlled by PE sponsor despite public listing. This is unusual structure (typical PE exit is full sale or complete IPO, not retention of majority control).

---

**Description:** Evidence of FCC, state banking, or other structural regulatory licenses  

**Why Expected:** If H3 (regulatory licensing) were true in structural sense, would expect to find: (1) FCC license numbers or authorizations, (2) State public utility commission approvals, (3) State banking or insurance licenses, (4) Regulatory filing requirements with industry-specific agencies, (5) 10-K risk factors discussing licensing requirements and renewal risks, (6) Change-of-control provisions requiring regulatory approval.

**Impact Of Absence:** Absence of structural licensing evidence WEAKENS H3. Company operates in substantially unregulated industry from structural perspective. Compliance certifications found (ISO, SOC, HIPAA, FedRAMP) are operational/contractual, not regulatory licenses. No evidence of government approvals required for ownership changes (beyond generally applicable SEC, antitrust, and Delaware corporate law).

---

**Description:** Evidence of minimal or no litigation exposure  

**Why Expected:** If H4 (material litigation) were false, would expect to find: (1) 10-K Item 3 stating 'Company is not party to any material litigation', (2) No PACER docket entries for Rackspace entities, (3) No contingent liability reserves in financial statements, (4) Absence of litigation-related press releases or news coverage, (5) No disclosed settlements or judgments.

**Impact Of Absence:** Partial absence: Found active patent litigation (Alpha Modus, filed June 2024) and one remaining ransomware class action, BUT most ransomware litigation resolved via arbitration/settlement. No regulatory investigations found. No securities litigation found. Litigation exposure is PRESENT but appears LIMITED in scope. Not 'no material litigation' but also not bet-the-company litigation.

---

**Description:** Evidence of independent board majority without PE sponsor representation  

**Why Expected:** If Apollo's control (H5) were governance-limited despite equity majority, would expect to find: (1) Board majority identified as 'independent' with no Apollo affiliations, (2) Lead independent director structure limiting sponsor influence, (3) Special committee structures for related-party transactions, (4) Public statements about board independence or governance best practices.

**Impact Of Absence:** Absence of independent board evidence SUPPORTS H5. Board includes Apollo affiliates (Sobel, Mahidhar). Apollo controlled Chairman role until January 2025 (Sambur). No evidence of governance structures limiting Apollo's board influence. Combined with 53-57% equity stake, Apollo has full governance and equity control.

---

**Description:** Evidence of material subsidiary operating licenses issued by foreign governments  

**Why Expected:** If H3 were true in international context, would expect to find: (1) References to data residency licenses in EU, China, or other jurisdictions, (2) Telecommunications licenses in countries with restrictive telecom regulations, (3) Cloud service provider registrations with foreign regulators, (4) Restrictions on foreign ownership in subsidiary jurisdictions.

**Impact Of Absence:** Absence of foreign licensing evidence further WEAKENS H3. No evidence of foreign government licenses creating change-of-control constraints. Company lists 'international subsidiaries' (Canada, Singapore, Mexico, etc.) but no indication these jurisdictions impose structural licensing beyond general business registration.

---

**Description:** Evidence that Inception entities have been dissolved or merged out of structure  

**Why Expected:** If Inception Parent Inc. and Inception Intermediate Inc. served no ongoing purpose, would expect to find: (1) Dissolution filings with Delaware Secretary of State, (2) Merger certificates showing consolidation into parent or operating entities, (3) Subsidiary lists excluding these entities, (4) Management discussion of corporate simplification.

**Impact Of Absence:** Absence of dissolution evidence indicates Inception entities remain in structure despite serving no obvious operating purpose. Possible explanations: (1) Hold tax attributes from 2016 acquisition, (2) Contractually required by Apollo as ownership vehicle, (3) Not yet eliminated due to low priority or legal/tax complexity. Creates structural complexity without clear operational benefit.

---


**Description:** Evidence of material intangible asset holdings (patents, trademarks, customer contracts) assigned to Rackspace Technology Inc. at parent level

**Why Expected:** If material assets consolidated at parent level (simplifying separation analysis), would expect to find: (1) IP assignment agreements from subsidiaries to parent, (2) Parent entity listed as party to material customer contracts, (3) Parent entity named as patent holder in USPTO records, (4) Master services agreements with parent as contracting entity.

**Impact Of Absence:** Absence of parent-level asset consolidation evidence suggests assets remain distributed across operating subsidiaries. This creates separation complexity: cannot acquire parent equity cleanly without inheriting all subsidiaries, and cannot carve out subsidiaries without addressing asset assignments and customer contract novations.

---


## Entities


### Material Legal Entities


#### Rackspace Technology, Inc.

**Jurisdiction:** Delaware  
**Entity Type:** C Corporation (Public)  

**Ownership Structure:** Publicly traded on NASDAQ (ticker: RXT). Apollo Global Management holds approximately 53-57% of outstanding shares as of Q4 2024/Q1 2025. Remaining ~43-47% dispersed among public shareholders and institutional investors.

**Control Mechanisms:** Board representation: Apollo affiliates Aaron Sobel (Principal, Apollo) and Vikram Mahidhar (Operating Partner, Apollo) serve as directors. Jeffrey Benjamin serves as Independent Chairman (as of January 2025, replacing Apollo's David Sambur). Apollo's majority shareholding provides effective control over shareholder votes requiring simple majority.

**Material Assets Or Functions:**
  - Parent entity for consolidated group
  - Publicly traded equity vehicle
  - Ultimate beneficial ownership consolidation point
  - SEC reporting entity

**Change Of Control Implications:** Change of control triggers: (1) Debt acceleration rights under First Lien Credit Agreement, (2) Potential repricing or refinancing requirements, (3) NASDAQ delisting if taken private without proper procedure, (4) Executive employment agreement change-of-control provisions.

**Touch Test Failure Mode:** LEGAL/CONTRACTUAL: Altering control of parent triggers debt acceleration rights, requiring lender consent or full repayment of $1.3B term loan. REGULATORY: Sale or merger requires SEC disclosure, shareholder vote, and compliance with Delaware corporate law. OPERATIONAL: Equity structure change affects public market access and investor base.
**Claim Type:** `FACT`  

**Evidence Sources:**
  - NASDAQ listing verified via public market data (RXT ticker active as of Feb 2026)
  - Apollo ownership: Yahoo Finance and ainvest.com articles citing 53-57% stake (Nov 2024-Jul 2025)
  - Board composition: Rackspace IR press release Jan 17, 2025 announcing board transitions
  - Change-of-control provisions: First Lien Credit Agreement disclosed in Form 8-K filed March 12, 2024

---


#### Rackspace Finance, LLC

**Jurisdiction:** Inferred Delaware (typical for finance SPVs, not explicitly disclosed in available sources)  
**Entity Type:** Limited Liability Company  
**Ownership Structure:** Indirect wholly-owned subsidiary of Rackspace Technology, Inc. Owned by Rackspace Finance Holdings, LLC.  

**Control Mechanisms:** Borrower entity under First Lien Credit Agreement. Control exercised through parent company ownership and credit agreement covenants.

**Material Assets Or Functions:**
  - Borrower under $1.3B First Lien Term Loan (as of March 2024)
  - Central debt issuance vehicle for consolidated group
  - Subject to financial maintenance covenants

**Change Of Control Implications:** Change of control at Rackspace Technology, Inc. level constitutes event of default under credit agreement, requiring lender consent or immediate repayment. Cannot be sold or transferred separately without triggering debt acceleration.

**Touch Test Failure Mode:** CONTRACTUAL (IMMEDIATE): Altering ownership triggers mandatory offer to repurchase debt or obtain lender consent. Debt sits at this entity level - cannot separate from parent without restructuring $1.3B obligation. LEGAL: Merger or dissolution requires lender approval per credit agreement negative covenants.
**Claim Type:** `FACT`  

**Evidence Sources:**
  - First Lien Credit Agreement dated March 12, 2024 (referenced in Form 8-K and press release)
  - Rackspace IR press release March 12, 2024 describing Rackspace Finance, LLC as borrower
  - Form 8-K filed March 7, 2024 with credit agreement exhibits

---


#### Rackspace Finance Holdings, LLC

**Jurisdiction:** Inferred Delaware (not explicitly disclosed in available sources)  
**Entity Type:** Limited Liability Company  

**Ownership Structure:** Indirect subsidiary of Rackspace Technology, Inc. Serves as intermediate holding company between parent and borrower entity.
**Control Mechanisms:** Provides limited-recourse guarantee of debt obligations. Intermediate layer between public parent and debt vehicle.  

**Material Assets Or Functions:**
  - Holdings entity for Rackspace Finance, LLC (borrower)
  - Limited-recourse guarantor of First Lien Credit Agreement obligations
  - Structural isolation layer between public parent and debt

**Change Of Control Implications:** Subject to same change-of-control triggers as borrower entity due to guarantee obligations and credit agreement definitions.

**Touch Test Failure Mode:** CONTRACTUAL: Cannot be dissolved, merged, or sold without violating credit agreement structure. Serves as intermediate layer for limited-recourse guarantee - removing this entity would alter creditor recourse rights. LEGAL: Restructuring requires lender consent and potential debt refinancing.
**Claim Type:** `FACT`  

**Evidence Sources:**
  - Rackspace IR press release March 12, 2024 identifying Rackspace Finance Holdings, LLC as holdings entity
  - Credit agreement structure disclosed in Form 8-K March 7, 2024

---


#### Rackspace Technology Global, Inc.

**Jurisdiction:** Inferred Delaware or Texas (formerly Rackspace Hosting, Inc., not explicitly disclosed)  
**Entity Type:** Corporation  

**Ownership Structure:** Wholly-owned subsidiary of Rackspace Technology, Inc. (formerly the target of Apollo's 2016 acquisition, now subsidiary after corporate reorganization for 2020 IPO).
**Control Mechanisms:** Operating subsidiary. Guarantor under debt instruments (both prior indentures and current credit agreement).  

**Material Assets Or Functions:**
  - Operating entity (inferred from name and history)
  - Party to indenture agreements as subsidiary guarantor (Feb 2021, Dec 2020)
  - Likely holds material customer contracts, IP, and operational licenses
  - Former pre-IPO parent entity (Rackspace Hosting, Inc.) renamed and repositioned as subsidiary

**Change Of Control Implications:** As subsidiary guarantor under credit agreement, change of control at parent level triggers guarantee obligations and potential acceleration. Cannot be sold separately without release from guarantee (requires lender consent).

**Touch Test Failure Mode:** CONTRACTUAL: Divestiture requires release from debt guarantee, which requires lender consent and likely debt paydown or replacement guarantee. OPERATIONAL: If this entity holds customer contracts, IP, or data center leases, separation would require assignment/assumption agreements with customers and landlords. REGULATORY: If this entity holds compliance certifications (ISO, SOC, HIPAA), separation triggers recertification requirements.
**Claim Type:** `INFERENCE`  

**Evidence Sources:**
  - Entity name found in subsidiary lists and contracts database (Justia)
  - Indenture agreements dated Feb 9, 2021 and Dec 1, 2020 listing as subsidiary guarantor
  - Historical context: Rackspace Hosting, Inc. was acquisition target in 2016, now renamed to Rackspace Technology Global, Inc. (per multiple sources including Wikipedia and acquisition documents)

---


#### Rackspace US, Inc.

**Jurisdiction:** Inferred United States (Delaware or Texas, not explicitly disclosed)  
**Entity Type:** Corporation  
**Ownership Structure:** Wholly-owned subsidiary of Rackspace Technology, Inc.  
**Control Mechanisms:** Operating subsidiary. Employing entity for U.S.-based personnel.  

**Material Assets Or Functions:**
  - U.S. employing entity (employment agreements with executives including DK Sinha, Mark Marino, Naushaza Molu list Rackspace US, Inc. as employer)
  - Named defendant in 2025 patent infringement lawsuit by Alpha Modus Ventures
  - Likely holds or operates under material regulatory compliance certifications
  - Inferred to control U.S. operations, customer relationships, and service delivery

**Change Of Control Implications:** As employing entity, change of control may trigger executive change-of-control provisions in employment agreements. As defendant in active patent litigation, transfer of ownership could complicate litigation posture or settlement negotiations.

**Touch Test Failure Mode:** OPERATIONAL: Separation requires employee transfer (WARN Act notifications, benefit plan transfers, state employment law compliance). CONTRACTUAL: Executive employment agreements contain change-of-control provisions tied to parent entity, but employment is with this entity. LEGAL: Active litigation (Alpha Modus patent case) - sale or transfer could be construed as attempt to evade judgment or complicate enforcement.
**Claim Type:** `FACT`  

**Evidence Sources:**
  - Employment agreements filed as exhibits to SEC filings (per Justia contracts database)
  - Alpha Modus Ventures federal lawsuit filed June 2024 in Western District of Texas naming Rackspace US, Inc. as defendant (Globenewswire June 24, 2025)
  - Stock Titan and Globenewswire reports on patent litigation

---


#### Inception Parent, Inc.

**Jurisdiction:** Delaware (typical for PE acquisition vehicles)  
**Entity Type:** Corporation  

**Ownership Structure:** Listed as subsidiary of Rackspace Technology, Inc. Originally formed as Apollo acquisition vehicle in 2016, retained in structure post-IPO.
**Control Mechanisms:** Legacy acquisition vehicle. Ownership inverted post-IPO (originally parent, now subsidiary).  

**Material Assets Or Functions:**
  - Legacy Apollo acquisition vehicle from 2016 take-private
  - No material operating function identified in current structure
  - Potentially holds historical tax attributes or serves structural purpose for Apollo's ongoing ownership

**Change Of Control Implications:** Unclear materiality. If entity holds tax attributes (NOLs, basis step-ups from 2016 acquisition), change of control at parent level could trigger limitations on tax attribute usage under IRC Section 382.

**Touch Test Failure Mode:** TAX (CONDITIONAL): If entity holds tax attributes from 2016 transaction, ownership change exceeding 50% within 3-year period triggers IRC Section 382 limitations on NOL utilization. STRUCTURAL: Apollo may require this entity to remain in structure as condition of ongoing ownership or financing arrangements (unknowable without internal documents).
**Claim Type:** `INFERENCE`  

**Evidence Sources:**
  - Entity listed in subsidiary disclosures (TrustArc PDF and search results)
  - Inception Parent, Inc. identified as Apollo acquisition vehicle in 2016 merger agreement (per OEM Capital and Law Insider references)
  - Retained in post-IPO structure per subsidiary lists

---


#### Inception Intermediate, Inc.

**Jurisdiction:** Delaware (typical for PE acquisition vehicles)  
**Entity Type:** Corporation  
**Ownership Structure:** Listed as subsidiary of Rackspace Technology, Inc. Part of Apollo's 2016 acquisition structure.  
**Control Mechanisms:** Intermediate holding vehicle between Inception Parent and operating entities (inferred from name).  

**Material Assets Or Functions:**
  - Intermediate holding layer from 2016 Apollo acquisition
  - No material operating function identified
  - May serve tax or structural isolation purpose

**Change Of Control Implications:** Similar to Inception Parent - potential tax attribute implications if entity holds step-up basis or other tax benefits from 2016 transaction.

**Touch Test Failure Mode:** TAX (CONDITIONAL): Ownership change may trigger tax attribute limitations. STRUCTURAL: Removal could violate Apollo's required ownership structure (unknowable without shareholder agreements or Apollo investment documents).
**Claim Type:** `INFERENCE`  

**Evidence Sources:**
  - Entity listed in subsidiary disclosures
  - Part of 2016 Apollo acquisition structure (per historical transaction documents)

---


## Hypotheses


### Hypothesis Framework


#### H1: The target operates through a multi-tiered entity structure with subsidiaries in multiple jurisdictions, creating layered ownership and potential regulatory complexity.


**Supporting Evidence Sought:**
  - SEC Exhibit 21 listing multiple subsidiaries
  - State and international corporate registry records
  - Credit agreement schedules listing borrower and guarantor entities
  - Multiple entity names appearing in contracts and litigation

**Disconfirming Evidence Sought:**
  - Single entity structure in SEC filings
  - No subsidiaries listed in Exhibit 21 or formation documents
  - Absence of intercompany transactions in financial statements
  - Simple single-entity credit agreement structure
**Status:** ✅ SUPPORTED  

**Notes:** SUPPORTING EVIDENCE FOUND: (1) Multiple entities identified: Rackspace Technology Inc. (parent), Rackspace Finance LLC and Holdings (debt vehicles), Rackspace Technology Global Inc., Rackspace US Inc., Inception entities. (2) Credit agreement explicitly references 'New Borrower' (Rackspace Finance LLC), 'New Holdings' (Rackspace Finance Holdings LLC), and 'Subsidiary Guarantors' (plural). (3) Employment agreements, indentures, and litigation name different Rackspace entities. (4) Subsidiary lists found in multiple sources (TrustArc PDF, search results referencing Exhibit 21). DISCONFIRMING EVIDENCE SOUGHT BUT NOT FOUND: No evidence of single-entity structure. Financial statements (not directly accessed but inferred from debt structure) must consolidate multiple entities. CONCLUSION: Multi-tiered structure confirmed. Complexity level: MODERATE (7+ material entities, 2-3 jurisdictional layers, debt isolated in separate vehicle).

---


#### H2: The target operates under debt agreements containing financial covenants, change-of-control provisions, and operational restrictions that materially constrain corporate actions.


**Supporting Evidence Sought:**
  - Credit agreements with financial maintenance covenants
  - Change-of-control definitions and consent requirements
  - Negative covenants restricting liens, asset sales, dividends, or additional debt
  - SEC filings disclosing covenant compliance or waivers

**Disconfirming Evidence Sought:**
  - Covenant-lite loan structure with no financial maintenance
  - Absence of debt or unencumbered balance sheet
  - Unrestricted debt with no operational constraints
  - Public statements confirming no material debt covenants
**Status:** ✅ SUPPORTED  

**Notes:** SUPPORTING EVIDENCE FOUND: (1) First Lien Credit Agreement dated March 12, 2024 with $1.3B term loan. (2) Springing financial covenant: 5.0x super-priority net senior secured leverage ratio (applies to revolving facility when utilization exceeds 35%). (3) Negative covenants confirmed: restrictions on debt incurrence, dividends/restricted payments, asset sales, liens, and mergers/consolidations. (4) Change-of-control provisions: mandatory offer to repurchase or lender consent required. (5) Make-whole premium on prepayments until Sep 12, 2025. DISCONFIRMING EVIDENCE SOUGHT BUT NOT FOUND: No evidence of covenant-lite structure. No evidence of unencumbered balance sheet (debt explicitly disclosed at $1.3B). CONCLUSION: Debt covenants materially constrain corporate actions. Springing covenant creates risk if revolving facility is drawn. Change-of-control provisions are HARD CONSTRAINT on M&A.

---


#### H3: The target operates in regulated industries requiring licenses, permits, or ongoing regulatory compliance that creates jurisdictional dependencies and operational constraints.


**Supporting Evidence Sought:**
  - Operating licenses required in specific states/countries
  - Regulatory filings with industry-specific agencies (FCC, banking, healthcare)
  - Compliance obligations disclosed in SEC filings
  - Regulatory consent requirements for ownership changes

**Disconfirming Evidence Sought:**
  - Business model in unregulated industry
  - No specialized licenses beyond basic business registrations
  - Absence of regulatory agency filings
  - 10-K risk factors lacking regulatory compliance discussion
**Status:** ⚠️ WEAKENED  

**Notes:** DISCONFIRMING EVIDENCE FOUND: (1) No evidence of FCC licensing requirements. (2) No evidence of state banking, insurance, or other structural licenses. (3) Compliance certifications found (ISO 27001, SOC 2, HIPAA/HITRUST, FedRAMP, PCI) are OPERATIONAL/CONTRACTUAL certifications, not regulatory licenses. These are earned through audits and can be re-certified by any entity willing to undergo audit process. (4) No evidence of regulatory agency oversight (FCC, state banking boards, healthcare regulators) that would create change-of-control approval requirements. SUPPORTING EVIDENCE (LIMITED): (1) FedRAMP authorization is government-issued but is an authorization to serve government customers, not a license required to operate. (2) Compliance certifications create OPERATIONAL constraints (recertification required if entities change) but not REGULATORY constraints (no government approval required for ownership changes). CONCLUSION: Hypothesis WEAKENED. Company operates in substantially unregulated industry from structural perspective. Compliance requirements are contractual/customer-driven, not regulatory. No evidence of change-of-control regulatory approvals required.

---


#### H4: The target is party to material litigation, regulatory investigations, or legal proceedings that create contingent liabilities or operational constraints beyond routine commercial disputes.


**Supporting Evidence Sought:**
  - Legal proceedings disclosed in 10-K with material dollar exposure
  - Ongoing regulatory investigations
  - Securities class actions or derivative suits
  - Contingent liabilities recorded in financial statements

**Disconfirming Evidence Sought:**
  - 10-K stating 'no material litigation'
  - PACER federal docket searches returning no material cases
  - No contingent liability reserves in financial statements
  - Only routine contract disputes below materiality thresholds
**Status:** ✅ SUPPORTED  

**Notes:** SUPPORTING EVIDENCE FOUND: (1) Alpha Modus Ventures patent infringement lawsuit filed June 2024 in W.D. Texas against Rackspace US, Inc. Claims infringe three foundational FCoE patents (U.S. Patents 11,108,591; 11,310,077; 11,303,473). Patents relate to core networking technology potentially used in service offerings. (2) 2022 ransomware attack generated multiple class action lawsuits. Most resolved via arbitration (judge granted motion to compel arbitration) or confidential settlement, but one class action remains pending. (3) Ransomware response costs: $10.8 million disclosed, 30,000 customers affected, Hosted Exchange product discontinued. WEAKENING EVIDENCE: (1) Most ransomware litigation resolved - only one class action remains. (2) No regulatory investigations disclosed (SEC, DOJ, FTC). (3) Patent lawsuit recently filed (June 2024) - no judgment yet, damages unknown. (4) No securities litigation or derivative suits identified. CONCLUSION: Hypothesis SUPPORTED but LIMITED. Material litigation exists (patent case, remaining ransomware class action) but exposure magnitude is UNKNOWN. Patent case could be material if technology is core to offerings. Ransomware litigation largely resolved. No regulatory enforcement actions identified.

---


#### H5: The target has concentrated ownership or control held by private equity sponsors, founder-insiders, or institutional blocks that creates principal-agent dynamics and potential conflicts in decision-making.


**Supporting Evidence Sought:**
  - Proxy statements showing >20% ownership blocks
  - Dual-class share structures with differential voting rights
  - Private equity ownership disclosed
  - Board composition dominated by sponsor-affiliated directors

**Disconfirming Evidence Sought:**
  - Widely dispersed public ownership with no >5% holders
  - Single-class common stock with one-share-one-vote
  - Independent board majority with no controlling shareholder
  - No disclosed beneficial owners above reporting thresholds
**Status:** ✅ SUPPORTED  

**Notes:** SUPPORTING EVIDENCE FOUND: (1) Apollo Global Management holds 53-57% of equity (per multiple sources Nov 2024-Jul 2025). This is MAJORITY CONTROL. (2) Board includes Apollo affiliates: Aaron Sobel (Principal, Apollo since 2011) and Vikram Mahidhar (Operating Partner, Apollo since 2021). (3) Former Apollo partner David Sambur served as Chairman until January 2025 (9 years). (4) Apollo led 2016 take-private transaction ($4.3B), took company public in 2020 IPO, maintained majority stake post-IPO. (5) Company returned to public markets but operates as PE-controlled public company (unusual structure). DISCONFIRMING EVIDENCE SOUGHT BUT NOT FOUND: No evidence of dispersed ownership. No evidence of independent board majority (Apollo has 2 of ~7-9 board seats inferred, plus Chairman until Jan 2025). CONCLUSION: Hypothesis STRONGLY SUPPORTED. Apollo has absolute control via majority equity stake. Board representation provides governance participation and information rights. Principal-agent conflict exists: Apollo's interests (financial return, exit optionality) may diverge from minority public shareholders or other stakeholders. Market cap of ~$120M on $0.48 stock price suggests market views Apollo control as value-destructive or is pricing in poor fundamentals.

---


## Uncertainties


### Uncertainty Register


**Unknown:** Complete list of subsidiary entities and their jurisdictions of incorporation. Exhibit 21 to 10-K not directly accessed due to SEC.gov 403 errors. Partial entity list compiled from secondary sources (employment agreements, litigation, contracts, press releases) but may be incomplete.
**Type:** UNKNOWN  

**Decision Impact:** MATERIAL: Incomplete subsidiary list creates risk of: (1) Missing entities holding material assets (IP, customer contracts, data center leases), (2) Unidentified jurisdictional exposures (foreign tax, regulatory, employment law), (3) Hidden guarantor obligations or cross-default triggers, (4) Missed change-of-control provisions at subsidiary level. Carve-out or divestiture analysis cannot be completed without complete entity list.

**What Would Reduce Uncertainty:** Direct access to: (1) Exhibit 21 to most recent 10-K (FY 2024 or FY 2025), (2) Credit agreement Schedule listing all borrower/guarantor entities, (3) Corporate organizational chart from management, (4) State/international corporate registry searches (requires budget and time).

---


**Unknown:** Existence and terms of Apollo investor rights agreement or shareholders agreement. Typical PE-backed public companies have investor rights agreements granting PE sponsor: (1) Board nomination rights, (2) Information rights, (3) Registration rights, (4) Consent rights over material actions, (5) Tag-along/drag-along rights. No such agreement found in public filings searched, but these are often filed as exhibits to IPO S-1 or subsequent 8-Ks.
**Type:** UNKNOWN  

**Decision Impact:** CRITICAL: If Apollo has contractual governance rights beyond equity voting: (1) Apollo consent may be required for M&A even if majority vote sufficient, (2) Apollo may have veto over divestitures, financing, or strategic changes, (3) Tag-along rights could force inclusion of Apollo in any sale process, (4) Drag-along rights could force minority holders to sell if Apollo exits. Without knowing these terms, cannot assess true control constraints.

**What Would Reduce Uncertainty:** Search SEC EDGAR for: (1) Form S-1 filed in connection with August 2020 IPO (Exhibits), (2) Form 8-K filings from 2020 announcing IPO and listing material agreements, (3) DEF 14A proxy statements (typically disclose material agreements with shareholders). If not publicly filed, would require management disclosure or data room access.

---


**Unknown:** Specific allocation of material assets (IP, customer contracts, data center leases, compliance certifications) to entity level. Know that Rackspace US Inc. employs U.S. staff and Rackspace Technology Global Inc. likely operates assets, but precise mapping unclear.
**Type:** UNKNOWN  

**Decision Impact:** MATERIAL: Cannot assess separability or carve-out feasibility without knowing: (1) Which entity holds IP (patents, trademarks, copyrights), (2) Which entity is party to customer contracts (and whether contracts are assignable), (3) Which entity leases data centers (and lease assignability), (4) Which entity holds compliance certifications (ISO, SOC, FedRAMP). Asset-level due diligence required before any M&A structuring.

**What Would Reduce Uncertainty:** Management disclosure: (1) IP assignment register showing which entity owns patents/trademarks, (2) Material contract schedule showing contracting entity for top customers, (3) Real estate schedule showing lessee entity for data centers, (4) Compliance certification schedule showing certificate holder entity. Alternatively: review 10-K risk factor section and MD&A for hints about asset location.

---


**Unknown:** Magnitude of contingent liabilities from: (1) Alpha Modus patent litigation (damages sought not disclosed in available sources), (2) Remaining ransomware class action (settlement value or judgment exposure unknown), (3) Unasserted claims from 2022 ransomware attack (customer claims, regulatory fines).
**Type:** UNKNOWN  

**Decision Impact:** MATERIAL: Patent damages could range from immaterial ($1-5M) to material ($50M+) depending on: (1) Revenue attributable to accused technology, (2) Willfulness finding (treble damages), (3) Ongoing royalty rate. Ransomware class action could settle for negligible amount or result in tens of millions judgment. Cannot assess true litigation risk without damages estimates. Material adverse judgment could trigger debt covenant violations or impair valuation.

**What Would Reduce Uncertainty:** Review: (1) 10-K Item 3 (Legal Proceedings) for disclosed litigation and damages estimates, (2) Financial statement footnotes for contingent liability reserves and range of exposure, (3) PACER dockets for Alpha Modus case to see damages contentions in complaint, (4) Engage litigation counsel to assess exposure range.

---


**Unknown:** Tax attributes held by Inception Parent Inc. and Inception Intermediate Inc. from 2016 Apollo acquisition. These legacy acquisition vehicles may hold NOLs, basis step-ups, or other tax benefits subject to IRC Section 382 limitations upon ownership change.
**Type:** UNKNOWN  

**Decision Impact:** MATERIAL: If entities hold significant NOLs (net operating losses) from pre-acquisition period or post-acquisition losses: (1) Ownership change exceeding 50% in 3-year period triggers Section 382 annual limitation on NOL usage, (2) Value of tax attributes could be impaired or lost, (3) Tax efficiency of structure may depend on maintaining these entities in current form. If no material tax attributes exist, entities may be eliminable through merger/dissolution (simplifying structure).

**What Would Reduce Uncertainty:** Review: (1) 10-K financial statement footnote on income taxes showing NOL carryforwards by jurisdiction and entity, (2) Tax provision footnote showing valuation allowances, (3) Deferred tax asset schedule. Would require tax diligence with management cooperation to access tax returns and Section 382 studies.

---


**Unknown:** Compliance certification entity-level holdings and recertification timelines. Assume operating subsidiaries hold ISO 27001, SOC 2, HIPAA/HITRUST, FedRAMP certifications, but precise mapping unknown.
**Type:** UNKNOWN  

**Decision Impact:** MATERIAL: If entity holding certifications is sold, restructured, or merged: (1) Certifications may not automatically transfer, (2) Recertification required (6-18 month timeline depending on framework), (3) During recertification gap, cannot serve regulated customers (healthcare HIPAA customers, government FedRAMP customers) - representing revenue loss. Need to map certifications to entities and assess recertification risk for any corporate structure change.

**What Would Reduce Uncertainty:** Request from management: (1) Compliance certification register showing entity name on each certificate, (2) Certification expiration dates and audit schedules, (3) Customer contract analysis showing which customers require which certifications, (4) Revenue mapping to certification-dependent customers.

---


**Unknown:** NASDAQ minimum bid price compliance status. Stock trading at $0.48 (below $1.00 minimum). Unknown whether company has received deficiency notice or is subject to cure period.
**Type:** UNKNOWN  

**Decision Impact:** MATERIAL: If company has received NASDAQ deficiency notice: (1) Typically 180-day cure period to regain compliance (stock must close above $1.00 for 10 consecutive trading days), (2) If not cured, company faces delisting to OTC markets, (3) Delisting impairs liquidity, institutional ownership, and public currency for M&A, (4) May trigger debt covenant violations if credit agreement contains listing covenant. If delisting is imminent, could force going-private transaction or reverse stock split.

**What Would Reduce Uncertainty:** Review: (1) Recent 8-K filings for NASDAQ deficiency notice, (2) Press releases addressing stock price or listing status, (3) 10-K/10-Q risk factors discussing exchange listing, (4) Direct inquiry to NASDAQ or company IR.

---


**Unknown:** Borrowing base availability and revolving credit facility utilization. Springing leverage covenant (5.0x ratio) applies only when revolving facility utilization exceeds 35% of commitments. Unknown: (1) Total revolver commitment size, (2) Current drawn amount, (3) Available capacity, (4) Whether company is approaching 35% threshold that would trigger covenant testing.
**Type:** UNKNOWN  

**Decision Impact:** MATERIAL: If revolver utilization is approaching or exceeds 35% threshold: (1) Financial covenant becomes active, (2) Must maintain 5.0x super-priority net senior secured leverage ratio, (3) Covenant violation triggers default and acceleration, (4) Operating flexibility constrained by need to manage leverage ratio. If well below 35%, covenant is dormant and less concerning. Liquidity position depends on revolver availability.

**What Would Reduce Uncertainty:** Review: (1) 10-Q/10-K financial statement footnote on debt showing revolver size and utilization, (2) MD&A liquidity discussion, (3) Credit agreement to understand revolver terms and borrowing base mechanics.

---


**Unknown:** Ultimate beneficial ownership structure of Apollo Global Management's stake. Apollo likely holds through multiple funds (Apollo Fund VIII or later vintage). Ownership may be fragmented across funds with different liquidity profiles and exit timing.
**Type:** UNKNOWN  

**Decision Impact:** INFORMATIVE: Understanding which Apollo funds hold stake informs: (1) Apollo's exit timeline (older vintage funds approaching end of life may seek exit sooner), (2) Whether stake can be easily sold or must be distributed to LPs, (3) Whether multiple Apollo funds have different interests. Does not change control analysis (Apollo controls regardless of fund structure) but informs negotiations and exit optionality.

**What Would Reduce Uncertainty:** Review: (1) Schedule 13D/13G filings by Apollo Global Management showing reporting persons and fund names, (2) Apollo's fund vintage and lifecycle (public information), (3) Management discussion of Apollo as investor.

---

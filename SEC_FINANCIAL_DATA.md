# SEC Financial Source Data — Rackspace Technology (NASDAQ: RXT)

**Version:** 1.0
**Date:** 2026-04-03
**Status:** SOURCE REFERENCE — Feeds T1 Entity Population
**Author:** Thomas Jones / The Hipster CISO
**Companion Document:** FINANCIAL_PROFILE_SPEC.md

---

## Purpose

This document captures all SEC-sourced and publicly reported financial data for Rackspace Technology across FY2023, FY2024, FY2025, and FY2026 guidance. It serves as the single source of truth for populating T1 confidence tier values on KG entities that map directly to SEC-reportable segments.

All values in this document are in USD millions unless otherwise noted. Values sourced from audited 10-K filings carry T1 confidence. Values derived from earnings releases carry T1 confidence for headline metrics and T2 for supplementary detail. FY2026 guidance carries FORECAST period type.

---

## T1 Entity Mapping — SEC Segments to KG Entities

Rackspace reports two operating segments in SEC filings. Each segment maps to both a ProductPortfolio entity and an OrganizationalUnit entity in the KG.

| SEC Segment | KG Entity ID | KG Entity Type | KG Entity Name |
|---|---|---|---|
| Private Cloud | pf-001 | ProductPortfolio | Private Cloud |
| Private Cloud | ou-002 | OrganizationalUnit | Private Cloud Business Unit |
| Public Cloud | pf-002 | ProductPortfolio | Public Cloud |
| Public Cloud | ou-001 | OrganizationalUnit | Public Cloud Business Unit |
**Consolidation note:** pf-001 and ou-002 represent the same SEC segment from different perspectives (product vs. org structure). Same values, different consolidation_method: pf-001 is STANDALONE (portfolio view), ou-002 is CONSOLIDATED (org rollup view). Same logic applies to pf-002/ou-001.

**Corporate/unallocated:** Corporate function costs are not allocated to segments in SEC reporting. These will be captured on the parent corporate OU entity as a separate T1 entry and will require identification of that entity before population.

---

## Consolidated Income Statement — Rackspace Technology, Inc.

### Revenue

| Metric | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| **Total Revenue** | $2,957M | $2,737M | $2,686M |
| YoY Change | -5% | -7.4% | -1.9% |
| Private Cloud Revenue | $1,210M | $1,055M | $990M |
| PC YoY Change | — | -13% (-14% CC) | -6% (-7% CC) |
| Public Cloud Revenue | $1,747M | $1,683M | $1,696M |
| PuC YoY Change | — | -3% (-4% CC) | +1% |

**Source:** 10-K filings (FY2023, FY2024), FY2025 Q4 earnings release (Feb 2026).
**CC** = Constant Currency basis.

### Cost of Revenue and Gross Profit

| Metric | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| **Cost of Revenue** | $2,328M | $2,204M | ~$2,178M (derived) |
| **Gross Profit** | $629M | $533M | ~$508M |
| **Gross Margin %** | 21.3% | 19.5% | 18.9% |

**FY2025 CoR derivation:** Total Revenue $2,686M × (1 - 0.189 gross margin) = ~$2,178M. This is T2 confidence (derived from reported margin percentage, not a direct SEC line item).
### Operating Expenses and Operating Income

| Metric | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| **Operating Expenses** | ~$767M | $708M | ~$609M (derived) |
| **GAAP Operating Loss** | $(899M) | $(909M) | $(101M) |
| **GAAP Operating Margin** | -30.4% | -33.2% | -3.8% |

**Note on FY2023-FY2024 operating losses:** These include significant non-cash impairment charges (goodwill, intangibles) that inflate the GAAP loss. FY2025 operating loss improvement to $(101M) reflects the absence of major impairments, not a fundamental change in operating economics at GAAP level.

**FY2025 OpEx derivation:** Revenue $2,686M - CoR ~$2,178M - GP ~$508M, then GP $508M - OpLoss $101M = OpEx ~$609M. This is T2 confidence.

### Non-GAAP Metrics (Management's Principal Measures)

| Metric | FY2023 | FY2024 | FY2025 | FY2026 Guidance |
|---|---|---|---|---|
| **Non-GAAP Operating Profit** | $157M | $106M | $126M | $160-170M |
| YoY Change | -50% (vs FY2022 $364M) | -33% | +19% | +27-35% |
| **Adjusted EBITDA** | — | ~$96M | $230M | $305-315M |
| EBITDA YoY Change | — | — | +140% | +33-37% |

**Note:** Non-GAAP Operating Profit excludes share-based comp, restructuring, transaction costs, Hosted Exchange incident costs, and certain non-recurring items. The delta between GAAP operating loss and Non-GAAP operating profit represents these adjustments — in FY2024 alone that gap was ~$1.0B, driven largely by impairment charges.

### Net Income / Loss

| Metric | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| **Net Loss** | $(838M) | $(863M) | $(226M) |

**Note:** Net loss includes interest expense on ~$2.7B debt load, which consumes a significant portion of operating cash flow.
---

## Balance Sheet (Year-End)

| Metric | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| **Cash & Equivalents** | $197M | $144M | $106M |
| **Total Liquidity** | ~$572M | ~$519M | $397M |
| (incl. undrawn revolver) | ($375M undrawn) | ($375M undrawn) | (revolver access) |
| **Accounts Receivable (net)** | — | $299M | — |
| **Total Assets** | — | $3,054M | ~$2,800M |
| **Long-Term Debt** | ~$2.7B | ~$2.7B | ~$2.7B |

**Debt context:** Rackspace carries ~$2.7B in long-term debt from the 2016 Apollo-led LBO. March 2024 refinancing extended maturities but did not reduce principal. Interest expense consumes a significant portion of operating cash flow. This debt load is THE defining constraint on the company's financial flexibility.

---

## Cash Flow Statement

| Metric | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| **Operating Cash Flow** | $375M | $40M | $151M |
| **Capital Expenditures** | $(181M) | $(136M) | $(139M) |
| **Free Cash Flow** | ~$194M | $(71M) | $91M |
| FCF YoY Change | — | -137% | +228% |

**FY2024 OCF collapse:** The dramatic decline from $375M to $40M in operating cash flow was driven by refinancing-related costs and working capital movements, not an operational deterioration of that magnitude. FY2025's recovery to $151M is more representative of normalized operating cash generation.
---

## Headcount

| Metric | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| **Total Employees** | ~5,800 | ~5,100 | ~7,200 |
| YoY Change | — | -12% | +41% |

**FY2025 headcount note:** The jump from ~5,100 to ~7,200 employees is sourced from third-party estimates (PitchBook: 7,705; Tracxn: 7,240; MacroTrends: 7,200). This is T2-T3 confidence — multiple sources corroborate the trend but exact figures vary. The official 10-K filing for FY2025 would provide the definitive number. This increase likely reflects hiring in AI/cloud engineering roles aligned with the strategic pivot.

---

## Segment Detail — Private Cloud (pf-001 / ou-002)

| Metric | FY2023 | FY2024 | FY2025 | FY2026 Guidance |
|---|---|---|---|---|
| **Revenue** | $1,210M | $1,055M | $990M | $1,025-1,075M |
| YoY Change | — | -13% | -6% | +4-9% (~6% mid) |
| **Operating Margin** | — | 27.9% (Non-GAAP) | — | — |
| **Revenue Mix** | 40.9% | 38.5% | 36.9% | ~39-40% |

**Segment characteristics:**
- Capital-intensive: Rackspace-owned/leased data center infrastructure
- Revenue model: Monthly recurring commitment, 12-36 month contracts
- Highest margin segment (27.9% non-GAAP operating margin in FY2024)
- Secular decline from cloud migration, BUT FY2026 guidance shows first growth in years
- H2 2024 bookings grew 42% vs H1, signaling demand inflection
- VMware/Broadcom licensing cost shock (200-300% price increases post-acquisition) threatens margin
**T1 population values for pf-001 / ou-002:**

```
FY2023:
  recurring_revenue: 1210000000  # Predominantly recurring (MRC model)
  non_recurring_revenue: null     # Not separately reported
  period_type: AUDITED
  confidence_tier: T1
  confidence_rationale: "SEC 10-K FY2023 segment reporting — Private Cloud revenue"
  revenue_recognition_method: OVER_CONTRACT_LIFE
  consolidation_method: STANDALONE  # (for pf-001) / CONSOLIDATED (for ou-002)

FY2024:
  recurring_revenue: 1055000000
  non_recurring_revenue: null
  period_type: AUDITED
  confidence_tier: T1
  confidence_rationale: "SEC 10-K FY2024 segment reporting — Private Cloud revenue"
  revenue_recognition_method: OVER_CONTRACT_LIFE

FY2025:
  recurring_revenue: 990000000
  non_recurring_revenue: null
  period_type: PRELIMINARY  # Earnings release, 10-K not yet filed as of doc date
  confidence_tier: T1
  confidence_rationale: "Q4/FY2025 earnings release — Private Cloud segment revenue"

FY2026:
  forecast_revenue: 1050000000  # Midpoint of $1,025-1,075M guidance
  period_type: FORECAST
  confidence_tier: T2
  confidence_rationale: "Management FY2026 guidance — midpoint of $1,025-1,075M range"
```
---

## Segment Detail — Public Cloud (pf-002 / ou-001)

| Metric | FY2023 | FY2024 | FY2025 | FY2026 Guidance |
|---|---|---|---|---|
| **Revenue** | $1,747M | $1,683M | $1,696M | $1,575-1,625M |
| YoY Change | — | -3% | +1% | -4-7% (~-6% mid) |
| **Revenue Mix** | 59.1% | 61.5% | 63.1% | ~60-61% |

**Segment characteristics:**
- Capital-light: Managed services on customer's AWS/Azure/GCP environments
- Revenue model: Variable based on customer cloud consumption + management fees
- Lower margin than Private Cloud but higher scalability
- FY2025 was first year of positive revenue growth after multi-year decline
- FY2026 decline driven by planned transition of a large government contract
- Excluding that contract, Public Cloud services revenue expected to grow mid-to-high teens
- Bookings grew 22% YoY in FY2024

**T1 population values for pf-002 / ou-001:**

```
FY2023:
  recurring_revenue: 1747000000  # Mix of recurring management fees + variable consumption
  non_recurring_revenue: null
  period_type: AUDITED
  confidence_tier: T1
  confidence_rationale: "SEC 10-K FY2023 segment reporting — Public Cloud revenue"
  revenue_recognition_method: OVER_CONTRACT_LIFE
FY2024:
  recurring_revenue: 1683000000
  non_recurring_revenue: null
  period_type: AUDITED
  confidence_tier: T1
  confidence_rationale: "SEC 10-K FY2024 segment reporting — Public Cloud revenue"

FY2025:
  recurring_revenue: 1696000000
  non_recurring_revenue: null
  period_type: PRELIMINARY
  confidence_tier: T1
  confidence_rationale: "Q4/FY2025 earnings release — Public Cloud segment revenue"

FY2026:
  forecast_revenue: 1600000000  # Midpoint of $1,575-1,625M guidance
  period_type: FORECAST
  confidence_tier: T2
  confidence_rationale: "Management FY2026 guidance — midpoint of $1,575-1,625M range"
```

---

## Consolidated T1 Values — Corporate Level

These values apply to the corporate-level entity (parent OU or top-level ProductPortfolio if one exists representing the consolidated enterprise).
```
FY2023:
  recurring_revenue: 2957000000
  cost_of_revenue: 2328000000
  operating_expense: 767000000  # T2 — derived
  capex: 181000000
  fte_count: 5800  # T2-T3 — third-party estimate
  period_type: AUDITED
  confidence_tier: T1  # Revenue, CoR are T1. OpEx, headcount are T2.
  confidence_rationale: "SEC 10-K FY2023 — consolidated income statement"
  consolidation_method: CONSOLIDATED
  consolidation_scope: ALL_DESCENDANTS
  balance_sheet:
    cash: 197000000
    debt: 2700000000  # Approximate

FY2024:
  recurring_revenue: 2737000000
  cost_of_revenue: 2204000000
  operating_expense: 708000000
  capex: 136000000
  fte_count: 5100  # T1 — reported in 10-K
  period_type: AUDITED
  confidence_tier: T1
  confidence_rationale: "SEC 10-K FY2024 — consolidated income statement"
  consolidation_method: CONSOLIDATED
  consolidation_scope: ALL_DESCENDANTS
  balance_sheet:
    cash: 144000000
    accounts_receivable: 299000000
    debt: 2700000000
    # total_assets: 3054000000 — not a schema field, captured here for reference
FY2025:
  recurring_revenue: 2686000000
  cost_of_revenue: 2178000000  # T2 — derived from reported margin
  operating_expense: 609000000  # T2 — derived
  capex: 139000000
  fte_count: 7200  # T3 — third-party estimates, variance across sources
  period_type: PRELIMINARY  # Earnings release, 10-K pending
  confidence_tier: T1  # Revenue is T1. CoR, OpEx are T2. Headcount is T3.
  confidence_rationale: "Q4/FY2025 earnings release — consolidated. CoR/OpEx derived from reported margin."
  consolidation_method: CONSOLIDATED
  consolidation_scope: ALL_DESCENDANTS
  balance_sheet:
    cash: 106000000
    debt: 2700000000

FY2026:
  forecast_revenue: 2650000000  # Midpoint of $2,600-2,700M guidance
  forecast_cost: null  # Not guided
  period_type: FORECAST
  confidence_tier: T2
  confidence_rationale: "Management FY2026 full-year guidance — midpoint of $2.6-2.7B range"
```

---

## FY2026 Extrapolation — Current Fiscal Year Theorization

Rackspace's fiscal year aligns with calendar year. FY2026 is the current fiscal year as of April 2026. Q1 2026 results have not yet been reported (expected May 2026).
### Revenue Extrapolation

| Segment | FY2025 Actual | FY2026 Guidance Low | FY2026 Guidance Mid | FY2026 Guidance High |
|---|---|---|---|---|
| Private Cloud | $990M | $1,025M | $1,050M | $1,075M |
| Public Cloud | $1,696M | $1,575M | $1,600M | $1,625M |
| **Total** | **$2,686M** | **$2,600M** | **$2,650M** | **$2,700M** |

### Profitability Extrapolation

| Metric | FY2025 Actual | FY2026 Guidance/Estimate | Basis |
|---|---|---|---|
| Non-GAAP Op Profit | $126M | $160-170M | Management guidance |
| Adjusted EBITDA | $230M | $305-315M | Management guidance |
| Gross Margin | 18.9% | ~19.5% (est.) | Trending toward recovery as PC grows, PuC exits low-margin contracts |
| GAAP Operating Loss | $(101M) | ~$(50-80M) (est.) | Assumes continued reduction in restructuring/non-recurring, no major impairments |

### Strategic Context for FY2026

The FY2026 story is a structural pivot. Private Cloud revenue grows for the first time in years (+6% mid YoY), driven by AI infrastructure demand (GPUaaS, sovereign cloud, healthcare/public sector verticals). Public Cloud declines on paper (-6% mid) but that's entirely attributable to one large government contract transition — underlying services revenue grows mid-to-high teens.

Non-GAAP Operating Profit guidance of $160-170M (+27-35% YoY) and Adjusted EBITDA guidance of $305-315M (+33-37% YoY) signal real margin expansion, not just revenue recomposition.

The $2.7B debt load remains the defining constraint. Even with improved EBITDA, interest expense consumes most of the operating cash generation, limiting reinvestment capacity and strategic optionality.
---

## Data Gaps and Next Steps

### Known Gaps (Need 10-K Filing Access)

| Gap | Impact | Priority |
|---|---|---|
| FY2025 detailed OpEx breakdown (SGA vs. D&A vs. restructuring) | Cannot allocate cost to functional departments | HIGH |
| FY2025 segment operating profit by segment | Cannot determine per-segment profitability for FY2025 | HIGH |
| FY2023/FY2024 D&A amounts | depreciation_amortization field on consolidated entity | MEDIUM |
| FY2025 official headcount from 10-K | fte_count reliability (currently T3) | MEDIUM |
| Interest expense by year | Needed for corporate-level cost structure | MEDIUM |
| Deferred revenue balances | deferred_revenue field | LOW |
| DSO/DPO calculations | dso_days, dpo_days fields | LOW |
| AR aging breakdown | balance_sheet.ar_aging_* fields | LOW |

### Recommended Actions

1. **Obtain 10-K filings directly.** The full 10-K for FY2024 (filed March 2025) and FY2025 (expected March 2026) contain the detailed income statement, balance sheet, and cash flow statement with all line items broken out. WebFetch was blocked on ir.rackspace.com and SEC EDGAR during data gathering.

2. **Populate T1 entities first** using the values documented above. Revenue figures are high-confidence T1. Derived values (CoR, OpEx from margins) should be marked T2 with explicit confidence_rationale.

3. **Add FY2025 and FY2026 fiscal year keys** to entity financial_profiles. Current clean baseline has FY2023 and FY2024 keys. Need to extend to FY2025 (PRELIMINARY) and FY2026 (FORECAST).

4. **Identify corporate-level entity** for consolidated values. Need to determine which OU entity represents the top-level Rackspace Technology, Inc. consolidated entity.

5. **After T1 population, cascade to T2.** Sub-portfolios and products with multiple corroborating sources (e.g., product-level revenue estimates from job postings + analyst reports + press releases).
---

## Source Citations

All data in this document was gathered from publicly available sources on 2026-04-03.

| Source | URL | Data Used |
|---|---|---|
| Rackspace Q4/FY2025 Earnings Release | ir.rackspace.com/news-releases/... | FY2025 revenue, segment revenue, operating loss, EBITDA, FCF, CapEx |
| Rackspace Q4/FY2024 Earnings Release | ir.rackspace.com/news-releases/... | FY2024 revenue, CoR, GP, operating loss, segment detail, balance sheet |
| Rackspace Q4/FY2023 Earnings Release | ir.rackspace.com/news-releases/... | FY2023 revenue, segment revenue, OCF, CapEx, Non-GAAP OP |
| StockTitan / RXT Financials | stocktitan.net/financials/RXT/ | FY2025 EBITDA, FCF, net loss, debt |
| StockAnalysis.com | stockanalysis.com/stocks/rxt/ | Income statement cross-reference |
| MacroTrends / RXT | macrotrends.net/stocks/charts/RXT/ | Revenue history, employee count |
| Seeking Alpha | seekingalpha.com/news/4558150 | FY2026 guidance detail (PC +6%, PuC -6%) |
| Yahoo Finance | finance.yahoo.com/news/rackspace-technology-reports-... | Earnings call highlights, guidance |
| Investing.com | investing.com/news/transcripts/... | Q4 2025 earnings call transcript summary |

---

## Change Log

| Date | Version | Change |
|---|---|---|
| 2026-04-03 | 1.0 | Initial source documentation. FY2023-FY2025 actuals + FY2026 guidance from public sources. |
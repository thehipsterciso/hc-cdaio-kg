# T1 Population — Common Decisions

**Date:** 2026-04-03
**Operator:** Claude (AI agent) under direction of Thomas Jones
**Source Document:** SEC_FINANCIAL_DATA.md
**Schema Reference:** FINANCIAL_PROFILE_SPEC.md

This file documents decisions that apply uniformly to all 5 T1 entities. Each per-entity audit file references this document rather than repeating the rationale.

---

## Why FY2025 and FY2026 keys were added

The clean baseline only had FY2023 and FY2024. We added FY2025 because audited/preliminary annual results exist (Q4/FY2025 earnings release, Feb 2026). We added FY2026 because management issued full-year guidance at the FY2025 earnings call. Four years of data enables trend analysis and forecasting.

## Why recurring_revenue is used instead of a generic "revenue" field

The schema has no "total_revenue" field — it has recurring_revenue and non_recurring_revenue, designed to be summed. Rackspace's segment revenue is predominantly recurring (MRC contracts for Private Cloud, managed services for Public Cloud). We map segment revenue to recurring_revenue because (a) the 10-K does not break out recurring vs. non-recurring at the segment level, and (b) both segments are structurally recurring businesses.

## Why non_recurring_revenue stays null

Not separately reported in SEC filings at segment level. Null (not zero) because absence of data ≠ assertion of zero. Rackspace has professional services and implementation fees that could qualify, but they're not broken out.
## Why most fields stay null

The universal schema has 25 core fields + 6 grouped containers per fiscal year. SEC segment-level reporting provides revenue only — not CoR, OpEx, CapEx, headcount, or balance sheet per segment. Those exist only at consolidated level. Leaving them null preserves integrity: null = "we don't know."

## Why forecast_revenue is used for FY2026

FY2026 is a FORECAST period. Management guidance is a range, not actuals. Using forecast_revenue (not recurring_revenue) correctly signals forward-looking vs. realized. Schema was designed with this distinction.

## Why confidence_tier changes from T4 to T1 or T2

T4 was the placeholder ("no data"). SEC filings → T1. FY2025 earnings release headline numbers → T1 (company stands behind them publicly). FY2026 guidance → T2 (management estimate, not audited, subject to revision).

## Why consolidation_method differs between portfolio and OU entities

ProductPortfolio (pf-001, pf-002): STANDALONE — product-line view, no accounting consolidation.
OrganizationalUnit (ou-001, ou-002, ou-029): CONSOLIDATED — organizational rollup where child financials aggregate upward.

## Why consolidation_scope differs

Segment-level OUs (ou-001, ou-002): DIRECT_CHILDREN — segment total = sum of direct child products/services.
Corporate (ou-029): ALL_DESCENDANTS — fully consolidated enterprise total.
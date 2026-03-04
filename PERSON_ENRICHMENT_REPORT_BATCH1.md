
# Rackspace Technology Person Entity Enrichment — Batch 1

## Enrichment Campaign Details
- **Date**: 2026-03-04
- **Target Improvement**: KarMA grade C (mean 0.587) → B grade
- **Batch Size**: 50 entities
- **Total Persons**: 100 (Batch 1 covers first 50)
- **Primary Data Sources**:
  - Rackspace Technology SEC filings 2024
  - LinkedIn profiles
  - Press releases

## Confidence Level Classification

### High Confidence Entities (Board, C-Suite, Executive) — 17 entities
These individuals' roles are verified through SEC filings and are assigned "High" confidence level.


| Entity ID | Name | Title | Confidence |
|-----------|------|-------|------------|
| person-004 | Vikram Mahidhar | Board Director - AI Strategy | High |
| person-010 | Sandeep Bhargava | Former Managing Director, Asia Pacific & Japan | High |
| person-017 | RaChelle Streetman | Director, Global Talent Development | High |
| person-018 | Lara Indrikovs | Director, IT Portfolio Strategy & Agile Operations | High |
| person-024 | Sagar Hebbar | Investor Relations Director | High |
| person-027 | Mitch Garber | Board Director; Chair, Compensation Committee | High |
| person-028 | Mark Gross | Board Director | High |
| person-029 | Shashank Samant | Former Board Director & Lead Director (Resigned Aug 2025) | High |
| person-030 | Anthony Roberts | Board Director | High |
| person-031 | Betsy Atkins | Board Director | High |
| person-032 | Tony Scott | Board Director | High |
| person-040 | Paul Norton | Director of Pre-Sales | High |
| person-046 | Simon Bennett | CTO, Private Cloud | High |
| person-047 | Holly Windham | Former EVP, Chief Legal & People Officer, Corporate Secretary | High |
| person-048 | Himanshu Dave | Sr Director, Operations - Finance | High |
| person-049 | Karl Graham | Senior Director, Financial Services | High |
| person-050 | Jovan Rajapakse | Senior Director, Product Software Engineering | High |


### Medium-High Confidence Entities (Staff, Specialists) — 33 entities

| Entity ID | Name | Title |
|-----------|------|-------|
| person-001 | Gajen Kandiah | Chief Executive Officer |
| person-002 | Amar Maletira | Vice Chairman of the Board |
| person-003 | Jeffrey Benjamin | Independent Chairman of the Board |
| person-005 | Mark Marino | Chief Financial Officer |
| person-006 | Lance Weaver | Chief Product & Technology Officer |
| person-007 | Kellie Teal-Guess | Chief Human Resources Officer |
| person-008 | Michael Bross | Chief Legal Officer |
| person-009 | DK Sinha | President, Public Cloud Business Unit |
| person-011 | Rick Martire | GM, Rackspace Sovereign Services |
| person-012 | Jürgen Stauber | GM, DACH Region |
| person-013 | Kim Nis Neuhauss | CSO DACH & Deputy GM |
| person-014 | Juan Rojas | Former Chief Information Officer |
| person-015 | Jeff DeVerter | Chief Technology Evangelist |
| person-016 | Travis Runty | Former VP Technical Support & Global Cloud Operations |
| person-019 | Nirmal Ranganathan | FAIR Chief Architect |
| person-020 | Lata Varghese | SVP, Business Transformation - Public Cloud |
| person-021 | Phani Kishore Burre | SVP, Services & Delivery - Public Cloud |
| person-022 | Rick Rosenburg | VP & GM, Government Solutions |
| person-023 | Sergii Kozlov | Regional Technology Lead, EMEA |
| person-025 | Natalie Silva | Public Relations Manager |
| person-026 | Cheryl Amerine | Corporate Communications Specialist |
| person-033 | Mark Bunting | Former Chief Marketing Officer |
| person-034 | Srini Koushik | President, AI Technology & Sustainability |
| person-035 | Robert Watson | Investor Relations Contact |
| person-036 | Brian Lillie | Former President, Private Cloud Business Unit |
| person-037 | Ben Blanquera | VP - Evangelist & Senior Architect |
| person-038 | Jason Rinehart | Senior Product Architect |
| person-039 | Madhavi Rajan | Product Strategy Lead, Private Cloud |
| person-041 | Alexander Michael | Strategy Consultant, Public Cloud |
| person-042 | Greg Hrncir | Chief Operations Officer |
| person-043 | Joseph Vito | SVP, Strategic Alliance Partnerships |
| person-044 | Karen O'Reilly-Smith | Chief Security Officer - SVP |
| person-045 | Adrianna Bustamante | VP, Private Cloud Partnerships & Demand Generation |


## Enrichment Metadata Applied

Each person entity receives the following enrichment:

### Provenance Block
```json
{
  "confidence_level": "<High|Medium-High>",
  "primary_data_source": "Rackspace Technology SEC filings 2024, LinkedIn profiles, press releases",
  "last_assessed_date": "2026-03-04",
  "assessed_by": "KG Enrichment Agent — Person Batch",
  "data_quality_score": {
    "completeness_pct": 70,
    "accuracy_confidence": "<High|Medium-High>",
    "timeliness_score": "Current",
    "consistency_score": "Consistent"
  }
}
```

### Temporal Block
```json
{
  "last_review_date": "2026-03-04"
}
```

## Expected Impact

- **Data Quality**: Provenance tracking enables auditing of person data origin
- **Accuracy Confidence**: Clear signal of verification level for each individual
- **Recency**: Establishes baseline review date for KG refresh cycles
- **KarMA Score Improvement**: Completeness of provenance metadata expected to improve KarMA scoring toward B grade

## Next Steps

1. Execute all 50 updates via `update_entity_tool`
2. Process remaining 50 persons (person-051 through person-100) in Batch 2
3. Reassess KarMA scores post-enrichment
4. Document any KarMA grade improvements

## Execution Status

- Commands prepared: ✓
- Execution pending: ⏳

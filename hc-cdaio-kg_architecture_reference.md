# hc-cdaio-kg: Knowledge Graph Architecture and Schema Reference

**Technical Document** | March 4, 2026 | Thomas Jones

---

## Document Summary

| Metric | Value |
|---|---|
| Total Entities | 2,944 |
| Total Relationships | 7,466 |
| Entity Types | 26 |
| Relationship Types | 42 |
| Distinct Edge Patterns | 114 |
| Graph File Size | 16.7 MB |
| Due Diligence Analysis Files | 401 JSON |

---

## Table of Contents

1. [Platform and Dataset](#platform-and-dataset)
2. [Architecture Overview](#architecture-overview)
3. [Base Entity Schema](#base-entity-schema)
4. [Entity Type Catalog](#entity-type-catalog)
5. [Relationship Architecture](#relationship-architecture)
6. [Edge Pattern Analysis](#edge-pattern-analysis)
7. [Due Diligence Analysis Layer](#due-diligence-analysis-layer)
8. [Known Structural Gaps](#known-structural-gaps)

---

## Platform and Dataset

### hc-enterprise-kg: The Platform

The [hc-enterprise-kg](https://github.com/thehipsterciso/hc-enterprise-kg) is an open-source enterprise knowledge graph platform designed to generate and analyze structural models of organizations. It provides the schema definition (30 entity types, 58 relationship types), the Pydantic v2 data models, the NetworkX graph backend, and a 16-tool MCP server that exposes graph analysis capabilities to AI assistants through natural language.

The platform's core premise is that in enterprise decision-making, the relationships between entities are where the insight lives. A list of systems is inventory. A graph of systems connected by dependency, hosting, governance, and data flow relationships is intelligence. hc-enterprise-kg provides the schema vocabulary and analytical tooling to build and interrogate that graph.

The platform supports synthetic generation for scenario modeling (with industry-specific profiles for technology, financial services, and healthcare organizations), CSV and text ingestion for real-world data, and a quality validation module that scores schema compliance, relationship integrity, and field correlation consistency. The MCP server enables Claude Desktop to perform blast radius analysis, centrality scoring, shortest-path traversal, and entity search against any loaded graph through conversational interaction.

### hc-cdaio-kg: The Dataset

This document describes hc-cdaio-kg, which is a specific dataset built on the hc-enterprise-kg platform. Where hc-enterprise-kg defines how to model an enterprise, hc-cdaio-kg models a specific one: Rackspace Technology, Inc., constructed entirely from public sources using AI-augmented OSINT as a practicum deliverable for the Carnegie Mellon University Heinz College CDAIO program.

The relationship between platform and dataset is analogous to a database engine and a specific database instance. hc-enterprise-kg provides the schema, validation rules, and query tools. hc-cdaio-kg provides the populated entities, relationships, and analytical conclusions for one target organization. The platform's 30-type schema defines the maximum vocabulary; this dataset uses 26 of those types and 42 of the 58 available relationship types, reflecting what was discoverable and material for the target organization.

The dataset includes a structured due diligence analysis layer (401 JSON files across nine stages) that does not exist in the platform itself. This layer represents the analytical methodology and findings specific to evaluating Rackspace Technology as a potential acquisition, investment, or transformation target. The platform provides the structural graph; hc-cdaio-kg adds both the populated data and the assessed conclusions.

| Concern | hc-enterprise-kg (Platform) | hc-cdaio-kg (Dataset) |
|---|---|---|
| Schema definition | 30 entity types, 58 relationship types | 26 entity types, 42 relationship types (subset) |
| Data population | Synthetic generation or ingestion | OSINT-sourced from public filings and records |
| Graph backend | NetworkX (swappable to Neo4j) | NetworkX via assembled graph.json |
| MCP server | 16 analytical tools | Loaded as the active graph instance |
| Quality validation | Schema compliance, relationship integrity | Pre-commit hooks, GitHub Actions CI |
| Analytical layer | Not included | 401 JSON files across 9 due diligence stages |
| Target audience | Any enterprise modeling use case | Rackspace Technology CDAIO assessment |

## Architecture Overview

The hc-cdaio-kg knowledge graph is an enterprise intelligence structure built to model a single target organization across every dimension material to a CDAIO-grade due diligence assessment. The graph stores 2,944 entities connected by 7,466 relationships, encoding 26 entity types and 42 relationship types that form 114 distinct source-type / relationship-type / target-type edge patterns.

The graph is accompanied by 401 structured JSON analysis files organized across nine due diligence stages, which represent the analytical conclusions built on top of the structural data.

### Design Philosophy

Three principles govern the schema design:

**Attribute density over entity count.** The schema prioritizes deep attribute coverage within each entity type over creating large populations of shallow entities. Data assets carry 60+ fields at near-complete population. In a due diligence context where follow-up access to the target organization may be limited, that density determines whether the graph generates new questions or answers existing ones.

**Temporal versioning.** Every entity carries `created_at`, `updated_at`, `valid_from`, `valid_until`, and `version` fields as part of the base schema. The graph can represent enterprise state at a specific point in time and track how entities change, which matters when assessing whether a governance program is improving or stagnating.

**Provenance tracking.** Every entity includes a `provenance` field recording the source and quality assessment of the information used to create it. In due diligence, the difference between a fact, an inference, and a claim from management can determine the reliability of the entire assessment. Entity-level provenance makes the graph's own epistemic confidence queryable.

### Graph Statistics

Entity type distribution ordered by population count:

| Entity Type | Count | % of Total | Schema Fields |
|---|---|---|---|
| role | 427 | 14.5% | 63 |
| integration | 378 | 12.8% | 32 |
| control | 340 | 11.5% | 35 |
| department | 250 | 8.5% | 11 |
| data_asset | 164 | 5.6% | 83 |
| system | 164 | 5.6% | 117 |
| policy | 114 | 3.9% | 36 |
| organizational_unit | 109 | 3.7% | 86 |
| person | 100 | 3.4% | 70 |
| network | 94 | 3.2% | 12 |
| data_domain | 88 | 3.0% | 23 |
| customer | 85 | 2.9% | 60 |
| product_portfolio | 71 | 2.4% | 20 |
| regulation | 70 | 2.4% | 21 |
| business_capability | 64 | 2.2% | 81 |
| jurisdiction | 61 | 2.1% | 23 |
| site | 58 | 2.0% | 83 |
| geography | 57 | 1.9% | 20 |
| vendor | 55 | 1.9% | 81 |
| location | 46 | 1.6% | 15 |
| contract | 37 | 1.3% | 43 |
| product | 33 | 1.1% | 72 |
| market_segment | 26 | 0.9% | 24 |
| initiative | 24 | 0.8% | 79 |
| risk | 22 | 0.7% | 43 |
| incident | 7 | 0.2% | 19 |

---

## Base Entity Schema

Every entity in the graph inherits a common set of base attributes regardless of type. These attributes provide identity, temporal context, versioning, and provenance tracking across the entire graph.

| Attribute | Population % | Sample Value |
|---|---|---|
| `id` | 100.0% | `bc-001` |
| `entity_type` | 100.0% | `business_capability` |
| `created_at` | 100.0% | `2026-02-25T19:01:57.283991Z` |
| `updated_at` | 100.0% | `2026-03-04T08:43:28.787752Z` |
| `valid_from` | 0.0% | `None` |
| `valid_until` | 0.0% | `None` |
| `version` | 100.0% | `2` |
| `tags` | 0.0% | `[]` |
| `name` | 100.0% | `Corporate Strategy & Planning` |
| `description` | 97.5% | `Enterprise-level strategic planning, long-term vision develo` |
| `provenance` | 100.0% | `{'data_quality_score': {'completeness_pct': 50.0, 'accuracy_` |
| `temporal` | 100.0% | `{'effective_date': None, 'expiration_date': None, 'last_revi` |

### Identity and Classification

The `id` field is a unique identifier (format varies by type: some use structured IDs like `bc-001` for business capabilities, others use UUIDs). The `entity_type` field classifies each entity into one of 26 types, which determines which type-specific attributes are available. The `name` field provides a human-readable label, populated across 100% of entities. The `description` field carries a prose summary of the entity's purpose, populated at 97.5%.

### Temporal Metadata

The `created_at` and `updated_at` fields track when each entity was first ingested into the graph and when it was last modified (both ISO 8601 timestamps, 100% populated). The `valid_from` and `valid_until` fields are available for modeling the business-effective period of an entity but are currently unpopulated (0%), indicating the graph captures current-state rather than historical-state data. The `version` field (100% populated) tracks modification count, enabling change detection across graph iterations.

### Provenance

The `provenance` field is a structured object containing data quality scores (completeness percentage, accuracy confidence, timeliness score) and source attribution. This field is populated at 100% across all 2,944 entities. Provenance operates at the entity level rather than the attribute level, meaning the quality assessment applies to the entity as a whole rather than to individual fields.

### Temporal Object

The `temporal` field is a structured object carrying `effective_date`, `expiration_date`, `last_review_date`, and `next_review_date`. While the field itself is populated at 100%, the interior dates may be null for entities where review cadence has not been established. This structure exists to support governance maturity tracking: an entity with a populated `next_review_date` is under active stewardship, while one with null review dates may represent an unmanaged asset.

---

## Entity Type Catalog

This chapter documents every entity type in the graph, organized by functional layer. Each type section includes a rationale for the layer's existence, a complete attribute schema table showing field names and population percentages, and sample values where they illuminate the schema's intent.

### Operational Infrastructure

*These entity types model the connective tissue of enterprise operations. Roles define who has authority over what. Integrations define how systems exchange data. Controls define what governance mechanisms exist and whether they function. Most due diligence assessments treat these as second-order concerns behind financials and market position. This graph treats them as primary because operational fragility is where post-acquisition surprises live.*

#### `role` (427 entities)

| Field | Populated | Sample Value |
|---|---|---|
| `access_level` | 100.0% | `privileged` |
| `authority_delegated` | 100.0% | `{'financial_approval_limit': {'amount': None, 'currency` |
| `competency_model_reference` | 100.0% | `{'model_name': '', 'applicable_competencies': []}` |
| `department` | 0.2% | `dept-218` |
| `description` | 99.8% | `Top executive responsible for overall corporate strateg` |
| `direct_reports_target` | 100.0% | `{'target_count': None, 'actual_count': None, 'includes_` |
| `fte_count` | 0.2% | `1` |
| `is_active` | 0.2% | `True` |
| `is_privileged` | 100.0% | `True` |
| `name` | 100.0% | `Chief Executive Officer` |
| `physical_requirements` | 100.0% | `{'has_physical_requirements': False, 'requirement_descr` |
| `provenance` | 100.0% | `{'data_quality_score': {'completeness_pct': 45.0, 'accu` |
| `reports_to` | 0.2% | `role-001` |
| `required_education` | 100.0% | `{'minimum_level': '', 'preferred_fields': [], 'equivale` |
| `required_experience` | 100.0% | `{'minimum_years_total': None, 'minimum_years_in_domain'` |
| `responsibilities` | 0.2% | `Oversees product strategy across Private and Public Clo` |
| `role_family` | 100.0% | `{'family_name': '', 'subfamily': ''}` |
| `role_id` | 99.8% | `ROLE-001` |
| `role_level` | 100.0% | `{'level_code': 'M1', 'level_name': 'Management', 'level` |
| `role_mandate_document` | 100.0% | `{'document_reference': '', 'document_date': None, 'last` |
| `role_type` | 100.0% | `Executive` |
| `seniority` | 0.2% | `C-Level` |
| `temporal` | 100.0% | `{'effective_date': None, 'expiration_date': None, 'last` |
| `travel_requirement` | 100.0% | `{'travel_pct': None, 'travel_scope': '', 'travel_freque` |

*Unpopulated fields (0%):* `allocation_model`, `belongs_to_unit`, `compensation_range`, `decision_rights`, `department_id`, `dotted_line_to`, `employment_type_target`, `filled_by_persons`, `fills_capability`, `functional_domain_primary`, `functional_domain_secondary`, `governance_memberships`, `governed_by`, `headcount_authorized`, `headcount_by_location`, `headcount_filled`, `headcount_vacant`, `language_requirements`, `location_flexibility`, `max_headcount`, `metadata`, `origin`, `permissions`, `regulatory_accountability`, `regulatory_designation`, `reports_to_role`, `required_certifications`, `required_clearances`, `required_skills`, `requires_data_access`, `requires_systems_access`, `role_description_extended`, `role_name_former`, `role_name_local`, `role_subtype`, `succession_criticality`, `supports_initiatives`, `taxonomy_lineage`, `vacancy_duration`

#### `integration` (378 entities)

| Field | Populated | Sample Value |
|---|---|---|
| `annual_cost` | 100.0% | `{'amount': None, 'currency': 'USD', 'cost_components': ` |
| `availability_sla` | 100.0% | `{'target_uptime_pct': None, 'actual_uptime_pct': None, ` |
| `crosses_boundary` | 100.0% | `{'crosses_network_boundary': False, 'boundary_type': ''` |
| `data_exchanged` | 100.0% | `{'data_description': '', 'data_classification': '', 'da` |
| `data_quality_score` | 100.0% | `{'completeness_pct': None, 'accuracy_confidence': '', '` |
| `description` | 100.0% | `Customer portal session authentication and token manage` |
| `direction` | 100.0% | `Bidirectional` |
| `error_handling` | 100.0% | `{'retry_mechanism': '', 'dead_letter_queue': False, 'al` |
| `frequency` | 100.0% | `Real-Time` |
| `integration_id` | 100.0% | `INT-0001` |
| `integration_pattern` | 100.0% | `Request-Response` |
| `integration_type` | 100.0% | `API` |
| `last_major_change` | 100.0% | `{'change_date': None, 'change_description': '', 'change` |
| `latency_requirement` | 100.0% | `{'max_acceptable_ms': None, 'actual_p95_ms': None, 'mee` |
| `middleware_platform` | 100.0% | `{'platform_name': '', 'platform_system_id': '', 'manage` |
| `name` | 100.0% | `Identity Auth: Customer Portal (Fabric)` |
| `operational_status` | 100.0% | `Active` |
| `provenance` | 100.0% | `{'data_quality_score': {'completeness_pct': 32.0, 'accu` |
| `security_profile` | 100.0% | `{'authentication': '', 'encryption_in_transit': False, ` |
| `temporal` | 100.0% | `{'effective_date': None, 'expiration_date': None, 'last` |

*Unpopulated fields (0%):* `change_history`, `confidence_level`, `effective_date`, `integration_support_team`, `metadata`, `monitoring_status`, `owner`, `retirement_date`, `source_systems`, `target_systems`, `technical_debt_indicators`, `vendor`

#### `control` (340 entities)

| Field | Populated | Sample Value |
|---|---|---|
| `applicability_dimensions` | 100.0% | `{'people': False, 'process': False, 'technology': False` |
| `automation_details` | 100.0% | `{'tool_name': '', 'system_id': '', 'configuration_refer` |
| `control_domain` | 100.0% | `Access Control` |
| `control_effectiveness` | 100.0% | `{'rating': '', 'methodology': '', 'last_assessed': None` |
| `control_id` | 100.0% | `CTL-001` |
| `control_owner` | 100.0% | `Identity Team` |
| `control_status` | 100.0% | `Implemented` |
| `control_type` | 100.0% | `Preventive` |
| `description` | 100.0% | `MFA enforcement for all privileged, remote, and adminis` |
| `evidence_requirements` | 100.0% | `{'evidence_types': [], 'evidence_location': '', 'retent` |
| `gap_status` | 100.0% | `{'gap_exists': False, 'gap_description': '', 'remediati` |
| `kpi` | 100.0% | `{'metric_name': '', 'target': '', 'current_value': '', ` |
| `name` | 100.0% | `Multi-Factor Authentication` |
| `provenance` | 100.0% | `{'data_quality_score': {'completeness_pct': 35.0, 'accu` |
| `temporal` | 100.0% | `{'effective_date': None, 'expiration_date': None, 'last` |
| `testing_approach` | 100.0% | `{'test_type': '', 'test_frequency': '', 'last_test_date` |

*Unpopulated fields (0%):* `assessment_cadence`, `assessment_history`, `assessment_question`, `audit_findings`, `compensating_controls`, `control_category`, `control_class`, `control_operator`, `control_weighting`, `dependencies`, `exceptions`, `implementing_org_unit`, `implements_policies`, `maps_to_frameworks`, `maps_to_regulations`, `metadata`, `mitigates_risks`, `next_assessment_date`, `privacy_principle_mappings`

### Organizational Structure

*Departments, organizational units, and persons model the human topology of the enterprise. The schema captures reporting lines, headcount, budget ownership, and geographic distribution at a level of specificity that supports analysis of decision authority concentration, single points of organizational failure, and talent dependency risk.*

#### `department` (250 entities)

| Field | Populated | Sample Value |
|---|---|---|
| `budget` | 100.0% | `5980000.0` |
| `code` | 100.0% | `FIN` |
| `description` | 100.0% | `Corporate finance function including financial planning` |
| `headcount` | 100.0% | `46` |
| `name` | 100.0% | `Finance Department` |
| `provenance` | 100.0% | `{'data_quality_score': {'completeness_pct': 55.0, 'accu` |
| `temporal` | 100.0% | `{'effective_date': None, 'expiration_date': None, 'last` |

*Unpopulated fields (0%):* `head_id`, `location_id`, `metadata`, `parent_department_id`

#### `organizational_unit` (109 entities)

| Field | Populated | Sample Value |
|---|---|---|
| `acquisition_source` | 100.0% | `{'source_entity_name': '', 'acquisition_date': None, 'd` |
| `attrition_rate` | 100.0% | `{'annual_total_pct': None, 'voluntary_pct': None, 'invo` |
| `budget_authority` | 100.0% | `{'approval_limit': None, 'currency': 'USD', 'delegation` |
| `center_of_excellence_details` | 100.0% | `{'expertise_domains': [], 'standards_published': [], 'a` |
| `charter_document` | 100.0% | `{'document_reference': '', 'document_date': None, 'last` |
| `control_environment_maturity` | 100.0% | `{'overall_score': None, 'dimensions': [], 'assessed_dat` |
| `cost_structure` | 100.0% | `{'annual_opex': None, 'annual_capex': None, 'total_annu` |
| `delegation_of_authority` | 100.0% | `{'financial_limit': None, 'hiring_authority': False, 'c` |
| `description` | 100.0% | `SEC-reportable segment. Service-centric, capital-light ` |
| `employee_count` | 100.0% | `{'fte': None, 'contractor': None, 'vendor_fte': None, '` |
| `functional_domain_primary` | 100.0% | `Service Delivery` |
| `governing_board` | 100.0% | `{'board_name': '', 'board_type': '', 'member_count': No` |
| `integration_management_office_details` | 100.0% | `{'integration_target': '', 'start_date': None, 'target_` |
| `joint_venture_details` | 100.0% | `{'partner_entities': [], 'ownership_split': {'enterpris` |
| `legal_entity_details` | 100.0% | `{'jurisdiction': '', 'registration_id': '', 'entity_typ` |
| `litigation_exposure` | 100.0% | `{'active_matters_count': None, 'severity_assessment': '` |
| `market_position` | 100.0% | `{'position_description': '', 'competitive_rank': None, ` |
| `name` | 100.0% | `Public Cloud Business Unit` |
| `operating_hours` | 100.0% | `{'timezone_primary': '', 'timezones_all': [], 'operatin` |
| `operating_model` | 100.0% | `Hybrid` |
| `organizational_health_score` | 100.0% | `{'score': None, 'methodology': '', 'dimensions': [], 'a` |
| `parent_reporting_relationship` | 100.0% | `{'reports_to_unit_id': '', 'reports_to_leader': '', 're` |
| `pl_accountability` | 100.0% | `False` |
| `provenance` | 100.0% | `{'data_quality_score': {'completeness_pct': 48.0, 'accu` |
| `revenue_attribution` | 100.0% | `{'annual_revenue': None, 'currency': 'USD', 'fiscal_yea` |
| `shared_service_details` | 100.0% | `{'service_catalog': [], 'chargeback_model': '', 'client` |
| `span_of_control` | 100.0% | `{'average_direct_reports': None, 'min_direct_reports': ` |
| `temporal` | 100.0% | `{'effective_date': None, 'expiration_date': None, 'last` |
| `unit_id` | 100.0% | `OU-001` |
| `unit_type` | 100.0% | `Business Unit` |

*Unpopulated fields (0%):* `audit_findings`, `audit_scope`, `bu_fy2025_bookings_growth_target_pct`, `bu_fy2025_goals`, `bu_fy2025_kpis`, `bu_fy2025_revenue_growth_target_pct`, `bu_fy2025_revenue_target_usd`, `business_continuity_tier`, `business_criticality`, `compliance_officer`, `cost_breakdown`, `cost_center_id`, `criticality_justification`, `culture_integration_status`, `data_protection_officer`, `divestiture_candidacy`, `employee_count_by_location`, `financial_consolidation_entity`, `formation_date`, `functional_domain_secondary`, `geographic_presence`, `geographic_scope`, `governance_cadence`, `hierarchy_memberships`, `intercompany_relationships`, `key_person_dependencies`, `language_primary`, `languages_supported`, `leadership_team`, `management_layers`, `matrix_relationships`, `metadata`, `operational_status`, `operational_status_effective_date`, `operational_status_rationale`, `origin`, `osint_sources`, `profit_center_id`, `regulatory_environment`, `risk_exposure_inherent`, `risk_exposure_residual`, `risk_factors`, `sanctions_screening_status`, `statutory_reporting_obligations`, `strategic_alignment`, `strategic_role`, `strategic_role_rationale`, `tax_jurisdictions`, `taxonomy_lineage`, `transformation_stage`, `unit_description_extended`, `unit_leader`, `unit_leader_title`, `unit_name_former`, `unit_name_local`, `unit_subtype`

#### `person` (100 entities)

| Field | Populated | Sample Value |
|---|---|---|
| `background_check_status` | 100.0% | `{'status': '', 'check_type': [], 'completion_date': Non` |
| `confidence_score` | 13.0% | `0.88` |
| `department` | 13.0% | `Revenue Operations` |
| `description` | 28.0% | `Former Managing Director, Asia Pacific and Japan at Rac` |
| `email` | 31.0% | `ir@rackspace.com` |
| `employee_id` | 98.0% | `EMP-001` |
| `employment_status` | 1.0% | `Active` |
| `experience_profile` | 100.0% | `{'total_years_professional': None, 'years_in_current_ro` |
| `first_name` | 100.0% | `Gajen` |
| `hire_date` | 25.0% | `2025-09-03` |
| `insider_status` | 100.0% | `{'is_insider': False, 'insider_type': '', 'effective_da` |
| `is_active` | 100.0% | `True` |
| `is_privileged` | 1.0% | `True` |
| `job_title` | 1.0% | `Chief Commercial Officer` |
| `last_name` | 100.0% | `Kandiah` |
| `location` | 13.0% | `San Antonio, TX` |
| `name` | 100.0% | `Gajen Kandiah` |
| `person_name` | 100.0% | `{'display_name': '', 'given_name': '', 'family_name': '` |
| `provenance` | 100.0% | `{'data_quality_score': {'completeness_pct': 50.0, 'accu` |
| `reporting_to` | 100.0% | `{'manager_person_id': '', 'manager_role_id': '', 'repor` |
| `seniority_level` | 14.0% | `C-Suite` |
| `source_attribution` | 13.0% | `dept-175 Revenue Operations description, LinkedIn, Rack` |
| `temporal` | 100.0% | `{'effective_date': None, 'expiration_date': None, 'last` |
| `title` | 99.0% | `Chief Executive Officer` |

*Unpopulated fields (0%):* `access_privileges`, `acquisition_origin`, `career_aspirations`, `certifications_held`, `clearance_level`, `clearances_held`, `conflict_of_interest_declarations`, `cost_center`, `current_roles`, `department_id`, `development_plan`, `dotted_line_to`, `education`, `employment_type`, `flight_risk`, `has_system_access`, `holds_roles`, `languages`, `located_at`, `location_primary`, `location_secondary`, `manages_vendor_relationships`, `mandatory_training_compliance`, `member_of_unit`, `mentored_by`, `mentors`, `metadata`, `organizational_unit_primary`, `organizational_unit_secondary`, `original_hire_date`, `participates_in_initiatives`, `performance_rating_current`, `performance_rating_history`, `performance_trajectory`, `person_id`, `phone`, `potential_assessment`, `regulatory_fitness`, `retention_actions`, `skills_gap_assessment`, `skills_inventory`, `subject_to_compliance`, `succession_candidate_for`, `timezone`, `training_completed`, `work_arrangement`

### Data and Information

*Data assets and data domains are the most attribute-dense types in the graph. They exist because the CDAIO assessment premise is that enterprise data is an asset class, and asset classes require inventories with standardized attributes. The containment hierarchy (domains contain assets) models the logical structure a data governance program needs to function.*

#### `data_asset` (164 entities)

| Field | Populated | Sample Value |
|---|---|---|
| `access_control_model` | 100.0% | `RBAC` |
| `access_governance` | 100.0% | `{'access_request_process': 'ServiceNow access request w` |
| `acquisition_cost` | 100.0% | `{'cost': None, 'currency': 'USD', 'renewal_date': None}` |
| `acquisition_source` | 100.0% | `{'source_name': '', 'acquisition_date': None, 'license_` |
| `ai_training_usage` | 100.0% | `{'used_for_ai_training': False, 'model_references': [],` |
| `anonymization_status` | 100.0% | `{'anonymized': False, 'anonymization_method': '', 're_i` |
| `archival_strategy` | 100.0% | `{'hot_tier_retention': '', 'warm_tier_retention': '', '` |
| `asset_subtype` | 100.0% | `Security Event & Log Aggregation Store` |
| `asset_type` | 100.0% | `SIEM Index Cluster` |
| `backup_status` | 100.0% | `{'backup_frequency': 'Daily', 'backup_type': 'Full + In` |
| `breach_notification_obligation` | 100.0% | `{'applicable': True, 'notification_timeframe_hours': 72` |
| `catalog_status` | 100.0% | `{'cataloged': True, 'catalog_platform': 'ServiceNow CMD` |
| `change_reason` | 9.1% | `KG enrichment — Phase 1 data asset completion` |
| `classification` | 100.0% | `confidential` |
| `consent_management` | 100.0% | `{'requires_consent': False, 'consent_type': '', 'consen` |
| `cross_border_transfer_status` | 100.0% | `{'data_crosses_borders': True, 'source_jurisdictions': ` |
| `current_access_grants` | 100.0% | `{'total_users_with_access': None, 'roles_with_access': ` |
| `data_classification` | 100.0% | `confidential` |
| `data_custodian` | 85.4% | `Splunk Platform Administrator` |
| `data_domain_primary` | 100.0% | `Security Operations` |
| `data_format` | 89.0% | `Semi-Structured` |
| `data_masking` | 100.0% | `{'masking_applied': True, 'masking_type': 'Dynamic Mask` |
| `data_owner` | 85.4% | `CISO / VP of Security Operations` |
| `data_steward` | 85.4% | `Director of Security Engineering` |
| `data_subject_rights_applicable` | 100.0% | `True` |
| `data_type` | 100.0% | `semi-structured` |
| `description` | 100.0% | `Primary security information and event management data ` |
| `dsar_process_reference` | 4.3% | `Privacy team DSAR process — billing data subject to cus` |
| `effective_date` | 9.1% | `2024-01-01` |
| `encryption_at_rest` | 100.0% | `{'encrypted': True, 'algorithm': 'AES-256', 'key_manage` |
| `format` | 100.0% | `Splunk Index` |
| `functional_domain_primary` | 100.0% | `Security Operations` |
| `functional_domain_secondary` | 61.6% | `['IT Operations', 'Compliance', 'DevOps']` |
| `golden_record_status` | 100.0% | `{'is_golden_source': False, 'golden_source_reference': ` |
| `is_encrypted` | 100.0% | `True` |
| `last_review_date` | 9.1% | `2025-10-01` |
| `lineage_completeness` | 85.4% | `Substantially Documented` |
| `lineage_downstream` | 78.0% | `[{'asset_id': '', 'asset_name': 'Microsoft Sentinel SIE` |
| `lineage_upstream` | 81.1% | `[{'asset_id': '', 'asset_name': 'All Infrastructure & A` |
| `name` | 100.0% | `Splunk Enterprise Security Index Cluster` |
| `next_review_date` | 9.1% | `2026-10-01` |
| `origin` | 89.0% | `Organic` |
| `partitioning_strategy` | 100.0% | `{'partition_key': '', 'partition_type': ''}` |
| `pii_categories` | 70.7% | `['IP Addresses', 'Usernames', 'Authentication Tokens', ` |
| `privacy_impact_assessment` | 100.0% | `{'pia_required': True, 'pia_completed': True, 'pia_date` |
| `processing_cost` | 100.0% | `{'annual_cost': None, 'currency': 'USD', 'cost_driver':` |
| `profiling_status` | 100.0% | `{'last_profiled_date': None, 'profiling_tool': '', 'pro` |
| `provenance` | 100.0% | `{'data_quality_score': {'completeness_pct': 62.0, 'accu` |
| `quality_monitoring` | 100.0% | `{'automated_monitoring': False, 'monitoring_tool': '', ` |
| `quality_score_composite` | 100.0% | `{'score': None, 'scale': '1-5', 'assessed_date': None}` |
| `record_count_detail` | 100.0% | `{'current_count': None, 'growth_rate_monthly_pct': None` |
| `regulations` | 24.4% | `['SOC 2 Type II', 'PCI DSS', 'GDPR', 'FedRAMP']` |
| `regulatory_applicability` | 93.9% | `[{'regulation_id': '', 'regulation_name': 'SOC 2 Type I` |
| `replication` | 100.0% | `{'is_replicated': True, 'replication_type': 'Synchronou` |
| `retention_compliance` | 100.0% | `{'policy_reference': 'Rackspace Log Retention Policy + ` |
| `retention_days` | 84.8% | `365` |
| `storage_cost` | 100.0% | `{'annual_cost': None, 'currency': 'USD', 'cost_driver':` |
| `storage_format` | 100.0% | `{'format_type': 'Splunk TSIDX + Journal (Proprietary In` |
| `storage_technology` | 100.0% | `{'system_id': '', 'system_name': 'Splunk Enterprise Sec` |
| `system_id` | 12.2% | `sys-141` |
| `temporal` | 100.0% | `{'effective_date': '2020-01-01', 'expiration_date': Non` |
| `third_party_sharing` | 0.6% | `[{'third_party_name': 'Foundation Model Providers (Open` |
| `total_data_cost` | 100.0% | `{'annual_total': None, 'currency': 'USD'}` |
| `value_assessment` | 100.0% | `{'estimated_value': None, 'valuation_method': '', 'conf` |
| `velocity` | 100.0% | `{'creation_rate': '', 'update_rate': '', 'deletion_rate` |
| `volume` | 100.0% | `{'current_size': 110.0, 'size_unit': 'TB', 'growth_rate` |

*Unpopulated fields (0%):* `asset_description_extended`, `asset_id`, `asset_name_common`, `attestation_status`, `audit_findings`, `cost_optimization_opportunities`, `data_cleansing_history`, `data_domain_secondary`, `fitness_for_purpose`, `indexing_strategy`, `metadata`, `owner_id`, `quality_dimensions`, `quality_issues_open`, `quality_rules`, `quality_trend`, `record_count`

#### `data_domain` (88 entities)

| Field | Populated | Sample Value |
|---|---|---|
| `business_glossary_reference` | 100.0% | `{'glossary_platform': '', 'glossary_url': '', 'term_cou` |
| `data_classification` | 100.0% | `Confidential` |
| `description` | 100.0% | `Master data for 81,000+ customer accounts across 120 co` |
| `domain_id` | 100.0% | `DD-001` |
| `domain_owner` | 100.0% | `Chief Revenue Officer` |
| `domain_type` | 100.0% | `Business` |
| `maturity_level` | 100.0% | `Managed` |
| `monetization_potential` | 100.0% | `{'potential_type': '', 'estimated_annual_value': None, ` |
| `name` | 100.0% | `Customer Account Data` |
| `provenance` | 100.0% | `{'data_quality_score': {'completeness_pct': 45.0, 'accu` |
| `quality_targets` | 100.0% | `{'completeness_target_pct': None, 'accuracy_target_pct'` |
| `retention_policy` | 100.0% | `{'minimum_retention': 'Duration of customer relationshi` |
| `sensitivity_flags` | 100.0% | `{'pii_flag': True, 'phi_flag': False, 'pci_flag': False` |
| `strategic_value` | 100.0% | `Critical` |
| `temporal` | 100.0% | `{'effective_date': None, 'expiration_date': None, 'last` |

*Unpopulated fields (0%):* `data_residency_requirements`, `domain_scope`, `domain_steward`, `governing_policies`, `maturity_dimensions`, `metadata`, `regulatory_sensitivity`, `sub_domains`

### Systems and Technology

*Systems, networks, sites, and locations model the physical and logical infrastructure that hosts, processes, and transmits enterprise data. These types support analysis of technology concentration risk, hosting dependency, and geographic distribution of processing capability.*

#### `system` (164 entities)

| Field | Populated | Sample Value |
|---|---|---|
| `access_control_model` | 100.0% | `RBAC` |
| `access_review_status` | 100.0% | `{'last_review_date': None, 'next_review_date': None, 'r` |
| `acquisition_source` | 100.0% | `{'source_entity_name': '', 'acquisition_date': None, 'i` |
| `api_surface` | 100.0% | `{'api_count': None, 'api_types': ['REST'], 'api_documen` |
| `authentication_mechanisms` | 99.4% | `[{'mechanism': 'SSO', 'protocol': 'SAML', 'mfa_supporte` |
| `availability` | 0.6% | `high` |
| `availability_design` | 100.0% | `{'architecture_pattern': 'Active-Active', 'redundancy_l` |
| `availability_sla` | 100.0% | `{'target_uptime_pct': None, 'measurement_window': '', '` |
| `backup_status` | 100.0% | `{'backup_frequency': 'Daily', 'backup_type': 'Full', 'l` |
| `business_fitness` | 100.0% | `{'composite_score': None, 'dimensions': [], 'assessed_d` |
| `business_impact_if_unavailable` | 100.0% | `{'impact_description': 'Complete loss of customer self-` |
| `capacity_current` | 100.0% | `{'cpu_utilization_pct': None, 'memory_utilization_pct':` |
| `capacity_headroom` | 100.0% | `{'months_to_capacity': None, 'scaling_plan': '', 'scali` |
| `capex_remaining` | 100.0% | `{'remaining_book_value': None, 'currency': 'USD', 'amor` |
| `change_velocity` | 100.0% | `{'releases_per_month': None, 'deployment_frequency': ''` |
| `cloud_provider` | 0.6% | `AWS` |
| `confidentiality` | 0.6% | `high` |
| `containerized` | 100.0% | `{'is_containerized': False, 'container_platform': '', '` |
| `contract_details` | 100.0% | `{'vendor': '', 'contract_id': '', 'contract_start': Non` |
| `cost_per_transaction` | 100.0% | `{'amount': None, 'currency': 'USD', 'basis': ''}` |
| `cost_per_user` | 100.0% | `{'amount': None, 'currency': 'USD', 'basis': ''}` |
| `criticality` | 100.0% | `critical` |
| `current_users` | 100.0% | `{'total_licensed_users': None, 'total_provisioned_users` |
| `current_version_info` | 100.0% | `{'version': '', 'release_date': None, 'patch_level': ''` |
| `cyber_exposure` | 100.0% | `{'attack_surface_type': 'Internet Facing', 'threat_prof` |
| `deployment` | 2.4% | `on-premises Kubernetes` |
| `deployment_model` | 100.0% | `on_premises` |
| `description` | 100.0% | `Rackspace customer management portal built on Fabric au` |
| `encryption_profile` | 100.0% | `{'data_at_rest': 'AES-256', 'data_in_transit': 'TLS 1.2` |
| `environment` | 100.0% | `production` |
| `hostname` | 97.6% | `portal.rackspace.com` |
| `incident_history` | 100.0% | `{'p1_count_12m': None, 'p2_count_12m': None, 'mttr_hour` |
| `infrastructure_as_code` | 100.0% | `{'iac_enabled': False, 'iac_tool': '', 'coverage_pct': ` |
| `integration_points` | 0.6% | `['prometheus', 'splunk', 'datadog', 'servicenow', 'slac` |
| `integrity` | 0.6% | `critical` |
| `ip_address` | 97.6% | `N/A` |
| `is_internet_facing` | 100.0% | `True` |
| `license_details` | 100.0% | `{'license_type': '', 'license_count': None, 'licenses_i` |
| `lifecycle_stage` | 97.6% | `production` |
| `maintenance_windows` | 100.0% | `{'schedule': '', 'duration_hours': None, 'impact_scope'` |
| `name` | 100.0% | `Rackspace Customer Portal (Fabric)` |
| `observability_stack` | 100.0% | `{'logging_tool': 'Splunk Enterprise Security', 'logging` |
| `open_source_components` | 100.0% | `{'component_count': None, 'license_types': [], 'sbom_av` |
| `os` | 97.6% | `Linux` |
| `osint_confidence` | 2.4% | `0.92` |
| `patch_compliance` | 100.0% | `{'patch_policy': '', 'compliance_pct': None, 'days_to_p` |
| `penetration_test_status` | 100.0% | `{'last_test_date': None, 'test_type': '', 'findings_cri` |
| `performance_sla` | 100.0% | `{'response_time_target_ms': None, 'throughput_target': ` |
| `provenance` | 100.0% | `{'data_quality_score': {'completeness_pct': 40.0, 'accu` |
| `replacement_candidate` | 100.0% | `{'has_replacement_planned': False, 'replacement_system_` |
| `scalability_profile` | 100.0% | `{'horizontal_scaling': True, 'vertical_scaling': True, ` |
| `security_architecture_review` | 100.0% | `{'last_review_date': None, 'review_outcome': '', 'open_` |
| `support_model` | 100.0% | `{'support_provider': 'Internal', 'support_tier': 'Tier ` |
| `system_cost_benchmark` | 100.0% | `{'benchmark_source': '', 'benchmark_value': None, 'perc` |
| `system_id` | 2.4% | `sys-vault-001` |
| `system_type` | 97.6% | `application` |
| `technical_fitness` | 100.0% | `{'composite_score': None, 'dimensions': [], 'assessed_d` |
| `temporal` | 100.0% | `{'effective_date': None, 'expiration_date': None, 'last` |
| `tier` | 2.4% | `T2` |
| `total_cost_of_ownership` | 100.0% | `{'annual_tco': None, 'currency': 'USD', 'fiscal_year': ` |
| `vendor` | 2.4% | `HashiCorp (IBM)` |
| `vulnerability_profile` | 100.0% | `{'last_scan_date': None, 'critical_count': None, 'high_` |

*Unpopulated fields (0%):* `architecture_type`, `audit_findings`, `business_criticality`, `cloud_native_score`, `compliance_certifications`, `cost_breakdown`, `cost_optimization_opportunities`, `cost_trend`, `criticality_justification`, `data_classification_handled`, `data_residency_constraints`, `data_steward`, `data_stores`, `department_id`, `development_team`, `functional_domain_primary`, `functional_domain_secondary`, `governance_body`, `hosting_model`, `innovation_potential`, `metadata`, `monitoring_coverage`, `network_id`, `network_zone`, `operational_status`, `operational_status_rationale`, `origin`, `owner_id`, `ports`, `procurement_type`, `programming_languages`, `regulatory_applicability`, `risk_exposure_inherent`, `risk_exposure_residual`, `security_owner`, `strategic_alignment`, `strategic_classification`, `strategic_classification_rationale`, `support_team`, `system_category`, `system_description_extended`, `system_name_common`, `system_name_former`, `system_owner`, `system_subcategory`, `system_tier`, `taxonomy_lineage`, `technical_debt_indicators`, `technical_owner`, `technologies`, `technology_stack`, `user_base_by_geography`, `vendor_account_manager`, `vendor_id`, `version_currency`

#### `network` (94 entities)

| Field | Populated | Sample Value |
|---|---|---|
| `cidr` | 100.0% | `Various (4 IPv4 prefixes, 11,776 IPs originated)` |
| `description` | 100.0% | `[CONFIDENCE: T1] RADB as-name RACKSPACE. Global backbon` |
| `is_monitored` | 100.0% | `True` |
| `name` | 100.0% | `AS12200 Rackspace Global Backbone` |
| `provenance` | 100.0% | `{'data_quality_score': {'completeness_pct': 45, 'accura` |
| `temporal` | 100.0% | `{'effective_date': None, 'expiration_date': None, 'last` |
| `zone` | 100.0% | `backbone` |

*Unpopulated fields (0%):* `dns_servers`, `gateway`, `location_id`, `metadata`, `vlan_id`

#### `site` (58 entities)

| Field | Populated | Sample Value |
|---|---|---|
| `address` | 100.0% | `{'street_line_1': '1 Fanatical Place', 'street_line_2':` |
| `annual_operating_cost` | 100.0% | `{'amount': None, 'currency': 'USD', 'fiscal_year': ''}` |
| `coordinates` | 100.0% | `{'latitude': None, 'longitude': None}` |
| `current_occupancy` | 100.0% | `{'headcount': None, 'as_of_date': None}` |
| `description` | 100.0% | `Corporate HQ. Executive leadership, corporate functions` |
| `name` | 100.0% | `Global Headquarters - San Antonio` |
| `ownership_type` | 100.0% | `Leased` |
| `provenance` | 100.0% | `{'data_quality_score': {'completeness_pct': 60.0, 'accu` |
| `site_code` | 13.8% | `SAT-HQ` |
| `site_id` | 100.0% | `SITE-001` |
| `site_status` | 100.0% | `Active` |
| `site_type` | 100.0% | `Headquarters` |
| `strategic_designation` | 100.0% | `Strategic` |
| `temporal` | 100.0% | `{'effective_date': None, 'expiration_date': None, 'last` |

*Unpopulated fields (0%):* `accessibility_compliance`, `acquisition_source`, `available_capacity`, `backup_site`, `book_value`, `building_count`, `business_continuity_tier`, `capacity_forecast`, `capital_investment_planned`, `climate_risk_assessment`, `connected_to_sites`, `cooling_capacity`, `cost_benchmark`, `cost_breakdown`, `cost_per_unit`, `crime_environment`, `deferred_maintenance_backlog`, `design_capacity`, `disaster_recovery_role`, `employs_persons`, `environmental_certifications`, `environmental_controls`, `evacuation_plan`, `expansion_potential`, `facility_condition_index`, `fire_suppression`, `floors`, `geopolitical_risk`, `governed_by`, `hosts_systems`, `houses_org_units`, `insurance_coverage`, `last_incident`, `lease_details`, `located_in_geography`, `managed_by_vendors`, `metadata`, `natural_hazard_profile`, `network_connectivity`, `occupancy_by_unit`, `origin`, `parking_capacity`, `physical_security_systems`, `physical_security_tier`, `power_supply`, `proximity_risks`, `replacement_value`, `risk_exposure_inherent`, `risk_exposure_residual`, `seasonal_variation`, `serves_customers_from`, `shift_model`, `single_points_of_failure`, `site_description`, `site_name_former`, `site_name_local`, `site_status_rationale`, `site_subtype`, `special_infrastructure`, `stores_data`, `subject_to_initiatives`, `subject_to_jurisdictions`, `total_area`, `usable_area`, `utilization_rate`, `waste_management`, `water_supply`, `year_built`, `year_last_renovated`

#### `location` (46 entities)

| Field | Populated | Sample Value |
|---|---|---|
| `address` | 54.3% | `19122 US Highway 281 N, Suite 128` |
| `city` | 100.0% | `San Antonio` |
| `country` | 100.0% | `US` |
| `description` | 100.0% | `Corporate office at RidgeWood Plaza II, ~80,000 sq ft, ` |
| `has_physical_security` | 100.0% | `True` |
| `is_primary` | 100.0% | `True` |
| `location_type` | 100.0% | `office` |
| `name` | 100.0% | `Global Headquarters - RidgeWood Plaza II` |
| `provenance` | 100.0% | `{'confidence_level': 'High', 'assessed_by': 'AI Enrichm` |
| `security_level` | 100.0% | `standard` |
| `state` | 80.4% | `TX` |
| `temporal` | 100.0% | `{'effective_date': None, 'expiration_date': None, 'last` |

*Unpopulated fields (0%):* `capacity`, `metadata`, `zip_code`

### Market and External

*No enterprise operates in isolation. Customers, vendors, regulations, jurisdictions, geographies, contracts, and market segments model the external forces that constrain and enable the enterprise. Regulatory and contractual constraints on data movement are as material to a CDAIO assessment as internal architecture.*

#### `customer` (85 entities)

| Field | Populated | Sample Value |
|---|---|---|
| `account_tier` | 100.0% | `Strategic` |
| `customer_id` | 100.0% | `CUST-001` |
| `customer_type` | 100.0% | `Enterprise` |
| `description` | 100.0% | `Leading pediatric hospital in Seattle, Washington. Oper` |
| `name` | 100.0% | `Seattle Children's Hospital` |
| `provenance` | 100.0% | `{'data_quality_score': {'completeness_pct': None, 'accu` |
| `relationship_status` | 100.0% | `Active` |
| `temporal` | 100.0% | `{'effective_date': None, 'expiration_date': None, 'last` |

*Unpopulated fields (0%):* `account_roles`, `account_team`, `audit_findings`, `belongs_to_segment`, `buys_products`, `communication_preferences`, `contract_value`, `credit_profile`, `customer_compliance_certifications`, `customer_locations`, `customer_name_common`, `customer_name_former`, `customer_risk_profile`, `customer_size`, `customer_subtype`, `customizations`, `data_privacy_obligations`, `data_shared_with`, `deployment_model`, `engagement_model`, `expansion_potential`, `export_control_status`, `functional_domain_primary`, `headquarters_location`, `health_score`, `industry_classification`, `integration_points`, `kyc_status`, `located_in`, `managed_by_org_unit`, `managed_through_vendors`, `metadata`, `origin`, `parent_customer`, `payment_terms`, `primary_contact`, `products_active`, `products_historical`, `profitability`, `regulatory_applicability`, `relationship_start_date`, `relationship_tenure_years`, `revenue_by_product`, `revenue_concentration_risk`, `revenue_current`, `revenue_lifetime`, `sanctions_screening`, `satisfaction_current`, `service_agreements`, `subsidiaries`, `uses_systems`, `wallet_share`

#### `vendor` (55 entities)

| Field | Populated | Sample Value |
|---|---|---|
| `description` | 100.0% | `Hyperscale public cloud platform provider; Rackspace Pu` |
| `has_data_access` | 100.0% | `True` |
| `name` | 100.0% | `Amazon Web Services, Inc.` |
| `primary_contact` | 78.2% | `https://aws.amazon.com/contact-us/` |
| `provenance` | 100.0% | `{'data_quality_score': {'completeness_pct': None, 'accu` |
| `risk_tier` | 100.0% | `critical` |
| `temporal` | 100.0% | `{'effective_date': None, 'expiration_date': None, 'last` |
| `vendor_id` | 100.0% | `VND-001` |
| `vendor_type` | 100.0% | `Hyperscale Cloud Platform` |

*Unpopulated fields (0%):* `audit_findings`, `business_continuity`, `co_investment`, `compliance_certifications`, `contract_expiry`, `contract_value`, `cost_benchmark`, `cost_trend`, `cybersecurity_assessment`, `data_classification_access`, `data_processing`, `delivery_performance`, `dependency_on_vendor`, `diversity_classification`, `engagement_model`, `escalation_history`, `exclusivity`, `executive_sponsor`, `financial_stability`, `force_majeure_exposure`, `geographic_concentration`, `governance_cadence`, `headquarters_location`, `holds_contracts`, `incident_history`, `industry_classification`, `innovation_contribution`, `insurance_coverage`, `joint_governance`, `managed_by_org_unit`, `metadata`, `operates_from_locations`, `origin`, `ownership_structure`, `parent_company`, `partnership_structure`, `payment_terms`, `performance_dimensions`, `performance_scorecard`, `provides_data`, `provides_systems`, `quality_metrics`, `regulatory_applicability`, `relationship_start_date`, `relationship_status`, `relationship_tenure_years`, `sanctions_screening`, `savings_realized`, `serves_customers_through`, `shared_ip`, `sla_compliance`, `sla_uptime`, `spend_by_business_unit`, `spend_by_category`, `spend_concentration_risk`, `strategic_importance`, `subsidiaries`, `substitutability`, `supplies_products`, `supply_chain_role`, `total_annual_spend`, `vendor_category`, `vendor_compliance_certifications`, `vendor_dependencies`, `vendor_locations`, `vendor_management_roles`, `vendor_manager`, `vendor_name_common`, `vendor_name_former`, `vendor_risk_profile`, `vendor_size`, `vendor_subcategory`

#### `regulation` (70 entities)

| Field | Populated | Sample Value |
|---|---|---|
| `applicability_criteria` | 100.0% | `{'criteria_description': '', 'triggers': []}` |
| `applicability_status` | 100.0% | `Applicable` |
| `compliance_status` | 100.0% | `{'status': '', 'last_assessed': None, 'assessed_by': ''` |
| `description` | 100.0% | `EU-wide data protection and privacy regulation governin` |
| `effective_date` | 100.0% | `2018-05-25` |
| `issuing_body` | 100.0% | `{'body_name': '', 'body_type': '', 'jurisdiction': ''}` |
| `monitoring_approach` | 100.0% | `{'method': '', 'frequency': '', 'automated': False, 're` |
| `name` | 100.0% | `General Data Protection Regulation` |
| `penalties` | 100.0% | `{'penalty_type': '', 'maximum_penalty': '', 'penalty_ba` |
| `provenance` | 100.0% | `{'data_quality_score': {'completeness_pct': 55.0, 'accu` |
| `regulation_category` | 100.0% | `Data Privacy` |
| `regulation_id` | 100.0% | `REG-001` |
| `regulation_type` | 100.0% | `Statutory` |
| `short_name` | 100.0% | `GDPR` |
| `temporal` | 100.0% | `{'effective_date': None, 'expiration_date': None, 'last` |

*Unpopulated fields (0%):* `compliance_gaps`, `jurisdictions`, `key_requirements`, `last_amended_date`, `metadata`, `regulatory_change_pipeline`

#### `jurisdiction` (61 entities)

| Field | Populated | Sample Value |
|---|---|---|
| `description` | 100.0% | `US federal regulatory jurisdiction. SEC reporting (Exch` |
| `jurisdiction_code` | 100.0% | `US` |
| `jurisdiction_id` | 100.0% | `JUR-001` |
| `jurisdiction_type` | 100.0% | `Federal` |
| `name` | 100.0% | `United States Federal` |
| `provenance` | 100.0% | `{'confidence_level': 'High', 'assessed_by': 'Thomas Jon` |
| `temporal` | 100.0% | `{'effective_date': None, 'expiration_date': None, 'last` |

*Unpopulated fields (0%):* `applicable_to_entities`, `child_jurisdictions`, `cross_border_transfer_rules`, `data_residency_requirements`, `governing_body`, `governs_capabilities`, `jurisdiction_name_local`, `labor_law_summary`, `links_to_compliance`, `metadata`, `parent_jurisdiction`, `privacy_regulation`, `regulatory_framework_summary`, `sanctions_status`, `sites_in_jurisdiction`, `tax_regime`

#### `geography` (57 entities)

| Field | Populated | Sample Value |
|---|---|---|
| `description` | 100.0% | `Primary operating region covering United States, Canada` |
| `geography_id` | 100.0% | `GEO-001` |
| `geography_type` | 100.0% | `Region` |
| `name` | 100.0% | `North America` |
| `operational_status` | 100.0% | `Active` |
| `provenance` | 100.0% | `{'confidence_level': 'High', 'assessed_by': 'Thomas Jon` |
| `temporal` | 100.0% | `{'effective_date': None, 'expiration_date': None, 'last` |

*Unpopulated fields (0%):* `child_geographies`, `countries_included`, `geography_description`, `geography_name_short`, `market_characteristics`, `metadata`, `overlaps_with_jurisdictions`, `parent_geography`, `primary_languages`, `regional_leadership`, `sites_in_geography`, `strategic_importance`, `time_zones`

#### `contract` (37 entities)

| Field | Populated | Sample Value |
|---|---|---|
| `contract_id` | 100.0% | `230302` |
| `contract_status` | 100.0% | `Active` |
| `contract_type` | 100.0% | `Cooperative Purchasing Agreement` |
| `currency` | 100.0% | `USD` |
| `description` | 100.0% | `Cooperative purchasing agreement managed by The Interlo` |
| `end_date` | 86.5% | `2026-05-31` |
| `name` | 100.0% | `TIPS 230302 — Data Center Hosting, Sales and Service` |
| `provenance` | 100.0% | `{'data_quality_score': {'completeness_pct': None, 'accu` |
| `start_date` | 100.0% | `2023-05-31` |
| `temporal` | 100.0% | `{'effective_date': None, 'expiration_date': None, 'last` |
| `total_contract_value` | 100.0% | `0.0` |

*Unpopulated fields (0%):* `amendments`, `annual_value`, `associated_contracts`, `auto_renewal`, `contract_owner`, `contracting_org_unit`, `covers_data`, `covers_products`, `covers_systems`, `current_term`, `data_handling_provisions`, `early_termination_penalty`, `governing_law`, `initial_term`, `insurance_requirements`, `ip_provisions`, `legal_owner`, `liability_caps`, `metadata`, `notice_period_days`, `opt_out_deadline`, `payment_schedule`, `payment_terms`, `procurement_owner`, `renewal_cap_pct`, `renewal_term`, `sla_summary`, `termination_for_convenience`, `termination_notice_days`, `termination_provisions`, `vendor_id`, `with_vendor`

#### `market_segment` (26 entities)

| Field | Populated | Sample Value |
|---|---|---|
| `competitive_intensity` | 100.0% | `High` |
| `description` | 100.0% | `Large enterprise customers with 1000+ employees. Racksp` |
| `name` | 100.0% | `Enterprise` |
| `provenance` | 100.0% | `{'data_quality_score': {'completeness_pct': None, 'accu` |
| `segment_id` | 100.0% | `SEG-001` |
| `segment_type` | 100.0% | `Company Size` |
| `strategic_priority` | 100.0% | `Primary` |
| `temporal` | 100.0% | `{'effective_date': None, 'expiration_date': None, 'last` |

*Unpopulated fields (0%):* `child_segments`, `contains_customers`, `entry_barriers`, `growth_rate`, `managed_by_org_unit`, `managing_org_unit`, `market_sizing`, `metadata`, `parent_segment`, `regulatory_environment`, `segment_criteria`, `segment_financial_summary`, `segment_level`, `segment_owner`, `served_by_products`, `win_rate`

### Strategic and Risk

*Initiatives, risks, business capabilities, and incidents represent assessed conclusions rather than observed infrastructure. Their lower entity counts are intentional. Each connects to operational entities through typed relationships that preserve causal chains.*

#### `initiative` (24 entities)

| Field | Populated | Sample Value |
|---|---|---|
| `annual_investment_usd` | 45.8% | `150000000` |
| `annual_savings_target_usd` | 4.2% | `100000000` |
| `current_status` | 100.0% | `In Progress` |
| `description` | 100.0% | `The foundational transformation of Rackspace's core bus` |
| `executive_sponsor` | 100.0% | `Amar Maletira (CEO)` |
| `fiscal_year` | 100.0% | `FY2025` |
| `functional_domain_primary` | 100.0% | `Technology and Operations` |
| `initiative_category` | 100.0% | `Strategic` |
| `initiative_dependencies` | 50.0% | `['INIT-003', 'INIT-008', 'INIT-011']` |
| `initiative_id` | 100.0% | `INIT-001` |
| `initiative_lead` | 100.0% | `Dhrupad Trivedi (COO)` |
| `initiative_tier` | 100.0% | `Portfolio` |
| `initiative_type` | 100.0% | `Digital Transformation` |
| `name` | 100.0% | `Multi-Cloud Managed Services Transformation` |
| `okrs_fy2025` | 100.0% | `['Grow multi-cloud bookings to 70%+ of total new ARR', ` |
| `phase` | 100.0% | `Execution` |
| `planned_end_date` | 100.0% | `2026-12-31` |
| `planned_start_date` | 100.0% | `2021-01-01` |
| `provenance` | 100.0% | `{'data_quality_score': {'completeness_pct': None, 'accu` |
| `quarterly_milestones_fy2025` | 100.0% | `{'Q1': 'APAC multi-cloud delivery model operational; Fa` |
| `rag_status` | 100.0% | `Amber` |
| `strategic_priority` | 100.0% | `Must Do` |
| `temporal` | 100.0% | `{'effective_date': None, 'expiration_date': None, 'last` |

*Unpopulated fields (0%):* `active_issues`, `active_risks`, `actual_end_date`, `actual_start_date`, `budget_breakdown`, `budget_variance`, `business_case_summary`, `child_initiatives`, `constraints`, `cost_benefit_analysis`, `critical_path_items`, `decision_log`, `dependencies_on_other_initiatives`, `expected_outcomes`, `forecast_at_completion`, `functional_domain_secondary`, `funding_source`, `governance_cadence`, `impacts_capabilities`, `impacts_customers`, `impacts_data`, `impacts_locations`, `impacts_org_units`, `impacts_products`, `impacts_roles`, `impacts_systems`, `impacts_vendors`, `initiative_description_extended`, `initiative_risk_profile`, `investment_thesis`, `key_milestones`, `lessons_learned`, `metadata`, `methodology`, `origin`, `owning_org_unit`, `parent_initiative`, `planned_duration_months`, `program_manager`, `related_initiatives`, `resource_allocation`, `resource_requirements`, `run_rate_impact`, `schedule_variance`, `spend_to_date`, `status_rationale`, `steering_committee`, `strategic_alignment`, `strategic_objectives`, `success_criteria`, `taxonomy_lineage`, `technology_requirements`, `total_budget`, `training_requirements`, `value_realized`, `vendor_engagement`

#### `risk` (22 entities)

| Field | Populated | Sample Value |
|---|---|---|
| `acceptance_record` | 100.0% | `{'accepted_by': '', 'acceptance_date': None, 'acceptanc` |
| `assessment_cadence` | 100.0% | `Quarterly` |
| `assessment_methodology` | 100.0% | `Scenario Analysis` |
| `board_reportable` | 100.0% | `True` |
| `control_effectiveness_on_risk` | 100.0% | `{'risk_reduction_pct': None, 'control_count': None, 'we` |
| `description` | 100.0% | `Risk of ransomware attack against Rackspace-managed inf` |
| `emerging_risk_flag` | 100.0% | `False` |
| `inherent_financial_impact` | 100.0% | `{'estimated_loss_low': None, 'estimated_loss_high': Non` |
| `inherent_impact` | 100.0% | `Catastrophic` |
| `inherent_impact_dimensions` | 100.0% | `{'financial': '', 'operational': '', 'reputational': ''` |
| `inherent_likelihood` | 100.0% | `Likely` |
| `inherent_risk_level` | 100.0% | `Critical` |
| `materiality_assessment` | 100.0% | `{'pct_of_pretax_income': None, 'pct_of_total_assets': N` |
| `name` | 100.0% | `Ransomware Attack on Hosted Exchange Infrastructure` |
| `nist_csf_function` | 100.0% | `Respond` |
| `provenance` | 100.0% | `{'data_quality_score': {'completeness_pct': 55.0, 'accu` |
| `residual_impact` | 100.0% | `Major` |
| `residual_likelihood` | 100.0% | `Possible` |
| `residual_risk_level` | 100.0% | `High` |
| `risk_appetite` | 100.0% | `Averse` |
| `risk_category` | 100.0% | `Cybersecurity` |
| `risk_id` | 100.0% | `RSK-00001` |
| `risk_owner` | 100.0% | `CISO` |
| `risk_source` | 100.0% | `External` |
| `risk_status` | 100.0% | `Mitigated` |
| `risk_subcategory` | 100.0% | `Ransomware / Destructive Malware` |
| `risk_tolerance` | 100.0% | `{'tolerance_threshold': '', 'escalation_trigger': '', '` |
| `risk_treatment` | 100.0% | `Mitigate` |
| `risk_trend` | 100.0% | `Stable` |
| `risk_velocity` | 100.0% | `Instant` |
| `temporal` | 100.0% | `{'effective_date': None, 'expiration_date': None, 'last` |
| `transfer_record` | 100.0% | `{'transfer_mechanism': '', 'transfer_counterparty': '',` |
| `treatment_plan` | 100.0% | `{'plan_description': '', 'target_residual_risk_level': ` |

*Unpopulated fields (0%):* `assessment_history`, `key_risk_indicators`, `last_assessed`, `loss_event_history`, `metadata`, `next_assessment`, `risk_group`, `risk_interconnections`, `risk_scenarios`, `risk_taxonomy_references`

#### `business_capability` (64 entities)

| Field | Populated | Sample Value |
|---|---|---|
| `business_criticality` | 100.0% | `Business Critical` |
| `capability_id` | 100.0% | `BC-001` |
| `capability_type` | 100.0% | `Business` |
| `description` | 100.0% | `Enterprise-level strategic planning, long-term vision d` |
| `lifecycle_state` | 100.0% | `Active` |
| `name` | 100.0% | `Corporate Strategy & Planning` |
| `provenance` | 100.0% | `{'data_quality_score': {'completeness_pct': 50.0, 'accu` |
| `temporal` | 100.0% | `{'effective_date': None, 'expiration_date': None, 'last` |
| `tier` | 100.0% | `Strategic` |

*Unpopulated fields (0%):* `acquisition_source`, `audit_findings`, `business_impact_if_degraded`, `business_model_relevance`, `capability_description_extended`, `capability_name_local`, `capability_owner`, `capacity_utilization`, `child_capabilities`, `control_coverage`, `control_references`, `cost_benchmark`, `cost_to_operate`, `criticality_justification`, `cyber_exposure`, `delivered_through_products`, `depends_on_capabilities`, `depends_on_vendors`, `differentiation_evidence`, `differentiation_level`, `enables_capabilities`, `executive_sponsor`, `functional_domain`, `functional_domain_secondary`, `funding_amount`, `funding_model`, `governance_body`, `governance_cadence`, `governed_by`, `headcount_allocation`, `interfaces_with`, `kpi_current_values`, `kpi_definitions`, `lifecycle_next_state`, `lifecycle_next_state_target_date`, `lifecycle_state_rationale`, `lifecycle_transition_date`, `located_at`, `maturity_by_business_unit`, `maturity_by_region`, `maturity_composite_score`, `maturity_dimensions`, `maturity_model_reference`, `maturity_target`, `maturity_trajectory`, `metadata`, `origin`, `owned_by_organization`, `parent_capability`, `performance_status`, `raci_matrix`, `realized_by_initiatives`, `regulatory_applicability`, `resilience_tier`, `revenue_attribution`, `risk_exposure_inherent`, `risk_exposure_residual`, `risk_factors`, `rpo`, `rto`, `serves_customers`, `shared_service_model`, `single_points_of_failure`, `sourcing_suitability`, `staffed_by`, `strategic_alignment`, `strategic_risk_if_lost`, `supported_by_data`, `supported_by_systems`, `taxonomy_lineage`, `tier_justification`, `value_stream_alignment`

#### `incident` (7 entities)

| Field | Populated | Sample Value |
|---|---|---|
| `description` | 100.0% | `Complete outage of Rackspace Hosted Microsoft Exchange ` |
| `detected_at` | 100.0% | `2023-11-21` |
| `detection_method` | 100.0% | `user_report` |
| `impact_description` | 100.0% | `Complete outage of Rackspace Hosted Microsoft Exchange ` |
| `incident_type` | 100.0% | `malware` |
| `lessons_learned` | 100.0% | `Patch velocity for critical Exchange vulnerabilities mu` |
| `name` | 100.0% | `PLAY Ransomware Attack on Hosted Exchange (November 202` |
| `occurred_at` | 100.0% | `2023-11-21` |
| `provenance` | 100.0% | `{'confidence_level': 'High', 'assessed_by': 'AI Enrichm` |
| `resolved_at` | 100.0% | `2024-03-31` |
| `root_cause` | 100.0% | `PLAY ransomware group (Russia-linked threat actor) expl` |
| `severity` | 100.0% | `critical` |
| `status` | 100.0% | `closed` |
| `temporal` | 100.0% | `{'effective_date': None, 'expiration_date': None, 'last` |

*Unpopulated fields (0%):* `affected_data_asset_ids`, `affected_system_ids`, `metadata`, `responder_ids`, `threat_actor_id`

### Products and Services

*Product portfolios and products model the commercial output of the enterprise, connecting what the organization sells to the systems, data, and people that deliver it.*

#### `product_portfolio` (71 entities)

| Field | Populated | Sample Value |
|---|---|---|
| `description` | 100.0% | `SEC-reported revenue segment encompassing managed priva` |
| `lifecycle_stage` | 100.0% | `Maturity` |
| `name` | 100.0% | `Private Cloud` |
| `portfolio_id` | 100.0% | `PF-001` |
| `portfolio_level` | 100.0% | `L1` |
| `portfolio_type` | 100.0% | `Service` |
| `provenance` | 100.0% | `{'data_quality_score': {'completeness_pct': None, 'accu` |
| `strategic_role` | 100.0% | `Core` |
| `temporal` | 100.0% | `{'effective_date': None, 'expiration_date': None, 'last` |

*Unpopulated fields (0%):* `child_portfolios`, `contains_products`, `financial_summary`, `investment_priority`, `managed_by_org_unit`, `managing_org_unit`, `market_position`, `metadata`, `parent_portfolio`, `portfolio_owner`, `strategic_alignment`

#### `product` (33 entities)

| Field | Populated | Sample Value |
|---|---|---|
| `description` | 100.0% | `Proprietary multi-tenant software platform providing un` |
| `lifecycle_stage` | 100.0% | `Maturity` |
| `name` | 100.0% | `Rackspace Fabric` |
| `offering_subtype` | 100.0% | `Platform` |
| `offering_type` | 100.0% | `SaaS` |
| `product_id` | 100.0% | `PRD-001` |
| `provenance` | 100.0% | `{'data_quality_score': {'completeness_pct': None, 'accu` |
| `temporal` | 100.0% | `{'effective_date': None, 'expiration_date': None, 'last` |

*Unpopulated fields (0%):* `acquisition_source`, `belongs_to_portfolio`, `certifications_required`, `churn_rate`, `competitive_landscape`, `cost_to_deliver`, `customer_complaints`, `customer_count`, `customer_lifetime_value`, `customer_satisfaction`, `delivered_from_locations`, `delivery_channels`, `delivery_model`, `depends_on_vendors`, `differentiation_factors`, `enabled_by_capabilities`, `enabled_by_systems`, `environmental_compliance`, `export_control_classification`, `fulfillment_model`, `functional_domain_primary`, `functional_domain_secondary`, `generation`, `launch_date`, `liability_exposure`, `lifecycle_stage_rationale`, `managed_by_org_unit`, `manufacturing_locations`, `margin_profile`, `market_position`, `metadata`, `origin`, `planned_retirement_date`, `pricing_model`, `pricing_range`, `product_category`, `product_description_internal`, `product_name_former`, `product_name_internal`, `product_name_local`, `product_reviews`, `product_roles`, `quality_metrics`, `recall_history`, `regulatory_applicability`, `regulatory_approval_status`, `regulatory_classification`, `related_products`, `revenue_by_geography`, `revenue_by_segment`, `revenue_current`, `revenue_trend`, `safety_certifications`, `scalability_constraints`, `serves_customers`, `service_level_performance`, `service_level_targets`, `sku_count`, `strategic_alignment`, `supply_chain_complexity`, `taxonomy_lineage`, `uses_data`, `version_current`, `version_history`

### Governance

*Policies model the formal governance instruments that define expected behavior. The gap between policy count (114) and enforcement relationship count (386) indicates that enforcement mechanisms are modeled at a higher granularity than the policies they implement.*

#### `policy` (114 entities)

| Field | Populated | Sample Value |
|---|---|---|
| `applies_to` | 100.0% | `{'org_units': [], 'roles': [], 'systems': [], 'data_dom` |
| `communication_plan` | 100.0% | `{'last_communicated': None, 'communication_channel': ''` |
| `compliance_measurement` | 100.0% | `{'metric': '', 'target': '', 'current_value': '', 'meas` |
| `current_version` | 100.0% | `{'version': '', 'effective_date': None, 'change_summary` |
| `description` | 100.0% | `Top-level ISMS policy establishing Rackspace Technology` |
| `enforcement_mechanism` | 100.0% | `{'mechanism_type': '', 'description': '', 'automated': ` |
| `framework` | 100.0% | `ISO 27001` |
| `is_enforced` | 100.0% | `True` |
| `name` | 100.0% | `Information Security Management Policy` |
| `policy_id` | 100.0% | `POL-001` |
| `policy_type` | 100.0% | `Governance` |
| `provenance` | 100.0% | `{'data_quality_score': {'completeness_pct': 40.0, 'accu` |
| `review_frequency_days` | 100.0% | `365` |
| `severity` | 100.0% | `critical` |
| `temporal` | 100.0% | `{'effective_date': None, 'expiration_date': None, 'last` |
| `training_requirement` | 100.0% | `{'required': False, 'training_program': '', 'completion` |

*Unpopulated fields (0%):* `applicable_systems`, `approval_date`, `approving_authority`, `control_id`, `driven_by_regulations`, `driven_by_risks`, `effective_date`, `exceptions`, `last_reviewed_date`, `metadata`, `next_review_date`, `owner_id`, `policy_author`, `policy_owner`, `policy_requirements`, `policy_scope`, `policy_status`, `related_policies`, `review_cadence`, `version_history`

---

## Relationship Architecture

The graph encodes 7,466 relationships across 42 types, forming 114 distinct edge patterns (unique combinations of source entity type, relationship type, and target entity type). This chapter documents every relationship type, organized by functional category.

### Base Relationship Schema

Every relationship carries a common set of attributes:

| Attribute | Description | Population |
|---|---|---|
| `id` | Unique relationship identifier | 100% |
| `relationship_type` | One of 42 defined types | 100% |
| `source_id` | ID of the source entity | 100% |
| `target_id` | ID of the target entity | 100% |
| `weight` | Edge weight (0.0 to 1.0) | ~100% |
| `confidence` | Confidence score (0.0 to 1.0) | ~100% |
| `description` | Optional prose description | Varies |
| `properties` | Optional structured metadata | Varies |

The `weight` field encodes the strength or significance of the relationship. The `confidence` field encodes the assessed reliability of the relationship's existence. Both default to 1.0 when not explicitly set, meaning absence of a confidence score does not indicate low confidence but rather that confidence has not been independently assessed.

### Spatial and Jurisdictional

*Geographic and jurisdictional placement are modeled as first-class relationships rather than entity attributes. This design decision enables queries about data residency compliance, regulatory exposure by jurisdiction, and operational concentration without requiring secondary attribute lookups. The high edge count (1,943 combined) reflects the enterprise's global operational footprint.*

#### `located_in` (1260 edges)

| Source Type | Target Type | Count |
|---|---|---|
| role | department | 416 |
| department | organizational_unit | 250 |
| data_asset | system | 157 |
| network | network | 102 |
| customer | geography | 81 |
| site | geography | 58 |
| geography | geography | 53 |
| location | geography | 46 |
| network | geography | 37 |
| contract | geography | 26 |

*Metadata coverage: description: 73.8%*

#### `located_at` (683 edges)

| Source Type | Target Type | Count |
|---|---|---|
| system | site | 484 |
| site | location | 104 |
| network | site | 52 |
| organizational_unit | site | 41 |
| data_asset | site | 2 |

*Metadata coverage: description: 0.3%, properties: 8.5%*

### Dependency and Constraint

*These relationships form the analytical backbone of the graph. When a system depends_on another system that is hosted_on infrastructure subject_to a regulation, the graph can traverse the full obligation chain in a single query. This is where blast radius analysis and change impact assessment operate.*

#### `subject_to` (1120 edges)

| Source Type | Target Type | Count |
|---|---|---|
| data_domain | regulation | 207 |
| data_domain | policy | 183 |
| data_asset | data_domain | 176 |
| data_domain | jurisdiction | 137 |
| site | jurisdiction | 80 |
| regulation | jurisdiction | 72 |
| location | jurisdiction | 68 |
| customer | regulation | 39 |
| jurisdiction | jurisdiction | 37 |
| product | regulation | 18 |

*Metadata coverage: description: 74.6%*

#### `depends_on` (790 edges)

| Source Type | Target Type | Count |
|---|---|---|
| integration | system | 463 |
| system | system | 213 |
| integration | network | 64 |
| business_capability | system | 50 |

*Metadata coverage: description: 10.3%*

#### `hosted_on` (490 edges)

| Source Type | Target Type | Count |
|---|---|---|
| system | site | 489 |
| system | system | 1 |

*Metadata coverage: properties: 99.8%*

#### `applies_to` (543 edges)

| Source Type | Target Type | Count |
|---|---|---|
| control | system | 543 |

*Metadata coverage: properties: 1.8%*

### Governance and Control

*The distinction between enforces (386 edges) and governed_by (12 edges) is structurally significant. The graph contains extensive modeling of which controls enforce which policies, but sparse modeling of formal data governance accountability. This gap reflects the enterprise's actual governance maturity, not a modeling omission.*

#### `enforces` (386 edges)

| Source Type | Target Type | Count |
|---|---|---|
| control | policy | 386 |

#### `managed_by` (385 edges)

| Source Type | Target Type | Count |
|---|---|---|
| system | department | 162 |
| system | person | 160 |
| data_domain | department | 63 |

*Metadata coverage: description: 16.4%*

#### `implements` (178 edges)

| Source Type | Target Type | Count |
|---|---|---|
| policy | regulation | 155 |
| product | product_portfolio | 9 |
| product | system | 6 |
| product_portfolio | system | 5 |
| product_portfolio | product_portfolio | 3 |

*Metadata coverage: description: 12.9%*

#### `governs` (32 edges)

| Source Type | Target Type | Count |
|---|---|---|
| contract | customer | 20 |
| contract | system | 5 |
| contract | data_asset | 4 |
| contract | vendor | 3 |

*Metadata coverage: description: 100.0%*

#### `governed_by` (12 edges)

| Source Type | Target Type | Count |
|---|---|---|
| organizational_unit | policy | 10 |
| policy | regulation | 2 |

### Data Flow

*These relationships model how data moves through the enterprise. Combined with integration entities (which carry their own rich attribute schemas), these edges create a queryable data lineage layer that supports both regulatory compliance analysis and operational dependency mapping.*

#### `stores` (165 edges)

| Source Type | Target Type | Count |
|---|---|---|
| system | data_asset | 165 |

*Metadata coverage: properties: 99.4%*

#### `connects_to` (140 edges)

| Source Type | Target Type | Count |
|---|---|---|
| integration | system | 88 |
| integration | data_asset | 52 |

#### `integrates_with` (101 edges)

| Source Type | Target Type | Count |
|---|---|---|
| system | system | 101 |

*Metadata coverage: properties: 99.0%*

#### `processes` (55 edges)

| Source Type | Target Type | Count |
|---|---|---|
| vendor | data_asset | 55 |

*Metadata coverage: description: 69.1%*

### Organizational

*These connect people to their functions, departments to their parent units, and data domains to their constituent assets. The low count on reports_to (9) compared to has_role (92) reflects a deliberate design choice: the graph prioritizes functional authority mapping over hierarchical org-chart modeling.*

#### `has_role` (92 edges)

| Source Type | Target Type | Count |
|---|---|---|
| person | role | 92 |

*Metadata coverage: description: 83.7%, properties: 16.3%*

#### `works_in` (48 edges)

| Source Type | Target Type | Count |
|---|---|---|
| person | department | 48 |

*Metadata coverage: description: 43.8%, properties: 56.2%*

#### `reports_to` (9 edges)

| Source Type | Target Type | Count |
|---|---|---|
| person | person | 9 |

*Metadata coverage: properties: 100.0%*

#### `staffed_by` (3 edges)

| Source Type | Target Type | Count |
|---|---|---|
| organizational_unit | person | 3 |

*Metadata coverage: properties: 100.0%*

#### `belongs_to` (71 edges)

| Source Type | Target Type | Count |
|---|---|---|
| product | product_portfolio | 71 |

*Metadata coverage: properties: 100.0%*

#### `holds` (37 edges)

| Source Type | Target Type | Count |
|---|---|---|
| customer | contract | 37 |

*Metadata coverage: properties: 100.0%*

#### `contains` (75 edges)

| Source Type | Target Type | Count |
|---|---|---|
| data_domain | data_asset | 51 |
| market_segment | customer | 21 |
| product_portfolio | product | 3 |

*Metadata coverage: description: 96.0%*

### Commercial

*Market-facing relationships connect the enterprise to its customers, vendors, and service delivery mechanisms. These support analysis of revenue concentration, vendor dependency, and contract-based constraints on operational flexibility.*

#### `serves` (137 edges)

| Source Type | Target Type | Count |
|---|---|---|
| system | customer | 40 |
| product | market_segment | 39 |
| product_portfolio | customer | 32 |
| organizational_unit | market_segment | 26 |

*Metadata coverage: description: 52.6%, properties: 41.6%*

#### `provides_service` (71 edges)

| Source Type | Target Type | Count |
|---|---|---|
| vendor | department | 50 |
| system | organizational_unit | 21 |

*Metadata coverage: properties: 100.0%*

#### `buys` (22 edges)

| Source Type | Target Type | Count |
|---|---|---|
| customer | product | 22 |

#### `contracts_with` (7 edges)

| Source Type | Target Type | Count |
|---|---|---|
| contract | vendor | 7 |

*Metadata coverage: properties: 100.0%*

#### `supplies` (6 edges)

| Source Type | Target Type | Count |
|---|---|---|
| vendor | product_portfolio | 5 |
| vendor | product | 1 |

*Metadata coverage: description: 100.0%*

#### `supplied_by` (28 edges)

| Source Type | Target Type | Count |
|---|---|---|
| system | vendor | 28 |

*Metadata coverage: properties: 100.0%*

#### `delivers` (33 edges)

| Source Type | Target Type | Count |
|---|---|---|
| system | product | 33 |

*Metadata coverage: properties: 100.0%*

### Risk and Impact

*Risk relationships connect assessed risk entities to the operational entities they affect. The causal chain is preserved: a risk creates_risk for a system, which impacts a business capability, which affects a product portfolio. This enables multi-hop impact analysis.*

#### `mitigates` (29 edges)

| Source Type | Target Type | Count |
|---|---|---|
| control | risk | 29 |

*Metadata coverage: properties: 96.6%*

#### `creates_risk` (4 edges)

| Source Type | Target Type | Count |
|---|---|---|
| vendor | risk | 4 |

*Metadata coverage: properties: 100.0%*

#### `impacts` (14 edges)

| Source Type | Target Type | Count |
|---|---|---|
| initiative | business_capability | 10 |
| initiative | risk | 4 |

*Metadata coverage: properties: 85.7%*

#### `impacted_by` (17 edges)

| Source Type | Target Type | Count |
|---|---|---|
| business_capability | risk | 6 |
| system | risk | 6 |
| system | incident | 3 |
| product | risk | 2 |

*Metadata coverage: properties: 100.0%*

#### `affects` (21 edges)

| Source Type | Target Type | Count |
|---|---|---|
| incident | system | 19 |
| incident | data_asset | 2 |

#### `addresses` (15 edges)

| Source Type | Target Type | Count |
|---|---|---|
| initiative | risk | 15 |

*Metadata coverage: properties: 73.3%*

### Strategic

*Strategic relationships connect initiatives to the capabilities they enable, the budgets that fund them, and the systems they support. These provide the forward-looking dimension of the graph.*

#### `supports` (209 edges)

| Source Type | Target Type | Count |
|---|---|---|
| product_portfolio | business_capability | 59 |
| business_capability | department | 52 |
| system | business_capability | 36 |
| business_capability | organizational_unit | 24 |
| vendor | product_portfolio | 18 |
| policy | policy | 12 |
| vendor | system | 5 |
| product_portfolio | organizational_unit | 3 |

*Metadata coverage: description: 77.0%, properties: 17.2%*

#### `enables` (33 edges)

| Source Type | Target Type | Count |
|---|---|---|
| product | business_capability | 33 |

*Metadata coverage: properties: 100.0%*

#### `drives` (28 edges)

| Source Type | Target Type | Count |
|---|---|---|
| initiative | business_capability | 20 |
| initiative | product | 6 |
| initiative | control | 2 |

*Metadata coverage: properties: 100.0%*

#### `funded_by` (12 edges)

| Source Type | Target Type | Count |
|---|---|---|
| initiative | organizational_unit | 12 |

*Metadata coverage: properties: 100.0%*

#### `subject_of` (30 edges)

| Source Type | Target Type | Count |
|---|---|---|
| customer | data_asset | 30 |

*Metadata coverage: description: 100.0%*

#### `hosts` (26 edges)

| Source Type | Target Type | Count |
|---|---|---|
| site | system | 26 |

#### `regulates` (49 edges)

| Source Type | Target Type | Count |
|---|---|---|
| jurisdiction | geography | 49 |

---

## Edge Pattern Analysis

The 114 distinct edge patterns represent the full vocabulary of structural relationships the graph can express.

### Relationship Volume Distribution

The top 10 relationship types by edge count:

| Relationship Type | Count | % of Total | Most Common Pattern |
|---|---|---|---|
| located_in | 1260 | 16.9% | role -> department |
| subject_to | 1120 | 15.0% | data_domain -> regulation |
| depends_on | 790 | 10.6% | integration -> system |
| located_at | 683 | 9.1% | system -> site |
| applies_to | 543 | 7.3% | control -> system |
| hosted_on | 490 | 6.6% | system -> site |
| enforces | 386 | 5.2% | control -> policy |
| managed_by | 385 | 5.2% | system -> department |
| supports | 209 | 2.8% | product_portfolio -> business_capability |
| implements | 178 | 2.4% | policy -> regulation |

### Entity Type Connectivity

Which entity types participate as sources and targets across the most relationship types, indicating structural centrality:

| Entity Type | Outbound Rel Types | Inbound Rel Types | Total Edges |
|---|---|---|---|
| system | 12 | 11 | 3624 |
| product | 6 | 5 | 243 |
| data_asset | 3 | 7 | 694 |
| organizational_unit | 4 | 4 | 390 |
| customer | 5 | 3 | 322 |
| product_portfolio | 4 | 4 | 211 |
| vendor | 5 | 3 | 176 |
| policy | 3 | 4 | 760 |
| business_capability | 3 | 4 | 290 |
| department | 1 | 5 | 1041 |
| site | 4 | 2 | 1336 |
| person | 3 | 3 | 321 |
| risk | 0 | 5 | 66 |
| network | 2 | 2 | 357 |
| contract | 3 | 1 | 102 |
| data_domain | 3 | 1 | 817 |
| regulation | 1 | 3 | 493 |
| control | 3 | 1 | 960 |
| initiative | 4 | 0 | 69 |
| geography | 1 | 2 | 403 |
| location | 2 | 1 | 218 |
| jurisdiction | 2 | 1 | 480 |
| role | 1 | 1 | 508 |
| integration | 2 | 0 | 667 |
| market_segment | 1 | 1 | 86 |
| incident | 1 | 1 | 24 |

---

## Due Diligence Analysis Layer

The 401 structured JSON analysis files organized across nine due diligence stages represent the analytical layer built on top of the graph. The graph provides structural truth; the analysis layer provides assessed truth.

| Stage | Name | Scope |
|---|---|---|
| Stage 0 | Diligence Governance | Defines the constitutional rules and constraints governing the entire assessment methodology. |
| Stage 1 | Corporate Legal Structural | Corporate legal existence, ownership and control structures, structural debt from historical M&A, change-of-control constraints, and jurisdictional licensing requirements. |
| Stage 2 | Business Model Economics | Revenue engines, cost structure and margin physics, value flow friction, customer segmentation and dependency, partner and channel value capture, and business model coherence contradictions. |
| Stage 3 | Market Competitive Force | Market structure and power migration, competitive threat vectors, customer buying and switching inertia, pricing power and discounting signals, partner and platform dependency, and external shock sensitivity. |
| Stage 4 | Operating Model Execution | Decision rights and authority, operating cadence and throughput, cross-functional bottlenecks, incentive and accountability structures, and talent deployment constraints. |
| Stage 5 | Financial Capital Stress | Revenue quality and stability, margin physics, liquidity and cash runway, debt covenants and control transfer triggers, capital allocation capacity, and financial coherence contradictions. |
| Stage 6 | Technology Platform | Compute and datacenter control, cloud and hyperscaler dependency, platform criticality and fragility, vendor lock-in and licensing, technical debt constraints, and technology estate coherence. |
| Stage 7 | Data Information Epistemic | Data domain authoritativeness, data lineage and meaning drift, data quality and error tolerance, stewardship accountability, access and privilege asymmetry, data flow latency, and epistemic coherence. |
| Stage 8 | Risk Security Regulatory | Cybersecurity control failure surfaces, privacy and data use limits, regulatory enforcement exposure, data residency and sovereignty, and governance power and veto rights. |
| Stage 9 | Resilience ESG Continuity | Business continuity and failure sequencing, workforce and talent fragility, vendor ecosystem shock propagation, insurance and risk transfer, and ESG materiality constraints. |

### Analysis File Structure

Each due diligence stage follows a consistent internal structure. Substages contain hypothesis files, disconfirming evidence searches, uncertainty registers, and domain-specific analysis artifacts. Each stage concludes with a validation folder containing contradiction analysis, exit criteria tests, gate decisions, and hypothesis discipline audits.

This structure encodes the analytical methodology itself, not just findings. The hypothesis-disconfirmation-validation cycle ensures that conclusions are stress-tested against contradicting evidence before they advance to the next stage.

---

## Known Structural Gaps

Three structural gaps in the current graph constrain specific categories of analysis.

### Data Quality Targets

The graph contains zero data quality target entities. It can describe the current state of data quality through composite scores on data asset entities, but it cannot model the gap between current state and target state. For a CDAIO assessment, that gap analysis is where actionable recommendations originate. Adding a `quality_target` entity type with relationships to `data_asset` and `data_domain` entities would close this gap.

### Governance Relationship Density

The governance relationship layer is thin relative to the operational layer. Twelve `governed_by` edges across 252 data entities (88 domains plus 164 data assets) represents a 4.8% governance linkage rate. This limits the graph's ability to model accountability chains for data stewardship. The gap reflects the state of the enterprise being modeled rather than a schema limitation: the schema supports `governed_by` relationships, but the enterprise has not established them.

### Temporal Window Coverage

The `valid_from` and `valid_until` base attributes are unpopulated across all 2,944 entities, meaning the graph represents a current-state snapshot rather than a time-series. Historical state analysis (such as tracking governance maturity improvement over quarters) would require populating these fields across future graph iterations.

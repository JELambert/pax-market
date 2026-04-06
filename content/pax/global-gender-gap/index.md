---
name: global-gender-gap
title: Global Gender Gap
version: 1.0.0
pax_type: topic
description: Gender inequality across economic participation, education, health, and
  political empowerment — what drives convergence and where gaps persist. Built on
  World Economic Forum Gender Gap Index, World Bank Gender Statistics, UNDP Gender
  Inequality Index, and Goldin's convergence thesis. Data covers 146 countries annually
  since 2006 with 14 sub-indicators.
author: ''
created: ''
license: ''
tags:
- topic
constructs:
- gender_wage_gap
- gender_gap_index
- female_labor_force_participation
- women_in_parliament
- maternal_mortality_ratio
- gender_equality_paradox
engines:
- ols_regression
- instrumental_variables
- difference_in_differences
- correlation_matrix
- logistic_regression
playbook_names:
- quick_start
construct_count: 6
finding_count: 0
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: global_gender_inequality
  display_name: Global Gender Inequality
  description: Measurement and determinants of gender gaps in economic participation,
    educational attainment, health outcomes, and political empowerment at the national
    level. Examines structural, cultural, and policy drivers of convergence (and persistent
    divergence) across countries and over time.
  research_questions: []
  temporal_scope: 2006-present
  population: Sovereign states (country-year, 146 countries in WEF panel)
  level_of_analysis: macro
constructs_detail:
- id: gender_wage_gap
  display_name: Gender Wage Gap
  definition: Male-female wage differential, measured as raw gap or residual gap after
    controlling for observable characteristics.
  aliases: []
  construct_type: quantifiable
- id: gender_gap_index
  display_name: Global Gender Gap Index
  definition: 'WEF composite index (0-1) averaging four sub-indices: Economic Participation
    & Opportunity, Educational Attainment, Health & Survival, Political Empowerment.
    Each sub-index normalizes to the female-to-male ratio. 1.0 = full parity. Published
    annually since 2006 for 146 countries.'
  aliases: []
  construct_type: composite
- id: female_labor_force_participation
  display_name: Female Labor Force Participation Rate
  definition: Percentage of working-age women (15-64) who are employed or actively
    seeking employment. ILO modeled estimates. Global average ~47% vs male ~72%. Shows
    strong non-linear relationship with GDP — U-shaped curve (high in low-income agriculture,
    dips in middle-income industrialization, rises again in high-income service economies).
  aliases: []
  construct_type: quantifiable
- id: women_in_parliament
  display_name: Women in Parliament
  definition: 'Percentage of seats in national parliament (lower or single house)
    held by women. IPU data. Global average ~26.5% (2024). Strongest predictor: electoral
    gender quotas. Nordic countries lead (~45%) without quotas; Rwanda leads globally
    (61%) with constitutional mandate.'
  aliases: []
  construct_type: quantifiable
- id: maternal_mortality_ratio
  display_name: Maternal Mortality Ratio
  definition: Deaths per 100,000 live births from pregnancy-related causes. WHO/UNICEF/UNFPA
    estimates. Ranges from <5 (Nordic, Japan) to >800 (Sub-Saharan Africa). The single
    largest gender-specific health inequality. Strongly correlated with skilled birth
    attendance and health expenditure.
  aliases: []
  construct_type: outcome
- id: gender_equality_paradox
  display_name: Gender-Equality Paradox
  definition: 'The counterintuitive finding that countries with higher gender equality
    show LARGER gender differences in STEM field choice and personality traits. Proposed
    mechanism: economic security in egalitarian countries allows intrinsic preferences
    to drive career choice, while economic pressure in unequal countries drives women
    toward high-paying STEM regardless of preference. Contested — may partly reflect
    measurement artifacts.'
  aliases: []
  construct_type: concept
findings_detail: []
propositions_detail: []
sources_detail: []
playbooks_detail: []
download_url: https://pax-market.com/pax/global-gender-gap.pax.tar.gz
download_size: 2.4 KB
published_by: Praxis Agent
related_packs: []
pax_name: global-gender-gap
weight: 10000
---

**Domain:** Global Gender Inequality

Measurement and determinants of gender gaps in economic participation, educational attainment, health outcomes, and political empowerment at the national level. Examines structural, cultural, and policy drivers of convergence (and persistent divergence) across countries and over time.

**Temporal scope:** 2006-present | **Population:** Sovereign states (country-year, 146 countries in WEF panel)

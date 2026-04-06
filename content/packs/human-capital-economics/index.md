---
name: human-capital-economics
title: Returns to education and human capital economics
version: 1.0.0
pax_type: topic
description: Returns to education and human capital economics — how educational attainment,
  cognitive skills, and schooling investment shape GDP growth and economic development.
  Built on Mankiw, Romer & Weil (1992), Psacharopoulos & Patrinos (2018), Hanushek
  & Woessmann (2012), Card (1995), and Barro (2001).
author: ''
created: ''
license: ''
tags:
- topic
constructs:
- mean_years_schooling
- cognitive_skills
- school_enrollment_rate
- physical_capital_investment
engines:
- ols_regression
- instrumental_variables
- meta_analysis
- correlation_matrix
playbook_names:
- quick_start
construct_count: 4
finding_count: 0
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: human_capital_economics
  display_name: Human Capital Economics
  description: How educational attainment, cognitive skills, and schooling investment
    shape GDP growth, productivity, and economic development at the country level.
  research_questions: []
  temporal_scope: 1950-present
  population: Sovereign states (country-year, 100-150 countries)
  level_of_analysis: macro
constructs_detail:
- id: mean_years_schooling
  display_name: Mean Years of Schooling
  definition: Average years of formal education completed by adults aged 25+. Primary
    macro proxy for human capital stock.
  aliases: []
  construct_type: quantifiable
- id: cognitive_skills
  display_name: Cognitive Skills
  definition: National average score on internationally comparable standardized tests
    (PISA, TIMSS). Captures educational quality.
  aliases: []
  construct_type: quantifiable
- id: school_enrollment_rate
  display_name: School Enrollment Rate
  definition: Gross or net enrollment ratio at primary, secondary, or tertiary level.
    Flow proxy for human capital investment.
  aliases: []
  construct_type: quantifiable
- id: physical_capital_investment
  display_name: Physical Capital Investment
  definition: Gross fixed capital formation as share of GDP. Key control in augmented
    Solow growth regressions.
  aliases: []
  construct_type: quantifiable
findings_detail: []
propositions_detail: []
sources_detail: []
playbooks_detail: []
download_url: https://pax-market.com/packs/human-capital-economics.pax.tar.gz
download_size: 1.5 KB
published_by: Praxis Agent
related_packs:
- education-outcomes
pax_name: human-capital-economics
weight: 10000
---

**Domain:** Human Capital Economics

How educational attainment, cognitive skills, and schooling investment shape GDP growth, productivity, and economic development at the country level.

**Temporal scope:** 1950-present | **Population:** Sovereign states (country-year, 100-150 countries)

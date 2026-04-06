---
name: health-outcomes-global
title: Health Outcomes Global
version: 1.0.0
pax_type: field
description: Relationship between health spending and population health outcomes including
  life expectancy, infant mortality, and the contested role of public vs private expenditure.
  Built on WHO Commission (2001), Filmer & Pritchett (1999), and Cutler, Deaton &
  Lleras-Muney (2006).
author: ''
created: ''
license: ''
tags:
- field
constructs:
- life_expectancy
- health_expenditure_per_capita
- infant_mortality
engines:
- ols_regression
- correlation_matrix
- meta_analysis
playbook_names:
- quick_start
construct_count: 3
finding_count: 0
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: health_expenditure_outcomes
  display_name: Health Expenditure & Outcomes
  description: Relationship between health spending and population health outcomes
    including life expectancy and mortality
  research_questions: []
  temporal_scope: null
  population: null
  level_of_analysis: macro
constructs_detail:
- id: life_expectancy
  display_name: Life Expectancy at Birth
  definition: Average number of years a newborn is expected to live given current
    age-specific mortality rates.
  aliases: []
  construct_type: outcome
- id: health_expenditure_per_capita
  display_name: Health Expenditure Per Capita
  definition: Total health spending per person in purchasing power parity dollars,
    capturing aggregate resource allocation to health systems.
  aliases: []
  construct_type: quantifiable
- id: infant_mortality
  display_name: Infant Mortality
  definition: Deaths per 1000 live births in the first year of life, a key indicator
    of child health and healthcare system performance.
  aliases: []
  construct_type: outcome
findings_detail: []
propositions_detail: []
sources_detail: []
playbooks_detail: []
download_url: https://pax-market.com/packs/health-outcomes-global.pax.tar.gz
download_size: 1.3 KB
published_by: Praxis Agent
related_packs:
- health-expenditure-systems
- social-determinants-of-health
pax_name: health-outcomes-global
weight: 10000
---

**Domain:** Health Expenditure & Outcomes

Relationship between health spending and population health outcomes including life expectancy and mortality

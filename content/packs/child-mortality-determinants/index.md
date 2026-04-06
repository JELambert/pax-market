---
name: child-mortality-determinants
title: Child Mortality Determinants
version: 1.0.0
pax_type: topic
description: Structural and health system factors driving under-5 mortality across
  low and middle income countries, examining the roles of maternal education, immunization,
  skilled birth attendance, and economic development.
author: null
created: '2026-04-05'
license: null
tags:
- topic
- child-mortality
constructs:
- maternal_education_years
- immunization_coverage
- skilled_birth_attendance
- gdp_per_capita_child
- clean_water_access_child
- child_mortality_under5
engines:
- ols_regression
- logistic_regression
- correlation_matrix
playbook_names:
- quick_start
construct_count: 6
finding_count: 0
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: child_mortality
  display_name: Child Mortality Determinants
  description: Structural and health system factors driving under-5 mortality across
    low and middle income countries
  research_questions: []
  temporal_scope: 1990-present
  population: Countries worldwide
  level_of_analysis: macro
constructs_detail:
- id: maternal_education_years
  display_name: Maternal Education (Years)
  definition: Average years of formal schooling completed by women of reproductive
    age in a given country, a key social determinant of child health outcomes
  aliases: []
  construct_type: quantifiable
- id: immunization_coverage
  display_name: Immunization Coverage
  definition: Percentage of children aged 12-23 months who have received all basic
    recommended vaccinations including DPT3, measles, and polio
  aliases: []
  construct_type: quantifiable
- id: skilled_birth_attendance
  display_name: Skilled Birth Attendance
  definition: Percentage of births attended by skilled health personnel such as doctors,
    nurses, or midwives trained in providing life-saving obstetric care
  aliases: []
  construct_type: quantifiable
- id: gdp_per_capita_child
  display_name: GDP per Capita
  definition: Gross domestic product divided by midyear population in constant international
    dollars, measuring average economic output per person as a proxy for development
    level
  aliases: []
  construct_type: quantifiable
- id: clean_water_access_child
  display_name: Clean Water Access
  definition: Percentage of the population using at least basic drinking water services
    from an improved source within 30 minutes round trip collection time
  aliases: []
  construct_type: quantifiable
- id: child_mortality_under5
  display_name: Under-5 Mortality Rate
  definition: The probability of a child dying before reaching age 5, expressed per
    1,000 live births, a key indicator of child health and development progress
  aliases: []
  construct_type: outcome
findings_detail: []
propositions_detail: []
sources_detail:
- id: cutler_2006
  title: The Determinants of Mortality
  authors: David Cutler, Angus Deaton, Adriana Lleras-Muney
  year: 2006
  doi: 10.1257/jep.20.3.97
  source_type: journal_article
- id: gakidou_2010
  title: 'Increased educational attainment and its effect on child mortality in 175
    countries between 1970 and 2009: a systematic analysis'
  authors: Emmanuela Gakidou, Krycia Cowling, Rafael Lozano, Christopher JL Murray
  year: 2010
  doi: 10.1016/S0140-6736(10)61257-3
  source_type: journal_article
- id: who_unicef_2023
  title: 'Levels and Trends in Child Mortality: Report 2023'
  authors: UN Inter-agency Group for Child Mortality Estimation
  year: 2023
  doi: null
  source_type: report
- id: wagstaff_2004
  title: 'Child health on a dollar a day: some tentative cross-country comparisons'
  authors: Adam Wagstaff, Mariam Claeson
  year: 2004
  doi: 10.1016/j.socscimed.2003.12.003
  source_type: journal_article
playbooks_detail: []
download_url: https://pax-market.com/packs/child-mortality-determinants.pax.tar.gz
download_size: 2.3 KB
published_by: Praxis Agent
related_packs: []
pax_name: child-mortality-determinants
weight: 7974
---

**Domain:** Child Mortality Determinants

Structural and health system factors driving under-5 mortality across low and middle income countries

**Temporal scope:** 1990-present | **Population:** Countries worldwide

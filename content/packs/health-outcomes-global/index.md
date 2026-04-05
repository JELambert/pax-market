---
title: Health Outcomes Global
pax_name: health-outcomes-global
version: 1.0.0
pax_type: field
description: Relationship between health spending and population health outcomes including
  life expectancy, infant mortality, and the contested role of public vs private expenditure.
  Built on WHO Commission (2001), Filmer & Pritchett (1999), and Cutler, Deaton &
  Lleras-Muney (2006).
author: Josh Lambert (stress test)
created: '2026-04-05'
license: ''
tags:
- field
- health-expenditure-outcomes
constructs:
- health_expenditure_per_capita
- life_expectancy
- infant_mortality
engines:
- ols_regression
- correlation_matrix
- meta_analysis
playbook_names:
- quick_start
construct_count: 3
finding_count: 3
proposition_count: 0
has_playbooks: true
has_data_sources: true
domain:
  id: health_expenditure_outcomes
  display_name: Health Expenditure & Outcomes
  description: Relationship between health spending and population health outcomes
  research_questions: []
  temporal_scope: 1960-present
  population: Countries worldwide
  level_of_analysis: macro
constructs_detail:
- id: health_expenditure_per_capita
  display_name: Health Expenditure Per Capita
  definition: Total health spending per person in PPP dollars
  aliases: []
  construct_type: quantifiable
- id: life_expectancy
  display_name: Life Expectancy
  definition: Expected years of life at birth
  aliases:
  - longevity
  - all-cause mortality
  construct_type: outcome
- id: infant_mortality
  display_name: Infant Mortality
  definition: Deaths per 1000 live births in first year
  aliases: []
  construct_type: outcome
findings_detail:
- finding_text: Health spending has strong positive effect on life expectancy — each
    10% increase associated with ~0.3 year gain
  construct_ids:
  - health_expenditure_per_capita
  - life_expectancy
  direction: positive
  effect_size: ''
  confidence: moderate
  method_used: ''
  finding_type: ''
  evidence_type: ''
- finding_text: Public health spending has NO significant effect on child mortality
    after controlling for income and education
  construct_ids:
  - health_expenditure_per_capita
  - infant_mortality
  direction: 'null'
  effect_size: ''
  confidence: strong
  method_used: ''
  finding_type: ''
  evidence_type: ''
- finding_text: Returns to health spending exhibit strong diminishing returns at high
    income levels
  construct_ids:
  - health_expenditure_per_capita
  - life_expectancy
  direction: conditional
  effect_size: ''
  confidence: moderate
  method_used: ''
  finding_type: ''
  evidence_type: ''
propositions_detail: []
sources_detail:
- id: who_commission_2001
  title: 'Macroeconomics and Health: Investing in Health for Economic Development'
  authors: WHO Commission
  year: 2001
  doi: null
  source_type: report
- id: filmer_pritchett_1999
  title: 'The Impact of Public Spending on Health: Does Money Matter?'
  authors: Deon Filmer, Lant Pritchett
  year: 1999
  doi: null
  source_type: journal_article
- id: cutler_deaton_lleras_muney_2006
  title: The Determinants of Mortality
  authors: David Cutler, Angus Deaton, Adriana Lleras-Muney
  year: 2006
  doi: null
  source_type: working_paper
playbooks_detail:
- id: quick_start
  display_name: Quick Start — Health Expenditure Outcomes
  description: Basic analysis workflow for the health_expenditure_outcomes domain.
  estimated_runtime: 1–3 minutes
  step_count: 2
  engines_used:
  - ols_regression
  - correlation_matrix
download_url: /packs/health-outcomes-global.pax.tar.gz
download_size: 2.2 KB
weight: 7974
related_packs:
- social-determinants-of-health
---

**Domain:** Health Expenditure & Outcomes

Relationship between health spending and population health outcomes

**Temporal scope:** 1960-present | **Population:** Countries worldwide

## Key Findings

- Health spending has strong positive effect on life expectancy — each 10% increase associated with ~0.3 year gain *(positive, moderate)*
- Public health spending has NO significant effect on child mortality after controlling for income and education *(null, strong)*
- Returns to health spending exhibit strong diminishing returns at high income levels *(conditional, moderate)*

## Sources

- WHO Commission (2001). *Macroeconomics and Health: Investing in Health for Economic Development*.
- Deon Filmer, Lant Pritchett (1999). *The Impact of Public Spending on Health: Does Money Matter?*.
- David Cutler, Angus Deaton, Adriana Lleras-Muney (2006). *The Determinants of Mortality*.

---
name: health-expenditure-systems
title: Health Expenditure Systems
version: 1.0.0
pax_type: topic
description: How health financing models, spending levels, and system organization
  affect population health outcomes, equity, and financial protection across countries
  worldwide.
author: null
created: '2026-04-05'
license: null
tags:
- topic
- health-systems
constructs:
- health_expenditure_per_capita
- hospital_beds_per_1000
- physician_density_per_1000
- out_of_pocket_health_pct
- universal_health_coverage_index
- catastrophic_health_expenditure_rate
engines:
- ols_regression
- correlation_matrix
playbook_names:
- quick_start
construct_count: 6
finding_count: 4
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
- id: health_expenditure_per_capita
  display_name: Health Expenditure Per Capita
  definition: Total health spending per person in purchasing power parity dollars,
    capturing aggregate resource allocation to health systems.
  aliases: []
  construct_type: quantifiable
- id: hospital_beds_per_1000
  display_name: Hospital Beds Per 1000
  definition: Number of inpatient hospital beds available per 1,000 population including
    public and private facilities
  aliases: []
  construct_type: quantifiable
- id: physician_density_per_1000
  display_name: Physician Density Per 1000
  definition: Number of practicing physicians per 1,000 population including generalists
    and specialists
  aliases: []
  construct_type: quantifiable
- id: out_of_pocket_health_pct
  display_name: Out-of-Pocket Health Expenditure Share
  definition: Share of total health expenditure paid directly by households at point
    of service delivery
  aliases: []
  construct_type: quantifiable
- id: universal_health_coverage_index
  display_name: Universal Health Coverage Index
  definition: WHO composite index measuring coverage of essential health services
    on a scale from 0 to 100
  aliases: []
  construct_type: quantifiable
- id: catastrophic_health_expenditure_rate
  display_name: Catastrophic Health Expenditure Rate
  definition: Percentage of households spending more than 10% of total household expenditure
    on out-of-pocket health payments
  aliases: []
  construct_type: outcome
findings_detail:
- finding_text: Health expenditure per capita is positively associated with life expectancy
    but with strongly diminishing returns above approximately $5000 PPP per capita
  construct_ids:
  - health_expenditure_per_capita
  direction: conditional
  effect_size: null
  confidence: strong
  method_used: ols_regression
- finding_text: Out-of-pocket health spending share is the strongest predictor of
    catastrophic health expenditure across 59 countries
  construct_ids:
  - out_of_pocket_health_pct
  - catastrophic_health_expenditure_rate
  direction: positive
  effect_size: null
  confidence: strong
  method_used: ols_regression
- finding_text: Universal health coverage index is negatively associated with preventable
    mortality across 153 countries in panel analysis
  construct_ids:
  - universal_health_coverage_index
  direction: negative
  effect_size: null
  confidence: strong
  method_used: ols_regression
- finding_text: Physician density is positively associated with health outcomes but
    with threshold effects plateauing around 3 physicians per 1,000 population
  construct_ids:
  - physician_density_per_1000
  direction: conditional
  effect_size: null
  confidence: moderate
  method_used: ols_regression
propositions_detail: []
sources_detail:
- id: who_ghed_2023
  title: WHO Global Health Expenditure Database 2023
  authors: World Health Organization
  year: 2023
  doi: null
  source_type: dataset
- id: wagstaff_2018_catastrophic
  title: 'Progress on catastrophic health spending in 133 countries: a retrospective
    observational study'
  authors: Wagstaff A, Flores G, Hsu J, et al.
  year: 2018
  doi: 10.1016/S2214-109X(17)30486-2
  source_type: journal_article
- id: moreno_serra_2015
  title: 'Broader health coverage is good for the nation''s health: evidence from
    country level panel data'
  authors: Moreno-Serra R, Smith PC
  year: 2015
  doi: 10.1098/rspa.2015.0626
  source_type: journal_article
- id: xu_2003_catastrophic
  title: 'Household catastrophic health expenditure: a multicountry analysis'
  authors: Xu K, Evans DB, Kawabata K, et al.
  year: 2003
  doi: 10.1016/S0140-6736(03)14639-8
  source_type: journal_article
playbooks_detail: []
download_url: https://pax-market.com/pax/health-expenditure-systems.pax.tar.gz
download_size: 2.5 KB
published_by: Praxis Agent
related_packs:
- health-outcomes-global
pax_name: health-expenditure-systems
weight: 7974
---

**Domain:** Health Expenditure & Outcomes

Relationship between health spending and population health outcomes including life expectancy and mortality

## Key Findings

- Health expenditure per capita is positively associated with life expectancy but with strongly diminishing returns above approximately $5000 PPP per capita *(conditional, strong)*
- Out-of-pocket health spending share is the strongest predictor of catastrophic health expenditure across 59 countries *(positive, strong)*
- Universal health coverage index is negatively associated with preventable mortality across 153 countries in panel analysis *(negative, strong)*
- Physician density is positively associated with health outcomes but with threshold effects plateauing around 3 physicians per 1,000 population *(conditional, moderate)*

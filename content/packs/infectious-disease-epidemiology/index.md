---
name: infectious-disease-epidemiology
title: Infectious Disease Epidemiology
version: 1.0.0
pax_type: topic
description: Determinants of infectious disease burden including vaccination coverage,
  healthcare capacity, antibiotic resistance, and cross-border transmission dynamics
  across countries worldwide.
author: null
created: '2026-04-05'
license: null
tags:
- topic
- infectious-disease-epi
constructs:
- disease_incidence_rate
- vaccination_coverage_rate
- healthcare_workforce_density
- infectious_disease_mortality
- outbreak_detection_capacity
- antibiotic_resistance_prevalence
engines:
- ols_regression
- logistic_regression
- correlation_matrix
- poisson_regression
playbook_names:
- quick_start
construct_count: 6
finding_count: 5
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: infectious_disease_epi
  display_name: Infectious Disease Epidemiology
  description: Determinants of infectious disease burden including vaccination coverage,
    healthcare capacity, and cross-border transmission dynamics
  research_questions: []
  temporal_scope: 2000-present
  population: Countries worldwide
  level_of_analysis: macro
constructs_detail:
- id: disease_incidence_rate
  display_name: Disease Incidence Rate
  definition: Number of new cases of a specified infectious disease per 100,000 population
    per year
  aliases: []
  construct_type: quantifiable
- id: vaccination_coverage_rate
  display_name: Vaccination Coverage Rate
  definition: Percentage of target population that has received recommended vaccine
    doses
  aliases: []
  construct_type: quantifiable
- id: healthcare_workforce_density
  display_name: Healthcare Workforce Density
  definition: Number of physicians, nurses, and midwives per 10,000 population
  aliases: []
  construct_type: quantifiable
- id: infectious_disease_mortality
  display_name: Infectious Disease Mortality
  definition: Deaths attributable to communicable diseases per 100,000 population
    per year
  aliases: []
  construct_type: outcome
- id: outbreak_detection_capacity
  display_name: Outbreak Detection Capacity
  definition: Country-level score for disease surveillance and early warning system
    capacity based on IHR core capacities
  aliases: []
  construct_type: quantifiable
- id: antibiotic_resistance_prevalence
  display_name: Antibiotic Resistance Prevalence
  definition: Proportion of bacterial isolates showing resistance to first-line antibiotics
    in clinical settings
  aliases: []
  construct_type: quantifiable
findings_detail:
- finding_text: Each 10 percentage point increase in DTP3 vaccination coverage is
    associated with a 5-7% reduction in under-5 mortality from vaccine-preventable
    diseases
  construct_ids:
  - vaccination_coverage_rate
  - disease_incidence_rate
  direction: negative
  effect_size: null
  confidence: strong
  method_used: ols_regression
- finding_text: Healthcare workforce density is negatively associated with infectious
    disease mortality across 204 countries after controlling for income and urbanization
  construct_ids:
  - healthcare_workforce_density
  - infectious_disease_mortality
  direction: negative
  effect_size: null
  confidence: strong
  method_used: poisson_regression
- finding_text: Countries scoring above 60 on IHR core capacity index experienced
    significantly shorter epidemic durations compared to countries scoring below 40
  construct_ids:
  - outbreak_detection_capacity
  - disease_incidence_rate
  direction: negative
  effect_size: null
  confidence: moderate
  method_used: logistic_regression
- finding_text: Antibiotic resistance prevalence is positively associated with treatment
    failure rates and excess mortality from bacterial infections, with an estimated
    700,000 annual deaths attributable to AMR globally
  construct_ids:
  - antibiotic_resistance_prevalence
  - infectious_disease_mortality
  direction: positive
  effect_size: null
  confidence: strong
  method_used: ols_regression
- finding_text: Vaccination coverage rate is the single strongest modifiable predictor
    of communicable disease burden in low-income countries
  construct_ids:
  - vaccination_coverage_rate
  - infectious_disease_mortality
  direction: negative
  effect_size: null
  confidence: strong
  method_used: correlation_matrix
propositions_detail: []
sources_detail:
- id: gbd_2019_diseases
  title: Global burden of 369 diseases and injuries in 204 countries and territories,
    1990-2019
  authors: GBD 2019 Diseases and Injuries Collaborators
  year: 2020
  doi: 10.1016/S0140-6736(20)30925-9
  source_type: journal_article
- id: ozawa_2016_roi
  title: Return on investment from childhood immunization in low- and middle-income
    countries
  authors: Ozawa S, Clark S, Portnoy A, et al.
  year: 2016
  doi: 10.1016/j.healthpol.2016.07.004
  source_type: journal_article
- id: who_ihr_2023
  title: WHO International Health Regulations State Party Self-Assessment Annual Report
    2023
  authors: World Health Organization
  year: 2023
  doi: null
  source_type: report
- id: oneill_2016_amr
  title: 'Tackling Drug-Resistant Infections Globally: Final Report and Recommendations'
  authors: O'Neill J
  year: 2016
  doi: null
  source_type: report
playbooks_detail: []
download_url: https://pax-market.com/packs/infectious-disease-epidemiology.pax.tar.gz
download_size: 2.6 KB
published_by: Praxis Agent
related_packs: []
pax_name: infectious-disease-epidemiology
weight: 7974
---

**Domain:** Infectious Disease Epidemiology

Determinants of infectious disease burden including vaccination coverage, healthcare capacity, and cross-border transmission dynamics

**Temporal scope:** 2000-present | **Population:** Countries worldwide

## Key Findings

- Each 10 percentage point increase in DTP3 vaccination coverage is associated with a 5-7% reduction in under-5 mortality from vaccine-preventable diseases *(negative, strong)*
- Healthcare workforce density is negatively associated with infectious disease mortality across 204 countries after controlling for income and urbanization *(negative, strong)*
- Countries scoring above 60 on IHR core capacity index experienced significantly shorter epidemic durations compared to countries scoring below 40 *(negative, moderate)*
- Antibiotic resistance prevalence is positively associated with treatment failure rates and excess mortality from bacterial infections, with an estimated 700,000 annual deaths attributable to AMR globally *(positive, strong)*
- Vaccination coverage rate is the single strongest modifiable predictor of communicable disease burden in low-income countries *(negative, strong)*

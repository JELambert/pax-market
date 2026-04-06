---
name: noncommunicable-diseases
title: Noncommunicable Diseases
version: 1.0.0
pax_type: topic
description: How lifestyle risk factors including obesity, tobacco use, alcohol consumption,
  and physical inactivity drive the global noncommunicable disease epidemic and mortality
  burden.
author: null
created: '2026-04-05'
license: null
tags:
- topic
- ncd-burden
constructs:
- ncd_mortality_rate
- obesity_prevalence_adult
- tobacco_use_prevalence
- alcohol_consumption_per_capita
- physical_inactivity_prevalence
- metabolic_risk_factor_burden
engines:
- ols_regression
- correlation_matrix
- logistic_regression
playbook_names:
- quick_start
construct_count: 6
finding_count: 4
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: ncd_burden
  display_name: Noncommunicable Disease Burden
  description: How lifestyle risk factors including obesity, tobacco use, alcohol
    consumption, and physical inactivity drive the global NCD epidemic
  research_questions: []
  temporal_scope: 2000-present
  population: Countries worldwide
  level_of_analysis: macro
constructs_detail:
- id: ncd_mortality_rate
  display_name: NCD Mortality Rate
  definition: Age-standardized mortality rate from noncommunicable diseases including
    cardiovascular, cancer, diabetes, and chronic respiratory diseases per 100,000
    population
  aliases: []
  construct_type: outcome
- id: obesity_prevalence_adult
  display_name: Adult Obesity Prevalence
  definition: Age-standardized prevalence of obesity (BMI >= 30) among adults aged
    18 and over
  aliases: []
  construct_type: quantifiable
- id: tobacco_use_prevalence
  display_name: Tobacco Use Prevalence
  definition: Age-standardized prevalence of current tobacco smoking among persons
    aged 15 years and older
  aliases: []
  construct_type: quantifiable
- id: alcohol_consumption_per_capita
  display_name: Alcohol Consumption Per Capita
  definition: Total per capita alcohol consumption in liters of pure alcohol among
    persons aged 15 years and older
  aliases: []
  construct_type: quantifiable
- id: physical_inactivity_prevalence
  display_name: Physical Inactivity Prevalence
  definition: Age-standardized prevalence of insufficient physical activity among
    adults aged 18 and over based on WHO guidelines
  aliases: []
  construct_type: quantifiable
- id: metabolic_risk_factor_burden
  display_name: Metabolic Risk Factor Burden
  definition: Composite measure of population exposure to metabolic risk factors including
    high blood pressure, high blood sugar, high BMI, and abnormal lipids
  aliases: []
  construct_type: quantifiable
findings_detail:
- finding_text: Tobacco use is the leading preventable risk factor for noncommunicable
    diseases causing approximately 8 million deaths annually worldwide
  construct_ids:
  - tobacco_use_prevalence
  - ncd_mortality_rate
  direction: positive
  effect_size: null
  confidence: strong
  method_used: ols_regression
- finding_text: Adult obesity prevalence has tripled globally since 1975 and is positively
    associated with diabetes incidence and cardiovascular mortality across 200 countries
  construct_ids:
  - obesity_prevalence_adult
  - ncd_mortality_rate
  direction: positive
  effect_size: null
  confidence: strong
  method_used: ols_regression
- finding_text: Physical inactivity accounts for approximately 5 million deaths per
    year globally and is an independent risk factor for cardiovascular disease, diabetes,
    and cancer
  construct_ids:
  - physical_inactivity_prevalence
  - ncd_mortality_rate
  direction: positive
  effect_size: null
  confidence: strong
  method_used: logistic_regression
- finding_text: Noncommunicable diseases cause 74% of all global deaths with cardiovascular
    diseases, cancers, chronic respiratory diseases, and diabetes as leading causes
  construct_ids:
  - ncd_mortality_rate
  direction: positive
  effect_size: null
  confidence: strong
  method_used: correlation_matrix
propositions_detail: []
sources_detail:
- id: gbd_2019_risk
  title: Global burden of 87 risk factors in 204 countries and territories, 1990-2019
  authors: GBD 2019 Risk Factors Collaborators
  year: 2020
  doi: 10.1016/S0140-6736(20)30752-2
  source_type: journal_article
- id: ncdrisc_2016_bmi
  title: Trends in adult body-mass index in 200 countries from 1975 to 2014
  authors: NCD Risk Factor Collaboration
  year: 2016
  doi: 10.1016/S0140-6736(16)30054-X
  source_type: journal_article
- id: who_ncd_2023
  title: WHO Global Status Report on Noncommunicable Diseases 2023
  authors: World Health Organization
  year: 2023
  doi: null
  source_type: report
- id: afshin_2019_diet
  title: Health effects of dietary risks in 195 countries, 1990-2017
  authors: Afshin A, Sur PJ, Fay KA, et al.
  year: 2019
  doi: 10.1016/S0140-6736(19)30041-8
  source_type: journal_article
playbooks_detail: []
download_url: https://pax-market.com/packs/noncommunicable-diseases.pax.tar.gz
download_size: 2.4 KB
published_by: Praxis Agent
related_packs: []
pax_name: noncommunicable-diseases
weight: 7974
---

**Domain:** Noncommunicable Disease Burden

How lifestyle risk factors including obesity, tobacco use, alcohol consumption, and physical inactivity drive the global NCD epidemic

**Temporal scope:** 2000-present | **Population:** Countries worldwide

## Key Findings

- Tobacco use is the leading preventable risk factor for noncommunicable diseases causing approximately 8 million deaths annually worldwide *(positive, strong)*
- Adult obesity prevalence has tripled globally since 1975 and is positively associated with diabetes incidence and cardiovascular mortality across 200 countries *(positive, strong)*
- Physical inactivity accounts for approximately 5 million deaths per year globally and is an independent risk factor for cardiovascular disease, diabetes, and cancer *(positive, strong)*
- Noncommunicable diseases cause 74% of all global deaths with cardiovascular diseases, cancers, chronic respiratory diseases, and diabetes as leading causes *(positive, strong)*

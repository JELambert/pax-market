---
name: mental-health-global
title: Mental Health Global
version: 1.0.0
pax_type: topic
description: Prevalence, determinants, and economic costs of mental health disorders
  globally including depression, anxiety, substance use disorders, and suicide mortality.
author: null
created: '2026-04-05'
license: null
tags:
- topic
- global-mental-health
constructs:
- depression_prevalence_rate
- anxiety_disorder_prevalence
- suicide_mortality_rate
- mental_health_workforce
- substance_use_disorder_prevalence
- mental_health_spending_pct
engines:
- ols_regression
- correlation_matrix
playbook_names:
- quick_start
construct_count: 6
finding_count: 5
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: global_mental_health
  display_name: Global Mental Health Burden
  description: Prevalence, determinants, and economic costs of mental health disorders
    globally including depression, anxiety, and suicide
  research_questions: []
  temporal_scope: 1990-present
  population: Countries worldwide
  level_of_analysis: macro
constructs_detail:
- id: depression_prevalence_rate
  display_name: Depression Prevalence Rate
  definition: Age-standardized prevalence of major depressive disorder per 100,000
    population
  aliases: []
  construct_type: quantifiable
- id: anxiety_disorder_prevalence
  display_name: Anxiety Disorder Prevalence
  definition: Age-standardized prevalence of anxiety disorders including GAD, social
    phobia, and panic disorder per 100,000 population
  aliases: []
  construct_type: quantifiable
- id: suicide_mortality_rate
  display_name: Suicide Mortality Rate
  definition: Age-standardized suicide deaths per 100,000 population per year
  aliases: []
  construct_type: outcome
- id: mental_health_workforce
  display_name: Mental Health Workforce
  definition: Number of mental health professionals including psychiatrists, psychologists,
    and social workers per 100,000 population
  aliases: []
  construct_type: quantifiable
- id: substance_use_disorder_prevalence
  display_name: Substance Use Disorder Prevalence
  definition: Age-standardized prevalence of alcohol and drug use disorders per 100,000
    population
  aliases: []
  construct_type: quantifiable
- id: mental_health_spending_pct
  display_name: Mental Health Spending Share
  definition: Proportion of total health budget allocated specifically to mental health
    services and programs
  aliases: []
  construct_type: quantifiable
findings_detail:
- finding_text: Depression is the leading cause of disability worldwide affecting
    approximately 280 million people with an age-standardized prevalence of 3,440
    per 100,000
  construct_ids:
  - depression_prevalence_rate
  direction: positive
  effect_size: null
  confidence: strong
  method_used: ols_regression
- finding_text: Mental disorders account for approximately 13% of the global disease
    burden measured in DALYs but receive less than 2% of government health budgets
    on average
  construct_ids:
  - mental_health_spending_pct
  direction: negative
  effect_size: null
  confidence: strong
  method_used: correlation_matrix
- finding_text: Mental health workforce density is negatively associated with age-standardized
    suicide mortality rate across 130 countries
  construct_ids:
  - mental_health_workforce
  - suicide_mortality_rate
  direction: negative
  effect_size: null
  confidence: moderate
  method_used: ols_regression
- finding_text: Substance use disorder prevalence is positively associated with depression
    prevalence reflecting strong bidirectional comorbidity patterns across populations
  construct_ids:
  - substance_use_disorder_prevalence
  - depression_prevalence_rate
  direction: positive
  effect_size: null
  confidence: strong
  method_used: correlation_matrix
- finding_text: Anxiety disorders are the most prevalent mental health condition globally
    with age-standardized rates of approximately 3,800 per 100,000 population
  construct_ids:
  - anxiety_disorder_prevalence
  direction: positive
  effect_size: null
  confidence: strong
  method_used: ols_regression
propositions_detail: []
sources_detail:
- id: gbd_2019_mental
  title: Global, regional, and national burden of 12 mental disorders in 204 countries
    and territories, 1990-2019
  authors: GBD 2019 Mental Disorders Collaborators
  year: 2022
  doi: 10.1016/S2215-0366(21)00395-3
  source_type: journal_article
- id: patel_2018_lancet
  title: The Lancet Commission on global mental health and sustainable development
  authors: Patel V, Saxena S, Lund C, et al.
  year: 2018
  doi: 10.1016/S0140-6736(18)31612-X
  source_type: journal_article
- id: bloom_2011_ncd
  title: The Global Economic Burden of Noncommunicable Diseases
  authors: Bloom DE, Cafiero ET, Jane-Llopis E, et al.
  year: 2011
  doi: null
  source_type: report
- id: who_mh_atlas_2020
  title: Mental Health Atlas 2020
  authors: World Health Organization
  year: 2021
  doi: null
  source_type: report
playbooks_detail: []
download_url: https://pax-market.com/packs/mental-health-global.pax.tar.gz
download_size: 2.4 KB
published_by: Praxis Agent
related_packs: []
pax_name: mental-health-global
weight: 7974
---

**Domain:** Global Mental Health Burden

Prevalence, determinants, and economic costs of mental health disorders globally including depression, anxiety, and suicide

**Temporal scope:** 1990-present | **Population:** Countries worldwide

## Key Findings

- Depression is the leading cause of disability worldwide affecting approximately 280 million people with an age-standardized prevalence of 3,440 per 100,000 *(positive, strong)*
- Mental disorders account for approximately 13% of the global disease burden measured in DALYs but receive less than 2% of government health budgets on average *(negative, strong)*
- Mental health workforce density is negatively associated with age-standardized suicide mortality rate across 130 countries *(negative, moderate)*
- Substance use disorder prevalence is positively associated with depression prevalence reflecting strong bidirectional comorbidity patterns across populations *(positive, strong)*
- Anxiety disorders are the most prevalent mental health condition globally with age-standardized rates of approximately 3,800 per 100,000 population *(positive, strong)*

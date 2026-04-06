---
name: water-sanitation-hygiene
title: Water Sanitation Hygiene
version: 1.0.0
pax_type: topic
description: Impact of water, sanitation and hygiene infrastructure on health outcomes
  and economic development in low and middle income countries
author: null
created: '2026-04-05'
license: null
tags:
- topic
- wash-development
constructs:
- safe_drinking_water_access
- basic_sanitation_access
- hygiene_facility_access
- diarrheal_disease_mortality
- stunting_prevalence_under5
- wash_investment_per_capita
engines:
- ols_regression
- meta_analysis
- cost_benefit_analysis
playbook_names:
- quick_start
construct_count: 6
finding_count: 4
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: wash_development
  display_name: Water, Sanitation and Hygiene (WASH)
  description: Impact of water and sanitation infrastructure on health outcomes and
    economic development in low and middle income countries
  research_questions: []
  temporal_scope: 2000-present
  population: Low and middle income countries
  level_of_analysis: macro
constructs_detail:
- id: safe_drinking_water_access
  display_name: Safe Drinking Water Access
  definition: Percentage of population using safely managed drinking water services
    as defined by WHO/UNICEF Joint Monitoring Programme
  aliases: []
  construct_type: quantifiable
- id: basic_sanitation_access
  display_name: Basic Sanitation Access
  definition: Percentage of population using at least basic sanitation services including
    flush and pit latrines
  aliases: []
  construct_type: quantifiable
- id: hygiene_facility_access
  display_name: Hygiene Facility Access
  definition: Percentage of population with basic handwashing facility with soap and
    water on premises
  aliases: []
  construct_type: quantifiable
- id: diarrheal_disease_mortality
  display_name: Diarrheal Disease Mortality
  definition: Deaths from diarrheal diseases per 100000 population per year including
    cholera dysentery and rotavirus
  aliases: []
  construct_type: quantifiable
- id: stunting_prevalence_under5
  display_name: Stunting Prevalence Under 5
  definition: Percentage of children under 5 years with height-for-age z-score below
    minus 2 standard deviations from median
  aliases: []
  construct_type: quantifiable
- id: wash_investment_per_capita
  display_name: WASH Investment Per Capita
  definition: Annual per capita expenditure on water supply and sanitation infrastructure
    measured in constant USD
  aliases: []
  construct_type: quantifiable
findings_detail:
- finding_text: Water, sanitation and hygiene interventions yield benefit-cost ratios
    ranging from 5:1 to 28:1 depending on intervention type. Halving the population
    without access would generate $84 billion in annual benefits.
  construct_ids:
  - wash_investment_return
  - safe_water_access
  direction: positive
  effect_size: BCR 5:1 to 28:1; $84B annual benefits
  confidence: moderate
  method_used: Cost-benefit economic modeling
- finding_text: Safe drinking water access is negatively associated with diarrheal
    disease mortality across low and middle income countries
  construct_ids:
  - safe_drinking_water_access
  - diarrheal_disease_mortality
  direction: negative
  effect_size: null
  confidence: strong
  method_used: systematic review and meta-analysis
- finding_text: Basic sanitation coverage is negatively associated with stunting prevalence
    in children under five years of age
  construct_ids:
  - basic_sanitation_access
  - stunting_prevalence_under5
  direction: negative
  effect_size: null
  confidence: moderate
  method_used: cross-country regression analysis
- finding_text: WASH interventions demonstrate approximately 4 to 1 benefit-cost ratio
    in developing countries when accounting for health productivity and time savings
  construct_ids:
  - wash_investment_per_capita
  - diarrheal_disease_mortality
  - stunting_prevalence_under5
  direction: positive
  effect_size: null
  confidence: strong
  method_used: cost-benefit analysis
propositions_detail: []
sources_detail:
- id: hutton_haller_2004
  title: Evaluation of the Costs and Benefits of Water and Sanitation Improvements
    at the Global Level
  authors: Guy Hutton, Laurence Haller
  year: 2004
  doi: null
  source_type: report
- id: pruss_ustun_2014
  title: Burden of disease from inadequate water sanitation and hygiene in low and
    middle income settings
  authors: Pruss-Ustun, Annette, Bartram, Jamie, Clasen, Thomas, Colford, John, Cumming,
    Oliver, Curtis, Valerie
  year: 2014
  doi: 10.1111/tmi.12329
  source_type: academic_paper
- id: wolf_2018
  title: Systematic review meta-analysis and dose-response assessment of the relationship
    between water sanitation and hygiene and diarrhoeal diseases
  authors: Wolf, Jennyfer, Hunter, Paul, Freeman, Matthew, Cumming, Oliver, Clasen,
    Thomas, Bartram, Jamie, Pruss-Ustun, Annette
  year: 2018
  doi: 10.1016/j.ijheh.2018.05.003
  source_type: academic_paper
playbooks_detail: []
download_url: https://pax-market.com/packs/water-sanitation-hygiene.pax.tar.gz
download_size: 2.6 KB
published_by: Praxis Agent
related_packs: []
pax_name: water-sanitation-hygiene
weight: 7974
---

**Domain:** Water, Sanitation and Hygiene (WASH)

Impact of water and sanitation infrastructure on health outcomes and economic development in low and middle income countries

**Temporal scope:** 2000-present | **Population:** Low and middle income countries

## Key Findings

- Water, sanitation and hygiene interventions yield benefit-cost ratios ranging from 5:1 to 28:1 depending on intervention type. Halving the population without access would generate $84 billion in annual benefits. *(positive, moderate)*
- Safe drinking water access is negatively associated with diarrheal disease mortality across low and middle income countries *(negative, strong)*
- Basic sanitation coverage is negatively associated with stunting prevalence in children under five years of age *(negative, moderate)*
- WASH interventions demonstrate approximately 4 to 1 benefit-cost ratio in developing countries when accounting for health productivity and time savings *(positive, strong)*

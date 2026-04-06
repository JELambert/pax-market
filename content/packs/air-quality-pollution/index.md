---
name: air-quality-pollution
title: Air Quality Pollution
version: 1.0.0
pax_type: topic
description: Relationship between ambient and household air pollution exposure and
  mortality, respiratory disease, and economic productivity. Covers PM2.5, ozone,
  indoor air pollution, and the health benefits of clean fuel transitions.
author: null
created: '2026-04-05'
license: null
tags:
- topic
- air-quality-health
constructs:
- pm25_annual_mean
- air_pollution_attributable_deaths
- household_air_pollution_exposure
- respiratory_disease_burden
- outdoor_ozone_concentration
- clean_fuel_access
engines:
- ols_regression
- correlation_matrix
- logistic_regression
playbook_names:
- quick_start
construct_count: 6
finding_count: 5
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: air_quality_health
  display_name: Air Quality and Health Impacts
  description: Relationship between ambient and household air pollution exposure and
    mortality, respiratory disease, and economic productivity
  research_questions: []
  temporal_scope: 1990-present
  population: Global population
  level_of_analysis: macro
constructs_detail:
- id: pm25_annual_mean
  display_name: Annual Mean PM2.5 Concentration
  definition: Population-weighted annual mean concentration of fine particulate matter
    (particles smaller than 2.5 micrometers) in ambient air, measured in micrograms
    per cubic meter
  aliases: []
  construct_type: quantifiable
- id: air_pollution_attributable_deaths
  display_name: Air Pollution Attributable Deaths
  definition: Number of premature deaths annually attributable to exposure to ambient
    and household air pollution, estimated through integrated exposure-response functions
  aliases: []
  construct_type: outcome
- id: household_air_pollution_exposure
  display_name: Household Air Pollution Exposure
  definition: Level of indoor air pollution exposure from use of solid fuels for cooking
    and heating, measured by proportion of population relying on polluting fuels
  aliases: []
  construct_type: quantifiable
- id: respiratory_disease_burden
  display_name: Respiratory Disease Burden
  definition: Total burden of respiratory diseases including COPD, lower respiratory
    infections, and lung cancer, measured in disability-adjusted life years (DALYs)
    or deaths
  aliases: []
  construct_type: outcome
- id: outdoor_ozone_concentration
  display_name: Outdoor Ozone Concentration
  definition: Seasonal average of daily maximum 8-hour mean ozone concentration in
    ambient outdoor air, measured in parts per billion
  aliases: []
  construct_type: quantifiable
- id: clean_fuel_access
  display_name: Access to Clean Fuels for Cooking
  definition: Proportion of the population with primary reliance on clean fuels and
    technology for cooking, including electricity, LPG, natural gas, and biogas
  aliases: []
  construct_type: quantifiable
findings_detail:
- finding_text: Long-term exposure to ambient PM2.5 is positively associated with
    all-cause mortality, with a supralinear concentration-response function showing
    greatest risk increases at lower concentrations
  construct_ids:
  - pm25_annual_mean
  - air_pollution_attributable_deaths
  direction: positive
  effect_size: null
  confidence: strong
  method_used: meta_analysis
- finding_text: Ambient air pollution was responsible for an estimated 4.2 million
    deaths globally in 2015, making it the fifth-ranking mortality risk factor worldwide
  construct_ids:
  - pm25_annual_mean
  - air_pollution_attributable_deaths
  direction: positive
  effect_size: null
  confidence: strong
  method_used: integrated_exposure_response
- finding_text: Household air pollution from solid fuel combustion accounts for approximately
    3.8 million premature deaths annually, primarily from COPD, pneumonia, and lung
    cancer
  construct_ids:
  - household_air_pollution_exposure
  - respiratory_disease_burden
  direction: positive
  effect_size: null
  confidence: strong
  method_used: comparative_risk_assessment
- finding_text: Transition from solid fuels to clean cooking fuels reduces household
    air pollution exposure and respiratory disease burden by 40-60% in intervention
    studies
  construct_ids:
  - clean_fuel_access
  - respiratory_disease_burden
  direction: negative
  effect_size: null
  confidence: moderate
  method_used: systematic_review
- finding_text: Ambient ozone exposure is independently associated with respiratory
    mortality, contributing an estimated 254,000 deaths from COPD globally in 2015
  construct_ids:
  - outdoor_ozone_concentration
  - respiratory_disease_burden
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: integrated_exposure_response
propositions_detail: []
sources_detail:
- id: cohen_2017
  title: 'Estimates and 25-year trends of the global burden of disease attributable
    to ambient air pollution: an analysis of data from the Global Burden of Diseases
    Study 2015'
  authors: Cohen, A.J., Brauer, M., Burnett, R., Anderson, H.R., et al.
  year: 2017
  doi: 10.1016/S0140-6736(17)30505-6
  source_type: journal_article
- id: burnett_2018
  title: Global estimates of mortality associated with long-term exposure to outdoor
    fine particulate matter
  authors: Burnett, R., Chen, H., Szyszkowicz, M., Fann, N., et al.
  year: 2018
  doi: 10.1073/pnas.1803222115
  source_type: journal_article
- id: who_2021
  title: 'WHO Global Air Quality Guidelines: Particulate Matter (PM2.5 and PM10),
    Ozone, Nitrogen Dioxide, Sulfur Dioxide and Carbon Monoxide'
  authors: World Health Organization
  year: 2021
  doi: null
  source_type: report
- id: gordon_2014
  title: Respiratory risks from household air pollution in low and middle income countries
  authors: Gordon, S.B., Bruce, N.G., Grigg, J., et al.
  year: 2014
  doi: 10.1016/S2213-2600(14)70168-7
  source_type: journal_article
playbooks_detail: []
download_url: https://pax-market.com/packs/air-quality-pollution.pax.tar.gz
download_size: 2.9 KB
published_by: Praxis Agent
related_packs: []
pax_name: air-quality-pollution
weight: 7974
---

**Domain:** Air Quality and Health Impacts

Relationship between ambient and household air pollution exposure and mortality, respiratory disease, and economic productivity

**Temporal scope:** 1990-present | **Population:** Global population

## Key Findings

- Long-term exposure to ambient PM2.5 is positively associated with all-cause mortality, with a supralinear concentration-response function showing greatest risk increases at lower concentrations *(positive, strong)*
- Ambient air pollution was responsible for an estimated 4.2 million deaths globally in 2015, making it the fifth-ranking mortality risk factor worldwide *(positive, strong)*
- Household air pollution from solid fuel combustion accounts for approximately 3.8 million premature deaths annually, primarily from COPD, pneumonia, and lung cancer *(positive, strong)*
- Transition from solid fuels to clean cooking fuels reduces household air pollution exposure and respiratory disease burden by 40-60% in intervention studies *(negative, moderate)*
- Ambient ozone exposure is independently associated with respiratory mortality, contributing an estimated 254,000 deaths from COPD globally in 2015 *(positive, moderate)*

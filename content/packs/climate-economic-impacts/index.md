---
title: Economic impacts of climate change
pax_name: climate-economic-impacts
version: 1.0.0
pax_type: topic
description: Economic impacts of climate change — how temperature and precipitation
  affect GDP growth, agricultural yields, and long-run development. Built on Dell,
  Jones & Olken (2012), Burke, Hsiang & Miguel (2015), Nordhaus (2018), Hsiang et
  al. (2017), and Schlenker & Roberts (2009).
author: Dell, Melissa; Burke, Marshall; Nordhaus, William D.; Hsiang, Solomon; Schlenker,
  Wolfram
created: '2026-04-04'
license: ''
tags:
- topic
- climate-economic-impacts
constructs:
- mean_surface_temperature
- gdp_per_capita_growth
- climate_damage_fraction
- agricultural_yield
- precipitation
- social_cost_of_carbon
engines:
- ols_regression
- instrumental_variables
- difference_in_differences
- correlation_matrix
playbook_names:
- quick_start
construct_count: 6
finding_count: 5
proposition_count: 0
has_playbooks: true
has_data_sources: true
domain:
  id: climate_economic_impacts
  display_name: Economic Impacts of Climate Change
  description: 'How climatic variables affect macroeconomic outcomes including GDP
    growth, agricultural output, and long-run development. Core debate: level effects
    vs growth-rate effects.'
  research_questions: []
  temporal_scope: 1960-present
  population: Sovereign states (country-year observations)
  level_of_analysis: macro
constructs_detail:
- id: mean_surface_temperature
  display_name: Mean Surface Temperature
  definition: Annual average surface temperature (degrees Celsius) for a country,
    from gridded meteorological datasets.
  aliases:
  - average temperature
  - temperature anomaly
  construct_type: quantifiable
- id: gdp_per_capita_growth
  display_name: GDP Per Capita Growth Rate
  definition: Annual percentage change in real GDP per capita. Growth-rate effects
    compound; level effects do not.
  aliases:
  - economic growth
  - income growth
  construct_type: quantifiable
- id: climate_damage_fraction
  display_name: Climate Damage Fraction
  definition: Share of GDP lost due to climate change impacts, from integrated assessment
    damage functions.
  aliases:
  - climate damages
  - GDP loss fraction
  construct_type: outcome
- id: agricultural_yield
  display_name: Agricultural Yield
  definition: Crop output per unit of harvested area (tonnes per hectare).
  aliases:
  - crop yield
  - crop productivity
  construct_type: quantifiable
- id: precipitation
  display_name: Annual Precipitation
  definition: Total annual precipitation (mm) from gridded meteorological data.
  aliases:
  - rainfall
  - annual rainfall
  construct_type: quantifiable
- id: social_cost_of_carbon
  display_name: Social Cost of Carbon
  definition: Marginal economic damage of one additional tonne of CO2, in USD. Ranges
    from ~$50 to ~$185/tonne.
  aliases:
  - SCC
  - carbon price
  construct_type: quantifiable
findings_detail:
- finding_text: A 1C increase in temperature reduces GDP per capita growth by ~1.2
    percentage points in poor countries. Rich countries show no significant effect.
  construct_ids:
  - mean_surface_temperature
  - gdp_per_capita_growth
  direction: negative
  effect_size: ''
  confidence: strong
  method_used: OLS with country and year fixed effects
  finding_type: ''
  evidence_type: ''
- finding_text: Economic productivity peaks at ~13C and declines nonlinearly above
    that threshold, for both rich and poor countries.
  construct_ids:
  - mean_surface_temperature
  - gdp_per_capita_growth
  direction: negative
  effect_size: ''
  confidence: strong
  method_used: OLS with country and year FE, quadratic
  finding_type: ''
  evidence_type: ''
- finding_text: Unmitigated warming projected to reduce average global incomes by
    ~23% by 2100 and widen global inequality.
  construct_ids:
  - mean_surface_temperature
  - climate_damage_fraction
  direction: negative
  effect_size: ''
  confidence: moderate
  method_used: Panel econometrics + Monte Carlo projections
  finding_type: ''
  evidence_type: ''
- finding_text: DICE quadratic damage function implies 2.1% GDP loss at 3C and 8.5%
    at 6C of warming.
  construct_ids:
  - mean_surface_temperature
  - climate_damage_fraction
  - social_cost_of_carbon
  direction: negative
  effect_size: ''
  confidence: moderate
  method_used: Integrated assessment model (DICE)
  finding_type: ''
  evidence_type: ''
- finding_text: Climate trends 1980-2008 reduced global maize yields by 3.8% and wheat
    by 5.5% vs counterfactual.
  construct_ids:
  - mean_surface_temperature
  - agricultural_yield
  direction: negative
  effect_size: ''
  confidence: strong
  method_used: Panel regression, cross-country
  finding_type: ''
  evidence_type: ''
propositions_detail: []
sources_detail:
- id: dell_jones_olken_2012
  title: 'Temperature Shocks and Economic Growth: Evidence from the Last Half Century'
  authors: Dell, Melissa; Jones, Benjamin F.; Olken, Benjamin A.
  year: 2012
  doi: null
  source_type: academic_paper
- id: burke_hsiang_miguel_2015
  title: Global non-linear effect of temperature on economic production
  authors: Burke, Marshall; Hsiang, Solomon M.; Miguel, Edward
  year: 2015
  doi: null
  source_type: academic_paper
- id: nordhaus_2018
  title: 'Evolution of modeling of the economics of global warming: changes in the
    DICE model, 1992-2017'
  authors: Nordhaus, William D.
  year: 2018
  doi: null
  source_type: academic_paper
- id: lobell_schlenker_roberts_2011
  title: Climate Trends and Global Crop Production Since 1980
  authors: Lobell, David B.; Schlenker, Wolfram; Costa-Roberts, Justin
  year: 2011
  doi: null
  source_type: academic_paper
playbooks_detail:
- id: quick_start
  display_name: Quick Start — Climate Economic Impacts
  description: Basic analysis workflow for the climate_economic_impacts domain.
  estimated_runtime: 1–3 minutes
  step_count: 2
  engines_used:
  - ols_regression
  - correlation_matrix
download_url: /packs/climate-economic-impacts.pax.tar.gz
download_size: 3.1 KB
weight: 7974
related_packs: []
---

**Domain:** Economic Impacts of Climate Change

How climatic variables affect macroeconomic outcomes including GDP growth, agricultural output, and long-run development. Core debate: level effects vs growth-rate effects.

**Temporal scope:** 1960-present | **Population:** Sovereign states (country-year observations)

## Key Findings

- A 1C increase in temperature reduces GDP per capita growth by ~1.2 percentage points in poor countries. Rich countries show no significant effect. *(negative, strong)*
- Economic productivity peaks at ~13C and declines nonlinearly above that threshold, for both rich and poor countries. *(negative, strong)*
- Unmitigated warming projected to reduce average global incomes by ~23% by 2100 and widen global inequality. *(negative, moderate)*
- DICE quadratic damage function implies 2.1% GDP loss at 3C and 8.5% at 6C of warming. *(negative, moderate)*
- Climate trends 1980-2008 reduced global maize yields by 3.8% and wheat by 5.5% vs counterfactual. *(negative, strong)*

## Sources

- Dell, Melissa; Jones, Benjamin F.; Olken, Benjamin A. (2012). *Temperature Shocks and Economic Growth: Evidence from the Last Half Century*.
- Burke, Marshall; Hsiang, Solomon M.; Miguel, Edward (2015). *Global non-linear effect of temperature on economic production*.
- Nordhaus, William D. (2018). *Evolution of modeling of the economics of global warming: changes in the DICE model, 1992-2017*.
- Lobell, David B.; Schlenker, Wolfram; Costa-Roberts, Justin (2011). *Climate Trends and Global Crop Production Since 1980*.

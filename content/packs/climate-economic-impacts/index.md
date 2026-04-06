---
name: climate-economic-impacts
title: Economic impacts of climate change
version: 1.0.0
pax_type: topic
description: Economic impacts of climate change — how temperature and precipitation
  affect GDP growth, agricultural yields, and long-run development. Built on Dell,
  Jones & Olken (2012), Burke, Hsiang & Miguel (2015), Nordhaus (2018), Hsiang et
  al. (2017), and Schlenker & Roberts (2009).
author: ''
created: ''
license: ''
tags:
- topic
constructs:
- gdp_per_capita_growth
- climate_damage_fraction
- agricultural_yield
- precipitation
- social_cost_of_carbon
- mean_surface_temperature
engines:
- ols_regression
- instrumental_variables
- difference_in_differences
- correlation_matrix
playbook_names:
- quick_start
construct_count: 6
finding_count: 0
proposition_count: 0
has_playbooks: true
has_data_sources: false
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
- id: gdp_per_capita_growth
  display_name: GDP Per Capita Growth Rate
  definition: Annual percentage change in real GDP per capita. Growth-rate effects
    compound; level effects do not.
  aliases: []
  construct_type: quantifiable
- id: climate_damage_fraction
  display_name: Climate Damage Fraction
  definition: Share of GDP lost due to climate change impacts, from integrated assessment
    damage functions.
  aliases: []
  construct_type: outcome
- id: agricultural_yield
  display_name: Agricultural Yield
  definition: Crop output per unit of harvested area (tonnes per hectare).
  aliases: []
  construct_type: quantifiable
- id: precipitation
  display_name: Annual Precipitation
  definition: Total annual precipitation (mm) from gridded meteorological data.
  aliases: []
  construct_type: quantifiable
- id: social_cost_of_carbon
  display_name: Social Cost of Carbon
  definition: Marginal economic damage of one additional tonne of CO2, in USD. Ranges
    from ~$50 to ~$185/tonne.
  aliases: []
  construct_type: quantifiable
- id: mean_surface_temperature
  display_name: Mean Surface Temperature
  definition: Annual average surface temperature (degrees Celsius) for a country,
    from gridded meteorological datasets.
  aliases: []
  construct_type: quantifiable
findings_detail: []
propositions_detail: []
sources_detail: []
playbooks_detail: []
download_url: https://pax-market.com/packs/climate-economic-impacts.pax.tar.gz
download_size: 1.6 KB
published_by: Praxis Agent
related_packs: []
pax_name: climate-economic-impacts
weight: 10000
---

**Domain:** Economic Impacts of Climate Change

How climatic variables affect macroeconomic outcomes including GDP growth, agricultural output, and long-run development. Core debate: level effects vs growth-rate effects.

**Temporal scope:** 1960-present | **Population:** Sovereign states (country-year observations)

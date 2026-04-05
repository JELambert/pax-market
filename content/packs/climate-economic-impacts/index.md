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
findings:
- dell_jones_olken_2012_0
- burke_hsiang_miguel_2015_1
- burke_hsiang_miguel_2015_2
- nordhaus_2018_3
- lobell_schlenker_roberts_2011_4
engines:
- ols_regression
- instrumental_variables
- difference_in_differences
- correlation_matrix
playbooks:
- quick_start
propositions: []
construct_count: 6
finding_count: 5
proposition_count: 0
has_playbooks: true
has_data_sources: true
download_url: /packs/climate-economic-impacts.pax.tar.gz
download_size: 3.1 KB
weight: 7974
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

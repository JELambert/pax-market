---
name: energy-access-transition
title: Energy Access Transition
version: 1.0.0
pax_type: topic
description: How electricity access and clean energy transitions affect economic growth
  health outcomes and human capital formation
author: null
created: '2026-04-05'
license: null
tags:
- topic
- energy-access
constructs:
- electricity_access_rate
- energy_intensity_gdp
- fossil_fuel_consumption_per_capita
- energy_poverty_rate
- co2_emissions_per_capita_energy
- renewable_energy_share_total
engines:
- ols_regression
- instrumental_variables
- panel_regression
playbook_names:
- quick_start
construct_count: 6
finding_count: 3
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: energy_access
  display_name: Energy Access and Economic Development
  description: How electricity access and clean energy transitions affect economic
    growth health outcomes and human capital formation
  research_questions: []
  temporal_scope: 1990-present
  population: Countries worldwide
  level_of_analysis: macro
constructs_detail:
- id: electricity_access_rate
  display_name: Electricity Access Rate
  definition: Percentage of total population with access to electricity including
    grid and off-grid sources
  aliases: []
  construct_type: quantifiable
- id: energy_intensity_gdp
  display_name: Energy Intensity of GDP
  definition: Energy use per unit of GDP measured in megajoules per constant 2017
    PPP dollar reflecting economic efficiency of energy use
  aliases: []
  construct_type: quantifiable
- id: fossil_fuel_consumption_per_capita
  display_name: Fossil Fuel Consumption Per Capita
  definition: Primary energy consumption from fossil fuels per capita measured in
    kilowatt-hours per year
  aliases: []
  construct_type: quantifiable
- id: energy_poverty_rate
  display_name: Energy Poverty Rate
  definition: Percentage of population relying on traditional biomass such as wood
    dung and charcoal for cooking and heating
  aliases: []
  construct_type: quantifiable
- id: co2_emissions_per_capita_energy
  display_name: CO2 Emissions Per Capita from Energy
  definition: Carbon dioxide emissions from energy use per capita measured in metric
    tonnes per year
  aliases: []
  construct_type: quantifiable
- id: renewable_energy_share_total
  display_name: Renewable Energy Share of Total
  definition: Renewable energy share of total final energy consumption measured as
    percentage including hydro solar wind and biomass
  aliases: []
  construct_type: quantifiable
findings_detail:
- finding_text: Electricity access is positively associated with GDP per capita growth
    through increased labor force participation and firm productivity
  construct_ids:
  - electricity_access_rate
  direction: positive
  effect_size: null
  confidence: strong
  method_used: instrumental variable regression
- finding_text: Higher renewable energy share is negatively associated with CO2 emissions
    per capita controlling for GDP and industrialization levels
  construct_ids:
  - renewable_energy_share_total
  - co2_emissions_per_capita_energy
  direction: negative
  effect_size: null
  confidence: strong
  method_used: panel regression with fixed effects
- finding_text: Energy intensity of GDP decreases with economic development following
    an inverted-U pattern consistent with structural transformation theory
  construct_ids:
  - energy_intensity_gdp
  direction: negative
  effect_size: null
  confidence: moderate
  method_used: cross-country panel analysis
propositions_detail: []
sources_detail:
- id: dinkelman_2011
  title: The effects of rural electrification on employment new evidence from South
    Africa
  authors: Dinkelman, Taryn
  year: 2011
  doi: 10.1257/aer.101.7.3078
  source_type: academic_paper
- id: burke_2018
  title: Global energy and CO2 emissions trends and projections
  authors: Burke, Paul, Shahiduzzaman, Md, Stern, David
  year: 2018
  doi: null
  source_type: academic_paper
- id: iea_weo_2023
  title: World Energy Outlook 2023
  authors: International Energy Agency
  year: 2023
  doi: null
  source_type: report
- id: wolfram_2012
  title: How will energy demand develop in the developing world
  authors: Wolfram, Catherine, Shelef, Orie, Gertler, Paul
  year: 2012
  doi: 10.1257/aer.102.3.338
  source_type: academic_paper
playbooks_detail: []
download_url: https://pax-market.com/pax/energy-access-transition.pax.tar.gz
download_size: 2.4 KB
published_by: Praxis Agent
related_packs: []
pax_name: energy-access-transition
weight: 7974
---

**Domain:** Energy Access and Economic Development

How electricity access and clean energy transitions affect economic growth health outcomes and human capital formation

**Temporal scope:** 1990-present | **Population:** Countries worldwide

## Key Findings

- Electricity access is positively associated with GDP per capita growth through increased labor force participation and firm productivity *(positive, strong)*
- Higher renewable energy share is negatively associated with CO2 emissions per capita controlling for GDP and industrialization levels *(negative, strong)*
- Energy intensity of GDP decreases with economic development following an inverted-U pattern consistent with structural transformation theory *(negative, moderate)*

---
name: climate-conflict-food-nexus
title: Climate Conflict Food Nexus
version: 1.0.1
pax_type: topic
description: The causal chain from climate shocks through agricultural disruption
  to food insecurity, displacement, and armed conflict. Maps the transmission mechanisms
  and compounding effects across environmental, food system, and political violence
  domains.
author: ''
created: '2026-04-06'
license: ''
tags:
- topic
- climate-conflict-food-nexus
constructs:
- drought_severity_index
- crop_failure_index
- livelihood_vulnerability
- resource_competition
- food_riot_incidence
- climate_migration
- pastoral_conflict
- compounding_shocks
engines:
- logistic_regression
- random_forest
playbook_names:
- quick_start
construct_count: 8
finding_count: 7
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: climate_conflict_food_nexus
  display_name: Climate-Conflict-Food Nexus
  description: Causal pathways linking climate variability and extreme weather to
    food insecurity, livelihood collapse, displacement, and armed conflict. Covers
    drought-crop failure-hunger chains, resource competition as conflict driver, and
    compounding shocks.
  research_questions: []
  temporal_scope: 1990-present
  population: Countries and subnational regions
  level_of_analysis: cross-level
constructs_detail:
- id: drought_severity_index
  display_name: Drought Severity Index
  definition: Standardized Precipitation Index (SPI) or Palmer Drought Severity Index
    (PDSI) measuring meteorological drought intensity. Negative values indicate drought;
    values below -2.0 indicate extreme drought. Key trigger for crop failure in rain-fed
    agricultural systems.
  aliases: []
  construct_type: quantifiable
- id: crop_failure_index
  display_name: Crop Failure Index
  definition: Agricultural production shortfall relative to 5-year moving average.
    Captures acute food supply shocks from weather, pests, or conflict. Directly links
    climate variability to food availability.
  aliases: []
  construct_type: quantifiable
- id: livelihood_vulnerability
  display_name: Livelihood Vulnerability
  definition: Dependence on climate-sensitive livelihoods (rain-fed farming, pastoralism,
    fishing) without diversification or buffering capacity. High vulnerability means
    climate shocks translate directly to food insecurity and displacement.
  aliases: []
  construct_type: concept
- id: resource_competition
  display_name: Resource Competition
  definition: Competition over scarce natural resources (water, pasture, arable land)
    as a driver of communal violence and armed conflict. Intensified by climate change
    reducing resource availability and demographic pressure increasing demand.
  aliases: []
  construct_type: concept
- id: food_riot_incidence
  display_name: Food Riot Incidence
  definition: Occurrence of food-price-triggered social unrest, protests, or riots.
    Food price spikes have historically triggered political instability — the 2007-08
    and 2010-11 global food price crises sparked unrest in 30+ countries and contributed
    to the Arab Spring.
  aliases: []
  construct_type: outcome
- id: climate_migration
  display_name: Climate Migration
  definition: Population movement driven primarily by environmental degradation, climate
    variability, or extreme weather events. Includes both internal displacement and
    cross-border migration. World Bank estimates 216 million internal climate migrants
    by 2050 under pessimistic scenarios.
  aliases: []
  construct_type: quantifiable
- id: pastoral_conflict
  display_name: Pastoral Conflict
  definition: Violence between pastoralist and farming communities driven by resource
    scarcity, particularly in the Sahel, Horn of Africa, and Central Africa. Droughts
    compress pastoral range, forcing herders into farming areas. A key transmission
    mechanism from climate stress to armed violence.
  aliases: []
  construct_type: outcome
- id: compounding_shocks
  display_name: Compounding Shocks
  definition: 'The interaction of multiple simultaneous stressors — climate shock
    + conflict + economic downturn + pandemic — that overwhelm coping capacity. Compounding
    effects are non-linear: each additional shock disproportionately increases food
    insecurity. The COVID-19 pandemic layered onto existing climate and conflict crises
    illustrates this dynamic.'
  aliases: []
  construct_type: concept
findings_detail:
- finding_text: Economic productivity peaks at ~13C and declines nonlinearly above
    that threshold, for both rich and poor countries.
  construct_ids:
  - mean_surface_temperature
  - gdp_per_capita_growth
  direction: negative
  effect_size: null
  confidence: strong
  method_used: OLS with country and year FE, quadratic
- finding_text: Unmitigated warming projected to reduce average global incomes by
    ~23% by 2100 and widen global inequality.
  construct_ids:
  - mean_surface_temperature
  - climate_damage_fraction
  direction: negative
  effect_size: null
  confidence: moderate
  method_used: Panel econometrics + Monte Carlo projections
- finding_text: The global relationship between temperature and economic output is
    strongly nonlinear — productivity peaks at approximately 13°C mean annual temperature
    and declines sharply at higher temperatures.
  construct_ids:
  - temperature_anomaly
  - climate_gdp_damage
  direction: negative
  effect_size: null
  confidence: strong
  method_used: Panel regression across 166 countries, 1960-2010
- finding_text: Unmitigated warming could reduce global GDP by 23% by 2100 relative
    to a no-warming scenario, with poor tropical countries projected to lose 75% or
    more of GDP.
  construct_ids:
  - climate_gdp_damage
  - temperature_anomaly
  direction: negative
  effect_size: 23% global GDP loss by 2100; 75%+ for poorest countries
  confidence: moderate
  method_used: Projection from estimated nonlinear damage function
- finding_text: 'Expert elicitation of 11 leading climate-conflict researchers concludes
    climate variability has influenced 3-20% of armed conflict risk over the past
    century, and this influence will grow substantially under 2-4C warming scenarios.
    The pathway is indirect: climate affects conflict through food insecurity, economic
    shocks, and displacement, not directly.'
  construct_ids:
  - drought_severity_index
  - resource_competition
  direction: positive
  effect_size: null
  confidence: strong
  method_used: Expert elicitation, structured protocol, 11 experts
- finding_text: Meta-analysis of 55 studies finds that a 1 standard deviation increase
    in temperature is associated with a 2.4% increase in interpersonal violence and
    a 11.3% increase in intergroup conflict. Effects are strongest in agricultural
    economies and conflict-prone regions.
  construct_ids:
  - drought_severity_index
  - resource_competition
  - pastoral_conflict
  direction: positive
  effect_size: null
  confidence: strong
  method_used: Meta-analysis of 55 quantitative studies
- finding_text: Extreme rainfall deviations (both drought and excess) significantly
    increase the likelihood of social conflict events in Africa. Water scarcity increases
    communal conflict and civil unrest; excess rainfall can also trigger violence
    through displacement and crop damage.
  construct_ids:
  - drought_severity_index
  - food_riot_incidence
  - pastoral_conflict
  direction: positive
  effect_size: null
  confidence: strong
  method_used: Negative binomial regression, African country-year/month panel, SCAD
    conflict data
propositions_detail: []
sources_detail:
- id: burke_hsiang_miguel_2015
  title: Global non-linear effect of temperature on economic production
  authors: Burke, Marshall; Hsiang, Solomon M.; Miguel, Edward
  year: 2015
  doi: null
  source_type: academic_paper
- id: mach_et_al_2019
  title: Climate as a risk factor for armed conflict
  authors: Katharine Mach et al.
  year: 2019
  doi: 10.1038/s41586-019-1300-6
  source_type: journal_article
- id: hendrix_salehyan_2012
  title: Climate shocks and political violence
  authors: Cullen Hendrix, Idean Salehyan
  year: 2012
  doi: 10.1016/j.gloenvcha.2011.12.001
  source_type: journal_article
playbooks_detail: []
download_url: https://pax-market.com/packs/climate-conflict-food-nexus.pax.tar.gz
download_size: 4.0 KB
published_by: Praxis Agent
related_packs: []
pax_name: climate-conflict-food-nexus
weight: 7974
---

**Domain:** Climate-Conflict-Food Nexus

Causal pathways linking climate variability and extreme weather to food insecurity, livelihood collapse, displacement, and armed conflict. Covers drought-crop failure-hunger chains, resource competition as conflict driver, and compounding shocks.

**Temporal scope:** 1990-present | **Population:** Countries and subnational regions

## Key Findings

- Economic productivity peaks at ~13C and declines nonlinearly above that threshold, for both rich and poor countries. *(negative, strong)*
- Unmitigated warming projected to reduce average global incomes by ~23% by 2100 and widen global inequality. *(negative, moderate)*
- The global relationship between temperature and economic output is strongly nonlinear — productivity peaks at approximately 13°C mean annual temperature and declines sharply at higher temperatures. *(negative, strong)*
- Unmitigated warming could reduce global GDP by 23% by 2100 relative to a no-warming scenario, with poor tropical countries projected to lose 75% or more of GDP. *(negative, moderate)*
- Expert elicitation of 11 leading climate-conflict researchers concludes climate variability has influenced 3-20% of armed conflict risk over the past century, and this influence will grow substantially under 2-4C warming scenarios. The pathway is indirect: climate affects conflict through food insecurity, economic shocks, and displacement, not directly. *(positive, strong)*
- Meta-analysis of 55 studies finds that a 1 standard deviation increase in temperature is associated with a 2.4% increase in interpersonal violence and a 11.3% increase in intergroup conflict. Effects are strongest in agricultural economies and conflict-prone regions. *(positive, strong)*
- Extreme rainfall deviations (both drought and excess) significantly increase the likelihood of social conflict events in Africa. Water scarcity increases communal conflict and civil unrest; excess rainfall can also trigger violence through displacement and crop damage. *(positive, strong)*

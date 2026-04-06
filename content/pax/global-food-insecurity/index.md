---
name: global-food-insecurity
title: Global Food Insecurity
version: 1.0.1
pax_type: topic
description: ''
author: ''
created: ''
license: ''
tags:
- topic
constructs:
- food_insecurity_experience_scale
- ipc_phase_classification
- global_hunger_index
- food_consumption_score
- dietary_energy_supply
- crop_yield_variability
- food_price_inflation
- conflict_food_insecurity
- climate_shock_food
- food_import_dependency
- social_protection_coverage
- coping_strategy_index
- stunting_prevalence_fi
- wasting_prevalence_fi
- prevalence_undernourishment
engines:
- logistic_regression
- random_forest
- ols_regression
playbook_names:
- quick_start
construct_count: 15
finding_count: 0
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: global_food_insecurity
  display_name: Global Food Insecurity
  description: Measurement, determinants, and geospatial variation in food insecurity
    at global, national, and subnational scales. Covers prevalence of undernourishment,
    food insecurity experience, acute food crises (IPC phases), and links to climate,
    conflict, poverty, and governance.
  research_questions: []
  temporal_scope: 1990-present
  population: Countries and subnational regions, household and individual observations
  level_of_analysis: cross-level
constructs_detail:
- id: food_insecurity_experience_scale
  display_name: Food Insecurity Experience Scale (FIES)
  definition: 'Experience-based metric (SDG 2.1.2) measuring severity of food insecurity
    through 8 yes/no questions about behaviors and experiences (worry about food,
    skipping meals, going hungry, going a whole day without eating). Collected via
    Gallup World Poll in 140+ countries since 2014. Yields prevalence of moderate
    and severe food insecurity. Advantage over PoU: captures lived experience, not
    just caloric supply.'
  aliases: []
  construct_type: quantifiable
- id: ipc_phase_classification
  display_name: IPC Phase Classification
  definition: 'Integrated Food Security Phase Classification: a 5-phase scale (Minimal,
    Stressed, Crisis, Emergency, Famine) classifying the severity of acute food insecurity
    at subnational level. Used by IPC Global Partnership across 30+ countries. Based
    on convergence of evidence from food consumption, livelihood change, nutritional
    status, and mortality. The standard framework for humanitarian food crisis assessment
    and response planning.'
  aliases: []
  construct_type: outcome
- id: global_hunger_index
  display_name: Global Hunger Index (GHI)
  definition: 'Composite index (0-100 scale) combining four indicators: prevalence
    of undernourishment (FAO), child wasting (WHO), child stunting (WHO), and child
    mortality (UN IGME). Published annually by Welthungerhilfe and Concern Worldwide
    for ~130 countries. Provides a single summary metric of hunger severity at country
    level.'
  aliases: []
  construct_type: composite
- id: food_consumption_score
  display_name: Food Consumption Score (FCS)
  definition: 'WFP''s standard proxy indicator for household food access and dietary
    quality. Composite score based on dietary diversity, food frequency, and relative
    nutritional importance of food groups consumed over the past 7 days. Thresholds:
    poor (<21), borderline (21.5-35), acceptable (>35). Collected in WFP vulnerability
    assessments and used in HungerMap LIVE nowcasting.'
  aliases: []
  construct_type: quantifiable
- id: dietary_energy_supply
  display_name: Dietary Energy Supply (DES)
  definition: Per capita daily caloric availability (kcal/capita/day) derived from
    FAO food balance sheets. Measures national food supply adequacy — the total food
    available for consumption after accounting for production, imports, exports, stock
    changes, and non-food uses. Does not capture distribution within country or household-level
    access.
  aliases: []
  construct_type: quantifiable
- id: crop_yield_variability
  display_name: Crop Yield Variability
  definition: Inter-annual variation in crop yields driven by climate variability,
    extreme weather, pest/disease pressure, and input availability. Climate variation
    explains roughly one-third of global crop yield variability (Ray et al. 2015).
    Key transmission mechanism from climate shocks to food insecurity, especially
    in rain-fed agriculture systems.
  aliases: []
  construct_type: quantifiable
- id: food_price_inflation
  display_name: Food Price Inflation
  definition: Rate of increase in food prices at market or national level. Rapid food
    price spikes erode purchasing power of poor households, directly increasing food
    insecurity. Monitored by WFP (ALPS indicator), FAO Food Price Index, and FEWS
    NET market data. Particularly impactful in countries with high food import dependency
    and low social protection coverage.
  aliases: []
  construct_type: quantifiable
- id: conflict_food_insecurity
  display_name: Conflict (Food Insecurity Driver)
  definition: 'Armed conflict as a primary driver of acute food insecurity. Conflict
    disrupts food production, destroys agricultural assets, displaces populations,
    blocks humanitarian access, and collapses markets. Conflict-affected countries
    account for the majority of people in IPC Phase 3+ (Crisis or worse). The conflict-hunger
    nexus is bidirectional: food insecurity can also fuel conflict.'
  aliases: []
  construct_type: quantifiable
- id: climate_shock_food
  display_name: Climate Shock
  definition: Extreme weather events (drought, flood, cyclone, heat wave) and climate
    variability affecting food production and access. Operationalized via NDVI anomalies,
    rainfall deficits (CHIRPS data), temperature extremes, or crop damage assessments.
    Primary driver of food crises in pastoral and rain-fed agricultural regions. Climate
    shocks interact with conflict and poverty to compound food insecurity.
  aliases: []
  construct_type: quantifiable
- id: food_import_dependency
  display_name: Food Import Dependency
  definition: Share of domestic food supply derived from imports, typically measured
    as cereal import dependency ratio. Countries highly dependent on food imports
    are vulnerable to global price shocks, supply chain disruptions, and currency
    depreciation. Small island developing states and conflict-affected countries often
    have extreme import dependency.
  aliases: []
  construct_type: quantifiable
- id: social_protection_coverage
  display_name: Social Protection Coverage
  definition: Share of population covered by social safety net programs (cash transfers,
    food assistance, school feeding, public works). Effective social protection buffers
    households against food insecurity during shocks. Measured by World Bank ASPIRE
    database. Coverage ranges from <10% in fragile states to >80% in OECD countries.
  aliases: []
  construct_type: quantifiable
- id: coping_strategy_index
  display_name: Coping Strategy Index (rCSI)
  definition: 'Reduced Coping Strategy Index: a rapid household-level measure of food
    insecurity severity based on frequency of five universal coping behaviors (eating
    less preferred foods, borrowing food, reducing portion sizes, restricting adult
    consumption, reducing number of meals). Higher scores indicate worse food insecurity.
    Used by WFP alongside FCS for real-time monitoring.'
  aliases: []
  construct_type: quantifiable
- id: stunting_prevalence_fi
  display_name: Stunting Prevalence
  definition: Percentage of children under 5 with height-for-age below -2 standard
    deviations of the WHO Child Growth Standards median. Primary indicator of chronic
    undernutrition and long-term food insecurity. Reflects cumulative effects of inadequate
    nutrition, repeated infections, and poor care practices. Links to existing Praxis
    construct stunting_prevalence in nutrition_stunting domain.
  aliases: []
  construct_type: outcome
- id: wasting_prevalence_fi
  display_name: Wasting Prevalence (GAM)
  definition: 'Global Acute Malnutrition: percentage of children under 5 with weight-for-height
    below -2 SD (moderate + severe wasting). Key indicator of acute food insecurity
    at population level, used in IPC nutrition analyses and SMART surveys. Threshold
    of 15% GAM triggers emergency classification. Links to existing Praxis construct
    wasting_prevalence.'
  aliases: []
  construct_type: outcome
- id: prevalence_undernourishment
  display_name: Prevalence of Undernourishment (PoU)
  definition: 'FAO''s flagship indicator (SDG 2.1.1): the estimated share of a population
    whose habitual food consumption is insufficient to meet dietary energy requirements.
    Derived from food balance sheets, food consumption surveys, and population distribution
    parameters. Country-level, annual. Widely used but criticized for masking within-country
    variation and relying on caloric adequacy alone.'
  aliases: []
  construct_type: outcome
findings_detail: []
propositions_detail: []
sources_detail: []
playbooks_detail: []
download_url: https://pax-market.com/pax/global-food-insecurity.pax.tar.gz
download_size: 4.1 KB
published_by: Praxis Agent
related_packs: []
pax_name: global-food-insecurity
weight: 10000
---

**Domain:** Global Food Insecurity

Measurement, determinants, and geospatial variation in food insecurity at global, national, and subnational scales. Covers prevalence of undernourishment, food insecurity experience, acute food crises (IPC phases), and links to climate, conflict, poverty, and governance.

**Temporal scope:** 1990-present | **Population:** Countries and subnational regions, household and individual observations

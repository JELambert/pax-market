---
name: water-stress-scarcity
title: Water Stress Scarcity
version: 1.0.0
pax_type: topic
description: Global freshwater scarcity, agricultural water use, and the water-energy-food
  nexus with implications for conflict and development.
author: null
created: '2026-04-05'
license: null
tags:
- topic
- water-stress
constructs:
- freshwater_withdrawal_percent
- water_stress_level
- agricultural_water_use_percent
- water_use_efficiency
- renewable_freshwater_per_capita
- water_related_conflict_events
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
  id: water_stress
  display_name: Water Stress and Scarcity
  description: Global freshwater scarcity, agricultural water use, and the water-energy-food
    nexus with implications for conflict and development
  research_questions: []
  temporal_scope: 1990-present
  population: Water-stressed regions worldwide
  level_of_analysis: macro
constructs_detail:
- id: freshwater_withdrawal_percent
  display_name: Freshwater Withdrawal as Percent of Resources
  definition: Total annual freshwater withdrawals as a percentage of total renewable
    internal freshwater resources, indicating the intensity of water resource exploitation
  aliases: []
  construct_type: quantifiable
- id: water_stress_level
  display_name: Water Stress Level
  definition: Composite indicator of the ratio of total water withdrawals to available
    renewable surface and groundwater supplies, categorized from low to extremely
    high stress
  aliases: []
  construct_type: quantifiable
- id: agricultural_water_use_percent
  display_name: Agricultural Water Use Percentage
  definition: Share of total freshwater withdrawals used for agricultural irrigation
    and livestock production, expressed as a percentage of total withdrawals
  aliases: []
  construct_type: quantifiable
- id: water_use_efficiency
  display_name: Water Use Efficiency
  definition: Economic value added per unit of water withdrawn, measured in dollars
    of GDP per cubic meter of freshwater used, indicating how productively water resources
    are being utilized
  aliases: []
  construct_type: quantifiable
- id: renewable_freshwater_per_capita
  display_name: Renewable Freshwater Per Capita
  definition: Total internal renewable freshwater resources per person per year measured
    in cubic meters, reflecting natural water availability adjusted for population
    size
  aliases: []
  construct_type: quantifiable
- id: water_related_conflict_events
  display_name: Water-Related Conflict Events
  definition: Number of documented conflict events in which water scarcity, access
    to water resources, or water infrastructure were identified as contributing factors
    or triggers
  aliases: []
  construct_type: outcome
findings_detail:
- finding_text: Four billion people (two-thirds of the global population) experience
    severe water scarcity during at least one month of the year, with half a billion
    facing severe scarcity year-round
  construct_ids:
  - water_stress_level
  - renewable_freshwater_per_capita
  direction: positive
  effect_size: null
  confidence: strong
  method_used: spatial_hydrological_model
- finding_text: Agricultural irrigation accounts for approximately 70% of global freshwater
    withdrawals, making it by far the largest consumptive use of freshwater resources
    worldwide
  construct_ids:
  - agricultural_water_use_percent
  - freshwater_withdrawal_percent
  direction: positive
  effect_size: null
  confidence: strong
  method_used: global_water_balance
- finding_text: Water stress levels are positively associated with localized conflict
    events, particularly in arid and semi-arid regions where competition for scarce
    water resources intensifies during drought periods
  construct_ids:
  - water_stress_level
  - water_related_conflict_events
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: ols_regression
- finding_text: Nearly 80% of the worlds population lives in areas where threats to
    human water security or biodiversity exceed critical thresholds, with developing
    countries facing greatest vulnerability
  construct_ids:
  - water_stress_level
  - renewable_freshwater_per_capita
  direction: negative
  effect_size: null
  confidence: strong
  method_used: geospatial_analysis
- finding_text: Higher water use efficiency (GDP per cubic meter) is associated with
    lower freshwater withdrawal intensity, but gains are often offset by population
    and economic growth
  construct_ids:
  - water_use_efficiency
  - freshwater_withdrawal_percent
  direction: negative
  effect_size: null
  confidence: moderate
  method_used: ols_regression
propositions_detail: []
sources_detail:
- id: mekonnen_2016
  title: Four billion people facing severe water scarcity
  authors: Mekonnen, M.M. and Hoekstra, A.Y.
  year: 2016
  doi: 10.1126/sciadv.1500323
  source_type: journal_article
- id: vorosmarty_2010
  title: Global threats to human water security and river biodiversity
  authors: Vorosmarty, C.J., McIntyre, P.B., Gessner, M.O., et al.
  year: 2010
  doi: 10.1038/nature09440
  source_type: journal_article
- id: gain_2016
  title: Measuring global water security towards sustainable development goals
  authors: Gain, A.K., Giupponi, C., Wada, Y.
  year: 2016
  doi: null
  source_type: journal_article
playbooks_detail: []
download_url: https://pax-market.com/packs/water-stress-scarcity.pax.tar.gz
download_size: 2.7 KB
published_by: Praxis Agent
related_packs: []
pax_name: water-stress-scarcity
weight: 7974
---

**Domain:** Water Stress and Scarcity

Global freshwater scarcity, agricultural water use, and the water-energy-food nexus with implications for conflict and development

**Temporal scope:** 1990-present | **Population:** Water-stressed regions worldwide

## Key Findings

- Four billion people (two-thirds of the global population) experience severe water scarcity during at least one month of the year, with half a billion facing severe scarcity year-round *(positive, strong)*
- Agricultural irrigation accounts for approximately 70% of global freshwater withdrawals, making it by far the largest consumptive use of freshwater resources worldwide *(positive, strong)*
- Water stress levels are positively associated with localized conflict events, particularly in arid and semi-arid regions where competition for scarce water resources intensifies during drought periods *(positive, moderate)*
- Nearly 80% of the worlds population lives in areas where threats to human water security or biodiversity exceed critical thresholds, with developing countries facing greatest vulnerability *(negative, strong)*
- Higher water use efficiency (GDP per cubic meter) is associated with lower freshwater withdrawal intensity, but gains are often offset by population and economic growth *(negative, moderate)*

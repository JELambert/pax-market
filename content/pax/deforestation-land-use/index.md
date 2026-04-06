---
name: deforestation-land-use
title: Deforestation Land Use
version: 1.0.0
pax_type: topic
description: Causes and consequences of tropical deforestation, land use transitions,
  and their links to biodiversity loss and carbon emissions. Covers forest cover change
  dynamics, agricultural expansion as a deforestation driver, and CO2 contributions
  from land use change.
author: null
created: '2026-04-05'
license: null
tags:
- topic
- deforestation-land-use
constructs:
- forest_area_percent
- annual_deforestation_rate
- agricultural_land_share
- co2_from_land_use_change
- tree_cover_loss_hectares
- palm_oil_production
engines:
- ols_regression
- correlation_matrix
- random_forest
playbook_names:
- quick_start
construct_count: 6
finding_count: 5
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: deforestation_land_use
  display_name: Deforestation and Land Use Change
  description: Causes and consequences of tropical deforestation, land use transitions,
    and their links to biodiversity loss and carbon emissions
  research_questions: []
  temporal_scope: 2000-present
  population: Tropical and subtropical countries
  level_of_analysis: macro
constructs_detail:
- id: forest_area_percent
  display_name: Forest Area as Percentage of Land Area
  definition: The proportion of total land area covered by forest, measured as a percentage
    of the country's total land area
  aliases: []
  construct_type: quantifiable
- id: annual_deforestation_rate
  display_name: Annual Deforestation Rate
  definition: The rate of forest area loss per year, typically expressed as a percentage
    of remaining forest or in hectares per year
  aliases: []
  construct_type: quantifiable
- id: agricultural_land_share
  display_name: Agricultural Land Share
  definition: The proportion of total land area used for agriculture including cropland
    and pasture, expressed as a percentage
  aliases: []
  construct_type: quantifiable
- id: co2_from_land_use_change
  display_name: CO2 Emissions from Land Use Change
  definition: Carbon dioxide emissions resulting from changes in land use, particularly
    deforestation and forest degradation, measured in tonnes of CO2 equivalent
  aliases: []
  construct_type: outcome
- id: tree_cover_loss_hectares
  display_name: Tree Cover Loss in Hectares
  definition: Total area of tree cover removed or destroyed in a given year, measured
    in hectares using satellite-derived estimates
  aliases: []
  construct_type: quantifiable
- id: palm_oil_production
  display_name: Palm Oil Production Volume
  definition: Annual production volume of palm oil in metric tonnes, a key commodity
    crop linked to tropical deforestation in Southeast Asia and West Africa
  aliases: []
  construct_type: quantifiable
findings_detail:
- finding_text: Agricultural expansion is the primary driver of tropical deforestation,
    with more than 80% of new agricultural land in the tropics replacing forests during
    the 1980s and 1990s
  construct_ids:
  - agricultural_land_share
  - annual_deforestation_rate
  direction: positive
  effect_size: null
  confidence: strong
  method_used: remote_sensing_analysis
- finding_text: Global forest loss contributes approximately 10% of total anthropogenic
    CO2 emissions, making land use change the second largest source after fossil fuels
  construct_ids:
  - tree_cover_loss_hectares
  - co2_from_land_use_change
  direction: positive
  effect_size: null
  confidence: strong
  method_used: satellite_time_series
- finding_text: Commodity-driven deforestation accounts for 27% of global tree cover
    loss, with the remainder attributed to forestry, shifting agriculture, wildfire,
    and urbanization
  construct_ids:
  - tree_cover_loss_hectares
  - palm_oil_production
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: classification_analysis
- finding_text: Annual global tree cover loss increased by approximately 2,101 square
    kilometers per year from 2000 to 2012, with tropical regions showing the steepest
    increases
  construct_ids:
  - annual_deforestation_rate
  - tree_cover_loss_hectares
  direction: positive
  effect_size: null
  confidence: strong
  method_used: remote_sensing_analysis
- finding_text: Countries with higher forest area percentages experienced greater
    rates of agricultural land conversion, indicating that remaining forests face
    increasing pressure
  construct_ids:
  - forest_area_percent
  - agricultural_land_share
  direction: negative
  effect_size: null
  confidence: moderate
  method_used: ols_regression
propositions_detail: []
sources_detail:
- id: hansen_2013
  title: High-resolution global maps of 21st-century forest cover change
  authors: Hansen, M.C., Potapov, P.V., Moore, R., Hancher, M., et al.
  year: 2013
  doi: 10.1126/science.1244693
  source_type: journal_article
- id: gibbs_2010
  title: Tropical forests were the primary sources of new agricultural land in the
    1980s and 1990s
  authors: Gibbs, H.K., Ruesch, A.S., Achard, F., Clayton, M.K., et al.
  year: 2010
  doi: 10.1073/pnas.0910275107
  source_type: journal_article
- id: curtis_2018
  title: Classifying drivers of global forest loss
  authors: Curtis, P.G., Slay, C.M., Harris, N.L., Tyukavina, A., Hansen, M.C.
  year: 2018
  doi: 10.1126/science.aau3445
  source_type: journal_article
playbooks_detail: []
download_url: https://pax-market.com/pax/deforestation-land-use.pax.tar.gz
download_size: 2.7 KB
published_by: Praxis Agent
related_packs: []
pax_name: deforestation-land-use
weight: 7974
---

**Domain:** Deforestation and Land Use Change

Causes and consequences of tropical deforestation, land use transitions, and their links to biodiversity loss and carbon emissions

**Temporal scope:** 2000-present | **Population:** Tropical and subtropical countries

## Key Findings

- Agricultural expansion is the primary driver of tropical deforestation, with more than 80% of new agricultural land in the tropics replacing forests during the 1980s and 1990s *(positive, strong)*
- Global forest loss contributes approximately 10% of total anthropogenic CO2 emissions, making land use change the second largest source after fossil fuels *(positive, strong)*
- Commodity-driven deforestation accounts for 27% of global tree cover loss, with the remainder attributed to forestry, shifting agriculture, wildfire, and urbanization *(positive, moderate)*
- Annual global tree cover loss increased by approximately 2,101 square kilometers per year from 2000 to 2012, with tropical regions showing the steepest increases *(positive, strong)*
- Countries with higher forest area percentages experienced greater rates of agricultural land conversion, indicating that remaining forests face increasing pressure *(negative, moderate)*

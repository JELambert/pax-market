---
name: ocean-fisheries
title: Ocean Fisheries
version: 1.0.0
pax_type: topic
description: Global fisheries production, overfishing dynamics, aquaculture growth,
  and marine ecosystem health. Covers wild fish catch trends, stock depletion, marine
  protected area effectiveness, and the aquaculture transition.
author: null
created: '2026-04-05'
license: null
tags:
- topic
- ocean-fisheries
constructs:
- marine_fish_catch_tonnes
- overfished_stock_percentage
- aquaculture_production_tonnes
- marine_protected_area_coverage
- fish_consumption_per_capita_kg
- fishing_fleet_capacity
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
  id: ocean_fisheries
  display_name: Ocean Fisheries and Marine Resources
  description: Global fisheries production, overfishing dynamics, aquaculture growth,
    and marine ecosystem health
  research_questions: []
  temporal_scope: 1970-present
  population: Maritime nations
  level_of_analysis: macro
constructs_detail:
- id: marine_fish_catch_tonnes
  display_name: Marine Fish Catch in Tonnes
  definition: Total annual marine capture fisheries production measured in metric
    tonnes, including all marine fish, crustaceans, and mollusks harvested from ocean
    waters
  aliases: []
  construct_type: quantifiable
- id: overfished_stock_percentage
  display_name: Percentage of Overfished Stocks
  definition: Proportion of assessed fish stocks that are fished at biologically unsustainable
    levels, where current biomass is below the level that produces maximum sustainable
    yield
  aliases: []
  construct_type: quantifiable
- id: aquaculture_production_tonnes
  display_name: Aquaculture Production in Tonnes
  definition: Total annual production from aquaculture (farming of fish, crustaceans,
    mollusks, and aquatic plants) measured in metric tonnes
  aliases: []
  construct_type: quantifiable
- id: marine_protected_area_coverage
  display_name: Marine Protected Area Coverage
  definition: Proportion of a country's territorial waters designated as marine protected
    areas with restrictions on fishing and extractive activities, expressed as a percentage
  aliases: []
  construct_type: quantifiable
- id: fish_consumption_per_capita_kg
  display_name: Fish Consumption Per Capita
  definition: Average annual per capita consumption of fish and seafood products measured
    in kilograms of live weight equivalent per person
  aliases: []
  construct_type: quantifiable
- id: fishing_fleet_capacity
  display_name: Fishing Fleet Capacity
  definition: Total capacity of a country's fishing fleet measured in gross tonnage
    or number of motorized vessels, indicating fishing effort potential
  aliases: []
  construct_type: quantifiable
findings_detail:
- finding_text: The percentage of global fish stocks fished at biologically unsustainable
    levels increased from 10% in 1974 to 35.4% in 2019, indicating a long-term trend
    of increasing overexploitation
  construct_ids:
  - overfished_stock_percentage
  - marine_fish_catch_tonnes
  direction: positive
  effect_size: null
  confidence: strong
  method_used: stock_assessment
- finding_text: Marine protected areas with no-take restrictions show an average 670%
    increase in fish biomass within their borders compared to unprotected adjacent
    areas
  construct_ids:
  - marine_protected_area_coverage
  - marine_fish_catch_tonnes
  direction: positive
  effect_size: null
  confidence: strong
  method_used: meta_analysis
- finding_text: Global aquaculture production surpassed wild capture fisheries for
    the first time in 2020, producing 87.5 million tonnes compared to 78.8 million
    tonnes from marine and inland capture
  construct_ids:
  - aquaculture_production_tonnes
  - marine_fish_catch_tonnes
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: descriptive_statistics
- finding_text: Excess fishing fleet capacity is a primary driver of overfishing,
    with global fleet capacity estimated at 2-3 times the level needed to harvest
    current sustainable yields
  construct_ids:
  - fishing_fleet_capacity
  - overfished_stock_percentage
  direction: positive
  effect_size: null
  confidence: strong
  method_used: ols_regression
- finding_text: Rights-based fisheries management could rebuild stocks to levels producing
    98% of maximum sustainable yield, increasing global catch by 12% relative to business-as-usual
  construct_ids:
  - overfished_stock_percentage
  - marine_fish_catch_tonnes
  direction: conditional
  effect_size: null
  confidence: moderate
  method_used: bioeconomic_model
propositions_detail: []
sources_detail:
- id: pauly_2002
  title: Towards sustainability in world fisheries
  authors: Pauly, D., Christensen, V., Guenette, S., Pitcher, T.J., et al.
  year: 2002
  doi: 10.1038/nature01017
  source_type: journal_article
- id: fao_2022
  title: 'The State of World Fisheries and Aquaculture 2022: Towards Blue Transformation'
  authors: Food and Agriculture Organization of the United Nations
  year: 2022
  doi: null
  source_type: report
- id: costello_2016
  title: Global fishery prospects under contrasting management regimes
  authors: Costello, C., Ovando, D., Clavelle, T., Strauss, C.K., et al.
  year: 2016
  doi: 10.1073/pnas.1520420113
  source_type: journal_article
- id: lester_2009
  title: 'Biological effects within no-take marine reserves: a global synthesis'
  authors: Lester, S.E., Halpern, B.S., Grorud-Colvert, K., et al.
  year: 2009
  doi: 10.1111/j.1439-0485.2008.00260.x
  source_type: journal_article
playbooks_detail: []
download_url: https://pax-market.com/pax/ocean-fisheries.pax.tar.gz
download_size: 2.8 KB
published_by: Praxis Agent
related_packs: []
pax_name: ocean-fisheries
weight: 7974
---

**Domain:** Ocean Fisheries and Marine Resources

Global fisheries production, overfishing dynamics, aquaculture growth, and marine ecosystem health

**Temporal scope:** 1970-present | **Population:** Maritime nations

## Key Findings

- The percentage of global fish stocks fished at biologically unsustainable levels increased from 10% in 1974 to 35.4% in 2019, indicating a long-term trend of increasing overexploitation *(positive, strong)*
- Marine protected areas with no-take restrictions show an average 670% increase in fish biomass within their borders compared to unprotected adjacent areas *(positive, strong)*
- Global aquaculture production surpassed wild capture fisheries for the first time in 2020, producing 87.5 million tonnes compared to 78.8 million tonnes from marine and inland capture *(positive, moderate)*
- Excess fishing fleet capacity is a primary driver of overfishing, with global fleet capacity estimated at 2-3 times the level needed to harvest current sustainable yields *(positive, strong)*
- Rights-based fisheries management could rebuild stocks to levels producing 98% of maximum sustainable yield, increasing global catch by 12% relative to business-as-usual *(conditional, moderate)*

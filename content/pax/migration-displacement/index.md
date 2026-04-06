---
name: migration-displacement
title: Migration Displacement
version: 1.0.0
pax_type: topic
description: Drivers and consequences of international migration forced displacement
  and remittance flows for origin and host countries
author: null
created: '2026-04-05'
license: null
tags:
- topic
- migration-displacement
constructs:
- refugee_stock_per_capita
- net_migration_rate_per_1000
- remittance_inflows_gdp_pct
- asylum_applications_per_capita
- internally_displaced_persons_total
- conflict_battle_deaths
engines:
- ols_regression
- instrumental_variables
- difference_in_differences
playbook_names:
- quick_start
construct_count: 6
finding_count: 3
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: migration_displacement
  display_name: Migration and Forced Displacement
  description: Drivers and consequences of international migration forced displacement
    and remittance flows for origin and host countries
  research_questions: []
  temporal_scope: 1990-present
  population: Countries worldwide
  level_of_analysis: macro
constructs_detail:
- id: refugee_stock_per_capita
  display_name: Refugee Stock Per Capita
  definition: Number of refugees and people in refugee-like situations per 1000 population
    in the host country
  aliases: []
  construct_type: quantifiable
- id: net_migration_rate_per_1000
  display_name: Net Migration Rate
  definition: Difference between immigration and emigration per 1000 population per
    year measuring net population movement
  aliases: []
  construct_type: quantifiable
- id: remittance_inflows_gdp_pct
  display_name: Remittance Inflows as GDP Percentage
  definition: Personal remittances received as percentage of gross domestic product
    measuring diaspora financial transfers
  aliases: []
  construct_type: quantifiable
- id: asylum_applications_per_capita
  display_name: Asylum Applications Per Capita
  definition: Number of new asylum applications per 100000 host country population
    per year
  aliases: []
  construct_type: quantifiable
- id: internally_displaced_persons_total
  display_name: Internally Displaced Persons
  definition: Total number of persons displaced within their own country by conflict
    violence or disaster
  aliases: []
  construct_type: quantifiable
- id: conflict_battle_deaths
  display_name: Conflict Battle Deaths
  definition: Number of battle-related deaths from armed conflicts per 100000 population
    per year
  aliases: []
  construct_type: quantifiable
findings_detail:
- finding_text: Conflict intensity measured by battle deaths is strongly positively
    associated with both refugee outflows and internal displacement
  construct_ids:
  - conflict_battle_deaths
  - refugee_stock_per_capita
  - internally_displaced_persons_total
  direction: positive
  effect_size: null
  confidence: strong
  method_used: panel regression with country fixed effects
- finding_text: Remittance inflows are positively associated with household welfare
    and poverty reduction in origin countries through consumption smoothing and investment
  construct_ids:
  - remittance_inflows_gdp_pct
  direction: positive
  effect_size: null
  confidence: strong
  method_used: instrumental variable estimation
- finding_text: Forced displacement is negatively associated with host country GDP
    per capita in the short run but shows neutral to positive effects in the long
    run conditional on labor market integration
  construct_ids:
  - refugee_stock_per_capita
  direction: negative
  effect_size: null
  confidence: moderate
  method_used: difference-in-differences
propositions_detail: []
sources_detail:
- id: unhcr_2023
  title: UNHCR Global Trends Forced Displacement in 2023
  authors: United Nations High Commissioner for Refugees
  year: 2023
  doi: null
  source_type: report
- id: clemens_2011
  title: Economics and emigration trillion-dollar bills on the sidewalk
  authors: Clemens, Michael
  year: 2011
  doi: 10.1257/jep.25.3.83
  source_type: academic_paper
- id: yang_2011
  title: Migrant remittances
  authors: Yang, Dean
  year: 2011
  doi: 10.1146/annurev-economics-061109-080154
  source_type: academic_paper
- id: beine_2016
  title: Comparing immigration policies an overview from the IMPALA database
  authors: Beine, Michel, Boucher, Anna, Burgoon, Brian, Crock, Mary, Gest, Justin,
    Hiscox, Michael
  year: 2016
  doi: null
  source_type: academic_paper
playbooks_detail: []
download_url: https://pax-market.com/pax/migration-displacement.pax.tar.gz
download_size: 2.4 KB
published_by: Praxis Agent
related_packs: []
pax_name: migration-displacement
weight: 7974
---

**Domain:** Migration and Forced Displacement

Drivers and consequences of international migration forced displacement and remittance flows for origin and host countries

**Temporal scope:** 1990-present | **Population:** Countries worldwide

## Key Findings

- Conflict intensity measured by battle deaths is strongly positively associated with both refugee outflows and internal displacement *(positive, strong)*
- Remittance inflows are positively associated with household welfare and poverty reduction in origin countries through consumption smoothing and investment *(positive, strong)*
- Forced displacement is negatively associated with host country GDP per capita in the short run but shows neutral to positive effects in the long run conditional on labor market integration *(negative, moderate)*

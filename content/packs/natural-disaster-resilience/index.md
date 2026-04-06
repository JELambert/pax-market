---
name: natural-disaster-resilience
title: Natural Disaster Resilience
version: 1.0.0
pax_type: topic
description: How natural disasters affect mortality, economic output, and long-term
  development, and what factors build resilience. Covers disaster mortality trends,
  economic damages, early warning systems, and the relationship between development
  and disaster vulnerability.
author: null
created: '2026-04-05'
license: null
tags:
- topic
- disaster-resilience
constructs:
- disaster_economic_damage_gdp
- disaster_event_frequency
- early_warning_system_coverage
- disaster_preparedness_spending
- disaster_deaths_annual
- infrastructure_resilience_index
engines:
- ols_regression
- poisson_regression
- correlation_matrix
playbook_names:
- quick_start
construct_count: 6
finding_count: 5
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: disaster_resilience
  display_name: Natural Disaster Impacts and Resilience
  description: How natural disasters affect mortality, economic output, and long-term
    development, and what factors build resilience
  research_questions: []
  temporal_scope: 1970-present
  population: Countries worldwide
  level_of_analysis: macro
constructs_detail:
- id: disaster_economic_damage_gdp
  display_name: Disaster Economic Damage as Share of GDP
  definition: Total direct economic losses from natural disasters expressed as a percentage
    of national gross domestic product, including infrastructure damage and crop losses
  aliases: []
  construct_type: outcome
- id: disaster_event_frequency
  display_name: Disaster Event Frequency
  definition: Number of recorded natural disaster events per year meeting minimum
    thresholds for deaths, affected population, or economic damage, tracked through
    EM-DAT database
  aliases: []
  construct_type: quantifiable
- id: early_warning_system_coverage
  display_name: Early Warning System Coverage
  definition: Proportion of population covered by multi-hazard early warning systems
    that provide timely alerts for impending natural disasters
  aliases: []
  construct_type: quantifiable
- id: disaster_preparedness_spending
  display_name: Disaster Preparedness Spending
  definition: Government expenditure on disaster risk reduction and preparedness measures
    as a share of total government spending or GDP, including early warning, building
    codes, and emergency response capacity
  aliases: []
  construct_type: quantifiable
- id: disaster_deaths_annual
  display_name: Annual Deaths from Natural Disasters
  definition: Total number of people killed annually as a direct result of natural
    disasters including earthquakes, floods, storms, droughts, and volcanic eruptions
  aliases: []
  construct_type: outcome
- id: infrastructure_resilience_index
  display_name: Infrastructure Resilience Index
  definition: Composite measure of the capacity of built infrastructure to withstand
    and recover from natural hazards, incorporating building codes, structural standards,
    and redundancy
  aliases: []
  construct_type: quantifiable
findings_detail:
- finding_text: 'GDP per capita is negatively associated with disaster deaths: richer
    countries experience significantly lower mortality from comparable natural disasters
    due to better infrastructure, institutions, and emergency response'
  construct_ids:
  - disaster_deaths_annual
  - infrastructure_resilience_index
  direction: negative
  effect_size: null
  confidence: strong
  method_used: ols_regression
- finding_text: Multi-hazard early warning systems reduce disaster mortality by 50-80%
    when coupled with effective response protocols and public education on protective
    actions
  construct_ids:
  - early_warning_system_coverage
  - disaster_deaths_annual
  direction: negative
  effect_size: null
  confidence: strong
  method_used: comparative_case_study
- finding_text: Only the most catastrophic natural disasters (top 1% by severity)
    show significant negative effects on long-run GDP growth; moderate disasters have
    no detectable long-term economic impact
  construct_ids:
  - disaster_economic_damage_gdp
  - disaster_event_frequency
  direction: conditional
  effect_size: null
  confidence: moderate
  method_used: synthetic_control
- finding_text: Democratic institutions and higher government quality are associated
    with lower disaster mortality independent of income, suggesting governance mediates
    disaster resilience
  construct_ids:
  - disaster_preparedness_spending
  - disaster_deaths_annual
  direction: negative
  effect_size: null
  confidence: moderate
  method_used: ols_regression
- finding_text: The frequency of recorded natural disaster events has increased over
    time, but deaths per disaster event have declined substantially, reflecting improved
    warning systems and preparedness
  construct_ids:
  - disaster_event_frequency
  - disaster_deaths_annual
  direction: conditional
  effect_size: null
  confidence: moderate
  method_used: descriptive_statistics
propositions_detail: []
sources_detail:
- id: kahn_2005
  title: 'The Death Toll from Natural Disasters: The Role of Income, Geography, and
    Institutions'
  authors: Kahn, M.E.
  year: 2005
  doi: 10.1162/0034653053970339
  source_type: journal_article
- id: cavallo_2013
  title: Catastrophic Natural Disasters and Economic Growth
  authors: Cavallo, E., Galiani, S., Noy, I., Pantano, J.
  year: 2013
  doi: 10.1162/REST_a_00413
  source_type: journal_article
- id: hallegatte_2017
  title: 'Unbreakable: Building the Resilience of the Poor in the Face of Natural
    Disasters'
  authors: Hallegatte, S., Vogt-Schilb, A., Bangalore, M., Rozenberg, J.
  year: 2017
  doi: null
  source_type: book
- id: emdat_2023
  title: 'EM-DAT: The International Disaster Database'
  authors: Centre for Research on the Epidemiology of Disasters (CRED)
  year: 2023
  doi: null
  source_type: dataset
playbooks_detail: []
download_url: https://pax-market.com/packs/natural-disaster-resilience.pax.tar.gz
download_size: 2.9 KB
published_by: Praxis Agent
related_packs: []
pax_name: natural-disaster-resilience
weight: 7974
---

**Domain:** Natural Disaster Impacts and Resilience

How natural disasters affect mortality, economic output, and long-term development, and what factors build resilience

**Temporal scope:** 1970-present | **Population:** Countries worldwide

## Key Findings

- GDP per capita is negatively associated with disaster deaths: richer countries experience significantly lower mortality from comparable natural disasters due to better infrastructure, institutions, and emergency response *(negative, strong)*
- Multi-hazard early warning systems reduce disaster mortality by 50-80% when coupled with effective response protocols and public education on protective actions *(negative, strong)*
- Only the most catastrophic natural disasters (top 1% by severity) show significant negative effects on long-run GDP growth; moderate disasters have no detectable long-term economic impact *(conditional, moderate)*
- Democratic institutions and higher government quality are associated with lower disaster mortality independent of income, suggesting governance mediates disaster resilience *(negative, moderate)*
- The frequency of recorded natural disaster events has increased over time, but deaths per disaster event have declined substantially, reflecting improved warning systems and preparedness *(conditional, moderate)*

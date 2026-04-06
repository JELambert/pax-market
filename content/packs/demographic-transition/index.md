---
name: demographic-transition
title: Demographic Transition
version: 1.0.0
pax_type: topic
description: How societies move from high birth and death rates to low birth and death
  rates, examining the demographic dividend, urbanization effects, and the relationship
  between mortality decline and fertility transition.
author: null
created: '2026-04-05'
license: null
tags:
- topic
- demographic-transition
constructs:
- population_growth_rate
- life_expectancy_at_birth
- fertility_rate
- dependency_ratio
- urbanization_rate
- infant_mortality_rate
engines:
- ols_regression
- correlation_matrix
playbook_names:
- quick_start
construct_count: 6
finding_count: 0
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: demographic_transition
  display_name: Demographic Transition Theory
  description: How societies move from high birth/death rates to low birth/death rates
    and the economic consequences
  research_questions: []
  temporal_scope: 1950-present
  population: Countries worldwide
  level_of_analysis: macro
constructs_detail:
- id: population_growth_rate
  display_name: Population Growth Rate
  definition: Annual rate of change in total population, including natural increase
    and net migration. In growth models, higher population growth dilutes per-capita
    capital.
  aliases: []
  construct_type: quantifiable
- id: life_expectancy_at_birth
  display_name: Life Expectancy at Birth
  definition: The average number of years a newborn is expected to live if current
    mortality rates remain constant, reflecting overall population health and development
  aliases: []
  construct_type: quantifiable
- id: fertility_rate
  display_name: Total Fertility Rate
  definition: The average number of children a woman would bear over her lifetime
    if current age-specific fertility rates remained constant throughout her childbearing
    years
  aliases: []
  construct_type: quantifiable
- id: dependency_ratio
  display_name: Age Dependency Ratio
  definition: The ratio of dependents (people younger than 15 or older than 64) to
    the working-age population (ages 15-64), expressed as a percentage
  aliases: []
  construct_type: quantifiable
- id: urbanization_rate
  display_name: Urbanization Rate
  definition: The percentage of a country's total population residing in urban areas
    as defined by national statistical offices, reflecting structural economic transformation
  aliases: []
  construct_type: quantifiable
- id: infant_mortality_rate
  display_name: Infant Mortality Rate
  definition: The number of deaths of infants under one year of age per 1,000 live
    births in a given year, a sensitive indicator of population health and development
  aliases: []
  construct_type: outcome
findings_detail: []
propositions_detail: []
sources_detail:
- id: lee_2003
  title: 'The Demographic Transition: Three Centuries of Fundamental Change'
  authors: Ronald Lee
  year: 2003
  doi: 10.1257/089533003772034943
  source_type: journal_article
- id: galor_weil_2000
  title: 'Population, Technology, and Growth: From Malthusian Stagnation to the Demographic
    Transition and Beyond'
  authors: Oded Galor, David N. Weil
  year: 2000
  doi: 10.1257/aer.90.4.806
  source_type: journal_article
- id: bloom_2003
  title: 'The Demographic Dividend: A New Perspective on the Economic Consequences
    of Population Change'
  authors: David Bloom, David Canning, Jaypee Sevilla
  year: 2003
  doi: 10.7249/MR1274
  source_type: journal_article
- id: dyson_2010
  title: 'Population and Development: The Demographic Transition'
  authors: Tim Dyson
  year: 2010
  doi: null
  source_type: book
playbooks_detail: []
download_url: https://pax-market.com/packs/demographic-transition.pax.tar.gz
download_size: 2.1 KB
published_by: Praxis Agent
related_packs:
- economic-growth-panel
pax_name: demographic-transition
weight: 7974
---

**Domain:** Demographic Transition Theory

How societies move from high birth/death rates to low birth/death rates and the economic consequences

**Temporal scope:** 1950-present | **Population:** Countries worldwide

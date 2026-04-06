---
name: economic-growth-panel
title: Economic Growth Panel
version: 1.0.0
pax_type: field
description: Determinants of long-run economic growth including physical capital accumulation,
  human capital, population growth, and total factor productivity. Built on Solow
  (1956), Barro (1991), and Mankiw-Romer-Weil (1992).
author: ''
created: ''
license: ''
tags:
- field
constructs:
- gdp_per_capita
- physical_capital
- human_capital
- population_growth_rate
- total_factor_productivity
- convergence_rate
engines:
- ols_regression
- ridge_regression
- correlation_matrix
- instrumental_variables
playbook_names:
- quick_start
construct_count: 6
finding_count: 0
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: economic_growth
  display_name: Economic Growth & Productivity
  description: Determinants of long-run economic growth including physical capital,
    human capital, technology, and institutions
  research_questions: []
  temporal_scope: 1950-present
  population: Countries worldwide
  level_of_analysis: macro
constructs_detail:
- id: gdp_per_capita
  display_name: GDP Per Capita
  definition: Total economic output divided by population, measured in constant purchasing
    power parity dollars. The standard measure of average material living standards
    across countries.
  aliases: []
  construct_type: quantifiable
- id: physical_capital
  display_name: Physical Capital Accumulation
  definition: The stock of produced means of production including machinery, equipment,
    structures, and infrastructure. Accumulated through investment (savings) and depreciated
    over time.
  aliases: []
  construct_type: quantifiable
- id: human_capital
  display_name: Human Capital
  definition: The stock of knowledge, skills, and health embodied in the labor force.
    Accumulated through education, training, and health investment.
  aliases: []
  construct_type: quantifiable
- id: population_growth_rate
  display_name: Population Growth Rate
  definition: Annual rate of change in total population, including natural increase
    and net migration. In growth models, higher population growth dilutes per-capita
    capital.
  aliases: []
  construct_type: quantifiable
- id: total_factor_productivity
  display_name: Total Factor Productivity
  definition: The portion of output not explained by the quantity of inputs used in
    production. Reflects technological progress, efficiency, and institutional quality.
  aliases: []
  construct_type: quantifiable
- id: convergence_rate
  display_name: Convergence Rate
  definition: The speed at which poorer economies catch up to richer ones in terms
    of per-capita income, conditional on structural characteristics.
  aliases: []
  construct_type: quantifiable
findings_detail: []
propositions_detail: []
sources_detail: []
playbooks_detail: []
download_url: https://pax-market.com/packs/economic-growth-panel.pax.tar.gz
download_size: 1.6 KB
published_by: Praxis Agent
related_packs:
- demographic-transition
pax_name: economic-growth-panel
weight: 10000
---

**Domain:** Economic Growth & Productivity

Determinants of long-run economic growth including physical capital, human capital, technology, and institutions

**Temporal scope:** 1950-present | **Population:** Countries worldwide

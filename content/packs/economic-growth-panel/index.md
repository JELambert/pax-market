---
title: Economic Growth Panel
pax_name: economic-growth-panel
version: 1.0.0
pax_type: field
description: Determinants of long-run economic growth including physical capital accumulation,
  human capital, population growth, and total factor productivity. Built on Solow
  (1956), Barro (1991), and Mankiw-Romer-Weil (1992).
author: Josh Lambert (stress test)
created: '2026-04-05'
license: ''
tags:
- field
- economic-growth
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
finding_count: 4
proposition_count: 0
has_playbooks: true
has_data_sources: true
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
  definition: Total economic output divided by population in PPP dollars
  aliases: []
  construct_type: quantifiable
- id: physical_capital
  display_name: Physical Capital Accumulation
  definition: Stock of produced means of production — investment share of GDP
  aliases: []
  construct_type: quantifiable
- id: human_capital
  display_name: Human Capital
  definition: Stock of knowledge and skills embodied in the labor force
  aliases: []
  construct_type: quantifiable
- id: population_growth_rate
  display_name: Population Growth Rate
  definition: Annual rate of change in total population
  aliases: []
  construct_type: quantifiable
- id: total_factor_productivity
  display_name: Total Factor Productivity
  definition: Portion of output not explained by quantity of inputs — technological
    progress
  aliases: []
  construct_type: quantifiable
- id: convergence_rate
  display_name: Convergence Rate
  definition: Speed at which poorer economies catch up to richer ones
  aliases: []
  construct_type: quantifiable
findings_detail:
- finding_text: Long-run GDP per capita is determined by savings rate and population
    growth given diminishing returns to capital
  construct_ids:
  - gdp_per_capita
  - physical_capital
  - population_growth_rate
  direction: positive
  effect_size: ''
  confidence: foundational
  method_used: Mathematical growth model
  finding_type: ''
  evidence_type: ''
- finding_text: TFP growth is the only source of sustained long-run growth in per-capita
    output
  construct_ids:
  - total_factor_productivity
  - gdp_per_capita
  direction: positive
  effect_size: ''
  confidence: foundational
  method_used: ''
  finding_type: ''
  evidence_type: ''
- finding_text: Augmented Solow model with human capital explains 80% of cross-country
    income variation
  construct_ids:
  - gdp_per_capita
  - human_capital
  - physical_capital
  direction: positive
  effect_size: ''
  confidence: strong
  method_used: OLS cross-country, N=98
  finding_type: ''
  evidence_type: ''
- finding_text: Conditional convergence at approximately 2% per year across country
    samples
  construct_ids:
  - convergence_rate
  - gdp_per_capita
  direction: positive
  effect_size: ''
  confidence: strong
  method_used: OLS cross-country, N=98
  finding_type: ''
  evidence_type: ''
propositions_detail: []
sources_detail:
- id: solow_1956
  title: A Contribution to the Theory of Economic Growth
  authors: Robert M. Solow
  year: 1956
  doi: 10.2307/1884513
  source_type: journal_article
- id: barro_1991
  title: Economic Growth in a Cross Section of Countries
  authors: Robert J. Barro
  year: 1991
  doi: 10.2307/2937943
  source_type: journal_article
- id: mankiw_romer_weil_1992
  title: A Contribution to the Empirics of Economic Growth
  authors: N. Gregory Mankiw, David Romer, David N. Weil
  year: 1992
  doi: 10.2307/2118477
  source_type: journal_article
playbooks_detail:
- id: quick_start
  display_name: Quick Start — Economic Growth
  description: Basic analysis workflow for the economic_growth domain.
  estimated_runtime: 1–3 minutes
  step_count: 1
  engines_used:
  - correlation_matrix
download_url: /packs/economic-growth-panel.pax.tar.gz
download_size: 2.4 KB
weight: 7974
related_packs: []
---

**Domain:** Economic Growth & Productivity

Determinants of long-run economic growth including physical capital, human capital, technology, and institutions

**Temporal scope:** 1950-present | **Population:** Countries worldwide

## Key Findings

- Long-run GDP per capita is determined by savings rate and population growth given diminishing returns to capital *(positive, foundational)*
- TFP growth is the only source of sustained long-run growth in per-capita output *(positive, foundational)*
- Augmented Solow model with human capital explains 80% of cross-country income variation *(positive, strong)*
- Conditional convergence at approximately 2% per year across country samples *(positive, strong)*

## Sources

- Robert M. Solow (1956). *A Contribution to the Theory of Economic Growth*. DOI: 10.2307/1884513
- Robert J. Barro (1991). *Economic Growth in a Cross Section of Countries*. DOI: 10.2307/2937943
- N. Gregory Mankiw, David Romer, David N. Weil (1992). *A Contribution to the Empirics of Economic Growth*. DOI: 10.2307/2118477

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
findings:
- solow_1956_0
- solow_1956_1
- mankiw_romer_weil_1992_2
- barro_1991_3
engines:
- ols_regression
- ridge_regression
- correlation_matrix
- instrumental_variables
playbooks:
- quick_start
propositions: []
construct_count: 6
finding_count: 4
proposition_count: 0
has_playbooks: true
has_data_sources: true
download_url: /packs/economic-growth-panel.pax.tar.gz
download_size: 2.4 KB
weight: 7974
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

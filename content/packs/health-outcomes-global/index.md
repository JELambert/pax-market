---
title: Health Outcomes Global
pax_name: health-outcomes-global
version: 1.0.0
pax_type: field
description: Relationship between health spending and population health outcomes including
  life expectancy, infant mortality, and the contested role of public vs private expenditure.
  Built on WHO Commission (2001), Filmer & Pritchett (1999), and Cutler, Deaton &
  Lleras-Muney (2006).
author: Josh Lambert (stress test)
created: '2026-04-05'
license: ''
tags:
- field
- health-expenditure-outcomes
constructs:
- health_expenditure_per_capita
- life_expectancy
- infant_mortality
findings:
- who_commission_2001_0
- filmer_pritchett_1999_1
- cutler_deaton_lleras_muney_2006_2
engines:
- ols_regression
- correlation_matrix
- meta_analysis
playbooks:
- quick_start
propositions: []
construct_count: 3
finding_count: 3
proposition_count: 0
has_playbooks: true
has_data_sources: true
download_url: /packs/health-outcomes-global.pax.tar.gz
download_size: 2.2 KB
weight: 7974
---

**Domain:** Health Expenditure & Outcomes

Relationship between health spending and population health outcomes

**Temporal scope:** 1960-present | **Population:** Countries worldwide

## Key Findings

- Health spending has strong positive effect on life expectancy — each 10% increase associated with ~0.3 year gain *(positive, moderate)*
- Public health spending has NO significant effect on child mortality after controlling for income and education *(null, strong)*
- Returns to health spending exhibit strong diminishing returns at high income levels *(conditional, moderate)*

## Sources

- WHO Commission (2001). *Macroeconomics and Health: Investing in Health for Economic Development*.
- Deon Filmer, Lant Pritchett (1999). *The Impact of Public Spending on Health: Does Money Matter?*.
- David Cutler, Angus Deaton, Adriana Lleras-Muney (2006). *The Determinants of Mortality*.

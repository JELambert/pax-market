---
name: income-inequality-gini
title: Income Inequality Gini
version: 1.0.0
pax_type: topic
description: Causes and consequences of income and wealth inequality including determinants
  and effects on growth and social outcomes
author: null
created: '2026-04-05'
license: null
tags:
- topic
- income-inequality
constructs:
- gini_coefficient_income
- income_share_top_10_pct
- poverty_headcount_215_ppp
- intergenerational_earnings_elasticity
- wealth_share_top_1_pct
- labor_income_share_gdp
engines:
- ols_regression
- correlation_matrix
- panel_regression
playbook_names:
- quick_start
construct_count: 6
finding_count: 3
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: income_inequality
  display_name: Income Inequality
  description: Measurement, determinants, and consequences of income and wealth inequality
    within and between countries
  research_questions: []
  temporal_scope: null
  population: null
  level_of_analysis: macro
constructs_detail:
- id: gini_coefficient_income
  display_name: Gini Coefficient Income
  definition: Index from 0 to 1 measuring the degree of inequality in national income
    distribution where 0 is perfect equality
  aliases: []
  construct_type: quantifiable
- id: income_share_top_10_pct
  display_name: Income Share Top 10 Percent
  definition: Share of pre-tax national income accruing to the top 10 percent of earners
    in the income distribution
  aliases: []
  construct_type: quantifiable
- id: poverty_headcount_215_ppp
  display_name: Poverty Headcount 2.15 PPP
  definition: Percentage of population living below international poverty line of
    2.15 dollars per day at purchasing power parity
  aliases: []
  construct_type: quantifiable
- id: intergenerational_earnings_elasticity
  display_name: Intergenerational Earnings Elasticity
  definition: Correlation between parent and child income rankings measuring the degree
    of social mobility across generations
  aliases: []
  construct_type: quantifiable
- id: wealth_share_top_1_pct
  display_name: Wealth Share Top 1 Percent
  definition: Share of total national wealth held by the wealthiest 1 percent of the
    adult population
  aliases: []
  construct_type: quantifiable
- id: labor_income_share_gdp
  display_name: Labor Income Share of GDP
  definition: Total employee compensation as share of gross domestic product measuring
    the split between labor and capital
  aliases: []
  construct_type: quantifiable
findings_detail:
- finding_text: High inequality with Gini above 0.45 is negatively associated with
    the duration of economic growth spells
  construct_ids:
  - gini_coefficient_income
  direction: negative
  effect_size: null
  confidence: moderate
  method_used: growth spell duration analysis
- finding_text: Intergenerational mobility is negatively correlated with inequality
    known as the Great Gatsby Curve showing that more unequal societies have less
    mobility
  construct_ids:
  - intergenerational_earnings_elasticity
  - gini_coefficient_income
  direction: negative
  effect_size: null
  confidence: strong
  method_used: cross-country correlation analysis
- finding_text: Top income shares have risen in most OECD countries since 1980 driven
    by capital income growth and executive compensation increases
  construct_ids:
  - income_share_top_10_pct
  - wealth_share_top_1_pct
  direction: positive
  effect_size: null
  confidence: strong
  method_used: historical tax record analysis
propositions_detail: []
sources_detail:
- id: piketty_2014
  title: Capital in the Twenty-First Century
  authors: Piketty, Thomas
  year: 2014
  doi: null
  source_type: book
- id: chetty_2014
  title: Where is the land of opportunity the geography of intergenerational mobility
    in the United States
  authors: Chetty, Raj, Hendren, Nathaniel, Kline, Patrick, Saez, Emmanuel
  year: 2014
  doi: 10.1093/qje/qju022
  source_type: academic_paper
- id: ostry_2014
  title: Redistribution inequality and growth
  authors: Ostry, Jonathan, Berg, Andrew, Tsangarides, Charalambos
  year: 2014
  doi: null
  source_type: academic_paper
- id: atkinson_2011
  title: Top incomes in the long run of history
  authors: Atkinson, Anthony, Piketty, Thomas, Saez, Emmanuel
  year: 2011
  doi: 10.1257/jel.49.1.3
  source_type: academic_paper
playbooks_detail: []
download_url: https://pax-market.com/pax/income-inequality-gini.pax.tar.gz
download_size: 2.4 KB
published_by: Praxis Agent
related_packs: []
pax_name: income-inequality-gini
weight: 7974
---

**Domain:** Income Inequality

Measurement, determinants, and consequences of income and wealth inequality within and between countries

## Key Findings

- High inequality with Gini above 0.45 is negatively associated with the duration of economic growth spells *(negative, moderate)*
- Intergenerational mobility is negatively correlated with inequality known as the Great Gatsby Curve showing that more unequal societies have less mobility *(negative, strong)*
- Top income shares have risen in most OECD countries since 1980 driven by capital income growth and executive compensation increases *(positive, strong)*

---
name: inflation-monetary-policy
title: Inflation Monetary Policy
version: 1.0.0
pax_type: topic
description: How central bank policies inflation targeting and monetary frameworks
  affect price stability output growth and financial conditions
author: null
created: '2026-04-05'
license: null
tags:
- topic
- monetary-policy
constructs:
- consumer_price_inflation_annual
- central_bank_policy_rate
- broad_money_growth_m2
- exchange_rate_volatility_neer
- real_interest_rate_lending
- inflation_expectations_12m
engines:
- ols_regression
- var_model
- cointegration_analysis
playbook_names:
- quick_start
construct_count: 6
finding_count: 4
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: monetary_policy
  display_name: Inflation and Monetary Policy
  description: How central bank policies inflation targeting and monetary frameworks
    affect price stability output growth and financial conditions
  research_questions: []
  temporal_scope: 1970-present
  population: Countries worldwide
  level_of_analysis: macro
constructs_detail:
- id: consumer_price_inflation_annual
  display_name: Consumer Price Inflation Annual
  definition: Annual percentage change in consumer price index measuring the average
    price change of a basket of goods and services
  aliases: []
  construct_type: quantifiable
- id: central_bank_policy_rate
  display_name: Central Bank Policy Rate
  definition: Benchmark interest rate set by central bank for interbank lending or
    monetary policy operations
  aliases: []
  construct_type: quantifiable
- id: broad_money_growth_m2
  display_name: Broad Money Growth M2
  definition: Annual percentage change in M2 money supply including currency demand
    deposits savings deposits and money market funds
  aliases: []
  construct_type: quantifiable
- id: exchange_rate_volatility_neer
  display_name: Exchange Rate Volatility NEER
  definition: Standard deviation of monthly nominal effective exchange rate changes
    over a rolling 12-month window
  aliases: []
  construct_type: quantifiable
- id: real_interest_rate_lending
  display_name: Real Interest Rate Lending
  definition: Nominal lending interest rate adjusted for inflation using the GDP deflator
    measuring true cost of borrowing
  aliases: []
  construct_type: quantifiable
- id: inflation_expectations_12m
  display_name: Inflation Expectations 12 Month
  definition: Median expected inflation rate over next 12 months from consumer surveys
    or professional forecaster surveys
  aliases: []
  construct_type: quantifiable
findings_detail:
- finding_text: Inflation targeting regimes reduce inflation volatility by approximately
    1 to 2 percentage points compared to non-targeting regimes
  construct_ids:
  - consumer_price_inflation_annual
  - central_bank_policy_rate
  direction: negative
  effect_size: null
  confidence: moderate
  method_used: difference-in-differences with matching
- finding_text: Money supply growth is positively associated with inflation in the
    long run consistent with the quantity theory of money
  construct_ids:
  - broad_money_growth_m2
  - consumer_price_inflation_annual
  direction: positive
  effect_size: null
  confidence: strong
  method_used: long-run panel cointegration
- finding_text: Central bank independence is negatively associated with average inflation
    rates across countries controlling for fiscal and structural factors
  construct_ids:
  - central_bank_policy_rate
  - consumer_price_inflation_annual
  direction: negative
  effect_size: null
  confidence: strong
  method_used: cross-country regression
- finding_text: Exchange rate volatility is negatively associated with trade and investment
    flows particularly in emerging market economies
  construct_ids:
  - exchange_rate_volatility_neer
  direction: negative
  effect_size: null
  confidence: moderate
  method_used: gravity model estimation
propositions_detail: []
sources_detail:
- id: taylor_1993
  title: Discretion versus policy rules in practice
  authors: Taylor, John
  year: 1993
  doi: 10.1016/0167-2231(93)90009-L
  source_type: academic_paper
- id: romer_romer_2004
  title: A new measure of monetary shocks derivation and implications
  authors: Romer, Christina, Romer, David
  year: 2004
  doi: 10.1257/0002828042002651
  source_type: academic_paper
- id: ball_sheridan_2005
  title: Does inflation targeting matter
  authors: Ball, Laurence, Sheridan, Niamh
  year: 2005
  doi: null
  source_type: academic_paper
- id: friedman_schwartz_1963
  title: A monetary history of the United States 1867 to 1960
  authors: Friedman, Milton, Schwartz, Anna
  year: 1963
  doi: null
  source_type: book
playbooks_detail: []
download_url: https://pax-market.com/pax/inflation-monetary-policy.pax.tar.gz
download_size: 2.5 KB
published_by: Praxis Agent
related_packs: []
pax_name: inflation-monetary-policy
weight: 7974
---

**Domain:** Inflation and Monetary Policy

How central bank policies inflation targeting and monetary frameworks affect price stability output growth and financial conditions

**Temporal scope:** 1970-present | **Population:** Countries worldwide

## Key Findings

- Inflation targeting regimes reduce inflation volatility by approximately 1 to 2 percentage points compared to non-targeting regimes *(negative, moderate)*
- Money supply growth is positively associated with inflation in the long run consistent with the quantity theory of money *(positive, strong)*
- Central bank independence is negatively associated with average inflation rates across countries controlling for fiscal and structural factors *(negative, strong)*
- Exchange rate volatility is negatively associated with trade and investment flows particularly in emerging market economies *(negative, moderate)*

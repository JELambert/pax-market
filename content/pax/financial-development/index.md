---
name: financial-development
title: Financial Development
version: 1.0.0
pax_type: topic
description: How financial deepening banking access and inclusive finance affect economic
  growth poverty reduction and household welfare
author: null
created: '2026-04-05'
license: null
tags:
- topic
- financial-development
constructs:
- stock_market_capitalization_gdp
- domestic_credit_private_gdp
- bank_account_ownership_adult
- financial_inclusion_composite
- mobile_money_accounts_per_1000
- non_performing_loan_ratio_pct
engines:
- ols_regression
- instrumental_variables
- panel_regression
playbook_names:
- quick_start
construct_count: 6
finding_count: 8
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: financial_development
  display_name: Financial Development and Inclusion
  description: How financial deepening banking access and inclusive finance affect
    economic growth poverty reduction and household welfare
  research_questions: []
  temporal_scope: 1990-present
  population: Countries worldwide
  level_of_analysis: macro
constructs_detail:
- id: stock_market_capitalization_gdp
  display_name: Stock Market Capitalization / GDP
  definition: Total market capitalization of listed companies as a share of GDP, measuring
    equity market development.
  aliases: []
  construct_type: quantifiable
- id: domestic_credit_private_gdp
  display_name: Domestic Credit to Private Sector
  definition: Domestic credit to private sector by banks as percentage of GDP measuring
    financial depth and intermediation
  aliases: []
  construct_type: quantifiable
- id: bank_account_ownership_adult
  display_name: Bank Account Ownership Adult
  definition: Percentage of adults age 15 plus with an account at a financial institution
    or mobile money provider
  aliases: []
  construct_type: quantifiable
- id: financial_inclusion_composite
  display_name: Financial Inclusion Composite Index
  definition: Composite index measuring access to and usage of formal financial services
    across multiple dimensions including accounts savings and credit
  aliases: []
  construct_type: quantifiable
- id: mobile_money_accounts_per_1000
  display_name: Mobile Money Accounts Per 1000
  definition: Registered mobile money accounts per 1000 adult population measuring
    digital financial service penetration
  aliases: []
  construct_type: quantifiable
- id: non_performing_loan_ratio_pct
  display_name: Non-Performing Loan Ratio
  definition: Value of non-performing loans as percentage of total gross loans in
    the banking sector measuring credit quality
  aliases: []
  construct_type: quantifiable
findings_detail:
- finding_text: Financial depth (private credit/GDP) strongly predicts subsequent
    economic growth (beta=0.03, p<.01) even after controlling for other standard growth
    determinants.
  construct_ids:
  - private_credit_gdp
  - gdp_growth_financial
  direction: positive
  effect_size: β=0.03, p<.01
  confidence: strong
  method_used: cross-country growth regression with initial financial depth
- finding_text: Systemic banking crises cause GDP losses of 5-10%, partially offsetting
    the long-run growth benefits of financial deepening.
  construct_ids:
  - banking_crisis_indicator
  - gdp_growth_financial
  - financial_depth_index
  direction: negative
  effect_size: 5-10% GDP loss per banking crisis
  confidence: strong
  method_used: event study of banking crisis episodes
- finding_text: 'The finance-growth relationship is not merely correlational: initial
    financial depth in 1960 predicts growth over the subsequent 30 years, suggesting
    a causal channel from finance to growth.'
  construct_ids:
  - private_credit_gdp
  - gdp_growth_financial
  direction: positive
  effect_size: null
  confidence: strong
  method_used: lagged initial conditions growth regression (1960-1989)
- finding_text: Legal origin (common law vs civil law) serves as a valid instrument
    for financial development, with common law countries developing deeper financial
    markets on average.
  construct_ids:
  - financial_depth_index
  - private_credit_gdp
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: instrumental variables with legal origin as instrument
- finding_text: Financial depth measured by private credit to GDP is positively associated
    with GDP growth but the relationship flattens above approximately 100 percent
    credit-to-GDP ratio
  construct_ids:
  - domestic_credit_private_gdp
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: panel regression with threshold effects
- finding_text: Mobile money adoption reduced poverty by approximately 2 percent in
    Kenya through improved risk sharing and consumption smoothing
  construct_ids:
  - mobile_money_accounts_per_1000
  direction: negative
  effect_size: null
  confidence: strong
  method_used: instrumental variable regression
- finding_text: Bank account ownership is positively associated with household savings
    rates across developing countries
  construct_ids:
  - bank_account_ownership_adult
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: cross-country household survey analysis
- finding_text: High non-performing loan ratios are negatively associated with credit
    growth and economic recovery in post-crisis periods
  construct_ids:
  - non_performing_loan_ratio_pct
  direction: negative
  effect_size: null
  confidence: strong
  method_used: panel VAR estimation
propositions_detail: []
sources_detail:
- id: king_levine_1993
  title: 'Finance and Growth: Schumpeter Might Be Right'
  authors: Robert G. King, Ross Levine
  year: 1993
  doi: 10.2307/2118406
  source_type: journal_article
- id: levine_2005
  title: 'Finance and Growth: Theory and Evidence'
  authors: Ross Levine
  year: 2005
  doi: null
  source_type: book_chapter
- id: demirguc_kunt_2018
  title: The Global Findex Database 2017 measuring financial inclusion and the fintech
    revolution
  authors: Demirguc-Kunt, Asli, Klapper, Leora, Singer, Dorothe, Ansar, Saniya, Hess,
    Jake
  year: 2018
  doi: 10.1596/978-1-4648-1259-0
  source_type: report
- id: jack_suri_2014
  title: Risk sharing and transactions costs evidence from Kenyas mobile money revolution
  authors: Jack, William, Suri, Tavneet
  year: 2014
  doi: 10.1257/aer.104.1.183
  source_type: academic_paper
playbooks_detail: []
download_url: https://pax-market.com/pax/financial-development.pax.tar.gz
download_size: 3.2 KB
published_by: Praxis Agent
related_packs: []
pax_name: financial-development
weight: 7974
---

**Domain:** Financial Development and Inclusion

How financial deepening banking access and inclusive finance affect economic growth poverty reduction and household welfare

**Temporal scope:** 1990-present | **Population:** Countries worldwide

## Key Findings

- Financial depth (private credit/GDP) strongly predicts subsequent economic growth (beta=0.03, p<.01) even after controlling for other standard growth determinants. *(positive, strong)*
- Systemic banking crises cause GDP losses of 5-10%, partially offsetting the long-run growth benefits of financial deepening. *(negative, strong)*
- The finance-growth relationship is not merely correlational: initial financial depth in 1960 predicts growth over the subsequent 30 years, suggesting a causal channel from finance to growth. *(positive, strong)*
- Legal origin (common law vs civil law) serves as a valid instrument for financial development, with common law countries developing deeper financial markets on average. *(positive, moderate)*
- Financial depth measured by private credit to GDP is positively associated with GDP growth but the relationship flattens above approximately 100 percent credit-to-GDP ratio *(positive, moderate)*
- Mobile money adoption reduced poverty by approximately 2 percent in Kenya through improved risk sharing and consumption smoothing *(negative, strong)*
- Bank account ownership is positively associated with household savings rates across developing countries *(positive, moderate)*
- High non-performing loan ratios are negatively associated with credit growth and economic recovery in post-crisis periods *(negative, strong)*

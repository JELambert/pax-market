---
name: sovereign-debt-crises
title: Sovereign Debt Crises
version: 1.0.0
pax_type: topic
description: How public debt levels fiscal sustainability and debt crises affect economic
  growth financial stability and development outcomes
author: null
created: '2026-04-05'
license: null
tags:
- topic
- sovereign-debt
constructs:
- public_debt_to_gdp
- debt_service_exports_pct
- sovereign_credit_rating_numeric
- fiscal_balance_gdp
- foreign_reserves_import_months
- government_bond_yield_10y
engines:
- ols_regression
- logistic_regression
- event_study
playbook_names:
- quick_start
construct_count: 6
finding_count: 3
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: sovereign_debt
  display_name: Sovereign Debt and Fiscal Crises
  description: How public debt levels fiscal sustainability and debt crises affect
    economic growth financial stability and development outcomes
  research_questions: []
  temporal_scope: 1970-present
  population: Countries worldwide
  level_of_analysis: macro
constructs_detail:
- id: public_debt_to_gdp
  display_name: Public Debt to GDP
  definition: Central government gross debt as percentage of gross domestic product
    measuring overall public indebtedness
  aliases: []
  construct_type: quantifiable
- id: debt_service_exports_pct
  display_name: Debt Service to Exports Ratio
  definition: Total debt service payments including principal and interest as percentage
    of exports of goods and services
  aliases: []
  construct_type: quantifiable
- id: sovereign_credit_rating_numeric
  display_name: Sovereign Credit Rating Numeric
  definition: Numerical encoding of sovereign credit ratings from AAA equals 21 to
    D equals 1 enabling quantitative analysis
  aliases: []
  construct_type: quantifiable
- id: fiscal_balance_gdp
  display_name: Fiscal Balance GDP Share
  definition: General government net lending or borrowing as percentage of GDP where
    positive values indicate fiscal surplus
  aliases: []
  construct_type: quantifiable
- id: foreign_reserves_import_months
  display_name: Foreign Reserves in Import Months
  definition: Total foreign exchange reserves measured in months of imports coverage
    indicating external liquidity buffer
  aliases: []
  construct_type: quantifiable
- id: government_bond_yield_10y
  display_name: Government Bond Yield 10 Year
  definition: Yield to maturity on benchmark 10-year government bonds in domestic
    currency reflecting sovereign borrowing cost
  aliases: []
  construct_type: quantifiable
findings_detail:
- finding_text: Debt crises are more likely when sovereign debt is denominated in
    foreign currency a phenomenon known as original sin
  construct_ids:
  - public_debt_to_gdp
  - sovereign_credit_rating_numeric
  direction: positive
  effect_size: null
  confidence: strong
  method_used: historical event analysis
- finding_text: Foreign reserve adequacy measured in import months is negatively associated
    with the probability of experiencing a sovereign debt crisis
  construct_ids:
  - foreign_reserves_import_months
  direction: negative
  effect_size: null
  confidence: strong
  method_used: probit regression with early warning indicators
- finding_text: Fiscal deterioration typically precedes sovereign credit rating downgrades
    by 12 to 18 months creating a predictable lag pattern
  construct_ids:
  - fiscal_balance_gdp
  - sovereign_credit_rating_numeric
  direction: negative
  effect_size: null
  confidence: moderate
  method_used: event study with Granger causality
propositions_detail: []
sources_detail:
- id: reinhart_rogoff_2009
  title: This Time Is Different Eight Centuries of Financial Folly
  authors: Reinhart, Carmen, Rogoff, Kenneth
  year: 2009
  doi: null
  source_type: book
- id: herndon_2014
  title: Does high public debt consistently stifle economic growth a critique of Reinhart
    and Rogoff
  authors: Herndon, Thomas, Ash, Michael, Pollin, Robert
  year: 2014
  doi: 10.1093/cje/bet075
  source_type: academic_paper
- id: abbas_2011
  title: Historical patterns and dynamics of public debt
  authors: Abbas, Ali, Belhocine, Nazim, ElGanainy, Asmaa, Horton, Mark
  year: 2011
  doi: null
  source_type: academic_paper
- id: eichengreen_2005
  title: The pain of original sin
  authors: Eichengreen, Barry, Hausmann, Ricardo, Panizza, Ugo
  year: 2005
  doi: null
  source_type: academic_paper
playbooks_detail: []
download_url: https://pax-market.com/pax/sovereign-debt-crises.pax.tar.gz
download_size: 2.5 KB
published_by: Praxis Agent
related_packs: []
pax_name: sovereign-debt-crises
weight: 7974
---

**Domain:** Sovereign Debt and Fiscal Crises

How public debt levels fiscal sustainability and debt crises affect economic growth financial stability and development outcomes

**Temporal scope:** 1970-present | **Population:** Countries worldwide

## Key Findings

- Debt crises are more likely when sovereign debt is denominated in foreign currency a phenomenon known as original sin *(positive, strong)*
- Foreign reserve adequacy measured in import months is negatively associated with the probability of experiencing a sovereign debt crisis *(negative, strong)*
- Fiscal deterioration typically precedes sovereign credit rating downgrades by 12 to 18 months creating a predictable lag pattern *(negative, moderate)*

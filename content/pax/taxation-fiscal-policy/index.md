---
name: taxation-fiscal-policy
title: Taxation Fiscal Policy
version: 1.0.0
pax_type: topic
description: How tax structure, revenue mobilization, and fiscal policy affect economic
  growth, inequality, and public goods provision across countries.
author: null
created: '2026-04-05'
license: null
tags:
- topic
- taxation-fiscal
constructs:
- tax_revenue_gdp_pct
- income_tax_share
- government_expenditure_gdp_pct
- fiscal_balance_gdp_pct
- public_debt_gdp_pct
- tax_compliance_rate
engines:
- ols_regression
- correlation_matrix
- difference_in_differences
playbook_names:
- quick_start
construct_count: 6
finding_count: 3
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: taxation_fiscal
  display_name: Taxation and Fiscal Policy
  description: How tax structure, revenue mobilization, and fiscal policy affect economic
    growth, inequality, and public goods provision
  research_questions: []
  temporal_scope: 1990-present
  population: Countries worldwide
  level_of_analysis: macro
constructs_detail:
- id: tax_revenue_gdp_pct
  display_name: Tax Revenue as Percent of GDP
  definition: Total tax revenue collected by government as a percentage of gross domestic
    product, measuring fiscal capacity and the overall tax burden on the economy
  aliases: []
  construct_type: quantifiable
- id: income_tax_share
  display_name: Income Tax Share of Revenue
  definition: Proportion of total tax revenue derived from personal and corporate
    income taxes, indicating the progressivity and direct taxation reliance of the
    tax system
  aliases: []
  construct_type: quantifiable
- id: government_expenditure_gdp_pct
  display_name: Government Expenditure as Percent of GDP
  definition: Total government spending including consumption and investment as a
    percentage of gross domestic product, measuring the size of government in the
    economy
  aliases: []
  construct_type: quantifiable
- id: fiscal_balance_gdp_pct
  display_name: Fiscal Balance as Percent of GDP
  definition: Difference between government revenue and expenditure as a percentage
    of GDP, where negative values indicate budget deficits and positive values indicate
    surpluses
  aliases: []
  construct_type: quantifiable
- id: public_debt_gdp_pct
  display_name: Public Debt as Percent of GDP
  definition: Total accumulated government debt as a percentage of gross domestic
    product, measuring the long-term fiscal sustainability and debt burden of the
    public sector
  aliases: []
  construct_type: quantifiable
- id: tax_compliance_rate
  display_name: Tax Compliance Rate
  definition: Proportion of tax obligations that are voluntarily fulfilled by taxpayers,
    reflecting tax morale, administrative effectiveness, and perceived fairness of
    the tax system
  aliases: []
  construct_type: quantifiable
findings_detail:
- finding_text: Tax revenue mobilization is positively associated with public goods
    quality and state capacity, with countries collecting more tax revenue providing
    better infrastructure, education, and health services
  construct_ids:
  - tax_revenue_gdp_pct
  direction: positive
  effect_size: null
  confidence: strong
  method_used: ols_regression
- finding_text: Progressive taxation reduces income inequality with moderate efficiency
    costs, though the optimal top marginal rate depends on behavioral elasticities
    that vary across contexts
  construct_ids:
  - income_tax_share
  direction: conditional
  effect_size: null
  confidence: moderate
  method_used: ols_regression
- finding_text: Tax cuts have asymmetric effects across the income distribution, with
    cuts for lower-income households generating higher fiscal multipliers than cuts
    for higher-income households
  construct_ids:
  - income_tax_share
  - tax_revenue_gdp_pct
  direction: conditional
  effect_size: null
  confidence: moderate
  method_used: difference_in_differences
propositions_detail: []
sources_detail:
- id: mertens_ravn_2013
  title: The Dynamic Effects of Personal and Corporate Income Tax Changes in the United
    States
  authors: Mertens, K., Ravn, M.O.
  year: 2013
  doi: 10.1257/aer.103.4.1212
  source_type: journal_article
- id: besley_persson_2014
  title: Why Do Developing Countries Tax So Little?
  authors: Besley, T., Persson, T.
  year: 2014
  doi: 10.1257/jep.28.4.99
  source_type: journal_article
- id: reinhart_rogoff_2010
  title: Growth in a Time of Debt
  authors: Reinhart, C.M., Rogoff, K.S.
  year: 2010
  doi: 10.1257/aer.100.2.573
  source_type: journal_article
- id: piketty_saez_2007
  title: How Progressive is the U.S. Federal Tax System?
  authors: Piketty, T., Saez, E.
  year: 2007
  doi: null
  source_type: journal_article
playbooks_detail: []
download_url: https://pax-market.com/pax/taxation-fiscal-policy.pax.tar.gz
download_size: 2.5 KB
published_by: Praxis Agent
related_packs: []
pax_name: taxation-fiscal-policy
weight: 7974
---

**Domain:** Taxation and Fiscal Policy

How tax structure, revenue mobilization, and fiscal policy affect economic growth, inequality, and public goods provision

**Temporal scope:** 1990-present | **Population:** Countries worldwide

## Key Findings

- Tax revenue mobilization is positively associated with public goods quality and state capacity, with countries collecting more tax revenue providing better infrastructure, education, and health services *(positive, strong)*
- Progressive taxation reduces income inequality with moderate efficiency costs, though the optimal top marginal rate depends on behavioral elasticities that vary across contexts *(conditional, moderate)*
- Tax cuts have asymmetric effects across the income distribution, with cuts for lower-income households generating higher fiscal multipliers than cuts for higher-income households *(conditional, moderate)*

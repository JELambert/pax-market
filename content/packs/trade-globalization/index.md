---
name: trade-globalization
title: Trade Globalization
version: 1.0.0
pax_type: topic
description: How trade openness tariff policy and global value chain participation
  affect economic growth inequality and development
author: null
created: '2026-04-05'
license: null
tags:
- topic
- trade-globalization
constructs:
- merchandise_exports_gdp_pct
- applied_tariff_rate_weighted
- trade_balance_gdp
- gvc_participation_index
- terms_of_trade_index_2015
- trade_openness_gdp
engines:
- ols_regression
- instrumental_variables
- gmm_estimation
playbook_names:
- quick_start
construct_count: 6
finding_count: 6
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: trade_globalization
  display_name: International Trade and Globalization
  description: How trade openness tariff policy and global value chain participation
    affect economic growth inequality and development
  research_questions: []
  temporal_scope: 1960-present
  population: Countries worldwide
  level_of_analysis: macro
constructs_detail:
- id: merchandise_exports_gdp_pct
  display_name: Merchandise Exports Share of GDP
  definition: Total merchandise exports as percentage of GDP measuring goods export
    dependency
  aliases: []
  construct_type: quantifiable
- id: applied_tariff_rate_weighted
  display_name: Applied Tariff Rate Weighted
  definition: Trade-weighted mean applied tariff rate across all product categories
    reflecting actual trade barriers
  aliases: []
  construct_type: quantifiable
- id: trade_balance_gdp
  display_name: Trade Balance as GDP Share
  definition: Net exports of goods and services as percentage of GDP with positive
    values indicating trade surplus
  aliases: []
  construct_type: quantifiable
- id: gvc_participation_index
  display_name: GVC Participation Index
  definition: Share of exports involving cross-border production stages measured by
    foreign value added content in exports
  aliases: []
  construct_type: quantifiable
- id: terms_of_trade_index_2015
  display_name: Terms of Trade Index
  definition: Ratio of export prices to import prices with 2015 as base year equals
    100 measuring relative trade advantage
  aliases: []
  construct_type: quantifiable
- id: trade_openness_gdp
  display_name: Trade Openness
  definition: Sum of exports and imports of goods and services as share of GDP measured
    as percentage reflecting overall trade integration
  aliases: []
  construct_type: quantifiable
findings_detail:
- finding_text: Natural resource abundance negatively predicts economic growth (beta=-0.09,
    p<.01 on resource exports/GDP), controlling for initial income, openness, investment,
    and rule of law.
  construct_ids:
  - resource_dependence_index
  - economic_growth_resource
  direction: negative
  effect_size: β=-0.09, p<.01
  confidence: strong
  method_used: cross-country OLS growth regression
- finding_text: 'Resource-rich economies suffer from Dutch disease: resource booms
    appreciate the real exchange rate and crowd out manufacturing, reducing long-run
    growth potential.'
  construct_ids:
  - dutch_disease_indicator
  - economic_growth_resource
  - natural_resource_rents_gdp
  direction: negative
  effect_size: null
  confidence: moderate
  method_used: cross-country growth decomposition
- finding_text: Trade openness is positively associated with GDP per capita growth
    but the relationship is sensitive to instrumental variable choice and estimation
    method
  construct_ids:
  - trade_openness_gdp
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: instrumental variable regression
- finding_text: Tariff reductions are associated with faster economic growth in developing
    countries particularly in the post-1990 liberalization period
  construct_ids:
  - applied_tariff_rate_weighted
  direction: negative
  effect_size: null
  confidence: moderate
  method_used: cross-country growth regression
- finding_text: Global value chain participation is positively associated with manufacturing
    productivity growth through technology transfer and specialization gains
  construct_ids:
  - gvc_participation_index
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: panel data analysis
- finding_text: Terms of trade volatility is negatively associated with economic growth
    in commodity-dependent economies through investment uncertainty channels
  construct_ids:
  - terms_of_trade_index_2015
  direction: negative
  effect_size: null
  confidence: strong
  method_used: GMM dynamic panel estimation
propositions_detail: []
sources_detail:
- id: sachs_warner_1995
  title: Natural Resource Abundance and Economic Growth
  authors: Jeffrey D. Sachs, Andrew M. Warner
  year: 1995
  doi: null
  source_type: working_paper
- id: frankel_romer_1999
  title: Does trade cause growth
  authors: Frankel, Jeffrey, Romer, David
  year: 1999
  doi: 10.1257/aer.89.3.379
  source_type: academic_paper
- id: rodriguez_rodrik_2000
  title: Trade policy and economic growth a skeptics guide to the cross-national evidence
  authors: Rodriguez, Francisco, Rodrik, Dani
  year: 2000
  doi: null
  source_type: academic_paper
- id: worldbank_wto_gvc_2020
  title: Trading for development in the age of global value chains
  authors: World Bank, World Trade Organization
  year: 2020
  doi: null
  source_type: report
playbooks_detail: []
download_url: https://pax-market.com/packs/trade-globalization.pax.tar.gz
download_size: 2.8 KB
published_by: Praxis Agent
related_packs: []
pax_name: trade-globalization
weight: 7974
---

**Domain:** International Trade and Globalization

How trade openness tariff policy and global value chain participation affect economic growth inequality and development

**Temporal scope:** 1960-present | **Population:** Countries worldwide

## Key Findings

- Natural resource abundance negatively predicts economic growth (beta=-0.09, p<.01 on resource exports/GDP), controlling for initial income, openness, investment, and rule of law. *(negative, strong)*
- Resource-rich economies suffer from Dutch disease: resource booms appreciate the real exchange rate and crowd out manufacturing, reducing long-run growth potential. *(negative, moderate)*
- Trade openness is positively associated with GDP per capita growth but the relationship is sensitive to instrumental variable choice and estimation method *(positive, moderate)*
- Tariff reductions are associated with faster economic growth in developing countries particularly in the post-1990 liberalization period *(negative, moderate)*
- Global value chain participation is positively associated with manufacturing productivity growth through technology transfer and specialization gains *(positive, moderate)*
- Terms of trade volatility is negatively associated with economic growth in commodity-dependent economies through investment uncertainty channels *(negative, strong)*

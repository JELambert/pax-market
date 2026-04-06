---
name: research-innovation
title: Research Innovation
version: 1.0.0
pax_type: topic
description: How R&D investment, patent activity, scientific output, and researcher
  density drive technological change, productivity growth, and national competitiveness.
author: null
created: '2026-04-05'
license: null
tags:
- topic
- research-innovation
constructs:
- rd_expenditure_gdp_pct
- patent_applications_per_million
- researchers_per_million
- high_tech_exports_pct
- scientific_publications_per_capita
- total_factor_productivity_growth
engines:
- ols_regression
- correlation_matrix
- random_forest
playbook_names:
- quick_start
construct_count: 6
finding_count: 4
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: research_innovation
  display_name: Research, Innovation, and Economic Growth
  description: How R&D investment, patent activity, and scientific output drive technological
    change, productivity growth, and competitiveness
  research_questions: []
  temporal_scope: 1996-present
  population: Countries worldwide
  level_of_analysis: macro
constructs_detail:
- id: rd_expenditure_gdp_pct
  display_name: R&D Expenditure as % of GDP
  definition: Gross domestic expenditure on research and development as a percentage
    of gross domestic product
  aliases: []
  construct_type: quantifiable
- id: patent_applications_per_million
  display_name: Patent Applications Per Million
  definition: Number of patent applications filed per million population at national
    and international patent offices
  aliases: []
  construct_type: quantifiable
- id: researchers_per_million
  display_name: Researchers Per Million
  definition: Full-time equivalent researchers engaged in R&D per million population
  aliases: []
  construct_type: quantifiable
- id: high_tech_exports_pct
  display_name: High-Tech Exports Share
  definition: High-technology exports as a percentage of total manufactured exports
    based on OECD SITC classification
  aliases: []
  construct_type: quantifiable
- id: scientific_publications_per_capita
  display_name: Scientific Publications Per Capita
  definition: Number of citable scientific and technical journal articles per million
    population per year
  aliases: []
  construct_type: quantifiable
- id: total_factor_productivity_growth
  display_name: Total Factor Productivity Growth
  definition: Annual growth rate of total factor productivity measuring technological
    progress and efficiency gains
  aliases: []
  construct_type: outcome
findings_detail:
- finding_text: R&D expenditure as share of GDP is positively associated with TFP
    growth with estimated social returns 2-4 times larger than private returns to
    R&D investment
  construct_ids:
  - rd_expenditure_gdp_pct
  - total_factor_productivity_growth
  direction: positive
  effect_size: null
  confidence: strong
  method_used: ols_regression
- finding_text: Patent applications per capita are positively associated with GDP
    per capita growth but with heterogeneous effects across technology sectors and
    country income levels
  construct_ids:
  - patent_applications_per_million
  - total_factor_productivity_growth
  direction: conditional
  effect_size: null
  confidence: moderate
  method_used: ols_regression
- finding_text: Researcher density per million population is strongly positively correlated
    with scientific publication output per capita across 140 countries
  construct_ids:
  - researchers_per_million
  - scientific_publications_per_capita
  direction: positive
  effect_size: null
  confidence: strong
  method_used: correlation_matrix
- finding_text: High-technology export share is positively associated with economic
    complexity and long-run growth in Schumpeterian growth models with empirical validation
  construct_ids:
  - high_tech_exports_pct
  - total_factor_productivity_growth
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: ols_regression
propositions_detail: []
sources_detail:
- id: jones_williams_1998
  title: Measuring the Social Return to R&D
  authors: Jones CI, Williams JC
  year: 1998
  doi: 10.2307/2586967
  source_type: journal_article
- id: aghion_howitt_1992
  title: A Model of Growth Through Creative Destruction
  authors: Aghion P, Howitt P
  year: 1992
  doi: 10.2307/2951599
  source_type: journal_article
- id: unesco_science_2021
  title: 'UNESCO Science Report: The Race Against Time for Smarter Development'
  authors: UNESCO
  year: 2021
  doi: null
  source_type: report
- id: jaffe_trajtenberg_2002
  title: 'Patents, Citations, and Innovations: A Window on the Knowledge Economy'
  authors: Jaffe AB, Trajtenberg M
  year: 2002
  doi: 10.7551/mitpress/5263.001.0001
  source_type: book
playbooks_detail: []
download_url: https://pax-market.com/pax/research-innovation.pax.tar.gz
download_size: 2.4 KB
published_by: Praxis Agent
related_packs: []
pax_name: research-innovation
weight: 7974
---

**Domain:** Research, Innovation, and Economic Growth

How R&D investment, patent activity, and scientific output drive technological change, productivity growth, and competitiveness

**Temporal scope:** 1996-present | **Population:** Countries worldwide

## Key Findings

- R&D expenditure as share of GDP is positively associated with TFP growth with estimated social returns 2-4 times larger than private returns to R&D investment *(positive, strong)*
- Patent applications per capita are positively associated with GDP per capita growth but with heterogeneous effects across technology sectors and country income levels *(conditional, moderate)*
- Researcher density per million population is strongly positively correlated with scientific publication output per capita across 140 countries *(positive, strong)*
- High-technology export share is positively associated with economic complexity and long-run growth in Schumpeterian growth models with empirical validation *(positive, moderate)*

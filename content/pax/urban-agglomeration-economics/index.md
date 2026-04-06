---
name: urban-agglomeration-economics
title: Why cities make people more productive and what the limits are
version: 1.0.0
pax_type: topic
description: Why cities make people more productive and what the limits are — agglomeration
  economies, knowledge spillovers, sorting, and congestion costs. Built on Glaeser,
  Moretti, Duranton & Puga, and Combes. Data from OECD Metropolitan Database (650+
  metro areas), US Census urban-rural panels, and European city-level wage regressions.
  Covers the urban wage premium, innovation clustering, housing affordability tradeoffs,
  and remote work disruption.
author: ''
created: ''
license: ''
tags:
- topic
constructs:
- population_density
- urban_wage_premium
- knowledge_spillovers
- housing_cost_burden
- patent_density
- commute_time
engines:
- ols_regression
- instrumental_variables
- difference_in_differences
- correlation_matrix
- logistic_regression
playbook_names:
- quick_start
construct_count: 6
finding_count: 0
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: disease_outbreak_frequency
  display_name: Disease Outbreak Frequency
  description: Frequency and determinants of infectious disease outbreaks reported
    through surveillance systems
  research_questions: []
  temporal_scope: null
  population: Countries worldwide
  level_of_analysis: macro
constructs_detail:
- id: population_density
  display_name: Population Density
  definition: The number of people per unit area (typically per km²), which affects
    disease transmission dynamics and outbreak potential.
  aliases: []
  construct_type: quantifiable
- id: urban_wage_premium
  display_name: Urban Wage Premium
  definition: The percentage by which wages in dense urban areas exceed wages in less
    dense areas, controlling for worker characteristics. Raw premium ~30% for doubling
    city size; after controlling for sorting (education, ability), residual agglomeration
    premium is ~4-8% per doubling of density. Measured via Mincerian wage equations
    with city-size or density controls.
  aliases: []
  construct_type: quantifiable
- id: knowledge_spillovers
  display_name: Knowledge Spillovers
  definition: 'The informal transfer of knowledge between co-located workers and firms
    through face-to-face interaction, labor mobility, and observation. Measured via
    patent citation localization, co-invention networks, or productivity growth after
    arrival of star scientists. Jaffe (1993): patent citations are 5-10x more likely
    to cite geographically proximate patents, controlling for technology class.'
  aliases: []
  construct_type: concept
- id: housing_cost_burden
  display_name: Housing Cost Burden
  definition: Ratio of median housing costs (rent or mortgage) to median household
    income in a metro area. The primary congestion cost of agglomeration. US metros
    range from 20% (Sun Belt) to 50%+ (San Francisco, New York). When housing costs
    are subtracted, the real urban wage premium shrinks or vanishes for many workers.
  aliases: []
  construct_type: quantifiable
- id: patent_density
  display_name: Patent Density
  definition: 'Patents per capita or per worker in a metro area. Proxy for localized
    innovation output. Correlation with population density: r~0.35. Highly concentrated:
    top 20 MSAs produce ~60% of US patents. OECD REGPAT database provides geocoded
    patent data back to 1977.'
  aliases: []
  construct_type: quantifiable
- id: commute_time
  display_name: Average Commute Time
  definition: Mean one-way commute duration in minutes for metro area workers. The
    primary time-cost of agglomeration. US average ~27 minutes; NYC ~40 minutes. Increases
    approximately 8 minutes per doubling of metro population. ACS and OECD provide
    annual estimates.
  aliases: []
  construct_type: quantifiable
findings_detail: []
propositions_detail: []
sources_detail: []
playbooks_detail: []
download_url: https://pax-market.com/pax/urban-agglomeration-economics.pax.tar.gz
download_size: 2.3 KB
published_by: Praxis Agent
related_packs: []
pax_name: urban-agglomeration-economics
weight: 10000
---

**Domain:** Disease Outbreak Frequency

Frequency and determinants of infectious disease outbreaks reported through surveillance systems

**Population:** Countries worldwide

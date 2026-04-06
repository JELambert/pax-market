---
name: corruption-governance
title: Corruption Governance
version: 1.0.0
pax_type: topic
description: How corruption affects economic development, foreign investment, public
  service delivery, and institutional trust across countries worldwide.
author: null
created: '2026-04-05'
license: null
tags:
- topic
- corruption-governance
constructs:
- corruption_perception_index
- government_effectiveness_score
- regulatory_quality_score
- fdi_inflows_gdp
- bribery_incidence_rate
- public_trust_government
engines:
- ols_regression
- correlation_matrix
- instrumental_variables
playbook_names:
- quick_start
construct_count: 6
finding_count: 8
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: corruption_governance
  display_name: Corruption and Governance Quality
  description: How corruption affects economic development, foreign investment, public
    service delivery, and institutional trust
  research_questions: []
  temporal_scope: 1995-present
  population: Countries worldwide
  level_of_analysis: macro
constructs_detail:
- id: corruption_perception_index
  display_name: Corruption Perception Index
  definition: Transparency International's composite index measuring perceived levels
    of public sector corruption across countries, scored 0-100 where higher values
    indicate less corruption
  aliases: []
  construct_type: quantifiable
- id: government_effectiveness_score
  display_name: Government Effectiveness Score
  definition: World Governance Indicators measure of the quality of public services,
    civil service independence from political pressures, quality of policy formulation
    and implementation
  aliases: []
  construct_type: quantifiable
- id: regulatory_quality_score
  display_name: Regulatory Quality Score
  definition: World Governance Indicators measure of government ability to formulate
    and implement sound policies and regulations that permit and promote private sector
    development
  aliases: []
  construct_type: quantifiable
- id: fdi_inflows_gdp
  display_name: FDI Inflows as Percent of GDP
  definition: Net inflows of foreign direct investment as a percentage of gross domestic
    product, measuring international investor confidence and capital attraction
  aliases: []
  construct_type: quantifiable
- id: bribery_incidence_rate
  display_name: Bribery Incidence Rate
  definition: Percentage of firms or individuals reporting having paid a bribe to
    a public official in the past year, measuring direct corruption experience rather
    than perception
  aliases: []
  construct_type: quantifiable
- id: public_trust_government
  display_name: Public Trust in Government
  definition: Survey-based measure of citizen confidence in national government institutions,
    typically measured as percentage expressing trust or confidence in government
  aliases: []
  construct_type: quantifiable
findings_detail:
- finding_text: 1 SD improvement in corruption index associated with +4 pp investment
    rate and +0.5 pp annual growth.
  construct_ids:
  - control_of_corruption
  - per_capita_income
  direction: negative
  effect_size: null
  confidence: strong
  method_used: OLS and IV, N~67
- finding_text: Corruption negatively affects investment as a share of GDP. A one-standard-deviation
    decrease in corruption is associated with an increase in the investment rate of
    over 4 percentage points.
  construct_ids:
  - corruption_level
  - gdp_per_capita
  direction: negative
  effect_size: β≈-0.3 to -0.9 depending on specification; 1 SD corruption reduction
    → +4pp investment/GDP
  confidence: strong
  method_used: OLS and IV using ethno-linguistic fractionalization as instrument,
    N≈67 countries
- finding_text: Corruption negatively affects economic growth both directly and indirectly
    through reduced investment. The relationship is robust to controlling for political
    instability and other institutional variables.
  construct_ids:
  - corruption_level
  - gdp_per_capita
  direction: negative
  effect_size: Significant negative effect on growth, robust across specifications
  confidence: moderate
  method_used: OLS and IV, cross-country regression
- finding_text: Ethno-linguistic fractionalization serves as a valid instrument for
    corruption, establishing a causal channel from bureaucratic inefficiency to lower
    investment and growth.
  construct_ids:
  - corruption_level
  direction: positive
  effect_size: IV estimates confirm and strengthen OLS findings
  confidence: moderate
  method_used: IV/2SLS with ethno-linguistic fractionalization instrument
- finding_text: Corruption is negatively associated with GDP growth rate, with approximately
    0.5 percentage point decrease in growth per standard deviation increase in corruption
    index
  construct_ids:
  - corruption_perception_index
  direction: negative
  effect_size: null
  confidence: moderate
  method_used: ols_regression
- finding_text: High corruption reduces FDI inflows by an amount equivalent to raising
    the tax rate by more than 20 percentage points, demonstrating corruption acts
    as a significant tax on foreign investment
  construct_ids:
  - corruption_perception_index
  - fdi_inflows_gdp
  direction: negative
  effect_size: null
  confidence: strong
  method_used: instrumental_variables
- finding_text: Government effectiveness is positively associated with public service
    delivery quality across all country income groups, with stronger effects in developing
    countries
  construct_ids:
  - government_effectiveness_score
  direction: positive
  effect_size: null
  confidence: strong
  method_used: correlation_matrix
- finding_text: Regulatory quality is positively associated with new business formation
    rates and private sector development indicators across countries
  construct_ids:
  - regulatory_quality_score
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: ols_regression
propositions_detail: []
sources_detail:
- id: mauro_1995
  title: Corruption and Growth
  authors: Mauro, Paolo
  year: 1995
  doi: null
  source_type: academic_paper
- id: kaufmann_2010
  title: 'The Worldwide Governance Indicators: Methodology and Analytical Issues'
  authors: Kaufmann, D., Kraay, A., Mastruzzi, M.
  year: 2010
  doi: 10.1596/1813-9450-5430
  source_type: working_paper
- id: wei_2000
  title: How Taxing is Corruption on International Investors?
  authors: Wei, S.-J.
  year: 2000
  doi: 10.1162/003465300558533
  source_type: journal_article
- id: svensson_2005
  title: Eight Questions about Corruption
  authors: Svensson, J.
  year: 2005
  doi: 10.1257/089533005774357860
  source_type: journal_article
playbooks_detail: []
download_url: https://pax-market.com/packs/corruption-governance.pax.tar.gz
download_size: 3.2 KB
published_by: Praxis Agent
related_packs: []
pax_name: corruption-governance
weight: 7974
---

**Domain:** Corruption and Governance Quality

How corruption affects economic development, foreign investment, public service delivery, and institutional trust

**Temporal scope:** 1995-present | **Population:** Countries worldwide

## Key Findings

- 1 SD improvement in corruption index associated with +4 pp investment rate and +0.5 pp annual growth. *(negative, strong)*
- Corruption negatively affects investment as a share of GDP. A one-standard-deviation decrease in corruption is associated with an increase in the investment rate of over 4 percentage points. *(negative, strong)*
- Corruption negatively affects economic growth both directly and indirectly through reduced investment. The relationship is robust to controlling for political instability and other institutional variables. *(negative, moderate)*
- Ethno-linguistic fractionalization serves as a valid instrument for corruption, establishing a causal channel from bureaucratic inefficiency to lower investment and growth. *(positive, moderate)*
- Corruption is negatively associated with GDP growth rate, with approximately 0.5 percentage point decrease in growth per standard deviation increase in corruption index *(negative, moderate)*
- High corruption reduces FDI inflows by an amount equivalent to raising the tax rate by more than 20 percentage points, demonstrating corruption acts as a significant tax on foreign investment *(negative, strong)*
- Government effectiveness is positively associated with public service delivery quality across all country income groups, with stronger effects in developing countries *(positive, strong)*
- Regulatory quality is positively associated with new business formation rates and private sector development indicators across countries *(positive, moderate)*

---
title: Institutional quality and economic development
pax_name: institutional-quality-development
version: 1.0.0
pax_type: topic
description: Institutional quality and economic development — how property rights,
  rule of law, corruption control, and democratic governance shape long-run per capita
  income. Built on Acemoglu, Johnson & Robinson (2001), North (1990), Rodrik et al.
  (2004), Kaufmann et al. (2010), and Mauro (1995).
author: Acemoglu, Daron; North, Douglass C.; Rodrik, Dani; Kaufmann, Daniel; Mauro,
  Paolo
created: '2026-04-04'
license: ''
tags:
- topic
- institutional-quality-development
constructs:
- rule_of_law
- control_of_corruption
- property_rights_security
- government_effectiveness
- democratic_governance
engines:
- ols_regression
- instrumental_variables
- difference_in_differences
- lasso_regression
playbook_names:
- quick_start
construct_count: 5
finding_count: 5
proposition_count: 0
has_playbooks: true
has_data_sources: true
domain:
  id: institutional_quality_development
  display_name: Institutional Quality and Economic Development
  description: How formal and informal institutions — property rights, rule of law,
    corruption control, governance — shape long-run economic development outcomes
    across countries.
  research_questions: []
  temporal_scope: 1960-present
  population: Sovereign states (country-year)
  level_of_analysis: macro
constructs_detail:
- id: rule_of_law
  display_name: Rule of Law
  definition: Confidence in and abidance by the rules of society, including contract
    enforcement, property rights, and the courts. WGI Rule of Law indicator.
  aliases:
  - WGI Rule of Law
  - legal institutions quality
  construct_type: quantifiable
- id: control_of_corruption
  display_name: Control of Corruption
  definition: The extent to which public power is NOT exercised for private gain,
    including petty and grand corruption.
  aliases:
  - WGI Control of Corruption
  - CPI score
  construct_type: quantifiable
- id: property_rights_security
  display_name: Property Rights Security
  definition: Degree to which private property rights are legally protected against
    state expropriation and private predation.
  aliases:
  - expropriation risk
  - ICRG property rights
  construct_type: quantifiable
- id: government_effectiveness
  display_name: Government Effectiveness
  definition: Quality of public services, civil service, and credibility of government
    commitment to policies. WGI Government Effectiveness.
  aliases:
  - bureaucratic quality
  - state capacity
  construct_type: quantifiable
- id: democratic_governance
  display_name: Democratic Governance
  definition: Degree to which political leaders are chosen through free elections
    with civil liberties protection. Polity2, V-Dem, Freedom House.
  aliases:
  - democracy
  - Polity2 score
  construct_type: quantifiable
findings_detail:
- finding_text: IV/2SLS using settler mortality shows institutions have a large causal
    effect on income per capita. 1 SD improvement in expropriation risk ~ 1+ log point
    increase in income.
  construct_ids:
  - property_rights_security
  - per_capita_income
  direction: positive
  effect_size: ''
  confidence: strong
  method_used: IV/2SLS, N=64 former colonies
  finding_type: ''
  evidence_type: ''
- finding_text: Once institutions are instrumented, geography has no direct effect
    and trade is insignificant. Institutions dominate.
  construct_ids:
  - rule_of_law
  - per_capita_income
  direction: positive
  effect_size: ''
  confidence: strong
  method_used: IV/2SLS horse race, N~80
  finding_type: ''
  evidence_type: ''
- finding_text: 1 SD improvement in corruption index associated with +4 pp investment
    rate and +0.5 pp annual growth.
  construct_ids:
  - control_of_corruption
  - per_capita_income
  direction: negative
  effect_size: ''
  confidence: strong
  method_used: OLS and IV, N~67
  finding_type: ''
  evidence_type: ''
- finding_text: ICRG-based property rights measures have substantially larger positive
    association with investment and growth than political freedom indices.
  construct_ids:
  - property_rights_security
  - per_capita_income
  direction: positive
  effect_size: ''
  confidence: strong
  method_used: OLS cross-country, N~97
  finding_type: ''
  evidence_type: ''
- finding_text: Strong correlation (r~0.80) between rule of law and GDP per capita
    across 200+ countries, though causal inference requires instrumentation.
  construct_ids:
  - rule_of_law
  - control_of_corruption
  - per_capita_income
  direction: positive
  effect_size: ''
  confidence: moderate
  method_used: Descriptive, 200+ countries
  finding_type: ''
  evidence_type: ''
propositions_detail: []
sources_detail:
- id: acemoglu_johnson_robinson_2001
  title: 'The Colonial Origins of Comparative Development: An Empirical Investigation'
  authors: Acemoglu, Daron; Johnson, Simon; Robinson, James A.
  year: 2001
  doi: null
  source_type: academic_paper
- id: rodrik_subramanian_trebbi_2004
  title: 'Institutions Rule: The Primacy of Institutions Over Geography and Integration
    in Economic Development'
  authors: Rodrik, Dani; Subramanian, Arvind; Trebbi, Francesco
  year: 2004
  doi: null
  source_type: academic_paper
- id: mauro_1995
  title: Corruption and Growth
  authors: Mauro, Paolo
  year: 1995
  doi: null
  source_type: academic_paper
- id: kaufmann_kraay_mastruzzi_2010
  title: 'The Worldwide Governance Indicators: Methodology and Analytical Issues'
  authors: Kaufmann, Daniel; Kraay, Aart; Mastruzzi, Massimo
  year: 2010
  doi: null
  source_type: academic_paper
- id: knack_keefer_1995
  title: 'Institutions and Economic Performance: Cross-Country Tests Using Alternative
    Institutional Measures'
  authors: Knack, Stephen; Keefer, Philip
  year: 1995
  doi: null
  source_type: academic_paper
playbooks_detail:
- id: quick_start
  display_name: Quick Start — Institutional Quality Development
  description: Basic analysis workflow for the institutional_quality_development domain.
  estimated_runtime: 1–3 minutes
  step_count: 1
  engines_used: []
download_url: /packs/institutional-quality-development.pax.tar.gz
download_size: 3.1 KB
weight: 7974
related_packs: []
---

**Domain:** Institutional Quality and Economic Development

How formal and informal institutions — property rights, rule of law, corruption control, governance — shape long-run economic development outcomes across countries.

**Temporal scope:** 1960-present | **Population:** Sovereign states (country-year)

## Key Findings

- IV/2SLS using settler mortality shows institutions have a large causal effect on income per capita. 1 SD improvement in expropriation risk ~ 1+ log point increase in income. *(positive, strong)*
- Once institutions are instrumented, geography has no direct effect and trade is insignificant. Institutions dominate. *(positive, strong)*
- 1 SD improvement in corruption index associated with +4 pp investment rate and +0.5 pp annual growth. *(negative, strong)*
- ICRG-based property rights measures have substantially larger positive association with investment and growth than political freedom indices. *(positive, strong)*
- Strong correlation (r~0.80) between rule of law and GDP per capita across 200+ countries, though causal inference requires instrumentation. *(positive, moderate)*

## Sources

- Acemoglu, Daron; Johnson, Simon; Robinson, James A. (2001). *The Colonial Origins of Comparative Development: An Empirical Investigation*.
- Rodrik, Dani; Subramanian, Arvind; Trebbi, Francesco (2004). *Institutions Rule: The Primacy of Institutions Over Geography and Integration in Economic Development*.
- Mauro, Paolo (1995). *Corruption and Growth*.
- Kaufmann, Daniel; Kraay, Aart; Mastruzzi, Massimo (2010). *The Worldwide Governance Indicators: Methodology and Analytical Issues*.
- Knack, Stephen; Keefer, Philip (1995). *Institutions and Economic Performance: Cross-Country Tests Using Alternative Institutional Measures*.

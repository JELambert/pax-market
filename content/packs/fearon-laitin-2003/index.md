---
title: Fearon & Laitin (2003) — Ethnicity, Insurgency, and Civil War
pax_name: fearon-laitin-2003
version: 1.0.0
pax_type: paper
description: Fearon & Laitin (2003) "Ethnicity, Insurgency, and Civil War" — foundational
  paper on civil war onset. Challenges ethnic grievance explanations, finds insurgency-opportunity
  factors (poverty, terrain, weak states) are stronger predictors.
author: Fearon, James D.; Laitin, David D.
created: '2003-02-01'
license: CC-BY-4.0
tags:
- civil-war
- conflict
- insurgency
- ethnic-fractionalization
- state-capacity
constructs:
- civil_war_onset
- mountainous_terrain
- political_instability
- noncontiguous_territory
- oil_exporter
- new_state
- religious_fractionalization
- per_capita_income
- population_size
- anocracy
engines:
- ''
playbook_names:
- quick_start
construct_count: 10
finding_count: 11
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: intra_state_conflict
  display_name: Intra-State Conflict
  description: Study of civil war onset, duration, and termination within sovereign
    states. Examines structural, economic, political, and geographic determinants
    of armed conflict.
  research_questions:
  - What conditions increase the probability of civil war onset?
  - Does ethnic or religious diversity cause conflict, or do structural factors dominate?
  - How do state capacity and economic development affect conflict risk?
  - What role does terrain and geography play in insurgency feasibility?
  temporal_scope: 1945-present
  population: Sovereign states (country-year observations)
  level_of_analysis: macro
constructs_detail:
- id: civil_war_onset
  display_name: Civil War Onset
  definition: 'Binary indicator: 1 if a civil war began in this country-year, 0 otherwise.
    Fearon & Laitin define civil wars as internal conflicts with organized violence,
    at least 1,000 battle deaths, and effective resistance by both sides.'
  aliases:
  - conflict onset
  - war initiation
  - armed conflict start
  - intrastate war onset
  - onset
  - PRIO onset
  - UCDP onset
  construct_type: quantifiable
- id: mountainous_terrain
  display_name: Mountainous Terrain
  definition: Percentage of a country's territory that is mountainous, per the Geomorphic
    Units of the World dataset. Logged in regression models. Higher values increase
    insurgency viability by providing rebel sanctuary.
  aliases:
  - rough terrain
  - percent mountainous
  - lmtnest
  construct_type: quantifiable
- id: political_instability
  display_name: Political Instability
  definition: 'Binary indicator: 1 if there was a three-or-more-point change in Polity
    score in the previous three years. Captures regime transitions and political turbulence
    that may lower the cost of civil war initiation.'
  aliases: []
  construct_type: quantifiable
- id: noncontiguous_territory
  display_name: Noncontiguous Territory
  definition: 'Binary indicator: 1 if the state has territory that is physically separated
    from the main territory (e.g., islands, exclaves). Noncontiguity creates zones
    where state capacity is lower and rebel control is easier to establish.'
  aliases: []
  construct_type: quantifiable
- id: oil_exporter
  display_name: Oil Exporter
  definition: 'Binary indicator: 1 if fuel exports exceeded one-third of export revenues.
    Oil states may face conflict due to prize capture incentives, weaker tax-based
    state institutions, or Dutch disease effects on state capacity.'
  aliases: []
  construct_type: quantifiable
- id: new_state
  display_name: New State
  definition: 'Binary indicator: 1 if the state became independent within the prior
    two years. New states face elevated conflict risk due to weak institutions, contested
    borders, and unresolved ethnic or regional claims.'
  aliases: []
  construct_type: quantifiable
- id: religious_fractionalization
  display_name: Religious Fractionalization
  definition: Probability that two randomly selected individuals belong to different
    religious groups (Herfindahl index). Ranges 0-1. Included as a control alongside
    ethnic fractionalization; not found to be a robust predictor of civil war onset.
  aliases: []
  construct_type: quantifiable
- id: per_capita_income
  display_name: Per Capita Income
  definition: 'GDP per capita, typically logged and lagged one year. One of the strongest
    predictors of civil war onset: wealthier countries have lower risk, reflecting
    higher opportunity costs of rebellion and greater state capacity to deter it.'
  aliases:
  - income per capita
  - GDP per capita
  - log GDP per capita
  - economic development
  - national wealth
  - lgdp_pc
  - lgdp_pc_l1
  construct_type: quantifiable
- id: population_size
  display_name: Population Size
  definition: Total population, logged and lagged one year. Larger populations increase
    civil war risk — more people means more potential recruits and more heterogeneous
    grievances, though the mechanism is contested.
  aliases: []
  construct_type: quantifiable
- id: anocracy
  display_name: Anocracy (Mixed Regime)
  definition: 'Binary indicator: 1 if Polity IV score is between -5 and +5, indicating
    a mixed or incoherent regime type. Anocracies are predicted to have higher conflict
    risk than either full democracies or full autocracies (inverted-U).'
  aliases: []
  construct_type: quantifiable
findings_detail:
- finding_text: 'Per capita income (logged, lagged) is one of the strongest predictors
    of civil war onset: a one standard deviation increase reduces onset probability
    by roughly half.'
  construct_ids:
  - civil_war_onset
  - per_capita_income
  direction: negative
  effect_size: strong — one SD increase (~1.5 log units) ≈ 50% reduction in onset
    odds
  confidence: strong
  method_used: Logistic regression, country-year panel, N=6,327
  finding_type: empirical
  evidence_type: quantitative
- finding_text: Ethnic fractionalization (ELF index) is NOT a significant predictor
    of civil war onset once per capita income, terrain, and state capacity are controlled
    for.
  construct_ids:
  - civil_war_onset
  - ethnic_fractionalization
  direction: 'null'
  effect_size: near zero, not statistically significant (p > .10)
  confidence: strong
  method_used: Logistic regression, country-year panel, N=6,327
  finding_type: empirical
  evidence_type: quantitative
- finding_text: Mountainous terrain significantly increases civil war onset probability.
    Log mountainous terrain has a positive and significant coefficient. Mountains
    provide insurgents with sanctuary and raise the costs of counterinsurgency.
  construct_ids:
  - civil_war_onset
  - mountainous_terrain
  direction: positive
  effect_size: moderate — one SD increase in log terrain ≈ 30% increase in onset odds
  confidence: strong
  method_used: Logistic regression, country-year panel, N=6,327
  finding_type: empirical
  evidence_type: quantitative
- finding_text: Population size (logged, lagged) increases civil war onset risk. Larger
    countries have more potential recruits and greater heterogeneity.
  construct_ids:
  - civil_war_onset
  - population_size
  direction: positive
  effect_size: moderate
  confidence: strong
  method_used: Logistic regression, country-year panel, N=6,327
  finding_type: empirical
  evidence_type: quantitative
- finding_text: Political instability (3+ point Polity change in prior 3 years) significantly
    increases civil war onset. Regime transitions create windows of vulnerability.
  construct_ids:
  - civil_war_onset
  - political_instability
  direction: positive
  effect_size: moderate to strong
  confidence: strong
  method_used: Logistic regression, country-year panel, N=6,327
  finding_type: empirical
  evidence_type: quantitative
- finding_text: Anocracy (mixed regime, Polity -5 to +5) is positively associated
    with civil war onset, consistent with the inverted-U hypothesis. Neither full
    democracies nor full autocracies have elevated onset risk compared to anocracies.
  construct_ids:
  - civil_war_onset
  - anocracy
  direction: positive
  effect_size: moderate
  confidence: moderate
  method_used: Logistic regression, country-year panel, N=6,327
  finding_type: empirical
  evidence_type: quantitative
- finding_text: Oil exporters have higher civil war onset probability. Oil rents reduce
    the need for broad-based taxation, weaken state-society ties, and may create prize-capture
    incentives for rebel groups.
  construct_ids:
  - civil_war_onset
  - oil_exporter
  direction: positive
  effect_size: moderate
  confidence: moderate
  method_used: Logistic regression, country-year panel, N=6,327
  finding_type: empirical
  evidence_type: quantitative
- finding_text: New states (independent less than 2 years) have substantially elevated
    civil war risk. State formation and decolonization create windows of institutional
    fragility.
  construct_ids:
  - civil_war_onset
  - new_state
  direction: positive
  effect_size: strong
  confidence: moderate
  method_used: Logistic regression, country-year panel, N=6,327
  finding_type: empirical
  evidence_type: quantitative
- finding_text: Noncontiguous territory increases civil war onset. Separated territories
    are harder to control militarily and may harbor aggrieved groups beyond state
    reach.
  construct_ids:
  - civil_war_onset
  - noncontiguous_territory
  direction: positive
  effect_size: moderate
  confidence: moderate
  method_used: Logistic regression, country-year panel, N=6,327
  finding_type: empirical
  evidence_type: quantitative
- finding_text: Religious fractionalization is not a significant predictor of civil
    war onset when controlled for other factors. Religion per se does not drive conflict
    risk.
  construct_ids:
  - civil_war_onset
  - religious_fractionalization
  direction: 'null'
  effect_size: not significant
  confidence: moderate
  method_used: Logistic regression, country-year panel, N=6,327
  finding_type: empirical
  evidence_type: quantitative
- finding_text: The key mechanism for civil war is insurgency feasibility, not ethnic
    grievance. Conditions that make guerrilla warfare viable (rough terrain, weak
    states, poverty for cheap recruits) matter more than ethnic diversity or polarization.
  construct_ids:
  - civil_war_onset
  - ethnic_fractionalization
  - per_capita_income
  - mountainous_terrain
  direction: conditional
  effect_size: theoretical framing, not a single coefficient
  confidence: strong
  method_used: Comparative analysis + logistic regression
  finding_type: mechanism
  evidence_type: mixed
propositions_detail: []
sources_detail:
- id: fearon_laitin_2003
  title: Ethnicity, Insurgency, and Civil War
  authors: Fearon, James D.; Laitin, David D.
  year: 2003
  doi: 10.1017/S0003055403000534
  source_type: academic_paper
playbooks_detail:
- id: quick_start
  display_name: Quick Start — Replicate Fearon & Laitin (2003) Core Findings
  description: 'Three-step analysis replicating the core Fearon & Laitin (2003) results.
    Step 1: Correlation matrix of key predictors against civil war onset. Step 2:
    Core logistic regression (income, terrain, population → onset). Step 3: Full model
    with all controls. Validates against known findings from the paper. Requires the
    conflict panel dataset to be loaded.

    '
  estimated_runtime: 30 seconds
  step_count: 3
  engines_used:
  - logistic_regression
  - correlation_matrix
download_url: /packs/fearon-laitin-2003.pax.tar.gz
download_size: 5.1 KB
weight: 7997
related_packs: []
---

# Fearon & Laitin (2003) — Praxis PAX

**"Ethnicity, Insurgency, and Civil War"**

Foundational paper challenging ethnic grievance explanations of civil war.
Finds that insurgency-opportunity factors (poverty, rough terrain, weak states,
large populations) are stronger predictors of civil war onset than ethnic or
religious diversity.

## Contents

- **1 domain:** Intra-State Conflict
- **10 constructs:** civil_war_onset, per_capita_income, mountainous_terrain,
  population_size, political_instability, anocracy, oil_exporter, new_state,
  noncontiguous_territory, religious_fractionalization
- **11 findings:** Empirical results from logistic regression on country-year panel (N=6,327)
- **10 aliases:** Covering key synonyms and operationalizations

## Source

Fearon, James D.; Laitin, David D. (2003). "Ethnicity, Insurgency, and Civil War."
*American Political Science Review* 97(1): 75-90. DOI: 10.1017/S0003055403000534

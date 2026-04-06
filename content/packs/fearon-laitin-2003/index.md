---
name: fearon-laitin-2003
title: Fearon & Laitin (2003) "Ethnicity, Insurgency, and Civil War"
version: 1.0.0
pax_type: paper
description: Fearon & Laitin (2003) "Ethnicity, Insurgency, and Civil War" — foundational
  paper on civil war onset. Challenges ethnic grievance explanations, finds insurgency-opportunity
  factors (poverty, terrain, weak states) are stronger predictors.
author: ''
created: ''
license: ''
tags:
- paper
constructs:
- mountainous_terrain
- political_instability
- noncontiguous_territory
- oil_exporter
- new_state
- religious_fractionalization
- per_capita_income
- population_size
- anocracy
- civil_war_onset
engines: []
playbook_names:
- quick_start
construct_count: 10
finding_count: 0
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: intra_state_conflict
  display_name: Intra-State Conflict
  description: Study of civil war onset, duration, and termination within sovereign
    states. Examines structural, economic, political, and geographic determinants
    of armed conflict.
  research_questions: []
  temporal_scope: 1945-present
  population: Sovereign states (country-year observations)
  level_of_analysis: macro
constructs_detail:
- id: mountainous_terrain
  display_name: Mountainous Terrain
  definition: Percentage of a country's territory that is mountainous, per the Geomorphic
    Units of the World dataset. Logged in regression models. Higher values increase
    insurgency viability by providing rebel sanctuary.
  aliases: []
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
  aliases: []
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
- id: civil_war_onset
  display_name: Civil War Onset
  definition: 'Binary indicator: 1 if a civil war began in this country-year, 0 otherwise.
    Fearon & Laitin define civil wars as internal conflicts with organized violence,
    at least 1,000 battle deaths, and effective resistance by both sides.'
  aliases: []
  construct_type: quantifiable
findings_detail: []
propositions_detail: []
sources_detail: []
playbooks_detail: []
download_url: https://pax-market.com/packs/fearon-laitin-2003.pax.tar.gz
download_size: 2.4 KB
published_by: Praxis Agent
related_packs: []
pax_name: fearon-laitin-2003
weight: 10000
---

**Domain:** Intra-State Conflict

Study of civil war onset, duration, and termination within sovereign states. Examines structural, economic, political, and geographic determinants of armed conflict.

**Temporal scope:** 1945-present | **Population:** Sovereign states (country-year observations)

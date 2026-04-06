---
name: state-fragility
title: State Fragility
version: 1.0.2
pax_type: topic
description: 'State fragility: measurement, determinants, and prediction of state
  weakness, institutional collapse, and crisis pathways. Bridges conflict, food insecurity,
  governance, climate, and economic domains.'
author: ''
created: '2026-04-06'
license: ''
tags:
- topic
- state-fragility
constructs:
- state_fragility_index
- institutional_capacity
- economic_resilience
- security_apparatus_strength
- legitimacy_deficit
- demographic_pressure
- refugee_displacement
- external_intervention_fragility
- group_grievance
- factionalized_elites
- public_services_decline
- human_flight_brain_drain
engines:
- logistic_regression
- random_forest
playbook_names:
- quick_start
construct_count: 12
finding_count: 5
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: conflict_event_counts
  display_name: Conflict Event Counts
  description: Determinants of the frequency and intensity of political violence events,
    protests, and armed conflict incidents
  research_questions: []
  temporal_scope: null
  population: Countries and subnational regions
  level_of_analysis: macro
constructs_detail:
- id: state_fragility_index
  display_name: State Fragility Index
  definition: A composite measure of state weakness capturing effectiveness and legitimacy
    across security, political, economic, and social dimensions.
  aliases: []
  construct_type: composite
- id: institutional_capacity
  display_name: Institutional Capacity
  definition: Government effectiveness and bureaucratic quality — the ability of the
    state to formulate and implement policy. Operationalized via WGI Government Effectiveness
    score or CPIA. Low capacity amplifies all other fragility drivers.
  aliases: []
  construct_type: quantifiable
- id: economic_resilience
  display_name: Economic Resilience
  definition: Capacity of a state economy to absorb and recover from shocks — measured
    by GDP volatility, fiscal space (debt-to-GDP), foreign reserves, and export diversification.
    Low resilience states are coup-prone and food-crisis-prone.
  aliases: []
  construct_type: quantifiable
- id: security_apparatus_strength
  display_name: Security Apparatus Strength
  definition: 'Fragile States Index sub-indicator measuring internal security threats:
    state monopoly on force, politically motivated violence, arms proliferation, insurgency,
    and civil unrest. Higher values indicate greater security fragility.'
  aliases: []
  construct_type: quantifiable
- id: legitimacy_deficit
  display_name: Legitimacy Deficit
  definition: 'Fragile States Index sub-indicator: public confidence in state institutions,
    corruption perceptions, political participation restrictions, and regime contestation.
    States with large legitimacy deficits face elevated coup and revolution risk.'
  aliases: []
  construct_type: quantifiable
- id: demographic_pressure
  display_name: Demographic Pressure
  definition: 'Population-driven stress: youth bulge (15-29 age cohort > 20% of population),
    rapid urbanization, food/water scarcity per capita, and disease burden. Youth
    bulges are robustly associated with conflict onset (Urdal 2006).'
  aliases: []
  construct_type: quantifiable
- id: refugee_displacement
  display_name: Refugee & IDP Displacement
  definition: Total forcibly displaced population (refugees + internally displaced
    persons) as count or per capita. Both cause and consequence of state fragility
    — displacement strains host communities, creates governance vacuums, and indicates
    state failure to protect.
  aliases: []
  construct_type: quantifiable
- id: external_intervention_fragility
  display_name: External Intervention
  definition: Degree of foreign involvement in state affairs — military intervention,
    peacekeeping presence, foreign aid dependency (ODA as % of GNI), and sanctions.
    High external intervention signals inability to self-govern and can entrench fragility.
  aliases: []
  construct_type: quantifiable
- id: group_grievance
  display_name: Group Grievance
  definition: 'Fragile States Index sub-indicator: ethnic, religious, or communal
    tensions and violence, including historical atrocities and discrimination. Captures
    the mobilizable resentment that can be weaponized for conflict.'
  aliases: []
  construct_type: quantifiable
- id: factionalized_elites
  display_name: Factionalized Elites
  definition: 'Fragile States Index sub-indicator: elite competition, power-sharing
    breakdown, defections, and brinksmanship. Factionalized elites are a proximate
    trigger for coups, civil war, and state collapse.'
  aliases: []
  construct_type: quantifiable
- id: public_services_decline
  display_name: Public Services Decline
  definition: 'Deterioration in essential state services: health system capacity,
    education access, infrastructure maintenance, and social safety nets. Measured
    via FSI sub-indicator or composite of WDI health/education spending.'
  aliases: []
  construct_type: quantifiable
- id: human_flight_brain_drain
  display_name: Human Flight & Brain Drain
  definition: Emigration of educated/skilled population and economic displacement.
    FSI sub-indicator capturing the loss of human capital that further degrades state
    capacity and economic prospects.
  aliases: []
  construct_type: quantifiable
findings_detail:
- finding_text: 'The PITF global instability model achieves ~80% accuracy in forecasting
    state instability onset 2 years ahead using only 4 variables: regime type (partial
    autocracy with factionalism), infant mortality rate, armed conflict in 4+ neighboring
    states, and state-led discrimination. Partial democracies with factionalism are
    the single strongest predictor.'
  construct_ids:
  - state_fragility_index
  - factionalized_elites
  - demographic_pressure
  direction: positive
  effect_size: null
  confidence: strong
  method_used: Logistic regression, global country-year panel 1955-2003
- finding_text: Youth bulges (ages 15-24 exceeding 35% of adult population) significantly
    increase the risk of armed conflict onset, low-intensity conflict, and terrorism.
    A 1 percentage point increase in youth share raises conflict risk by ~7%. Effect
    is strongest in low-income countries with limited economic opportunities.
  construct_ids:
  - demographic_pressure
  - state_fragility_index
  direction: positive
  effect_size: null
  confidence: strong
  method_used: Negative binomial regression, country-year panel 1950-2000
- finding_text: Infant mortality rate (a proxy for state capacity and development)
    is the second strongest predictor in the PITF model after regime type. Countries
    with infant mortality above the global median face ~2.5x higher instability risk,
    reflecting the deep link between public health capacity and state resilience.
  construct_ids:
  - state_fragility_index
  - public_services_decline
  - demographic_pressure
  direction: positive
  effect_size: null
  confidence: strong
  method_used: Logistic regression, global country-year panel 1955-2003
- finding_text: The concept of 'failed states' is analytically misleading — states
    rarely fail across all dimensions simultaneously. Call proposes distinguishing
    between 'collapsed states' (no central authority), 'weak states' (low capacity
    but functional), and 'war-torn states' (conflict-degraded). Most so-called failed
    states retain significant institutional capacity in some domains.
  construct_ids:
  - state_fragility_index
  - institutional_capacity
  direction: conditional
  effect_size: null
  confidence: moderate
  method_used: Conceptual analysis, comparative case studies
- finding_text: 'State fragility shows strong path dependence: countries in the ''Alert''
    category (FSI > 90) have a >80% probability of remaining in that category the
    following year. Escape from deep fragility requires sustained multi-dimensional
    improvement. The average time to move from Alert to Warning category is ~15 years.'
  construct_ids:
  - state_fragility_index
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: Longitudinal tracking of FSI scores 2006-2024
propositions_detail: []
sources_detail:
- id: fund_for_peace_fsi_2024
  title: Fragile States Index 2024
  authors: Fund for Peace
  year: 2024
  doi: null
  source_type: dataset
- id: goldstone_et_al_2010
  title: A Global Model for Forecasting Political Instability
  authors: Jack Goldstone et al.
  year: 2010
  doi: 10.1111/j.1540-5907.2009.00426.x
  source_type: journal_article
- id: call_2011
  title: 'Beyond the Failed State: Toward Conceptual Alternatives'
  authors: Charles T. Call
  year: 2011
  doi: 10.1177/1354066110383437
  source_type: journal_article
- id: urdal_2006
  title: A Clash of Generations? Youth Bulges and Political Violence
  authors: Henrik Urdal
  year: 2006
  doi: 10.1177/0738894206290079
  source_type: journal_article
playbooks_detail: []
download_url: https://pax-market.com/packs/state-fragility.pax.tar.gz
download_size: 4.2 KB
published_by: Praxis Agent
related_packs: []
pax_name: state-fragility
weight: 7974
---

**Domain:** Conflict Event Counts

Determinants of the frequency and intensity of political violence events, protests, and armed conflict incidents

**Population:** Countries and subnational regions

## Key Findings

- The PITF global instability model achieves ~80% accuracy in forecasting state instability onset 2 years ahead using only 4 variables: regime type (partial autocracy with factionalism), infant mortality rate, armed conflict in 4+ neighboring states, and state-led discrimination. Partial democracies with factionalism are the single strongest predictor. *(positive, strong)*
- Youth bulges (ages 15-24 exceeding 35% of adult population) significantly increase the risk of armed conflict onset, low-intensity conflict, and terrorism. A 1 percentage point increase in youth share raises conflict risk by ~7%. Effect is strongest in low-income countries with limited economic opportunities. *(positive, strong)*
- Infant mortality rate (a proxy for state capacity and development) is the second strongest predictor in the PITF model after regime type. Countries with infant mortality above the global median face ~2.5x higher instability risk, reflecting the deep link between public health capacity and state resilience. *(positive, strong)*
- The concept of 'failed states' is analytically misleading — states rarely fail across all dimensions simultaneously. Call proposes distinguishing between 'collapsed states' (no central authority), 'weak states' (low capacity but functional), and 'war-torn states' (conflict-degraded). Most so-called failed states retain significant institutional capacity in some domains. *(conditional, moderate)*
- State fragility shows strong path dependence: countries in the 'Alert' category (FSI > 90) have a >80% probability of remaining in that category the following year. Escape from deep fragility requires sustained multi-dimensional improvement. The average time to move from Alert to Warning category is ~15 years. *(positive, moderate)*

---
name: cao-2025-personalist-rebel-sponsorship
title: Cao 2025 Personalist Rebel Sponsorship
version: 1.0.0
pax_type: paper
description: 'Investigates when external sponsor states provide direct combat support
  to rebel groups in civil conflicts. Argues that personalist regime type of the target
  state drives sponsors toward troop/combat support (vs. other forms) through three
  mechanisms: perception of the target as aggressive and unreliable, military ineffectiveness
  due to coup-proofing, and international isolation reducing reputational costs. Tests
  against NAGs triad-year data 1945-2010. Unit of analysis: sponsor-rebel group-target
  triad-year.'
author: ''
created: ''
license: ''
tags:
- paper
constructs:
- combat-support
- rebel-sponsorship
- internal-constraints
- coup-proofing
- interstate-rivalry
- international-isolation
- personalist-regime
- military-effectiveness
engines:
- negative_binomial_regression
- trend_analysis
- descriptive_frequency_analysis
- binary_logit_target_initiation_and_ordinal_logit_hostility_level
- binary_logit_with_cubic_splines
playbook_names:
- quick_start
construct_count: 8
finding_count: 0
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: civil-war-rebel-sponsorship
  display_name: Civil War Rebel Sponsorship and Regime Type
  description: The study of how target state regime characteristics — specifically
    personalism — shape the type and intensity of external support that sponsor states
    provide to rebel groups in civil conflicts. Covers triadic sponsor-rebel-target
    relationships in intrastate conflicts, 1945-2010.
  research_questions: []
  temporal_scope: 1945-2010
  population: Triadic relationships between sponsor states, rebel groups, and target
    states in active civil conflicts, 1945-2010
  level_of_analysis: macro
constructs_detail:
- id: combat-support
  display_name: Combat Support for Rebels
  definition: 'Direct military intervention by a sponsor state in a civil conflict,
    involving deployment of troops to fight alongside rebel forces against the target
    government. Represents the highest level of sponsor involvement and provides direct
    control over the conflict process. Coded 2 in the NAGs support typology (vs. 1
    for material/logistical support, 0 for no support). Predicted probability: ~2%
    for non-personalist targets, ~6.6% for personalist targets (230% increase).'
  aliases: []
  construct_type: outcome
- id: rebel-sponsorship
  display_name: Rebel Sponsorship (General)
  definition: Any form of external state support provided to rebel groups in civil
    conflicts, including material resources (weapons, financing), logistical support
    (safe haven, training camps, transport), and direct combat support. Emergence
    of sponsorship is not predicted by personalism (H2); only the type of sponsorship
    varies.
  aliases: []
  construct_type: outcome
- id: internal-constraints
  display_name: Internal Constraints on Leader
  definition: The degree to which a leader faces meaningful checks from domestic political
    elites, military officers, or party structures that limit unilateral foreign policy
    decisions. High under institutionalized regimes (party-based, military junta,
    monarchy); minimal under personalist rule where other elites lack independent
    power bases to challenge the leader.
  aliases: []
  construct_type: concept
- id: coup-proofing
  display_name: Coup-Proofing
  definition: 'Strategies adopted by authoritarian leaders to neutralize military
    threats to their rule: creating parallel security forces with conflicting jurisdictions,
    frequent purges of senior officers, loyalty-based promotions over competence,
    restricting inter-unit coordination, and appointing ethnic/family loyalists to
    command positions. Effective at reducing coup risk but systematically degrades
    military cohesion and battlefield effectiveness.'
  aliases: []
  construct_type: process
- id: interstate-rivalry
  display_name: Interstate Rivalry
  definition: A persistent, militarized dispute relationship between two states characterized
    by repeated conflicts, mutual threat perception, and ongoing competition. Operationalized
    as binary indicator from Goertz, Diehl & Balas (2016) peace and rivalry dataset.
    Strong positive predictor of both general rebel sponsorship emergence and combat
    support provision. Sponsoring rebels is an indirect, lower-cost strategy for rivals
    to weaken each other.
  aliases: []
  construct_type: quantifiable
- id: international-isolation
  display_name: International Isolation of Target
  definition: The degree to which the target state is excluded from international
    economic, diplomatic, and military networks. Personalist regimes tend toward greater
    isolation due to limited trade openness, fewer stable alliances, and repressive
    practices that draw international condemnation. Reduces the reputational cost
    for sponsors of directly intervening in the target's civil conflict.
  aliases: []
  construct_type: concept
- id: personalist-regime
  display_name: Personalist Regime
  definition: 'A regime type in which power is concentrated in a single leader who
    dominates both the military and party (if any), with weak formal institutions
    and no independent elite power bases. Operationalized as: (1) binary indicator
    from GWF typology (Geddes, Wright & Frantz 2014) distinguishing personalist from
    all other regime types including democracies; (2) continuous latent personalism
    index 0-1 (Geddes, Wright & Frantz 2018) covering 118 authoritarian regimes 1946-2010.'
  aliases: []
  construct_type: quantifiable
- id: military-effectiveness
  display_name: Military Effectiveness
  definition: 'The battlefield capacity of state armed forces, including command coordination,
    tactical competence, and ability to generate intelligence and civilian cooperation.
    Systematically reduced under personalist regimes due to coup-proofing strategies.
    Acts as partial mediator between personalism and combat support: weaker target
    militaries lower the cost and risk of sponsor troop intervention.'
  aliases: []
  construct_type: quantifiable
findings_detail: []
propositions_detail: []
sources_detail: []
playbooks_detail: []
download_url: https://pax-market.com/packs/cao-2025-personalist-rebel-sponsorship.pax.tar.gz
download_size: 3.0 KB
published_by: Praxis Agent
related_packs: []
pax_name: cao-2025-personalist-rebel-sponsorship
weight: 10000
---

**Domain:** Civil War Rebel Sponsorship and Regime Type

The study of how target state regime characteristics — specifically personalism — shape the type and intensity of external support that sponsor states provide to rebel groups in civil conflicts. Covers triadic sponsor-rebel-target relationships in intrastate conflicts, 1945-2010.

**Temporal scope:** 1945-2010 | **Population:** Triadic relationships between sponsor states, rebel groups, and target states in active civil conflicts, 1945-2010

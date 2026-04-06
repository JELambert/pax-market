---
name: rebel-sponsorship-civilian-abuse
title: Rebel Sponsorship Civilian Abuse
version: 1.0.0
pax_type: paper
description: Explains why externally sponsored rebel groups engage in more civilian
  abuse through a principal-agent framework. External funding creates moral hazard
  by reducing rebel need for civilian cooperation; but sponsor characteristics (democracy,
  human rights lobbies) and competition among multiple principals moderate this effect.
  Tested with negative binomial regression on count data of one-sided violence, dyad-year
  structure.
author: ''
created: ''
license: ''
tags:
- paper
constructs:
- external-funding-moral-hazard
- sponsor-democracy
- multiple-principals
- human-rights-lobby
- civilian-abuse
engines:
- negative_binomial_regression
- negative_binomial_regression_with_interaction_term
- negative_binomial_regression_nbreg
playbook_names:
- quick_start
construct_count: 5
finding_count: 0
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: rebel-civilian-violence
  display_name: Rebel Civilian Violence and Accountability
  description: The study of how rebel groups decide to target or spare civilians,
    with focus on how external sponsorship affects these incentives through principal-agent
    dynamics. Covers one-sided violence, atrocity commission, and civilian victimization
    by non-state armed groups.
  research_questions: []
  temporal_scope: Post-Cold War period
  population: Rebel group-years with active conflict and potential external state
    sponsorship
  level_of_analysis: meso
constructs_detail:
- id: external-funding-moral-hazard
  display_name: External Funding Moral Hazard
  definition: The mechanism by which external state funding reduces rebel incentives
    to maintain civilian cooperation. Rebels relying on external resources no longer
    need to extract resources from the population through taxation or civilian support
    networks, reducing the cost-benefit calculus that otherwise deters mass atrocities.
    Creates agency slack in the principal-agent relationship between sponsor and rebel.
  aliases: []
  construct_type: process
- id: sponsor-democracy
  display_name: Sponsor Democracy
  definition: Binary indicator for whether a rebel group's external sponsor is a democracy
    (democ_supdum), or continuous proportion of democratic sponsors (perc_dem). Democratic
    sponsors are more sensitive to human rights concerns and face stronger domestic
    accountability pressures, making them more likely to condition support on rebel
    restraint of civilian targeting. Moderates the negative effect of external funding
    on civilian safety.
  aliases: []
  construct_type: quantifiable
- id: multiple-principals
  display_name: Number of External Sponsors
  definition: 'Count of distinct state actors providing external support to a rebel
    group (num_supp). Multiple principals create a collective action problem: no single
    sponsor can effectively monitor and discipline the rebel agent, each free-riding
    on others'' oversight efforts. Higher values associated with more civilian abuse
    due to reduced effective monitoring.'
  aliases: []
  construct_type: quantifiable
- id: human-rights-lobby
  display_name: Human Rights Lobby Strength
  definition: Count of human rights organization secretariats in the sponsor state
    (hrosecretariat_sum). States with stronger human rights advocacy sectors face
    greater domestic pressure to condition foreign support on rebels' conduct toward
    civilians. Operationalizes the 'principled' dimension of sponsor oversight beyond
    formal democratic institutions.
  aliases: []
  construct_type: quantifiable
- id: civilian-abuse
  display_name: Civilian Abuse by Rebel Groups
  definition: Count of civilian fatalities from one-sided violence perpetrated by
    rebel organizations (UCDP One-Sided Violence dataset). Operationalized as 'best
    estimate' of annual civilian deaths (rebbest). Overdispersed count variable modeled
    with negative binomial regression. Key dependent variable for testing how external
    sponsorship affects rebel restraint of violence against noncombatants.
  aliases: []
  construct_type: outcome
findings_detail: []
propositions_detail: []
sources_detail: []
playbooks_detail: []
download_url: https://pax-market.com/pax/rebel-sponsorship-civilian-abuse.pax.tar.gz
download_size: 2.3 KB
published_by: Praxis Agent
related_packs: []
pax_name: rebel-sponsorship-civilian-abuse
weight: 10000
---

**Domain:** Rebel Civilian Violence and Accountability

The study of how rebel groups decide to target or spare civilians, with focus on how external sponsorship affects these incentives through principal-agent dynamics. Covers one-sided violence, atrocity commission, and civilian victimization by non-state armed groups.

**Temporal scope:** Post-Cold War period | **Population:** Rebel group-years with active conflict and potential external state sponsorship

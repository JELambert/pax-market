---
name: dukalskis-et-al-2024-transnational-repression
title: Dukalskis Et Al 2024 Transnational Repression
version: 1.0.0
pax_type: paper
description: First large-N quantitative study of domestic drivers of transnational
  repression (TR). Tests the hypothesis that authoritarian crackdowns at home increase
  the subsequent likelihood of the same state repressing its citizens abroad. Uses
  the Authoritarian Actions Abroad Database (AAAD, ~1,205 events, 1991-2019) across
  88 authoritarian regimes in a country-year panel.
author: ''
created: ''
license: ''
tags:
- paper
constructs:
- transnational_repression_binary
- transnational_repression_count
- domestic_repression_cli
- diplomatic_capacity_abroad
- state_capacity_latent
- polity_score
- leader_tenure
engines:
- logistic_regression
- ols_regression
playbook_names:
- quick_start
construct_count: 7
finding_count: 0
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: transnational_repression
  display_name: Transnational Repression
  description: The extraterritorial use of coercive tactics by authoritarian states
    to silence, monitor, threaten, abduct, extradite, or assassinate dissidents and
    regime opponents beyond their national borders. Encompasses threats, arrests,
    extraditions, abductions, family harassment, and assassination. TR is distinct
    from domestic repression and from targeting foreign citizens.
  research_questions: []
  temporal_scope: 1991-2019
  population: Authoritarian states with diaspora populations, country-year panel,
    1991-2019
  level_of_analysis: macro
constructs_detail:
- id: transnational_repression_binary
  display_name: Transnational Repression (Binary)
  definition: 'Binary indicator equal to 1 if an authoritarian state carried out one
    or more transnational repression events (threats, arrests, extraditions, abductions,
    assassinations) against its own citizens abroad in a given country-year, 0 otherwise.
    Source: AAAD (Dukalskis 2021).'
  aliases: []
  construct_type: outcome
- id: transnational_repression_count
  display_name: Transnational Repression (Count)
  definition: 'Count of transnational repression events carried out by an authoritarian
    state against its own citizens abroad in a given country-year. Ranges from 0 to
    61 (Uzbekistan 2005). Source: AAAD (Dukalskis 2021).'
  aliases: []
  construct_type: outcome
- id: domestic_repression_cli
  display_name: Domestic Repression (V-Dem CLI)
  definition: 'Inverted V-Dem Civil Liberties Index (CLI), measuring the intensity
    of domestic state repression. The CLI aggregates three component indices: physical
    violence index (torture, killings), political civil liberties index (censorship,
    parties, civil society), and private civil liberties index (forced labor, property
    rights, religion). Higher values indicate more repression. Lagged one year in
    analysis. Source: V-Dem v12, Coppedge et al. 2022.'
  aliases: []
  construct_type: quantifiable
- id: diplomatic_capacity_abroad
  display_name: Diplomatic Representation Abroad
  definition: 'Number of diplomatic representations (embassies, consulates, and other
    missions) a state maintains abroad in a given year. Captures the logistical infrastructure
    enabling a state to project repression transnationally. Source: Diplometrics Diplomatic
    Representation dataset (Moyer et al. 2021), 1960-2020. Mean in sample: 50.8, range:
    1-170.'
  aliases: []
  construct_type: quantifiable
- id: state_capacity_latent
  display_name: State Capacity Index
  definition: 'Latent measure of state capacity aggregating 21 variables across three
    conceptual pillars: extractive capacity, coercive capacity, and administrative
    capacity. Estimated via item response theory model. Source: Hanson and Sigman
    (2021), State Capacity Dataset v1. Mean in sample: -0.059, range: -1.541 to 1.28.'
  aliases: []
  construct_type: quantifiable
- id: polity_score
  display_name: Polity Score
  definition: 'Revised combined Polity score measuring level of authoritarianism/democracy
    on a scale from -10 (full autocracy) to +10 (full democracy). Used as control
    for regime type. Source: Marshall and Gurr (2020). Mean in sample: -4.46.'
  aliases: []
  construct_type: quantifiable
- id: leader_tenure
  display_name: Leader Tenure (Log)
  definition: 'Log of the incumbent ruler''s cumulative time in office (years). Controls
    for the possibility that crackdowns occur around regime consolidation periods
    and that repression spikes during transitions. Source: Bell, Besaw, and Frank
    (2021). Mean: 4.60 log-years.'
  aliases: []
  construct_type: quantifiable
findings_detail: []
propositions_detail: []
sources_detail: []
playbooks_detail: []
download_url: https://pax-market.com/pax/dukalskis-et-al-2024-transnational-repression.pax.tar.gz
download_size: 2.4 KB
published_by: Praxis Agent
related_packs: []
pax_name: dukalskis-et-al-2024-transnational-repression
weight: 10000
---

**Domain:** Transnational Repression

The extraterritorial use of coercive tactics by authoritarian states to silence, monitor, threaten, abduct, extradite, or assassinate dissidents and regime opponents beyond their national borders. Encompasses threats, arrests, extraditions, abductions, family harassment, and assassination. TR is distinct from domestic repression and from targeting foreign citizens.

**Temporal scope:** 1991-2019 | **Population:** Authoritarian states with diaspora populations, country-year panel, 1991-2019

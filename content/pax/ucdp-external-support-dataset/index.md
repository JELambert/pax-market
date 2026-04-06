---
name: ucdp-external-support-dataset
title: UCDP External Support Dataset
version: 1.0.0
pax_type: paper
description: 'Introduces the UCDP External Support Dataset (ESD) covering external
  support to warring parties in armed conflicts 1975-2017. Presents three key empirical
  trends: dramatic increase in number of supporters, shift to pro-government interventions
  post-9/11, and rise of direct military intervention as predominant support mode.
  Supersedes the Högbladh, Pettersson & Themnér (2011) dataset with expanded coverage
  including non-state supporters and ten support type dimensions.'
author: ''
created: ''
license: ''
tags:
- paper
constructs:
- external-support-prevalence
- pro-government-intervention
- direct-military-intervention
- multilateral-support-coalition
- non-state-supporter
engines:
- descriptive_frequency_analysis
- frequency_tabulation_by_support_type_and_recipient_type
- trend_analysis
- time_series_frequency_analysis
playbook_names:
- quick_start
construct_count: 5
finding_count: 0
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: external-support-measurement
  display_name: External Support Measurement and Trends
  description: The study of empirical patterns and measurement infrastructure for
    external support in armed conflicts. Covers dataset construction, coding decisions,
    prevalence estimates, and secular trends in the type, direction, and multilateral
    nature of external support provision globally.
  research_questions: []
  temporal_scope: 1975-2017
  population: All state-based armed conflicts worldwide, 1975-2017
  level_of_analysis: macro
constructs_detail:
- id: external-support-prevalence
  display_name: External Support Prevalence
  definition: 'The share of armed conflict-dyads or intrastate conflicts that receive
    at least one form of external support from state or non-state actors in a given
    time period. ESD documents: 80% of all intrastate conflicts (1975-2017) received
    external support; 72% of interstate conflicts. External support is the rule, not
    the exception, in modern armed conflict.'
  aliases: []
  construct_type: quantifiable
- id: pro-government-intervention
  display_name: Pro-Government Intervention
  definition: External support provided to government forces (rather than rebel groups)
    in intrastate conflicts. After 9/11, the share of conflict-dyads with exclusively
    rebel-sided support fell to near zero by 2016, while government-sided support
    reached 77% of all active conflict-dyads by 2017. Reflects the international anti-terrorism
    norm shift that reframed rebel groups as terrorist organizations.
  aliases: []
  construct_type: quantifiable
- id: direct-military-intervention
  display_name: Direct Military Intervention (Troop Deployment)
  definition: External support involving deployment of foreign troops for combat operations
    on behalf of a recipient party. Coded separately from indirect support (weapons,
    training, funding, intelligence, logistics). Direct intervention first exceeded
    indirect support in 2015 and continues to grow. Conceptually distinct from delegation/orchestration
    framing by requiring actual combat role.
  aliases: []
  construct_type: quantifiable
- id: multilateral-support-coalition
  display_name: Multilateral Support Coalition
  definition: Three or more states coordinating their provision of external support
    to achieve a common goal. Coalition-based support was rare before 2001 (Gulf War
    Coalition 1990-91 is the first recorded instance) but grew dramatically after
    9/11, reaching nearly one-third of all support instances by 2017. Implications
    for effective principal discipline over rebel recipients.
  aliases: []
  construct_type: quantifiable
- id: non-state-supporter
  display_name: Non-State External Supporter
  definition: An armed opposition organization or rebel group that provides external
    support to another warring party in a different conflict. ESD is the first global
    dataset to systematically track non-state actors as supporters (not just recipients).
    Non-state supporters peaked at 38 active groups in 2012 (including al-Shabaab
    training Boko Haram). More than a quarter of all support to rebel groups comes
    from non-state actors.
  aliases: []
  construct_type: quantifiable
findings_detail: []
propositions_detail: []
sources_detail: []
playbooks_detail: []
download_url: https://pax-market.com/pax/ucdp-external-support-dataset.pax.tar.gz
download_size: 2.3 KB
published_by: Praxis Agent
related_packs: []
pax_name: ucdp-external-support-dataset
weight: 10000
---

**Domain:** External Support Measurement and Trends

The study of empirical patterns and measurement infrastructure for external support in armed conflicts. Covers dataset construction, coding decisions, prevalence estimates, and secular trends in the type, direction, and multilateral nature of external support provision globally.

**Temporal scope:** 1975-2017 | **Population:** All state-based armed conflicts worldwide, 1975-2017

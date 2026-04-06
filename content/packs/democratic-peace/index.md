---
name: democratic-peace
title: Democratic peace theory
version: 1.0.0
pax_type: topic
description: Democratic peace theory — why democracies rarely fight each other and
  how regime type, economic interdependence, and international organizations jointly
  reduce militarized interstate disputes. Built on Doyle (1986), Maoz & Russett (1993),
  Oneal & Russett (1999), and Gartzke (2007).
author: ''
created: ''
license: ''
tags:
- topic
constructs:
- dyadic_democracy
- militarized_interstate_dispute
- trade_interdependence
- shared_igo_membership
- territorial_contiguity
- capability_ratio
engines:
- logistic_regression
- ols_regression
- cox_ph
playbook_names:
- quick_start
construct_count: 6
finding_count: 0
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: democratic_peace
  display_name: Democratic Peace
  description: Study of why democracies rarely fight each other and how regime type,
    trade interdependence, and IGO membership jointly reduce interstate conflict probability.
  research_questions: []
  temporal_scope: 1885-present
  population: Directed and non-directed dyad-year observations of sovereign state
    pairs
  level_of_analysis: dyadic
constructs_detail:
- id: dyadic_democracy
  display_name: Dyadic Democracy Score
  definition: 'The Polity IV score of the less democratic state in a dyad. Captures
    the binding constraint: a dyad is only jointly democratic if both members clear
    the threshold.'
  aliases: []
  construct_type: quantifiable
- id: militarized_interstate_dispute
  display_name: Militarized Interstate Dispute Onset
  definition: 'Binary indicator: 1 if a dyad experienced MID onset in a given year,
    per the COW MID dataset.'
  aliases: []
  construct_type: outcome
- id: trade_interdependence
  display_name: Bilateral Trade Interdependence
  definition: The lower of the two states' ratios of bilateral trade to GDP, capturing
    the dyadic member with least to gain from trade continuity.
  aliases: []
  construct_type: quantifiable
- id: shared_igo_membership
  display_name: Shared IGO Memberships
  definition: Count of intergovernmental organizations to which both states belong
    simultaneously.
  aliases: []
  construct_type: quantifiable
- id: territorial_contiguity
  display_name: Territorial Contiguity
  definition: Binary indicator of whether two states share a land border or narrow
    sea corridor. Standard opportunity control.
  aliases: []
  construct_type: quantifiable
- id: capability_ratio
  display_name: Dyadic Capability Ratio
  definition: Ratio of the stronger state's CINC score to the sum of both states'
    CINC scores, capturing power asymmetry.
  aliases: []
  construct_type: quantifiable
findings_detail: []
propositions_detail: []
sources_detail: []
playbooks_detail: []
download_url: https://pax-market.com/packs/democratic-peace.pax.tar.gz
download_size: 1.7 KB
published_by: Praxis Agent
related_packs: []
pax_name: democratic-peace
weight: 10000
---

**Domain:** Democratic Peace

Study of why democracies rarely fight each other and how regime type, trade interdependence, and IGO membership jointly reduce interstate conflict probability.

**Temporal scope:** 1885-present | **Population:** Directed and non-directed dyad-year observations of sovereign state pairs

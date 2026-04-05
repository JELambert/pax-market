---
title: Democratic peace theory
pax_name: democratic-peace
version: 1.0.0
pax_type: topic
description: Democratic peace theory — why democracies rarely fight each other and
  how regime type, economic interdependence, and international organizations jointly
  reduce militarized interstate disputes. Built on Doyle (1986), Maoz & Russett (1993),
  Oneal & Russett (1999), and Gartzke (2007).
author: Doyle, Michael W.; Russett, Bruce M.; Oneal, John R.; Maoz, Zeev; Gartzke,
  Erik
created: '2026-04-04'
license: ''
tags:
- topic
- democratic-peace
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
finding_count: 5
proposition_count: 0
has_playbooks: true
has_data_sources: true
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
  aliases:
  - joint democracy
  - DEML
  construct_type: quantifiable
- id: militarized_interstate_dispute
  display_name: Militarized Interstate Dispute Onset
  definition: 'Binary indicator: 1 if a dyad experienced MID onset in a given year,
    per the COW MID dataset.'
  aliases:
  - MID onset
  - dyadic conflict onset
  construct_type: outcome
- id: trade_interdependence
  display_name: Bilateral Trade Interdependence
  definition: The lower of the two states' ratios of bilateral trade to GDP, capturing
    the dyadic member with least to gain from trade continuity.
  aliases:
  - economic interdependence
  - TRADEDEPL
  construct_type: quantifiable
- id: shared_igo_membership
  display_name: Shared IGO Memberships
  definition: Count of intergovernmental organizations to which both states belong
    simultaneously.
  aliases:
  - joint IGO membership
  - institutional embeddedness
  construct_type: quantifiable
- id: territorial_contiguity
  display_name: Territorial Contiguity
  definition: Binary indicator of whether two states share a land border or narrow
    sea corridor. Standard opportunity control.
  aliases:
  - shared border
  - geographic proximity
  construct_type: quantifiable
- id: capability_ratio
  display_name: Dyadic Capability Ratio
  definition: Ratio of the stronger state's CINC score to the sum of both states'
    CINC scores, capturing power asymmetry.
  aliases:
  - power asymmetry
  - CINC ratio
  construct_type: quantifiable
findings_detail:
- finding_text: Jointly democratic dyads are significantly less likely to experience
    MIDs than mixed or autocratic dyads, 1946-1986.
  construct_ids:
  - dyadic_democracy
  - militarized_interstate_dispute
  direction: negative
  effect_size: ''
  confidence: strong
  method_used: Logistic regression, dyad-year panel
  finding_type: ''
  evidence_type: ''
- finding_text: Dyadic democracy significantly reduces MID onset probability across
    1885-1992, robust to controls for capability ratio, contiguity, alliance ties,
    and other Kantian variables.
  construct_ids:
  - dyadic_democracy
  - militarized_interstate_dispute
  direction: negative
  effect_size: ''
  confidence: strong
  method_used: Logistic regression with cubic spline
  finding_type: ''
  evidence_type: ''
- finding_text: Bilateral trade interdependence independently reduces dyadic MID onset,
    net of democracy and IGO membership.
  construct_ids:
  - trade_interdependence
  - militarized_interstate_dispute
  direction: negative
  effect_size: ''
  confidence: strong
  method_used: Logistic regression
  finding_type: ''
  evidence_type: ''
- finding_text: Shared IGO membership count significantly reduces dyadic MID onset,
    net of democracy and trade.
  construct_ids:
  - shared_igo_membership
  - militarized_interstate_dispute
  direction: negative
  effect_size: ''
  confidence: moderate
  method_used: Logistic regression
  finding_type: ''
  evidence_type: ''
- finding_text: When financial market integration and aligned state preferences are
    controlled, democratic peace coefficient is substantially attenuated and loses
    significance in some specifications.
  construct_ids:
  - dyadic_democracy
  - trade_interdependence
  - militarized_interstate_dispute
  direction: 'null'
  effect_size: ''
  confidence: moderate
  method_used: Logistic regression, dyad-year panel
  finding_type: ''
  evidence_type: ''
propositions_detail: []
sources_detail:
- id: doyle_1986
  title: Liberalism and World Politics
  authors: Doyle, Michael W.
  year: 1986
  doi: null
  source_type: academic_paper
- id: maoz_russett_1993
  title: Normative and Structural Causes of Democratic Peace, 1946-1986
  authors: Maoz, Zeev; Russett, Bruce M.
  year: 1993
  doi: null
  source_type: academic_paper
- id: oneal_russett_1999
  title: 'The Kantian Peace: The Pacific Benefits of Democracy, Interdependence, and
    International Organizations, 1885-1992'
  authors: Oneal, John R.; Russett, Bruce M.
  year: 1999
  doi: null
  source_type: academic_paper
- id: gartzke_2007
  title: The Capitalist Peace
  authors: Gartzke, Erik
  year: 2007
  doi: null
  source_type: academic_paper
playbooks_detail:
- id: quick_start
  display_name: Quick Start — Democratic Peace
  description: Basic analysis workflow for the democratic_peace domain.
  estimated_runtime: 1–3 minutes
  step_count: 1
  engines_used:
  - logistic_regression
download_url: /packs/democratic-peace.pax.tar.gz
download_size: 2.9 KB
weight: 7974
related_packs: []
---

**Domain:** Democratic Peace

Study of why democracies rarely fight each other and how regime type, trade interdependence, and IGO membership jointly reduce interstate conflict probability.

**Temporal scope:** 1885-present | **Population:** Directed and non-directed dyad-year observations of sovereign state pairs

## Key Findings

- Jointly democratic dyads are significantly less likely to experience MIDs than mixed or autocratic dyads, 1946-1986. *(negative, strong)*
- Dyadic democracy significantly reduces MID onset probability across 1885-1992, robust to controls for capability ratio, contiguity, alliance ties, and other Kantian variables. *(negative, strong)*
- Bilateral trade interdependence independently reduces dyadic MID onset, net of democracy and IGO membership. *(negative, strong)*
- Shared IGO membership count significantly reduces dyadic MID onset, net of democracy and trade. *(negative, moderate)*
- When financial market integration and aligned state preferences are controlled, democratic peace coefficient is substantially attenuated and loses significance in some specifications. *(null, moderate)*

## Sources

- Doyle, Michael W. (1986). *Liberalism and World Politics*.
- Maoz, Zeev; Russett, Bruce M. (1993). *Normative and Structural Causes of Democratic Peace, 1946-1986*.
- Oneal, John R.; Russett, Bruce M. (1999). *The Kantian Peace: The Pacific Benefits of Democracy, Interdependence, and International Organizations, 1885-1992*.
- Gartzke, Erik (2007). *The Capitalist Peace*.

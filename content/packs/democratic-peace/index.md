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
findings:
- maoz_russett_1993_0
- oneal_russett_1999_1
- oneal_russett_1999_2
- oneal_russett_1999_3
- gartzke_2007_4
engines:
- logistic_regression
- ols_regression
- cox_ph
playbooks:
- quick_start
propositions: []
construct_count: 6
finding_count: 5
proposition_count: 0
has_playbooks: true
has_data_sources: true
download_url: /packs/democratic-peace.pax.tar.gz
download_size: 2.9 KB
weight: 7974
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

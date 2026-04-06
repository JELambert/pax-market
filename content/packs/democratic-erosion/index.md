---
name: democratic-erosion
title: Democratic Erosion
version: 1.0.1
pax_type: topic
description: 'Democratic erosion and autocratization: measurement, mechanisms, and
  consequences of democratic backsliding. V-Dem powered analysis of how democracies
  die in the 21st century.'
author: ''
created: '2026-04-06'
license: ''
tags:
- topic
- democratic-erosion
constructs:
- democratic_backsliding_index
- executive_aggrandizement
- judicial_independence_erosion
- media_freedom_decline
- civil_society_repression
- electoral_manipulation
- opposition_suppression
- information_control
- autocratization_episode
engines:
- logistic_regression
- cox_ph
playbook_names:
- quick_start
construct_count: 9
finding_count: 6
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: democratic_erosion
  display_name: Democratic Erosion & Autocratization
  description: The gradual degradation of democratic institutions, norms, and practices
    — executive aggrandizement, judicial capture, media repression, and electoral
    manipulation. Covers the third wave of autocratization and mechanisms of democratic
    death.
  research_questions: []
  temporal_scope: 1900-present
  population: Sovereign states, country-year panel observations
  level_of_analysis: macro
constructs_detail:
- id: democratic_backsliding_index
  display_name: Democratic Backsliding Index
  definition: Sustained decline in V-Dem Liberal Democracy Index (v2x_libdem) over
    a rolling window. A country is coded as backsliding if its LDI drops by >0.05
    over 5 years. The third wave of autocratization (2010-present) has affected 40+
    countries including major democracies.
  aliases: []
  construct_type: outcome
- id: executive_aggrandizement
  display_name: Executive Aggrandizement
  definition: 'The incremental concentration of power in the executive branch through
    legal and semi-legal means: extending term limits, packing courts, weakening legislative
    oversight, ruling by decree. The dominant mode of democratic death in the 21st
    century (Bermeo 2016).'
  aliases: []
  construct_type: process
- id: judicial_independence_erosion
  display_name: Judicial Independence Erosion
  definition: V-Dem indicator measuring decline in judicial independence — court packing,
    removal of judges, reduced jurisdictional scope, intimidation. Operationalized
    as v2juhcind (high court independence). Judicial capture is typically an early
    step in democratic erosion.
  aliases: []
  construct_type: quantifiable
- id: media_freedom_decline
  display_name: Media Freedom Decline
  definition: Reduction in press freedom through legal restrictions, ownership concentration,
    journalist harassment/imprisonment, and internet censorship. Measured by V-Dem
    media freedom indices, RSF Press Freedom Index, or Freedom House scores.
  aliases: []
  construct_type: quantifiable
- id: civil_society_repression
  display_name: Civil Society Repression
  definition: Restrictions on NGOs, protest movements, labor unions, and civic organizations.
    V-Dem CSO participatory environment index (v2xcs_ccsi). Repression of civil society
    removes accountability mechanisms and early warning signals.
  aliases: []
  construct_type: quantifiable
- id: electoral_manipulation
  display_name: Electoral Manipulation
  definition: Subversion of electoral integrity through gerrymandering, voter suppression,
    media manipulation, harassment of opposition, and outright fraud. V-Dem clean
    elections index (v2xel_frefair). Declining electoral quality is a hallmark of
    competitive authoritarianism.
  aliases: []
  construct_type: quantifiable
- id: opposition_suppression
  display_name: Opposition Suppression
  definition: 'Legal and extralegal measures to weaken political opposition: party
    bans, leader imprisonment, defamation lawsuits, and selective prosecution. V-Dem
    opposition parties autonomy index.'
  aliases: []
  construct_type: quantifiable
- id: information_control
  display_name: Information Control
  definition: 'State control over information flows: internet shutdowns, social media
    censorship, disinformation campaigns, and surveillance. Increasingly important
    mechanism of 21st-century autocratization. V-Dem internet censorship + government
    disinformation indicators.'
  aliases: []
  construct_type: quantifiable
- id: autocratization_episode
  display_name: Autocratization Episode
  definition: 'V-Dem binary indicator: country is experiencing a sustained and substantial
    decline in democratic attributes. ~60 countries experienced autocratization episodes
    between 2012-2022. Distinct from democratic backsliding in that it captures the
    process, not just the outcome.'
  aliases: []
  construct_type: outcome
findings_detail:
- finding_text: K-means clustering on V-Dem indices produces optimal k=4-5 clusters
    that match expert typologies, validating data-driven regime classification.
  construct_ids:
  - regime_type
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: K-means clustering
- finding_text: DBSCAN identifies hybrid regimes as noise points between clean democratic
    and autocratic clusters, which is theoretically meaningful as these cases genuinely
    lack clear classification.
  construct_ids:
  - regime_type
  - democracy_score_continuous
  direction: conditional
  effect_size: null
  confidence: moderate
  method_used: DBSCAN
- finding_text: Classic coups d'etat have declined sharply since the Cold War, replaced
    by executive aggrandizement — the incremental dismantling of democratic checks
    by elected leaders. This is now the modal form of democratic breakdown globally,
    making backsliding harder to detect and resist than sudden regime change.
  construct_ids:
  - executive_aggrandizement
  - democratic_backsliding_index
  direction: positive
  effect_size: null
  confidence: strong
  method_used: Comparative historical analysis, global cases 1990-2015
- finding_text: 'Authoritarian regimes that establish nominally democratic institutions
    (legislatures, parties) survive significantly longer than those without. Institutions
    serve as co-optation mechanisms: they provide a forum for distributing spoils
    and absorbing potential opposition, reducing the threat of rebellion and palace
    coups.'
  construct_ids:
  - autocratization_episode
  - opposition_suppression
  direction: negative
  effect_size: null
  confidence: strong
  method_used: Event history analysis, all autocracies 1946-2002
- finding_text: 'Regime type strongly predicts mode of autocratic breakdown: military
    regimes fall to coups, personalist regimes to revolution or insurgency, and single-party
    regimes to negotiated transitions. Different autocratic institutions create different
    vulnerabilities and exit pathways.'
  construct_ids:
  - autocratization_episode
  - executive_aggrandizement
  direction: conditional
  effect_size: null
  confidence: strong
  method_used: Original dataset of 280 autocratic regimes 1946-2010, event history
    analysis
- finding_text: 'The third wave of autocratization is qualitatively different from
    previous waves: it affects democracies more than autocracies, proceeds through
    legal channels rather than sudden rupture, and is harder to identify in real-time.
    V-Dem data shows 24 countries autocratizing as of 2019, home to 2.8 billion people.'
  construct_ids:
  - autocratization_episode
  - democratic_backsliding_index
  direction: positive
  effect_size: null
  confidence: strong
  method_used: V-Dem episode data, 174 countries, 1900-2018
propositions_detail: []
sources_detail:
- id: geddes_wright_frantz_2014
  title: 'Autocratic Breakdown and Regime Transitions: A New Data Set'
  authors: Geddes, B., Wright, J., Frantz, E.
  year: 2014
  doi: null
  source_type: journal_article
- id: bermeo_2016
  title: On Democratic Backsliding
  authors: Nancy Bermeo
  year: 2016
  doi: 10.1353/jod.2016.0012
  source_type: journal_article
- id: luhrmann_lindberg_2019
  title: 'A third wave of autocratization is here: what is new about it?'
  authors: Anna Luhrmann, Staffan I. Lindberg
  year: 2019
  doi: 10.1080/13510347.2019.1582029
  source_type: journal_article
- id: gandhi_przeworski_2007
  title: Authoritarian Institutions and the Survival of Autocrats
  authors: Jennifer Gandhi, Adam Przeworski
  year: 2007
  doi: 10.1177/0010414007305817
  source_type: journal_article
- id: vdem_v14_2024
  title: V-Dem Dataset v14
  authors: V-Dem Institute, University of Gothenburg
  year: 2024
  doi: null
  source_type: dataset
playbooks_detail: []
download_url: https://pax-market.com/packs/democratic-erosion.pax.tar.gz
download_size: 4.2 KB
published_by: Praxis Agent
related_packs: []
pax_name: democratic-erosion
weight: 7974
---

**Domain:** Democratic Erosion & Autocratization

The gradual degradation of democratic institutions, norms, and practices — executive aggrandizement, judicial capture, media repression, and electoral manipulation. Covers the third wave of autocratization and mechanisms of democratic death.

**Temporal scope:** 1900-present | **Population:** Sovereign states, country-year panel observations

## Key Findings

- K-means clustering on V-Dem indices produces optimal k=4-5 clusters that match expert typologies, validating data-driven regime classification. *(positive, moderate)*
- DBSCAN identifies hybrid regimes as noise points between clean democratic and autocratic clusters, which is theoretically meaningful as these cases genuinely lack clear classification. *(conditional, moderate)*
- Classic coups d'etat have declined sharply since the Cold War, replaced by executive aggrandizement — the incremental dismantling of democratic checks by elected leaders. This is now the modal form of democratic breakdown globally, making backsliding harder to detect and resist than sudden regime change. *(positive, strong)*
- Authoritarian regimes that establish nominally democratic institutions (legislatures, parties) survive significantly longer than those without. Institutions serve as co-optation mechanisms: they provide a forum for distributing spoils and absorbing potential opposition, reducing the threat of rebellion and palace coups. *(negative, strong)*
- Regime type strongly predicts mode of autocratic breakdown: military regimes fall to coups, personalist regimes to revolution or insurgency, and single-party regimes to negotiated transitions. Different autocratic institutions create different vulnerabilities and exit pathways. *(conditional, strong)*
- The third wave of autocratization is qualitatively different from previous waves: it affects democracies more than autocracies, proceeds through legal channels rather than sudden rupture, and is harder to identify in real-time. V-Dem data shows 24 countries autocratizing as of 2019, home to 2.8 billion people. *(positive, strong)*

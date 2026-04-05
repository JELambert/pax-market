---
title: Dukalskis (2024)
pax_name: dukalskis-et-al-2024-transnational-repression
version: 1.0.0
pax_type: paper
description: First large-N quantitative study of domestic drivers of transnational
  repression (TR). Tests the hypothesis that authoritarian crackdowns at home increase
  the subsequent likelihood of the same state repressing its citizens abroad. Uses
  the Authoritarian Actions Abroad Database (AAAD, ~1,205 events, 1991-2019) across
  88 authoritarian regimes in a country-year panel.
author: Dukalskis, Furstenberg, Hellmeier, Scales
created: '2026-04-02'
license: ''
tags:
- paper
- transnational-repression
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
finding_count: 7
proposition_count: 2
has_playbooks: true
has_data_sources: true
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
  aliases:
  - TR binary
  - transnational repression occurrence
  - extraterritorial repression
  construct_type: outcome
- id: transnational_repression_count
  display_name: Transnational Repression (Count)
  definition: 'Count of transnational repression events carried out by an authoritarian
    state against its own citizens abroad in a given country-year. Ranges from 0 to
    61 (Uzbekistan 2005). Source: AAAD (Dukalskis 2021).'
  aliases:
  - TR count
  - number of TR events
  construct_type: outcome
- id: domestic_repression_cli
  display_name: Domestic Repression (V-Dem CLI)
  definition: 'Inverted V-Dem Civil Liberties Index (CLI), measuring the intensity
    of domestic state repression. The CLI aggregates three component indices: physical
    violence index (torture, killings), political civil liberties index (censorship,
    parties, civil society), and private civil liberties index (forced labor, property
    rights, religion). Higher values indicate more repression. Lagged one year in
    analysis. Source: V-Dem v12, Coppedge et al. 2022.'
  aliases:
  - domestic repression
  - inverted CLI
  - V-Dem civil liberties index (inverted)
  - state repression intensity
  construct_type: quantifiable
- id: diplomatic_capacity_abroad
  display_name: Diplomatic Representation Abroad
  definition: 'Number of diplomatic representations (embassies, consulates, and other
    missions) a state maintains abroad in a given year. Captures the logistical infrastructure
    enabling a state to project repression transnationally. Source: Diplometrics Diplomatic
    Representation dataset (Moyer et al. 2021), 1960-2020. Mean in sample: 50.8, range:
    1-170.'
  aliases:
  - diplomatic representation
  - diplomatic capacity
  - embassies abroad
  construct_type: quantifiable
- id: state_capacity_latent
  display_name: State Capacity Index
  definition: 'Latent measure of state capacity aggregating 21 variables across three
    conceptual pillars: extractive capacity, coercive capacity, and administrative
    capacity. Estimated via item response theory model. Source: Hanson and Sigman
    (2021), State Capacity Dataset v1. Mean in sample: -0.059, range: -1.541 to 1.28.'
  aliases:
  - state capacity
  - government capacity
  - Hanson-Sigman capacity
  construct_type: quantifiable
- id: polity_score
  display_name: Polity Score
  definition: 'Revised combined Polity score measuring level of authoritarianism/democracy
    on a scale from -10 (full autocracy) to +10 (full democracy). Used as control
    for regime type. Source: Marshall and Gurr (2020). Mean in sample: -4.46.'
  aliases:
  - Polity
  - Polity IV
  - regime type score
  construct_type: quantifiable
- id: leader_tenure
  display_name: Leader Tenure (Log)
  definition: 'Log of the incumbent ruler''s cumulative time in office (years). Controls
    for the possibility that crackdowns occur around regime consolidation periods
    and that repression spikes during transitions. Source: Bell, Besaw, and Frank
    (2021). Mean: 4.60 log-years.'
  aliases:
  - leader time in office
  - incumbent tenure
  construct_type: quantifiable
findings_detail:
- finding_text: 'Domestic repression (inverted V-Dem CLI) is positively and significantly
    associated with subsequent transnational repression in the bivariate model: β=1.09,
    SE=0.20, p<0.001 (logistic regression, country and year FE, N=857 country-years).
    This is the first large-N quantitative confirmation that domestic crackdowns predict
    TR.'
  construct_ids:
  - transnational_repression_binary
  - domestic_repression_cli
  direction: positive
  effect_size: β=1.09 (SE=0.20), p<0.001 — bivariate logistic with country/year FE
  confidence: strong
  method_used: logistic regression with country and year fixed effects, bias-reducing
    score adjustments (bife), N=857
  finding_type: empirical
  evidence_type: quantitative
- finding_text: 'Domestic repression remains positively and significantly associated
    with transnational repression after adding controls for polity score, elections,
    leader tenure, military and party dimension, population, GDP per capita, and state
    capacity: β=0.83, SE=0.26, p<0.01 (Model 2, logistic regression with country/year
    FE, N=731).'
  construct_ids:
  - transnational_repression_binary
  - domestic_repression_cli
  direction: positive
  effect_size: β=0.83 (SE=0.26), p<0.01 — full controls model
  confidence: strong
  method_used: logistic regression with country and year fixed effects, bias-reducing
    score adjustments (bife), N=731
  finding_type: empirical
  evidence_type: quantitative
- finding_text: The interaction between domestic repression and diplomatic representation
    abroad is positive and statistically significant (β=0.15, SE=0.05, p<0.01, Model
    4). States with high diplomatic capacity are substantially more likely to translate
    domestic crackdowns into transnational repression than states with few diplomatic
    ties. The predicted probability of TR increases drastically for states with high
    diplomatic representation when domestic repression increases, but not for states
    with few representations.
  construct_ids:
  - transnational_repression_binary
  - domestic_repression_cli
  - diplomatic_capacity_abroad
  direction: positive
  effect_size: β=0.15 (SE=0.05), p<0.01 — interaction term
  confidence: strong
  method_used: logistic regression with country/year FE, interaction term, N=723
  finding_type: empirical
  evidence_type: quantitative
- finding_text: The interaction between domestic repression and state capacity is
    not statistically significant (β=0.01, SE=0.03, Model 3, N=731). General state
    capacity does not significantly moderate the domestic-to-transnational repression
    pathway, in contrast to diplomatic capacity which does.
  construct_ids:
  - transnational_repression_binary
  - domestic_repression_cli
  - state_capacity_latent
  direction: 'null'
  effect_size: β=0.01 (SE=0.03), n.s.
  confidence: moderate
  method_used: logistic regression with country/year FE, interaction term, N=731
  finding_type: empirical
  evidence_type: quantitative
- finding_text: State capacity index is positively and significantly associated with
    transnational repression in the main model (β=0.20, SE=0.05, p<0.001, Model 2).
    More capable states are more likely to engage in TR, though the interaction with
    domestic repression does not reach significance.
  construct_ids:
  - transnational_repression_binary
  - state_capacity_latent
  direction: positive
  effect_size: β=0.20 (SE=0.05), p<0.001
  confidence: strong
  method_used: logistic regression with country/year FE, N=731
  finding_type: empirical
  evidence_type: quantitative
- finding_text: Leader tenure (log) is negatively associated with transnational repression
    (β=-0.37, SE=0.18, p<0.05, Model 2), suggesting that more consolidated, longer-tenured
    regimes are somewhat less likely to engage in TR, possibly because they face fewer
    acute threats.
  construct_ids:
  - transnational_repression_binary
  - leader_tenure
  direction: negative
  effect_size: β=-0.37 (SE=0.18), p<0.05
  confidence: moderate
  method_used: logistic regression with country/year FE, N=731
  finding_type: empirical
  evidence_type: quantitative
- finding_text: 'Robustness checks confirm the main finding across alternative specifications:
    conditional logistic regression (bife package), Poisson, negative binomial, and
    OLS models all yield statistically significant positive relationships between
    domestic and transnational repression. Results also hold when disaggregating TR
    events by target type (activists, journalists, citizens) and action type (threats,
    arrests, extraditions, assassination attempts).'
  construct_ids:
  - transnational_repression_binary
  - domestic_repression_cli
  direction: positive
  effect_size: ''
  confidence: strong
  method_used: conditional logistic (bife), Poisson, negative binomial, OLS
  finding_type: empirical
  evidence_type: quantitative
propositions_detail:
- id: domestic_crackdown_causes_tr
  proposition_text: An increase in domestic repression by an authoritarian state is
    likely to lead to a subsequent increase in transnational repression, because crackdowns
    at home (1) drive dissidents abroad who then become targets, and (2) activate
    state surveillance of international links that can be seen as threats to regime
    stability.
  construct_from: domestic_repression_cli
  construct_to: transnational_repression_binary
  direction: positive
  scope_conditions: Authoritarian regimes only; lagged effect (t-1 → t); effect amplified
    by diplomatic capacity
- id: diplomatic_capacity_amplifies_tr
  proposition_text: 'Diplomatic capacity abroad (number of embassies and consulates)
    moderates the domestic-to-transnational repression pathway: states with greater
    diplomatic infrastructure are significantly more likely to translate domestic
    crackdowns into transnational repression, as diplomatic presence provides the
    logistical means to execute TR in host countries.'
  construct_from: diplomatic_capacity_abroad
  construct_to: transnational_repression_binary
  direction: positive
  scope_conditions: Moderation effect; conditional on domestic repression intensity
sources_detail:
- id: dukalskis_et_al_2024
  title: 'The Long Arm and the Iron Fist: Authoritarian Crackdowns and Transnational
    Repression'
  authors: Dukalskis, Alexander; Furstenberg, Saipira; Hellmeier, Sebastian; Scales,
    Redmond
  year: 2024
  doi: 10.1177/00220027231188896
  source_type: academic_paper
- id: dukalskis_2021_aaad
  title: Authoritarian Actions Abroad Database (AAAD)
  authors: Dukalskis, Alexander
  year: 2021
  doi: 10.7910/DVN/WIXVLJ
  source_type: dataset
playbooks_detail:
- id: quick_start
  display_name: Quick Start — Transnational Repression
  description: Basic analysis workflow for the transnational_repression domain.
  estimated_runtime: 1–3 minutes
  step_count: 1
  engines_used:
  - logistic_regression
download_url: /packs/dukalskis-et-al-2024-transnational-repression.pax.tar.gz
download_size: 5.0 KB
weight: 7974
related_packs: []
---

**Domain:** Transnational Repression

The extraterritorial use of coercive tactics by authoritarian states to silence, monitor, threaten, abduct, extradite, or assassinate dissidents and regime opponents beyond their national borders. Encompasses threats, arrests, extraditions, abductions, family harassment, and assassination. TR is distinct from domestic repression and from targeting foreign citizens.

**Temporal scope:** 1991-2019 | **Population:** Authoritarian states with diaspora populations, country-year panel, 1991-2019

## Key Findings

- Domestic repression (inverted V-Dem CLI) is positively and significantly associated with subsequent transnational repression in the bivariate model: β=1.09, SE=0.20, p<0.001 (logistic regression, country and year FE, N=857 country-years). This is the first large-N quantitative confirmation that domestic crackdowns predict TR. *(positive, strong)*
- Domestic repression remains positively and significantly associated with transnational repression after adding controls for polity score, elections, leader tenure, military and party dimension, population, GDP per capita, and state capacity: β=0.83, SE=0.26, p<0.01 (Model 2, logistic regression with country/year FE, N=731). *(positive, strong)*
- The interaction between domestic repression and diplomatic representation abroad is positive and statistically significant (β=0.15, SE=0.05, p<0.01, Model 4). States with high diplomatic capacity are substantially more likely to translate domestic crackdowns into transnational repression than states with few diplomatic ties. The predicted probability of TR increases drastically for states with high diplomatic representation when domestic repression increases, but not for states with few representations. *(positive, strong)*
- The interaction between domestic repression and state capacity is not statistically significant (β=0.01, SE=0.03, Model 3, N=731). General state capacity does not significantly moderate the domestic-to-transnational repression pathway, in contrast to diplomatic capacity which does. *(null, moderate)*
- State capacity index is positively and significantly associated with transnational repression in the main model (β=0.20, SE=0.05, p<0.001, Model 2). More capable states are more likely to engage in TR, though the interaction with domestic repression does not reach significance. *(positive, strong)*
- Leader tenure (log) is negatively associated with transnational repression (β=-0.37, SE=0.18, p<0.05, Model 2), suggesting that more consolidated, longer-tenured regimes are somewhat less likely to engage in TR, possibly because they face fewer acute threats. *(negative, moderate)*
- Robustness checks confirm the main finding across alternative specifications: conditional logistic regression (bife package), Poisson, negative binomial, and OLS models all yield statistically significant positive relationships between domestic and transnational repression. Results also hold when disaggregating TR events by target type (activists, journalists, citizens) and action type (threats, arrests, extraditions, assassination attempts). *(positive, strong)*

## Theoretical Propositions

- [+] An increase in domestic repression by an authoritarian state is likely to lead to a subsequent increase in transnational repression, because crackdowns at home (1) drive dissidents abroad who then become targets, and (2) activate state surveillance of international links that can be seen as threats to regime stability.
- [+] Diplomatic capacity abroad (number of embassies and consulates) moderates the domestic-to-transnational repression pathway: states with greater diplomatic infrastructure are significantly more likely to translate domestic crackdowns into transnational repression, as diplomatic presence provides the logistical means to execute TR in host countries.

## Sources

- Dukalskis, Alexander; Furstenberg, Saipira; Hellmeier, Sebastian; Scales, Redmond (2024). *The Long Arm and the Iron Fist: Authoritarian Crackdowns and Transnational Repression*. DOI: 10.1177/00220027231188896
- Dukalskis, Alexander (2021). *Authoritarian Actions Abroad Database (AAAD)*. DOI: 10.7910/DVN/WIXVLJ

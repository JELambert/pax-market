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
findings:
- dukalskis_et_al_2024_0
- dukalskis_et_al_2024_1
- dukalskis_et_al_2024_2
- dukalskis_et_al_2024_3
- dukalskis_et_al_2024_4
- dukalskis_et_al_2024_5
- dukalskis_et_al_2024_6
engines:
- logistic_regression
- ols_regression
playbooks:
- quick_start
propositions:
- domestic_crackdown_causes_tr
- diplomatic_capacity_amplifies_tr
construct_count: 7
finding_count: 7
proposition_count: 2
has_playbooks: true
has_data_sources: true
download_url: /packs/dukalskis-et-al-2024-transnational-repression.pax.tar.gz
download_size: 5.0 KB
weight: 7974
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

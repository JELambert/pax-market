---
title: Institutional quality and economic development
pax_name: institutional-quality-development
version: 1.0.0
pax_type: topic
description: Institutional quality and economic development — how property rights,
  rule of law, corruption control, and democratic governance shape long-run per capita
  income. Built on Acemoglu, Johnson & Robinson (2001), North (1990), Rodrik et al.
  (2004), Kaufmann et al. (2010), and Mauro (1995).
author: Acemoglu, Daron; North, Douglass C.; Rodrik, Dani; Kaufmann, Daniel; Mauro,
  Paolo
created: '2026-04-04'
license: ''
tags:
- topic
- institutional-quality-development
constructs:
- rule_of_law
- control_of_corruption
- property_rights_security
- government_effectiveness
- democratic_governance
findings:
- acemoglu_johnson_robinson_2001_0
- rodrik_subramanian_trebbi_2004_1
- mauro_1995_2
- knack_keefer_1995_3
- kaufmann_kraay_mastruzzi_2010_4
engines:
- ols_regression
- instrumental_variables
- difference_in_differences
- lasso_regression
playbooks:
- quick_start
propositions: []
construct_count: 5
finding_count: 5
proposition_count: 0
has_playbooks: true
has_data_sources: true
download_url: /packs/institutional-quality-development.pax.tar.gz
download_size: 3.1 KB
weight: 7974
---

**Domain:** Institutional Quality and Economic Development

How formal and informal institutions — property rights, rule of law, corruption control, governance — shape long-run economic development outcomes across countries.

**Temporal scope:** 1960-present | **Population:** Sovereign states (country-year)

## Key Findings

- IV/2SLS using settler mortality shows institutions have a large causal effect on income per capita. 1 SD improvement in expropriation risk ~ 1+ log point increase in income. *(positive, strong)*
- Once institutions are instrumented, geography has no direct effect and trade is insignificant. Institutions dominate. *(positive, strong)*
- 1 SD improvement in corruption index associated with +4 pp investment rate and +0.5 pp annual growth. *(negative, strong)*
- ICRG-based property rights measures have substantially larger positive association with investment and growth than political freedom indices. *(positive, strong)*
- Strong correlation (r~0.80) between rule of law and GDP per capita across 200+ countries, though causal inference requires instrumentation. *(positive, moderate)*

## Sources

- Acemoglu, Daron; Johnson, Simon; Robinson, James A. (2001). *The Colonial Origins of Comparative Development: An Empirical Investigation*.
- Rodrik, Dani; Subramanian, Arvind; Trebbi, Francesco (2004). *Institutions Rule: The Primacy of Institutions Over Geography and Integration in Economic Development*.
- Mauro, Paolo (1995). *Corruption and Growth*.
- Kaufmann, Daniel; Kraay, Aart; Mastruzzi, Massimo (2010). *The Worldwide Governance Indicators: Methodology and Analytical Issues*.
- Knack, Stephen; Keefer, Philip (1995). *Institutions and Economic Performance: Cross-Country Tests Using Alternative Institutional Measures*.

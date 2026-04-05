---
title: Algorithmic Fairness
pax_name: algorithmic-fairness
version: 1.0.0
pax_type: topic
description: Measurement and mitigation of bias in ML prediction systems. Covers impossibility
  theorems (Chouldechova, Kleinberg), facial recognition bias (Buolamwini & Gebru),
  and accuracy-fairness tradeoffs in criminal justice risk assessment.
author: ''
created: '2026-04-05'
license: ''
tags:
- topic
- algorithmic-fairness
constructs:
- prediction_accuracy
- false_positive_rate
- demographic_parity
- calibration
findings:
- chouldechova_2017_0
- buolamwini_gebru_2018_1
engines:
- logistic_regression
- random_forest
- gradient_boosting
playbooks:
- quick_start
propositions: []
construct_count: 4
finding_count: 2
proposition_count: 0
has_playbooks: true
has_data_sources: true
download_url: /packs/algorithmic-fairness.pax.tar.gz
download_size: 1.9 KB
weight: 7974
---

**Domain:** Algorithmic Fairness & Bias

Bias in ML systems, fairness constraints, and societal impacts

## Key Findings

- Mathematically impossible to simultaneously satisfy calibration AND equal FPR/FNR across groups when base rates differ *(negative, foundational)*
- Commercial facial recognition error rates up to 34.7% for dark-skinned women vs 0.8% for light-skinned men *(negative, strong)*

## Sources

- Alexandra Chouldechova (2017). *Fair Prediction with Disparate Impact*.
- Joy Buolamwini, Timnit Gebru (2018). *Gender Shades*.

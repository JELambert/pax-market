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
engines:
- logistic_regression
- random_forest
- gradient_boosting
playbook_names:
- quick_start
construct_count: 4
finding_count: 2
proposition_count: 0
has_playbooks: true
has_data_sources: true
domain:
  id: algorithmic_fairness
  display_name: Algorithmic Fairness & Bias
  description: Bias in ML systems, fairness constraints, and societal impacts
  research_questions: []
  temporal_scope: ''
  population: ''
  level_of_analysis: micro
constructs_detail:
- id: prediction_accuracy
  display_name: Prediction Accuracy
  definition: Correctness of ML model predictions
  aliases: []
  construct_type: quantifiable
- id: false_positive_rate
  display_name: False Positive Rate
  definition: Rate of incorrect positive predictions per group
  aliases: []
  construct_type: quantifiable
- id: demographic_parity
  display_name: Demographic Parity
  definition: Equal positive prediction rates across groups
  aliases: []
  construct_type: quantifiable
- id: calibration
  display_name: Calibration
  definition: Predicted probabilities match observed frequencies
  aliases: []
  construct_type: quantifiable
findings_detail:
- finding_text: Mathematically impossible to simultaneously satisfy calibration AND
    equal FPR/FNR across groups when base rates differ
  construct_ids:
  - calibration
  - false_positive_rate
  direction: negative
  effect_size: ''
  confidence: foundational
  method_used: ''
  finding_type: ''
  evidence_type: ''
- finding_text: Commercial facial recognition error rates up to 34.7% for dark-skinned
    women vs 0.8% for light-skinned men
  construct_ids:
  - prediction_accuracy
  - demographic_parity
  direction: negative
  effect_size: ''
  confidence: strong
  method_used: ''
  finding_type: ''
  evidence_type: ''
propositions_detail: []
sources_detail:
- id: chouldechova_2017
  title: Fair Prediction with Disparate Impact
  authors: Alexandra Chouldechova
  year: 2017
  doi: null
  source_type: journal_article
- id: buolamwini_gebru_2018
  title: Gender Shades
  authors: Joy Buolamwini, Timnit Gebru
  year: 2018
  doi: null
  source_type: journal_article
playbooks_detail:
- id: quick_start
  display_name: Quick Start — Algorithmic Fairness
  description: Basic analysis workflow for the algorithmic_fairness domain.
  estimated_runtime: 1–3 minutes
  step_count: 1
  engines_used: []
download_url: /packs/algorithmic-fairness.pax.tar.gz
download_size: 1.9 KB
weight: 7974
related_packs: []
---

**Domain:** Algorithmic Fairness & Bias

Bias in ML systems, fairness constraints, and societal impacts

## Key Findings

- Mathematically impossible to simultaneously satisfy calibration AND equal FPR/FNR across groups when base rates differ *(negative, foundational)*
- Commercial facial recognition error rates up to 34.7% for dark-skinned women vs 0.8% for light-skinned men *(negative, strong)*

## Sources

- Alexandra Chouldechova (2017). *Fair Prediction with Disparate Impact*.
- Joy Buolamwini, Timnit Gebru (2018). *Gender Shades*.

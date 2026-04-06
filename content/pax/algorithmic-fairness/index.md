---
name: algorithmic-fairness
title: Algorithmic Fairness
version: 1.0.0
pax_type: topic
description: Measurement and mitigation of bias in ML prediction systems. Covers impossibility
  theorems (Chouldechova, Kleinberg), facial recognition bias (Buolamwini & Gebru),
  and accuracy-fairness tradeoffs in criminal justice risk assessment.
author: ''
created: ''
license: ''
tags:
- topic
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
finding_count: 0
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: algorithmic_fairness
  display_name: Algorithmic Fairness & Bias
  description: Measurement and mitigation of bias in machine learning systems, fairness
    constraints, and societal impacts of algorithmic decision-making
  research_questions: []
  temporal_scope: null
  population: null
  level_of_analysis: micro
constructs_detail:
- id: prediction_accuracy
  display_name: Prediction Accuracy
  definition: Correctness of model predictions, measuring how well a classifier or
    regression model maps inputs to true outcomes across the full population or subgroups.
  aliases: []
  construct_type: quantifiable
- id: false_positive_rate
  display_name: False Positive Rate
  definition: Rate of incorrect positive predictions, measuring how often a classifier
    incorrectly labels negative instances as positive, potentially causing harm through
    false accusations or unnecessary interventions.
  aliases: []
  construct_type: quantifiable
- id: demographic_parity
  display_name: Demographic Parity
  definition: Fairness criterion requiring equal positive prediction rates across
    demographic groups, ensuring that the proportion of individuals receiving a positive
    classification is independent of group membership.
  aliases: []
  construct_type: concept
- id: calibration
  display_name: Calibration
  definition: Property that predicted probabilities match observed frequencies of
    the outcome, meaning that among all individuals assigned a predicted risk of X%,
    approximately X% actually experience the outcome.
  aliases: []
  construct_type: quantifiable
findings_detail: []
propositions_detail: []
sources_detail: []
playbooks_detail: []
download_url: https://pax-market.com/pax/algorithmic-fairness.pax.tar.gz
download_size: 1.5 KB
published_by: Praxis Agent
related_packs: []
pax_name: algorithmic-fairness
weight: 10000
---

**Domain:** Algorithmic Fairness & Bias

Measurement and mitigation of bias in machine learning systems, fairness constraints, and societal impacts of algorithmic decision-making

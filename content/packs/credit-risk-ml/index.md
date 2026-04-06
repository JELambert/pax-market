---
name: credit-risk-ml
title: Credit Risk ML
version: 1.0.0
pax_type: topic
description: Machine learning approaches to credit default prediction. Covers logistic
  regression, random forest, and gradient boosting benchmarks across UCI/Kaggle credit
  datasets.
author: ''
created: ''
license: ''
tags:
- topic
constructs:
- credit_default_binary
- credit_amount
- applicant_age
engines:
- logistic_regression
- random_forest
- gradient_boosting
- lasso_regression
playbook_names:
- quick_start
construct_count: 3
finding_count: 0
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: credit_default_prediction
  display_name: Credit Default Prediction
  description: Prediction of loan default using applicant characteristics, credit
    history, and financial indicators
  research_questions: []
  temporal_scope: null
  population: Loan applicants
  level_of_analysis: micro
constructs_detail:
- id: credit_default_binary
  display_name: Credit Default
  definition: Binary indicator of whether a loan applicant defaulted on their credit
    obligation
  aliases: []
  construct_type: outcome
- id: credit_amount
  display_name: Credit Amount
  definition: Total loan amount in Deutsche Marks or equivalent
  aliases: []
  construct_type: quantifiable
- id: applicant_age
  display_name: Applicant Age
  definition: Age of the loan applicant in years
  aliases: []
  construct_type: quantifiable
findings_detail: []
propositions_detail: []
sources_detail: []
playbooks_detail: []
download_url: https://pax-market.com/packs/credit-risk-ml.pax.tar.gz
download_size: 1.1 KB
published_by: Praxis Agent
related_packs: []
pax_name: credit-risk-ml
weight: 10000
---

**Domain:** Credit Default Prediction

Prediction of loan default using applicant characteristics, credit history, and financial indicators

**Population:** Loan applicants

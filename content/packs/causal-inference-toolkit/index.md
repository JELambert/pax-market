---
name: causal-inference-toolkit
title: Causal Inference Toolkit
version: 1.0.0
pax_type: field
description: Cross-domain causal inference methods PAX. Bundles DID, PSM, and IV engines
  with documented use cases from minimum wage, microfinance, and institutional quality
  domains.
author: ''
created: ''
license: ''
tags:
- field
constructs:
- treatment_effect_ate
engines:
- difference_in_differences
- propensity_score_matching
- instrumental_variables
- ols_regression
- logistic_regression
playbook_names:
- quick_start
construct_count: 1
finding_count: 0
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: causal_inference_methods
  display_name: Causal Inference Methods
  description: Statistical methods for identifying causal effects from observational
    data
  research_questions: []
  temporal_scope: null
  population: null
  level_of_analysis: cross-level
constructs_detail:
- id: treatment_effect_ate
  display_name: Average Treatment Effect
  definition: Average causal effect of treatment on outcome across all units
  aliases: []
  construct_type: quantifiable
findings_detail: []
propositions_detail: []
sources_detail: []
playbooks_detail: []
download_url: https://pax-market.com/packs/causal-inference-toolkit.pax.tar.gz
download_size: 1.0 KB
published_by: Praxis Agent
related_packs: []
pax_name: causal-inference-toolkit
weight: 10000
---

**Domain:** Causal Inference Methods

Statistical methods for identifying causal effects from observational data

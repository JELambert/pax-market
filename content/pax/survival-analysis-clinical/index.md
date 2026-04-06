---
name: survival-analysis-clinical
title: Survival Analysis Clinical
version: 1.0.0
pax_type: field
description: Clinical survival analysis PAX covering lung cancer, HIV, transplant,
  ICU, and cardiovascular domains. Bundles KM and Cox PH engines with survival-specific
  constructs.
author: ''
created: ''
license: ''
tags:
- field
constructs:
- time_to_event_generic
- event_indicator_generic
engines:
- kaplan_meier
- cox_ph
- logistic_regression
playbook_names:
- quick_start
construct_count: 2
finding_count: 0
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: clinical_survival_analysis
  display_name: Clinical Survival Analysis
  description: Time-to-event analysis in clinical settings
  research_questions: []
  temporal_scope: null
  population: null
  level_of_analysis: micro
constructs_detail:
- id: time_to_event_generic
  display_name: Time to Event
  definition: Duration from index event to outcome or censoring
  aliases: []
  construct_type: quantifiable
- id: event_indicator_generic
  display_name: Event Indicator
  definition: 'Binary indicator: 1 if event occurred, 0 if censored'
  aliases: []
  construct_type: outcome
findings_detail: []
propositions_detail: []
sources_detail: []
playbooks_detail: []
download_url: https://pax-market.com/pax/survival-analysis-clinical.pax.tar.gz
download_size: 1.0 KB
published_by: Praxis Agent
related_packs: []
pax_name: survival-analysis-clinical
weight: 10000
---

**Domain:** Clinical Survival Analysis

Time-to-event analysis in clinical settings

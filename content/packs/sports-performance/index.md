---
title: Sports Performance
pax_name: sports-performance
version: 1.0.0
pax_type: topic
description: Statistical analysis of team performance, Elo ratings, and win probability
  in professional sports. Tests domain-agnosticism with a deliberately non-academic
  domain.
author: ''
created: '2026-04-05'
license: ''
tags:
- topic
- sports-analytics
constructs:
- elo_rating
- win_probability
- offensive_efficiency
- defensive_efficiency
engines:
- ols_regression
- logistic_regression
- random_forest
playbook_names:
- quick_start
construct_count: 4
finding_count: 1
proposition_count: 0
has_playbooks: true
has_data_sources: true
domain:
  id: sports_analytics
  display_name: Sports Analytics
  description: Statistical analysis of athletic performance, team strategy, and game
    outcomes
  research_questions: []
  temporal_scope: ''
  population: ''
  level_of_analysis: micro
constructs_detail:
- id: elo_rating
  display_name: Elo Rating
  definition: Skill rating based on results against rated opponents
  aliases: []
  construct_type: quantifiable
- id: win_probability
  display_name: Win Probability
  definition: Estimated probability of winning a game
  aliases: []
  construct_type: outcome
- id: offensive_efficiency
  display_name: Offensive Efficiency
  definition: Points or runs scored per possession or opportunity
  aliases: []
  construct_type: quantifiable
- id: defensive_efficiency
  display_name: Defensive Efficiency
  definition: Points or runs allowed per possession or opportunity
  aliases: []
  construct_type: quantifiable
findings_detail:
- finding_text: Elo ratings with K-factor tuning produce well-calibrated win probabilities,
    mean absolute error 4-6 percentage points
  construct_ids:
  - elo_rating
  - win_probability
  direction: positive
  effect_size: ''
  confidence: strong
  method_used: ''
  finding_type: ''
  evidence_type: ''
propositions_detail: []
sources_detail:
- id: silver_538_elo
  title: FiveThirtyEight NBA Elo Ratings
  authors: Nate Silver, FiveThirtyEight
  year: 2015
  doi: null
  source_type: dataset
playbooks_detail:
- id: quick_start
  display_name: Quick Start — Sports Analytics
  description: Basic analysis workflow for the sports_analytics domain.
  estimated_runtime: 1–3 minutes
  step_count: 1
  engines_used:
  - logistic_regression
download_url: /packs/sports-performance.pax.tar.gz
download_size: 1.7 KB
weight: 7974
related_packs: []
---

**Domain:** Sports Analytics

Statistical analysis of athletic performance, team strategy, and game outcomes

## Key Findings

- Elo ratings with K-factor tuning produce well-calibrated win probabilities, mean absolute error 4-6 percentage points *(positive, strong)*

## Sources

- Nate Silver, FiveThirtyEight (2015). *FiveThirtyEight NBA Elo Ratings*.

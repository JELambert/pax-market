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
findings:
- silver_538_elo_0
engines:
- ols_regression
- logistic_regression
- random_forest
playbooks:
- quick_start
propositions: []
construct_count: 4
finding_count: 1
proposition_count: 0
has_playbooks: true
has_data_sources: true
download_url: /packs/sports-performance.pax.tar.gz
download_size: 1.7 KB
weight: 7974
---

**Domain:** Sports Analytics

Statistical analysis of athletic performance, team strategy, and game outcomes

## Key Findings

- Elo ratings with K-factor tuning produce well-calibrated win probabilities, mean absolute error 4-6 percentage points *(positive, strong)*

## Sources

- Nate Silver, FiveThirtyEight (2015). *FiveThirtyEight NBA Elo Ratings*.

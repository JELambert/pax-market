---
name: sports-performance
title: Sports Performance
version: 1.0.0
pax_type: topic
description: Statistical analysis of team performance, Elo ratings, and win probability
  in professional sports. Tests domain-agnosticism with a deliberately non-academic
  domain.
author: ''
created: ''
license: ''
tags:
- topic
constructs:
- win_probability
- elo_rating
- offensive_efficiency
- defensive_efficiency
engines:
- ols_regression
- logistic_regression
- random_forest
playbook_names:
- quick_start
construct_count: 4
finding_count: 0
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: sports_analytics
  display_name: Sports Analytics
  description: Statistical analysis of athletic performance, team strategy, game outcomes,
    and player valuation
  research_questions: []
  temporal_scope: null
  population: null
  level_of_analysis: micro
constructs_detail:
- id: win_probability
  display_name: Win Probability
  definition: Estimated probability of winning a game given current state, capturing
    pre-game expectations and in-game dynamics
  aliases: []
  construct_type: quantifiable
- id: elo_rating
  display_name: Elo Rating
  definition: Skill rating of a team based on results against rated opponents, updated
    after each game using a transfer function
  aliases: []
  construct_type: quantifiable
- id: offensive_efficiency
  display_name: Offensive Efficiency
  definition: Points or runs scored per possession or opportunity, measuring a team's
    ability to convert opportunities into scoring
  aliases: []
  construct_type: quantifiable
- id: defensive_efficiency
  display_name: Defensive Efficiency
  definition: Points or runs allowed per possession or opportunity, measuring a team's
    ability to prevent opponent scoring
  aliases: []
  construct_type: quantifiable
findings_detail: []
propositions_detail: []
sources_detail: []
playbooks_detail: []
download_url: https://pax-market.com/packs/sports-performance.pax.tar.gz
download_size: 1.2 KB
published_by: Praxis Agent
related_packs: []
pax_name: sports-performance
weight: 10000
---

**Domain:** Sports Analytics

Statistical analysis of athletic performance, team strategy, game outcomes, and player valuation

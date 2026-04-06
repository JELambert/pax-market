---
name: collective-intelligence-group-cognition
title: When and why groups outthink individuals
version: 1.0.0
pax_type: topic
description: When and why groups outthink individuals — the science of collective
  intelligence. Covers Woolley's c-factor (group IQ), Surowiecki's wisdom of crowds
  conditions, diversity-ability tradeoffs (Page), prediction markets, and the breakdown
  conditions where groups become dumber than their members. Bridges organizational
  psychology, decision science, and complexity theory.
author: ''
created: ''
license: ''
tags:
- topic
constructs:
- collective_intelligence_factor
- social_sensitivity
- conversational_turn_taking
- cognitive_diversity
- social_influence_bias
- prediction_market_accuracy
engines:
- ols_regression
- meta_analysis
- correlation_matrix
- logistic_regression
playbook_names:
- quick_start
construct_count: 6
finding_count: 0
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: collective_intelligence
  display_name: Collective Intelligence & Group Cognition
  description: Study of how cognitive diversity, social structure, and information
    aggregation rules determine whether groups produce more accurate judgments than
    individuals. Examines prediction markets, team problem-solving, crowd forecasting,
    and deliberation failures.
  research_questions: []
  temporal_scope: 1906-present
  population: Small groups (3-10), crowds (100+), online platforms, prediction markets
  level_of_analysis: meso
constructs_detail:
- id: collective_intelligence_factor
  display_name: Collective Intelligence Factor (c)
  definition: A single statistical factor explaining 30-50% of variance in group performance
    across diverse tasks — analogous to 'g' for individuals. Measured via group performance
    battery (Brainstorming, Typing, Matrix Reasoning, Moral Judgments). NOT correlated
    with average or maximum member IQ.
  aliases: []
  construct_type: quantifiable
- id: social_sensitivity
  display_name: Social Sensitivity
  definition: Average group member score on the Reading the Mind in the Eyes Test
    (RME). The strongest individual-level predictor of collective intelligence — groups
    with higher average social perceptiveness coordinate and integrate information
    more effectively.
  aliases: []
  construct_type: quantifiable
- id: conversational_turn_taking
  display_name: Conversational Turn-Taking Equality
  definition: Evenness of speaking time distribution within a group. Measured as 1
    - Gini coefficient of turn counts. Groups where one member dominates discussion
    show lower collective intelligence, even if that member is the smartest.
  aliases: []
  construct_type: quantifiable
- id: cognitive_diversity
  display_name: Cognitive Diversity
  definition: Variance in problem-solving approaches, mental models, and heuristics
    within a group. Operationalized via diverse cognitive toolkit measures or functional
    background diversity. Distinct from demographic diversity — cognitive diversity
    predicts group performance; demographic diversity does not after controlling for
    cognitive diversity.
  aliases: []
  construct_type: quantifiable
- id: social_influence_bias
  display_name: Social Influence Bias
  definition: The distortion of independent judgments when group members observe each
    others' estimates before finalizing their own. Reduces effective sample size of
    the crowd, destroying the error-cancellation mechanism that produces wisdom. Even
    small amounts of social information can cut crowd accuracy by 25-50%.
  aliases: []
  construct_type: concept
- id: prediction_market_accuracy
  display_name: Prediction Market Accuracy
  definition: Calibration and discrimination of market-aggregated probability estimates
    compared to polls, models, and expert panels. Prediction markets consistently
    outperform polls for election forecasting and match or beat expert panels for
    geopolitical questions. Brier scores typically 0.15-0.25 for well-functioning
    markets.
  aliases: []
  construct_type: outcome
findings_detail: []
propositions_detail: []
sources_detail: []
playbooks_detail: []
download_url: https://pax-market.com/pax/collective-intelligence-group-cognition.pax.tar.gz
download_size: 2.3 KB
published_by: Praxis Agent
related_packs: []
pax_name: collective-intelligence-group-cognition
weight: 10000
---

**Domain:** Collective Intelligence & Group Cognition

Study of how cognitive diversity, social structure, and information aggregation rules determine whether groups produce more accurate judgments than individuals. Examines prediction markets, team problem-solving, crowd forecasting, and deliberation failures.

**Temporal scope:** 1906-present | **Population:** Small groups (3-10), crowds (100+), online platforms, prediction markets

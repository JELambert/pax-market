---
name: sleep-cognition-productivity
title: Sleep Cognition Productivity
version: 1.0.0
pax_type: topic
description: 'How sleep duration and quality affect cognitive performance, decision-making,
  and economic productivity — the neuroscience and economics of sleep deprivation.
  Built on Walker, Dinges, Gibson & Shrader, Hafner et al. Data from ATUS (American
  Time Use Survey, 200K+ respondents), NHANES sleep modules, Fitbit/wearable population
  studies, and natural experiments using daylight saving time shifts. The most data-rich
  domain nobody packages: sleep is measured at population scale but rarely linked
  to economic outcomes.'
author: ''
created: ''
license: ''
tags:
- topic
constructs:
- sleep_duration
- cognitive_performance
- gdp_cost_of_sleep_loss
- sleep_quality
- workplace_accident_risk
- nap_restoration_effect
engines:
- ols_regression
- instrumental_variables
- difference_in_differences
- meta_analysis
- correlation_matrix
playbook_names:
- quick_start
construct_count: 6
finding_count: 0
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: sleep_cognition_productivity
  display_name: Sleep, Cognition & Economic Productivity
  description: Interdisciplinary study linking sleep duration and quality to cognitive
    performance, workplace productivity, and macroeconomic outcomes. Bridges neuroscience
    (memory consolidation, prefrontal function), occupational health (accident risk,
    absenteeism), and economics (GDP impact of insufficient sleep). Unique because
    individual-level sleep data exists at massive scale (wearables, time-use surveys)
    but cross-domain synthesis is rare.
  research_questions: []
  temporal_scope: 2003-present
  population: Working-age adults (18-65), population surveys, wearable device users,
    shift workers
  level_of_analysis: micro
constructs_detail:
- id: sleep_duration
  display_name: Sleep Duration
  definition: 'Total hours of sleep per 24-hour period, measured via polysomnography
    (gold standard), actigraphy (wearables), or self-report (ATUS, NHANES). Recommended
    7-9 hours for adults (AASM). US average: 6.8 hours on workdays. Population-level
    data available from ATUS (N>200K), NHANES sleep module, and Fitbit aggregate studies
    (N>6M nights).'
  aliases: []
  construct_type: quantifiable
- id: cognitive_performance
  display_name: Cognitive Performance Under Sleep Restriction
  definition: 'Composite of reaction time (PVT), working memory (n-back), executive
    function (Stroop), and decision quality measured after controlled sleep restriction.
    Performance declines are cumulative: 6h/night for 14 days produces impairment
    equivalent to 48 hours total sleep deprivation. Crucially, subjective sleepiness
    plateaus after ~3 days while objective impairment continues to worsen.'
  aliases: []
  construct_type: outcome
- id: gdp_cost_of_sleep_loss
  display_name: GDP Cost of Insufficient Sleep
  definition: 'Estimated annual GDP loss from workforce sleep deprivation through
    three channels: mortality (shorter lifespan), absenteeism (more sick days), and
    presenteeism (reduced on-the-job productivity). Hafner et al. (2017) estimate:
    US loses $411B/year (2.28% GDP), Japan $138B (2.92% GDP), UK $50B (1.86% GDP).
    Calculated via human capital approach.'
  aliases: []
  construct_type: quantifiable
- id: sleep_quality
  display_name: Sleep Quality
  definition: Composite measure of sleep efficiency (% time in bed asleep), number
    of awakenings, time in deep/REM sleep, and sleep onset latency. Pittsburgh Sleep
    Quality Index (PSQI) is the standard self-report instrument (0-21 scale, >5 =
    poor quality). Wearable devices now provide objective proxies at population scale.
  aliases: []
  construct_type: quantifiable
- id: workplace_accident_risk
  display_name: Workplace Accident Risk
  definition: Probability of occupational injury or error per shift as a function
    of prior sleep. Workers sleeping <6 hours have 1.7x the accident risk of those
    sleeping 7-8 hours. After DST spring-forward (population loses 1 hour), US workplace
    injuries increase 5.7% and severity increases 67.6% on the following Monday.
  aliases: []
  construct_type: outcome
- id: nap_restoration_effect
  display_name: Nap Restoration Effect
  definition: Degree to which a daytime nap (10-30 minutes) restores cognitive performance
    after sleep restriction. A 26-minute nap improves pilot performance by 34% and
    alertness by 54% (NASA nap study). However, naps do not fully compensate for chronic
    sleep debt — they provide temporary relief, not recovery. Longer naps (>30 min)
    risk sleep inertia.
  aliases: []
  construct_type: quantifiable
findings_detail: []
propositions_detail: []
sources_detail: []
playbooks_detail: []
download_url: https://pax-market.com/pax/sleep-cognition-productivity.pax.tar.gz
download_size: 2.7 KB
published_by: Praxis Agent
related_packs: []
pax_name: sleep-cognition-productivity
weight: 10000
---

**Domain:** Sleep, Cognition & Economic Productivity

Interdisciplinary study linking sleep duration and quality to cognitive performance, workplace productivity, and macroeconomic outcomes. Bridges neuroscience (memory consolidation, prefrontal function), occupational health (accident risk, absenteeism), and economics (GDP impact of insufficient sleep). Unique because individual-level sleep data exists at massive scale (wearables, time-use surveys) but cross-domain synthesis is rare.

**Temporal scope:** 2003-present | **Population:** Working-age adults (18-65), population surveys, wearable device users, shift workers

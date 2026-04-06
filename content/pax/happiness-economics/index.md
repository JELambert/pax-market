---
name: happiness-economics
title: Happiness Economics
version: 1.0.0
pax_type: topic
description: 'Subjective wellbeing and its economic, social, and institutional determinants.
  Based on the World Happiness Report 2023 framework: GDP per capita, social support,
  healthy life expectancy, freedom of choice, generosity, and perceptions of corruption
  as the six key predictors of national life satisfaction.'
author: ''
created: ''
license: ''
tags:
- topic
constructs:
- life_satisfaction
- social_support
- healthy_life_expectancy
- freedom_of_choice
- generosity
- perceptions_of_corruption
engines: []
playbook_names:
- quick_start
- standard_analysis
construct_count: 6
finding_count: 0
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: subjective_wellbeing
  display_name: Subjective Wellbeing
  description: Study of life satisfaction, happiness, and psychological wellbeing
    at the population level. Examines structural, social, economic, and institutional
    correlates of self-reported life evaluations.
  research_questions: []
  temporal_scope: 2005-present
  population: Sovereign states (country-year Gallup World Poll observations)
  level_of_analysis: macro
constructs_detail:
- id: life_satisfaction
  display_name: Life Satisfaction
  definition: 'Cantril Self-Anchoring Striving Scale: respondents rate their life
    on a ladder from 0 (worst possible life) to 10 (best possible life). National
    average. Primary outcome in WHR analyses.'
  aliases: []
  construct_type: quantifiable
- id: social_support
  display_name: Social Support
  definition: Share of respondents answering 'yes' to 'If you were in trouble, do
    you have relatives or friends you can count on?' Gallup World Poll. Ranges 0-1.
  aliases: []
  construct_type: quantifiable
- id: healthy_life_expectancy
  display_name: Healthy Life Expectancy
  definition: Healthy life expectancy at birth (years), from WHO/GHO data. Captures
    both longevity and health-adjusted quality of life.
  aliases: []
  construct_type: quantifiable
- id: freedom_of_choice
  display_name: Freedom of Choice
  definition: Share of respondents answering 'yes' to 'Are you satisfied or dissatisfied
    with your freedom to choose what you do with your life?' Ranges 0-1.
  aliases: []
  construct_type: quantifiable
- id: generosity
  display_name: Generosity
  definition: Residual of regressing national average response to 'Have you donated
    money to a charity in the past month?' on log GDP per capita. Captures pro-social
    behavior beyond what income explains.
  aliases: []
  construct_type: quantifiable
- id: perceptions_of_corruption
  display_name: Perceptions of Corruption
  definition: 'Average of two Gallup binary questions: is corruption widespread throughout
    government/business in this country? Ranges 0-1 (higher = more corruption perceived).'
  aliases: []
  construct_type: quantifiable
findings_detail: []
propositions_detail: []
sources_detail: []
playbooks_detail: []
download_url: https://pax-market.com/pax/happiness-economics.pax.tar.gz
download_size: 1.7 KB
published_by: Praxis Agent
related_packs:
- social-determinants-of-health
pax_name: happiness-economics
weight: 10000
---

**Domain:** Subjective Wellbeing

Study of life satisfaction, happiness, and psychological wellbeing at the population level. Examines structural, social, economic, and institutional correlates of self-reported life evaluations.

**Temporal scope:** 2005-present | **Population:** Sovereign states (country-year Gallup World Poll observations)

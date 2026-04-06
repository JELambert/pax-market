---
name: social-determinants-of-health
title: Social determinants of health
version: 1.0.0
pax_type: topic
description: Social determinants of health — how income, education, housing, social
  support, and neighborhood environment shape health outcomes and drive health inequalities.
  Built on Berkman & Syme (1979), Marmot (2005), Cutler & Lleras-Muney (2010), Chetty
  et al. (2016), and Holt-Lunstad et al. (2015).
author: ''
created: ''
license: ''
tags:
- topic
constructs:
- social_support
- educational_attainment
- social_isolation
- life_expectancy
- household_income
- income_inequality
engines:
- ols_regression
- logistic_regression
- cox_ph
- meta_analysis
- instrumental_variables
playbook_names:
- quick_start
construct_count: 6
finding_count: 0
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: social_determinants_of_health
  display_name: Social Determinants of Health
  description: Non-medical factors — income, education, housing, social support —
    that shape health outcomes and drive health inequalities within and between populations.
  research_questions: []
  temporal_scope: 1965-present
  population: General population, country-year and individual-level
  level_of_analysis: macro
constructs_detail:
- id: social_support
  display_name: Social Support
  definition: Share of respondents answering 'yes' to 'If you were in trouble, do
    you have relatives or friends you can count on?' Gallup World Poll. Ranges 0-1.
  aliases: []
  construct_type: quantifiable
- id: educational_attainment
  display_name: Educational Attainment
  definition: Highest level of formal schooling completed, operationalized as years
    of schooling or credential level.
  aliases: []
  construct_type: quantifiable
- id: social_isolation
  display_name: Social Isolation
  definition: Objective lack of social contacts or relationships, measured by network
    size or frequency of social interaction.
  aliases: []
  construct_type: quantifiable
- id: life_expectancy
  display_name: Life Expectancy at Birth
  definition: Average number of years a newborn is expected to live given current
    age-specific mortality rates.
  aliases: []
  construct_type: outcome
- id: household_income
  display_name: Household Income
  definition: Annual pre-tax income received by all members of a household, inflation-adjusted.
    Primary measure of material resources for health-relevant consumption.
  aliases: []
  construct_type: quantifiable
- id: income_inequality
  display_name: Income Inequality
  definition: Degree of dispersion in income distribution, most commonly measured
    by the Gini coefficient (0-1 scale).
  aliases: []
  construct_type: quantifiable
findings_detail: []
propositions_detail: []
sources_detail: []
playbooks_detail: []
download_url: https://pax-market.com/pax/social-determinants-of-health.pax.tar.gz
download_size: 1.8 KB
published_by: Praxis Agent
related_packs:
- happiness-economics
- health-outcomes-global
pax_name: social-determinants-of-health
weight: 10000
---

**Domain:** Social Determinants of Health

Non-medical factors — income, education, housing, social support — that shape health outcomes and drive health inequalities within and between populations.

**Temporal scope:** 1965-present | **Population:** General population, country-year and individual-level

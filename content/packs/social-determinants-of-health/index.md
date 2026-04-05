---
title: Social determinants of health
pax_name: social-determinants-of-health
version: 1.0.0
pax_type: topic
description: Social determinants of health — how income, education, housing, social
  support, and neighborhood environment shape health outcomes and drive health inequalities.
  Built on Berkman & Syme (1979), Marmot (2005), Cutler & Lleras-Muney (2010), Chetty
  et al. (2016), and Holt-Lunstad et al. (2015).
author: Berkman, Lisa F.; Marmot, Michael; Cutler, David M.; Chetty, Raj; Holt-Lunstad,
  Julianne
created: '2026-04-04'
license: ''
tags:
- topic
- social-determinants-of-health
constructs:
- household_income
- educational_attainment
- income_inequality
- social_support
- social_isolation
- life_expectancy
engines:
- ols_regression
- logistic_regression
- cox_ph
- meta_analysis
- instrumental_variables
playbook_names:
- quick_start
construct_count: 6
finding_count: 5
proposition_count: 0
has_playbooks: true
has_data_sources: true
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
- id: household_income
  display_name: Household Income
  definition: Annual pre-tax income received by all members of a household, inflation-adjusted.
    Primary measure of material resources for health-relevant consumption.
  aliases:
  - family income
  - income level
  construct_type: quantifiable
- id: educational_attainment
  display_name: Educational Attainment
  definition: Highest level of formal schooling completed, operationalized as years
    of schooling or credential level.
  aliases:
  - years of schooling
  - education level
  construct_type: quantifiable
- id: income_inequality
  display_name: Income Inequality
  definition: Degree of dispersion in income distribution, most commonly measured
    by the Gini coefficient (0-1 scale).
  aliases:
  - Gini coefficient
  - economic inequality
  construct_type: quantifiable
- id: social_support
  display_name: Social Support
  definition: Perceived or received availability of emotional, informational, or instrumental
    assistance from social network members.
  aliases:
  - social ties
  - social connectedness
  construct_type: quantifiable
- id: social_isolation
  display_name: Social Isolation
  definition: Objective lack of social contacts or relationships, measured by network
    size or frequency of social interaction.
  aliases:
  - loneliness
  - social disconnection
  construct_type: quantifiable
- id: life_expectancy
  display_name: Life Expectancy at Birth
  definition: Average number of years a newborn is expected to live given current
    age-specific mortality rates.
  aliases:
  - longevity
  - all-cause mortality
  construct_type: outcome
findings_detail:
- finding_text: People with fewest social ties had age-adjusted relative mortality
    risks of 2.3 (men) and 2.8 (women) over nine years, independent of SES and health
    behaviors.
  construct_ids:
  - social_isolation
  - life_expectancy
  direction: negative
  effect_size: ''
  confidence: strong
  method_used: Cox proportional hazards
  finding_type: ''
  evidence_type: ''
- finding_text: A consistent social gradient in health runs from top to bottom of
    the occupational hierarchy; higher social position predicts better health outcomes.
  construct_ids:
  - household_income
  - life_expectancy
  direction: positive
  effect_size: ''
  confidence: strong
  method_used: Descriptive epidemiology
  finding_type: ''
  evidence_type: ''
- finding_text: Income, insurance, and background account for ~30% of the education-health
    gradient; knowledge and cognitive ability ~30%; social networks ~10%.
  construct_ids:
  - educational_attainment
  - household_income
  - social_support
  - life_expectancy
  direction: positive
  effect_size: ''
  confidence: strong
  method_used: OLS regression
  finding_type: ''
  evidence_type: ''
- finding_text: Gap in life expectancy between richest 1% and poorest 1% of Americans
    is 14.6 years for men and 10.1 years for women.
  construct_ids:
  - household_income
  - life_expectancy
  direction: positive
  effect_size: ''
  confidence: strong
  method_used: Descriptive regression, N=1.4 billion
  finding_type: ''
  evidence_type: ''
- finding_text: 'Meta-analysis of 70 studies: social isolation (OR=1.29), loneliness
    (OR=1.26), and living alone (OR=1.32) each predicted elevated all-cause mortality.'
  construct_ids:
  - social_isolation
  - life_expectancy
  direction: negative
  effect_size: ''
  confidence: strong
  method_used: Meta-analysis, N=3.4 million
  finding_type: ''
  evidence_type: ''
propositions_detail: []
sources_detail:
- id: berkman_syme_1979
  title: 'Social Networks, Host Resistance, and Mortality: A Nine-Year Follow-Up Study
    of Alameda County Residents'
  authors: Berkman, Lisa F.; Syme, S. Leonard
  year: 1979
  doi: null
  source_type: journal_article
- id: marmot_2005
  title: Social Determinants of Health Inequalities
  authors: Marmot, Michael
  year: 2005
  doi: null
  source_type: journal_article
- id: cutler_lleras_muney_2010
  title: Understanding Differences in Health Behaviors by Education
  authors: Cutler, David M.; Lleras-Muney, Adriana
  year: 2010
  doi: null
  source_type: journal_article
- id: chetty_2016
  title: The Association Between Income and Life Expectancy in the United States,
    2001-2014
  authors: Chetty, Raj; Stepner, Michael; Abraham, Sarah
  year: 2016
  doi: null
  source_type: journal_article
- id: holt_lunstad_2015
  title: 'Loneliness and Social Isolation as Risk Factors for Mortality: A Meta-Analytic
    Review'
  authors: Holt-Lunstad, Julianne; Smith, Timothy B.; Baker, Mark
  year: 2015
  doi: null
  source_type: journal_article
playbooks_detail:
- id: quick_start
  display_name: Quick Start — Social Determinants Of Health
  description: Basic analysis workflow for the social_determinants_of_health domain.
  estimated_runtime: 1–3 minutes
  step_count: 1
  engines_used:
  - logistic_regression
download_url: /packs/social-determinants-of-health.pax.tar.gz
download_size: 3.2 KB
weight: 7974
related_packs:
- happiness-economics
- health-outcomes-global
---

**Domain:** Social Determinants of Health

Non-medical factors — income, education, housing, social support — that shape health outcomes and drive health inequalities within and between populations.

**Temporal scope:** 1965-present | **Population:** General population, country-year and individual-level

## Key Findings

- People with fewest social ties had age-adjusted relative mortality risks of 2.3 (men) and 2.8 (women) over nine years, independent of SES and health behaviors. *(negative, strong)*
- A consistent social gradient in health runs from top to bottom of the occupational hierarchy; higher social position predicts better health outcomes. *(positive, strong)*
- Income, insurance, and background account for ~30% of the education-health gradient; knowledge and cognitive ability ~30%; social networks ~10%. *(positive, strong)*
- Gap in life expectancy between richest 1% and poorest 1% of Americans is 14.6 years for men and 10.1 years for women. *(positive, strong)*
- Meta-analysis of 70 studies: social isolation (OR=1.29), loneliness (OR=1.26), and living alone (OR=1.32) each predicted elevated all-cause mortality. *(negative, strong)*

## Sources

- Berkman, Lisa F.; Syme, S. Leonard (1979). *Social Networks, Host Resistance, and Mortality: A Nine-Year Follow-Up Study of Alameda County Residents*.
- Marmot, Michael (2005). *Social Determinants of Health Inequalities*.
- Cutler, David M.; Lleras-Muney, Adriana (2010). *Understanding Differences in Health Behaviors by Education*.
- Chetty, Raj; Stepner, Michael; Abraham, Sarah (2016). *The Association Between Income and Life Expectancy in the United States, 2001-2014*.
- Holt-Lunstad, Julianne; Smith, Timothy B.; Baker, Mark (2015). *Loneliness and Social Isolation as Risk Factors for Mortality: A Meta-Analytic Review*.

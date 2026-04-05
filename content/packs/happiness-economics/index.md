---
title: Happiness Economics
pax_name: happiness-economics
version: 1.0.0
pax_type: topic
description: 'Subjective wellbeing and its economic, social, and institutional determinants.
  Based on the World Happiness Report 2023 framework: GDP per capita, social support,
  healthy life expectancy, freedom of choice, generosity, and perceptions of corruption
  as the six key predictors of national life satisfaction.'
author: Helliwell, Layard, Sachs, De Neve, Aknin, Wang
created: '2023-03-20'
license: CC-BY-4.0
tags:
- happiness
- wellbeing
- economics
- life-satisfaction
- gallup-world-poll
constructs:
- life_satisfaction
- social_support
- healthy_life_expectancy
- freedom_of_choice
- generosity
- perceptions_of_corruption
engines:
- ''
playbook_names:
- quick_start
- standard_analysis
construct_count: 6
finding_count: 7
proposition_count: 4
has_playbooks: true
has_data_sources: true
domain:
  id: subjective_wellbeing
  display_name: Subjective Wellbeing
  description: Study of life satisfaction, happiness, and psychological wellbeing
    at the population level. Examines structural, social, economic, and institutional
    correlates of self-reported life evaluations.
  research_questions:
  - What economic and social factors predict national life satisfaction?
  - Does income growth translate to happiness gains at the national level?
  - How do social support and institutional trust affect wellbeing?
  - What role does freedom and absence of corruption play in life satisfaction?
  temporal_scope: 2005-present
  population: Sovereign states (country-year Gallup World Poll observations)
  level_of_analysis: macro
constructs_detail:
- id: life_satisfaction
  display_name: Life Satisfaction
  definition: 'Cantril Self-Anchoring Striving Scale: respondents rate their life
    on a ladder from 0 (worst possible life) to 10 (best possible life). National
    average. Primary outcome in WHR analyses.'
  aliases:
  - subjective wellbeing
  - SWB
  - happiness score
  - Cantril ladder
  - life evaluation
  - wellbeing index
  construct_type: quantifiable
- id: social_support
  display_name: Social Support
  definition: Share of respondents answering 'yes' to 'If you were in trouble, do
    you have relatives or friends you can count on?' Gallup World Poll. Ranges 0-1.
  aliases:
  - social connections
  - social capital (informal)
  - having someone to count on
  - social ties
  - social connectedness
  construct_type: quantifiable
- id: healthy_life_expectancy
  display_name: Healthy Life Expectancy
  definition: Healthy life expectancy at birth (years), from WHO/GHO data. Captures
    both longevity and health-adjusted quality of life.
  aliases:
  - HLE
  - HALE
  - health-adjusted life expectancy
  construct_type: quantifiable
- id: freedom_of_choice
  display_name: Freedom of Choice
  definition: Share of respondents answering 'yes' to 'Are you satisfied or dissatisfied
    with your freedom to choose what you do with your life?' Ranges 0-1.
  aliases:
  - autonomy
  - life freedom
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
  aliases:
  - corruption index
  - institutional trust (inverse)
  construct_type: quantifiable
findings_detail:
- finding_text: GDP per capita (log) positively predicts life satisfaction. A one
    log unit increase is associated with approximately +0.35 points on the Cantril
    ladder. Log GDP per capita independently explains roughly 25% of cross-national
    variance in ladder scores.
  construct_ids:
  - life_satisfaction
  - per_capita_income
  direction: positive
  effect_size: strong — explains ~25% of cross-national variance in ladder scores
    independently
  confidence: strong
  method_used: OLS regression, country-year panel with year fixed effects, N≈1,700
    country-years across 2005-2022, Gallup World Poll
  finding_type: empirical
  evidence_type: quantitative
- finding_text: Social support is a strong positive predictor of life satisfaction.
    A one-unit increase in the social support proportion is associated with approximately
    +1.4 points on the Cantril ladder.
  construct_ids:
  - life_satisfaction
  - social_support
  direction: positive
  effect_size: strong
  confidence: strong
  method_used: OLS regression, country-year panel with year fixed effects, N≈1,700
    country-years across 2005-2022, Gallup World Poll
  finding_type: empirical
  evidence_type: quantitative
- finding_text: Healthy life expectancy positively predicts life satisfaction. Each
    additional year of healthy life expectancy at birth is associated with approximately
    +0.03 points on the Cantril ladder.
  construct_ids:
  - life_satisfaction
  - healthy_life_expectancy
  direction: positive
  effect_size: moderate
  confidence: strong
  method_used: OLS regression, country-year panel with year fixed effects, N≈1,700
    country-years across 2005-2022, Gallup World Poll
  finding_type: empirical
  evidence_type: quantitative
- finding_text: Freedom of choice positively predicts life satisfaction. A one-unit
    increase in the freedom proportion is associated with approximately +1.2 points
    on the Cantril ladder.
  construct_ids:
  - life_satisfaction
  - freedom_of_choice
  direction: positive
  effect_size: moderate to strong
  confidence: strong
  method_used: OLS regression, country-year panel with year fixed effects, N≈1,700
    country-years across 2005-2022, Gallup World Poll
  finding_type: empirical
  evidence_type: quantitative
- finding_text: Perceptions of corruption negatively predict life satisfaction. A
    one-unit increase in corruption perceptions is associated with approximately -0.7
    points on the Cantril ladder.
  construct_ids:
  - life_satisfaction
  - perceptions_of_corruption
  direction: negative
  effect_size: moderate
  confidence: strong
  method_used: OLS regression, country-year panel with year fixed effects, N≈1,700
    country-years across 2005-2022, Gallup World Poll
  finding_type: empirical
  evidence_type: quantitative
- finding_text: Generosity is positively but weakly associated with life satisfaction.
    A one-unit increase in the generosity residual is associated with approximately
    +0.5 points on the Cantril ladder, though this relationship is less robust than
    the other five WHR predictors.
  construct_ids:
  - life_satisfaction
  - generosity
  direction: positive
  effect_size: weak to moderate
  confidence: moderate
  method_used: OLS regression, country-year panel with year fixed effects, N≈1,700
    country-years across 2005-2022, Gallup World Poll
  finding_type: empirical
  evidence_type: quantitative
- finding_text: The income-happiness relationship shows diminishing returns at high
    income levels. The slope between log GDP per capita and life satisfaction is steeper
    for lower-income countries, suggesting that additional income yields larger wellbeing
    gains in poorer nations.
  construct_ids:
  - life_satisfaction
  - per_capita_income
  direction: positive
  effect_size: nonlinear — stronger for poor countries
  confidence: moderate
  method_used: OLS regression, country-year panel with year fixed effects, N≈1,700
    country-years across 2005-2022, Gallup World Poll
  finding_type: mechanism
  evidence_type: mixed
propositions_detail:
- id: gdp_increases_happiness
  proposition_text: Higher national income (log GDP per capita) is positively associated
    with higher average life satisfaction scores across countries, though with diminishing
    returns and contested within-country dynamics (Easterlin Paradox).
  construct_from: per_capita_income
  construct_to: life_satisfaction
  direction: positive
  scope_conditions: Cross-sectional macro analysis; effect is concave and may not
    hold within countries over time
- id: social_support_increases_happiness
  proposition_text: Countries where more people report having someone to count on
    in times of trouble score substantially higher on the Cantril ladder. Social support
    is the strongest bivariate predictor of cross-national happiness differences.
  construct_from: social_support
  construct_to: life_satisfaction
  direction: positive
  scope_conditions: Bivariate association is strong; partial effects smaller in multivariate
    models controlling for GDP, health, and institutions
- id: freedom_predicts_happiness
  proposition_text: Freedom to make life choices has a strong positive association
    with life satisfaction, and dominates as the largest standardized coefficient
    in full multivariate models including GDP, social support, health, generosity,
    and corruption perceptions.
  construct_from: freedom_of_choice
  construct_to: life_satisfaction
  direction: positive
  scope_conditions: Conditional on partialling out other WHR predictors; in bivariate
    analysis social support is stronger
- id: diminishing_returns_income_happiness
  proposition_text: 'The income-happiness relationship follows a logarithmic (concave)
    function: equal percentage income gains produce roughly equal happiness gains,
    implying diminishing absolute returns to income as wealth increases.'
  construct_from: per_capita_income
  construct_to: life_satisfaction
  direction: positive
  scope_conditions: Log-linear fit supported in cross-national macro data; individual-level
    saturation threshold debated (Kahneman $75k vs Killingsworth $100k+)
sources_detail:
- id: world_happiness_report_2023
  title: World Happiness Report 2023
  authors: Helliwell, John F.; Layard, Richard; Sachs, Jeffrey D.; De Neve, Jan-Emmanuel;
    Aknin, Lara B.; Wang, Shun
  year: 2023
  doi: null
  source_type: academic_paper
playbooks_detail:
- id: quick_start
  display_name: Quick Start — Run This First
  description: 'Two-step minimal analysis to verify data acquisition and get an immediate
    sense of the core happiness-income-social relationships. Runs in under 2 minutes.
    No prior setup required. Run this before standard_analysis to confirm the data
    pipeline is working correctly.

    '
  estimated_runtime: 1–2 minutes
  step_count: 2
  engines_used:
  - correlation_matrix
- id: standard_analysis
  display_name: Standard Happiness-Economics Analysis
  description: 'Full four-step analysis of cross-national happiness determinants.
    Runs data acquisition, a full correlation matrix, a multivariate OLS regression
    of all six WHR predictors, and a bivariate deep dive on the freedom-happiness
    relationship. Produces publication-ready tables and plots.

    '
  estimated_runtime: 3–8 minutes depending on API latency
  step_count: 4
  engines_used:
  - ols_regression
  - correlation_matrix
download_url: /packs/happiness-economics.pax.tar.gz
download_size: 9.7 KB
weight: 7977
related_packs:
- social-determinants-of-health
---

# happiness-economics — Praxis PAX

A Praxis PAX for the economics of happiness and subjective well-being.

## What This PAX Contains

**Domain:** Cross-national determinants of life satisfaction, anchored by the World Happiness Report and Blanchflower (2020).

**7 Constructs:**
- `subjective_wellbeing` — Cantril ladder score (0–10), the outcome variable
- `gdp_per_capita_log` — Log GDP per capita (PPP), primary income predictor
- `social_support` — Proportion with someone to count on (Gallup)
- `healthy_life_expectancy` — WHO HALE at birth
- `freedom_life_choices` — Proportion satisfied with life freedom (Gallup)
- `generosity` — Charitable giving residualized on GDP
- `corruption_perception` — Proportion perceiving widespread corruption (Gallup)

**3 Propositions:** GDP increases happiness (positive, diminishing returns); social support increases happiness (strongest bivariate predictor); freedom dominates in multivariate models.

**2 Key Findings:** U-shaped age-happiness curve is universal across 145 countries (Blanchflower 2020); the six WHR factors explain >95% of variance in national Cantril scores (WHR 2024).

**2 Playbooks:** `quick_start` (2 steps, run first) and `standard_analysis` (4 steps, full analysis).

**2 Engines:** `ols_regression` and `correlation_matrix` (both from praxis-core).

## Data Sources

- **WHR 2024** — Auto-fetched from S3. Local cache at `data/raw/whr_2024.xls`.
- **World Bank WGI** — Auto-fetched via REST API. Local cache at `data/raw/wgi_cc.json`.

## How to Install

```bash
praxis pax install happiness-economics
```

Or clone this directory into your local pax folder and run:

```bash
praxis pax load ./pax/happiness-economics/
```

## How to Run

Start here:

```bash
praxis playbook run quick_start
```

Full analysis:

```bash
praxis playbook run standard_analysis
```

## Dependencies

- `core-economics` (optional) — adds baseline macroeconomic constructs. This PAX runs standalone without it.

## Refresh Policy

Annual. Refresh after each new World Happiness Report release (typically March). Update `data/sources.yaml` with the new WHR URL and re-run `standard_analysis` to check finding replication.

## Key References

- Helliwell, Layard, Sachs et al. — World Happiness Report 2024
- Blanchflower — Is Happiness U-Shaped Everywhere? (2020), *Journal of Population Economics*
- Stevenson & Wolfers — Subjective Well-Being and Income (2013)
- Kahneman & Deaton — High Income Improves Life Evaluation (2010)

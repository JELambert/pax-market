---
title: 'Subjective wellbeing and its economic, social, and institutional determinants.
  Based on the World Happiness Report 2023 framework: GDP per capita, social support,
  healthy life expectancy, freedom of choice, generosity, and perceptions of corruption
  as the six key predictors of national life satisfaction.'
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
findings: []
engines: []
construct_count: 6
finding_count: 7
has_playbooks: true
has_data_sources: true
download_url: /packs/happiness-economics.pax.tar.gz
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

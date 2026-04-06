---
name: education-outcomes
title: Education Outcomes
version: 1.0.0
pax_type: topic
description: How education spending, access, and quality affect learning outcomes,
  human capital formation, and economic returns across countries.
author: null
created: '2026-04-05'
license: null
tags:
- topic
- education-outcomes
constructs:
- mean_years_schooling
- education_expenditure_gdp_pct
- adult_literacy_rate
- learning_adjusted_years_schooling
- primary_enrollment_rate
- pupil_teacher_ratio
engines:
- ols_regression
- correlation_matrix
- random_forest
playbook_names:
- quick_start
construct_count: 6
finding_count: 8
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: education_outcomes
  display_name: Education Systems and Learning Outcomes
  description: How education spending, access, and quality affect learning outcomes,
    human capital formation, and economic returns
  research_questions: []
  temporal_scope: 1990-present
  population: Countries worldwide
  level_of_analysis: macro
constructs_detail:
- id: mean_years_schooling
  display_name: Mean Years of Schooling
  definition: Average years of formal education completed by adults aged 25+. Primary
    macro proxy for human capital stock.
  aliases: []
  construct_type: quantifiable
- id: education_expenditure_gdp_pct
  display_name: Education Expenditure as Percent of GDP
  definition: Total public expenditure on education as a percentage of gross domestic
    product, capturing government prioritization of education in national budgets
  aliases: []
  construct_type: quantifiable
- id: adult_literacy_rate
  display_name: Adult Literacy Rate
  definition: Percentage of population aged 15 and above who can read and write a
    short simple statement about their everyday life, measuring basic educational
    attainment
  aliases: []
  construct_type: quantifiable
- id: learning_adjusted_years_schooling
  display_name: Learning-Adjusted Years of Schooling
  definition: World Bank measure that combines quantity of schooling with quality
    of learning, discounting years of schooling by actual learning achievement on
    harmonized test scores
  aliases: []
  construct_type: quantifiable
- id: primary_enrollment_rate
  display_name: Primary Enrollment Rate
  definition: Gross enrollment ratio in primary education, calculated as total enrollment
    in primary education regardless of age divided by the population of official primary
    education age
  aliases: []
  construct_type: quantifiable
- id: pupil_teacher_ratio
  display_name: Pupil-Teacher Ratio
  definition: Average number of pupils per teacher at a given level of education,
    serving as a proxy for class size and resource allocation in the education system
  aliases: []
  construct_type: quantifiable
findings_detail:
- finding_text: One SD increase in cognitive skills test scores associated with ~2
    pp higher annual GDP growth. Robust to IV identification.
  construct_ids:
  - cognitive_skills
  - gdp_per_capita_growth
  direction: positive
  effect_size: null
  confidence: strong
  method_used: OLS and IV cross-country
- finding_text: Years of schooling loses significance once cognitive skills are controlled
    for — quantity without quality doesn't drive growth.
  construct_ids:
  - mean_years_schooling
  - cognitive_skills
  - gdp_per_capita_growth
  direction: 'null'
  effect_size: null
  confidence: moderate
  method_used: OLS with joint inclusion
- finding_text: Global average private return to one year of schooling is ~9% per
    year across 1,120 estimates in 139 countries.
  construct_ids:
  - mean_years_schooling
  direction: positive
  effect_size: null
  confidence: strong
  method_used: Meta-analysis of Mincerian regressions
- finding_text: Cognitive skills (test scores) are far more important for economic
    growth than years of schooling, with beta approximately 0.6 on growth versus beta
    approximately 0.1 for years of schooling.
  construct_ids:
  - cognitive_test_scores
  - years_of_schooling
  direction: positive
  effect_size: β≈0.6 for test scores vs β≈0.1 for years of schooling
  confidence: strong
  method_used: Cross-country OLS and IV regressions
- finding_text: School quality (proxied by test scores) explains most of cross-country
    variation in growth rates, not school quantity. A one standard deviation increase
    in test scores is associated with approximately 2 percentage points higher annual
    GDP growth.
  construct_ids:
  - cognitive_test_scores
  direction: positive
  effect_size: 1 SD increase in test scores → 2% higher annual GDP growth
  confidence: strong
  method_used: Cross-country panel regression with IV
- finding_text: Cognitive skills measured by international test scores are more strongly
    predictive of economic growth than years of schooling alone, with one standard
    deviation in test scores associated with 2 percentage points higher annual GDP
    growth
  construct_ids:
  - learning_adjusted_years_schooling
  - mean_years_schooling
  direction: positive
  effect_size: null
  confidence: strong
  method_used: ols_regression
- finding_text: Global average private returns to an additional year of schooling
    are approximately 9 percent per year, with returns highest in Sub-Saharan Africa
    and for primary education
  construct_ids:
  - mean_years_schooling
  direction: positive
  effect_size: null
  confidence: strong
  method_used: ols_regression
- finding_text: Pupil-teacher ratio is negatively associated with learning outcomes
    in developing countries, though the effect size is smaller than often assumed
    and depends on teacher quality
  construct_ids:
  - pupil_teacher_ratio
  - learning_adjusted_years_schooling
  direction: negative
  effect_size: null
  confidence: moderate
  method_used: random_forest
propositions_detail: []
sources_detail:
- id: hanushek_woessmann_2012
  title: Do Better Schools Lead to More Growth? Cognitive Skills, Economic Outcomes,
    and Causation
  authors: Hanushek, Eric A.; Woessmann, Ludger
  year: 2012
  doi: null
  source_type: academic_paper
- id: psacharopoulos_patrinos_2018
  title: 'Returns to Investment in Education: A Decennial Review of the Global Literature'
  authors: Psacharopoulos, George; Patrinos, Harry Anthony
  year: 2018
  doi: null
  source_type: academic_paper
- id: world_bank_hci_2020
  title: 'Human Capital Index 2020 Update: Human Capital in the Time of COVID-19'
  authors: World Bank
  year: 2020
  doi: null
  source_type: report
- id: glewwe_muralidharan_2016
  title: 'Improving Education Outcomes in Developing Countries: Evidence, Knowledge
    Gaps, and Policy Implications'
  authors: Glewwe, P., Muralidharan, K.
  year: 2016
  doi: null
  source_type: book_chapter
playbooks_detail: []
download_url: https://pax-market.com/pax/education-outcomes.pax.tar.gz
download_size: 3.3 KB
published_by: Praxis Agent
related_packs:
- human-capital-economics
pax_name: education-outcomes
weight: 7974
---

**Domain:** Education Systems and Learning Outcomes

How education spending, access, and quality affect learning outcomes, human capital formation, and economic returns

**Temporal scope:** 1990-present | **Population:** Countries worldwide

## Key Findings

- One SD increase in cognitive skills test scores associated with ~2 pp higher annual GDP growth. Robust to IV identification. *(positive, strong)*
- Years of schooling loses significance once cognitive skills are controlled for — quantity without quality doesn't drive growth. *(null, moderate)*
- Global average private return to one year of schooling is ~9% per year across 1,120 estimates in 139 countries. *(positive, strong)*
- Cognitive skills (test scores) are far more important for economic growth than years of schooling, with beta approximately 0.6 on growth versus beta approximately 0.1 for years of schooling. *(positive, strong)*
- School quality (proxied by test scores) explains most of cross-country variation in growth rates, not school quantity. A one standard deviation increase in test scores is associated with approximately 2 percentage points higher annual GDP growth. *(positive, strong)*
- Cognitive skills measured by international test scores are more strongly predictive of economic growth than years of schooling alone, with one standard deviation in test scores associated with 2 percentage points higher annual GDP growth *(positive, strong)*
- Global average private returns to an additional year of schooling are approximately 9 percent per year, with returns highest in Sub-Saharan Africa and for primary education *(positive, strong)*
- Pupil-teacher ratio is negatively associated with learning outcomes in developing countries, though the effect size is smaller than often assumed and depends on teacher quality *(negative, moderate)*

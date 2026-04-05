---
title: Returns to education and human capital economics
pax_name: human-capital-economics
version: 1.0.0
pax_type: topic
description: Returns to education and human capital economics — how educational attainment,
  cognitive skills, and schooling investment shape GDP growth and economic development.
  Built on Mankiw, Romer & Weil (1992), Psacharopoulos & Patrinos (2018), Hanushek
  & Woessmann (2012), Card (1995), and Barro (2001).
author: Mankiw, N. Gregory; Hanushek, Eric A.; Psacharopoulos, George; Card, David;
  Barro, Robert J.
created: '2026-04-04'
license: ''
tags:
- topic
- human-capital-economics
constructs:
- mean_years_schooling
- cognitive_skills
- school_enrollment_rate
- physical_capital_investment
engines:
- ols_regression
- instrumental_variables
- meta_analysis
- correlation_matrix
playbook_names:
- quick_start
construct_count: 4
finding_count: 4
proposition_count: 0
has_playbooks: true
has_data_sources: true
domain:
  id: human_capital_economics
  display_name: Human Capital Economics
  description: How educational attainment, cognitive skills, and schooling investment
    shape GDP growth, productivity, and economic development at the country level.
  research_questions: []
  temporal_scope: 1950-present
  population: Sovereign states (country-year, 100-150 countries)
  level_of_analysis: macro
constructs_detail:
- id: mean_years_schooling
  display_name: Mean Years of Schooling
  definition: Average years of formal education completed by adults aged 25+. Primary
    macro proxy for human capital stock.
  aliases:
  - educational attainment
  - years of schooling
  construct_type: quantifiable
- id: cognitive_skills
  display_name: Cognitive Skills
  definition: National average score on internationally comparable standardized tests
    (PISA, TIMSS). Captures educational quality.
  aliases:
  - test scores
  - human capital quality
  construct_type: quantifiable
- id: school_enrollment_rate
  display_name: School Enrollment Rate
  definition: Gross or net enrollment ratio at primary, secondary, or tertiary level.
    Flow proxy for human capital investment.
  aliases:
  - enrollment ratio
  - secondary enrollment
  construct_type: quantifiable
- id: physical_capital_investment
  display_name: Physical Capital Investment
  definition: Gross fixed capital formation as share of GDP. Key control in augmented
    Solow growth regressions.
  aliases:
  - investment share
  - capital accumulation
  construct_type: quantifiable
findings_detail:
- finding_text: Augmented Solow model including human capital explains ~80% of cross-country
    income variance vs 59% for baseline. Human capital coefficient positive and significant.
  construct_ids:
  - school_enrollment_rate
  - physical_capital_investment
  - gdp_per_capita_growth
  direction: positive
  effect_size: ''
  confidence: strong
  method_used: OLS cross-section, N=98
  finding_type: ''
  evidence_type: ''
- finding_text: One SD increase in cognitive skills test scores associated with ~2
    pp higher annual GDP growth. Robust to IV identification.
  construct_ids:
  - cognitive_skills
  - gdp_per_capita_growth
  direction: positive
  effect_size: ''
  confidence: strong
  method_used: OLS and IV cross-country
  finding_type: ''
  evidence_type: ''
- finding_text: Years of schooling loses significance once cognitive skills are controlled
    for — quantity without quality doesn't drive growth.
  construct_ids:
  - mean_years_schooling
  - cognitive_skills
  - gdp_per_capita_growth
  direction: 'null'
  effect_size: ''
  confidence: moderate
  method_used: OLS with joint inclusion
  finding_type: ''
  evidence_type: ''
- finding_text: Global average private return to one year of schooling is ~9% per
    year across 1,120 estimates in 139 countries.
  construct_ids:
  - mean_years_schooling
  direction: positive
  effect_size: ''
  confidence: strong
  method_used: Meta-analysis of Mincerian regressions
  finding_type: ''
  evidence_type: ''
propositions_detail: []
sources_detail:
- id: mankiw_romer_weil_1992
  title: A Contribution to the Empirics of Economic Growth
  authors: Mankiw, N. Gregory; Romer, David; Weil, David N.
  year: 1992
  doi: null
  source_type: academic_paper
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
- id: card_1995
  title: Using Geographic Variation in College Proximity to Estimate the Return to
    Schooling
  authors: Card, David
  year: 1995
  doi: null
  source_type: academic_paper
- id: barro_2001
  title: Human Capital and Growth
  authors: Barro, Robert J.
  year: 2001
  doi: null
  source_type: academic_paper
playbooks_detail:
- id: quick_start
  display_name: Quick Start — Human Capital Economics
  description: Basic analysis workflow for the human_capital_economics domain.
  estimated_runtime: 1–3 minutes
  step_count: 1
  engines_used:
  - correlation_matrix
download_url: /packs/human-capital-economics.pax.tar.gz
download_size: 2.8 KB
weight: 7974
related_packs: []
---

**Domain:** Human Capital Economics

How educational attainment, cognitive skills, and schooling investment shape GDP growth, productivity, and economic development at the country level.

**Temporal scope:** 1950-present | **Population:** Sovereign states (country-year, 100-150 countries)

## Key Findings

- Augmented Solow model including human capital explains ~80% of cross-country income variance vs 59% for baseline. Human capital coefficient positive and significant. *(positive, strong)*
- One SD increase in cognitive skills test scores associated with ~2 pp higher annual GDP growth. Robust to IV identification. *(positive, strong)*
- Years of schooling loses significance once cognitive skills are controlled for — quantity without quality doesn't drive growth. *(null, moderate)*
- Global average private return to one year of schooling is ~9% per year across 1,120 estimates in 139 countries. *(positive, strong)*

## Sources

- Mankiw, N. Gregory; Romer, David; Weil, David N. (1992). *A Contribution to the Empirics of Economic Growth*.
- Hanushek, Eric A.; Woessmann, Ludger (2012). *Do Better Schools Lead to More Growth? Cognitive Skills, Economic Outcomes, and Causation*.
- Psacharopoulos, George; Patrinos, Harry Anthony (2018). *Returns to Investment in Education: A Decennial Review of the Global Literature*.
- Card, David (1995). *Using Geographic Variation in College Proximity to Estimate the Return to Schooling*.
- Barro, Robert J. (2001). *Human Capital and Growth*.

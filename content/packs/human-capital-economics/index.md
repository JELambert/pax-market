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
findings:
- mankiw_romer_weil_1992_0
- hanushek_woessmann_2012_1
- hanushek_woessmann_2012_2
- psacharopoulos_patrinos_2018_3
engines:
- ols_regression
- instrumental_variables
- meta_analysis
- correlation_matrix
playbooks:
- quick_start
propositions: []
construct_count: 4
finding_count: 4
proposition_count: 0
has_playbooks: true
has_data_sources: true
download_url: /packs/human-capital-economics.pax.tar.gz
download_size: 2.8 KB
weight: 7974
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

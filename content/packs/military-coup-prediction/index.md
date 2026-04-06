---
name: military-coup-prediction
title: Military Coup Prediction
version: 1.0.3
pax_type: topic
description: ''
author: ''
created: ''
license: ''
tags:
- topic
constructs:
- coup_attempt
- coup_success
- gdp_per_capita_coup
- economic_growth_shock
- military_spending_share
- regime_durability_coup
- ethnic_fractionalization_military
- military_autonomy
- ethnic_stacking
- parallel_security_forces
- coup_contagion
- foreign_military_aid_coup
- cold_war_era_coup
- anocracy_coup
- leader_tenure_coup
- coup_forecast_score
- coup_history
engines:
- logistic_regression
- random_forest
playbook_names:
- drc_coup_analysis
construct_count: 17
finding_count: 0
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: military_coup_prediction
  display_name: Military Coup Prediction
  description: Determinants, risk factors, and prediction of military coups d'état.
    Covers structural conditions (economic, political, institutional), civil-military
    relations, coup-proofing strategies, ethnic dimensions of military loyalty, and
    quantitative forecasting models.
  research_questions: []
  temporal_scope: 1950-present
  population: Sovereign states, country-year panel observations
  level_of_analysis: macro
constructs_detail:
- id: coup_attempt
  display_name: Coup Attempt
  definition: 'Binary indicator: an illegal and overt attempt by the military or other
    elites within the state apparatus to unseat the sitting executive. Following Powell
    & Thyne (2011), includes both successful and failed attempts. Excludes popular
    revolutions, civil wars, and foreign invasions unless led by domestic military/elite
    actors.'
  aliases: []
  construct_type: outcome
- id: coup_success
  display_name: Coup Success
  definition: 'Binary indicator: a coup attempt that successfully results in the displacement
    of the incumbent chief executive and seizure of executive power for at least 7
    days. Subset of coup_attempt. Success rate globally ~50% across 1950-2010 period.'
  aliases: []
  construct_type: outcome
- id: gdp_per_capita_coup
  display_name: GDP per Capita (Coup Risk)
  definition: Logged real GDP per capita as a structural predictor of coup risk. Lower
    income levels are robustly associated with higher coup probability — the 'coup
    trap' mechanism where poverty creates grievances and lowers opportunity costs
    of plotting. One of the most robust predictors across studies (Londregan & Poole
    1990, Gassebner et al. 2016).
  aliases: []
  construct_type: quantifiable
- id: economic_growth_shock
  display_name: Economic Growth Shock
  definition: Short-term negative deviation in GDP growth rate, typically measured
    as annual real GDP growth or growth relative to trend. Sudden economic downturns
    increase coup risk by creating popular discontent, weakening regime legitimacy,
    and reducing the regime's ability to buy military loyalty through patronage.
  aliases: []
  construct_type: quantifiable
- id: military_spending_share
  display_name: Military Spending Share
  definition: 'Military expenditure as a percentage of GDP or total government expenditure.
    Has theoretically ambiguous effects on coup risk: higher spending may buy military
    loyalty and reduce grievances, but also empowers the military as an institution
    and increases its capacity to act. Empirical evidence is mixed (Gassebner et al.
    2016).'
  aliases: []
  construct_type: quantifiable
- id: regime_durability_coup
  display_name: Regime Durability
  definition: Number of years since the last regime transition (3+ point Polity score
    change). Longer-lived regimes face lower coup risk due to institutional consolidation,
    established patronage networks, and routinized civil-military relations. New regimes
    are vulnerable during transition periods.
  aliases: []
  construct_type: quantifiable
- id: ethnic_fractionalization_military
  display_name: Military Ethnic Composition
  definition: The degree to which the ethnic composition of the military (especially
    officer corps) diverges from the general population. Ethnic homogeneity in the
    military (via ethnic stacking) may increase loyalty to the regime but creates
    grievances among excluded groups that can fuel civil war (Roessler 2011, Harkness
    2014).
  aliases: []
  construct_type: quantifiable
- id: military_autonomy
  display_name: Military Autonomy
  definition: The degree to which the armed forces operate independently from civilian
    political control. High military autonomy — separate intelligence apparatus, independent
    budget authority, professional promotion criteria, corporate identity — increases
    both the capability and motivation for military intervention in politics. Reduced
    by coup-proofing but at the cost of military effectiveness.
  aliases: []
  construct_type: concept
- id: ethnic_stacking
  display_name: Ethnic Stacking
  definition: The deliberate appointment of co-ethnics or loyalists to key command
    positions in the military and security forces. A form of coup-proofing that increases
    short-term regime security by ensuring military leaders share identity-based loyalty
    with the ruler, but creates long-term instability by generating grievances among
    excluded ethnic groups and degrading meritocratic military performance (Harkness
    2014, Roessler 2011).
  aliases: []
  construct_type: process
- id: parallel_security_forces
  display_name: Parallel Security Forces
  definition: The creation of multiple, competing armed bodies (presidential guards,
    paramilitaries, intelligence agencies with arrest powers) with overlapping jurisdictions.
    A key coup-proofing mechanism that prevents any single military unit from accumulating
    enough power to execute a coup. Reduces coup risk but fragments the security apparatus
    and degrades conventional military effectiveness.
  aliases: []
  construct_type: process
- id: coup_contagion
  display_name: Coup Contagion
  definition: 'Regional diffusion or demonstration effects whereby coups in neighboring
    or culturally similar states increase coup risk domestically. Mechanisms include:
    (1) demonstration that coups are feasible, (2) diffusion of coup-facilitating
    networks among military officers trained together, (3) regional instability creating
    permissive international environments. Operationalized as count of coups in neighboring
    states or regional coup rate.'
  aliases: []
  construct_type: quantifiable
- id: foreign_military_aid_coup
  display_name: Foreign Military Aid
  definition: 'External military assistance (arms transfers, training, financial support)
    provided to a state''s armed forces. Theoretically ambiguous effect on coup risk:
    may professionalize the military and increase civilian control, but may also empower
    the military and create dependencies that make aid withdrawal destabilizing. Cold
    War-era aid was often coup-permissive.'
  aliases: []
  construct_type: quantifiable
- id: cold_war_era_coup
  display_name: Cold War Era
  definition: Binary indicator for the Cold War period (pre-1991). Coup rates were
    substantially higher during the Cold War when superpower competition created permissive
    environments for military intervention. Post-Cold War democratic norms, international
    organizations, and conditional aid reduced the international tolerance for coups.
    Structural break in coup patterns around 1991.
  aliases: []
  construct_type: quantifiable
- id: anocracy_coup
  display_name: Anocracy (Coup Risk)
  definition: Mixed regime type (Polity score approximately -5 to +5) that combines
    elements of democracy and autocracy. Anocracies face elevated coup risk compared
    to both full democracies and consolidated autocracies — the 'inverted U' hypothesis.
    Partial liberalization creates political competition without establishing strong
    civilian control institutions.
  aliases: []
  construct_type: quantifiable
- id: leader_tenure_coup
  display_name: Leader Tenure
  definition: 'Number of years the current chief executive has been in power. Non-linear
    relationship with coup risk: new leaders face high risk during consolidation period,
    risk declines as they establish control and patronage networks, but may rise again
    in very long tenures as succession anxieties emerge and loyalty networks calcify.'
  aliases: []
  construct_type: quantifiable
- id: coup_forecast_score
  display_name: Coup Forecast Score
  definition: Model-generated probability of a coup attempt occurring in a given country-year.
    Produced by statistical or machine learning models using structural, institutional,
    and contextual predictors. Examples include PITF models, ViEWS system (Hegre et
    al. 2019), and various logistic regression/random forest approaches in the literature.
  aliases: []
  construct_type: composite
- id: coup_history
  display_name: Coup History
  definition: Count or recency of prior coup attempts in a country. The single strongest
    predictor of future coups — the 'coup trap' dynamic where initial coups lower
    the normative and practical barriers to subsequent attempts. Countries with recent
    coup histories face 3-5x higher coup risk than countries without. Operationalized
    as binary (any prior coup), count, or years since last coup.
  aliases: []
  construct_type: quantifiable
findings_detail: []
propositions_detail: []
sources_detail: []
playbooks_detail:
- id: drc_coup_analysis
  display_name: DRC Coup Analysis — Full Pipeline
  description: End-to-end pipeline capturing the data acquisition, merging, ingestion,
    and analysis workflow used to analyze coup dynamics in the Democratic Republic
    of Congo. Acquires Powell & Thyne coup events and World Bank WDI indicators, merges
    into a country-year panel, ingests into Praxis, validates, and runs bivariate
    and multivariate models. Developed during an April 2026 analytical session.
  estimated_runtime: 5-10 minutes
  step_count: 13
  engines_used:
  - logistic_regression
  - correlation_matrix
download_url: https://pax-market.com/packs/military-coup-prediction.pax.tar.gz
download_size: 6.9 KB
published_by: Praxis Agent
related_packs: []
pax_name: military-coup-prediction
weight: 10000
---

**Domain:** Military Coup Prediction

Determinants, risk factors, and prediction of military coups d'état. Covers structural conditions (economic, political, institutional), civil-military relations, coup-proofing strategies, ethnic dimensions of military loyalty, and quantitative forecasting models.

**Temporal scope:** 1950-present | **Population:** Sovereign states, country-year panel observations

---
name: pmsc-market-for-force
title: Pmsc Market For Force
version: 1.0.25
pax_type: field
description: 'The market for force: private military and security companies (PMSCs),
  their typologies, conflict consequences, regulatory frameworks, and data infrastructure.
  Covers the diversity of commercial military actors post-Cold War, their impact on
  conflict duration/intensity/peace durability, subnational and non-conflict uses,
  and emerging domains including Chinese BRI security and cyber/space privatization.
  Built on Avant, Petersohn, McFate, Dunigan, Akcinaroglu & Radziszewski.'
author: ''
created: ''
license: ''
tags:
- field
constructs:
- pmsc_presence
- pmsc_type
- pmsc_government_linkage
- pmsc_service_spectrum
- pmsc_market_competition
- conflict_intensity_pmsc
- conflict_duration_pmsc
- peace_durability_pmsc
- pmsc_accountability
- anti_mercenary_norm
- state_capacity_pmsc
- pmsc_military_effectiveness
- civilian_victimization_pmsc
- conflict_onset_pmsc
- regulatory_framework_strength
- extractive_industry_presence
- pmsc_client_type
- bri_security_provision
- pmsc_personnel_welfare
- democratic_accountability_gap
- state_monopoly_violence
- neomedievalism
- pmsc_market_structure
- security_assemblage
- security_commodification
- post_conflict_recurrence
- montreux_document
- chinese_psc_presence
engines:
- ols_regression
- logistic_regression
- cox_ph
- kaplan_meier
- propensity_score_matching
- difference_in_differences
- correlation_matrix
- kmeans_clustering
- meta_analysis
playbook_names:
- cross_domain_pmsc_nexus
- pmsc_conflict_duration_survival
- pmsc_conflict_intensity_replication
- pmsc_literature_gap_survey
- pmsc_peace_durability_analysis
- pmsc_typology_clustering
- quick_start
construct_count: 28
finding_count: 36
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: pmsc_market_for_force
  display_name: Private Military and Security Companies
  description: The study of private military and security companies (PMSCs), commercial
    military actors, and mercenaries — their organizational typologies, market structure,
    consequences for conflict dynamics, regulatory frameworks, and evolving roles
    in international security. Encompasses the privatization of security from historical
    mercenaries through modern corporate military service providers.
  research_questions: []
  temporal_scope: 1945-present, with focus on post-Cold War (1990-present)
  population: PMSCs, mercenaries, and commercial military actors involved in armed
    conflicts and security provision worldwide
  level_of_analysis: meso
constructs_detail:
- id: pmsc_presence
  display_name: PMSC Presence
  definition: Binary indicator (0/1) of whether a private military or security company
    is active in a given conflict-year. The workhorse measure in quantitative PMSC
    research, though widely acknowledged as crude — service-type disaggregation consistently
    produces more nuanced findings.
  aliases: []
  construct_type: quantifiable
- id: pmsc_type
  display_name: PMSC Organizational Type
  definition: 'Categorical classification of private military and security companies
    by organizational form and service portfolio. Singer (2003) distinguishes military
    provider firms, military consulting firms, and military support firms. McFate
    (2014) uses a 2-axis typology: government linkage (state-connected to independent)
    × service spectrum (security-only to military operations).'
  aliases: []
  construct_type: concept
- id: pmsc_government_linkage
  display_name: PMSC Government Linkage
  definition: Degree of organizational connection between a PMSC and a state government,
    ranging from fully state-owned enterprises (e.g., Chinese SOE security companies)
    through government-contracted firms to fully independent market actors. One axis
    of McFate's (2014) two-dimensional typology.
  aliases: []
  construct_type: quantifiable
- id: pmsc_service_spectrum
  display_name: PMSC Service Spectrum
  definition: Range of services offered by a PMSC, from purely defensive security
    (site protection, convoy escort) through military consulting and training to direct
    participation in combat operations. The CMAD codes 11 service categories spanning
    logistics to frontline combat. One axis of McFate's (2014) typology.
  aliases: []
  construct_type: quantifiable
- id: pmsc_market_competition
  display_name: PMSC Market Competition
  definition: Level of competition among PMSCs operating within a conflict zone or
    market segment. Akcinaroglu & Radziszewski (2013, 2020) argue competition disciplines
    PMSC behavior and improves outcomes; Faulkner, Lambert & Powell (2019) critique
    the operationalization, showing co-presence does not equal competition.
  aliases: []
  construct_type: quantifiable
- id: conflict_intensity_pmsc
  display_name: Conflict Intensity
  definition: Battle deaths per conflict-year as a measure of how violent an armed
    conflict is. Commonly operationalized using UCDP best estimates (bd_best). The
    25 battle-death threshold distinguishes minor armed conflicts from wars.
  aliases: []
  construct_type: outcome
- id: conflict_duration_pmsc
  display_name: Conflict Duration
  definition: Length of armed conflict in years from onset to termination. Key dependent
    variable in survival analysis of PMSC effects. Akcinaroglu & Radziszewski (2013)
    find competitive PMSC markets shorten conflicts; Petersohn (2024) finds early
    CMA intervention increases termination probability.
  aliases: []
  construct_type: outcome
- id: peace_durability_pmsc
  display_name: Post-Conflict Peace Durability
  definition: Duration of peace following conflict termination, measured as time until
    conflict recurrence. Underexplored in PMSC literature relative to conflict duration
    and intensity.
  aliases: []
  construct_type: outcome
- id: pmsc_accountability
  display_name: PMSC Accountability
  definition: 'The degree to which private military and security companies are subject
    to legal, political, and market-based oversight mechanisms. Avant (2005) identifies
    three accountability channels: contractual, market, and public/political. PMSCs
    exist in legal gray zones between military and civilian status.'
  aliases: []
  construct_type: concept
- id: anti_mercenary_norm
  display_name: Anti-Mercenary Norm
  definition: International normative prohibition against mercenary activity, codified
    in the 1989 UN Mercenary Convention and the OAU Convention. Petersohn (2014) argues
    PMSCs achieved legitimacy by reframing their use of force as 'individual self-defence'
    rather than combat participation, effectively circumventing the norm without directly
    violating it.
  aliases: []
  construct_type: concept
- id: state_capacity_pmsc
  display_name: State Capacity (PMSC Context)
  definition: Government institutional strength and ability to provide security through
    national armed forces. Weak states are primary demand generators for PMSC services.
    Operationalized via GDP per capita, Polity scores, or composite fragility indices.
  aliases: []
  construct_type: quantifiable
- id: pmsc_military_effectiveness
  display_name: PMSC Military Effectiveness
  definition: The degree to which PMSC deployment improves the military capability
    of the hiring party. Dunigan (2011) identifies conditions under which PSC use
    yields positive or negative tactical/strategic outcomes. Petersohn (2017) shows
    effectiveness translates to increased conflict severity.
  aliases: []
  construct_type: outcome
- id: civilian_victimization_pmsc
  display_name: Civilian Victimization by PMSCs
  definition: Violence against civilians perpetrated by or attributable to PMSC operations.
    Penel & Petersohn (2022) use CMAD to test the 'outsourcing atrocities' hypothesis
    across four world regions. Distinguished from general civilian casualties in conflict.
  aliases: []
  construct_type: outcome
- id: conflict_onset_pmsc
  display_name: Conflict Onset
  definition: Initiation of armed conflict as defined by UCDP (25+ battle deaths in
    a year). Petersohn (2021) finds PMSC presence in year t-1 is associated with subsequent
    conflict onset, suggesting PMSCs may anticipate or contribute to conflict initiation
    rather than being purely reactive.
  aliases: []
  construct_type: outcome
- id: regulatory_framework_strength
  display_name: Regulatory Framework Strength
  definition: Strength of legal and institutional oversight mechanisms governing PMSC
    activity. Key instruments include the Montreux Document (2008), the International
    Code of Conduct for Private Security Providers (ICoC, 2010), national licensing
    regimes, and the ICoCA certification system.
  aliases: []
  construct_type: concept
- id: extractive_industry_presence
  display_name: Extractive Industry Presence
  definition: Presence and scale of mining, oil, gas, or other resource extraction
    operations in a country or conflict zone. Creates demand for private security
    services to protect investments and personnel, particularly in weak-state environments.
  aliases: []
  construct_type: quantifiable
- id: pmsc_client_type
  display_name: PMSC Client Type
  definition: 'Identity of the party hiring PMSC services: government (state), rebel
    group, international organization, corporation, or private individual. Client
    type shapes accountability dynamics, service provision, and conflict outcomes.
    The CMAD codes client identity for each contract.'
  aliases: []
  construct_type: concept
- id: bri_security_provision
  display_name: BRI Security Provision
  definition: Private security services provided by Chinese state-owned enterprises
    and private security companies to protect Belt and Road Initiative investments
    and personnel abroad. Represents an emerging model where security companies may
    evolve from asset protection to security force assistance and training.
  aliases: []
  construct_type: concept
- id: pmsc_personnel_welfare
  display_name: PMSC Personnel Welfare
  definition: Health, psychological, and well-being outcomes for PMSC personnel deployed
    in conflict environments, including rates of PTSD, mental health disorders, physical
    injury, and access to care relative to military counterparts.
  aliases: []
  construct_type: outcome
- id: democratic_accountability_gap
  display_name: Democratic Accountability Gap
  definition: The erosion of democratic oversight when security functions are privatized
    — confidentiality clauses, contractor legal ambiguity, and legislative exclusion
    combine to shield PMSCs from public accountability mechanisms that apply to uniformed
    forces.
  aliases: []
  construct_type: outcome
- id: state_monopoly_violence
  display_name: State Monopoly on Violence
  definition: The Weberian principle that states hold exclusive legitimate authority
    over the use of force within their territory. McFate (2014) argues this was a
    brief historical interlude (1648-1990s), not the natural state of international
    politics. PMSC proliferation challenges this principle.
  aliases: []
  construct_type: concept
- id: neomedievalism
  display_name: Neomedieval Warfare
  definition: McFate's (2014) thesis that the post-Cold War security environment resembles
    the medieval period, with multiple overlapping authorities, privatized violence,
    and non-state armed actors coexisting with weakened states. PMSCs are a key manifestation.
  aliases: []
  construct_type: concept
- id: pmsc_market_structure
  display_name: PMSC Market Structure Type
  definition: 'Classification of PMSC market organization as collaborative, competitive,
    or rival (Petersohn 2015). Alternatively: neoliberal, hybrid, or racketeering
    market types (Dunigan & Petersohn 2015). Market structure shapes PMSC behavior
    and conflict outcomes.'
  aliases: []
  construct_type: concept
- id: security_assemblage
  display_name: Global Security Assemblage
  definition: Abrahamsen & Williams' (2009) theoretical framework describing how security
    governance operates through transnational networks blurring public/private distinctions.
    PMSCs, state forces, and local actors interact to produce emergent security governance.
  aliases: []
  construct_type: concept
- id: security_commodification
  display_name: Security Commodification
  definition: The transformation of security from a public good provided by the state
    to a commodity exchanged on markets. Leander (2005) and Krahmann (2008) argue
    this undermines democratic accountability and creates profit-over-public-interest
    incentives.
  aliases: []
  construct_type: process
- id: post_conflict_recurrence
  display_name: Post-Conflict Recurrence Risk
  definition: Probability that armed conflict resumes after termination. Bara & Kreutz
    (2022) argue PMSC presence exacerbates the credible commitment problem, making
    durable peace harder to achieve.
  aliases: []
  construct_type: outcome
- id: montreux_document
  display_name: Montreux Document Compliance
  definition: Adherence to the 2008 Montreux Document on pertinent international legal
    obligations for states related to PMSC operations during armed conflict. Signed
    by 54 states and 3 international organizations. Penel & Petersohn (2022) find
    Montreux-member governments show 72% reduced civilian victimization.
  aliases: []
  construct_type: quantifiable
- id: chinese_psc_presence
  display_name: Chinese PSC Presence Abroad
  definition: Number and scale of Chinese private security companies operating internationally,
    primarily to protect Belt and Road Initiative investments. Arduino (2020) estimates
    35,000-62,000 Chinese security contractors in 50 African countries.
  aliases: []
  construct_type: quantifiable
findings_detail:
- finding_text: 'Singer''s tip-of-the-spear typology classifies PMSCs into three tiers
    by proximity to combat: Military Provider Firms (direct combat), Military Consulting
    Firms (advisory/training), and Military Support Firms (logistics/intelligence).
    This remains the most widely-used classification scheme despite limitations.'
  construct_ids:
  - pmsc_type
  - pmsc_service_spectrum
  direction: unknown
  effect_size: null
  confidence: strong
  method_used: Qualitative typology construction, case study analysis
  effect_size_value: null
  effect_size_se: null
  effect_size_type: null
  p_value: null
  sample_size: null
  r_squared: null
  ci_lower: null
  ci_upper: null
  model_specification: null
  covariates_controlled: null
- finding_text: PMSC services increase client military effectiveness which translates
    into increased conflict severity in weak states (1990-2007). Effects depend on
    service type — combat services have stronger severity effects than support/logistics
    services.
  construct_ids:
  - pmsc_presence
  - conflict_intensity_pmsc
  - pmsc_service_spectrum
  - pmsc_military_effectiveness
  direction: positive
  effect_size: null
  confidence: strong
  method_used: Quantitative panel analysis, 30 weak states, 1990-2007, PSD data
  effect_size_value: null
  effect_size_se: null
  effect_size_type: null
  p_value: null
  sample_size: null
  r_squared: null
  ci_lower: null
  ci_upper: null
  model_specification: null
  covariates_controlled: null
- finding_text: Both mercenaries and modern PMSCs increase civil war severity across
    1946-2002. The severity-increasing effect is present across the full historical
    range, challenging claims that modern PMSCs are fundamentally different from historical
    mercenaries in their conflict impacts.
  construct_ids:
  - pmsc_presence
  - conflict_intensity_pmsc
  direction: positive
  effect_size: null
  confidence: strong
  method_used: Quantitative panel, global civil wars 1946-2002
  effect_size_value: null
  effect_size_se: null
  effect_size_type: null
  p_value: null
  sample_size: null
  r_squared: null
  ci_lower: null
  ci_upper: null
  model_specification: null
  covariates_controlled: null
- finding_text: Competition among government-hired PMCs in African civil wars (1990-2008)
    incentivizes better service delivery and faster conflict termination. Monopoly
    PMSC arrangements extend conflicts.
  construct_ids:
  - pmsc_market_competition
  - conflict_duration_pmsc
  direction: negative
  effect_size: null
  confidence: moderate
  method_used: Survival analysis, African civil wars 1990-2008
  effect_size_value: null
  effect_size_se: null
  effect_size_type: null
  p_value: null
  sample_size: null
  r_squared: null
  ci_lower: null
  ci_upper: null
  model_specification: null
  covariates_controlled: null
- finding_text: 'The Akcinaroglu-Radziszewski competition operationalization suffers
    from four aggregation problems: (1) actual competition is rare despite co-presence;
    (2) multiple firms are often subsidiaries; (3) aggregation conflates collaboration
    with competition; (4) the competition measure lacks empirical validity. Sierra
    Leone case study demonstrates these coding issues.'
  construct_ids:
  - pmsc_market_competition
  - conflict_duration_pmsc
  direction: conditional
  effect_size: null
  confidence: strong
  method_used: Case study with coding critique, Sierra Leone
  effect_size_value: null
  effect_size_se: null
  effect_size_type: null
  p_value: null
  sample_size: null
  r_squared: null
  ci_lower: null
  ci_upper: null
  model_specification: null
  covariates_controlled: null
- finding_text: Early CMA intervention (within first year of conflict) substantially
    increases probability of conflict termination using CMAD data and Cox PH models.
    No evidence that CMAs select into easier conflicts (appendix logistic regression
    test).
  construct_ids:
  - pmsc_presence
  - conflict_duration_pmsc
  direction: negative
  effect_size: null
  confidence: strong
  method_used: Cox proportional hazard models, CMAD 1990-2010
  effect_size_value: null
  effect_size_se: null
  effect_size_type: null
  p_value: null
  sample_size: null
  r_squared: null
  ci_lower: null
  ci_upper: null
  model_specification: null
  covariates_controlled: null
- finding_text: Distinguishing corporate PMSCs from mercenaries, and government clients
    from rebel clients, matters substantively for civilian victimization outcomes.
    Collapsing these categories produces misleading inferences. Montreux Document
    coding is substantively significant.
  construct_ids:
  - pmsc_type
  - pmsc_client_type
  - civilian_victimization_pmsc
  direction: conditional
  effect_size: null
  confidence: strong
  method_used: Country-year panel with 1-year lag on all IVs, CMAD, Africa/MENA/LatAm/Asia
    1980-2011
  effect_size_value: null
  effect_size_se: null
  effect_size_type: null
  p_value: null
  sample_size: null
  r_squared: null
  ci_lower: null
  ci_upper: null
  model_specification: null
  covariates_controlled: null
- finding_text: PMSC presence in year t-1 is associated with conflict onset using
    Cox PH models and PSED data across Latin America, Africa, and Southeast Asia 1990-2011.
    PMSC presence slightly increases likelihood of conflict onset.
  construct_ids:
  - pmsc_presence
  - conflict_onset_pmsc
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: Cox proportional hazard models, PSED data 1990-2011
  effect_size_value: null
  effect_size_se: null
  effect_size_type: null
  p_value: null
  sample_size: null
  r_squared: null
  ci_lower: null
  ci_upper: null
  model_specification: null
  covariates_controlled: null
- finding_text: PMSCs achieved legitimacy by reinterpreting the anti-mercenary norm
    — redefining their use of force as individual self-defence rather than combat
    participation, carving normative space distinct from historical mercenaries.
  construct_ids:
  - anti_mercenary_norm
  - pmsc_type
  direction: conditional
  effect_size: null
  confidence: strong
  method_used: Norm analysis, qualitative/interpretive
  effect_size_value: null
  effect_size_se: null
  effect_size_type: null
  p_value: null
  sample_size: null
  r_squared: null
  ci_lower: null
  ci_upper: null
  model_specification: null
  covariates_controlled: null
- finding_text: Conditions under which PMSCs escalate or dampen conflict severity
    depend on client type, oversight mechanisms, and service categories — refining
    earlier finding that PMSCs uniformly increase severity.
  construct_ids:
  - pmsc_presence
  - conflict_intensity_pmsc
  - pmsc_client_type
  - pmsc_accountability
  direction: conditional
  effect_size: null
  confidence: moderate
  method_used: PSD data, 30 weak states 1990-2007, addresses endogeneity via lagged
    battle deaths
  effect_size_value: null
  effect_size_se: null
  effect_size_type: null
  p_value: null
  sample_size: null
  r_squared: null
  ci_lower: null
  ci_upper: null
  model_specification: null
  covariates_controlled: null
- finding_text: The PMSC industry grew from an estimated $55.6 billion in 1990 to
    over $100 billion by 2003, driven by post-Cold War military downsizing that created
    both supply (demobilized soldiers seeking employment) and demand (weak states,
    peacekeeping shortfalls, and new security threats).
  construct_ids:
  - pmsc_industry_size
  - pmsc_presence
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: Industry analysis, market size estimation
  effect_size_value: null
  effect_size_se: null
  effect_size_type: null
  p_value: null
  sample_size: null
  r_squared: null
  ci_lower: null
  ci_upper: null
  model_specification: null
  covariates_controlled: null
- finding_text: PMSCs represent not an anomaly but a historical norm. The state monopoly
    on violence was a brief 150-year interlude (roughly 1648-1990s). The current era
    of privatized violence represents a return to the pre-Westphalian norm of multiple
    competing armed actors.
  construct_ids:
  - state_monopoly_violence
  - neomedievalism
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: Historical analysis, neomedievalist theoretical framework
  effect_size_value: null
  effect_size_se: null
  effect_size_type: null
  p_value: null
  sample_size: null
  r_squared: null
  ci_lower: null
  ci_upper: null
  model_specification: null
  covariates_controlled: null
- finding_text: McFate's two-axis typology (government linkage × service spectrum)
    reveals that PMSC organizational forms are far more diverse than the simple mercenary/contractor
    binary suggests. Organizations range from state-owned enterprises to fully independent
    market actors, and from defensive security to offensive combat operations.
  construct_ids:
  - pmsc_type
  - pmsc_government_linkage
  - pmsc_service_spectrum
  direction: unknown
  effect_size: null
  confidence: strong
  method_used: Typological theory, practitioner analysis
  effect_size_value: null
  effect_size_se: null
  effect_size_type: null
  p_value: null
  sample_size: null
  r_squared: null
  ci_lower: null
  ci_upper: null
  model_specification: null
  covariates_controlled: null
- finding_text: Different institutional arrangements for overseeing private force
    — contract type, oversight mechanisms, market competition — produce systematically
    different accountability outcomes. Market structure shapes whether PMSCs face
    contractual, market-based, or political accountability.
  construct_ids:
  - pmsc_accountability
  - pmsc_market_structure
  direction: conditional
  effect_size: null
  confidence: strong
  method_used: Comparative institutional analysis, case studies
  effect_size_value: null
  effect_size_se: null
  effect_size_type: null
  p_value: null
  sample_size: null
  r_squared: null
  ci_lower: null
  ci_upper: null
  model_specification: null
  covariates_controlled: null
- finding_text: 'Avant identifies three functional arenas of private force: external
    security (military operations), internal security (policing, border control),
    and commercial security (corporate protection). Each arena has distinct accountability
    dynamics and regulatory challenges.'
  construct_ids:
  - pmsc_type
  - pmsc_service_spectrum
  direction: unknown
  effect_size: null
  confidence: strong
  method_used: Theoretical framework construction
  effect_size_value: null
  effect_size_se: null
  effect_size_type: null
  p_value: null
  sample_size: null
  r_squared: null
  ci_lower: null
  ci_upper: null
  model_specification: null
  covariates_controlled: null
- finding_text: CMAD covers all civil wars 1980-2016 globally except Europe, recording
    approximately 6,971 contractual relationships. It codes 11 service categories
    and explicitly distinguishes corporate PMSCs from mercenary outfits — a critical
    distinction that prior datasets (PSED, PSD) collapsed.
  construct_ids:
  - pmsc_type
  - pmsc_service_spectrum
  direction: unknown
  effect_size: null
  confidence: strong
  method_used: Dataset construction, systematic coding of open-source materials
  effect_size_value: null
  effect_size_se: null
  effect_size_type: null
  p_value: null
  sample_size: null
  r_squared: null
  ci_lower: null
  ci_upper: null
  model_specification: null
  covariates_controlled: null
- finding_text: Personal networks and relationship-based trust, not anonymous price-and-quality
    competition, drive PMSC procurement patterns. The market for force operates through
    three structures — collaborative, competitive, and rival — each producing different
    performance outcomes.
  construct_ids:
  - pmsc_market_structure
  - pmsc_market_competition
  direction: conditional
  effect_size: null
  confidence: moderate
  method_used: Social network analysis, market structure theory
  effect_size_value: null
  effect_size_se: null
  effect_size_type: null
  p_value: null
  sample_size: null
  r_squared: null
  ci_lower: null
  ci_upper: null
  model_specification: null
  covariates_controlled: null
- finding_text: Comparative analysis across 12 countries reveals the global market
    for force is not monolithic but a conglomeration of neoliberal, hybrid, and racketeering
    market types that vary by local political conditions and geostrategic context.
  construct_ids:
  - pmsc_market_structure
  - pmsc_type
  direction: conditional
  effect_size: null
  confidence: strong
  method_used: Comparative case studies across 12 countries
  effect_size_value: null
  effect_size_se: null
  effect_size_type: null
  p_value: null
  sample_size: null
  r_squared: null
  ci_lower: null
  ci_upper: null
  model_specification: null
  covariates_controlled: null
- finding_text: The historical transition from mercenary to citizen armies was driven
    by domestic political conditions and military defeats, not purely by state-building
    ideology. Path dependency played a key role, challenging both realist and constructivist
    accounts.
  construct_ids:
  - state_monopoly_violence
  direction: conditional
  effect_size: null
  confidence: strong
  method_used: Historical comparative analysis
  effect_size_value: null
  effect_size_se: null
  effect_size_type: null
  p_value: null
  sample_size: null
  r_squared: null
  ci_lower: null
  ci_upper: null
  model_specification: null
  covariates_controlled: null
- finding_text: A robust international social norm against mercenary use has persisted
    for centuries, but has never produced effective legal prohibition. The 1989 UN
    Mercenary Convention has been ratified by only 35 states and excludes all major
    PMSC-employing nations.
  construct_ids:
  - anti_mercenary_norm
  - regulatory_framework_strength
  direction: negative
  effect_size: null
  confidence: strong
  method_used: Historical norm tracing, international law analysis
  effect_size_value: null
  effect_size_se: null
  effect_size_type: null
  p_value: null
  sample_size: null
  r_squared: null
  ci_lower: null
  ci_upper: null
  model_specification: null
  covariates_controlled: null
- finding_text: 'The anti-mercenary norm has two components: illegitimacy of force
    outside authorized control, and moral problems with fighting for purely financial
    motives. PMSCs exploit the definitional ambiguity between these components to
    claim legitimacy.'
  construct_ids:
  - anti_mercenary_norm
  - pmsc_accountability
  direction: conditional
  effect_size: null
  confidence: strong
  method_used: Norm theory analysis
  effect_size_value: null
  effect_size_se: null
  effect_size_type: null
  p_value: null
  sample_size: null
  r_squared: null
  ci_lower: null
  ci_upper: null
  model_specification: null
  covariates_controlled: null
- finding_text: PMCs exercise symbolic power (Bourdieu) by shaping shared understandings
    of what counts as security and who constitutes a legitimate security actor. This
    power has shifted from the public/state sphere to the private/market sphere.
  construct_ids:
  - pmsc_symbolic_power
  - security_commodification
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: Bourdieu-inflected discourse analysis
  effect_size_value: null
  effect_size_se: null
  effect_size_type: null
  p_value: null
  sample_size: null
  r_squared: null
  ci_lower: null
  ci_upper: null
  model_specification: null
  covariates_controlled: null
- finding_text: The market for force undermines the public-goods character of security
    by commodifying it. Commodification erodes democratic accountability and creates
    incentive structures that prioritize profit over public interest.
  construct_ids:
  - security_commodification
  - democratic_accountability_gap
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: Critical security analysis
  effect_size_value: null
  effect_size_se: null
  effect_size_type: null
  p_value: null
  sample_size: null
  r_squared: null
  ci_lower: null
  ci_upper: null
  model_specification: null
  covariates_controlled: null
- finding_text: The Wagner Group does not fit existing PMC typology categories. It
    operates through corrupt informal networks linked to the Russian state, combining
    military operations with influence campaigns across 6+ countries (Nigeria, Crimea,
    Ukraine, Syria, Sudan, CAR). While operationally similar to PMCs, the informal
    state-PMC nexus serves purposes that potentially undermine Russian security interests.
  construct_ids:
  - wagner_group_model
  - pmsc_type
  - pmsc_government_linkage
  direction: conditional
  effect_size: null
  confidence: strong
  method_used: Process tracing, case study analysis across 6 countries
  effect_size_value: null
  effect_size_se: null
  effect_size_type: null
  p_value: null
  sample_size: null
  r_squared: null
  ci_lower: null
  ci_upper: null
  model_specification: null
  covariates_controlled: null
- finding_text: Civil conflicts featuring PMSCs in combat roles are more likely to
    recur post-war. PMSC presence exacerbates the post-war credible commitment problem
    — belligerents fear redeployment of hired forces, making durable peace harder
    to achieve.
  construct_ids:
  - pmsc_presence
  - post_conflict_recurrence
  - peace_durability_pmsc
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: Duration analysis, PSED and UCDP data 1990-2014
  effect_size_value: null
  effect_size_se: null
  effect_size_type: null
  p_value: null
  sample_size: null
  r_squared: null
  ci_lower: null
  ci_upper: null
  model_specification: null
  covariates_controlled: null
- finding_text: The Montreux Document (2008) resulted from three years of negotiations
    and establishes 27 statements on state obligations under IHL and human rights
    law applicable to PMSC operations. It represents the first international consensus
    framework for PMSC regulation.
  construct_ids:
  - montreux_document
  - regulatory_framework_strength
  direction: positive
  effect_size: null
  confidence: strong
  method_used: Legal analysis, participant observation of negotiations
  effect_size_value: null
  effect_size_se: null
  effect_size_type: null
  p_value: null
  sample_size: null
  r_squared: null
  ci_lower: null
  ci_upper: null
  model_specification: null
  covariates_controlled: null
- finding_text: The US is leading a norm shift, not just exploiting a loophole — extensive
    PMSC use is changing the normative environment in ways that allow other states
    to follow. The state monopoly on violence norm is being transformed, not just
    circumvented.
  construct_ids:
  - state_monopoly_violence
  - anti_mercenary_norm
  direction: negative
  effect_size: null
  confidence: moderate
  method_used: Norm change analysis, US policy analysis
  effect_size_value: null
  effect_size_se: null
  effect_size_type: null
  p_value: null
  sample_size: null
  r_squared: null
  ci_lower: null
  ci_upper: null
  model_specification: null
  covariates_controlled: null
- finding_text: Iraq demonstrates how contractor legal status falls between military
    and civilian categories, creating accountability voids. The Blackwater killings
    in Fallujah and Abu Ghraib involvement illustrate how heavy reliance on PMSCs
    creates both political and legal complications.
  construct_ids:
  - democratic_accountability_gap
  - pmsc_accountability
  direction: positive
  effect_size: null
  confidence: strong
  method_used: Case study analysis, Iraq 2003-2006
  effect_size_value: null
  effect_size_se: null
  effect_size_type: null
  p_value: null
  sample_size: null
  r_squared: null
  ci_lower: null
  ci_upper: null
  model_specification: null
  covariates_controlled: null
- finding_text: Reliance on private security contractors in Iraq undermined democratic
    accountability mechanisms. Confidentiality clauses and contractor legal status
    shielded PMSCs from both legislative and public oversight.
  construct_ids:
  - democratic_accountability_gap
  - pmsc_accountability
  direction: positive
  effect_size: null
  confidence: strong
  method_used: Democratic theory analysis, Iraq case study
  effect_size_value: null
  effect_size_se: null
  effect_size_type: null
  p_value: null
  sample_size: null
  r_squared: null
  ci_lower: null
  ci_upper: null
  model_specification: null
  covariates_controlled: null
- finding_text: Security governance operates through transnational networks — 'global
    security assemblages' — that blur public/private distinctions. Case studies from
    Sierra Leone and Nigeria show how PMSCs interact with state and non-state actors
    to produce emergent security governance institutions.
  construct_ids:
  - security_assemblage
  - pmsc_type
  direction: conditional
  effect_size: null
  confidence: strong
  method_used: Assemblage theory, comparative case studies (Sierra Leone, Nigeria)
  effect_size_value: null
  effect_size_se: null
  effect_size_type: null
  p_value: null
  sample_size: null
  r_squared: null
  ci_lower: null
  ci_upper: null
  model_specification: null
  covariates_controlled: null
- finding_text: 'Systematic survey of US military personnel with Iraq experience reveals
    mixed perceptions: PSCs are viewed as useful for gap-filling and specialized tasks
    but problematic for command integration and coordination with military units.'
  construct_ids:
  - pmsc_military_effectiveness
  - pmsc_presence
  direction: conditional
  effect_size: null
  confidence: moderate
  method_used: Survey research, US military and State Department personnel
  effect_size_value: null
  effect_size_se: null
  effect_size_type: null
  p_value: null
  sample_size: null
  r_squared: null
  ci_lower: null
  ci_upper: null
  model_specification: null
  covariates_controlled: null
- finding_text: PSC deployment yields positive tactical outcomes when integrated into
    clear command structures. PSC deployment yields negative outcomes when chains
    of command are unclear or when PSCs operate autonomously. Military effectiveness
    of PSCs is conditional on organizational integration.
  construct_ids:
  - pmsc_military_effectiveness
  - pmsc_accountability
  direction: conditional
  effect_size: null
  confidence: strong
  method_used: Comparative case studies of PSC deployments
  effect_size_value: null
  effect_size_se: null
  effect_size_type: null
  p_value: null
  sample_size: null
  r_squared: null
  ci_lower: null
  ci_upper: null
  model_specification: null
  covariates_controlled: null
- finding_text: At least 20 Chinese private security companies provide international
    services to protect Belt and Road Initiative investments in Pakistan, Sudan, Iraq,
    and other countries. Chinese domestic law does not apply overseas, creating a
    legal grey zone for these operations.
  construct_ids:
  - chinese_psc_presence
  - bri_security_provision
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: Policy analysis, company mapping
  effect_size_value: null
  effect_size_se: null
  effect_size_type: null
  p_value: null
  sample_size: null
  r_squared: null
  ci_lower: null
  ci_upper: null
  model_specification: null
  covariates_controlled: null
- finding_text: An estimated 35,000-62,000 Chinese private security contractors operate
    across 50 African countries to protect BRI-linked investments. Major companies
    include Beijing DeWe, Huaxin Zhong An, Overseas Security Guardians, and China
    Security Technology Group.
  construct_ids:
  - chinese_psc_presence
  - bri_security_provision
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: Empirical mapping, interview-based research
  effect_size_value: null
  effect_size_se: null
  effect_size_type: null
  p_value: null
  sample_size: null
  r_squared: null
  ci_lower: null
  ci_upper: null
  model_specification: null
  covariates_controlled: null
- finding_text: Executive Outcomes' operations in Angola (1993-94) and Sierra Leone
    (1995-96) with approximately 2,000 ex-SADF veterans achieved rapid tactical success.
    Qualified positive assessment of EO's stabilizing role, while identifying significant
    accountability gaps in the absence of regulatory oversight.
  construct_ids:
  - pmsc_military_effectiveness
  - pmsc_accountability
  - pmsc_presence
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: Case study analysis, Angola and Sierra Leone
  effect_size_value: null
  effect_size_se: null
  effect_size_type: null
  p_value: null
  sample_size: null
  r_squared: null
  ci_lower: null
  ci_upper: null
  model_specification: null
  covariates_controlled: null
- finding_text: Since 2013, combat services have been increasingly exchanged on the
    market despite the anti-mercenary norm. This reflects rational calculations by
    actors rather than norm collapse — compliance or violation of the norm reflects
    strategic interaction between states, PMSCs, and international audiences.
  construct_ids:
  - anti_mercenary_norm
  - pmsc_service_spectrum
  direction: negative
  effect_size: null
  confidence: strong
  method_used: Norm analysis, post-2013 market trends
  effect_size_value: null
  effect_size_se: null
  effect_size_type: null
  p_value: null
  sample_size: null
  r_squared: null
  ci_lower: null
  ci_upper: null
  model_specification: null
  covariates_controlled: null
propositions_detail: []
sources_detail:
- id: avant_2005_market_for_force
  title: 'The Market for Force: The Consequences of Privatizing Security'
  authors: Deborah D. Avant
  year: 2005
  doi: 10.1017/cbo9780511490866
  source_type: book
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: mcfate_2014_modern_mercenary
  title: 'The Modern Mercenary: Private Armies and What They Mean for World Order'
  authors: Sean McFate
  year: 2014
  doi: null
  source_type: book
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: singer_2003_corporate_warriors
  title: 'Corporate Warriors: The Rise of the Privatized Military Industry'
  authors: P. W. Singer
  year: 2003
  doi: null
  source_type: book
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: dunigan_2011_victory_for_hire
  title: 'Victory for Hire: Private Security Companies'' Impact on Military Effectiveness'
  authors: Molly Dunigan
  year: 2011
  doi: 10.1515/9780804777414
  source_type: book
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: akcinaroglu_radziszewski_2020_private_militaries
  title: 'Private Militaries and the Security Industry in Civil Wars: Competition
    and Market Accountability'
  authors: Seden Akcinaroglu, Elizabeth Radziszewski
  year: 2020
  doi: 10.1093/oso/9780197520802.001.0001
  source_type: book
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: petersohn_2022_cmad
  title: The Commercial Military Actor Database
  authors: Ulrich Petersohn, Vanessa Gottwick, Charlotte Penel, Leila Kellgren-Parker
  year: 2022
  doi: 10.1177/00220027211072528
  source_type: academic_paper
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: avant_neu_2019_psed
  title: The Private Security Events Database
  authors: Deborah Avant, Kara Kingma Neu
  year: 2019
  doi: 10.1177/0022002718824394
  source_type: academic_paper
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: petersohn_2017_effectiveness_severity
  title: Private Military and Security Companies (PMSCs), Military Effectiveness,
    and Conflict Severity in Weak States, 1990-2007
  authors: Ulrich Petersohn
  year: 2017
  doi: 10.1177/0022002715600758
  source_type: academic_paper
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: petersohn_2014_mercenaries_severity
  title: The Impact of Mercenaries and Private Military and Security Companies on
    Civil War Severity between 1946 and 2002
  authors: Ulrich Petersohn
  year: 2014
  doi: 10.1080/03050629.2014.880699
  source_type: academic_paper
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: akcinaroglu_radziszewski_2013_africa
  title: Private Military Companies, Opportunities, and Termination of Civil Wars
    in Africa
  authors: Seden Akcinaroglu, Elizabeth Radziszewski
  year: 2013
  doi: 10.1177/0022002712449325
  source_type: academic_paper
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: petersohn_2024_termination
  title: The Impact of Commercial Military Actors on Armed Conflict Termination, 1990-2010
  authors: Ulrich Petersohn
  year: 2024
  doi: 10.1093/jogss/ogae016
  source_type: academic_paper
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: penel_petersohn_2022_civilian
  title: Commercial Military Actors and Civilian Victimization in Africa, Middle East,
    Latin America, and Asia, 1980-2011
  authors: Charlotte Penel, Ulrich Petersohn
  year: 2022
  doi: 10.1093/jogss/ogab029
  source_type: academic_paper
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: faulkner_lambert_powell_2019
  title: 'Reassessing PMSC Competition in Civil War: Lessons from Sierra Leone'
  authors: Christopher Faulkner, Josh Lambert, Jonathan Powell
  year: 2019
  doi: 10.1080/09592318.2019.1601869
  source_type: academic_paper
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: dunigan_petersohn_2015_markets
  title: 'The Markets for Force: Privatization of Security Across World Regions'
  authors: Molly Dunigan, Ulrich Petersohn (eds.)
  year: 2015
  doi: 10.9783/9780812291438
  source_type: book
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: petersohn_2014_anti_mercenary_norm
  title: 'Reframing the Anti-Mercenary Norm: Private Military and Security Companies
    and Mercenarism'
  authors: Ulrich Petersohn
  year: 2014
  doi: 10.1177/0020702014544915
  source_type: academic_paper
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: petersohn_2021_combat_market
  title: The Anti-Mercenary Norm and the Market for Combat Force
  authors: Ulrich Petersohn
  year: 2021
  doi: 10.1177/0020702021994519
  source_type: academic_paper
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: petersohn_lees_2023_escalate
  title: To Escalate, or Not to Escalate? Private Military and Security Companies
    and Conflict Severity
  authors: Ulrich Petersohn, N. Lees
  year: 2023
  doi: 10.1080/1057610X.2021.1935700
  source_type: academic_paper
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: petersohn_2021_onset
  title: Onset of New Business? Private Military and Security Companies and Conflict
    Onset
  authors: Ulrich Petersohn
  year: 2021
  doi: 10.1080/09592318.2020.1866404
  source_type: academic_paper
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: avant_2016_pragmatic_networks
  title: Pragmatic Networks and Transnational Governance of Private Military and Security
    Services
  authors: Deborah Avant
  year: 2016
  doi: 10.1093/isq/sqv018
  source_type: academic_paper
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: petersohn_2015_social_structure
  title: The Social Structure of the Market for Force
  authors: Ulrich Petersohn
  year: 2015
  doi: 10.1177/0010836714545686
  source_type: academic_paper
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: avant_2006_iraq
  title: 'Privatization of Security: Lessons from Iraq'
  authors: Deborah Avant
  year: 2006
  doi: 10.1016/j.orbis.2006.01.009
  source_type: journal_article
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: avant_sigelman_2010_democracy
  title: 'Private Security and Democracy: Lessons from the US in Iraq'
  authors: Deborah Avant; Lee Sigelman
  year: 2010
  doi: 10.1080/09636412.2010.480906
  source_type: journal_article
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: avant_2007_emerging_market
  title: The Emerging Market for Private Military Services and the Problems of Regulation
  authors: Deborah Avant
  year: 2007
  doi: 10.1093/acprof:oso/9780199228485.003.0011
  source_type: book_chapter
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: petersohn_2020_disorder
  title: Everything in (Dis)order? PMSCs, International Order, and Violence
  authors: Ulrich Petersohn
  year: 2020
  doi: null
  source_type: journal_article
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: petersohn_2011_privatisation
  title: Military Privatisation and the Changing Civil-Military Force Mix
  authors: Ulrich Petersohn
  year: 2011
  doi: 10.1057/eps.2011.3
  source_type: journal_article
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: icoca_2010_code
  title: International Code of Conduct for Private Security Service Providers
  authors: ICoCA Multi-stakeholder Initiative
  year: 2010
  doi: null
  source_type: manual
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: spearin_2011_peacekeeping
  title: UN Peacekeeping and Private Military and Security Companies
  authors: Christopher Spearin
  year: 2011
  doi: 10.1080/13533312.2010.546099
  source_type: journal_article
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: spearin_2001_humanitarians
  title: 'Private Security Companies and Humanitarians: A Corporate Solution to Kidnappers
    and Carjackers?'
  authors: Christopher Spearin
  year: 2001
  doi: 10.1080/13533310108413877
  source_type: journal_article
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: leander_2005_power
  title: 'The Power to Construct International Security: On the Significance of Private
    Military Companies'
  authors: Anna Leander
  year: 2005
  doi: 10.1177/03058298050330030601
  source_type: journal_article
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: leander_2005_market_destabilizing
  title: 'The Market for Force and Public Security: The Destabilizing Consequences
    of Private Military Companies'
  authors: Anna Leander
  year: 2005
  doi: 10.1177/0022343305056237
  source_type: journal_article
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: cotton_petersohn_dunigan_2010_hired_guns
  title: 'Hired Guns: Views About Armed Contractors in Operation Iraqi Freedom'
  authors: Sarah K. Cotton, Ulrich Petersohn, Molly Dunigan, Q. Burkhart, Megan Zander-Cotugno,
    Edward O'Connell, Michael Webber
  year: 2010
  doi: null
  source_type: report
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: dunigan_2014_out_of_shadows
  title: 'Out of the Shadows: The Health and Well-Being of Private Contractors Working
    in Conflict Environments'
  authors: Molly Dunigan
  year: 2014
  doi: null
  source_type: report
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: avant_2000_mercenary_to_citizen
  title: 'From Mercenary to Citizen Armies: Explaining Change in the Practice of War'
  authors: Avant, Deborah
  year: 2000
  doi: 10.1162/002081800551118
  source_type: journal_article
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: petersohn_2018_force_of_relationships
  title: 'The Force of Relationships: Personal Networks in PMSC Procurement'
  authors: Petersohn, Ulrich
  year: 2018
  doi: 10.1080/09662839.2018.1425296
  source_type: journal_article
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: petersohn_2010_sovereignty_privatization
  title: 'Sovereignty and Privatizing the Military: An Institutional Explanation'
  authors: Petersohn, Ulrich
  year: 2010
  doi: 10.1080/13523260.2010.521706
  source_type: journal_article
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: marten_2019_wagner
  title: 'Russia''s Use of Semi-State Security Forces: The Case of the Wagner Group'
  authors: Kimberly Marten
  year: 2019
  doi: 10.1080/1060586X.2019.1591142
  source_type: journal_article
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: pokalova_2023_wagner_africa
  title: 'The Wagner Group in Africa: Russia''s Quasi-State Agent of Influence'
  authors: Elena Pokalova
  year: 2023
  doi: 10.1080/1057610X.2023.2231642
  source_type: journal_article
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: bures_cusumano_2021_hypocrisy
  title: 'The Anti-Mercenary Norm and United Nations'' Use of Private Military and
    Security Companies: From Norm Entrepreneurship to Organized Hypocrisy'
  authors: Oldřich Bureš; Eugenio Cusumano
  year: 2021
  doi: 10.1080/13533312.2020.1869542
  source_type: journal_article
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: ghiselli_2020_chinese_psc_abroad
  title: 'Market Opportunities and Political Responsibilities: The Difficult Development
    of Chinese Private Security Companies Abroad'
  authors: Andrea Ghiselli
  year: 2020
  doi: 10.1177/0095327X18806517
  source_type: journal_article
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: yuan_2021_chinese_psc_interests
  title: China's Private Security Companies and the Protection of Chinese Economic
    Interests Abroad
  authors: Jingdong Yuan
  year: 2021
  doi: 10.1080/09592318.2021.1940646
  source_type: journal_article
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: ghiselli_2023_chinese_psc_coercion
  title: Chinese Private Security Companies and the Limit of Coercion
  authors: Andrea Ghiselli
  year: 2023
  doi: 10.1080/09592318.2023.2256645
  source_type: journal_article
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: avant_2000_mercenary_citizen
  title: 'From Mercenary to Citizen Armies: Explaining Change in the Practice of War'
  authors: Deborah Avant
  year: 2000
  doi: 10.1162/002081800551118
  source_type: academic_paper
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: percy_2007_mercenaries_norm
  title: 'Mercenaries: The History of a Norm in International Relations'
  authors: Sarah Percy
  year: 2007
  doi: 10.1093/acprof:oso/9780199214334.001.0001
  source_type: book
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: abrahamsen_williams_2009_assemblages
  title: 'Security Beyond the State: Global Security Assemblages in International
    Politics'
  authors: Rita Abrahamsen, Michael C. Williams
  year: 2009
  doi: 10.1111/j.1749-5687.2008.00060.x
  source_type: academic_paper
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: leander_2005_destabilizing
  title: 'The Market for Force and Public Security: The Destabilizing Consequences
    of Private Military Companies'
  authors: Anna Leander
  year: 2005
  doi: 10.1177/0022343305056237
  source_type: academic_paper
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: bara_kreutz_2022_peace
  title: To Buy a War but Sell the Peace? Mercenaries and Post-Civil War Stability
  authors: Corinne Bara, Joakim Kreutz
  year: 2022
  doi: 10.1080/09636412.2022.2097890
  source_type: academic_paper
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: cockayne_2008_montreux
  title: 'Regulating Private Military and Security Companies: An Update on Legal Trends
    and Developments'
  authors: James Cockayne
  year: 2008
  doi: 10.1093/jcsl/krp006
  source_type: academic_paper
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: krahmann_2013_state_monopoly
  title: 'The United States, PMSCs and the State Monopoly on Violence: Leading the
    Way towards Norm Change'
  authors: Elke Krahmann
  year: 2013
  doi: 10.1177/0967010612470292
  source_type: academic_paper
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: cotton_petersohn_dunigan_2010
  title: 'Hired Guns: Views About Armed Contractors in Operation Iraqi Freedom'
  authors: Sarah K. Cotton, Ulrich Petersohn, Molly Dunigan, Q. Burkhart, Megan Zander-Cotugno,
    Edward O'Connell, Michael Webber
  year: 2010
  doi: null
  source_type: report
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: legarda_nouwens_2018_bri
  title: 'Guardians of the Belt and Road: The Internationalization of China''s Private
    Security Companies'
  authors: Helena Legarda, Meia Nouwens
  year: 2018
  doi: null
  source_type: report
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: arduino_2020_chinese_psc_africa
  title: The Footprint of Chinese Private Security Companies in Africa
  authors: Alessandro Arduino
  year: 2020
  doi: null
  source_type: working_paper
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: howe_1998_executive_outcomes
  title: 'Private Security Forces and African Stability: The Case of Executive Outcomes'
  authors: Herbert M. Howe
  year: 1998
  doi: 10.1017/s0022278x98002778
  source_type: academic_paper
  journal: null
  url: null
  abstract: null
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
playbooks_detail:
- id: cross_domain_pmsc_nexus
  display_name: Cross Domain Pmsc Nexus
  description: How do PMSC findings connect to the broader conflict literature? Uses
    cross-domain bridges to trace analytical pathways from PMSCs through rebel sponsorship,
    external support, and coup-proofing.
  estimated_runtime: ''
  step_count: 2
  engines_used: []
- id: pmsc_conflict_duration_survival
  display_name: Pmsc Conflict Duration Survival
  description: 'Does PMSC involvement extend or shorten conflicts? Tests competing
    hypotheses: Akcinaroglu & Radziszewski (2013) competition-shortens vs. Petersohn
    (2024) early-intervention-shortens vs. Faulkner, Lambert & Powell (2019) competition-coding-critique.'
  estimated_runtime: ''
  step_count: 4
  engines_used: []
- id: pmsc_conflict_intensity_replication
  display_name: Pmsc Conflict Intensity Replication
  description: 'Replicate the core question: does PMSC presence increase conflict
    intensity? Tests Petersohn (2017) and Petersohn (2014) findings using UCDP battle
    deaths as DV and PMSC presence (from PSED or CMAD) as IV, with controls for state
    capacity, conflict type, and external support.'
  estimated_runtime: ''
  step_count: 5
  engines_used: []
- id: pmsc_literature_gap_survey
  display_name: Pmsc Literature Gap Survey
  description: Systematic identification of gaps in the PMSC research landscape. Uses
    Praxis coverage, maturity, and consensus tools to map what is well-established,
    what is contested, and what remains unexplored.
  estimated_runtime: ''
  step_count: 3
  engines_used: []
- id: pmsc_peace_durability_analysis
  display_name: Pmsc Peace Durability Analysis
  description: Do PMSCs affect post-conflict peace? Tests Bara & Kreutz (2022) credible
    commitment hypothesis using survival analysis of peace duration.
  estimated_runtime: ''
  step_count: 2
  engines_used: []
- id: pmsc_typology_clustering
  display_name: Pmsc Typology Clustering
  description: Build an empirical typology from CMAD data using unsupervised learning.
    Test whether McFate's 2-axis and Singer's 3-tier typologies emerge from the data,
    or whether a different classification is more appropriate.
  estimated_runtime: ''
  step_count: 3
  engines_used: []
- id: quick_start
  display_name: Quick Start — Pmsc Market For Force
  description: Basic analysis workflow for the pmsc_market_for_force domain.
  estimated_runtime: 1–3 minutes
  step_count: 2
  engines_used:
  - logistic_regression
  - correlation_matrix
relationships_detail: []
quality: {}
pax_schema_version: '1.0'
download_url: https://pax-market.com/pax/pmsc-market-for-force.pax.tar.gz
download_size: 20.6 KB
published_by: Praxis Agent
related_packs: []
pax_name: pmsc-market-for-force
weight: 10000
---

**Domain:** Private Military and Security Companies

The study of private military and security companies (PMSCs), commercial military actors, and mercenaries — their organizational typologies, market structure, consequences for conflict dynamics, regulatory frameworks, and evolving roles in international security. Encompasses the privatization of security from historical mercenaries through modern corporate military service providers.

**Temporal scope:** 1945-present, with focus on post-Cold War (1990-present) | **Population:** PMSCs, mercenaries, and commercial military actors involved in armed conflicts and security provision worldwide

## Key Findings

- Singer's tip-of-the-spear typology classifies PMSCs into three tiers by proximity to combat: Military Provider Firms (direct combat), Military Consulting Firms (advisory/training), and Military Support Firms (logistics/intelligence). This remains the most widely-used classification scheme despite limitations. *(unknown, strong)*
- PMSC services increase client military effectiveness which translates into increased conflict severity in weak states (1990-2007). Effects depend on service type — combat services have stronger severity effects than support/logistics services. *(positive, strong)*
- Both mercenaries and modern PMSCs increase civil war severity across 1946-2002. The severity-increasing effect is present across the full historical range, challenging claims that modern PMSCs are fundamentally different from historical mercenaries in their conflict impacts. *(positive, strong)*
- Competition among government-hired PMCs in African civil wars (1990-2008) incentivizes better service delivery and faster conflict termination. Monopoly PMSC arrangements extend conflicts. *(negative, moderate)*
- The Akcinaroglu-Radziszewski competition operationalization suffers from four aggregation problems: (1) actual competition is rare despite co-presence; (2) multiple firms are often subsidiaries; (3) aggregation conflates collaboration with competition; (4) the competition measure lacks empirical validity. Sierra Leone case study demonstrates these coding issues. *(conditional, strong)*
- Early CMA intervention (within first year of conflict) substantially increases probability of conflict termination using CMAD data and Cox PH models. No evidence that CMAs select into easier conflicts (appendix logistic regression test). *(negative, strong)*
- Distinguishing corporate PMSCs from mercenaries, and government clients from rebel clients, matters substantively for civilian victimization outcomes. Collapsing these categories produces misleading inferences. Montreux Document coding is substantively significant. *(conditional, strong)*
- PMSC presence in year t-1 is associated with conflict onset using Cox PH models and PSED data across Latin America, Africa, and Southeast Asia 1990-2011. PMSC presence slightly increases likelihood of conflict onset. *(positive, moderate)*

*...and 28 more findings*

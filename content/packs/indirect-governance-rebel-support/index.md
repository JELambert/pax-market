---
name: indirect-governance-rebel-support
title: Indirect Governance Rebel Support
version: 1.0.0
pax_type: paper
description: 'Explains state sponsors'' choice between ''hands-on'' delegation and
  ''hands-off'' orchestration in indirect wars. Develops a governor''s dilemma theory
  of rebel support modes and tests it with UCDP External Support Dataset 1975-2009.
  Key finding: ethnic ties and rebel competition favor orchestration; rivalry favors
  delegation; and counterintuitively, sponsor capabilities increase orchestration
  likelihood.'
author: ''
created: ''
license: ''
tags:
- paper
constructs:
- orchestration-mode
- delegation-mode
- ethnic-ties-sponsor-rebel
- rebel-group-competition
- sponsor-military-capabilities
- plausible-deniability
- governors-dilemma
engines:
- frequency_tabulation_by_support_type_and_recipient_type
- cubic_time_polynomial_analysis_within_tscs_logit_framework
- time_series_frequency_analysis
- tscs_logit_with_cubic_time_polynomials
- theoretical_derivation_from_pa_framework_vs_tscs_logit_on_ucdp_support_dyad_data
playbook_names:
- quick_start
construct_count: 7
finding_count: 0
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: indirect-warfare-modes
  display_name: Modes of Indirect Warfare
  description: The study of how state sponsors choose between delegation (hands-on
    hierarchical control) and orchestration (hands-off material support) when supporting
    rebel groups in civil conflicts. Unit of analysis is the state-rebel support dyad.
  research_questions: []
  temporal_scope: 1975-2009
  population: State-rebel support dyads in civil conflicts, 1975-2009
  level_of_analysis: meso
constructs_detail:
- id: orchestration-mode
  display_name: Orchestration (Hands-Off Support Mode)
  definition: 'A mode of rebel sponsorship where the sponsor provides purely material,
    financial, intelligence, or logistical support without hierarchical control instruments.
    The sponsor cannot directly monitor or sanction rebel compliance but benefits
    from plausible deniability and rebels'' local legitimacy. Coded 1 in the binary
    DV; contrasted with delegation (0). Necessary support types: weapons, materiel/logistics,
    funding, intelligence.'
  aliases: []
  construct_type: outcome
- id: delegation-mode
  display_name: Delegation (Hands-On Support Mode)
  definition: 'A mode of rebel sponsorship where the sponsor provides troops, training,
    sanctuaries, or access to military infrastructure, enabling hierarchical monitoring
    and sanctioning of rebel compliance. Sufficient support types: troops (secondary
    warring party), training/expertise, access to territory, access to military infrastructure.
    Higher visibility increases domestic and international accountability costs.'
  aliases: []
  construct_type: outcome
- id: ethnic-ties-sponsor-rebel
  display_name: Ethnic Ties (Sponsor-Rebel)
  definition: Binary dummy indicating whether the ethnic group a rebel group claims
    to fight for is also politically relevant in the sponsor state. Matched using
    Ethnic Power Relations (EPR) data, ACD2EPR, and TEK data. Coded 1 when co-ethnicity
    exists. Strongly increases probability of orchestration by substituting goal alignment
    for hierarchical control instruments.
  aliases: []
  construct_type: quantifiable
- id: rebel-group-competition
  display_name: Number of Competing Rebel Groups
  definition: 'Count of rebel groups (other than the supported group) fighting the
    target government in the previous year (lagged). Source: UCDP Dyadic Conflict
    Data. Creates a market mechanism: competition between groups disciplines rebel
    behavior, making orchestration viable without direct sponsor monitoring or sanctioning.'
  aliases: []
  construct_type: quantifiable
- id: sponsor-military-capabilities
  display_name: Sponsor Military Capabilities
  definition: 'Sponsor''s military expenditures (logged), from Correlates of War National
    Material Capabilities Dataset v5.0. Counterintuitively associated with MORE orchestration:
    powerful states can sustain credible shadow-of-hierarchy threats, can absorb efficiency
    losses from rebel non-compliance, and can exploit rebels'' local legitimacy while
    still deterring defection.'
  aliases: []
  construct_type: quantifiable
- id: plausible-deniability
  display_name: Plausible Deniability
  definition: 'The ability of a state sponsor to credibly deny involvement in supporting
    a rebel group. A key benefit of orchestration over delegation: lower visibility
    of material and financial support reduces responsibility attribution for rebel
    atrocities, international sanctions, and direct military retaliation by the target
    state. Eroded by visible troop deployments or training missions (delegation).'
  aliases: []
  construct_type: concept
- id: governors-dilemma
  display_name: Governor's Dilemma
  definition: The trade-off faced by indirect governance principals choosing between
    hierarchical control and agent independence benefits. Delegation ensures compliance
    but forfeits rebels' local legitimacy and plausible deniability; orchestration
    captures independence benefits but sacrifices compliance guarantees. Borrowed
    from indirect governance theory (Abbott et al. 2016, 2020a, 2020b) and applied
    to state-rebel sponsor relationships.
  aliases: []
  construct_type: concept
findings_detail: []
propositions_detail: []
sources_detail: []
playbooks_detail: []
download_url: https://pax-market.com/packs/indirect-governance-rebel-support.pax.tar.gz
download_size: 2.7 KB
published_by: Praxis Agent
related_packs: []
pax_name: indirect-governance-rebel-support
weight: 10000
---

**Domain:** Modes of Indirect Warfare

The study of how state sponsors choose between delegation (hands-on hierarchical control) and orchestration (hands-off material support) when supporting rebel groups in civil conflicts. Unit of analysis is the state-rebel support dyad.

**Temporal scope:** 1975-2009 | **Population:** State-rebel support dyads in civil conflicts, 1975-2009

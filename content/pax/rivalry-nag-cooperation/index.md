---
name: rivalry-nag-cooperation
title: Rivalry Nag Cooperation
version: 1.0.0
pax_type: paper
description: 'Explains why states in strategic rivalries choose to support non-state
  armed groups (NAGs) targeting their rivals. Develops a rational choice model of
  rivalry management via indirect confrontation using frustration and opportunity
  game typologies. Tests with original triad-year data covering 175 NAGs and 83 state
  supporters, 1946-2001. Key finding: strategic rivalry increases NAG support probability
  by ~300%; state-NAG cooperation escalates rivalry conflicts.'
author: ''
created: ''
license: ''
tags:
- paper
constructs:
- status-quo-satisfaction
- capability-ratio
- frustration-game
- opportunity-game
- rivalry-duration
- rivalry-intensity
- nag-escalation-effect
engines:
- binary_logit_with_cubic_splines
playbook_names:
- quick_start
construct_count: 7
finding_count: 0
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: rivalry-nag-cooperation
  display_name: Strategic Rivalry and NAG Cooperation
  description: The study of how interstate rivalries shape states' decisions to support
    non-state armed groups targeting their rivals. Encompasses both the causes of
    state-NAG cooperation (rivalry characteristics, satisfaction, capabilities) and
    the consequences for rivalry escalation.
  research_questions: []
  temporal_scope: 1946-2001
  population: Triad-years (NAG, NAG target, potential state supporter in target's
    PRIE), 1946-2001
  level_of_analysis: macro
constructs_detail:
- id: status-quo-satisfaction
  display_name: Status Quo Satisfaction
  definition: 'A state''s level of satisfaction with the prevailing outcome in a rivalry,
    operationalized via prior MID outcomes: +1 (satisfied, won previous dispute),
    -1 (dissatisfied, lost), 0 (neutral/drawn). Derived from Maoz & Mor (2002) rivalry
    supergame framework. Dissatisfied states with low capabilities are the primary
    candidates for NAG support as a substitution strategy.'
  aliases: []
  construct_type: quantifiable
- id: capability-ratio
  display_name: Capability Ratio (Supporter/Target)
  definition: Ratio of the potential supporter's military capabilities to the NAG's
    target's capabilities. Computed as average of shares of military expenditures
    and military personnel (CAPRAT). Values < 1 indicate weaker supporter; > 1 indicate
    stronger. Weak dissatisfied states ('frustration games') and capable constrained
    states ('opportunity games') both increase NAG support probability.
  aliases: []
  construct_type: quantifiable
- id: frustration-game
  display_name: Frustration Game
  definition: A rivalry game type in which the focal state is dissatisfied with the
    status quo (SATISFLEV = -1) but lacks the capabilities to challenge it directly
    (CAPRAT < 1). Supporting NAGs targeting the rival serves as a low-cost substitution
    strategy to harass the rival and potentially weaken its capabilities without risking
    direct retaliation.
  aliases: []
  construct_type: concept
- id: opportunity-game
  display_name: Opportunity Game
  definition: A rivalry game type in which the focal state is dissatisfied with the
    status quo (SATISFLEV = -1) and has the capability to change it (CAPRAT > 1) but
    is deterred from direct confrontation by political constraints. Supporting NAGs
    allows the capable state to pursue strategic goals while managing domestic or
    international accountability costs.
  aliases: []
  construct_type: concept
- id: rivalry-duration
  display_name: Rivalry Duration
  definition: Number of years the rivalry has been in existence up to time t. Longer
    rivalries are associated with higher probability of NAG support (+204% over full
    range in strategic rivalries, Table 3). Entrenched rivalries feature more polarized
    preferences and greater frustration with the status quo.
  aliases: []
  construct_type: quantifiable
- id: rivalry-intensity
  display_name: Rivalry Intensity
  definition: Aggregate maximum hostility level of MIDs in the rivalry divided by
    rivalry duration. Captures the relative severity of the rivalry over time. Higher
    intensity rivalries are associated with more NAG support (+22% in strategic rivalry
    sample, Table 3).
  aliases: []
  construct_type: quantifiable
- id: nag-escalation-effect
  display_name: NAG Support Escalation Effect
  definition: The effect of state-NAG cooperation on the probability of direct conflict
    escalation between the supporter and the target. State-NAG support significantly
    increases target's MID initiation (coeff 1.441**, Table 4) and level of hostility
    against the supporter, making NAG sponsorship a strategy that ultimately intensifies
    rather than substitutes for direct confrontation.
  aliases: []
  construct_type: outcome
findings_detail: []
propositions_detail: []
sources_detail: []
playbooks_detail: []
download_url: https://pax-market.com/pax/rivalry-nag-cooperation.pax.tar.gz
download_size: 2.4 KB
published_by: Praxis Agent
related_packs: []
pax_name: rivalry-nag-cooperation
weight: 10000
---

**Domain:** Strategic Rivalry and NAG Cooperation

The study of how interstate rivalries shape states' decisions to support non-state armed groups targeting their rivals. Encompasses both the causes of state-NAG cooperation (rivalry characteristics, satisfaction, capabilities) and the consequences for rivalry escalation.

**Temporal scope:** 1946-2001 | **Population:** Triad-years (NAG, NAG target, potential state supporter in target's PRIE), 1946-2001

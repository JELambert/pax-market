---
name: ml-materials-discovery
title: Machine learning for computational materials discovery
version: 1.0.2
pax_type: field
description: Machine learning for computational materials discovery — benchmarking
  ML models on crystal stability prediction, thermodynamic property regression, and
  high-throughput materials screening. Covers graph neural network interatomic potentials,
  compositional feature engineering, and discovery-rate evaluation frameworks. Built
  on the Matbench and Matbench Discovery benchmark suites from the Materials Project.
author: ''
created: ''
license: ''
tags:
- field
constructs:
- formation_energy_per_atom
- energy_above_convex_hull
- thermodynamic_stability
- discovery_acceleration_factor
- band_gap
- gnn_interatomic_potential
- mean_absolute_error_materials
engines:
- random_forest
- gradient_boosting
playbook_names:
- quick_start
construct_count: 7
finding_count: 11
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: ml_materials_discovery
  display_name: ML for Materials Discovery
  description: Application of machine learning — particularly graph neural networks
    and gradient boosting on compositional/structural descriptors — to predict materials
    properties (formation energy, band gap, elastic moduli, thermodynamic stability)
    and accelerate computational screening of novel inorganic crystals. Benchmarked
    against DFT ground truth on standardized datasets from the Materials Project.
  research_questions: []
  temporal_scope: 2020–present (ML era of materials informatics)
  population: Inorganic crystalline materials (oxides, sulfides, intermetallics, etc.);
    benchmark datasets derived from the Materials Project and WBM database (256,963
    materials)
  level_of_analysis: material
constructs_detail:
- id: formation_energy_per_atom
  display_name: Formation Energy per Atom
  definition: The energy released or required to form a crystal from its constituent
    elements in their standard reference states, normalized by the number of atoms.
    Measured in eV/atom via DFT calculations. The primary regression target in materials
    property prediction benchmarks.
  aliases: []
  construct_type: quantifiable
- id: energy_above_convex_hull
  display_name: Energy Above Convex Hull
  definition: The thermodynamic distance of a material from the convex hull of stable
    phases in compositional space, measured in eV/atom. Materials with e_above_hull
    = 0 are thermodynamically stable; positive values indicate metastability. The
    key stability criterion in high-throughput screening.
  aliases: []
  construct_type: quantifiable
- id: thermodynamic_stability
  display_name: Thermodynamic Stability
  definition: Binary classification of whether a crystal is thermodynamically stable
    (on the convex hull) or not. In Matbench Discovery, 15.3% of WBM test structures
    are stable. The primary classification target for discovery benchmarks.
  aliases: []
  construct_type: outcome
- id: discovery_acceleration_factor
  display_name: Discovery Acceleration Factor (DAF)
  definition: The ratio of a model's precision at top-k screening relative to random
    selection baseline. Quantifies how much faster a model identifies stable materials
    compared to untargeted DFT calculation. A DAF of 6 means 6x more discoveries per
    DFT calculation than random. Primary efficiency metric in Matbench Discovery.
  aliases: []
  construct_type: quantifiable
- id: band_gap
  display_name: Band Gap
  definition: The energy difference between the valence band maximum and conduction
    band minimum in a crystalline material, measured in eV via DFT (PBE functional).
    Determines whether a material is metallic (0 eV), semiconducting, or insulating.
    A key target in Matbench regression tasks.
  aliases: []
  construct_type: quantifiable
- id: gnn_interatomic_potential
  display_name: Graph Neural Network Interatomic Potential (GNN-IP)
  definition: 'A machine-learned force field that maps crystal graph inputs to total
    energies, atomic forces, and stresses using message-passing neural networks. Trained
    on DFT trajectories (e.g., MPtrj ~1.6M structures), enabling geometry optimization
    at DFT accuracy but orders of magnitude faster. Examples: M3GNet, CHGNet, MACE-MP,
    SevenNet.'
  aliases: []
  construct_type: process
- id: mean_absolute_error_materials
  display_name: Mean Absolute Error (MAE) for Property Prediction
  definition: 'Primary regression metric in Matbench: average absolute difference
    between predicted and DFT-computed material properties (eV/atom for energies,
    eV for band gaps, GPa for moduli). Lower is better; state-of-the-art models achieve
    ~0.02–0.05 eV/atom for formation energy.'
  aliases: []
  construct_type: quantifiable
findings_detail:
- finding_text: GNN interatomic potentials (MACE-MP, CHGNet, SevenNet) achieve Discovery
    Acceleration Factors of 5–6x on the WBM test set, compared to ~1x for random baseline
    and ~2x for simpler one-shot GNN predictors like MEGNet.
  construct_ids:
  - discovery_acceleration_factor
  - gnn_interatomic_potential
  - thermodynamic_stability
  direction: positive
  effect_size: null
  confidence: strong
  method_used: benchmark evaluation on WBM holdout set (N=10,000 unique prototypes)
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
- finding_text: Only 15.3% of WBM test structures are thermodynamically stable (on
    or within 0 meV/atom of the convex hull), establishing the random discovery baseline
    for computing DAF.
  construct_ids:
  - thermodynamic_stability
  - energy_above_convex_hull
  direction: 'null'
  effect_size: null
  confidence: strong
  method_used: DFT convex hull analysis of WBM dataset (256,963 materials)
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
- finding_text: Models trained on geometry-relaxed structures significantly outperform
    those using unrelaxed (initial) structures for stability prediction, demonstrating
    that structural relaxation quality is a key bottleneck.
  construct_ids:
  - crystal_structure_representation
  - thermodynamic_stability
  - gnn_interatomic_potential
  direction: positive
  effect_size: null
  confidence: strong
  method_used: 'ablation comparison: relaxed vs. unrelaxed inputs across 45 model
    submissions'
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
- finding_text: Graph neural network models (coGN, coNGN, MEGNet) systematically outperform
    composition-only models on structure-dependent properties like elastic moduli
    and phonon frequencies, while performing comparably on formation energy where
    composition is highly predictive.
  construct_ids:
  - crystal_structure_representation
  - formation_energy_per_atom
  - bulk_modulus
  - mean_absolute_error_materials
  direction: positive
  effect_size: null
  confidence: strong
  method_used: cross-validated MAE comparison across 14 Matbench tasks, 28 algorithms
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
- finding_text: Gradient boosted trees with Magpie compositional features achieve
    competitive performance on formation energy prediction (MAE ~0.08 eV/atom) despite
    requiring no structural information, demonstrating the strength of composition-based
    features for chemically smooth properties.
  construct_ids:
  - formation_energy_per_atom
  - crystal_structure_representation
  - mean_absolute_error_materials
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: Matbench cross-validation, gradient boosting with Magpie featurization
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
- finding_text: CHGNet, trained on 1.5M MPtrj DFT trajectory frames with magnetic
    moment supervision, achieves force MAE of ~0.06 eV/Å and correctly predicts DFT-relaxed
    structure energies within ~0.03 eV/atom for the majority of Materials Project
    entries.
  construct_ids:
  - gnn_interatomic_potential
  - formation_energy_per_atom
  - energy_above_convex_hull
  direction: positive
  effect_size: null
  confidence: strong
  method_used: held-out test set evaluation on Materials Project data; phonon benchmark
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
- finding_text: GNN interatomic potentials (MACE-MP, CHGNet, SevenNet) achieve Discovery
    Acceleration Factors of 5–6x on the WBM test set, vs ~1x for random baseline and
    ~2x for simpler one-shot GNN predictors.
  construct_ids:
  - discovery_acceleration_factor
  - gnn_interatomic_potential
  - thermodynamic_stability
  direction: positive
  effect_size: null
  confidence: strong
  method_used: benchmark evaluation on WBM holdout set (N=10,000)
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
- finding_text: Only 15.3% of WBM test structures are thermodynamically stable, establishing
    the random discovery baseline for computing DAF.
  construct_ids:
  - thermodynamic_stability
  - energy_above_convex_hull
  direction: 'null'
  effect_size: null
  confidence: strong
  method_used: DFT convex hull analysis of WBM dataset (256,963 materials)
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
- finding_text: Graph neural network models (coGN, coNGN, MEGNet) systematically outperform
    composition-only models on structure-dependent properties like elastic moduli
    and phonon frequencies, while performing comparably on formation energy.
  construct_ids:
  - gnn_interatomic_potential
  - formation_energy_per_atom
  - mean_absolute_error_materials
  direction: positive
  effect_size: null
  confidence: strong
  method_used: cross-validated MAE comparison across 14 Matbench tasks, 28 algorithms
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
- finding_text: CHGNet trained on 1.5M MPtrj DFT trajectory frames achieves force
    MAE of ~0.06 eV/Å and energy MAE of ~0.03 eV/atom on Materials Project held-out
    entries.
  construct_ids:
  - gnn_interatomic_potential
  - formation_energy_per_atom
  - energy_above_convex_hull
  direction: positive
  effect_size: null
  confidence: strong
  method_used: held-out test evaluation on Materials Project data
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
- finding_text: Graph neural network models systematically outperform composition-only
    models on structure-dependent properties like elastic moduli and phonon frequencies,
    while performing comparably on formation energy.
  construct_ids:
  - gnn_interatomic_potential
  - formation_energy_per_atom
  - mean_absolute_error_materials
  direction: positive
  effect_size: null
  confidence: strong
  method_used: cross-validated MAE comparison across 14 Matbench tasks, 28 algorithms
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
- id: riebesell_2025_matbench_discovery
  title: A framework to evaluate machine learning crystal stability predictions
  authors: Riebesell, J., Goodall, R.E.A., Jain, A., Benner, P., Persson, K.A., Lee,
    A.A.
  year: 2025
  doi: 10.1038/s42256-025-00afz
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
- id: dunn_2020_matbench
  title: 'Benchmarking materials property prediction methods: the Matbench test set
    and Automatminer reference algorithm'
  authors: Dunn, A., Wang, Q., Ganose, A., Dopp, D., Jain, A.
  year: 2020
  doi: 10.1038/s41524-020-00406-3
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
- id: deng_2023_chgnet
  title: CHGNet as a pretrained universal neural network potential for charge-informed
    atomistic modelling
  authors: Deng, B., Zhong, P., Jun, K., Riebesell, J., Han, K., Bartel, C.J., Ceder,
    G.
  year: 2023
  doi: 10.1038/s42256-023-00716-3
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
playbooks_detail:
- id: quick_start
  display_name: Quick Start
  description: 'Five-step workflow covering the full Matbench benchmark methodology:
    from linear baselines through gradient boosting (the key tabular benchmark) to
    random forest stability classification. GNN-based engines (CGCNN, MEGNet, MACE-MP,
    CHGNet) are cataloged but require external PyTorch infrastructure to run.'
  estimated_runtime: ''
  step_count: 5
  engines_used:
  - random_forest
  - logistic_regression
  - ridge_regression
  - gradient_boosting
  - ols_regression
relationships_detail: []
quality: {}
pax_schema_version: '1.0'
download_url: https://pax-market.com/pax/ml-materials-discovery.pax.tar.gz
download_size: 5.1 KB
published_by: Praxis Agent
related_packs:
- bartel-comp-materials
pax_name: ml-materials-discovery
weight: 10000
---

**Domain:** ML for Materials Discovery

Application of machine learning — particularly graph neural networks and gradient boosting on compositional/structural descriptors — to predict materials properties (formation energy, band gap, elastic moduli, thermodynamic stability) and accelerate computational screening of novel inorganic crystals. Benchmarked against DFT ground truth on standardized datasets from the Materials Project.

**Temporal scope:** 2020–present (ML era of materials informatics) | **Population:** Inorganic crystalline materials (oxides, sulfides, intermetallics, etc.); benchmark datasets derived from the Materials Project and WBM database (256,963 materials)

## Key Findings

- GNN interatomic potentials (MACE-MP, CHGNet, SevenNet) achieve Discovery Acceleration Factors of 5–6x on the WBM test set, compared to ~1x for random baseline and ~2x for simpler one-shot GNN predictors like MEGNet. *(positive, strong)*
- Only 15.3% of WBM test structures are thermodynamically stable (on or within 0 meV/atom of the convex hull), establishing the random discovery baseline for computing DAF. *(null, strong)*
- Models trained on geometry-relaxed structures significantly outperform those using unrelaxed (initial) structures for stability prediction, demonstrating that structural relaxation quality is a key bottleneck. *(positive, strong)*
- Graph neural network models (coGN, coNGN, MEGNet) systematically outperform composition-only models on structure-dependent properties like elastic moduli and phonon frequencies, while performing comparably on formation energy where composition is highly predictive. *(positive, strong)*
- Gradient boosted trees with Magpie compositional features achieve competitive performance on formation energy prediction (MAE ~0.08 eV/atom) despite requiring no structural information, demonstrating the strength of composition-based features for chemically smooth properties. *(positive, moderate)*
- CHGNet, trained on 1.5M MPtrj DFT trajectory frames with magnetic moment supervision, achieves force MAE of ~0.06 eV/Å and correctly predicts DFT-relaxed structure energies within ~0.03 eV/atom for the majority of Materials Project entries. *(positive, strong)*
- GNN interatomic potentials (MACE-MP, CHGNet, SevenNet) achieve Discovery Acceleration Factors of 5–6x on the WBM test set, vs ~1x for random baseline and ~2x for simpler one-shot GNN predictors. *(positive, strong)*
- Only 15.3% of WBM test structures are thermodynamically stable, establishing the random discovery baseline for computing DAF. *(null, strong)*

*...and 3 more findings*

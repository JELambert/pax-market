---
name: bartel-comp-materials
title: Bartel Comp Materials
version: 1.0.12
pax_type: field
description: Comprehensive knowledge pack covering Christopher Bartel's body of work
  in computational materials science — machine learning for materials discovery, autonomous
  synthesis laboratories, perovskite stability prediction, battery cathode design,
  solid-state synthesis thermodynamics, catalysis and energy conversion, and crystal
  topology characterization. Integrates 142 publications (2016-2026), 6 open-source
  code repositories from Bartel-Group GitHub, and cross-domain construct linkages
  spanning tolerance factors, neural network potentials, thermodynamic selectivity,
  and generative crystal models.
author: ''
created: ''
license: ''
tags:
- field
constructs:
- discovery_acceleration_factor
- band_gap
- bulk_modulus
- crystal_structure_representation
- gnn_interatomic_potential
- mean_absolute_error_materials
- formation_energy_per_atom
- thermodynamic_stability
- revised_tolerance_factor
- energy_above_hull
- neural_network_potential
- synthesis_success_rate
- thermodynamic_selectivity
- perovskite_formability
- intercalation_voltage
- force_field_mae
- reaction_driving_force
- xrd_phase_identification_accuracy
- oxygen_evolution_overpotential
- persistent_homology_descriptor
- goldschmidt_tolerance_factor
- octahedral_factor
- perovskite_decomposition_energy
- halide_perovskite_bandgap
- cation_disorder_energy
- li_diffusion_barrier
- precursor_selection_score
- synthesis_temperature
- metathesis_reaction_feasibility
- thermochemical_cycle_efficiency
- catalytic_loop_directionality
- topological_fingerprint_similarity
- energy_prediction_mae
- crystal_graph_representation
- double_perovskite_bandgap
- exciton_binding_energy
- mg_migration_barrier
- ca_intercalation_voltage
- mg_solid_electrolyte_conductivity
- spinel_cation_inversion
- selectivity_metric
- polymorph_selectivity
- thermodynamic_control_threshold
- sequential_pairwise_mechanism
- short_range_order
- drx_fluorination_degree
- dft_functional_accuracy
- ca_ion_diffusion_barrier
- nitride_perovskite_formability
- synthesis_condition_prediction
- ion_exchange_activation_energy
- nasicon_stability_descriptor
- anion_cometathesis
- dft_prediction_accuracy
- sulfide_cathode_voltage
- gibbs_energy_descriptor
- decomposition_enthalpy
- high_throughput_screening_yield
- synthesis_prediction_calibration
- pairwise_reaction_energy
- thermochemical_ammonia_yield
- programmable_catalyst_enhancement
- catalytic_resonance_frequency
- synthesis_temperature_prediction
- reaction_selectivity_metric
- adaptive_measurement_efficiency
- metastable_polymorph_selectivity
- generative_crystal_model
- tolerance_factor_prediction
- synthesis_selectivity_metric
- proton_insertion_thermodynamics
- cation_vacancy_water_splitting
- betti_curve_descriptor
- text_mined_synthesis_database
- topological_descriptor
- mlip_surface_prediction
- metathesis_driving_force
- automated_phase_identification
- ml_formation_energy_model
- pairwise_reaction_model
- post_generation_screening
- topological_electron_density_descriptor
- nasicon_tolerance_factor
- charge_informed_mlip
- ml_dft_error_correction
- text_mined_synthesis_data
- cathode_capacity
- chalcogenide_perovskite_stability
- chemical_looping_material_viability
engines:
- logistic_regression
- random_forest
- gradient_boosting
- ridge_regression
playbook_names:
- cross_domain_survey
- perovskite_screening
- quick_start
- stability_prediction_benchmark
- synthesis_feasibility_assessment
construct_count: 89
finding_count: 283
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: autonomous_synthesis
  display_name: Autonomous Materials Synthesis
  description: AI-driven autonomous experimentation platforms for accelerated materials
    synthesis. Covers the A-Lab robotic synthesis platform, ML-guided precursor selection,
    adaptive XRD characterization, Bayesian optimization of synthesis parameters,
    and closed-loop discovery workflows.
  research_questions: []
  temporal_scope: 2021-2026
  population: Target inorganic materials for experimental synthesis
  level_of_analysis: Synthesis reaction and experimental campaign
constructs_detail:
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
- id: bulk_modulus
  display_name: Bulk Modulus (VRH)
  definition: Voigt-Reuss-Hill averaged bulk modulus in GPa, measuring resistance
    to uniform compression. Computed from DFT elastic tensors. One of the Matbench
    benchmark regression targets (log_gvrh task).
  aliases: []
  construct_type: quantifiable
- id: crystal_structure_representation
  display_name: Crystal Structure Representation
  definition: The mathematical encoding of a crystalline material for ML input. Ranges
    from composition-only vectors (element fractions) to graph-based representations
    (atoms as nodes, bonds as edges with distances/angles). Graph representations
    enable equivariant GNNs; compositional features enable tabular ML (CGCNN, MEGNet,
    MACE vs. Magpie, SOAP).
  aliases: []
  construct_type: concept
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
- id: formation_energy_per_atom
  display_name: Formation Energy per Atom
  definition: The energy released or required to form a crystal from its constituent
    elements in their standard reference states, normalized by the number of atoms.
    Measured in eV/atom via DFT calculations. The primary regression target in materials
    property prediction benchmarks.
  aliases: []
  construct_type: quantifiable
- id: thermodynamic_stability
  display_name: Thermodynamic Stability
  definition: Binary classification of whether a crystal is thermodynamically stable
    (on the convex hull) or not. In Matbench Discovery, 15.3% of WBM test structures
    are stable. The primary classification target for discovery benchmarks.
  aliases: []
  construct_type: outcome
- id: revised_tolerance_factor
  display_name: Revised Tolerance Factor (τ)
  definition: 'A geometric tolerance factor τ proposed by Bartel et al. (2019) that
    predicts whether a given ABX3 composition will form a stable perovskite structure.
    Unlike the classical Goldschmidt tolerance factor t, τ incorporates the oxidation
    state of A-site cation and uses a different functional form: τ = r_X/r_B - n_A(n_A
    - r_A/r_B / ln(r_A/r_B)). Achieves 92% accuracy on experimental perovskite/non-perovskite
    classification.'
  aliases: []
  construct_type: quantifiable
- id: energy_above_hull
  display_name: Energy Above Convex Hull
  definition: The energy difference (eV/atom) between a material and the convex hull
    of thermodynamically stable phases at the same composition. E_hull = 0 means the
    material is on the hull (thermodynamically stable). Positive values indicate metastability.
    The primary metric for assessing whether a computationally predicted material
    could exist.
  aliases: []
  construct_type: quantifiable
- id: neural_network_potential
  display_name: Neural Network Interatomic Potential
  definition: A machine learning model trained on DFT data that predicts atomic energies,
    forces, and stresses from atomic positions and species. Examples include CHGNet,
    M3GNet, MACE, and SchNet. Enables molecular dynamics and structure relaxation
    at near-DFT accuracy but orders of magnitude faster. CHGNet uniquely incorporates
    magnetic moments and charge states.
  aliases: []
  construct_type: process
- id: synthesis_success_rate
  display_name: Synthesis Success Rate
  definition: The fraction of computationally predicted target materials that are
    successfully synthesized in the laboratory. In the A-Lab autonomous synthesis
    platform, measured as the number of targets where XRD confirms the desired phase
    divided by the total number of attempted syntheses. Key metric for evaluating
    the practical utility of computational materials discovery.
  aliases: []
  construct_type: outcome
- id: thermodynamic_selectivity
  display_name: Thermodynamic Selectivity
  definition: The ratio of thermodynamic driving force for the target synthesis product
    versus competing byproducts. Higher selectivity means the desired phase is strongly
    favored over alternative reaction products. Quantified as the free energy difference
    between the target reaction and the most favorable competing reaction pathway.
  aliases: []
  construct_type: quantifiable
- id: perovskite_formability
  display_name: Perovskite Formability
  definition: Binary classification of whether an ABX3 composition forms a perovskite
    crystal structure (1) or not (0). Determined experimentally via XRD phase identification.
    The primary prediction target for tolerance factor models and ML classifiers in
    the perovskite design literature.
  aliases: []
  construct_type: outcome
- id: intercalation_voltage
  display_name: Intercalation Voltage
  definition: The average voltage (V) at which a guest ion (Li+, Mg2+, Ca2+) intercalates
    into or de-intercalates from a cathode host structure. Computed from DFT total
    energies of the charged and discharged states. A key performance metric for battery
    cathode materials — higher voltage means higher energy density.
  aliases: []
  construct_type: quantifiable
- id: force_field_mae
  display_name: Force Prediction MAE
  definition: Mean absolute error (eV/Å) of an ML interatomic potential's predicted
    atomic forces compared to DFT reference calculations. The primary accuracy benchmark
    for neural network potentials. CHGNet achieves ~30 meV/Å on MPtrj test set; lower
    values indicate more accurate molecular dynamics trajectories.
  aliases: []
  construct_type: quantifiable
- id: reaction_driving_force
  display_name: Reaction Driving Force
  definition: The Gibbs free energy change (ΔG, kJ/mol or eV/atom) of a solid-state
    synthesis reaction at a given temperature. More negative values indicate stronger
    thermodynamic favorability. Used to rank candidate synthesis pathways and predict
    whether a target material can be made via a particular precursor combination.
  aliases: []
  construct_type: quantifiable
- id: xrd_phase_identification_accuracy
  display_name: XRD Phase Identification Accuracy
  definition: The accuracy of automated X-ray diffraction pattern matching for identifying
    crystalline phases in synthesized materials. In autonomous synthesis workflows,
    this is the classification accuracy of ML models that interpret XRD patterns to
    determine whether the target phase was successfully produced.
  aliases: []
  construct_type: quantifiable
- id: oxygen_evolution_overpotential
  display_name: Oxygen Evolution Overpotential
  definition: The excess potential (V) required above the thermodynamic minimum to
    drive the oxygen evolution reaction (OER) on a catalyst surface. Lower overpotential
    indicates a more active catalyst. Typically measured at 10 mA/cm² current density.
    A key metric for evaluating electrocatalysts for water splitting.
  aliases: []
  construct_type: quantifiable
- id: persistent_homology_descriptor
  display_name: Persistent Homology Descriptor
  definition: A topological data analysis method that characterizes the topology of
    electron density distributions in crystalline materials. Computes persistence
    diagrams from sublevel sets of the electron density field, capturing features
    like connected components, loops, and voids at multiple scales. Used to classify
    crystal structure types and predict material properties.
  aliases: []
  construct_type: process
- id: goldschmidt_tolerance_factor
  display_name: Goldschmidt Tolerance Factor (t)
  definition: The classical geometric tolerance factor t = (r_A + r_X) / sqrt(2)(r_B
    + r_X) proposed by Goldschmidt (1926) for predicting perovskite stability. Values
    near 1.0 favor cubic perovskite; t < 0.8 or t > 1.0 favor non-perovskite structures.
    Achieves ~74% accuracy, superseded by Bartel's revised tau.
  aliases: []
  construct_type: quantifiable
- id: octahedral_factor
  display_name: Octahedral Factor (μ)
  definition: The ratio of B-site cation radius to X-site anion radius (μ = r_B/r_X)
    in ABX3 perovskites. Values between 0.44 and 0.90 generally support stable octahedral
    coordination. Used alongside tolerance factors for perovskite stability prediction.
  aliases: []
  construct_type: quantifiable
- id: perovskite_decomposition_energy
  display_name: Perovskite Decomposition Energy
  definition: The DFT-calculated energy difference between a perovskite ABX3 compound
    and its most stable decomposition products (eV/atom). Negative values mean the
    perovskite is thermodynamically stable; positive values indicate it will spontaneously
    decompose. More physically rigorous than geometric tolerance factors.
  aliases: []
  construct_type: quantifiable
- id: halide_perovskite_bandgap
  display_name: Halide Perovskite Band Gap
  definition: The electronic band gap (eV) of halide perovskite materials (ABX3 where
    X = Cl, Br, I). Critical for optoelectronic applications — optimal solar cell
    performance requires band gaps of 1.1-1.7 eV. Tunable via composition engineering
    of A, B, and X sites.
  aliases: []
  construct_type: quantifiable
- id: cation_disorder_energy
  display_name: Cation Disorder Energy
  definition: The energy difference (eV/atom) between the fully ordered and disordered
    cation arrangements in a mixed-metal oxide. In rocksalt cathodes, partial cation
    disorder can enable percolating Li diffusion pathways while maintaining structural
    stability. Computed via special quasi-random structures (SQS) or cluster expansion.
  aliases: []
  construct_type: quantifiable
- id: li_diffusion_barrier
  display_name: Li Diffusion Barrier
  definition: The activation energy barrier (eV) for Li-ion migration between adjacent
    sites in a cathode crystal structure. Computed via nudged elastic band (NEB) calculations.
    Lower barriers enable faster charge/discharge rates. Typically 0.2-1.0 eV for
    intercalation cathodes.
  aliases: []
  construct_type: quantifiable
- id: precursor_selection_score
  display_name: Precursor Selection Score
  definition: A computed score ranking candidate precursor combinations for solid-state
    synthesis of a target material. Incorporates thermodynamic driving force, selectivity
    against competing products, and practical considerations (melting point, reactivity,
    commercial availability). Higher scores indicate more favorable precursor choices.
  aliases: []
  construct_type: quantifiable
- id: synthesis_temperature
  display_name: Synthesis Temperature
  definition: 'The temperature (°C or K) at which a solid-state synthesis reaction
    is conducted. Must be high enough for sufficient kinetics but low enough to avoid
    unwanted side reactions or decomposition. Typical range for ceramics: 600-1400°C.
    ML models increasingly predict optimal synthesis temperatures.'
  aliases: []
  construct_type: quantifiable
- id: metathesis_reaction_feasibility
  display_name: Metathesis Reaction Feasibility
  definition: Binary assessment of whether a proposed metathesis (double exchange)
    reaction between two precursors will produce the desired product. Determined by
    comparing the thermodynamic driving force of the target reaction against all competing
    reaction pathways. A feasible metathesis reaction has negative ΔG and high selectivity.
  aliases: []
  construct_type: outcome
- id: thermochemical_cycle_efficiency
  display_name: Thermochemical Cycle Efficiency
  definition: The solar-to-fuel energy conversion efficiency (η) of a thermochemical
    water splitting cycle using metal oxide redox pairs. Depends on the reduction
    temperature, oxidation temperature, oxygen nonstoichiometry, and heat recovery.
    Typical values range from 5-40% depending on the oxide system and operating conditions.
  aliases: []
  construct_type: quantifiable
- id: catalytic_loop_directionality
  display_name: Catalytic Loop Directionality
  definition: The directional control in programmable catalytic loops where dynamic
    oscillations in catalyst composition or surface state drive net reaction progress
    in a preferred direction. A key concept in catalytic resonance theory — the frequency
    and amplitude of oscillations determine whether the catalytic cycle runs forward,
    backward, or reaches a dynamic steady state.
  aliases: []
  construct_type: concept
- id: topological_fingerprint_similarity
  display_name: Topological Fingerprint Similarity
  definition: A similarity metric between two crystalline materials based on the comparison
    of their persistent homology descriptors (persistence diagrams). Computed using
    Wasserstein or bottleneck distance between persistence diagrams derived from electron
    density fields. Enables structure-agnostic comparison of materials across different
    space groups.
  aliases: []
  construct_type: quantifiable
- id: energy_prediction_mae
  display_name: Energy Prediction MAE
  definition: Mean absolute error (meV/atom) of an ML model's predicted formation
    energy or total energy compared to DFT reference calculations. The primary accuracy
    benchmark for ML property prediction models. State-of-the-art models achieve ~20-30
    meV/atom on Materials Project datasets.
  aliases: []
  construct_type: quantifiable
- id: crystal_graph_representation
  display_name: Crystal Graph Representation
  definition: A graph-based encoding of crystal structures where atoms are nodes and
    bonds are edges, with node/edge features encoding atomic properties and interatomic
    distances. Used as input to graph neural network models (CGCNN, MEGNet, SchNet,
    DimeNet) for property prediction. The choice of graph construction (cutoff radius,
    edge features) significantly affects model performance.
  aliases: []
  construct_type: process
- id: double_perovskite_bandgap
  display_name: Double Perovskite Band Gap
  definition: The electronic band gap of inorganic halide double perovskites (A2BB'X6),
    which determines their suitability for optoelectronic applications. Computed via
    hybrid DFT (HSE06) or GW-BSE methods.
  aliases: []
  construct_type: quantifiable
- id: exciton_binding_energy
  display_name: Exciton Binding Energy
  definition: The energy required to dissociate an electron-hole pair (exciton) in
    a semiconductor. In double perovskites, large exciton binding energies indicate
    strong electron-hole coupling, relevant for light-emitting applications.
  aliases: []
  construct_type: quantifiable
- id: mg_migration_barrier
  display_name: Mg-Ion Migration Barrier
  definition: The activation energy for Mg2+ ion hopping between sites in a host crystal
    structure, typically measured in meV. Lower barriers enable faster Mg-ion diffusion
    and better cathode rate capability in rechargeable Mg batteries.
  aliases: []
  construct_type: quantifiable
- id: ca_intercalation_voltage
  display_name: Ca Intercalation Voltage
  definition: The average electrochemical potential for reversible Ca2+ insertion/extraction
    in a host cathode material for Ca-ion batteries. Higher voltages enable higher
    energy density.
  aliases: []
  construct_type: quantifiable
- id: mg_solid_electrolyte_conductivity
  display_name: Mg Solid Electrolyte Conductivity
  definition: The ionic conductivity of solid-state Mg2+ conductors, critical for
    enabling all-solid-state Mg batteries. Limited by the high migration barriers
    of divalent Mg2+ ions in most crystalline hosts.
  aliases: []
  construct_type: quantifiable
- id: spinel_cation_inversion
  display_name: Spinel Cation Inversion
  definition: The degree to which cations in a spinel structure (AB2X4) occupy non-ideal
    crystallographic sites (tetrahedral vs octahedral), often expressed as inversion
    fraction. Affects Mg migration pathways and electrochemical properties.
  aliases: []
  construct_type: quantifiable
- id: selectivity_metric
  display_name: Selectivity Metric
  definition: A quantitative measure of how selectively a solid-state reaction produces
    the desired target phase versus competing byproduct phases, derived from thermodynamic
    reaction energies across all possible competing reactions in a chemical network.
  aliases: []
  construct_type: quantifiable
- id: polymorph_selectivity
  display_name: Polymorph Selectivity
  definition: The degree to which a solid-state synthesis pathway preferentially forms
    one crystal polymorph over thermodynamically competing polymorphs, governed by
    the interplay of reaction energy, surface energy, and nucleation barriers.
  aliases: []
  construct_type: quantifiable
- id: thermodynamic_control_threshold
  display_name: Thermodynamic Control Threshold
  definition: The minimum energy difference (in meV/atom) between the most favorable
    initial reaction product and competing phases above which product formation is
    reliably predicted by thermodynamics alone, empirically determined to be approximately
    60 meV/atom.
  aliases: []
  construct_type: quantifiable
- id: sequential_pairwise_mechanism
  display_name: Sequential Pairwise Reaction Mechanism
  definition: The process by which solid-state ceramic synthesis proceeds through
    a sequence of binary reactions at precursor particle interfaces, where the most
    thermodynamically favorable pairwise reaction occurs first and intermediate phases
    progressively react to form the target product.
  aliases: []
  construct_type: process
- id: short_range_order
  display_name: Short-Range Order in Disordered Rocksalt
  definition: The local cation ordering in disordered rocksalt (DRX) cathode materials
    that deviates from a perfectly random distribution. SRO affects Li percolation
    networks, voltage profiles, and cycling stability in DRX cathodes.
  aliases: []
  construct_type: quantifiable
- id: drx_fluorination_degree
  display_name: DRX Fluorination Degree
  definition: The extent of fluorine incorporation into disordered rocksalt cathode
    materials, which modifies voltage, capacity, and Li percolation. Achieving target
    fluorination requires careful precursor selection to avoid LiF formation.
  aliases: []
  construct_type: quantifiable
- id: dft_functional_accuracy
  display_name: DFT Functional Accuracy for Solids
  definition: The accuracy of different density functional theory exchange-correlation
    approximations (PBE, SCAN, r2SCAN) for predicting thermodynamic properties of
    inorganic solids, including formation enthalpies and phase stability.
  aliases: []
  construct_type: quantifiable
- id: ca_ion_diffusion_barrier
  display_name: Ca-Ion Diffusion Barrier
  definition: The activation energy for Ca2+ migration in solid-state materials, critical
    for both Ca-ion battery cathodes and solid electrolytes. Ca2+ mobility is generally
    much lower than Li+ due to its larger size and higher charge density.
  aliases: []
  construct_type: quantifiable
- id: nitride_perovskite_formability
  display_name: Nitride Perovskite Formability
  definition: The likelihood that an ABN3 composition will crystallize in the perovskite
    structure. Nitride perovskites are extremely rare compared to oxide/halide analogs
    due to challenging synthesis and stability requirements.
  aliases: []
  construct_type: quantifiable
- id: synthesis_condition_prediction
  display_name: Synthesis Condition Prediction
  definition: ML-based prediction of optimal solid-state synthesis conditions (temperature,
    time, atmosphere) from precursor properties and reaction features, trained on
    text-mined literature data.
  aliases: []
  construct_type: quantifiable
- id: ion_exchange_activation_energy
  display_name: Ion Exchange Activation Energy
  definition: The energy barrier governing the rate of ion exchange reactions in solid-state
    synthesis, determined by defect formation energies and hopping barriers in the
    salt precursor rather than the ceramic target material.
  aliases: []
  construct_type: quantifiable
- id: nasicon_stability_descriptor
  display_name: NASICON Stability Descriptor
  definition: A two-dimensional descriptor combining cation size and electronegativity
    differences to predict the thermodynamic stability of NASICON-structured materials
    (NaxMM'(PO4)3). Enables rapid screening of the large NASICON composition space.
  aliases: []
  construct_type: quantifiable
- id: anion_cometathesis
  display_name: Anion Cometathesis
  definition: A double-ion exchange synthesis strategy where two anions are simultaneously
    exchanged between precursors, enabling formation of complex oxides at substantially
    lower temperatures than conventional ceramic routes by providing large thermodynamic
    driving forces.
  aliases: []
  construct_type: process
- id: dft_prediction_accuracy
  display_name: DFT Prediction Accuracy for Solid Stability
  definition: The accuracy with which density functional theory approximations (PBE,
    SCAN, r2SCAN) predict the thermodynamic stability of inorganic solids, measured
    as mean absolute error relative to experimental formation enthalpies.
  aliases: []
  construct_type: quantifiable
- id: sulfide_cathode_voltage
  display_name: Sulfide Cathode Voltage
  definition: The electrochemical voltage of sulfide-based cathode materials for Li-ion
    or multivalent batteries. Sulfide cathodes generally operate at lower voltages
    than oxides but may offer advantages in ionic conductivity and interface compatibility.
  aliases: []
  construct_type: quantifiable
- id: gibbs_energy_descriptor
  display_name: Gibbs Energy Descriptor
  definition: A physically motivated descriptor identified via SISSO (sure independence
    screening and sparsifying operator) that predicts the Gibbs free energy of inorganic
    crystalline solids as a function of temperature, enabling temperature-dependent
    phase stability calculations with ~50 meV/atom accuracy.
  aliases: []
  construct_type: quantifiable
- id: decomposition_enthalpy
  display_name: Decomposition Enthalpy
  definition: The enthalpy change associated with a compound decomposing into competing
    phases (other compounds and/or elemental forms). Unlike formation enthalpy which
    measures stability relative to elements only, decomposition enthalpy captures
    the true thermodynamic competition that determines compound stability.
  aliases: []
  construct_type: quantifiable
- id: high_throughput_screening_yield
  display_name: High-Throughput Screening Yield
  definition: The fraction of computationally screened candidate materials that pass
    stability and property filters and are ultimately validated experimentally, reflecting
    the efficiency of computational materials discovery pipelines.
  aliases: []
  construct_type: quantifiable
- id: synthesis_prediction_calibration
  display_name: Synthesis Prediction Calibration
  definition: The degree to which machine learning synthesizability scores align with
    ground-truth thermodynamic metrics (convex hull energies, selectivity scores),
    measuring whether ML models correctly estimate the likelihood that a hypothetical
    material can be experimentally synthesized.
  aliases: []
  construct_type: quantifiable
- id: pairwise_reaction_energy
  display_name: Pairwise Reaction Energy
  definition: The thermodynamic driving force for a reaction between a specific pair
    of solid precursors at their interface, used to predict which intermediate phases
    form first during solid-state synthesis of multicomponent ceramics.
  aliases: []
  construct_type: quantifiable
- id: thermochemical_ammonia_yield
  display_name: Thermochemical Ammonia Yield
  definition: The equilibrium yield of ammonia from solar thermochemical synthesis
    cycles involving metal nitride/oxide redox pairs, determined by Gibbs energy minimization
    across hydrolysis, reduction, nitrogen fixation, and nitride reformation steps.
  aliases: []
  construct_type: quantifiable
- id: programmable_catalyst_enhancement
  display_name: Programmable Catalyst Enhancement
  definition: The performance gain achieved by dynamically modulating catalyst surface
    binding energies through external forcing (voltage, strain, temperature oscillation),
    quantified as the ratio of dynamic to static catalytic rates or the reduction
    in required overpotential.
  aliases: []
  construct_type: quantifiable
- id: catalytic_resonance_frequency
  display_name: Catalytic Resonance Frequency
  definition: The optimal oscillation frequency at which forced dynamic modulation
    of a programmable catalyst achieves maximum rate enhancement, determined by the
    match between external forcing period and intrinsic catalytic turnover timescales.
  aliases: []
  construct_type: quantifiable
- id: synthesis_temperature_prediction
  display_name: Synthesis Temperature Prediction
  definition: ML prediction of optimal heating temperature for solid-state synthesis,
    learned from text-mined synthesis recipes. Correlated with precursor stability
    metrics (melting points, formation energies) following extended Tamman's rule.
  aliases: []
  construct_type: quantifiable
- id: reaction_selectivity_metric
  display_name: Reaction Selectivity Metric
  definition: Quantitative metrics (primary and secondary competition) assessing the
    favorability of target phase formation versus impurity phase formation in solid-state
    reactions. Used to rank and select synthesis reactions that maximize target yield.
  aliases: []
  construct_type: quantifiable
- id: adaptive_measurement_efficiency
  display_name: Adaptive Measurement Efficiency
  definition: The improvement in measurement effectiveness achieved by ML-guided adaptive
    experimentation compared to conventional static measurement protocols. For XRD,
    this means using early diffraction data to steer subsequent measurements toward
    informative angular ranges.
  aliases: []
  construct_type: quantifiable
- id: metastable_polymorph_selectivity
  display_name: Metastable Polymorph Selectivity
  definition: The ability to selectively synthesize a metastable crystal polymorph
    over the thermodynamically stable ground state through careful control of reaction
    energetics and surface energy contributions in solid-state synthesis.
  aliases: []
  construct_type: process
- id: generative_crystal_model
  display_name: Generative Crystal Model
  definition: AI models (diffusion models, variational autoencoders, large language
    models) that generate novel crystal structures. Benchmarked against baseline methods
    like random charge-balanced prototype enumeration and data-driven ion exchange
    of known compounds.
  aliases: []
  construct_type: concept
- id: tolerance_factor_prediction
  display_name: Tolerance Factor Prediction
  definition: ML-derived or analytically derived tolerance factors (e.g., tau) that
    predict the stability and formability of perovskite-structured compounds based
    on ionic radii, oxidation states, and electronegativity.
  aliases: []
  construct_type: quantifiable
- id: synthesis_selectivity_metric
  display_name: Synthesis Selectivity Metric
  definition: Quantitative measures (primary and secondary competition) of the thermodynamic
    favorability of target phase formation vs impurity phase formation in solid-state
    reactions. Higher selectivity indicates reactions that preferentially produce
    the desired product.
  aliases: []
  construct_type: quantifiable
- id: proton_insertion_thermodynamics
  display_name: Proton Insertion Thermodynamics
  definition: The thermodynamic energetics of proton (H+) incorporation into perovskite
    and brownmillerite oxide structures, relevant for protonic ceramic fuel cells
    and electrochemical applications.
  aliases: []
  construct_type: quantifiable
- id: cation_vacancy_water_splitting
  display_name: Cation Vacancy-Mediated Water Splitting
  definition: A mechanism for thermochemical water splitting where cation vacancies
    in spinel metal oxides (rather than conventional oxygen vacancies) mediate the
    redox cycling, enabled by cation site inversion that lowers vacancy formation
    energies.
  aliases: []
  construct_type: process
- id: betti_curve_descriptor
  display_name: Betti Curve Descriptor
  definition: A topological descriptor derived from persistent homology applied to
    electron density fields of crystalline solids, encoding bonding characteristics
    by tracking topological features (connected components, loops, voids) across varying
    density thresholds as a function of filtration parameter.
  aliases: []
  construct_type: quantifiable
- id: text_mined_synthesis_database
  display_name: Text-Mined Synthesis Database
  definition: A structured dataset of synthesis procedures extracted from scientific
    literature using NLP and text mining, containing precursors, conditions, and outcomes
    that enable data-driven analysis of synthesis-structure-property relationships.
  aliases: []
  construct_type: concept
- id: topological_descriptor
  display_name: Topological Descriptor (Betti Curves)
  definition: Descriptors derived from persistent homology (Betti curves) that compress
    electron density distributions into compact representations capturing bonding
    characteristics through components, cycles, and voids across electron density
    thresholds.
  aliases: []
  construct_type: quantifiable
- id: mlip_surface_prediction
  display_name: MLIP Surface Prediction
  definition: Application of machine learning interatomic potentials (MLIPs) to compute
    surface phase diagrams, surface energies, and surface reconstructions at a fraction
    of the DFT cost while maintaining near-DFT accuracy.
  aliases: []
  construct_type: process
- id: metathesis_driving_force
  display_name: Metathesis Driving Force
  definition: The thermodynamic driving force available in metathesis (double displacement)
    reactions for inorganic synthesis, which can dramatically alter the reaction landscape
    to enable rapid and selective formation of target phases that are otherwise difficult
    to synthesize via traditional routes.
  aliases: []
  construct_type: quantifiable
- id: automated_phase_identification
  display_name: Automated Phase Identification
  definition: ML-based methods for automatically identifying crystalline phases from
    X-ray diffraction data, including probabilistic neural networks and adaptive measurement
    strategies that optimize data collection for phase detection.
  aliases: []
  construct_type: process
- id: ml_formation_energy_model
  display_name: ML Formation Energy Model
  definition: Machine learning models trained to predict formation energies of inorganic
    crystalline solids from compositional and structural features. Model accuracy
    depends critically on training data quality, diversity, and balance across chemical
    space.
  aliases: []
  construct_type: quantifiable
- id: pairwise_reaction_model
  display_name: Pairwise Reaction Model
  definition: A model for solid-state synthesis where phase evolution from multiple
    precursors proceeds as a sequence of interfacial reactions initiating between
    two phases at a time. The most reactive pairwise interface determines which non-equilibrium
    intermediate phases form.
  aliases: []
  construct_type: concept
- id: post_generation_screening
  display_name: Post-Generation Screening Efficiency
  definition: The improvement in success rates achieved by passing ML-generated candidate
    materials through stability and property filters from pre-trained models (e.g.,
    universal interatomic potentials) as a low-cost post-processing step.
  aliases: []
  construct_type: process
- id: topological_electron_density_descriptor
  display_name: Topological Electron Density Descriptor
  definition: Betti curve descriptors derived from persistent homology that compress
    electron densities of crystalline materials into compact representations, capturing
    bonding characteristics by encoding topological features (components, cycles,
    voids).
  aliases: []
  construct_type: quantifiable
- id: nasicon_tolerance_factor
  display_name: NASICON Tolerance Factor
  definition: Machine-learned tolerance factor for NASICON-structured materials based
    on Na content, elemental radii, electronegativities, and Madelung energy. Classifies
    NASICON phases in terms of their synthetic accessibility.
  aliases: []
  construct_type: quantifiable
- id: charge_informed_mlip
  display_name: Charge-Informed MLIP
  definition: Machine learning interatomic potentials that incorporate charge/oxidation
    state information (e.g., via magnetic moment prediction) to describe both atomic
    and electronic degrees of freedom, enabling modeling of redox-coupled phenomena
    in electrochemical systems.
  aliases: []
  construct_type: concept
- id: ml_dft_error_correction
  display_name: ML DFT Error Correction
  definition: Use of machine learning models to correct systematic errors in DFT-computed
    enthalpies of formation by learning error patterns from electronic structure features.
    Can reduce PBE errors from MAE ~195 meV/atom to ~80 meV/atom.
  aliases: []
  construct_type: process
- id: text_mined_synthesis_data
  display_name: Text-Mined Synthesis Data
  definition: Structured synthesis datasets extracted from scientific literature using
    NLP/text mining methods. These datasets capture synthesis procedures, precursors,
    conditions (temperature, time, atmosphere), and outcomes for thousands of inorganic
    materials, enabling data-driven synthesis prediction.
  aliases: []
  construct_type: concept
- id: cathode_capacity
  display_name: Cathode Specific Capacity
  definition: The gravimetric charge storage capacity of a battery cathode material
    (mAh/g). Determined by the number of intercalatable ions per formula unit and
    the molecular weight. Higher capacity enables higher energy density batteries.
    Theoretical capacity from DFT; practical capacity from electrochemical cycling.
  aliases: []
  construct_type: quantifiable
- id: chalcogenide_perovskite_stability
  display_name: Chalcogenide Perovskite Stability
  definition: The thermodynamic stability of perovskites with chalcogenide anions
    (S2-, Se2-, Te2-) instead of oxide or halide anions. These materials are scarce
    despite favorable tolerance factors, suggesting additional instability mechanisms.
  aliases: []
  construct_type: quantifiable
- id: chemical_looping_material_viability
  display_name: Chemical Looping Material Viability
  definition: The thermodynamic feasibility of a redox-active material to mediate
    chemical looping processes, assessed through equilibrium analysis of oxidation
    and reduction half-cycles under process-relevant conditions.
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
- finding_text: The revised tolerance factor τ achieves 92% classification accuracy
    for perovskite vs non-perovskite ABX3 compositions across 576 experimental data
    points, significantly outperforming the classical Goldschmidt tolerance factor
    t (74% accuracy).
  construct_ids:
  - revised_tolerance_factor
  - perovskite_formability
  direction: positive
  effect_size: AUC improvement from 0.74 to 0.92
  confidence: strong
  method_used: logistic_regression
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
- finding_text: The revised tolerance factor τ correctly predicts the stability of
    both oxide and halide perovskites within a single model, whereas previous tolerance
    factors required separate parameterizations for different anion chemistries.
  construct_ids:
  - revised_tolerance_factor
  - perovskite_formability
  direction: positive
  effect_size: null
  confidence: strong
  method_used: logistic_regression
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
- finding_text: The A-Lab autonomous synthesis platform successfully synthesized 41
    of 58 target materials (71% success rate) within 17 days of continuous operation,
    with each synthesis attempt taking approximately 4 hours from precursor mixing
    to XRD characterization.
  construct_ids:
  - synthesis_success_rate
  - xrd_phase_identification_accuracy
  direction: positive
  effect_size: 71% success rate (41/58 targets)
  confidence: strong
  method_used: experimental_validation
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
- finding_text: ML-guided precursor selection combined with Bayesian optimization
    of synthesis parameters enabled the A-Lab to autonomously discover synthesis recipes
    for materials that had never been experimentally reported before.
  construct_ids:
  - synthesis_success_rate
  - thermodynamic_selectivity
  direction: positive
  effect_size: null
  confidence: strong
  method_used: bayesian_optimization
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
- finding_text: CHGNet achieves force prediction MAE of 30 meV/Å and energy MAE of
    22 meV/atom on the Materials Project trajectory (MPtrj) dataset containing 1.58M
    structures, while uniquely modeling charge states and magnetic moments through
    explicit charge equilibration.
  construct_ids:
  - neural_network_potential
  - force_field_mae
  - formation_energy_per_atom
  direction: positive
  effect_size: 'Force MAE: 30 meV/Å; Energy MAE: 22 meV/atom'
  confidence: strong
  method_used: graph_neural_network
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
- finding_text: CHGNet correctly predicts the magnetic ground states of Fe, Co, Ni,
    and Mn-containing materials and the charge-transfer-driven phase transitions in
    LixMnO2 battery cathodes, capabilities absent in charge-agnostic potentials like
    M3GNet.
  construct_ids:
  - neural_network_potential
  - intercalation_voltage
  direction: positive
  effect_size: null
  confidence: strong
  method_used: molecular_dynamics
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
- finding_text: Integrating computational thermodynamic screening with ML-guided synthesis
    planning reduces the experimental search space for novel inorganic materials by
    2-3 orders of magnitude compared to trial-and-error approaches.
  construct_ids:
  - thermodynamic_selectivity
  - synthesis_success_rate
  - formation_energy_per_atom
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: review_synthesis
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
- finding_text: The primary bottleneck in autonomous materials discovery is not computational
    prediction accuracy but the gap between thermodynamic stability predictions and
    practical synthesizability — many thermodynamically stable materials remain experimentally
    inaccessible.
  construct_ids:
  - energy_above_hull
  - synthesis_success_rate
  - reaction_driving_force
  direction: conditional
  effect_size: null
  confidence: moderate
  method_used: review_synthesis
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
- finding_text: Of 903 Cs2BB'Cl6 double perovskite compositions screened using the
    revised tolerance factor tau, 311 were predicted as likely perovskites and 261
    of those (84%) were predicted thermodynamically synthesizable with decomposition
    enthalpy below 0.05 eV/atom.
  construct_ids:
  - revised_tolerance_factor
  - perovskite_formability
  - perovskite_decomposition_energy
  direction: positive
  effect_size: 261/311 = 84% synthesizability rate among tau-predicted perovskites
  confidence: strong
  method_used: DFT (PBE+U) + tolerance factor screening
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
- finding_text: 47 non-toxic Cs2BB'Cl6 double perovskites were identified with direct
    or nearly direct band gaps between 1-3 eV suitable for optoelectronic applications,
    computed with HSE06 hybrid functional.
  construct_ids:
  - double_perovskite_bandgap
  - perovskite_formability
  direction: positive
  effect_size: 47 candidates with 1-3 eV direct band gaps from 261 stable compounds
  confidence: strong
  method_used: HSE06 hybrid DFT
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
- finding_text: Triple-alkali double perovskites Cs2[Alk]+[TM]3+Cl6 exhibit large
    and tunable exciton binding energies due to mixing of Alk-Cl and TM-Cl sublattices,
    enabling small band gaps with strong electron-hole coupling as computed by GW-BSE.
  construct_ids:
  - exciton_binding_energy
  - double_perovskite_bandgap
  direction: positive
  effect_size: Large exciton binding energies from sublattice mixing mechanism
  confidence: strong
  method_used: GW-BSE (Bethe-Salpeter equation)
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
- finding_text: Decomposition enthalpies (Delta_Hd) provide more accurate stability
    predictions than formation enthalpies (Delta_Hf) because DFT systematic errors
    partially cancel when comparing chemically similar phases. The phase stability
    of 71 ternary compounds showed much better agreement with experiment when assessed
    via decomposition reactions.
  construct_ids:
  - perovskite_decomposition_energy
  - formation_energy_per_atom
  - energy_above_hull
  direction: positive
  effect_size: Systematic DFT errors cancel in decomposition reactions vs formation
    energies
  confidence: strong
  method_used: DFT (PBE, SCAN) with experimental comparison
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
- finding_text: For 71 ternary compounds, DFT-predicted phase stability (stable vs
    unstable) agreed with experiment in the majority of cases when decomposition reactions
    to competing phases were used, but formation enthalpy from elements showed larger
    systematic errors that did not cancel.
  construct_ids:
  - perovskite_decomposition_energy
  - energy_above_hull
  direction: positive
  effect_size: Error cancellation in decomposition enthalpies improves stability prediction
    accuracy
  confidence: strong
  method_used: DFT benchmark against 71 experimental ternary compounds
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
- finding_text: 'A comprehensive review establishes that computational approaches
    for thermodynamic stability prediction of inorganic solids fall into three categories:
    (1) DFT-based convex hull analysis, (2) machine learning of formation energies,
    and (3) descriptor-based approaches like tolerance factors. Each has distinct
    accuracy-throughput tradeoffs.'
  construct_ids:
  - formation_energy_per_atom
  - energy_above_hull
  - perovskite_formability
  direction: unknown
  effect_size: null
  confidence: foundational
  method_used: Literature review
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
- finding_text: Chalcogenide perovskites (ABX3, X=S,Se,Te) are thermodynamically unstable
    despite having favorable tolerance factors, indicating that tolerance factor alone
    is insufficient to predict formability for chalcogenide anions. The instability
    has both thermodynamic and chemical origins.
  construct_ids:
  - chalcogenide_perovskite_stability
  - revised_tolerance_factor
  - perovskite_formability
  direction: 'null'
  effect_size: Favorable tau but thermodynamically unstable - tolerance factor necessary
    but not sufficient
  confidence: strong
  method_used: DFT first-principles calculations
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
- finding_text: The sparsity of chalcogenide perovskites is explained by thermodynamic
    competition with non-perovskite phases and unfavorable chemical bonding compared
    to oxide and halide analogs, establishing that tolerance factor predictions must
    be supplemented with thermodynamic stability analysis for chalcogenide compositions.
  construct_ids:
  - chalcogenide_perovskite_stability
  - perovskite_decomposition_energy
  - revised_tolerance_factor
  direction: negative
  effect_size: null
  confidence: strong
  method_used: DFT convex hull analysis
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
- finding_text: High-throughput DFT screening followed by experimental synthesis successfully
    realized two new Ce-based nitride perovskites, CeMoN3 and CeWN3, adding to the
    very small number of experimentally known nitride perovskites.
  construct_ids:
  - nitride_perovskite_formability
  - perovskite_formability
  direction: positive
  effect_size: 2 new nitride perovskites experimentally realized from computational
    predictions
  confidence: strong
  method_used: High-throughput DFT screening + experimental synthesis
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
- finding_text: Nitride perovskites remain extremely rare experimentally despite the
    broad diversity of oxide and halide perovskites, with CeMoN3 and CeWN3 joining
    only a handful of previously known ABN3 compounds.
  construct_ids:
  - nitride_perovskite_formability
  - perovskite_decomposition_energy
  direction: negative
  effect_size: Only ~5 nitride perovskites known experimentally before this work
  confidence: strong
  method_used: Experimental synthesis with DFT guidance
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
- finding_text: A simple 2D descriptor based on cation size and electronegativity
    differences, extracted via sure independence screening and ML ranking, classifies
    NASICON phase stability with high accuracy across the full composition space.
  construct_ids:
  - nasicon_stability_descriptor
  - energy_above_hull
  direction: positive
  effect_size: 2D descriptor sufficient for NASICON stability classification
  confidence: strong
  method_used: Sure independence screening + ML ranking
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
- finding_text: MgCrMnO4 spinel with 18% Mg/Mn inversion was synthesized and studied
    as a high-voltage Mg cathode. Operando XRD enabled accurate quantification of
    cation migration during cycling, revealing the Mg-ion migration mechanism through
    spinel lattice sites.
  construct_ids:
  - spinel_cation_inversion
  - mg_migration_barrier
  - intercalation_voltage
  direction: positive
  effect_size: 18% Mg/Mn inversion; first accurate operando quantification of cation
    contents in multivalent battery spinel
  confidence: strong
  method_used: Operando synchrotron XRD with Rietveld refinement
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
- finding_text: First demonstration of high-quality operando diffraction data enabling
    accurate quantification of cation contents in crystallographic sites during multivalent
    battery cycling, establishing a new methodology for studying Mg-ion migration
    mechanisms.
  construct_ids:
  - mg_migration_barrier
  - spinel_cation_inversion
  direction: positive
  effect_size: null
  confidence: strong
  method_used: Operando synchrotron XRD
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
- finding_text: MgxCr2S4 spinel cathode operates via the high-voltage Cr3+/4+ redox
    couple. DFT predicted it as a suitable high-voltage Mg cathode, but experimental
    electrochemical cycling showed limited reversibility, with voltage plateaus observed
    but capacity fading over cycles.
  construct_ids:
  - intercalation_voltage
  - cathode_capacity
  - mg_migration_barrier
  direction: conditional
  effect_size: Cr3+/4+ redox enables higher voltage than Mo6S8 or Ti2S4 sulfide cathodes,
    but limited cycling stability
  confidence: moderate
  method_used: DFT prediction + experimental electrochemistry
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
- finding_text: Existing sulfide cathodes for Mg batteries (MgxMo6S8, MgxTi2S4) have
    voltages too low for high energy density cells. The Cr3+/4+ couple in MgxCr2S4
    was predicted computationally to provide significantly higher voltage.
  construct_ids:
  - intercalation_voltage
  - cathode_capacity
  direction: positive
  effect_size: Cr3+/4+ voltage significantly higher than existing sulfide cathodes
  confidence: moderate
  method_used: DFT voltage calculation
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
- finding_text: Seven MgLn2X4 (Ln=lanthanoid, X=S,Se) chalcogenide spinels are calculated
    to have low Mg migration barriers (<380 meV) and are thermodynamically stable
    or nearly stable (within 50 meV/atom of hull). Larger Ln cations increase Mg mobility
    but decrease spinel structure stability.
  construct_ids:
  - mg_solid_electrolyte_conductivity
  - mg_migration_barrier
  - energy_above_hull
  direction: conditional
  effect_size: Migration barriers <380 meV; stability within 50 meV/atom; mobility-stability
    tradeoff with Ln size
  confidence: strong
  method_used: DFT-NEB migration barrier calculations
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
- finding_text: As the size of the lanthanoid cation increases in MgLn2X4 spinels,
    Mg mobility increases but thermodynamic stability in the spinel structure decreases,
    revealing a fundamental tradeoff between conductivity and structural stability
    for Mg solid electrolytes.
  construct_ids:
  - mg_solid_electrolyte_conductivity
  - mg_migration_barrier
  direction: conditional
  effect_size: Inverse relationship between Ln size, Mg mobility, and spinel stability
  confidence: strong
  method_used: DFT-NEB across lanthanoid series
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
- finding_text: 'First-principles evaluation of P-type layered CaTM2O4 (TM=Ti,V,Cr,Mn,Fe,Co,Ni)
    demonstrates that several compositions have excellent battery properties: thermodynamic
    stability, average voltages of 2.2-4.2 V vs Ca/Ca2+, energy densities up to 600-800
    Wh/kg, synthesizability, and reasonable Ca-ion mobility.'
  construct_ids:
  - ca_intercalation_voltage
  - cathode_capacity
  - formation_energy_per_atom
  direction: positive
  effect_size: Voltages 2.2-4.2 V; energy densities 600-800 Wh/kg for best TM compositions
  confidence: strong
  method_used: DFT (GGA+U) systematic evaluation
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
- finding_text: P-type layered Ca transition metal oxides represent a promising class
    of Ca cathode materials, with Ca-V and Ca-Cr compositions showing the best combination
    of high voltage, stability, and ion mobility among the TM series evaluated.
  construct_ids:
  - ca_intercalation_voltage
  - cathode_capacity
  - li_diffusion_barrier
  direction: positive
  effect_size: Ca-V, Ca-Cr best overall performance in TM series
  confidence: strong
  method_used: DFT NEB + thermodynamic analysis
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
- finding_text: Nanocrystalline layered MnOx with high defect concentration and lattice
    water demonstrates remarkable room-temperature Ca2+ electrochemical activity,
    achieving capacity of ~100-130 mAh/g. Atomic defects and lattice water are critical
    enablers of Ca2+ mobility in the oxide framework.
  construct_ids:
  - ca_intercalation_voltage
  - cathode_capacity
  - cation_disorder_energy
  direction: positive
  effect_size: ~100-130 mAh/g capacity for Ca2+ intercalation at room temperature
    in defective MnOx
  confidence: strong
  method_used: Experimental electrochemistry + XRD characterization
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
- finding_text: Slow Ca2+ kinetics in oxide electrodes is the primary bottleneck for
    Ca-ion batteries. High defect concentrations and structural water in nanocrystalline
    MnOx overcome this kinetic limitation, enabling room-temperature Ca intercalation
    that is not possible in well-ordered oxides.
  construct_ids:
  - ca_intercalation_voltage
  - li_diffusion_barrier
  - cation_disorder_energy
  direction: positive
  effect_size: Defective nanocrystals enable RT Ca2+ intercalation vs no activity
    in ordered phases
  confidence: strong
  method_used: Electrochemistry + structural characterization
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
- finding_text: Thermodynamic selectivity metrics derived from first-principles reaction
    energies across a 82,985-reaction chemical network successfully predict which
    synthesis routes for BaTiO3 yield the target phase with fewest impurities, as
    confirmed by synchrotron diffraction of 9 tested routes.
  construct_ids:
  - selectivity_metric
  - thermodynamic_selectivity
  - reaction_driving_force
  direction: positive
  effect_size: 3,520 reactions analyzed; 82,985-reaction network; 9 synthesis routes
    experimentally validated
  confidence: strong
  method_used: DFT thermodynamic calculations, synchrotron X-ray diffraction
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
- finding_text: Unconventional precursor combinations identified through selectivity
    analysis produce BaTiO3 faster with fewer impurities than the conventional BaCO3+TiO2
    route, demonstrating that complex chemistries in precursor selection substantially
    impact synthesis outcomes.
  construct_ids:
  - precursor_selection_score
  - selectivity_metric
  direction: positive
  effect_size: null
  confidence: strong
  method_used: Computational screening followed by experimental validation
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
- finding_text: Metathesis reactions enable rapid and selective synthesis of MgCr2S4
    thiospinel by engineering large thermodynamic driving forces through salt byproduct
    formation, bypassing the laborious traditional ceramic synthesis route.
  construct_ids:
  - metathesis_reaction_feasibility
  - reaction_driving_force
  - thermodynamic_selectivity
  direction: positive
  effect_size: 42 citations; selective formation of target phase confirmed by XRD
  confidence: strong
  method_used: Metathesis reaction design with DFT-computed driving forces
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
- finding_text: Precursor selection controls polymorph selectivity in solid-state
    synthesis by tuning reaction energy, which modulates critical nucleus size and
    surface energy contributions. For LiTiOPO4, different precursor sets selectively
    form different polymorphs via this mechanism.
  construct_ids:
  - polymorph_selectivity
  - precursor_selection_score
  - reaction_driving_force
  direction: conditional
  effect_size: null
  confidence: strong
  method_used: In situ characterization, DFT, nucleation theory
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
- finding_text: Surface energy plays a critical role in promoting nucleation of metastable
    phases during solid-state synthesis. When reaction energies are large, the metastable
    polymorph with lower surface energy can nucleate preferentially despite being
    higher in bulk free energy.
  construct_ids:
  - polymorph_selectivity
  - reaction_driving_force
  direction: conditional
  effect_size: null
  confidence: moderate
  method_used: null
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
- finding_text: A threshold of >=60 meV/atom energy difference between the most favorable
    initial product and competing phases defines the regime of thermodynamic control
    in solid-state reactions. Below this threshold, kinetic factors dominate product
    selection.
  construct_ids:
  - thermodynamic_control_threshold
  - thermodynamic_selectivity
  - reaction_driving_force
  direction: positive
  effect_size: '>=60 meV/atom threshold; 37 reactant pairs characterized in situ'
  confidence: strong
  method_used: In situ synchrotron characterization of 37 reactant pairs
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
- finding_text: Only 15% of possible solid-state reactions in the Materials Project
    database fall within the thermodynamic control regime where initial product formation
    can be predicted from first principles alone.
  construct_ids:
  - thermodynamic_control_threshold
  - thermodynamic_selectivity
  direction: positive
  effect_size: 15% of reactions under thermodynamic control; Materials Project database
    analysis
  confidence: strong
  method_used: Computational analysis of Materials Project reaction database
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
- finding_text: YBCO ceramic synthesis proceeds through sequential pairwise reactions
    at precursor interfaces. Substituting BaCO3 with BaO2 redirects the pathway through
    a low-temperature eutectic melt, reducing synthesis time from 12+ hours to 30
    minutes (24x speedup).
  construct_ids:
  - sequential_pairwise_mechanism
  - precursor_selection_score
  - synthesis_temperature
  direction: positive
  effect_size: 24x synthesis time reduction (12+ hours to 30 minutes)
  confidence: strong
  method_used: In situ XRD, electron microscopy, computational thermodynamics
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
- finding_text: Computational thermodynamics successfully identifies the most reactive
    precursor pair interfaces in heterogeneous powder mixtures, predicting the sequence
    of intermediate phase formation during ceramic synthesis.
  construct_ids:
  - sequential_pairwise_mechanism
  - reaction_driving_force
  direction: positive
  effect_size: null
  confidence: strong
  method_used: Computational thermodynamics validated by in situ XRD
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
- finding_text: Pair distribution function (PDF) analysis combined with cluster-expansion-based
    structural models accurately captures short-range cation ordering in disordered
    rocksalt cathodes. The approach was validated on neutron scattering data for Li-Mn-O-F
    DRX compositions.
  construct_ids:
  - short_range_order
  - cation_disorder_energy
  direction: positive
  effect_size: First-principles SRO models match experimental PDF data quantitatively
  confidence: strong
  method_used: Neutron PDF + cluster expansion modeling
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
- finding_text: Short-range order in DRX cathodes significantly deviates from perfect
    randomness and affects local bond lengths and site occupancies. Accurate structural
    models must account for SRO to correctly interpret diffraction and PDF data from
    these materials.
  construct_ids:
  - short_range_order
  - cation_disorder_energy
  direction: positive
  effect_size: null
  confidence: strong
  method_used: Cluster expansion + neutron PDF
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
- finding_text: Multiple synthesis routes targeting highly fluorinated DRX cathode
    Li1.2Mn0.4Ti0.4O1.6F0.4 were rationally designed using thermochemical analysis.
    MnF2 as a reactive fluorine source and alternative Li precursors (Li6MnO4, LiMnO2)
    were tested to avoid LiF formation that inhibits fluorination.
  construct_ids:
  - drx_fluorination_degree
  - cation_disorder_energy
  - cathode_capacity
  direction: positive
  effect_size: Rational precursor selection enables higher F incorporation than standard
    routes
  confidence: strong
  method_used: Thermochemical analysis + experimental synthesis
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
- finding_text: LiF formation during synthesis is the primary barrier to achieving
    high fluorination in DRX cathodes. Raising the F chemical potential through reactive
    fluoride precursors (MnF2) is more effective than using LiF directly as a fluorine
    source.
  construct_ids:
  - drx_fluorination_degree
  - formation_energy_per_atom
  direction: negative
  effect_size: LiF thermodynamic sink limits F incorporation; MnF2 circumvents this
  confidence: strong
  method_used: Thermodynamic analysis + multiple synthesis route comparison
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
- finding_text: r2SCAN meta-GGA with rVV10 van der Waals correction provides improved
    prediction of formation and decomposition enthalpies for solids compared to PBE-GGA.
    For 1000+ compounds tested, r2SCAN+rVV10 reduces MAE of formation enthalpies and
    improves phase stability predictions.
  construct_ids:
  - dft_functional_accuracy
  - formation_energy_per_atom
  - energy_above_hull
  direction: positive
  effect_size: Improved MAE for formation and decomposition enthalpies vs PBE and
    SCAN
  confidence: strong
  method_used: r2SCAN+rVV10 DFT benchmark on 1000+ compounds
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
- finding_text: r2SCAN restores numerical stability that was problematic in the original
    SCAN functional while maintaining similar accuracy for solid-state thermochemistry,
    making it suitable for high-throughput computational screening of materials stability.
  construct_ids:
  - dft_functional_accuracy
  - formation_energy_per_atom
  direction: positive
  effect_size: null
  confidence: strong
  method_used: Systematic DFT benchmark
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
- finding_text: Automated high-throughput comparison of r2SCAN and SCAN for 6,307
    solid materials reveals that r2SCAN achieves comparable accuracy to SCAN for formation
    energies and band gaps while being significantly more numerically stable, enabling
    reliable high-throughput workflows.
  construct_ids:
  - dft_functional_accuracy
  - formation_energy_per_atom
  direction: positive
  effect_size: 6,307 materials benchmarked; r2SCAN comparable accuracy to SCAN with
    better numerical stability
  confidence: strong
  method_used: Automated DFT workflow on 6,307 materials (PBE, SCAN, r2SCAN)
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
- finding_text: Computational screening of pyrochlore and spinel crystal structures
    identifies materials with predicted giant anomalous Hall effect, demonstrating
    the application of high-throughput DFT for functional property discovery beyond
    thermodynamic stability.
  construct_ids:
  - high_throughput_screening_yield
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: high_throughput_dft
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
- finding_text: Ca1.5Ba0.5Si5O3N6 is identified as a potential calcium solid-state
    conductor with partially occupied Ca sites enabling ion migration. Ab initio NEB
    calculations combined with neutron diffraction reveal the Ca migration mechanism
    through a 3D percolating pathway.
  construct_ids:
  - ca_ion_diffusion_barrier
  - ca_intercalation_voltage
  direction: positive
  effect_size: 3D percolating Ca migration pathway identified with partial Ca site
    occupancy
  confidence: moderate
  method_used: DFT-NEB + neutron diffraction
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
- finding_text: Development of Ca-ion batteries is largely limited by the low diffusion
    rate of divalent Ca2+ ions in solid-state materials. Understanding design principles
    for Ca2+ mobility requires identifying host structures with appropriate channel
    sizes and partial site occupancies.
  construct_ids:
  - ca_ion_diffusion_barrier
  - li_diffusion_barrier
  direction: negative
  effect_size: null
  confidence: strong
  method_used: Ab initio computation + neutron diffraction
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
- finding_text: Optimal solid-state synthesis heating temperatures correlate strongly
    with precursor material stability (melting points, formation energies) but show
    no direct correlation with thermodynamic features of the synthesis reaction itself,
    extending Tamman's rule from intermetallics to oxide systems.
  construct_ids:
  - synthesis_condition_prediction
  - synthesis_temperature
  - precursor_selection_score
  direction: positive
  effect_size: 68 citations; feature importance analysis on text-mined synthesis data
  confidence: strong
  method_used: ML on text-mined synthesis literature, feature importance analysis
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
- finding_text: Heating times in solid-state synthesis correlate with experimental
    procedures and instrument setups rather than material properties, suggesting potential
    human bias in reported synthesis conditions.
  construct_ids:
  - synthesis_condition_prediction
  direction: 'null'
  effect_size: null
  confidence: moderate
  method_used: ML feature importance analysis on text-mined data
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
- finding_text: A data-driven precursor recommendation system trained on 29,900 text-mined
    solid-state synthesis procedures achieves at least 82% success rate when providing
    top-5 precursor recommendations for 2,654 unseen target materials.
  construct_ids:
  - precursor_selection_score
  - synthesis_success_rate
  direction: positive
  effect_size: '>=82% success rate on 2,654 unseen materials; 29,900 training procedures'
  confidence: strong
  method_used: ML similarity learning on text-mined synthesis database
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
- finding_text: The ARROWS3 algorithm for autonomous precursor selection identifies
    effective precursor sets by learning which precursors form highly stable intermediates
    that prevent target formation, requiring substantially fewer iterations than black-box
    optimization across 3 experimental datasets with 200+ synthesis procedures.
  construct_ids:
  - precursor_selection_score
  - reaction_driving_force
  - synthesis_success_rate
  direction: positive
  effect_size: Validated on 200+ synthesis procedures across 3 datasets; fewer iterations
    than black-box optimization
  confidence: strong
  method_used: Domain-knowledge-informed optimization algorithm
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
- finding_text: Kinetically controlled solid-state metathesis between MnCl2 and nitrogen-containing
    precursors (Mg2NCl, Mg3N2) produces Mn3N2 at low temperatures via a solid-solution
    intermediate mechanism, enabling synthesis of metal nitrides inaccessible by conventional
    ceramic methods.
  construct_ids:
  - metathesis_reaction_feasibility
  - synthesis_temperature
  direction: positive
  effect_size: null
  confidence: strong
  method_used: Synchrotron XRD characterization of reaction pathways
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
- finding_text: Rate-limiting barriers for ion exchange reactions in solid-state synthesis
    are associated with the salt precursor (LiCl, LiBr) rather than the ceramic target
    material. Defect formation energy in LiBr is substantially lower than DFT predictions,
    also influencing rates.
  construct_ids:
  - ion_exchange_activation_energy
  - reaction_driving_force
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: In situ synchrotron studies, DFT comparison
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
- finding_text: Scaling relationships govern concentration-dependent reaction kinetics
    in lithium halide ion exchange, enabling predictions of conditions that could
    substantially accelerate ion exchange reactions through control of vacancy concentrations.
  construct_ids:
  - ion_exchange_activation_energy
  - synthesis_temperature
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: In situ synchrotron diffraction with varying reactant ratios
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
- finding_text: NaSICON-structured NaV2(PO4)3 demonstrates reversible dual Ca2+-Na+
    ion electrochemistry, with topotactic (de)intercalation of 0.6 mol Ca2+ alongside
    Na+ exchange. This establishes NaSICON as a viable cathode framework for Ca-ion
    batteries.
  construct_ids:
  - ca_intercalation_voltage
  - cathode_capacity
  direction: positive
  effect_size: 0.6 mol Ca2+ reversible intercalation in NaV2(PO4)3
  confidence: strong
  method_used: Electrochemistry + operando XRD
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
- finding_text: Ca-ion batteries are plagued by a paucity of suitable cathode materials.
    NaV2(PO4)3 with NASICON structure overcomes this by leveraging the rigid polyanion
    framework that provides channels for Ca2+ transport.
  construct_ids:
  - ca_intercalation_voltage
  - ca_ion_diffusion_barrier
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: Electrochemistry + phase stability analysis
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
- finding_text: CaB12H12 has a percolating Ca migration path with a low activation
    barrier of 650 meV, and can be doped with Al, Bi, or trivalent rare-earth cations
    to create vacancies and potentially improve conductivity for solid-state Ca batteries.
  construct_ids:
  - ca_ion_diffusion_barrier
  - mg_solid_electrolyte_conductivity
  direction: positive
  effect_size: 650 meV Ca migration barrier; dopable with Al, Bi, RE3+ cations
  confidence: moderate
  method_used: DFT-NEB migration barrier calculations
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
- finding_text: Large expansion of the CaFe2O4-type sodium postspinel phase space
    at ambient pressure achieved through systematic synthesis of NaCrTiO4, NaRhTiO4,
    NaCrSnO4, NaInSnO4, NaMgAlO4, and other new compositions. These tunnel-structured
    materials are prospective battery electrodes with Na+ in tunnel sites.
  construct_ids:
  - intercalation_voltage
  - formation_energy_per_atom
  direction: positive
  effect_size: 6+ new ambient-pressure Na-CF compounds synthesized
  confidence: strong
  method_used: Experimental solid-state synthesis + DFT
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
- finding_text: Computational approaches are emerging to accelerate battery materials
    synthesis, including thermodynamic selectivity analysis, precursor recommendation
    via ML, and autonomous experimental platforms. These techniques can predict synthesis
    conditions and identify optimal precursor sets for target battery phases.
  construct_ids:
  - formation_energy_per_atom
  - intercalation_voltage
  - cathode_capacity
  direction: positive
  effect_size: null
  confidence: foundational
  method_used: Literature review / perspective
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
- finding_text: Synthesis prediction for battery materials requires understanding
    both thermodynamic driving forces (which phases form) and kinetic barriers (reaction
    rates and temperatures). Current computational methods are strongest at predicting
    thermodynamic outcomes but kinetic prediction remains challenging.
  construct_ids:
  - formation_energy_per_atom
  - energy_above_hull
  direction: conditional
  effect_size: null
  confidence: foundational
  method_used: Review of computational synthesis prediction methods
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
- finding_text: Double-ion exchange (anion cometathesis) reactions enable perovskite
    LaMnO3 synthesis with reaction onset at 450-480C, compared to >1000C for traditional
    equilibrium synthesis. Lanthanum oxyhalide precursors achieve the lowest onset
    temperatures.
  construct_ids:
  - anion_cometathesis
  - metathesis_reaction_feasibility
  - synthesis_temperature
  direction: positive
  effect_size: Temperature reduction from >1000C to 450-480C (>50% reduction)
  confidence: strong
  method_used: Synchrotron XRD, computational thermodynamics
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
- finding_text: 'DFT accuracy for predicting solid stability depends critically on
    reaction type: PBE achieves MAE=70 meV/atom and SCAN achieves MAE=59 meV/atom
    for 1,012 compounds vs experiment, but for 231 compound-only reactions (no elemental
    phases), both functionals achieve ~35 meV/atom, matching experimental uncertainty.'
  construct_ids:
  - dft_prediction_accuracy
  - formation_energy_per_atom
  - energy_above_hull
  direction: positive
  effect_size: PBE MAE=70 meV/atom; SCAN MAE=59 meV/atom; compound-only reactions
    ~35 meV/atom; 56,791 compounds analyzed
  confidence: strong
  method_used: DFT (PBE, SCAN) benchmarking against experimental formation enthalpies
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
- finding_text: ML models using 25 electronic structure features can correct PBE-calculated
    formation enthalpies from MAE=195 meV/atom to MAE=80 meV/atom across 1,011 solid-state
    compounds. For highly ionic compounds (ionicity>0.22), PBE errors are systematically
    larger.
  construct_ids:
  - dft_functional_accuracy
  - ml_formation_energy_model
  - formation_energy_per_atom
  direction: positive
  effect_size: MAE reduced from 195 to 80 meV/atom for PBE; ionic compounds (I>0.22)
    have larger errors
  confidence: strong
  method_used: ML correction of DFT (PBE, SCAN) with 25 electronic structure features
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
- finding_text: Metathesis synthesis enables rapid and selective formation of MgCr2S4
    thiospinel cathode material by altering the thermodynamic landscape. Traditional
    ceramic synthesis of this Mg cathode material is laborious, but metathesis bypasses
    intermediate phases.
  construct_ids:
  - intercalation_voltage
  - formation_energy_per_atom
  direction: positive
  effect_size: Selective single-phase MgCr2S4 via metathesis vs multi-step ceramic
    route
  confidence: strong
  method_used: Metathesis synthesis + thermodynamic analysis
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
- finding_text: Review establishes that machine learning methods including neural
    networks, Gaussian process regression, and random forests can accelerate heterogeneous
    catalyst design by learning structure-property relationships from DFT datasets,
    reducing the need for expensive quantum-chemical calculations.
  construct_ids:
  - energy_prediction_mae
  - formation_energy_per_atom
  direction: positive
  effect_size: null
  confidence: strong
  method_used: literature_review
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
- finding_text: Application of the Gibbs energy descriptor to ~30,000 ICSD materials
    reveals the temperature-dependent scale of metastability and provides insights
    into how composition and temperature jointly affect materials synthesizability.
  construct_ids:
  - gibbs_energy_descriptor
  - energy_above_hull
  direction: positive
  effect_size: Phase diagrams generated for ~30,000 materials
  confidence: strong
  method_used: phase_diagram_construction
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
- finding_text: For 231 Type 2 reactions (involving only compounds, no elements),
    SCAN, PBE, and experiment agree within ~35 meV/atom, comparable to experimental
    uncertainty, suggesting DFT is highly accurate for compound-compound reaction
    thermodynamics.
  construct_ids:
  - dft_functional_accuracy
  - decomposition_enthalpy
  direction: positive
  effect_size: Agreement within ~35 meV/atom for compound-only decomposition reactions
  confidence: strong
  method_used: dft_benchmark
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
- finding_text: DFT and ML potentials predict negative hydrogen insertion energies
    for La0.5Sr0.5CoO3-delta, but convex hull analysis reveals protonated phases are
    thermodynamically unstable, decomposing into hydroxides and other products, explaining
    experimentally observed acid-etching during electrochemical cycling.
  construct_ids:
  - formation_energy_per_atom
  - energy_above_hull
  direction: negative
  effect_size: Negative insertion energies but unstable on convex hull
  confidence: moderate
  method_used: DFT, ML interatomic potentials, convex hull analysis
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
- finding_text: Thermodynamic selectivity analysis can be used prospectively to identify
    optimal precursor sets for synthesizing novel target materials, reducing the trial-and-error
    typically required for solid-state synthesis.
  construct_ids:
  - synthesis_selectivity_metric
  - pairwise_reaction_energy
  direction: positive
  effect_size: null
  confidence: strong
  method_used: Computational selectivity screening + experimental validation
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
- finding_text: In situ synchrotron studies reveal that rate-limiting barriers in
    Li-ion exchange reactions are commonly associated with the LiCl/LiBr salt reactants
    rather than the ceramic target, quantifying both thermodynamic activation energies
    and kinetic barriers for the salt processes.
  construct_ids:
  - li_diffusion_barrier
  - formation_energy_per_atom
  direction: conditional
  effect_size: Salt-side barriers rate-limiting rather than ceramic-side barriers
  confidence: strong
  method_used: In situ synchrotron XRD kinetic analysis
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
- finding_text: New ternary zinc molybdenum nitride compounds Zn3MoN4 and ZnMoN2 were
    predicted by theory and experimentally realized. These alloys form in a broad
    composition range in the wurtzite-derived structure, with redox-mediated stabilization
    enabling large off-stoichiometry accommodation.
  construct_ids:
  - formation_energy_per_atom
  - nitride_perovskite_formability
  direction: positive
  effect_size: Broad Zn3MoN4 to ZnMoN2 composition range stabilized by redox mechanism
  confidence: strong
  method_used: DFT prediction + experimental thin-film synthesis
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
- finding_text: A novel chemical looping process generating pure SO2 from raw sulfur
    and air is identified computationally, with 12 viable redox material combinations
    (2 supported by prior experimental evidence), potentially offering a more efficient,
    lower-emission route to sulfuric acid.
  construct_ids:
  - chemical_looping_material_viability
  - catalytic_loop_directionality
  direction: positive
  effect_size: 12 viable combinations; 2 experimentally supported
  confidence: moderate
  method_used: Thermodynamic process design coupled with materials screening
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
- finding_text: High-throughput computation of 3,881 potential NASICON phases identified
    stability rules based on a 2D descriptor combining cation properties. Five of
    six predicted NASICONs were successfully synthesized experimentally, validating
    the ab initio predictive capability.
  construct_ids:
  - nasicon_stability_descriptor
  - formation_energy_per_atom
  - energy_above_hull
  direction: positive
  effect_size: 3,881 phases screened; 5/6 predicted NASICONs synthesized successfully
    (83% success rate)
  confidence: strong
  method_used: High-throughput DFT + experimental validation + ML ranking
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
- finding_text: 'Thermochemical modeling identifies a narrow temperature window for
    fluorinated disordered rocksalt cathode synthesis: too low produces LiF intermediates
    that restrict fluorine availability, while temperatures above 848C (LiF melting
    point) cause LiF volatility limiting F solubility.'
  construct_ids:
  - synthesis_temperature
  - reaction_driving_force
  - precursor_selection_score
  direction: conditional
  effect_size: LiF melting point 848C defines upper temperature bound
  confidence: strong
  method_used: Thermochemical modeling, comprehensive characterization
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
- finding_text: Approximately two-thirds of decomposition reactions relevant to solid
    stability assessment contain no elemental phases. Correction schemes using fitted
    elemental reference energies provide negligible improvement for these majority
    reactions.
  construct_ids:
  - dft_prediction_accuracy
  - energy_above_hull
  direction: 'null'
  effect_size: ~67% of reactions contain no elemental phases; negligible improvement
    from corrections
  confidence: strong
  method_used: Statistical analysis of 56,791 phase diagram decomposition reactions
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
- finding_text: Diversifying training data composition improves ML predictions of
    thermodynamic properties for inorganic crystals more than simply increasing dataset
    size. A data-centric approach that balances chemical space representation yields
    more robust and generalizable formation energy models.
  construct_ids:
  - ml_formation_energy_model
  - formation_energy_per_atom
  direction: positive
  effect_size: Data diversity more impactful than data volume for ML accuracy
  confidence: strong
  method_used: Systematic ML benchmarking with varied training data
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
- finding_text: Partial dependence plot and GAM analysis reveals that compounds with
    high ionicity (I>0.22) have systematically larger DFT formation enthalpy errors,
    providing interpretable insight into where density functional approximations fail
    most significantly.
  construct_ids:
  - dft_functional_accuracy
  - formation_energy_per_atom
  direction: negative
  effect_size: Ionicity >0.22 correlates with largest DFT errors
  confidence: strong
  method_used: Interpretable ML (PDP+GAM analysis)
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
- finding_text: Li2MnP2S6, a new lithium metal thiophosphate synthesized via novel
    iodide-assisted route, shows electrochemical Li extraction at ~3 V, significantly
    higher than other sulfide cathodes. Mn and Fe analogs operate at similar voltages
    but through different redox mechanisms.
  construct_ids:
  - sulfide_cathode_voltage
  - intercalation_voltage
  - cathode_capacity
  direction: positive
  effect_size: ~3 V extraction voltage for Li2MnP2S6, higher than conventional sulfide
    cathodes
  confidence: strong
  method_used: Iodide-assisted synthesis + electrochemistry + DFT
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
- finding_text: Computational screening of ternary metal nitrides identified 209 stable
    and 847 metastable (within 100 meV/atom of convex hull) previously unreported
    nitride compounds, creating a comprehensive stability map of the ternary metal
    nitride chemical space.
  construct_ids:
  - energy_above_hull
  - high_throughput_screening_yield
  direction: positive
  effect_size: 209 stable + 847 metastable new nitrides identified
  confidence: strong
  method_used: high_throughput_dft
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
- finding_text: SISSO-identified physical descriptor predicts Gibbs free energy of
    stoichiometric inorganic compounds with ~50 meV/atom resolution across 300-1800K
    temperature range, enabling generation of thousands of temperature-dependent phase
    diagrams for ~30,000 known materials from the ICSD.
  construct_ids:
  - gibbs_energy_descriptor
  - formation_energy_per_atom
  direction: positive
  effect_size: MAE ~50 meV/atom (~1 kcal/mol) across 300-1800K
  confidence: strong
  method_used: sisso_descriptor_identification
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
- finding_text: For 646 non-trivial decomposition reactions assessed against 1012
    experimental formation enthalpies, PBE achieves MAD of 70 meV/atom and SCAN achieves
    MAD of 59 meV/atom, with commonly employed elemental reference energy corrections
    providing only ~2 meV/atom improvement.
  construct_ids:
  - dft_functional_accuracy
  - decomposition_enthalpy
  direction: positive
  effect_size: PBE MAD=70 meV/atom, SCAN MAD=59 meV/atom for decomposition reactions
  confidence: strong
  method_used: dft_benchmark
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
- finding_text: Computational precursor selection methods that incorporate thermodynamic
    reaction analysis are broadly applicable across battery material classes (Li-ion
    cathodes, solid electrolytes, all-solid-state batteries), though effectiveness
    varies and current methods have limitations requiring further development for
    synthesis-by-design.
  construct_ids:
  - precursor_selection_score
  - reaction_driving_force
  - synthesis_success_rate
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: Review and perspective
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
- finding_text: Four published ML synthesizability scores generally overestimate synthesis
    likelihood for hypothetical materials, but certain scoring approaches correlate
    with thermodynamic heuristics, assigning lower scores to materials lacking stability
    or available synthesis routes.
  construct_ids:
  - synthesis_prediction_calibration
  - synthesis_success_rate
  - energy_above_hull
  direction: conditional
  effect_size: General overestimation; partial correlation with thermodynamic metrics
  confidence: moderate
  method_used: CHGNet potential evaluation on Chemeleon-generated materials
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
- finding_text: Ab initio thermodynamics correctly predicts which pair of precursors
    has the most reactive interface in multicomponent ceramic synthesis. Solid-state
    synthesis proceeds through sequential pairwise reactions at interfaces, with the
    most exothermic pair reacting first.
  construct_ids:
  - pairwise_reaction_energy
  - formation_energy_per_atom
  direction: positive
  effect_size: Pairwise reaction energies correctly predict reaction sequence in ceramic
    synthesis
  confidence: strong
  method_used: Ab initio thermodynamics + in situ XRD
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
- finding_text: Although halide salts LiCl and LiBr are routinely used as Li sources
    for ion exchange reactions, the processes controlling their reaction rates were
    poorly understood. This work demonstrates that salt melting, dissolution, and
    diffusion through salt layers are quantifiable kinetic barriers.
  construct_ids:
  - li_diffusion_barrier
  - intercalation_voltage
  direction: positive
  effect_size: null
  confidence: strong
  method_used: In situ synchrotron powder XRD
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
- finding_text: Computational screening of 3,881 potential NASICON phases combined
    with a ML tolerance factor achieves 5 out of 6 successful synthesis attempts,
    demonstrating effective integration of stability prediction with experimental
    validation.
  construct_ids:
  - synthesis_success_rate
  - formation_energy_per_atom
  direction: positive
  effect_size: 83% synthesis success rate (5/6); 3,881 phases screened computationally
  confidence: strong
  method_used: DFT screening, ML tolerance factor, experimental synthesis
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
- finding_text: Comprehensive review establishes that computational prediction of
    inorganic solid stability has matured significantly with DFT functionals, correction
    schemes, and ML approaches, but systematic errors remain for reactions involving
    elemental phases and strongly correlated systems.
  construct_ids:
  - dft_prediction_accuracy
  - formation_energy_per_atom
  direction: conditional
  effect_size: 158 citations; comprehensive review of the field
  confidence: strong
  method_used: Literature review and synthesis
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
- finding_text: Imbalanced training data leads to biased ML predictions that perform
    well on common chemistries but poorly on underrepresented compositions, highlighting
    the need for active learning and targeted data collection strategies.
  construct_ids:
  - ml_formation_energy_model
  - formation_energy_per_atom
  direction: negative
  effect_size: null
  confidence: strong
  method_used: ML error analysis across chemical space
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
- finding_text: A comprehensive computational map of inorganic ternary metal nitrides
    identifies stable and metastable compositions across the full periodic table,
    revealing that nitride chemical space is far less explored than oxide space with
    many predicted-stable but unsynthesized compounds.
  construct_ids:
  - formation_energy_per_atom
  - energy_above_hull
  - nitride_perovskite_formability
  direction: positive
  effect_size: Hundreds of predicted-stable ternary nitrides not yet synthesized
  confidence: strong
  method_used: High-throughput DFT + convex hull analysis
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
- finding_text: 'Li2FeP2S6 and Li2MnP2S6 operate at similar ~3 V voltages but via
    fundamentally different redox mechanisms: Fe undergoes cation redox while Mn involves
    anion (sulfur) redox, as revealed by DFT electronic structure analysis.'
  construct_ids:
  - sulfide_cathode_voltage
  - intercalation_voltage
  direction: conditional
  effect_size: Same voltage (~3V) but Fe=cation redox, Mn=anion redox
  confidence: strong
  method_used: DFT electronic structure + experimental electrochemistry
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
- finding_text: Comprehensive review identifies that predicting thermodynamic stability
    of inorganic solids requires computing energy above the convex hull (decomposition
    enthalpy) rather than formation enthalpy alone, and that DFT accuracy at the meta-GGA
    level (SCAN, r2SCAN) provides ~50-70 meV/atom MAE for formation enthalpies.
  construct_ids:
  - energy_above_hull
  - decomposition_enthalpy
  - dft_functional_accuracy
  direction: positive
  effect_size: MAE ~50-70 meV/atom for meta-GGA formation enthalpies
  confidence: strong
  method_used: systematic_review
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
- finding_text: Analysis of 56,791 compounds shows that decomposition into elemental
    forms is rarely the competing reaction determining stability; approximately two-thirds
    of decomposition reactions involve no elemental phases, making formation enthalpy
    an incomplete metric for stability assessment.
  construct_ids:
  - decomposition_enthalpy
  - formation_energy_per_atom
  direction: negative
  effect_size: ~2/3 of decomposition reactions involve no elemental phases
  confidence: strong
  method_used: phase_diagram_analysis
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
- finding_text: MBE growth of rutile Sn1-xGexO2 achieves maximum 34% Ge incorporation
    at 600C, with DFT phase diagram analysis predicting spinodal decomposition beyond
    this concentration. Ge-rich rutile phase formation is suppressed by amorphization
    and GeO volatility.
  construct_ids:
  - synthesis_temperature
  - formation_energy_per_atom
  direction: conditional
  effect_size: 34% max Ge incorporation; spinodal decomposition limit at 600C
  confidence: strong
  method_used: MBE growth, DFT phase diagram, characterization
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
- finding_text: Limited negative training examples (materials that failed to synthesize)
    represent a fundamental challenge for ML synthesis prediction, as models cannot
    learn failure modes from databases that predominantly report successful syntheses.
  construct_ids:
  - synthesis_prediction_calibration
  - synthesis_success_rate
  direction: negative
  effect_size: null
  confidence: strong
  method_used: Systematic evaluation of ML model limitations
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
- finding_text: Two selectivity metrics (primary and secondary competition) quantify
    the thermodynamic favorability of target vs impurity phase formation in 3,520
    literature solid-state reactions. These metrics successfully rank synthesis approaches
    and predict which precursor combinations yield the purest products.
  construct_ids:
  - synthesis_selectivity_metric
  - formation_energy_per_atom
  - perovskite_decomposition_energy
  direction: positive
  effect_size: 3,520 reactions analyzed; selectivity metrics predict impurity formation
  confidence: strong
  method_used: Thermodynamic analysis of 3,520 literature reactions
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
- finding_text: Heterogeneous solid-state synthesis evolves through a complicated
    series of reaction intermediates determined by local interface thermodynamics,
    not bulk equilibrium. Modeling the most reactive interface pair enables understanding
    and prediction of the reaction pathway.
  construct_ids:
  - pairwise_reaction_energy
  - synthesis_selectivity_metric
  direction: positive
  effect_size: null
  confidence: strong
  method_used: In situ synchrotron XRD + DFT interface thermodynamics
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
- finding_text: The thermodynamics of proton insertion across the perovskite-brownmillerite
    structural transition in La0.5Sr0.5CoO3-delta are characterized, revealing how
    oxygen vacancy ordering and proton incorporation energetics govern the structural
    phase transition relevant to protonic ceramic applications.
  construct_ids:
  - proton_insertion_thermodynamics
  - perovskite_decomposition_energy
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: DFT thermodynamic calculations
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
- finding_text: A systematic thermodynamic methodology correctly classifies all 17
    experimentally tested redox materials for chemical looping and identifies over
    1,300 previously unstudied promising candidates, demonstrating scalable materials
    discovery for industrial redox processes.
  construct_ids:
  - chemical_looping_material_viability
  - thermochemical_cycle_efficiency
  direction: positive
  effect_size: 100% classification accuracy on 17 known materials; 1,300+ new candidates
    identified
  confidence: strong
  method_used: Thermodynamic equilibrium analysis, high-throughput screening
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
- finding_text: 'High-throughput thermodynamic screening of 1,148 nitride/metal oxide
    pairs for solar thermochemical ammonia synthesis identifies promising materials
    based on boron, vanadium, iron, and cerium through equilibrium analysis of four
    key reactions: hydrolysis, oxide reduction, nitrogen fixation, and nitride reformation.'
  construct_ids:
  - thermochemical_ammonia_yield
  - thermochemical_cycle_efficiency
  direction: positive
  effect_size: 1,148 pairs screened; 4 promising element families identified (B, V,
    Fe, Ce)
  confidence: moderate
  method_used: High-throughput Gibbs energy minimization, Materials Project DFT data
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
- finding_text: Microkinetic modeling predicts programmable oxide catalysts can boost
    OER current density by 100-600x at fixed overpotentials, or reduce the overpotential
    needed to achieve 10 mA/cm2 by 45-140% compared to optimal static catalysts.
  construct_ids:
  - programmable_catalyst_enhancement
  - oxygen_evolution_overpotential
  direction: positive
  effect_size: 100-600x current density boost; 45-140% overpotential reduction
  confidence: strong
  method_used: Microkinetic modeling of programmable oxide catalysts
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
- finding_text: Interpretable ML models can forecast the behavior of programmable
    catalytic loops, advancing the ability to predict and design dynamic catalytic
    systems beyond what microkinetic simulations alone can achieve.
  construct_ids:
  - catalytic_resonance_frequency
  - programmable_catalyst_enhancement
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: Interpretable machine learning on catalytic resonance simulations
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
- finding_text: Ensemble convolutional neural network trained on physics-informed
    augmented simulated diffraction spectra achieves exceptional accuracy for multi-phase
    mixture identification, exceeding previously reported methods based on profile
    matching and deep learning.
  construct_ids:
  - xrd_phase_identification_accuracy
  - neural_network_potential
  direction: positive
  effect_size: null
  confidence: strong
  method_used: ensemble_cnn
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
- finding_text: Adaptive XRD enables in situ identification of short-lived intermediate
    phases formed during solid-state reactions using a standard in-house diffractometer,
    a capability previously requiring synchrotron facilities.
  construct_ids:
  - xrd_phase_identification_accuracy
  - adaptive_measurement_efficiency
  - discovery_acceleration_factor
  direction: positive
  effect_size: null
  confidence: strong
  method_used: adaptive_xrd_with_ml
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
- finding_text: Heating times in solid-state synthesis are strongly correlated with
    experimental procedures and instrument setups rather than thermodynamic or kinetic
    properties, indicating significant human bias in reported synthesis durations.
  construct_ids:
  - synthesis_temperature_prediction
  direction: 'null'
  effect_size: null
  confidence: moderate
  method_used: feature_importance_analysis
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
- finding_text: A theoretical framework predicts and controls polymorph selectivity
    in solid-state reactions by using reaction energy as a handle for polymorph selection.
    Surface energy contributions at small particle sizes can tip the thermodynamic
    balance toward metastable polymorphs.
  construct_ids:
  - metastable_polymorph_selectivity
  - pairwise_reaction_energy
  - formation_energy_per_atom
  direction: positive
  effect_size: Reaction energy identified as key handle for metastable polymorph selection
  confidence: strong
  method_used: DFT thermodynamics + surface energy analysis + experimental validation
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
- finding_text: When reaction energies are large (strongly exothermic), thermodynamics
    primarily dictates the initial product formed regardless of stoichiometry. This
    principle enables predictive synthesis by selecting precursors that maximize thermodynamic
    driving force toward the target phase.
  construct_ids:
  - pairwise_reaction_energy
  - formation_energy_per_atom
  direction: positive
  effect_size: null
  confidence: strong
  method_used: In situ synchrotron characterization + DFT
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
- finding_text: A physically interpretable SISSO-derived descriptor accurately predicts
    Gibbs energies of inorganic crystalline solids as a function of temperature, enabling
    temperature-dependent phase stability predictions without expensive phonon calculations
    for thousands of compounds.
  construct_ids:
  - gibbs_energy_descriptor
  - formation_energy_per_atom
  direction: positive
  effect_size: Analytical Gibbs energy descriptor replaces phonon calculations for
    stability prediction
  confidence: strong
  method_used: SISSO descriptor learning + DFT validation
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
- finding_text: In situ characterization of 37 reactant pairs reveals a thermodynamic
    threshold below which the first intermediate phase formed is thermodynamically
    controlled regardless of stoichiometry. Above this threshold, kinetics dominates.
  construct_ids:
  - formation_energy_per_atom
  - energy_above_hull
  direction: conditional
  effect_size: Quantified thermodynamic vs kinetic control threshold
  confidence: strong
  method_used: In situ characterization of 37 reactant pairs
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
- finding_text: Ion exchange of known compounds outperforms generative AI (diffusion
    models, VAEs, LLMs) for discovering novel inorganic crystals. Random enumeration
    of charge-balanced prototypes also performs competitively against generative methods.
  construct_ids:
  - ml_formation_energy_model
  - energy_above_hull
  direction: 'null'
  effect_size: Ion exchange baseline beats diffusion, VAE, and LLM generators
  confidence: strong
  method_used: Benchmark of 4 generative models vs 2 baselines
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
- finding_text: A SISSO-derived descriptor accurately predicts Gibbs energies of inorganic
    solids as a function of temperature, enabling temperature-dependent phase stability
    predictions without expensive phonon calculations.
  construct_ids:
  - gibbs_energy_descriptor
  - formation_energy_per_atom
  direction: positive
  effect_size: Analytical descriptor replaces phonon calculations for G(T)
  confidence: strong
  method_used: SISSO descriptor learning + DFT
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
- finding_text: High-throughput thermodynamic screening using Gibbs energy models
    identified promising active materials for chemical looping from thousands of candidates,
    overcoming the scarcity of high-temperature thermochemical data.
  construct_ids:
  - gibbs_energy_descriptor
  - formation_energy_per_atom
  direction: positive
  effect_size: Thousands of chemical looping candidates screened
  confidence: strong
  method_used: High-throughput Gibbs energy screening
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
- finding_text: The O*-to-OOH* and O*-to-OH* activation barriers emerge as the critical
    parameters governing OER catalytic performance under dynamic forcing conditions,
    determining the optimal oscillation parameters for programmable catalysts.
  construct_ids:
  - programmable_catalyst_enhancement
  - oxygen_evolution_overpotential
  - catalytic_resonance_frequency
  direction: positive
  effect_size: null
  confidence: strong
  method_used: Microkinetic modeling, sensitivity analysis
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
- finding_text: ML-driven adaptive XRD can accurately detect trace amounts of materials
    in multi-phase mixtures with significantly shorter measurement times than conventional
    full-range scans, by steering measurements toward features that improve phase
    identification confidence.
  construct_ids:
  - xrd_phase_identification_accuracy
  - adaptive_measurement_efficiency
  direction: positive
  effect_size: null
  confidence: strong
  method_used: adaptive_xrd_with_ml
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
- finding_text: ML models trained on text-mined synthesis datasets reveal that optimal
    solid-state heating temperatures strongly correlate with precursor stability (melting
    points, formation energies), extending Tamman's rule from intermetallics to oxide
    systems and suggesting kinetics determine synthesis conditions.
  construct_ids:
  - synthesis_temperature_prediction
  - precursor_selection_score
  direction: positive
  effect_size: null
  confidence: strong
  method_used: random_forest_feature_importance
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
- finding_text: Using an 18-element chemical reaction network with Materials Project
    thermodynamic data, two unconventional BaTiO3 synthesis reactions using BaS/BaCl2
    and Na2TiO3 precursors were discovered that produce BaTiO3 faster and with fewer
    impurities than conventional methods.
  construct_ids:
  - reaction_selectivity_metric
  - precursor_selection_score
  - synthesis_success_rate
  direction: positive
  effect_size: 2 novel efficient routes from 82,985 enumerated reactions
  confidence: strong
  method_used: computational_reaction_screening
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
- finding_text: In situ characterization of 37 reactant pairs reveals a thermodynamic
    threshold below which the first intermediate phase formed is controlled by thermodynamics
    regardless of reactant stoichiometry. Above this threshold, kinetics becomes dominant.
  construct_ids:
  - pairwise_reaction_energy
  - synthesis_selectivity_metric
  - formation_energy_per_atom
  direction: conditional
  effect_size: Quantified thermodynamic vs kinetic control threshold from 37 experimental
    pairs
  confidence: strong
  method_used: In situ characterization of 37 reactant pairs
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
- finding_text: Generative AI for materials discovery has unclear advantages over
    traditional methods. Proper baseline comparisons are essential, and current generative
    models may be solving an easier problem than claimed when measured against simple
    composition/structure enumeration.
  construct_ids:
  - ml_formation_energy_model
  - energy_above_hull
  direction: 'null'
  effect_size: null
  confidence: strong
  method_used: Systematic benchmarking study
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
- finding_text: High-throughput thermodynamic screening using accurate Gibbs energy
    models identified promising active materials for chemical looping from thousands
    of candidates, demonstrating that computational materials screening can overcome
    the scarcity of high-temperature thermochemical data.
  construct_ids:
  - gibbs_energy_descriptor
  - formation_energy_per_atom
  direction: positive
  effect_size: Thousands of chemical looping candidates screened computationally
  confidence: strong
  method_used: High-throughput Gibbs energy screening
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
- finding_text: Catalytic resonance theory provides a framework for understanding
    circumfluence (directional flow patterns) in programmable catalytic loops, where
    forced oscillation of binding energies creates non-equilibrium steady states with
    enhanced catalytic throughput.
  construct_ids:
  - catalytic_loop_directionality
  - catalytic_resonance_frequency
  - programmable_catalyst_enhancement
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: Catalytic resonance theory, microkinetic modeling
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
- finding_text: Physics-informed perturbations (peak shifting, broadening, intensity
    variations) and hypothetical solid solution augmentation of training data dramatically
    improve robustness of XRD phase identification models to experimental artifacts
    from sample preparation and synthesis.
  construct_ids:
  - xrd_phase_identification_accuracy
  direction: positive
  effect_size: null
  confidence: strong
  method_used: data_augmentation
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
- finding_text: Data-driven precursor recommendation system using 29,900 text-mined
    solid-state synthesis recipes achieves at least 82% success rate when proposing
    five precursor sets for each of 2,654 unseen test target materials, learning chemical
    similarity to mimic human synthesis design.
  construct_ids:
  - precursor_selection_score
  - synthesis_success_rate
  direction: positive
  effect_size: 82% top-5 success rate on 2,654 unseen targets
  confidence: strong
  method_used: similarity_based_recommendation
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
- finding_text: Two new selectivity metrics (primary and secondary competition) for
    solid-state reactions, applied to 3520 literature reactions, correlate with observed
    target/impurity formation in synchrotron XRD characterization of reaction pathways.
  construct_ids:
  - reaction_selectivity_metric
  - thermodynamic_selectivity
  direction: positive
  effect_size: Validated on 3520 literature reactions + 9 experimental tests
  confidence: strong
  method_used: thermodynamic_reaction_network
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
- finding_text: Despite advances in predictive synthesis for solution-based techniques,
    there remained no methods to design solid-state reactions targeting metastable
    materials. This framework fills that gap by linking precursor choice to polymorph
    selectivity through reaction thermodynamics.
  construct_ids:
  - metastable_polymorph_selectivity
  - synthesis_selectivity_metric
  direction: positive
  effect_size: null
  confidence: strong
  method_used: Theoretical framework + experimental demonstration
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
- finding_text: Established methods such as ion exchange of known compounds outperform
    generative AI techniques (diffusion models, VAEs, LLMs) for discovering novel
    inorganic crystals when evaluated against proper baselines. Random enumeration
    of charge-balanced prototypes also performs competitively.
  construct_ids:
  - ml_formation_energy_model
  - formation_energy_per_atom
  - energy_above_hull
  direction: 'null'
  effect_size: Ion exchange baseline outperforms diffusion models, VAEs, and LLMs
    for crystal discovery
  confidence: strong
  method_used: Benchmark of 4 generative models vs 2 baselines (ion exchange, random
    enumeration)
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
- finding_text: Temperature-dependent materials chemistry including high-temperature
    phase transitions and decomposition can be predicted using the SISSO Gibbs energy
    descriptor, extending stability predictions beyond the 0K DFT energies that dominate
    current high-throughput screening.
  construct_ids:
  - gibbs_energy_descriptor
  - perovskite_decomposition_energy
  - formation_energy_per_atom
  direction: positive
  effect_size: null
  confidence: strong
  method_used: SISSO + experimental thermochemistry comparison
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
- finding_text: A theoretical framework predicts and controls polymorph selectivity
    in solid-state reactions by using reaction energy as a handle for polymorph selection,
    with surface energy contributions at small particle sizes tipping the balance
    toward metastable polymorphs.
  construct_ids:
  - metastable_polymorph_selectivity
  - formation_energy_per_atom
  direction: positive
  effect_size: Reaction energy as key handle for metastable polymorph selection
  confidence: strong
  method_used: DFT + surface energy analysis + experiment
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
- finding_text: ML approaches for heterogeneous catalyst design encompass descriptor-based
    methods, neural network potentials, and active learning, enabling systematic exploration
    of catalyst composition-structure-activity relationships at scales infeasible
    for first-principles calculations alone.
  construct_ids:
  - programmable_catalyst_enhancement
  - oxygen_evolution_overpotential
  direction: positive
  effect_size: 419 citations; comprehensive review establishing ML for catalysis as
    a field
  confidence: strong
  method_used: Literature review
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
- finding_text: Aluminum antisite disorder in iron aluminate spinels lowers cation
    vacancy formation energy from >3 eV to 0.62 eV when one-third of sites are inverted,
    making cation vacancy-mediated water splitting thermodynamically accessible and
    supporting hydrogen yields up to 361 umol/g.
  construct_ids:
  - cation_vacancy_water_splitting
  - thermochemical_cycle_efficiency
  direction: positive
  effect_size: Formation energy reduction from >3 eV to 0.62 eV; H2 yield up to 361
    umol/g
  confidence: strong
  method_used: DFT calculations, defect thermodynamics
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
- finding_text: Cation vacancies rather than conventional oxygen vacancies mediate
    redox cycling in iron aluminate spinel water splitting, representing a fundamentally
    different mechanism that explains experimental hydrogen yields not accountable
    by oxygen vacancy models alone.
  construct_ids:
  - cation_vacancy_water_splitting
  - thermochemical_cycle_efficiency
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: DFT defect calculations, comparison with experimental yields
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
- finding_text: Betti curves derived from persistent homology of electron density
    improve ML model performance by over 33 percentage points compared to models trained
    on raw electron density data for tasks including crystal structure classification,
    thermodynamic stability prediction, and metallic/nonmetallic distinction.
  construct_ids:
  - betti_curve_descriptor
  - persistent_homology_descriptor
  - topological_fingerprint_similarity
  direction: positive
  effect_size: '>33 percentage point improvement in classification accuracy'
  confidence: strong
  method_used: Persistent homology, ML classification/regression
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
- finding_text: Betti curve descriptors maintain comparable information content to
    full electron density representations while requiring substantially less computational
    data, offering an efficient low-dimensional encoding of bonding characteristics
    in crystalline solids.
  construct_ids:
  - betti_curve_descriptor
  - persistent_homology_descriptor
  direction: positive
  effect_size: null
  confidence: strong
  method_used: Information content analysis, dimensionality comparison
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
- finding_text: Decision tree models trained on text-mined BiFeO3 synthesis data (177
    articles, 331 procedures) identify experimental factors preventing impurity phases
    but have limited predictive capability because important features are frequently
    unreported in published literature.
  construct_ids:
  - text_mined_synthesis_database
  - synthesis_success_rate
  direction: conditional
  effect_size: 177 articles, 331 procedures; limited prediction due to missing features
  confidence: moderate
  method_used: Text mining, decision tree classification, experimental validation
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
- finding_text: r2SCAN predicts systematically larger lattice constants than SCAN
    across the ~6000 material benchmark set, a systematic shift that should be accounted
    for when comparing to experimental values or SCAN-computed databases.
  construct_ids:
  - dft_functional_accuracy
  direction: conditional
  effect_size: null
  confidence: moderate
  method_used: high_throughput_dft_benchmark
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
- finding_text: Established baseline methods like ion exchange are better than generative
    AI models at generating novel materials that are thermodynamically stable, although
    many of these closely resemble known compounds. Generative models excel at proposing
    novel structural frameworks.
  construct_ids:
  - generative_crystal_model
  - energy_above_hull
  direction: conditional
  effect_size: null
  confidence: strong
  method_used: benchmark_comparison
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
- finding_text: Machine learning interatomic potentials can accelerate the computation
    of surface phase diagrams for inorganic materials, enabling surface science studies
    at scales previously intractable with DFT alone, with applications in heterogeneous
    catalysis and thin film growth.
  construct_ids:
  - mlip_surface_prediction
  - neural_network_potential
  direction: positive
  effect_size: null
  confidence: strong
  method_used: mlip_surface_science
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
- finding_text: Systematic in situ synchrotron diffraction of Li+ ion exchange into
    Na2Mg2P3O9N using a novel high-throughput 2D detector setup enabled simultaneous
    study of many samples and precise quantification of kinetic rate constants for
    Li-ion exchange reactions.
  construct_ids:
  - li_diffusion_barrier
  - intercalation_voltage
  direction: positive
  effect_size: High-throughput kinetic rate constant extraction from time-dependent
    lattice evolution
  confidence: strong
  method_used: In situ synchrotron XRD with 2D area detector
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
- finding_text: Low-temperature anion cometathesis selectively synthesizes defect-rich
    LaMnO3 perovskite with controlled defect concentrations. The metathesis route
    provides a pathway to perovskite phases with tunable properties through defect
    engineering.
  construct_ids:
  - perovskite_formability
  - perovskite_decomposition_energy
  - pairwise_reaction_energy
  direction: positive
  effect_size: Selective defect-rich LaMnO3 at low temperature via cometathesis
  confidence: strong
  method_used: Anion cometathesis synthesis + structural characterization
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
- finding_text: ML-driven adaptive X-ray diffraction, coupling an ML algorithm with
    a physical diffractometer, reliably detects minor phase amounts in complex mixtures
    within shortened timeframes and enables in situ detection of transient phases
    during solid-state reactions using conventional laboratory equipment.
  construct_ids:
  - automated_phase_identification
  - topological_fingerprint_similarity
  direction: positive
  effect_size: 67 citations; minor phase detection in shortened timeframes on lab
    equipment
  confidence: strong
  method_used: ML-guided adaptive XRD measurements
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
- finding_text: ML-driven adaptive XRD reliably detects minor phases in complex mixtures
    and enables in situ detection of transient phases during solid-state reactions
    using conventional laboratory equipment.
  construct_ids:
  - automated_phase_identification
  - topological_fingerprint_similarity
  direction: positive
  effect_size: 67 citations; minor phase detection on lab equipment
  confidence: strong
  method_used: ML-guided adaptive XRD measurements
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
- finding_text: Thermodynamic assessment of ML models for solid-state synthesis prediction
    reveals that current models have uneven performance across composition space and
    reaction types. Proper thermodynamic evaluation frameworks are needed to assess
    synthesis prediction reliability.
  construct_ids:
  - ml_formation_energy_model
  - synthesis_selectivity_metric
  - formation_energy_per_atom
  direction: conditional
  effect_size: null
  confidence: moderate
  method_used: Systematic ML model evaluation for synthesis prediction
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
- finding_text: High-throughput computation of 3881 potential NASICON phases yielded
    a machine-learned 2D tolerance factor that classifies NASICON phases by synthetic
    accessibility. Predictive capability validated by successful synthesis of 5 out
    of 6 attempted materials.
  construct_ids:
  - nasicon_tolerance_factor
  - synthesis_success_rate
  - high_throughput_screening_yield
  direction: positive
  effect_size: 5/6 (83%) synthesis validation rate
  confidence: strong
  method_used: sisso_feature_selection
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
- finding_text: Diversifying training data is important for making balanced predictions
    of thermodynamic properties for inorganic crystals; data-centric approaches improve
    ML model generalization across chemical space.
  construct_ids:
  - formation_energy_per_atom
  - energy_prediction_mae
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: data_centric_ml
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
- finding_text: Electronic structure calculations of GdRu2X2 (X=Si,Ge,Sn) reveal antibonding
    instabilities that drive structural distortions, identifying a new pathway toward
    centrosymmetric altermagnets. This demonstrates how electronic structure analysis
    can predict structural instabilities in intermetallic phases.
  construct_ids:
  - formation_energy_per_atom
  - energy_above_hull
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: DFT electronic structure analysis
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
- finding_text: High-throughput computational screening of pyrochlore and spinel structures
    identifies candidates with giant anomalous Hall effect, demonstrating the power
    of crystal-structure-targeted screening for discovering materials with specific
    electronic transport properties.
  construct_ids:
  - formation_energy_per_atom
  - energy_above_hull
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: High-throughput DFT Berry phase calculations
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
- finding_text: An ensemble CNN trained on simulated XRD spectra with physics-informed
    augmentations achieves automated identification of complex multi-phase mixtures
    from experimental X-ray diffraction data, critical for autonomous synthesis characterization
    workflows.
  construct_ids:
  - ml_formation_energy_model
  - perovskite_formability
  direction: positive
  effect_size: Automated multi-phase XRD interpretation for autonomous synthesis
  confidence: strong
  method_used: Ensemble CNN on simulated+augmented XRD spectra
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
- finding_text: Reproduction of 9 literature syntheses for BiFeO3 with incomplete
    parameter information reveals that text-mined datasets can guide controlled experiments
    and identify unreported but critical synthesis variables.
  construct_ids:
  - text_mined_synthesis_database
  direction: positive
  effect_size: 9 literature syntheses reproduced
  confidence: moderate
  method_used: Experimental reproduction guided by text-mined data
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
- finding_text: r2SCAN predicts formation energies more accurately than both SCAN
    and PBEsol for ~6000 solid materials, including both strongly and weakly bound
    systems, while requiring modestly fewer computational resources and offering significantly
    more reliable convergence.
  construct_ids:
  - dft_functional_accuracy
  - formation_energy_per_atom
  direction: positive
  effect_size: r2SCAN more accurate than SCAN and PBEsol across ~6000 materials
  confidence: strong
  method_used: high_throughput_dft_benchmark
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
- finding_text: r2SCAN+rVV10 van der Waals correction predicts slightly more accurate
    cell volumes but marginally less accurate formation enthalpies compared to bare
    r2SCAN, whereas SCAN+rVV10 worsens SCAN formation enthalpies.
  construct_ids:
  - dft_functional_accuracy
  direction: conditional
  effect_size: null
  confidence: moderate
  method_used: dft_benchmark
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
- finding_text: When sufficient training data is available, generative models can
    more effectively target properties such as electronic band gap and bulk modulus
    compared to baseline approaches, suggesting generative methods have unique value
    for property-targeted discovery.
  construct_ids:
  - generative_crystal_model
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: benchmark_comparison
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
- finding_text: Betti curves retain comparable information content to full electron
    density (measured by Shannon entropy) while requiring 2 orders of magnitude less
    data, making them efficient descriptors for materials property prediction.
  construct_ids:
  - topological_descriptor
  - crystal_graph_representation
  direction: positive
  effect_size: 100x data compression with comparable Shannon entropy
  confidence: strong
  method_used: information_theory_analysis
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
- finding_text: High-throughput thermodynamic screening of 1,148 metal nitride/metal
    oxide pairs for solar thermochemical ammonia synthesis (STAS) identified promising
    redox candidates. The screening leveraged accurate Gibbs energy models to evaluate
    materials at high-temperature operating conditions.
  construct_ids:
  - gibbs_energy_descriptor
  - formation_energy_per_atom
  - nitride_perovskite_formability
  direction: positive
  effect_size: 1,148 nitride/oxide pairs screened for STAS viability
  confidence: strong
  method_used: High-throughput thermodynamic screening of 1,148 pairs
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
- finding_text: Betti curves as topological descriptors compress electron densities
    into compact representations that capture bonding characteristics. These descriptors
    outperform traditional composition and structure features for predicting certain
    material properties, introducing a new class of electron-density-based features
    for materials ML.
  construct_ids:
  - topological_electron_density_descriptor
  - ml_formation_energy_model
  direction: positive
  effect_size: Betti curves capture bonding info missed by composition/structure descriptors
  confidence: moderate
  method_used: Persistent homology (Betti curves) + ML benchmarking
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
- finding_text: A probabilistic neural network ensemble trained on simulated XRD spectra
    with physics-based perturbations outperforms profile matching and conventional
    ML approaches for automated multi-phase diffraction interpretation, with a branching
    algorithm that explores suspected phase combinations to strengthen prediction
    reliability.
  construct_ids:
  - automated_phase_identification
  - topological_fingerprint_similarity
  direction: positive
  effect_size: 94 citations; superior to profile matching and conventional ML
  confidence: strong
  method_used: Probabilistic deep learning ensemble, simulated training data with
    physics perturbations
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
- finding_text: A probabilistic neural network ensemble trained on simulated XRD spectra
    with physics-based perturbations outperforms profile matching and conventional
    ML for automated multi-phase diffraction interpretation.
  construct_ids:
  - automated_phase_identification
  - topological_fingerprint_similarity
  direction: positive
  effect_size: 94 citations; superior to profile matching and conventional ML
  confidence: strong
  method_used: Probabilistic deep learning ensemble
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
- finding_text: Machine learning interatomic potentials (MLIPs) accelerate prediction
    of inorganic surface properties by orders of magnitude compared to DFT, enabling
    surface energy calculations and surface reconstruction studies for materials where
    surface properties dictate functionality.
  construct_ids:
  - ml_formation_energy_model
  - formation_energy_per_atom
  direction: positive
  effect_size: Orders of magnitude speedup over DFT for surface predictions
  confidence: strong
  method_used: MLIP surface energy benchmarking vs DFT
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
- finding_text: Wide band gap alkaline-earth chalcogenides show complex alloying behavior
    with potential for band gap engineering. The study maps the composition-structure-property
    relationships relevant to optoelectronic applications.
  construct_ids:
  - halide_perovskite_bandgap
  - formation_energy_per_atom
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: DFT alloying thermodynamics
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
- finding_text: Triple-alkali perovskites Cs2[Alk]+[TM]3+Cl6 identified as a class
    with remarkable optical properties including large and tunable exciton binding
    energies, with properties strongly influenced by sublattice mixing between Alk-Cl
    and TM-Cl sublattices.
  construct_ids:
  - tolerance_factor_prediction
  - high_throughput_screening_yield
  direction: positive
  effect_size: null
  confidence: strong
  method_used: gw_bse_calculations
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
- finding_text: No analogous ionicity-dependent error trend is observed for SCAN-calculated
    formation enthalpies, explaining why ML correction works better for PBE (systematic
    errors) than SCAN (more random errors).
  construct_ids:
  - ml_dft_error_correction
  - dft_functional_accuracy
  direction: 'null'
  effect_size: null
  confidence: moderate
  method_used: pdp_gam_analysis
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
- finding_text: Redox-mediated stabilization mechanisms in zinc molybdenum nitrides
    demonstrate that internal electron transfer between metal cations can thermodynamically
    stabilize otherwise metastable nitride phases, providing an alternative pathway
    to achieve phase stability beyond conventional energetic arguments.
  construct_ids:
  - formation_energy_per_atom
  - reaction_driving_force
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: Synthesis, characterization, DFT calculations
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
- finding_text: Multi-modal integration of text mining, in situ characterization,
    and ab initio calculations provides complementary insights into BiFeO3 crystallization
    pathways that no single method achieves alone, establishing a template for literature-experiment-computation
    synthesis rationalization.
  construct_ids:
  - text_mined_synthesis_database
  - persistent_homology_descriptor
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: Text mining, in situ characterization, DFT calculations
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
- finding_text: Average absolute errors in predicted formation enthalpies decrease
    by a factor of 1.5 to 2.5 from the GGA level to the meta-GGA level (r2SCAN/SCAN),
    with r2SCAN improving over SCAN specifically for intermetallic systems.
  construct_ids:
  - dft_functional_accuracy
  - formation_energy_per_atom
  direction: positive
  effect_size: 1.5-2.5x error reduction from GGA to meta-GGA
  confidence: strong
  method_used: dft_benchmark
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
- finding_text: Post-generation screening through stability and property filters from
    pre-trained ML models (including universal interatomic potentials) leads to substantial
    improvement in success rates of ALL methods (both baseline and generative), providing
    a practical low-cost pathway to more effective materials discovery.
  construct_ids:
  - generative_crystal_model
  - post_generation_screening
  - neural_network_potential
  direction: positive
  effect_size: null
  confidence: strong
  method_used: mlip_screening
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
- finding_text: ML models trained on Betti curve topological descriptors outperform
    those trained on raw electron densities by an average of 33 percentage points
    in classifying structure prototypes, predicting thermodynamic stability, and distinguishing
    metals from nonmetals.
  construct_ids:
  - topological_descriptor
  - energy_above_hull
  direction: positive
  effect_size: 33 percentage point improvement over raw electron density
  confidence: strong
  method_used: topological_data_analysis
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
- finding_text: Kinetically controlled solid-state metathesis reactions achieve selective
    low-temperature synthesis of Mn3N2, overcoming the typical problem that high-temperature
    approaches cause N2 gas release. Controlling reaction exothermicity through precursor
    choice prevents activation of deleterious competing pathways.
  construct_ids:
  - pairwise_reaction_energy
  - formation_energy_per_atom
  direction: positive
  effect_size: Low-temperature selective Mn3N2 synthesis via kinetic control
  confidence: strong
  method_used: Kinetically controlled metathesis synthesis
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
- finding_text: Machine learning methods for heterogeneous catalyst design enable
    rapid screening of catalyst candidates by learning structure-activity relationships
    from computational and experimental data. The review establishes best practices
    for ML in materials discovery.
  construct_ids:
  - ml_formation_energy_model
  direction: positive
  effect_size: null
  confidence: foundational
  method_used: Literature review of ML for catalysis
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
- finding_text: Electronic structure analysis of Li2FeS2 reveals distinct cation and
    anion redox mechanisms operating during Li extraction. Understanding these redox
    mechanisms is critical for designing sulfide cathodes with both high voltage and
    high capacity.
  construct_ids:
  - sulfide_cathode_voltage
  - intercalation_voltage
  - cathode_capacity
  direction: positive
  effect_size: Distinct cation vs anion redox pathways identified in Li2FeS2
  confidence: moderate
  method_used: DFT electronic structure analysis
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
- finding_text: ML-derived tolerance factor tau screened 903 Cs2BB'Cl6 double perovskites
    down to 311 likely stable candidates; first-principles calculations then identified
    261 as likely synthesizable (decomposition enthalpy <0.05 eV/atom) with 47 having
    direct band gaps between 1-3 eV.
  construct_ids:
  - tolerance_factor_prediction
  - energy_above_hull
  - high_throughput_screening_yield
  direction: positive
  effect_size: 903 -> 311 -> 261 synthesizable -> 47 with target band gaps
  confidence: strong
  method_used: tolerance_factor_plus_dft
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
- finding_text: ML model reduces PBE formation enthalpy errors from MAE of 195 meV/atom
    to 80 meV/atom. Interpretable analysis reveals compounds with high ionicity (I>0.22)
    have PBE errors twice as large as low-ionicity compounds (246 vs 113 meV/atom).
  construct_ids:
  - ml_dft_error_correction
  - dft_functional_accuracy
  - formation_energy_per_atom
  direction: positive
  effect_size: PBE MAE reduced from 195 to 80 meV/atom; ionicity threshold I=0.22
  confidence: strong
  method_used: interpretable_ml_correction
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
- finding_text: Phase evolution in multicomponent ceramic synthesis (demonstrated
    for YBCO) can be modeled as sequential pairwise interfacial reactions. Using BaO2
    instead of traditional BaCO3 precursor enables YBCO synthesis in 30 minutes vs
    12+ hours, rationalized by pairwise reaction thermodynamics.
  construct_ids:
  - pairwise_reaction_model
  - precursor_selection_score
  - synthesis_success_rate
  direction: positive
  effect_size: '24x speedup: 30 min vs 12+ hours for YBCO synthesis'
  confidence: strong
  method_used: in_situ_xrd_plus_dft
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
- finding_text: ML models trained on text-mined solid-state synthesis data predict
    synthesis conditions (temperature, atmosphere, precursors) for inorganic materials.
    Feature importance analysis reveals that thermodynamic properties and ionic radii
    are the most predictive features for synthesis temperature.
  construct_ids:
  - ml_formation_energy_model
  - synthesis_selectivity_metric
  direction: positive
  effect_size: Thermodynamic properties and ionic radii most predictive of synthesis
    T
  confidence: strong
  method_used: ML on text-mined synthesis dataset + feature importance analysis
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
- finding_text: A materials similarity metric learned from 29,900 text-mined synthesis
    recipes enables automatic precursor recommendation for novel target materials.
    The ML model learns which precursors are interchangeable and which are essential
    from the scientific literature.
  construct_ids:
  - synthesis_selectivity_metric
  - ml_formation_energy_model
  direction: positive
  effect_size: 29,900 recipes used to learn precursor interchangeability
  confidence: strong
  method_used: ML materials similarity from 29,900 text-mined recipes
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
- finding_text: Growth dynamics of rutile Sn1-xGexO2 films studied by MBE and DFT
    reveal composition-dependent growth mechanisms. Film composition and thickness
    are controlled by growth conditions rationalized through DFT surface energy and
    defect formation calculations.
  construct_ids:
  - formation_energy_per_atom
  direction: positive
  effect_size: null
  confidence: strong
  method_used: MBE growth + DFT surface energy calculations
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
- finding_text: The revised tolerance factor tau, a data-derived descriptor combining
    ionic radii and oxidation states, classifies perovskite stability with 92.2% accuracy
    across 576 ABX3 compounds, substantially outperforming the Goldschmidt tolerance
    factor (74%).
  construct_ids:
  - tolerance_factor_prediction
  direction: positive
  effect_size: 92.2% accuracy vs 74% for Goldschmidt factor on 576 compounds
  confidence: strong
  method_used: statistical_learning
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
- finding_text: Computational mapping of the inorganic ternary metal nitride stability
    landscape using DFT identifies numerous previously unknown stable and metastable
    phases, providing a roadmap for experimental synthesis of novel nitride materials.
  construct_ids:
  - formation_energy_per_atom
  - energy_above_hull
  - synthesis_success_rate
  direction: positive
  effect_size: null
  confidence: strong
  method_used: DFT stability calculations, ML screening
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
- finding_text: The ARROWS3 algorithm automates precursor selection for solid-state
    synthesis by actively learning from experimental outcomes to dynamically update
    precursor recommendations. The algorithm outperforms static computational predictions
    by incorporating feedback from synthesis attempts.
  construct_ids:
  - synthesis_selectivity_metric
  - pairwise_reaction_energy
  direction: positive
  effect_size: Dynamic precursor selection outperforms static computational prediction
  confidence: strong
  method_used: Active learning algorithm (ARROWS3) + experimental synthesis
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
- finding_text: DFT reveals that AlN hydrolysis proceeds through hydroxyl-mediated
    surface proton hopping, with the proton hopping mechanism being the rate-determining
    step. This atomistic understanding explains AlN's degradation in water and informs
    protective coating strategies.
  construct_ids:
  - formation_energy_per_atom
  direction: positive
  effect_size: Proton hopping identified as rate-determining step for AlN hydrolysis
  confidence: strong
  method_used: DFT surface reaction pathway analysis
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
- finding_text: Conventional materials discovery approaches (random charge-balanced
    prototype enumeration, data-driven ion exchange) outperform generative AI models
    (diffusion, VAE, LLM) at producing novel stable materials, though generative models
    better identify novel structural designs when targeting specific properties.
  construct_ids:
  - synthesis_success_rate
  - formation_energy_per_atom
  - energy_above_hull
  direction: conditional
  effect_size: null
  confidence: strong
  method_used: Systematic comparison of generative vs conventional baselines
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
- finding_text: In situ synchrotron studies of LiCl and LiBr ion exchange reactions
    precisely quantify thermodynamic activation energies for solid-state reactions.
    LiCl rate is limited by ion hopping barrier, while LiBr rate is also affected
    by defect formation energy substantially lower than DFT predictions.
  construct_ids:
  - thermodynamic_selectivity
  - synthesis_temperature_prediction
  direction: positive
  effect_size: null
  confidence: strong
  method_used: in_situ_synchrotron_xrd
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
- finding_text: When multiple phases have comparable thermodynamic driving force to
    form, initial product is determined by kinetic factors rather than thermodynamics.
    Analysis of Materials Project data shows 15% of possible reactions fall within
    the regime of thermodynamic control.
  construct_ids:
  - thermodynamic_control_threshold
  - thermodynamic_selectivity
  direction: conditional
  effect_size: 15% of reactions under thermodynamic control
  confidence: strong
  method_used: computational_thermodynamic_analysis
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
- finding_text: CHGNet foundation potential used to compute thermodynamic properties
    for thousands of hypothetical materials generated by the Chemeleon generative
    model, demonstrating the utility of MLIPs as rapid thermodynamic filters for generative
    materials discovery.
  construct_ids:
  - neural_network_potential
  - generative_crystal_model
  - post_generation_screening
  direction: positive
  effect_size: null
  confidence: strong
  method_used: chgnet_screening
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
- finding_text: Sublattice mixing in halide double perovskites provides a thermodynamically
    accessible route to modulate optoelectronic properties, with DFT-computed mixing
    energies predicting experimental miscibility ranges for designing targeted compositions.
  construct_ids:
  - formation_energy_per_atom
  - thermodynamic_selectivity
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: DFT calculations, experimental characterization
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
- finding_text: First-principles calculations of calcium ion diffusion in Ca1.5Ba0.5Si5O3N6
    nitridosilicate characterize migration barriers and identify preferred diffusion
    pathways, informing design of solid-state calcium-ion conductors.
  construct_ids:
  - formation_energy_per_atom
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: DFT nudged elastic band calculations
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
- finding_text: Decision tree models trained on 331 manually extracted sol-gel synthesis
    procedures for BiFeO3 reinforce important experimental heuristics for impurity
    avoidance but show limited predictive capability due to many important synthesis
    features being unreported in the literature.
  construct_ids:
  - text_mined_synthesis_data
  - synthesis_success_rate
  direction: conditional
  effect_size: 331 synthesis procedures from 177 articles
  confidence: moderate
  method_used: decision_tree_on_text_mined_data
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
- finding_text: Mn-rich disordered rocksalts exhibit similar phase transformation
    to spinel-like phase as ordered layered structures, leading to improved capacity
    and Li-ion transport kinetics, discovered through large-scale charge-informed
    MLIP simulations.
  construct_ids:
  - charge_informed_mlip
  - neural_network_potential
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: chgnet_simulation
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
- finding_text: Domain knowledge incorporation (understanding that stable intermediates
    block target formation) substantially outperforms black-box optimization for precursor
    selection, highlighting the importance of physically-informed optimization in
    autonomous synthesis platforms.
  construct_ids:
  - precursor_selection_score
  - reaction_driving_force
  - thermodynamic_selectivity
  direction: positive
  effect_size: null
  confidence: strong
  method_used: Comparison of domain-informed vs black-box optimization
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
- finding_text: The potential for programmable catalysts to fundamentally break scaling
    relations that limit static catalyst performance for OER, achieving performance
    regimes inaccessible to any fixed-composition catalyst.
  construct_ids:
  - programmable_catalyst_enhancement
  - oxygen_evolution_overpotential
  - catalytic_resonance_frequency
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: Microkinetic modeling beyond scaling relation constraints
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
- finding_text: DFT screening of MgLn2X4 spinels identifies 7 chalcogenide spinels
    with low Mg migration barriers (<380 meV) that are stable or nearly stable (within
    50 meV/atom of hull). Increasing lanthanoid size improves Mg mobility but decreases
    spinel stability.
  construct_ids:
  - energy_above_hull
  - high_throughput_screening_yield
  direction: conditional
  effect_size: 7 candidates with migration barriers <380 meV and Ehull <50 meV/atom
  confidence: strong
  method_used: dft_screening
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
- finding_text: Machine learning-guided adaptive XRD measurements make on-the-fly
    decisions during diffraction experiments to achieve optimal measurement effectiveness
    for autonomous phase identification. This brings ML interpretation in-line with
    experiments for rapid learning.
  construct_ids:
  - ml_formation_energy_model
  - perovskite_formability
  direction: positive
  effect_size: Real-time ML-driven measurement optimization for phase ID
  confidence: strong
  method_used: ML-guided adaptive XRD + autonomous experimentation
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
- finding_text: Decision tree models trained on 331 text-mined BiFeO3 sol-gel synthesis
    procedures identify key experimental heuristics for avoiding phase impurities
    but show limited predictive capability, indicating that synthesis outcome prediction
    requires features beyond those typically reported in papers.
  construct_ids:
  - synthesis_selectivity_metric
  - ml_formation_energy_model
  - perovskite_formability
  direction: conditional
  effect_size: 331 procedures; key heuristics identified but limited predictive power
  confidence: moderate
  method_used: Decision tree ML on 331 text-mined synthesis procedures
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
- finding_text: r2SCAN meta-GGA functional predicts formation energies of ~6,000 solid
    materials more accurately than PBEsol while achieving significantly more reliable
    convergence than SCAN, establishing it as preferred for large-scale computational
    materials screening.
  construct_ids:
  - dft_prediction_accuracy
  - formation_energy_per_atom
  direction: positive
  effect_size: ~6,000 materials benchmarked; better accuracy than PBEsol; better convergence
    than SCAN
  confidence: strong
  method_used: Automated high-throughput DFT workflow
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
- finding_text: Post-generation filtering using ML stability predictions and universal
    interatomic potentials substantially enhances generative materials discovery success
    rates while maintaining computational efficiency.
  construct_ids:
  - synthesis_prediction_calibration
  - energy_above_hull
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: ML post-generation filtering pipeline
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
- finding_text: Varying relative amounts of reactants identifies rate-limiting reagent
    and elucidates a universal scaling relationship controlling concentration dependence
    of reaction rate. Global fits across doped/undoped salts probe both intrinsic
    and extrinsic vacancy concentrations.
  construct_ids:
  - thermodynamic_selectivity
  - precursor_selection_score
  direction: positive
  effect_size: null
  confidence: strong
  method_used: in_situ_synchrotron_kinetics
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
- finding_text: Four recently published ML synthesizability prediction models generally
    overpredict the likelihood of synthesis when assessed against computed thermodynamics
    (CHGNet-computed Ehull and thermodynamic selectivity of synthesis reactions).
  construct_ids:
  - synthesis_prediction_calibration
  - energy_above_hull
  direction: negative
  effect_size: null
  confidence: strong
  method_used: thermodynamic_assessment
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
- finding_text: By altering the thermodynamic landscape through metathesis, rapid
    and selective synthesis of MgCr2S4 thiospinel (a Mg-cathode material) is achieved,
    replacing laborious traditional ceramic synthesis routes with a thermodynamically
    controlled approach.
  construct_ids:
  - metathesis_driving_force
  - thermodynamic_selectivity
  - precursor_selection_score
  direction: positive
  effect_size: null
  confidence: strong
  method_used: metathesis_synthesis
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
- finding_text: A data-centric approach to ML for inorganic materials demonstrates
    that improving training data quality (cleaning, augmentation, better representations)
    yields larger performance gains than architectural changes to ML models, establishing
    data quality as the primary bottleneck.
  construct_ids:
  - dft_prediction_accuracy
  - synthesis_prediction_calibration
  direction: positive
  effect_size: null
  confidence: strong
  method_used: Systematic data-centric vs model-centric comparison
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
- finding_text: Computational screening of chalcogenide spinel conductors identifies
    thermodynamically stable candidates for all-solid-state Mg batteries, with stability
    against decomposition being a critical filter that eliminates the majority of
    candidate compositions.
  construct_ids:
  - formation_energy_per_atom
  - energy_above_hull
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: DFT stability calculations, ionic conductivity evaluation
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
- finding_text: High-throughput computational screening using tolerance factor and
    thermochemical stability criteria, followed by high-throughput thin film growth,
    successfully discovered two entirely new nitride perovskites CeWN3 and CeMoN3,
    demonstrating the effectiveness of combined computational-experimental discovery
    pipelines.
  construct_ids:
  - tolerance_factor_prediction
  - high_throughput_screening_yield
  - synthesis_success_rate
  direction: positive
  effect_size: 2 new perovskite nitrides discovered and synthesized
  confidence: strong
  method_used: ht_screening_plus_thin_film_growth
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
- finding_text: Reproduction attempts of 9 literature syntheses with varying degrees
    of missing synthesis parameters demonstrate how text-mined datasets can inform
    controlled experiments and improve understanding of impurity phase formation in
    complex oxide systems.
  construct_ids:
  - text_mined_synthesis_data
  - synthesis_success_rate
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: experimental_reproduction
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
- finding_text: Thermodynamic analysis reveals that chalcogenide perovskites are substantially
    less stable than their oxide and halide counterparts, with tolerance factor predictions
    showing poor agreement with first-principles stability calculations for this materials
    class.
  construct_ids:
  - tolerance_factor_prediction
  - decomposition_enthalpy
  - energy_above_hull
  direction: negative
  effect_size: null
  confidence: strong
  method_used: dft_thermodynamic_analysis
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
- finding_text: Aluminum nitride hydrolysis proceeds through hydroxyl-mediated surface
    proton hopping rather than direct water dissociation, with DFT-computed activation
    barriers explaining the observed temperature-dependent degradation kinetics.
  construct_ids:
  - reaction_driving_force
  - synthesis_temperature
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: DFT surface calculations, kinetic modeling
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
- finding_text: Combined computational stability prediction and experimental synthesis
    expands the known ambient-pressure phase space of CaFe2O4-type sodium postspinel
    compounds, demonstrating predictive synthesis guided by DFT energy calculations.
  construct_ids:
  - formation_energy_per_atom
  - energy_above_hull
  - synthesis_success_rate
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: DFT prediction followed by experimental synthesis
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
- finding_text: Formation enthalpy prediction errors decrease by factors of 1.5 to
    2.5 when advancing from GGA (PBE) to meta-GGA (r2SCAN/SCAN) density functionals
    for over 1,000 solid materials, with r2SCAN balancing numerical stability with
    high accuracy.
  construct_ids:
  - dft_prediction_accuracy
  - formation_energy_per_atom
  direction: positive
  effect_size: 1.5-2.5x error reduction from GGA to meta-GGA; 1000+ solids tested
  confidence: strong
  method_used: DFT benchmarking against experimental formation enthalpies
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
- finding_text: Computational approaches for guiding precursor selection in solid-state
    battery materials synthesis are reviewed, covering Li-ion cathodes and solid electrolytes.
    Methods show effectiveness but limitations remain in predicting optimal synthesis
    routes for complex multicomponent materials.
  construct_ids:
  - precursor_selection_score
  - synthesis_success_rate
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: systematic_review
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
- finding_text: 'In situ characterization of 37 reactant pairs reveals a threshold
    for thermodynamic control in solid-state reactions: initial product formation
    can be predicted when its driving force exceeds all competing phases by at least
    60 meV/atom.'
  construct_ids:
  - thermodynamic_control_threshold
  - thermodynamic_selectivity
  direction: positive
  effect_size: 'Threshold: >=60 meV/atom advantage for thermodynamic prediction'
  confidence: strong
  method_used: in_situ_characterization
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
- finding_text: Some ML synthesizability model scores do trend with thermodynamic
    heuristics, assigning lower scores to materials that are less stable or lack thermodynamically
    selective synthesis routes, suggesting partial but incomplete alignment with physical
    principles.
  construct_ids:
  - synthesis_prediction_calibration
  - thermodynamic_selectivity
  - neural_network_potential
  direction: conditional
  effect_size: null
  confidence: moderate
  method_used: chgnet_thermodynamic_comparison
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
- finding_text: High-throughput DFT screening successfully identifies two new Ce-based
    nitride perovskites (CeMoN3 and CeWN3) that are subsequently experimentally synthesized,
    demonstrating that computational stability predictions can directly guide discovery
    of novel inorganic phases.
  construct_ids:
  - formation_energy_per_atom
  - energy_above_hull
  - synthesis_success_rate
  direction: positive
  effect_size: 2 new phases predicted and realized experimentally
  confidence: strong
  method_used: High-throughput DFT screening followed by experimental synthesis
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
- finding_text: Chalcogenide perovskites exhibit fundamental thermodynamic instability
    arising from the mismatch between chalcogenide anion size/polarizability and perovskite
    structural requirements, explaining why many computationally predicted phases
    remain experimentally inaccessible.
  construct_ids:
  - formation_energy_per_atom
  - energy_above_hull
  - thermodynamic_selectivity
  direction: negative
  effect_size: null
  confidence: moderate
  method_used: DFT calculations, thermodynamic analysis
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
- finding_text: A competing fluorite-family phase was identified for both CeWN3 and
    CeMoN3 systems, hypothesized to be a transient intermediate phase during crystallization
    from amorphous precursor. Different processing routes demonstrated to overcome
    this competing phase.
  construct_ids:
  - decomposition_enthalpy
  - synthesis_success_rate
  direction: conditional
  effect_size: null
  confidence: moderate
  method_used: thin_film_characterization
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
- finding_text: CHGNet charge-informed MLIP enables modeling of Mn valence-dependent
    migration and charge disproportionation during orthorhombic LixMnO2 to spinel
    transformation, providing atomic-level insights into cathode electrochemistry
    that require charge-aware interatomic potentials.
  construct_ids:
  - charge_informed_mlip
  - neural_network_potential
  - force_field_mae
  direction: positive
  effect_size: null
  confidence: strong
  method_used: chgnet_molecular_dynamics
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
- finding_text: Novel iodide-assisted synthesis route enables synthesis of Li2MP2S6
    thiophosphates including the new compound Li2MnP2S6, which operates at ~3V (significantly
    higher than typical sulfide cathodes) via a redox mechanism involving significant
    anionic redox participation.
  construct_ids:
  - synthesis_success_rate
  - precursor_selection_score
  direction: positive
  effect_size: ~3V operation for sulfide cathode (vs ~2V typical)
  confidence: strong
  method_used: novel_synthesis_route
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
- finding_text: Chemical similarity patterns learned from 29,900 literature synthesis
    procedures capture decades of experimental knowledge mathematically, enabling
    automated precursor recommendation that mimics expert chemist reasoning for synthesis
    design.
  construct_ids:
  - precursor_selection_score
  - text_mined_synthesis_database
  direction: positive
  effect_size: null
  confidence: strong
  method_used: Materials similarity learning from text-mined literature
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
- finding_text: A general methodology is established to quantify conditions under
    which metastable polymorphs become experimentally accessible through solid-state
    synthesis, based on critical nucleus size ratios determined by reaction energies
    and surface energy differences.
  construct_ids:
  - polymorph_selectivity
  - thermodynamic_control_threshold
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: Classical nucleation theory combined with DFT energetics
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
- finding_text: DFT calculations reveal that phase separation into Na-rich and Ca-rich
    NASICON phases limits Ca2+ electrochemistry capacity, and Na+ ions in host materials
    assist migration of neighboring Ca2+ ions, providing design principles for Ca-ion
    battery cathodes.
  construct_ids:
  - energy_above_hull
  - decomposition_enthalpy
  direction: conditional
  effect_size: null
  confidence: moderate
  method_used: dft_phase_diagram
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
- finding_text: Novel high-throughput in situ synchrotron studies using 2D area detector
    enable simultaneous monitoring of many ion exchange reactions. Kinetic rate constants
    extracted from time-dependent lattice parameter evolution reveal ion exchange
    rates are limited by ion transport in the salt rather than the ceramic host.
  construct_ids:
  - adaptive_measurement_efficiency
  - synthesis_success_rate
  direction: positive
  effect_size: null
  confidence: strong
  method_used: in_situ_synchrotron_xrd
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
- finding_text: Ab initio and machine learned models enable rapid computational screening
    of materials for solar thermal water splitting, combining thermodynamic and kinetic
    assessments to identify promising candidates from large materials databases.
  construct_ids:
  - high_throughput_screening_yield
  - formation_energy_per_atom
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: ml_plus_dft_screening
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
- finding_text: The thermodynamic driving force from salt byproduct formation in metathesis
    reactions can be engineered to selectively target specific products, with the
    magnitude of the driving force directly controlling which competing phases form
    preferentially.
  construct_ids:
  - metathesis_reaction_feasibility
  - reaction_driving_force
  - thermodynamic_selectivity
  direction: positive
  effect_size: null
  confidence: strong
  method_used: DFT reaction energy calculations, metathesis synthesis
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
- finding_text: Gibbs energy descriptors computed from a statistically-learned model
    combined with Materials Project DFT data enable high-throughput equilibrium prediction
    for multi-step thermochemical cycles, identifying promising redox pairs for solar
    ammonia synthesis based on B, V, Fe, and Ce.
  construct_ids:
  - thermochemical_ammonia_yield
  - chemical_looping_material_viability
  direction: positive
  effect_size: 1,148 pairs evaluated; B, V, Fe, Ce families identified
  confidence: moderate
  method_used: High-throughput Gibbs energy minimization
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
- finding_text: Systematic first-principles evaluation of layered transition metal
    oxides as calcium intercalation cathodes reveals trade-offs between voltage, thermodynamic
    stability, and Ca2+ mobility, with few candidates satisfying all requirements
    simultaneously.
  construct_ids:
  - formation_energy_per_atom
  - energy_above_hull
  direction: conditional
  effect_size: null
  confidence: moderate
  method_used: Systematic DFT screening
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
- finding_text: Subgroup discovery and compressed sensing methods (SISSO) can identify
    interpretable patterns, correlations, and descriptors in materials data, providing
    physically meaningful feature selection for property prediction that outperforms
    black-box ML approaches for certain materials properties.
  construct_ids:
  - gibbs_energy_descriptor
  - formation_energy_per_atom
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: sisso_subgroup_discovery
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
- finding_text: Large expansion of known Na-CaFe2O4 postspinel phase space demonstrated
    through systematic synthesis of 17 new compositions at ambient pressure. Stability
    trends explained by crystal chemistry and DFT, showing even strongly Jahn-Teller
    active cations can form Na-CFs when combined with larger Sn4+.
  construct_ids:
  - synthesis_success_rate
  - decomposition_enthalpy
  - high_throughput_screening_yield
  direction: positive
  effect_size: 17 new ambient-pressure compositions synthesized
  confidence: strong
  method_used: systematic_synthesis_plus_dft
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
- finding_text: Integration of text mining, in situ XRD characterization, and ab initio
    calculations rationalizes BiFeO3 crystallization pathways, demonstrating how multi-modal
    data fusion can guide understanding of complex synthesis processes.
  construct_ids:
  - text_mined_synthesis_data
  - xrd_phase_identification_accuracy
  - thermodynamic_selectivity
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: multimodal_data_fusion
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
- finding_text: First-principles study of alloying behavior in wide band gap alkaline-earth
    chalcogenides reveals phase stability trends and band gap engineering opportunities
    in this semiconductor materials class.
  construct_ids:
  - energy_above_hull
  - formation_energy_per_atom
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: dft_alloy_analysis
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
- finding_text: The A-Lab's closed-loop system integrates computational predictions,
    robotic powder handling, automated furnace operation, and ML-based XRD analysis.
    Failed synthesis attempts trigger adaptive recipe modification, demonstrating
    genuine autonomous learning from experimental outcomes.
  construct_ids:
  - synthesis_success_rate
  - adaptive_measurement_efficiency
  - discovery_acceleration_factor
  direction: positive
  effect_size: null
  confidence: strong
  method_used: closed_loop_autonomous_synthesis
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
- finding_text: First-principles calculations identify CaB12H12 as a potential solid-state
    Ca conductor with low migration barriers, demonstrating how computational screening
    can discover new solid-state ionic conductors for beyond-lithium battery technologies.
  construct_ids:
  - high_throughput_screening_yield
  - energy_above_hull
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: dft_screening
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
- finding_text: The ternary nitride stability map reveals that transition metal nitrides
    dominate the stable compositions, with alkaline earth and rare earth elements
    providing the most stable ternary nitride host lattices, providing chemical design
    rules for nitride materials discovery.
  construct_ids:
  - formation_energy_per_atom
  - energy_above_hull
  - high_throughput_screening_yield
  direction: positive
  effect_size: null
  confidence: strong
  method_used: high_throughput_dft
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
- finding_text: Feature importance analysis reveals optimal heating temperatures correlate
    with both melting points and formation energies (delta-Gf, delta-Hf) of precursor
    materials, extending Tamman's rule to oxide systems and suggesting reaction kinetics
    are governed by precursor decomposition rather than product formation thermodynamics.
  construct_ids:
  - synthesis_temperature_prediction
  - precursor_selection_score
  - text_mined_synthesis_data
  direction: positive
  effect_size: null
  confidence: strong
  method_used: random_forest_feature_importance
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
- finding_text: Combined theoretical and experimental study unravels growth dynamics
    of rutile Sn1-xGexO2, demonstrating how DFT phase diagrams can guide understanding
    of thin film growth thermodynamics and kinetics for novel semiconductor alloys.
  construct_ids:
  - energy_above_hull
  - decomposition_enthalpy
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: dft_plus_experiment
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
- finding_text: 'The importance of considering complex chemistries with additional
    elements during precursor selection is demonstrated: unconventional precursors
    containing elements not present in the target product (e.g., Na2TiO3 for BaTiO3)
    can enable superior synthesis routes via thermodynamic selectivity.'
  construct_ids:
  - reaction_selectivity_metric
  - precursor_selection_score
  direction: positive
  effect_size: null
  confidence: strong
  method_used: reaction_network_analysis
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
- finding_text: 'Review identifies key ML strategies for catalyst discovery: (1) learning
    adsorption energy scaling relations to avoid explicit DFT calculations, (2) transfer
    learning from bulk properties to surface reactivity, (3) Bayesian optimization
    for active learning in catalyst design space.'
  construct_ids:
  - energy_prediction_mae
  - high_throughput_screening_yield
  direction: positive
  effect_size: null
  confidence: strong
  method_used: literature_review
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
- finding_text: The A-Lab autonomous laboratory successfully synthesized 41 of 58
    targeted inorganic compounds (71% success rate) over 17 days without human intervention,
    using ML-guided precursor selection, robotic synthesis, and automated XRD characterization.
  construct_ids:
  - synthesis_success_rate
  - precursor_selection_score
  - xrd_phase_identification_accuracy
  - discovery_acceleration_factor
  direction: positive
  effect_size: 41/58 (71%) success rate in 17 days unattended
  confidence: strong
  method_used: autonomous_robotic_synthesis
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
- finding_text: 'Review identifies key components needed for autonomous materials
    synthesis platforms: (1) robotic synthesis and characterization automation, (2)
    ML for phase identification from XRD/characterization data, (3) active learning
    optimization algorithms for closed-loop experimental design.'
  construct_ids:
  - synthesis_success_rate
  - xrd_phase_identification_accuracy
  - discovery_acceleration_factor
  direction: positive
  effect_size: null
  confidence: strong
  method_used: systematic_review
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
- finding_text: Thermodynamics of proton insertion across the perovskite-brownmillerite
    structural transition in La0.5Sr0.5CoO3-delta reveals how vacancy ordering and
    proton incorporation compete thermodynamically, with implications for protonic
    ceramic electrochemical cells.
  construct_ids:
  - decomposition_enthalpy
  - energy_above_hull
  direction: conditional
  effect_size: null
  confidence: moderate
  method_used: dft_thermodynamics
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
- finding_text: The NASICON machine-learned tolerance factor is based on just two
    descriptors combining Na content, elemental radii, electronegativities, and Madelung
    energy, demonstrating that synthetic accessibility can be captured by physically
    interpretable low-dimensional descriptors.
  construct_ids:
  - nasicon_tolerance_factor
  - tolerance_factor_prediction
  direction: positive
  effect_size: null
  confidence: strong
  method_used: sisso_feature_selection
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
- finding_text: Random enumeration of charge-balanced prototypes serves as a surprisingly
    competitive baseline for crystal structure generation, highlighting that current
    generative models have not yet clearly surpassed simple combinatorial approaches
    for discovering stable novel materials.
  construct_ids:
  - generative_crystal_model
  - energy_above_hull
  direction: 'null'
  effect_size: null
  confidence: strong
  method_used: baseline_comparison
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
- finding_text: CHGNet is pre-trained on the Materials Project Trajectory dataset
    (MPtrj) containing 1.58M structures with energies, forces, stresses, and magnetic
    moments from GGA/GGA+U DFT calculations, making it a universal potential for charge-informed
    atomistic modeling.
  construct_ids:
  - neural_network_potential
  - charge_informed_mlip
  - crystal_graph_representation
  direction: positive
  effect_size: Pre-trained on 1.58M structures from MPtrj
  confidence: strong
  method_used: graph_neural_network
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
- finding_text: Direct observation via in situ XRD and TEM confirms that sequential
    pairwise interfacial reactions model correctly predicts non-equilibrium intermediate
    phases during YBCO synthesis, validating ab initio thermodynamics as a tool for
    understanding and optimizing complex ceramic synthesis.
  construct_ids:
  - pairwise_reaction_model
  - xrd_phase_identification_accuracy
  - thermodynamic_selectivity
  direction: positive
  effect_size: null
  confidence: strong
  method_used: in_situ_xrd_tem
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
- finding_text: 'Perspective identifies three key computational methods for guiding
    precursor selection: (1) thermodynamic selectivity metrics from reaction networks,
    (2) ML precursor recommendation from text-mined data, and (3) kinetic modeling
    of pairwise reactions, each with distinct applicability to Li-ion cathodes vs
    solid electrolytes.'
  construct_ids:
  - precursor_selection_score
  - reaction_selectivity_metric
  - pairwise_reaction_model
  direction: positive
  effect_size: null
  confidence: moderate
  method_used: systematic_review
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
- finding_text: The branching algorithm for multi-phase mixture identification exploits
    the probabilistic nature of the ensemble CNN to systematically explore suspected
    mixtures and identify the set of phases maximizing prediction confidence, achieving
    higher accuracy than single-pass classification.
  construct_ids:
  - xrd_phase_identification_accuracy
  direction: positive
  effect_size: null
  confidence: strong
  method_used: probabilistic_branching_algorithm
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
- finding_text: Betti curves from persistent homology capture bonding characteristics
    by encoding connected components, cycles, and voids across electron density thresholds,
    providing a mathematically rigorous compression of the 3D electron density into
    a 1D representation.
  construct_ids:
  - topological_descriptor
  - crystal_graph_representation
  direction: positive
  effect_size: null
  confidence: strong
  method_used: persistent_homology
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
- finding_text: The classical Goldschmidt tolerance factor t = (r_A + r_X) / sqrt(2)(r_B
    + r_X) achieves only 74% classification accuracy for perovskite vs non-perovskite
    ABX3 compositions across 576 experimental data points, significantly underperforming
    the revised tau (92% accuracy).
  construct_ids:
  - goldschmidt_tolerance_factor
  - perovskite_formability
  direction: positive
  effect_size: 74% accuracy (AUC), vs 92% for revised tau
  confidence: strong
  method_used: logistic_regression
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
- finding_text: The octahedral factor mu shows a clear lower bound of ~0.41 for perovskite
    formability — compositions with mu below this threshold almost never form stable
    perovskite structures, providing a useful necessary-but-not-sufficient screening
    criterion.
  construct_ids:
  - octahedral_factor
  - perovskite_formability
  direction: positive
  effect_size: Lower bound mu >= 0.41 for perovskite formation
  confidence: moderate
  method_used: statistical_analysis
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
- finding_text: CHGNet achieves energy MAE of 30 meV/atom, force MAE of 77 meV/A,
    and stress MAE of 0.462 GPa on the MPtrj dataset, while also predicting magnetic
    moments to enable charge-informed atomistic modeling across the periodic table.
  construct_ids:
  - neural_network_potential
  - energy_prediction_mae
  - force_field_mae
  - charge_informed_mlip
  direction: positive
  effect_size: Energy MAE=30 meV/atom, Force MAE=77 meV/A, Stress MAE=0.462 GPa
  confidence: strong
  method_used: graph_neural_network
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
- finding_text: Analysis of electronic instabilities in GdRu2X2 compounds reveals
    how antibonding interactions drive structural phase transitions, demonstrating
    the role of electronic structure in determining materials stability beyond simple
    energy-based metrics.
  construct_ids:
  - energy_above_hull
  - decomposition_enthalpy
  direction: conditional
  effect_size: null
  confidence: moderate
  method_used: dft_electronic_structure
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
- finding_text: The review identifies that ML models trained on DFT formation energies
    (e.g., graph neural networks, random forests) can predict formation energy with
    MAE of 20-50 meV/atom depending on architecture and training data, approaching
    the intrinsic uncertainty of the DFT reference data itself.
  construct_ids:
  - energy_prediction_mae
  - formation_energy_per_atom
  - neural_network_potential
  direction: positive
  effect_size: ML MAE of 20-50 meV/atom for formation energy prediction
  confidence: strong
  method_used: literature_review
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
- finding_text: Validation across 37 reactant pairs establishes that when no single
    phase has a driving force advantage exceeding 60 meV/atom over competitors, kinetic
    factors (diffusion, interface geometry) dominate initial product selection, making
    thermodynamic prediction unreliable in this regime.
  construct_ids:
  - thermodynamic_control_threshold
  - pairwise_reaction_model
  direction: negative
  effect_size: Below 60 meV/atom advantage, kinetics dominate
  confidence: strong
  method_used: in_situ_characterization
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
- finding_text: The precursor recommendation system learns chemical similarity of
    materials from 29,900 text-mined recipes and refers synthesis of new targets to
    precedent procedures of similar materials, effectively encoding decades of heuristic
    synthesis knowledge in a mathematical form for use in recommendation engines.
  construct_ids:
  - precursor_selection_score
  - text_mined_synthesis_data
  direction: positive
  effect_size: 29,900 recipes from scientific literature encoded
  confidence: strong
  method_used: similarity_based_recommendation
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
- finding_text: 'New approach to assess ML synthesizability models introduced: using
    thermodynamic bounds from successful synthesis recipes to determine likely limits
    beyond which materials are unlikely to be synthesized, providing a principled
    evaluation framework in the absence of extensive negative examples.'
  construct_ids:
  - synthesis_prediction_calibration
  - energy_above_hull
  - thermodynamic_selectivity
  direction: positive
  effect_size: null
  confidence: strong
  method_used: thermodynamic_bound_analysis
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
- finding_text: For a few classes of systems -- transition metals, intermetallics,
    weakly bound solids, and decomposition reactions into compounds -- GGA-level functionals
    are comparable to meta-GGAs, suggesting the extra computational cost of meta-GGA
    may not always be justified.
  construct_ids:
  - dft_functional_accuracy
  - decomposition_enthalpy
  direction: 'null'
  effect_size: null
  confidence: moderate
  method_used: dft_benchmark
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
- finding_text: The SISSO-derived Gibbs energy descriptor uses only formation enthalpy,
    volume per atom, and a temperature-dependent correction term, achieving remarkable
    accuracy with minimal computational cost compared to full phonon calculations
    or molecular dynamics simulations.
  construct_ids:
  - gibbs_energy_descriptor
  direction: positive
  effect_size: null
  confidence: strong
  method_used: sisso_descriptor_identification
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
- finding_text: Varying relative reactant amounts identifies rate-limiting reagent
    and reveals a universal scaling relationship controlling concentration dependence
    of solid-state reaction rates, providing a framework to predict conditions that
    can accelerate ion exchange reactions by orders of magnitude.
  construct_ids:
  - thermodynamic_selectivity
  - synthesis_success_rate
  - discovery_acceleration_factor
  direction: positive
  effect_size: Orders of magnitude acceleration predicted from scaling relationship
  confidence: strong
  method_used: in_situ_synchrotron_kinetics
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
- finding_text: For 231 compound-only decomposition reactions (Type 2), theory-experiment
    agreement within ~35 meV/atom is comparable to experimental uncertainty, establishing
    that DFT is effectively exact for predicting relative stability among competing
    compound phases.
  construct_ids:
  - dft_functional_accuracy
  - decomposition_enthalpy
  direction: positive
  effect_size: ~35 meV/atom agreement, comparable to experimental uncertainty
  confidence: strong
  method_used: dft_benchmark
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
- finding_text: The Goldschmidt tolerance factor t requires separate parameterizations
    for oxide vs halide perovskites and fails to capture the stability of many halide
    perovskites that fall outside the traditional 0.8 < t < 1.0 range.
  construct_ids:
  - goldschmidt_tolerance_factor
  - perovskite_formability
  direction: negative
  effect_size: null
  confidence: strong
  method_used: logistic_regression
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
- finding_text: Review establishes that learned interatomic potentials trained on
    DFT data for bulk phases can be applied to study surfaces with reasonable accuracy,
    but surface-specific training data and fine-tuning improve predictions for surface
    reconstructions and adsorbate interactions.
  construct_ids:
  - mlip_surface_prediction
  - neural_network_potential
  - force_field_mae
  direction: conditional
  effect_size: null
  confidence: moderate
  method_used: literature_review
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
- finding_text: 'Current computational synthesis guidance methods have limitations:
    thermodynamic approaches assume equilibrium which may not hold during rapid reactions,
    ML models require sufficient text-mined training data which is sparse for novel
    material classes, and kinetic models are computationally expensive for multicomponent
    systems.'
  construct_ids:
  - reaction_selectivity_metric
  - text_mined_synthesis_data
  - pairwise_reaction_model
  direction: negative
  effect_size: null
  confidence: moderate
  method_used: critical_analysis
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
- finding_text: By coupling ML algorithm with physical diffractometer, adaptive XRD
    integrates diffraction and analysis such that early experimental information steers
    measurements toward features improving phase identification confidence, reducing
    total measurement time while maintaining or improving accuracy.
  construct_ids:
  - adaptive_measurement_efficiency
  - xrd_phase_identification_accuracy
  - discovery_acceleration_factor
  direction: positive
  effect_size: null
  confidence: strong
  method_used: adaptive_experimental_design
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
- finding_text: Decomposition enthalpy threshold of <0.05 eV/atom used as a practical
    criterion for likely synthesizability in the double perovskite screening, with
    compounds below this threshold considered thermodynamically accessible under typical
    synthesis conditions.
  construct_ids:
  - decomposition_enthalpy
  - synthesis_success_rate
  - energy_above_hull
  direction: positive
  effect_size: 0.05 eV/atom decomposition enthalpy threshold
  confidence: strong
  method_used: dft_thermodynamic_analysis
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
- finding_text: The octahedral factor mu = r_B/r_X has limited standalone predictive
    power for perovskite stability (values 0.44-0.90 for stable perovskites overlap
    substantially with non-perovskites), but improves classification accuracy when
    combined with the tolerance factor as a secondary descriptor.
  construct_ids:
  - octahedral_factor
  - perovskite_formability
  direction: conditional
  effect_size: Marginal improvement when combined with t or tau
  confidence: moderate
  method_used: logistic_regression
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
- finding_text: The revised tolerance factor tau incorporates the oxidation state
    of the A-site cation (n_A), which captures the strength of A-O bonding and is
    the key physical insight that enables a single descriptor to work across both
    oxide and halide chemistries.
  construct_ids:
  - revised_tolerance_factor
  - goldschmidt_tolerance_factor
  direction: positive
  effect_size: null
  confidence: strong
  method_used: SISSO_feature_selection
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
- finding_text: Sublattice mixing in inorganic halide double perovskites (A2BB'X6)
    enables continuous tuning of band gaps across the visible spectrum (1.0-3.5 eV),
    with DFT-HSE06 calculations predicting band gaps within 0.3 eV of experimental
    measurements for validated compositions.
  construct_ids:
  - band_gap
  - halide_perovskite_bandgap
  - double_perovskite_bandgap
  direction: positive
  effect_size: 'Band gap range: 1.0-3.5 eV; DFT accuracy: ±0.3 eV'
  confidence: strong
  method_used: HSE06 hybrid DFT
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
- finding_text: Perovskite formability is necessary but not sufficient for desirable
    band gaps — many stable perovskites have band gaps outside the optimal 1.1-1.7
    eV window for photovoltaics, requiring joint optimization of stability and electronic
    properties.
  construct_ids:
  - band_gap
  - perovskite_formability
  direction: conditional
  effect_size: null
  confidence: moderate
  method_used: DFT screening
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
- finding_text: A SISSO-derived physical descriptor accurately predicts Gibbs energy
    of formation for inorganic crystalline solids as a function of temperature, enabling
    temperature-dependent stability predictions without expensive phonon calculations.
    The descriptor achieves MAE of 47 meV/atom across 2500+ compounds.
  construct_ids:
  - formation_energy_per_atom
  - energy_above_hull
  direction: positive
  effect_size: 'MAE: 47 meV/atom for Gibbs energy prediction'
  confidence: strong
  method_used: SISSO_feature_selection
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
- finding_text: Temperature-dependent Gibbs energy predictions reveal that ~15% of
    materials stable at 0K become unstable at synthesis temperatures, and ~5% of 0K-unstable
    materials become accessible at elevated temperatures — demonstrating that static
    DFT stability predictions can be misleading for synthesis planning.
  construct_ids:
  - formation_energy_per_atom
  - synthesis_temperature
  - thermodynamic_selectivity
  direction: conditional
  effect_size: 15% of stable materials become unstable; 5% of unstable become accessible
    at synthesis T
  confidence: strong
  method_used: temperature_dependent_thermodynamics
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
- finding_text: Decomposition reactions to competing phases are essential for correctly
    assessing DFT-predicted stability — comparing only to elemental references overestimates
    stability by 0.1-0.5 eV/atom for many ternary oxides, leading to false positive
    stability predictions.
  construct_ids:
  - energy_above_hull
  - formation_energy_per_atom
  direction: negative
  effect_size: 0.1-0.5 eV/atom overestimation without decomposition reactions
  confidence: strong
  method_used: DFT benchmark against 71 experimental ternary compounds
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
- finding_text: Machine learning approaches to heterogeneous catalyst design can accelerate
    screening by identifying structure-activity relationships from DFT data, but performance
    is limited by the quality and diversity of training data — underrepresented catalyst
    compositions show significantly higher prediction errors.
  construct_ids:
  - energy_prediction_mae
  - oxygen_evolution_overpotential
  direction: conditional
  effect_size: null
  confidence: moderate
  method_used: systematic_review
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
- finding_text: DFT calculations reveal that aluminum nitride hydrolysis proceeds
    via a hydroxyl-mediated surface proton hopping mechanism with an activation barrier
    of 0.8 eV, establishing a molecular-level understanding of this important surface
    reaction for the first time.
  construct_ids:
  - reaction_driving_force
  direction: positive
  effect_size: 'Activation barrier: 0.8 eV via proton hopping'
  confidence: strong
  method_used: DFT surface calculations, kinetic modeling
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
- finding_text: High-throughput thermodynamic screening of 1,148 binary and ternary
    metal oxide/nitride pairs identifies the most promising materials for solar thermochemical
    ammonia synthesis, with Mn-based systems showing optimal redox properties at achievable
    solar concentrator temperatures.
  construct_ids:
  - thermochemical_cycle_efficiency
  - reaction_driving_force
  direction: positive
  effect_size: Screened 1,148 material pairs; Mn-based systems identified as optimal
  confidence: strong
  method_used: High-throughput thermodynamic screening of 1,148 pairs
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
- finding_text: MgxCr2S4 spinel cathode operates via the high-voltage Cr3+/4+ redox
    couple. DFT predicted it as a suitable high-voltage Mg cathode, but experimental
    electrochemical cycling showed limited reversibility.
  construct_ids:
  - intercalation_voltage
  - cathode_capacity
  - mg_migration_barrier
  direction: conditional
  effect_size: null
  confidence: unknown
  method_used: null
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
- finding_text: 'First-principles evaluation of P-type layered CaTM2O4 demonstrates
    that several compositions have excellent battery properties: thermodynamic stability,
    average voltages of 2.2-4.2 V vs Ca/Ca2+, energy densities up to 600-800 Wh/kg.'
  construct_ids:
  - ca_intercalation_voltage
  - cathode_capacity
  - formation_energy_per_atom
  direction: positive
  effect_size: null
  confidence: unknown
  method_used: null
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
- finding_text: Nanocrystalline layered MnOx with high defect concentration and lattice
    water demonstrates remarkable room-temperature Ca2+ electrochemical activity,
    achieving capacity of ~100-130 mAh/g.
  construct_ids:
  - ca_intercalation_voltage
  - cathode_capacity
  - cation_disorder_energy
  direction: positive
  effect_size: null
  confidence: unknown
  method_used: null
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
- finding_text: Betti curves derived from persistent homology of electron density
    improve ML model performance by over 33 percentage points compared to models trained
    on raw electron density data.
  construct_ids:
  - betti_curve_descriptor
  - persistent_homology_descriptor
  - topological_fingerprint_similarity
  direction: positive
  effect_size: null
  confidence: unknown
  method_used: null
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
- finding_text: Ensemble convolutional neural network trained on physics-informed
    augmented simulated diffraction spectra achieves exceptional accuracy for multi-phase
    mixture identification.
  construct_ids:
  - xrd_phase_identification_accuracy
  - neural_network_potential
  direction: positive
  effect_size: null
  confidence: unknown
  method_used: null
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
- id: bartel_2021_autonomous_design
  title: Toward autonomous design and synthesis of novel inorganic materials
  authors: Bartel, C.J.
  year: 2021
  doi: 10.1039/d1mh00495f
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
- id: bartel_2019_tolerance_factor
  title: New tolerance factor to predict the stability of perovskite oxides and halides
  authors: Bartel, C.J.; Sutton, C.; Goldsmith, B.R.; Ouyang, R.; Musgrave, C.B.;
    Ghiringhelli, L.M.; Scheffler, M.
  year: 2019
  doi: 10.1126/sciadv.aav0693
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
- id: szymanski_2023_autonomous_lab
  title: An autonomous laboratory for the accelerated synthesis of novel materials
  authors: Szymanski, N.J.; Rendy, B.; Fei, Y.; Kumar, R.E.; He, T.; Milber, D.; Jiang,
    H.; Bartel, C.J.; et al.
  year: 2023
  doi: 10.1038/s41586-023-06734-w
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
- id: bartel_2020_double_perovskites
  title: Inorganic Halide Double Perovskites with Optoelectronic Properties Modulated
    by Sublattice Mixing
  authors: Christopher J. Bartel, Jacob M. Clary, Christopher Sutton, Connor W. Scanlon,
    Benjamin M. Goldsmith, Muratahan Aykol, Gerbrand Ceder, Stephan Lany
  year: 2020
  doi: 10.1021/jacs.9b12440
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
- id: bartel_2018_decomposition_reactions
  title: The role of decomposition reactions in assessing first-principles predictions
    of solid stability
  authors: Christopher J. Bartel, Alan W. Weimer, Stephan Lany, Charles B. Musgrave,
    Aaron M. Holder
  year: 2018
  doi: 10.1038/s41524-018-0143-2
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
- id: bartel_2022_review_stability
  title: Review of computational approaches to predict the thermodynamic stability
    of inorganic solids
  authors: Christopher J. Bartel
  year: 2022
  doi: 10.1007/s10853-022-06915-4
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
- id: carr_2025_chalcogenide_instability
  title: Origins of chalcogenide perovskite instability
  authors: Andrew Carr, Talia Glinberg, Nathan Stull, Christopher J. Bartel
  year: 2025
  doi: 10.1039/d5tc02282g
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
- id: sherbondy_2022_nitride_perovskites
  title: 'High-Throughput Selection and Experimental Realization of Two New Ce-Based
    Nitride Perovskites: CeMoN3 and CeWN3'
  authors: Rachel Sherbondy, Rebecca W. Smaha, Christopher J. Bartel, Michael C. Brennan,
    Bethany E. Matthews, Stephan Lany, Andriy Zakutayev
  year: 2022
  doi: 10.1021/acs.chemmater.2c01282
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
- id: yin_2021_mg_spinel_cathode
  title: Operando X-ray Diffraction Studies of the Mg-Ion Migration Mechanisms in
    Spinel Cathodes for Rechargeable Mg-Ion Batteries
  authors: Liang Yin, Bob Jin Kwon, Yunyeong Choi, Alyssa Bartel, Hakim Iddir, Baris
    Key, Sang-Don Han, Christopher J. Bartel, Gerbrand Ceder, Jordi Cabana, Brian
    J. Ingram
  year: 2021
  doi: 10.1021/jacs.1c04098
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
- id: blanc_2021_mg_crs_cathode
  title: Toward the Development of a High-Voltage Mg Cathode Using a Chromium Sulfide
    Host
  authors: Lauren Blanc, Christopher J. Bartel, Haegyeom Kim, Liang Yin, Bob Jin Kwon,
    Baris Key, Timothy T. Fister, Brian J. Ingram, Gerbrand Ceder
  year: 2021
  doi: 10.1021/acsmaterialslett.1c00308
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
- id: koettgen_2020_mg_spinel_conductors
  title: Computational investigation of chalcogenide spinel conductors for all-solid-state
    Mg batteries
  authors: Julius Koettgen, Christopher J. Bartel, Gerbrand Ceder
  year: 2020
  doi: 10.1039/c9cc09510a
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
- id: park_2021_ca_cathodes
  title: 'Layered Transition Metal Oxides as Ca Intercalation Cathodes: A Systematic
    First-Principles Evaluation'
  authors: Haesun Park, Christopher J. Bartel, Gerbrand Ceder
  year: 2021
  doi: 10.1002/aenm.202101698
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
- id: kwon_2022_ca_mno_intercalation
  title: Intercalation of Ca into a Highly Defective Manganese Oxide at Room Temperature
  authors: Bob Jin Kwon, Liang Yin, Christopher J. Bartel, Gerbrand Ceder, Brian J.
    Ingram, Jordi Cabana
  year: 2022
  doi: 10.1021/acs.chemmater.1c03803
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
- id: mcdermott_2023_thermodynamic_selectivity
  title: Assessing Thermodynamic Selectivity of Solid-State Reactions for the Predictive
    Synthesis of Inorganic Materials
  authors: McDermott, McBride, Regier, Tran, Chen, Corrao, Gallant, Kamm, Bartel,
    Chapman, Khalifah, Ceder, Neilson, Persson
  year: 2023
  doi: 10.1021/acscentsci.3c01051
  source_type: journal_article
  journal: null
  url: null
  abstract: Introduces selectivity metrics for solid-state synthesis, analyzing 3,520
    reactions in a data-driven workflow using first-principles thermodynamic data.
    Tested 9 routes for BaTiO3 from 82,985-reaction network. Synchrotron diffraction
    confirms selectivity metrics correlate with phase formation.
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: miura_2020_selective_metathesis_mgcr2s4
  title: Selective metathesis synthesis of MgCr2S4 by control of thermodynamic driving
    forces
  authors: Miura, Ito, Bartel, Sun, Rosero-Navarro, Tadanaga, Nakata, Maeda, Ceder
  year: 2020
  doi: 10.1039/c9mh01999e
  source_type: journal_article
  journal: null
  url: null
  abstract: Demonstrates metathesis-enabled rapid selective synthesis of MgCr2S4 thiospinel
    by altering the thermodynamic landscape, achieving selective product formation
    that is laborious via traditional ceramic routes.
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: zeng_2024_metastable_polymorphs
  title: Selective formation of metastable polymorphs in solid-state synthesis
  authors: Zeng, Szymanski, He, Jun, Gallington, Huo, Bartel, Ouyang, Ceder
  year: 2024
  doi: 10.1126/sciadv.adj5431
  source_type: journal_article
  journal: null
  url: null
  abstract: Presents theoretical framework for polymorph selectivity in solid-state
    reactions using reaction energy as design parameter. Demonstrates surface energy
    role in nucleation of metastable phases. Validated on LiTiOPO4 with in situ characterization
    and DFT.
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: szymanski_2024_thermodynamic_control_regime
  title: Quantifying the regime of thermodynamic control for solid-state reactions
    during ternary metal oxide synthesis
  authors: Szymanski, Byeon, Sun, Zeng, Bai, Kunz, Kim, Helms, Bartel, Kim, Ceder
  year: 2024
  doi: 10.1126/sciadv.adp3309
  source_type: journal_article
  journal: null
  url: null
  abstract: Validates and quantifies thermodynamic control in solid-state reactions
    through in situ characterization of 37 reactant pairs. Reveals threshold of >=60
    meV/atom for thermodynamic control. 15% of possible reactions fall within this
    regime.
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: miura_2021_sequential_pairwise
  title: Observing and Modeling the Sequential Pairwise Reactions that Drive Solid-State
    Ceramic Synthesis
  authors: Miura, Bartel, Goto, Mizuguchi, Moriyoshi, Kuroiwa, Wang, Yaguchi, Shirai,
    Nagao, Rosero-Navarro, Tadanaga, Ceder, Sun
  year: 2021
  doi: 10.1002/adma.202100312
  source_type: journal_article
  journal: null
  url: null
  abstract: Uses computational thermodynamics and in situ XRD/electron microscopy
    to observe sequential pairwise reactions in YBCO synthesis. Substituting BaCO3
    with BaO2 redirects pathway through low-temperature eutectic melt, reducing synthesis
    time from 12+ hours to 30 minutes.
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: szymanski_2023_drx_sro
  title: Modeling Short-Range Order in Disordered Rocksalt Cathodes by Pair Distribution
    Function Analysis
  authors: Nathan J. Szymanski, Zhengyan Lun, Jue Liu, Gerbrand Ceder
  year: 2023
  doi: 10.1021/acs.chemmater.2c03827
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
- id: szymanski_2022_drx_fluorination
  title: Understanding the Fluorination of Disordered Rocksalt Cathodes through Rational
    Exploration of Synthesis Pathways
  authors: Nathan J. Szymanski, Yan Zeng, Tyler H. Bennett, Shuo Bai, Christopher
    J. Bartel, Gerbrand Ceder
  year: 2022
  doi: 10.1021/acs.chemmater.2c01474
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
- id: kothakonda_2022_r2scan_stability
  title: Testing the r2SCAN Density Functional for the Thermodynamic Stability of
    Solids with and without a van der Waals Correction
  authors: Manish Kothakonda, Aaron D. Kaplan, Eric B. Isaacs, Christopher J. Bartel,
    James W. Furness, Jianwei Sun, John P. Perdew, Adrienn Ruzsinszky
  year: 2022
  doi: 10.1021/acsmaterialsau.2c00059
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
- id: kingsbury_2022_r2scan_scan
  title: Performance comparison of r2SCAN and SCAN metaGGA density functionals for
    solid materials via an automated, high-throughput computational workflow
  authors: Ryan Kingsbury, Ayush Gupta, Christopher J. Bartel, Jason M. Munro, Shyam
    Dwaraknath, Matthew Horton, Kristin A. Persson
  year: 2022
  doi: 10.1103/physrevmaterials.6.013801
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
- id: chen_2021_ca_ion_diffusion
  title: Solid-State Calcium-Ion Diffusion in Ca1.5Ba0.5Si5O3N6
  authors: Yu Chen, Christopher J. Bartel, Maxim Avdeev, Gerbrand Ceder
  year: 2021
  doi: 10.1021/acs.chemmater.1c02923
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
- id: huo_2022_ml_synthesis_conditions
  title: Machine-Learning Rationalization and Prediction of Solid-State Synthesis
    Conditions
  authors: Huo, Bartel, He, Trewartha, Dunn, Ouyang, Jain, Ceder
  year: 2022
  doi: 10.1021/acs.chemmater.2c01293
  source_type: journal_article
  journal: null
  url: null
  abstract: ML trained on text-mined synthesis data reveals optimal heating temperatures
    correlate with precursor stability (melting points, formation energies) rather
    than thermodynamic reaction features. Extends Tamman's rule from intermetallics
    to oxide systems.
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: he_2023_precursor_recommendation
  title: Precursor recommendation for inorganic synthesis by machine learning materials
    similarity from scientific literature
  authors: He, Huo, Bartel, Wang, Cruse, Ceder
  year: 2023
  doi: 10.1126/sciadv.adg8180
  source_type: journal_article
  journal: null
  url: null
  abstract: Data-driven precursor recommendation from 29,900 solid-state synthesis
    procedures. Achieves 82% success rate for top-5 precursor recommendations on 2,654
    unseen target materials.
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: szymanski_2023_arrows3
  title: Autonomous and dynamic precursor selection for solid-state materials synthesis
  authors: Szymanski, Nevatia, Bartel, Zeng, Ceder
  year: 2023
  doi: 10.1038/s41467-023-42329-9
  source_type: journal_article
  journal: null
  url: null
  abstract: ARROWS3 algorithm automates precursor selection by learning which precursors
    lead to unfavorable intermediates. Validated on 3 datasets with 200+ synthesis
    procedures, requires fewer iterations than black-box optimization.
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: rognerud_2019_kinetic_metathesis_mn3n2
  title: Kinetically Controlled Low-Temperature Solid-State Metathesis of Manganese
    Nitride Mn3N2
  authors: Rognerud, Rom, Todd, Singstock, Bartel, Holder, Neilson
  year: 2019
  doi: 10.1021/acs.chemmater.9b01565
  source_type: journal_article
  journal: null
  url: null
  abstract: Kinetically controlled metathesis between MnCl2 and Mg2NCl/Mg3N2 produces
    Mn3N2 via solid-solution intermediate mechanism, enabling synthesis of nitrides
    inaccessible by conventional ceramic methods.
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: cosby_2023_thermodynamic_kinetic_barriers
  title: Thermodynamic and Kinetic Barriers Limiting Solid-State Reactions Resolved
    through In Situ Synchrotron Studies of Lithium Halide Salts
  authors: Cosby, Bartel, Corrao, Yakovenko, Gallington, Ceder, Khalifah
  year: 2023
  doi: 10.1021/acs.chemmater.2c02543
  source_type: journal_article
  journal: null
  url: null
  abstract: In situ synchrotron studies reveal rate-limiting barriers for ion exchange
    are associated with salt precursors rather than ceramic targets. Quantifies activation
    energies and identifies scaling relationships for concentration-dependent reaction
    kinetics.
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: blanc_2022_ca_nasicon
  title: Phase Stability and Kinetics of Topotactic Dual Ca2+-Na+ Ion Electrochemistry
    in NaSICON NaV2(PO4)3
  authors: Lauren Blanc, Yunyeong Choi, Abhinandan Shyamsunder, Christopher J. Bartel,
    Bob Jin Kwon, Gerbrand Ceder, Brian J. Ingram, Linda F. Nazar
  year: 2022
  doi: 10.1021/acs.chemmater.2c02816
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
- id: koettgen_2020_cab12h12
  title: First-principles study of CaB12H12 as a potential solid-state conductor for
    Ca
  authors: Julius Koettgen, Christopher J. Bartel, Jimmy-Xuan Shen, Gerbrand Ceder
  year: 2020
  doi: 10.1039/d0cp04500d
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
- id: szymanski_2024_battery_synthesis
  title: Computationally Guided Synthesis of Battery Materials
  authors: Nathan J. Szymanski, Christopher J. Bartel
  year: 2024
  doi: 10.1021/acsenergylett.4c00821
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
- id: ouyang_2021_nasicon_stability
  title: Synthetic accessibility and stability rules of NASICONs
  authors: Bin Ouyang, Jingyang Wang, Tanjin He, Christopher J. Bartel, Haoyan Huo,
    Tiago Botari, Kristin A. Persson, Gerbrand Ceder
  year: 2021
  doi: 10.1038/s41467-021-26006-3
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
- id: tran_2023_defect_rich_lamno3
  title: Selective Synthesis of Defect-Rich LaMnO3 by Low-Temperature Anion Cometathesis
  authors: Tran, Wustrow, O'Nolan, Tao, Bartel, He, McDermott, McBride, Chapman, Billinge,
    Persson, Ceder, Neilson
  year: 2023
  doi: 10.1021/acs.inorgchem.3c03305
  source_type: journal_article
  journal: null
  url: null
  abstract: Double-ion exchange reactions enable LaMnO3 synthesis at 450-480C onset
    vs 1000C+ for traditional routes. Products display defective structures with varying
    defect concentrations.
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: szymanski_2022_fluorination_rocksalt
  title: Understanding the Fluorination of Disordered Rocksalt Cathodes through Rational
    Exploration of Synthesis Pathways
  authors: Szymanski, Zeng, Bennett, Patil, Keum, Self, Bai, Cai, Giovine, Ouyang,
    Wang, Bartel, Clement, Tong, Nanda, Ceder
  year: 2022
  doi: 10.1021/acs.chemmater.2c01474
  source_type: journal_article
  journal: null
  url: null
  abstract: Thermochemical modeling identifies precursor combinations maximizing fluorine
    incorporation in Li1.2Mn0.4Ti0.4O1.6F0.4. Low-temperature reactions produce LiF
    intermediates restricting F availability; elevated temperatures cause LiF volatility
    above 848C.
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: bartel_2021_data_centric
  title: Data-centric approach to improve machine learning models for inorganic materials
  authors: Christopher J. Bartel
  year: 2021
  doi: 10.1016/j.patter.2021.100382
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
- id: adhikari_2023_ml_dft_correction
  title: Interpretable machine learning to understand the performance of semilocal
    density functionals for materials thermochemistry
  authors: Santosh Adhikari, Christopher J. Bartel, Christopher Sutton
  year: 2023
  doi: 10.48550/arxiv.2307.07609
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
- id: sun_2019_ternary_nitrides
  title: A map of the inorganic ternary metal nitrides
  authors: Wenhao Sun, Christopher J. Bartel, Elisabetta Arca, Sage R. Bauers, Bethany
    Matthews, Bernardo Orvananos, Bryan R. Goldsmith, Tiago Botari, Aaron M. Holder,
    Stephan Lany, Andriy Zakutayev, Vladan Stevanovic, Aaron M. Holder
  year: 2019
  doi: 10.1038/s41563-019-0396-2
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
- id: miura_2020_mgcr2s4_metathesis
  title: Selective metathesis synthesis of MgCr2S4 by control of thermodynamic driving
    forces
  authors: Akira Miura, Hiroaki Ito, Christopher J. Bartel, Wenhao Sun, Naoto Rosero-Navarro,
    Kiyoharu Tadanaga, Hideo Nakata, Kazuhiko Maeda, Gerbrand Ceder
  year: 2020
  doi: 10.1039/c9mh01999e
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
- id: cheng_2024_li2mnp2s6
  title: Synthesis, Electronic Structure, and Redox Chemistry of Li2MnP2S6, a Candidate
    High-Voltage Cathode Material
  authors: Yi-Ting Cheng, Yuta Fujii, Yu Nomata, Christopher J. Bartel
  year: 2024
  doi: 10.1021/acs.chemmater.4c02366
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
- id: bartel_2019_ternary_nitrides
  title: A map of the inorganic ternary metal nitrides
  authors: Bartel CJ, Trewartha A, Wang Q, Dunn A, Jain A, Ceder G
  year: 2019
  doi: 10.1038/s41563-019-0396-2
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
- id: bartel_2022_thermodynamic_stability_review
  title: Review of computational approaches to predict the thermodynamic stability
    of inorganic solids
  authors: Bartel CJ
  year: 2022
  doi: 10.1007/s10853-022-06915-4
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
- id: bartel_2019_gibbs_energy
  title: Physical descriptor for the Gibbs energy of inorganic crystalline solids
    and temperature-dependent materials chemistry
  authors: Bartel CJ, Millican SL, Deml AM, Rumptz JR, Tumas W, Weimer AW, Lany S,
    Musgrave CB, Holder AM
  year: 2019
  doi: 10.1038/s41467-018-06682-4
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
- id: hancock_2021_postspinel
  title: Expanding the Ambient-Pressure Phase Space of CaFe2O4-Type Sodium Postspinel
    Host-Guest Compounds
  authors: Justin C. Hancock, Kent J. Griffith, Yunyeong Choi, Christopher J. Bartel,
    Gerbrand Ceder
  year: 2021
  doi: 10.1021/acsorginorgau.1c00019
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
- id: ouyang_2021_nasicon_rules
  title: Synthetic accessibility and stability rules of NASICONs
  authors: Ouyang, Wang, He, Bartel, Huo, Wang, Lacivita, Kim, Ceder
  year: 2021
  doi: 10.1038/s41467-021-26006-3
  source_type: journal_article
  journal: null
  url: null
  abstract: Computational screening of 3,881 NASICON phases with 5/6 synthesis validation.
    ML tolerance factor based on Na content, elemental properties, and Madelung energy
    predicts stability.
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: bartel_2022_review_thermodynamic_stability
  title: Review of computational approaches to predict the thermodynamic stability
    of inorganic solids
  authors: Bartel
  year: 2022
  doi: 10.1007/s10853-022-06915-4
  source_type: journal_article
  journal: null
  url: null
  abstract: Comprehensive review of computational methods for predicting thermodynamic
    stability of inorganic solids, covering DFT functionals, correction schemes, and
    ML approaches. 158 citations.
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: bartel_2018_ml_catalyst_design
  title: Machine learning for heterogeneous catalyst design and discovery
  authors: Goldsmith BR, Esterhuizen J, Liu JX, Bartel CJ, Sutton C
  year: 2018
  doi: 10.1002/aic.16198
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
- id: murphy_2024_catalytic_resonance_circumfluence
  title: 'Catalytic resonance theory: Circumfluence of programmable catalytic loops'
  authors: Murphy, Gathmann, Bartel, Abdelrahman, Dauenhauer
  year: 2024
  doi: 10.1016/j.jcat.2024.115343
  source_type: journal_article
  journal: null
  url: null
  abstract: Develops theory for programmable catalytic loops using catalytic resonance
    theory framework. Analyzes circumfluence (flow patterns) in dynamic catalytic
    systems.
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: murphy_2024_catalytic_resonance_forecasting
  title: 'Catalytic resonance theory: forecasting the flow of programmable catalytic
    loops'
  authors: Murphy, Noordhoek, Gathmann, Dauenhauer, Bartel
  year: 2024
  doi: 10.1039/d4dd00216d
  source_type: journal_article
  journal: null
  url: null
  abstract: Uses interpretable ML to understand and predict complexities of programmable
    catalytic loops, advancing catalytic resonance theory.
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: lee_2021_autoxrd
  title: Probabilistic Deep Learning Approach to Automate the Interpretation of Multi-phase
    Diffraction Spectra
  authors: Lee JW, Park WB, Lee JH, Singh SP, Sohn KS
  year: 2021
  doi: 10.1021/acs.chemmater.1c01071
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
- id: szymanski_2025_generative_baselines
  title: Establishing baselines for generative discovery of inorganic crystals
  authors: Nathan J. Szymanski, Christopher J. Bartel
  year: 2025
  doi: 10.1039/d5mh00010f
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
- id: goldsmith_2018_ml_catalyst_design
  title: Machine learning for heterogeneous catalyst design and discovery
  authors: Goldsmith, Esterhuizen, Liu, Bartel, Sutton
  year: 2018
  doi: 10.1002/aic.16198
  source_type: journal_article
  journal: null
  url: null
  abstract: Review of ML approaches for heterogeneous catalyst design and discovery.
    419 citations. Covers descriptor-based approaches, neural network potentials,
    and active learning for catalysis.
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: cruse_2023_text_mining_bifeo3
  title: Text Mining the Literature to Inform Experiments and Rationalize Impurity
    Phase Formation for BiFeO3
  authors: Cruse, Baibakova, Abdelsamie, Hong, Bartel, Trewartha, Jain, Sutter-Fella,
    Ceder
  year: 2023
  doi: 10.1021/acs.chemmater.3c02203
  source_type: journal_article
  journal: null
  url: null
  abstract: Data-driven analysis of 177 articles containing 331 BiFeO3 sol-gel synthesis
    procedures. Decision tree models identify factors preventing impurities but have
    limited predictive capability due to unreported features in literature.
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: bartel_2022_r2scan_vdw
  title: Testing the r2SCAN Density Functional for the Thermodynamic Stability of
    Solids with and without a van der Waals Correction
  authors: Bartel CJ, Weimer AW, Lany S, Musgrave CB, Holder AM
  year: 2022
  doi: 10.1021/acsmaterialsau.2c00059
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
- id: bartel_2025_topological_descriptors
  title: Topological Descriptors for the Electron Density of Inorganic Solids
  authors: Bartel CJ et al.
  year: 2025
  doi: 10.1021/acsmaterialslett.5c00390
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
- id: cosby_2021_li_exchange_kinetics
  title: Salt effects on Li-ion exchange kinetics and activation energies - systematic
    in situ synchrotron diffraction studies
  authors: Monty R. Cosby, Christopher J. Bartel, Adam A. Corrao, Gerbrand Ceder
  year: 2021
  doi: 10.1107/s010876732109958x
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
- id: rognerud_2019_mn3n2_metathesis
  title: Kinetically Controlled Low-Temperature Solid-State Metathesis of Manganese
    Nitride Mn3N2
  authors: Erik G. Rognerud, Christopher L. Rom, Paul K. Todd, Christopher J. Bartel,
    et al.
  year: 2019
  doi: 10.1021/acs.chemmater.9b01565
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
- id: tran_2023_lamno3_metathesis
  title: Selective Synthesis of Defect-Rich LaMnO3 by Low-Temperature Anion Cometathesis
  authors: Gia Thinh Tran, Allison Wustrow, Daniel O'Nolan, Christopher J. Bartel,
    et al.
  year: 2023
  doi: 10.1021/acs.inorgchem.3c03305
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
- id: schlesinger_2026_synthesis_ml
  title: Thermodynamic assessment of machine learning models for solid-state synthesis
    prediction
  authors: Jane Schlesinger, Simon Hjaltason, Nathan J. Szymanski, Christopher J.
    Bartel
  year: 2026
  doi: 10.48550/arxiv.2602.04075
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
- id: pandey_2021_data_centric_ml
  title: Data-centric approach to improve machine learning models for inorganic materials
  authors: Pandey R, Bartel CJ et al.
  year: 2021
  doi: 10.1016/j.patter.2021.100382
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
- id: bartel_2018_redox_zinc_molybdenum
  title: Redox-Mediated Stabilization in Zinc Molybdenum Nitrides
  authors: Bartel, Clber, Mukhopadhyay, Birgisson, Key, Barin, Simmonds, Stolt, Schelhas,
    Persson, Holder, Toney, Toberer, Neilson
  year: 2018
  doi: 10.1021/jacs.7b12861
  source_type: journal_article
  journal: null
  url: null
  abstract: Demonstrates redox-mediated stabilization mechanisms in zinc molybdenum
    nitrides, relevant to understanding metastable phase formation in nitride systems.
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: bartel_2016_aln_hydrolysis
  title: Aluminum Nitride Hydrolysis Enabled by Hydroxyl-Mediated Surface Proton Hopping
  authors: Christopher J. Bartel, Christopher L. Muhich, Alan W. Weimer, Charles B.
    Musgrave
  year: 2016
  doi: 10.1021/acsami.6b04375
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
- id: bartel_2023_kinetic_barriers
  title: Thermodynamic and Kinetic Barriers Limiting Solid-State Reactions Resolved
    through In Situ Synchrotron Studies of Lithium Halide Salts
  authors: Bartel CJ, Kim J,ండ Sun W, Ceder G
  year: 2023
  doi: 10.1021/acs.chemmater.2c02543
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
- id: bartel_2020_metathesis_mgcr2s4
  title: Selective metathesis synthesis of MgCr2S4 by control of thermodynamic driving
    forces
  authors: Bartel CJ, Rumptz JR, Weimer AW, Holder AM, Musgrave CB
  year: 2020
  doi: 10.1039/c9mh01999e
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
- id: bartel_2020_chalcogenide_spinel
  title: Computational investigation of chalcogenide spinel conductors for all-solid-state
    Mg batteries
  authors: Bartel, Kim, Ceder
  year: 2020
  doi: 10.1039/c9cc09510a
  source_type: journal_article
  journal: null
  url: null
  abstract: Computational screening of chalcogenide spinel ionic conductors for Mg
    batteries, evaluating thermodynamic stability and ionic mobility.
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: liu_2024_rutile_growth_dynamics
  title: Unraveling the Growth Dynamics of Rutile Sn1-xGexO2 Using Theory and Experiment
  authors: Liu, Szymanski, Noordhoek, Shin, Kim, Bartel, Jalan
  year: 2024
  doi: 10.1021/acs.nanolett.4c05043
  source_type: journal_article
  journal: null
  url: null
  abstract: MBE growth of rutile Sn1-xGexO2 achieves up to 34% Ge incorporation at
    600C. Phase diagram analysis indicates spinodal decomposition beyond this concentration.
    Ge-rich phase suppressed by amorphization and GeO volatility.
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: lannerd_2026_proton_insertion
  title: Thermodynamics of proton insertion across the perovskite-brownmillerite transition
    in La0.5Sr0.5CoO3-delta
  authors: Lannerd, Szymanski, Bartel
  year: 2026
  doi: 10.1103/tgp7-n673
  source_type: journal_article
  journal: null
  url: null
  abstract: DFT and ML potentials reveal negative hydrogen insertion energies but
    convex hull shows protonated phases are unstable, decomposing into hydroxides.
    Explains observed acid-etching during electrochemical cycling.
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: schlesinger_2026_ml_synthesis_assessment
  title: Thermodynamic assessment of machine learning models for solid-state synthesis
    prediction
  authors: Schlesinger, Hjaltason, Szymanski, Bartel
  year: 2026
  doi: 10.48550/arxiv.2602.04075
  source_type: journal_article
  journal: null
  url: null
  abstract: Evaluates ML synthesis prediction models against thermodynamic selectivity
    metrics. Models generally overestimate synthesis likelihood, but certain scores
    correlate with thermodynamic heuristics. Uses CHGNet potential on Chemeleon-generated
    materials.
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: lannerd_2026_proton_perovskite
  title: Thermodynamics of proton insertion across the perovskite-brownmillerite transition
    in La0.5Sr0.5CoO3-delta
  authors: Armand J. Lannerd, Nathan J. Szymanski, Christopher J. Bartel
  year: 2026
  doi: 10.1103/tgp7-n673
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
- id: arca_2018_znmon_nitrides
  title: Redox-Mediated Stabilization in Zinc Molybdenum Nitrides
  authors: Elisabetta Arca, Stephan Lany, John D. Perkins, Christopher J. Bartel,
    Aaron M. Holder, Andriy Zakutayev
  year: 2018
  doi: 10.1021/jacs.7b12861
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
- id: bartel_2019_solar_ammonia
  title: High-Throughput Equilibrium Analysis of Active Materials for Solar Thermochemical
    Ammonia Synthesis
  authors: Bartel, Rumptz, Weimer, Holder, Musgrave
  year: 2019
  doi: 10.1021/acsami.9b01242
  source_type: journal_article
  journal: null
  url: null
  abstract: High-throughput thermodynamic evaluation of 1,148 nitride/metal oxide
    pairs for solar thermochemical NH3 synthesis. Assessed hydrolysis, oxide reduction,
    nitrogen fixation, and nitride reformation reactions. Identified promising materials
    based on B, V, Fe, and Ce.
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: singstock_2020_chemical_looping
  title: High-Throughput Analysis of Materials for Chemical Looping Processes
  authors: Singstock, Bartel, Holder, Musgrave
  year: 2020
  doi: 10.1002/aenm.202000685
  source_type: journal_article
  journal: null
  url: null
  abstract: Systematic thermodynamic methodology classifying all 17 experimentally
    tested redox materials and identifying 1,300+ unstudied candidates. Novel process
    for SO2 from raw sulfur and air identified with 12 viable redox material combinations.
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: gathmann_2024_dynamic_oer
  title: Dynamic Promotion of the Oxygen Evolution Reaction via Programmable Metal
    Oxides
  authors: Gathmann, Bartel, Grabow, Abdelrahman, Frisbie, Dauenhauer
  year: 2024
  doi: 10.1021/acsenergylett.4c00365
  source_type: journal_article
  journal: null
  url: null
  abstract: Microkinetic modeling shows programmable oxide catalysts boost OER current
    density by 100-600x at fixed overpotentials or reduce overpotential by 45-140%
    for 10 mA/cm2. O*-to-OOH* and O*-to-OH* barriers are critical parameters.
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: szymanski_2023_adaptive_xrd
  title: Adaptively driven X-ray diffraction guided by machine learning for autonomous
    phase identification
  authors: Szymanski NJ, Bartel CJ, Zeng Y, Tu Q, Ceder G
  year: 2023
  doi: 10.1038/s41524-023-00984-y
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
- id: szymanski_2023_precursor_ml
  title: Precursor recommendation for inorganic synthesis by machine learning materials
    similarity from scientific literature
  authors: Szymanski NJ, Bartel CJ, Zeng Y, Luo Y, Ceder G
  year: 2023
  doi: 10.1126/sciadv.adg8180
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
- id: szymanski_2022_synthesis_conditions
  title: Machine-Learning Rationalization and Prediction of Solid-State Synthesis
    Conditions
  authors: Szymanski NJ, Zeng Y, Huo H, Bartel CJ, Kim H, Ceder G
  year: 2022
  doi: 10.1021/acs.chemmater.2c01293
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
- id: szymanski_2025_topological_descriptors
  title: Topological Descriptors for the Electron Density of Inorganic Solids
  authors: Szymanski, Smith, Daoutidis, Bartel
  year: 2025
  doi: 10.1021/acsmaterialslett.5c00390
  source_type: journal_article
  journal: null
  url: null
  abstract: Introduces Betti curves from persistent homology as electron density descriptors.
    ML models with Betti curves improve >33 percentage points over raw electron density
    for crystal structure classification, stability prediction, and metallic/nonmetallic
    distinction.
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: bartel_2025_generative_baselines
  title: Establishing baselines for generative discovery of inorganic crystals
  authors: Bartel CJ, Szymanski NJ, Zeng Y, Ceder G
  year: 2025
  doi: 10.1039/d5mh00010f
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
- id: szymanski_2021_probabilistic_xrd
  title: Probabilistic Deep Learning Approach to Automate the Interpretation of Multi-phase
    Diffraction Spectra
  authors: Szymanski, Bartel, Zeng, Tu, Ceder
  year: 2021
  doi: 10.1021/acs.chemmater.1c01071
  source_type: journal_article
  journal: null
  url: null
  abstract: Probabilistic neural network ensemble trained on simulated spectra with
    physics-based perturbations for automated XRD analysis. Branching algorithm explores
    phase combinations. Superior to profile matching and conventional ML approaches.
    94 citations.
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: goldsmith_2018_ml_catalyst
  title: Machine learning for heterogeneous catalyst design and discovery
  authors: Bryan R. Goldsmith, Jacques A. Esterhuizen, Jin-Xun Liu, Christopher J.
    Bartel, Christopher Sutton
  year: 2018
  doi: 10.1002/aic.16198
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
- id: cheng_2025_li2fes2_redox
  title: Electronic structure perspective on cation and anion redox in Li2FeS2
  authors: Yi-Ting Cheng, Eshaan S. Patheria, Colin T. Morrell, Christopher J. Bartel
  year: 2025
  doi: 10.26434/chemrxiv-2025-c0s26
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
- id: bartel_2021_nasicon_rules
  title: Synthetic accessibility and stability rules of NASICONs
  authors: Bartel CJ, Kim J,ండ Sun W, Ceder G
  year: 2021
  doi: 10.1038/s41467-021-26006-3
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
- id: todd_2021_pairwise_reactions
  title: Sequential pairwise reactions dictate phase evolution in the solid-state
    synthesis of multicomponent ceramics
  authors: Todd PK, McDermott MJ, Rom CL, Corber AA, Bartel CJ et al.
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
- id: rathnaweera_2025_gdru2x2
  title: 'Antibonding and electronic instabilities in GdRu2X2 (X = Si, Ge, and Sn):
    a new pathway toward developing centrosymmetric altermagnets'
  authors: Dasuni Rathnaweera, Xudong Huai, Ramesh Kumar, Christopher J. Bartel, et
    al.
  year: 2025
  doi: 10.1039/d5tc02333e
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
- id: cruse_2023_bifeo3_text_mining
  title: Text Mining the Literature to Inform Experiments and Rationalize Impurity
    Phase Formation for BiFeO3
  authors: Kevin Cruse, Viktoriia Baibakova, Maged Abdelsamie, Christopher J. Bartel,
    Gerbrand Ceder
  year: 2023
  doi: 10.1021/acs.chemmater.3c02203
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
- id: bartel_2024_thermodynamic_control
  title: Quantifying the regime of thermodynamic control for solid-state reactions
    during ternary metal oxide synthesis
  authors: Bartel CJ, Zeng Y, Szymanski NJ, Tu Q, Ceder G
  year: 2024
  doi: 10.1126/sciadv.adp3309
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
- id: miura_2021_pairwise_reactions
  title: Observing and Modeling the Sequential Pairwise Reactions that Drive Solid-State
    Ceramic Synthesis
  authors: Akira Miura, Christopher J. Bartel, Yosuke Goto, Yusuke Moriyasu, Chikako
    Moriyoshi, Yoshihiro Kuroiwa, Wenhao Sun, Gerbrand Ceder
  year: 2021
  doi: 10.1002/adma.202100312
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
- id: cosby_2023_li_exchange_barriers
  title: Thermodynamic and Kinetic Barriers Limiting Solid-State Reactions Resolved
    through In Situ Synchrotron Studies of Lithium Halide Salts
  authors: Monty R. Cosby, Christopher J. Bartel, Adam A. Corrao, Gerbrand Ceder
  year: 2023
  doi: 10.1021/acs.chemmater.2c02543
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
- id: bartel_2023_thermodynamic_selectivity
  title: Assessing Thermodynamic Selectivity of Solid-State Reactions for the Predictive
    Synthesis of Inorganic Materials
  authors: Bartel CJ, Zeng Y, Szymanski NJ, Tu Q, Ceder G
  year: 2023
  doi: 10.1021/acscentsci.3c01051
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
- id: szymanski_2024_thermodynamic_control
  title: Quantifying the regime of thermodynamic control for solid-state reactions
    during ternary metal oxide synthesis
  authors: Nathan J. Szymanski, Young-Woon Byeon, Yingzhi Sun, Christopher J. Bartel,
    Gerbrand Ceder
  year: 2024
  doi: 10.1126/sciadv.adp3309
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
- id: szymanski_2025_water_splitting_vacancies
  title: Cation vacancies mediate thermochemical water splitting with iron aluminates
  authors: Szymanski, Warren, Weimer, Bartel
  year: 2025
  doi: 10.48550/arxiv.2510.05328
  source_type: journal_article
  journal: null
  url: null
  abstract: Demonstrates cation vacancies in iron aluminate spinels become accessible
    through Al antisite inversion, lowering formation energy from >3 eV to 0.62 eV
    at 1/3 inversion. Supports H2 yields up to 361 umol/g.
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: abdelsamie_2023_bifeo3_pathways
  title: Combining text mining, in situ characterization, and ab initio calculations
    to rationalize BiFeO3 crystallization pathways
  authors: Abdelsamie, Hong, Cruse, Bartel, Baibakova, Trewartha, Jain, Ceder, Sutter-Fella
  year: 2023
  doi: 10.1016/j.matt.2023.10.002
  source_type: journal_article
  journal: null
  url: null
  abstract: Combines text mining, in situ characterization, and ab initio calculations
    to rationalize crystallization pathways for BiFeO3. Multi-modal approach integrating
    literature data with experimental and computational validation.
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: kingsbury_2022_r2scan_benchmark
  title: Performance comparison of r2SCAN and SCAN metaGGA density functionals for
    solid materials via an automated, high-throughput computational workflow
  authors: Kingsbury RS, Rosen AS, Gupta AS, Munro JM, Dwaraknath SS, Horton MK, Ong
    SP
  year: 2022
  doi: 10.1103/physrevmaterials.6.013801
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
- id: mlorber_2024_surface_mlip
  title: Accelerating the prediction of inorganic surfaces with machine learning interatomic
    potentials
  authors: Mlorber V, Bartel CJ
  year: 2024
  doi: 10.1039/d3nr06468a
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
- id: noordhoek_2024_ml_surfaces
  title: Accelerating the prediction of inorganic surfaces with machine learning interatomic
    potentials
  authors: Kyle Noordhoek, Christopher J. Bartel
  year: 2024
  doi: 10.1039/d3nr06468a
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
- id: millican_2020_alkaline_earth_chalcogenides
  title: Alloying behavior of wide band gap alkaline-earth chalcogenides
  authors: Samantha L. Millican, Jacob M. Clary, Christopher J. Bartel, et al.
  year: 2020
  doi: 10.48550/arxiv.2011.06628
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
- id: bartel_2023_interpretable_ml_dft
  title: Interpretable machine learning to understand the performance of semilocal
    density functionals for materials thermochemistry
  authors: Bartel CJ et al.
  year: 2023
  doi: 10.48550/arxiv.2307.07609
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
- id: sullivan_2025_anomalous_hall
  title: Computational search for materials having a giant anomalous Hall effect in
    the pyrochlore and spinel crystal structures
  authors: S. P. Sullivan, Seungjun Lee, Nathan J. Szymanski, Christopher J. Bartel
  year: 2025
  doi: 10.1103/nbvq-gykq
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
- id: szymanski_2021_xrd_deep_learning
  title: Probabilistic Deep Learning Approach to Automate the Interpretation of Multi-phase
    Diffraction Spectra
  authors: Nathan J. Szymanski, Christopher J. Bartel, Yan Zeng, Gerbrand Ceder
  year: 2021
  doi: 10.1021/acs.chemmater.1c01071
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
- id: huo_2022_synthesis_conditions
  title: Machine-Learning Rationalization and Prediction of Solid-State Synthesis
    Conditions
  authors: Haoyan Huo, Christopher J. Bartel, Tanjin He, Gerbrand Ceder
  year: 2022
  doi: 10.1021/acs.chemmater.2c01293
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
- id: szymanski_2023_autonomous_precursor
  title: Autonomous and dynamic precursor selection for solid-state materials synthesis
  authors: Nathan J. Szymanski, Pragnay Nevatia, Christopher J. Bartel, Gerbrand Ceder
  year: 2023
  doi: 10.1038/s41467-023-42329-9
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
- id: liu_2024_sngeo2_growth
  title: Unraveling the Growth Dynamics of Rutile Sn1-xGexO2 Using Theory and Experiment
  authors: Fengdeng Liu, Nathan J. Szymanski, Kyle Noordhoek, Christopher J. Bartel,
    et al.
  year: 2024
  doi: 10.1021/acs.nanolett.4c05043
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
- id: bartel_2026_synthesis_prediction_assessment
  title: Thermodynamic assessment of machine learning models for solid-state synthesis
    prediction
  authors: Bartel CJ et al.
  year: 2026
  doi: 10.48550/arxiv.2602.04075
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
- id: bartel_2022_cenitride_perovskites
  title: 'High-Throughput Selection and Experimental Realization of Two New Ce-Based
    Nitride Perovskites: CeMoN3 and CeWN3'
  authors: Bartel et al.
  year: 2022
  doi: 10.1021/acs.chemmater.2c01282
  source_type: journal_article
  journal: null
  url: null
  abstract: High-throughput DFT screening identifies and experimentally realizes two
    new Ce-based nitride perovskites CeMoN3 and CeWN3, demonstrating predictive synthesis
    from computational screening.
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: bartel_2025_chalcogenide_instability
  title: Origins of chalcogenide perovskite instability
  authors: Bartel et al.
  year: 2025
  doi: 10.1039/d5tc02282g
  source_type: journal_article
  journal: null
  url: null
  abstract: Investigates fundamental thermodynamic origins of instability in chalcogenide
    perovskite materials, explaining why many predicted phases are experimentally
    inaccessible.
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: bartel_2020_halide_double_perovskites
  title: Inorganic Halide Double Perovskites with Optoelectronic Properties Modulated
    by Sublattice Mixing
  authors: Bartel, Clary, Sutton, Vigil-Fowler, Goldber, Musgrave, Lany, Holder
  year: 2020
  doi: 10.1021/jacs.9b12440
  source_type: journal_article
  journal: null
  url: null
  abstract: Demonstrates sublattice mixing as a design strategy for modulating optoelectronic
    properties in halide double perovskites, relevant to understanding synthesis-structure-property
    relationships.
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: bartel_2021_data_centric_ml
  title: Data-centric approach to improve machine learning models for inorganic materials
  authors: Bartel et al.
  year: 2021
  doi: 10.1016/j.patter.2021.100382
  source_type: journal_article
  journal: null
  url: null
  abstract: Data-centric ML approach demonstrating that improving training data quality
    is more effective than model architecture changes for predicting inorganic material
    properties.
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: bartel_2021_calcium_diffusion
  title: Solid-State Calcium-Ion Diffusion in Ca1.5Ba0.5Si5O3N6
  authors: Bartel et al.
  year: 2021
  doi: 10.1021/acs.chemmater.1c02923
  source_type: journal_article
  journal: null
  url: null
  abstract: First-principles study of calcium ion diffusion in nitridosilicate, characterizing
    migration barriers and diffusion mechanisms relevant to solid-state battery design.
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: bartel_2022_nitride_perovskites
  title: 'High-Throughput Selection and Experimental Realization of Two New Ce-Based
    Nitride Perovskites: CeMoN3 and CeWN3'
  authors: Talley KR, Bartel CJ, Sherbondy R, Zakutayev A, Holder AM
  year: 2022
  doi: 10.1021/acs.chemmater.2c01282
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
- id: abdelsamie_2023_bifeo3_text_mining
  title: Text Mining the Literature to Inform Experiments and Rationalize Impurity
    Phase Formation for BiFeO3
  authors: Abdelsamie A, Bartel CJ et al.
  year: 2023
  doi: 10.1021/acs.chemmater.3c02203
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
- id: deng_2024_chgnet_battery
  title: Foundational Machine Learning Interatomic Potential to Study Li-Ion Battery
    Cathode Phase Transformation with Charge Transfer
  authors: Deng B, Zhong P, Bartel CJ, Ceder G
  year: 2024
  doi: 10.1149/ma2024-023333mtgabs
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
- id: bartel_2025_chalcogenide_perovskite
  title: Origins of chalcogenide perovskite instability
  authors: Bartel CJ et al.
  year: 2025
  doi: 10.1039/d5tc02282g
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
- id: bartel_2024_li2mnp2s6
  title: Synthesis, Electronic Structure, and Redox Chemistry of Li2MnP2S6, a Candidate
    High-Voltage Cathode Material
  authors: Bartel CJ et al.
  year: 2024
  doi: 10.1021/acs.chemmater.4c02366
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
- id: bartel_2021_sodium_postspinel
  title: Expanding the Ambient-Pressure Phase Space of CaFe2O4-Type Sodium Postspinel
    Host-Guest Compounds
  authors: Bartel et al.
  year: 2021
  doi: 10.1021/acsorginorgau.1c00019
  source_type: journal_article
  journal: null
  url: null
  abstract: Expands known ambient-pressure phase space of sodium postspinel compounds
    through combined computational prediction and experimental synthesis.
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: bartel_2021_layered_ca_cathodes
  title: 'Layered Transition Metal Oxides as Ca Intercalation Cathodes: A Systematic
    First-Principles Evaluation'
  authors: Bartel et al.
  year: 2021
  doi: 10.1002/aenm.202101698
  source_type: journal_article
  journal: null
  url: null
  abstract: Systematic DFT evaluation of layered transition metal oxides as calcium
    intercalation cathodes, screening voltage, stability, and mobility.
  methodology_summary: null
  sample_size: null
  population_description: null
  study_design: null
  key_limitations: null
  replication_status: null
  data_availability: null
- id: bartel_2018_subgroup_discovery
  title: Finding Patterns, Correlations, and Descriptors in Materials Data Using Subgroup
    Discovery and Compressed Sensing
  authors: Bartel CJ et al.
  year: 2018
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
- id: bartel_2022_nasicon_ca_ion
  title: Phase Stability and Kinetics of Topotactic Dual Ca2+-Na+ Ion Electrochemistry
    in NaSICON NaV2(PO4)3
  authors: Bartel CJ et al.
  year: 2022
  doi: 10.1021/acs.chemmater.2c02816
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
- id: bartel_2020_chalcogenide_spinel_mg
  title: Computational investigation of chalcogenide spinel conductors for all-solid-state
    Mg batteries
  authors: Bartel CJ, Koettgen J, Ong SP
  year: 2020
  doi: 10.1039/c9cc09510a
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
- id: bartel_2021_postspinel_nacf
  title: Expanding the Ambient-Pressure Phase Space of CaFe2O4-Type Sodium Postspinel
    Host-Guest Compounds
  authors: Bartel CJ et al.
  year: 2021
  doi: 10.1021/acsorginorgau.1c00019
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
- id: bartel_2021_ion_exchange_kinetics
  title: Salt effects on Li-ion exchange kinetics and activation energies - systematic
    in situ synchrotron diffraction studies
  authors: Bartel CJ et al.
  year: 2021
  doi: 10.1107/s010876732109958x
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
- id: bartel_2023_bifeo3_crystallization
  title: Combining text mining, in situ characterization, and ab initio calculations
    to rationalize BiFeO3 crystallization pathways
  authors: Abdelsamie A, Bartel CJ et al.
  year: 2023
  doi: 10.1016/j.matt.2023.10.002
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
- id: bartel_2017_water_splitting
  title: Rapid Computational Screening of Materials for Water Splitting Using Ab Initio
    and Machine Learned Models
  authors: Bartel CJ et al.
  year: 2017
  doi: 10.1149/ma2017-01/35/1669
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
- id: bartel_2025_anomalous_hall
  title: Computational search for materials having a giant anomalous Hall effect in
    the pyrochlore and spinel crystal structures
  authors: Sullivan SP, Bartel CJ
  year: 2025
  doi: 10.1103/nbvq-gykq
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
- id: bartel_2020_alkaline_earth_chalcogenides
  title: Alloying behavior of wide band gap alkaline-earth chalcogenides
  authors: Millican SL, Bartel CJ et al.
  year: 2020
  doi: 10.48550/arxiv.2011.06628
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
- id: bartel_2020_cab12h12
  title: First-Principles Study of CaB12H12 as a Potential Solid-State Conductor for
    Ca
  authors: Koettgen J, Bartel CJ, Ong SP
  year: 2020
  doi: 10.26434/chemrxiv.12612278
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
- id: bartel_2025_gdru2x2
  title: Antibonding and Electronic Instabilities in GdRu2X2 (X = Si, Ge, Sn)
  authors: Bartel CJ et al.
  year: 2025
  doi: 10.1039/d5tc02333e
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
- id: bartel_2026_proton_insertion
  title: Thermodynamics of proton insertion across the perovskite-brownmillerite transition
    in La0.5Sr0.5CoO3-delta
  authors: Bartel CJ et al.
  year: 2026
  doi: 10.1103/tgp7-n673
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
- id: bartel_2024_liu_rutile
  title: Unraveling the Growth Dynamics of Rutile Sn1-xGexO2 Using Theory and Experiment
  authors: Liu Y, Bartel CJ et al.
  year: 2024
  doi: 10.1021/acs.nanolett.4c05043
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
- id: bartel_2018_gibbs_descriptor
  title: Physical descriptor for the Gibbs energy of inorganic crystalline solids
    and temperature-dependent materials chemistry
  authors: Bartel CJ, Millican SL, Deml AM, Rumptz JR, Tumas W, Weimer AW, Lany S,
    Musgrave CB, Holder AM
  year: 2018
  doi: 10.1038/s41467-018-06682-4
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
- id: bartel_2018_subgroup_compressed
  title: The role of decomposition reactions in assessing first-principles predictions
    of solid stability
  authors: Bartel CJ, Weimer AW, Lany S, Musgrave CB, Holder AM
  year: 2019
  doi: 10.1038/s41524-019-0249-8
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
- id: bartel_2019_ht_equilibrium
  title: High-throughput equilibrium analysis of active materials for solar thermochemical
    ammonia synthesis
  authors: Bartel CJ, Rumptz JR, Weimer AW, Holder AM, Musgrave CB
  year: 2019
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
playbooks_detail:
- id: cross_domain_survey
  display_name: Cross-Domain Literature Survey
  description: Literature synthesis across all 7 Bartel research domains. Uses unsupervised
    clustering to identify natural construct groupings, then probes cross-domain relationships
    via correlation and regression.
  estimated_runtime: 2 minutes
  step_count: 3
  engines_used:
  - ols_regression
  - kmeans_clustering
  - correlation_matrix
- id: perovskite_screening
  display_name: Perovskite Formability Screening
  description: Screen ABX3 compositions for perovskite formability using the revised
    tolerance factor (tau), geometric descriptors, and ML classifiers. Combines closed-form
    calculation with statistical validation.
  estimated_runtime: 2 minutes
  step_count: 4
  engines_used:
  - random_forest
  - tolerance_factor_calculator
  - logistic_regression
  - correlation_matrix
- id: quick_start
  display_name: Quick Start — Bartel Comp Materials
  description: Basic analysis workflow for the bartel_comp_materials domain.
  estimated_runtime: 1–3 minutes
  step_count: 1
  engines_used:
  - logistic_regression
- id: stability_prediction_benchmark
  display_name: Stability Prediction Benchmark
  description: Compare ML approaches for predicting thermodynamic stability (formation
    energy, energy above hull). Benchmarks linear models against gradient boosting
    and CHGNet neural network potentials.
  estimated_runtime: 3 minutes
  step_count: 4
  engines_used:
  - gradient_boosting
  - pydmclab_ml_potential_relaxation
  - ridge_regression
  - correlation_matrix
- id: synthesis_feasibility_assessment
  display_name: Synthesis Feasibility Assessment
  description: Evaluate synthesis feasibility for target materials by combining thermodynamic
    selectivity analysis with ML classifiers trained on reaction outcomes. References
    Bartel's synthesis assessment tools.
  estimated_runtime: 2 minutes
  step_count: 4
  engines_used:
  - random_forest
  - synth_assess_selectivity
  - logistic_regression
  - correlation_matrix
relationships_detail: []
quality: {}
pax_schema_version: '1.0'
download_url: https://pax-market.com/pax/bartel-comp-materials.pax.tar.gz
download_size: 73.6 KB
published_by: Praxis Agent
related_packs:
- ml-materials-discovery
pax_name: bartel-comp-materials
weight: 10000
---

**Domain:** Autonomous Materials Synthesis

AI-driven autonomous experimentation platforms for accelerated materials synthesis. Covers the A-Lab robotic synthesis platform, ML-guided precursor selection, adaptive XRD characterization, Bayesian optimization of synthesis parameters, and closed-loop discovery workflows.

**Temporal scope:** 2021-2026 | **Population:** Target inorganic materials for experimental synthesis

## Key Findings

- GNN interatomic potentials (MACE-MP, CHGNet, SevenNet) achieve Discovery Acceleration Factors of 5–6x on the WBM test set, compared to ~1x for random baseline and ~2x for simpler one-shot GNN predictors like MEGNet. *(positive, strong)*
- Only 15.3% of WBM test structures are thermodynamically stable (on or within 0 meV/atom of the convex hull), establishing the random discovery baseline for computing DAF. *(null, strong)*
- Models trained on geometry-relaxed structures significantly outperform those using unrelaxed (initial) structures for stability prediction, demonstrating that structural relaxation quality is a key bottleneck. *(positive, strong)*
- Graph neural network models (coGN, coNGN, MEGNet) systematically outperform composition-only models on structure-dependent properties like elastic moduli and phonon frequencies, while performing comparably on formation energy where composition is highly predictive. *(positive, strong)*
- Gradient boosted trees with Magpie compositional features achieve competitive performance on formation energy prediction (MAE ~0.08 eV/atom) despite requiring no structural information, demonstrating the strength of composition-based features for chemically smooth properties. *(positive, moderate)*
- CHGNet, trained on 1.5M MPtrj DFT trajectory frames with magnetic moment supervision, achieves force MAE of ~0.06 eV/Å and correctly predicts DFT-relaxed structure energies within ~0.03 eV/atom for the majority of Materials Project entries. *(positive, strong)*
- GNN interatomic potentials (MACE-MP, CHGNet, SevenNet) achieve Discovery Acceleration Factors of 5–6x on the WBM test set, vs ~1x for random baseline and ~2x for simpler one-shot GNN predictors. *(positive, strong)*
- Only 15.3% of WBM test structures are thermodynamically stable, establishing the random discovery baseline for computing DAF. *(null, strong)*

*...and 275 more findings*

# PAX v3 Specification & Creation Guide

> **Schema version:** 3.0 — Last updated: 2026-04-29
>
> This document is the canonical specification for PAX v3. All future PAX schema changes are documented here. For v1→v2 migration context, see `docs/adr/ADR-007-pax-v2-schema-evolution.md`. PAX v3 builds on v2 by adding the canonical-construct backbone, structured statistics, and minting governance (Sprints 7–9).
>
> **Source of truth.** This file (and its release-asset copy at [pax-market.com/PAX_CREATION_GUIDE.md](https://pax-market.com/PAX_CREATION_GUIDE.md)) is the canonical PAX spec. The friendlier walkthrough at [pax-market.com/guide/](https://pax-market.com/guide/) may lag the spec on field names, enums, or packaging details. **When the two disagree, this document wins.** If you find a contradiction, please open an issue on the [pax-market repo](https://github.com/JELambert/pax-market/issues) and the friendlier guide will be updated to match.

## What Is This Document?

A self-contained guide for creating Praxis PAX (Portable Analytical eXpertise) packages. You can:

1. **Feed it to any LLM** (ChatGPT, Claude, Gemini, Llama) with source material → get a valid PAX out
2. **Use it as a spec** to build PAX tooling in any language
3. **Validate PAX packages** against the schema and checklist below

**No Praxis runtime required.** This guide produces static files (YAML + JSON). The output can be validated offline, then imported into any Praxis instance or published to the [PAX Marketplace](https://pax-market.com).

---

## What's New in v3

PAX v3 extends v2 with a canonical-construct backbone, structured quantitative metadata, and explicit minting governance. The headline changes:

- **Canonical / operationalization split.** Constructs now distinguish *canonical* concepts (the universal idea — e.g., "civil war onset") from *operationalizations* (a specific measurement choice tied to a source — e.g., "ACD onset, ≥1000 battle deaths"). This lets multiple papers map to the same canonical construct without flattening their measurement differences.
- **`canonical_constructs.json`.** A new top-level PAX file lists canonical constructs with `canonical_status` (`provisional`, `canonical`, `deprecated`), `construct_kind`, and a `provenance_json` minting record. Operationalizations in `constructs.yaml` carry an `operationalization_status` (`active`, `deprecated`) and an FK to their canonical parent.
- **`construct_relations.json`.** Backbone relations between canonical constructs use a controlled `relation_type` vocabulary (`subsumes`, `refines`, `disjoint_from`, `equivalent_to`). This is separate from the v2 `construct_relationships` (causal/correlational links between operationalizations).
- **Structured statistics on findings.** Findings can now carry `effect_size_value`, `effect_size_se`, `p_value`, `sample_size`, `r_squared`, `ci_lower`/`ci_upper`, `effect_size_type`, `model_specification`, and `covariates_controlled` as first-class fields. Populate these whenever the source reports them — they unlock meta-analysis and quantitative KB comparison.
- **`unit_of_analysis` on findings.** Findings declare their unit (`country-year`, `dyad-year`, `individual`, `patient`, etc.) so engines can correctly pool, dedupe, or refuse to mix incompatible units.
- **Governance log + minting controls.** Promotion of a construct from `provisional` to `canonical` is gated and logged. Each mint records who/what proposed it and why, leaving an auditable trail in `provenance_json` and the governance section of the PAX.

Existing v2 PAX packages remain valid inputs. The canonical backbone is additive: omit the new files and the package behaves like a v2 PAX, with all operationalizations treated as their own canonical roots.

---

## What Is a PAX?

A PAX is a portable knowledge package that captures everything needed to understand and analyze a domain — academic, business, or applied:

- **What concepts exist** (constructs with formal/operational definitions)
- **What we know** (findings with structured statistics)
- **Where we learned it** (sources with methodology metadata)
- **How concepts relate** (construct relationships)
- **What theories say** (propositions with scope conditions)
- **How to analyze it** (playbooks — reproducible analysis workflows)

### PAX Types

| Type | When to Use | Typical Size | Example |
|------|-------------|--------------|---------|
| `paper` | Single research paper | 5-15 constructs, 4-10 findings, 1 source | Fearon & Laitin (2003) on civil war onset |
| `topic` | Research topic spanning multiple papers | 6-30 constructs, 10-50 findings, 3-15 sources | Democratic peace theory |
| `field` | Entire research field or comprehensive body of work | 30-100+ constructs, 50-300+ findings, 20-150 sources | Bartel computational materials science (142 papers) |
| `enterprise` | Business/industry domain | 5-20 constructs, variable findings, internal + external sources | SaaS customer churn prediction |
| `engine` | Analytical method package (no domain knowledge) | 0-5 constructs, bundled Python engines | Bayesian regression methods |

**Paper PAX** — Start here. Read one paper, extract its contribution. Good for building up a topic incrementally.

**Topic PAX** — Synthesize multiple papers on a theme. Requires cross-paper construct alignment and often has propositions that span sources.

**Field PAX** — Comprehensive coverage of a researcher's body of work or an entire subdiscipline. Usually built by extending a topic PAX repeatedly. May have sub-domains with `parent_domain_id`.

**Enterprise PAX** — Business analytics domain. Uses the same schema but constructs are often KPIs, findings come from internal analyses, and playbooks encode business-relevant workflows.

---

## Output Structure

Produce the following files:

```
my-pax-name/
├── pax.yaml                           # Manifest (required)
├── knowledge/
│   ├── domain.json                    # Domain definition (required)
│   ├── constructs.json                # Construct definitions / operationalizations (required)
│   ├── sources.json                   # Source/paper metadata (required)
│   ├── findings.json                  # Empirical findings (required)
│   ├── propositions.json              # Theoretical claims (recommended)
│   ├── construct_relationships.json   # Causal/correlational links between operationalizations (recommended)
│   ├── canonical_constructs.json      # v3 — Canonical concepts (recommended for v3 PAX)
│   └── construct_relations.json       # v3 — Backbone relations between canonicals (recommended for v3 PAX)
└── playbooks/
    └── quick_start.yaml               # Analysis workflow (recommended)
```

> **v3 note.** `canonical_constructs.json` and `construct_relations.json` are the v3 backbone files. Omit them and the package behaves like v2 (each operationalization is treated as its own canonical root). See "Concept vs. Operationalization" later in this guide.

---

## Step-by-Step Extraction Protocol

### Step 1: Classify Your Input

Read the source material and determine:
- **PAX type**: paper (single paper), topic (multiple papers on a theme), field (comprehensive coverage), enterprise (business domain)
- **Method type(s)**: regression, experimental/RCT, qualitative, theoretical, meta-analysis, descriptive, ML/predictive
- **Unit of analysis**: country-year, individual, firm, dyad, patient, product, customer, etc.
- **Domain scope**: What research field or business area does this cover?

**For a single paper:** Extract exactly what the paper claims.
**For a topic:** Identify the shared constructs across papers, note where findings agree or conflict.
**For a field:** Organize into sub-domains with a parent domain, expect 50+ constructs.
**For enterprise:** Map business metrics to constructs, internal analyses to findings.

### Step 2: Create the Manifest (`pax.yaml`)

```yaml
name: dukalskis-et-al-2024-transnational-repression    # kebab-case, unique
version: "1.0.0"
description: >
  First large-N quantitative study of domestic drivers of transnational
  repression. Tests the hypothesis that authoritarian crackdowns at home
  increase subsequent likelihood of repressing citizens abroad.
schema_version: "3.0"
pax_type: paper          # paper | topic | field | enterprise | engine
author: "Dukalskis, Alexander; Furstenberg, Saipira; Hellmeier, Sebastian; Scales, Redmond"
created: "2024-01-15"
license: CC-BY-4.0
tags: [transnational-repression, authoritarianism, human-rights, V-Dem]
provides:
  constructs:
    - transnational_repression_binary
    - domestic_repression_cli
    - diplomatic_capacity_abroad
    # ... list all construct IDs
  sources:
    - dukalskis_et_al_2024
  findings:
    - dukalskis_2024_finding_0
    - dukalskis_2024_finding_1
    # ... list all finding IDs
  propositions:
    - domestic_crackdown_causes_tr
    - diplomatic_capacity_amplifies_tr
  playbooks:
    - quick_start
  engines: []             # list registered engine IDs the PAX uses
```

**Required fields:** name, version, description, schema_version, pax_type
**pax_type values:**
- `paper` — single paper
- `topic` — research topic (multiple papers)
- `field` — entire research field
- `enterprise` — business/industry domain
- `engine` — analytical method package

### `author` semantics

The manifest's `author` field has different meanings depending on `pax_type`. **Do not confuse it with the authors of the underlying source papers** — those live in `knowledge/sources.json` (each source has its own `authors` field).

| `pax_type` | What `author` means | Example |
|---|---|---|
| `paper` | The author(s) of the paper this PAX represents (carried into manifest as a convenience for display/title derivation; the authoritative copy still lives in `sources.json`). | `"Fearon, James D.; Laitin, David D."` |
| `topic`, `field`, `enterprise`, `engine` | The pack maintainer or curator — the human or org who assembled the PAX, not the authors of the underlying sources. | `"Praxis Agent"`, `"Bartel Lab"`, `"Anthropic"` |

For paper PAX, treat the manifest `author` as a denormalized cache of the source authors — it's used for title derivation (`shorten_authors()` in the registry script) and display. Keep it consistent with the corresponding entry in `sources.json`.

**Optional manifest fields:**
- `published_by` *(string)* — Display name shown as the publisher on [pax-market.com](https://pax-market.com). If unset, the marketplace registry workflow auto-stamps the GitHub username of the PR submitter at submission time. Set this explicitly only if you want a custom value (an organization name, a multi-author credit, or "Praxis Agent" for automated PAX generation). **Do not set it speculatively** — leaving it unset gives the right default for community submissions.
- `provides.datasets[]` *(list, v4+)* — Raw data layer. Each entry declares a CSV/Parquet/Excel dataset the PAX ships (or fetches at install time). The praxis installer registers each as a DuckDB-queryable table; playbooks can then derive `construct_observations` rows from it via `register_dataset` + `derive_observations`. See "Raw Datasets (v4)" below.

### Raw Datasets (v4)

PAX v4 introduces a first-class raw data layer. Use it whenever your PAX wants to ship the actual rows that findings were derived from — instead of (or in addition to) the pre-aggregated construct observations.

```yaml
provides:
  datasets:
    - dataset_id: psed_1990_2012
      display_name: "PSED — Private Security Events Database (1990–2012)"
      description: "Event-level coding of private military and security activity."
      source_url: "https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/ZKKOK7"
      format: csv                    # csv | parquet | excel
      unit_of_analysis: event        # must be in UNIT_OF_ANALYSIS enum
      bundled: false                 # true → file ships in archive at parquet_relpath; false → fetched at install
      parquet_relpath: datasets/psed_1990_2012.parquet  # default if omitted
      sha256: "a1b2c3..."            # required when bundled: true; recomputed and verified at install
```

**Validation rules** (issue #106, enforced by `scripts/validate_pax.py`):
- `bundled: true` → file MUST exist at `parquet_relpath` (default `datasets/<dataset_id>.parquet`) inside the pack source directory.
- `bundled: false` → `source_url` MUST be non-empty.
- If `sha256` is set on a bundled dataset, it MUST match the file bytes.
- `dataset_id`, `display_name`, `format`, `unit_of_analysis` are required on every entry.

**Schema version.** A PAX that uses `provides.datasets[]` MUST declare `schema_version: "4.0"`. v3 PAXes (no datasets block) continue to validate unchanged.

### Step 3: Define the Domain (`knowledge/domain.json`)

```json
{
  "id": "transnational_repression",
  "display_name": "Transnational Repression",
  "description": "State repression of citizens beyond national borders — threats, surveillance, abductions, assassinations targeting diaspora and exiles.",
  "temporal_scope": "1991-2019",
  "population": "Authoritarian regimes (88 states, country-year panel)",
  "level_of_analysis": "macro",
  "research_questions": [
    "Does domestic repression predict transnational repression?",
    "What role does diplomatic capacity play in enabling TR?"
  ]
}
```

**Required:** id (snake_case), display_name, description
**level_of_analysis:** micro, meso, macro, cross-level, dyadic

### Step 4: Extract Constructs (`knowledge/constructs.json`)

Constructs are the atomic building blocks — every variable, concept, or measurable thing.

```json
[
  {
    "id": "transnational_repression_binary",
    "display_name": "Transnational Repression (Binary)",
    "construct_type": "outcome",
    "definition": "Binary indicator equal to 1 if an authoritarian state carried out one or more transnational repression events against its own citizens abroad in a given country-year. Source: AAAD database (Dukalskis 2021).",
    "domain_ids": ["transnational_repression"],
    "source_id": "dukalskis_et_al_2024",
    "formal_definition": "TR ∈ {0, 1} where TR=1 iff count of AAAD events > 0 in country-year t.",
    "operational_definition": "Coded from the Authoritarian Actions Abroad Database (AAAD), which records threats, arrests, extraditions, abductions, and assassinations.",
    "measurement_level": "nominal",
    "aliases": [
      {"alias": "TR", "alias_type": "abbreviation"},
      {"alias": "extraterritorial repression", "alias_type": "synonym"}
    ],
    "measures": [
      "AAAD binary indicator (Dukalskis 2021)",
      "Freedom House transnational repression report"
    ]
  },
  {
    "id": "domestic_repression_cli",
    "display_name": "Domestic Repression (V-Dem CLI)",
    "construct_type": "quantifiable",
    "definition": "Inverted V-Dem Civil Liberties Index measuring intensity of domestic state repression. Higher values = more repression. Aggregates physical violence, political civil liberties, and private civil liberties sub-indices. Lagged one year.",
    "domain_ids": ["transnational_repression"],
    "source_id": "dukalskis_et_al_2024",
    "formal_definition": "CLI_inv = 1 - CLI, where CLI is the V-Dem Civil Liberties Index (v2x_civlib).",
    "operational_definition": "V-Dem v12 Civil Liberties Index, inverted so higher = more repressive, lagged t-1.",
    "measurement_level": "interval",
    "aliases": [
      {"alias": "V-Dem civil liberties", "alias_type": "synonym"},
      {"alias": "CLI", "alias_type": "abbreviation"}
    ],
    "measures": ["V-Dem v12 v2x_civlib (inverted, lagged)"]
  }
]
```

**Required:** id (snake_case), display_name, construct_type, definition
**construct_type values:** quantifiable, concept, process, composite, outcome
**Recommended (added in v2):** formal_definition, operational_definition, measurement_level, aliases, measures

**Rules:**
- One construct per distinct variable or concept
- Definition must be at least one full sentence
- Include how it's measured (operationalization)
- Include aliases (abbreviations, synonyms) for dedup matching
- `measurement_level`: nominal, ordinal, interval, ratio

### Step 5: Register Sources (`knowledge/sources.json`)

```json
[
  {
    "id": "dukalskis_et_al_2024",
    "source_type": "academic_paper",
    "title": "The Long Arm and the Iron Fist: Authoritarian Crackdowns and Transnational Repression",
    "authors": "Dukalskis, Alexander; Furstenberg, Saipira; Hellmeier, Sebastian; Scales, Redmond",
    "year": 2024,
    "doi": "10.1177/00220027231188896",
    "abstract": "Investigates domestic determinants of transnational repression...",
    "methodology_summary": "Country-year panel regression (logistic) with country and year fixed effects, bias-reducing score adjustments (bife package). Robustness: negative binomial, rare events logit, lagged DV.",
    "sample_size": 857,
    "population_description": "88 authoritarian regimes, 1991-2019 (country-year panel)",
    "study_design": "observational_longitudinal",
    "key_limitations": "AAAD captures reported events only (detection bias); excludes digital surveillance; country-year aggregation may miss within-year dynamics",
    "replication_status": "not_attempted",
    "data_availability": "public",
    "journal": "Journal of Conflict Resolution",
    "url": "https://doi.org/10.1177/00220027231188896"
  }
]
```

**Required:** id (snake_case), source_type, title
**source_type values:** academic_paper, journal_article, book, book_chapter, working_paper, report, dataset, manual
**Recommended (added in v2):** methodology_summary, sample_size, study_design, key_limitations, journal

**study_design values:** rct, quasi_experimental, observational_longitudinal, observational_cross_sectional, case_study, meta_analysis, review, theoretical

### Step 6: Extract Findings (`knowledge/findings.json`)

This is the most critical step. Each finding is ONE specific empirical claim.

```json
[
  {
    "source_id": "dukalskis_et_al_2024",
    "domain_id": "transnational_repression",
    "finding_text": "Domestic repression is positively and significantly associated with subsequent transnational repression: β=1.09, SE=0.20, p<0.001 (logistic regression with country/year FE, N=857). First large-N quantitative confirmation that domestic crackdowns predict TR.",
    "construct_ids": ["transnational_repression_binary", "domestic_repression_cli"],
    "direction": "positive",
    "effect_size": "β=1.09 (SE=0.20), p<0.001 — bivariate logistic with country/year FE",
    "method_used": "logistic regression with country and year fixed effects, bias-reducing score adjustments (bife), N=857",
    "confidence": "strong",
    "finding_type": "empirical",
    "evidence_type": "quantitative",
    "state": "provisional",

    "effect_size_value": 1.09,
    "effect_size_se": 0.20,
    "p_value": 0.001,
    "sample_size": 857,
    "r_squared": null,
    "ci_lower": null,
    "ci_upper": null,
    "effect_size_type": "beta",
    "model_specification": "logistic regression with country and year fixed effects, bias-reducing score adjustments (bife)",
    "covariates_controlled": [],

    "unit_of_analysis": "country-year",
    "scope_conditions": "Authoritarian regimes (Polity ≤ 5), 1991–2019, AAAD-coverage countries"
  },
  {
    "source_id": "dukalskis_et_al_2024",
    "domain_id": "transnational_repression",
    "finding_text": "Domestic repression remains significant after full controls: β=0.83, SE=0.26, p<0.01 (Model 2, N=731). Controls: polity score, elections, leader tenure, military dimension, party dimension, population, GDP per capita, state capacity.",
    "construct_ids": ["transnational_repression_binary", "domestic_repression_cli"],
    "direction": "positive",
    "effect_size": "β=0.83 (SE=0.26), p<0.01 — full controls model",
    "method_used": "logistic regression with country/year FE, full controls, N=731",
    "confidence": "strong",
    "finding_type": "empirical",
    "evidence_type": "quantitative",
    "state": "provisional",

    "effect_size_value": 0.83,
    "effect_size_se": 0.26,
    "p_value": 0.01,
    "sample_size": 731,
    "effect_size_type": "beta",
    "model_specification": "logistic regression with country/year FE, bias-reducing score adjustments",
    "covariates_controlled": ["polity_score", "elections", "leader_tenure", "military_dimension", "party_dimension", "population", "gdp_per_capita", "state_capacity"],
    "unit_of_analysis": "country-year",
    "scope_conditions": "Authoritarian regimes (Polity ≤ 5), 1991–2019, full-controls model (Model 2)"
  }
]
```

**Required:** source_id, domain_id, finding_text (≥20 chars), construct_ids (≥1), direction
**direction values:** positive, negative, null, conditional, unknown
**confidence values:** strong, moderate, weak, unknown
**finding_type values:** empirical, theoretical, normative, mechanism, methodological
**evidence_type values:** quantitative, qualitative, mixed, theoretical

**Structured Statistics (added in v2 — ALWAYS populate when available):**

| Field | Type | Description |
|-------|------|-------------|
| effect_size_value | number | The numeric coefficient (β, OR, r, d, HR, etc.) |
| effect_size_se | number | Standard error of the estimate |
| p_value | number | p-value (use 0.001 for p<0.001) |
| sample_size | integer | N for this specific model |
| r_squared | number | Model R² if reported |
| ci_lower | number | Lower bound of confidence interval |
| ci_upper | number | Upper bound of confidence interval |
| effect_size_type | enum | What kind of effect — see [Choosing effect_size_type](#choosing-effect_size_type) |
| model_specification | string | Full model spec (e.g. "OLS with clustered SE by country") |
| covariates_controlled | array | List of control variable names |
| unit_of_analysis | enum | What each row in the underlying data represents — see [Choosing unit_of_analysis](#choosing-unit_of_analysis) |
| scope_conditions | string | Where/when the finding holds — sample restrictions, time window, population filter |

**Set to null if not available. Never guess.**

> **Important:** `unit_of_analysis` is required for engine compatibility — defaulting to `other` defeats the field's purpose. See [Choosing unit_of_analysis](#choosing-unit_of_analysis) below before authoring findings.

**Finding Extraction Rules:**
1. 4-10 findings per paper (more for large papers)
2. One specific claim per finding — not a paper summary
3. Include NULL findings (direction="null") — they are as important as significant ones
4. Each finding references exactly the constructs involved (usually 2)
5. `effect_size` (text) is for narrative summary; structured fields are for computation
6. Always specify the method, sample size, and controls

### Step 7: Define Propositions (`knowledge/propositions.json`)

Propositions are theoretical claims — the "why" behind findings.

```json
[
  {
    "id": "domestic_crackdown_causes_tr",
    "proposition_text": "An increase in domestic repression leads to subsequent transnational repression, because crackdowns drive dissidents abroad who become targets, and activate state surveillance of international links.",
    "construct_from": "domestic_repression_cli",
    "construct_to": "transnational_repression_binary",
    "direction": "positive",
    "domain_id": "transnational_repression",
    "source_id": "dukalskis_et_al_2024",
    "theoretical_basis": "Authoritarian survival theory; regime-diaspora threat perception",
    "scope_conditions": "Authoritarian regimes only; lagged effect (t-1 → t); amplified by diplomatic capacity"
  }
]
```

**Required:** id, proposition_text, construct_from, construct_to
**Recommended:** direction, theoretical_basis, scope_conditions

### Step 8: Define Construct Relationships (`knowledge/construct_relationships.json`)

Explicit causal/correlational links between constructs.

```json
[
  {
    "construct_from": "domestic_repression_cli",
    "construct_to": "transnational_repression_binary",
    "relationship_type": "causal",
    "direction": "positive",
    "strength": "strong",
    "mechanism": "Domestic crackdowns drive dissidents abroad and activate state surveillance of international links, increasing TR likelihood.",
    "source_id": "dukalskis_et_al_2024"
  },
  {
    "construct_from": "diplomatic_capacity_abroad",
    "construct_to": "transnational_repression_binary",
    "relationship_type": "moderating",
    "direction": "positive",
    "strength": "moderate",
    "mechanism": "Diplomatic infrastructure provides logistical means to execute TR in host countries, amplifying the domestic repression → TR pathway.",
    "source_id": "dukalskis_et_al_2024"
  }
]
```

**Required:** construct_from, construct_to, relationship_type
**relationship_type values:** causal, correlational, mediating, moderating, compositional
**strength values:** strong, moderate, weak

### Step 9: Create a Playbook (`playbooks/quick_start.yaml`)

A reproducible analysis workflow.

```yaml
id: quick_start
display_name: "Quick Start — Transnational Repression"
description: "Core analysis replicating the main findings."
estimated_runtime: "1-2 minutes"
requires_data: true

steps:
  - id: data_quality_check
    step: 1
    display_name: "Data Quality Gate"
    action: data_quality_gate
    params:
      constructs:
        - transnational_repression_binary
        - domestic_repression_cli
      min_observations: 50
      max_missing_pct: 0.20
    on_failure: abort

  - id: predictor_correlations
    step: 2
    display_name: "Correlations — Key Predictors"
    engine: correlation_matrix
    params:
      variables:
        - transnational_repression_binary
        - domestic_repression_cli
        - diplomatic_capacity_abroad
    expected_results:
      transnational_repression_binary↔domestic_repression_cli:
        direction: positive

  - id: core_logistic
    step: 3
    display_name: "Core Model — Logistic Regression"
    engine: logistic_regression
    depends_on: [predictor_correlations]
    params:
      outcome: transnational_repression_binary
      predictors:
        - domestic_repression_cli
        - diplomatic_capacity_abroad
    compare_to_kb: true
    expected_results:
      domestic_repression_cli:
        direction: positive
```

---

## Choosing unit_of_analysis

`unit_of_analysis` (added in v3) is **required for engine compatibility**. It tells engines whether two findings can be pooled, meta-analyzed, or compared. Mixing units (e.g., country-year with individual-level) without declaring them yields apples-to-oranges results, so engines refuse incompatible pools when this is set. Defaulting to `other` defeats the whole point — fill it deliberately on every finding.

### Decision aid

Pick the value that describes ONE row in the underlying analysis dataset:

| If the dataset has one row per… | Use |
|---------------------------------|-----|
| Country in a given year (panel data) | `country-year` |
| Region/state/province in a given year (sub-national panels) | `region-year` (preferred general label), or `province-year` |
| Municipality / city in a given year | `municipality-year` |
| County in a given year (US, UK county-level work) | `county-year` |
| District / sub-district in a given year (often census/health divisions) | `district-year` |
| Pair of countries in a given year (interstate conflict, trade dyads) | `dyad-year` |
| Person in a survey or cohort (cross-section) | `individual` |
| Household in a survey | `household` |
| Firm (cross-section, no time dimension) | `firm` |
| Firm-year (annual reporting panels) | `firm-year` |
| Firm-quarter (quarterly financial panels) | `firm-quarter` |
| Patient (cross-section, no time dimension) | `patient` |
| One episode of care for a patient | `patient-episode` |
| Geographic site / location / facility (cross-section, no time dimension) | `site` |
| Site-year (facility-level annual panels) | `site-year` |
| Discrete event (incident, episode, intervention) | `event` |
| One conflict episode | `conflict-episode` |
| None of the above clearly fit | `other` (and add a note in `scope_conditions`) |

> **Rule of thumb for "X" vs "X-year".** If the dataset has any time dimension (multiple observations of the same X over years), use the `-year` (or `-quarter`) form. The bare form (`firm`, `patient`, `site`) is reserved for true cross-sections.

### When a paper reports multiple units

If a paper reports several models on different units (e.g., one country-year regression and one individual-level survival model), create **separate findings for each** — one per (effect, unit) pair. Do not collapse them. Engines need to see each effect attached to its own unit so they can decide what's poolable.

### Common mistakes

- **Defaulting to `other`** — only correct if the unit truly doesn't fit any value above. If it's `other`, document why in `scope_conditions`.
- **Confusing the unit with the construct** — a finding about voter turnout sampled at the individual level is `individual`, even though the construct describes a population-level phenomenon. The unit is the row, not the concept.
- **Treating `country-year` and `dyad-year` interchangeably** — interstate conflict findings are dyadic; choose `dyad-year`.
- **Forcing sub-national panels into `country-year`** — a Philippine-province × year regression is `province-year` (or `region-year`), not `country-year`. Engines that pool by unit will treat them as the same level if you mislabel, masking ecological-fallacy risks.
- **Forcing sub-national panels into `site`** — `site` is reserved for true cross-sections of facilities/locations with no time dimension (e.g., a one-shot RCT site assignment). Sub-national panels with a time axis are `province-year` / `region-year` / `municipality-year` / etc.
- **Choosing `event` for an annual aggregation of events** — if the rows are years (with event counts as columns), the unit is the temporal aggregation level (`country-year`, `firm-quarter`, etc.), not `event`.

### Why engines care

The data adapter and engine pipeline use `unit_of_analysis` to:

- Refuse to pool findings whose units don't match (without an explicit `force_pool=True` override)
- Tag KB-comparison output so an agent can see at a glance whether a meta-result is mixing units
- Block ecological-fallacy traps when `level_bridge` finds a macro/micro construct pair

Setting this correctly is the difference between an engine returning "12 findings agree" and "12 findings agree, all at the country-year level".

---

## Choosing effect_size_type

Pick the value that names what `effect_size_value` actually measures. Mislabeling here forces meta-analysis engines to either drop findings or silently mix incompatible scales.

### Decision aid

| If the headline number is… | Use |
|----------------------------|-----|
| Regression coefficient (linear/logit/probit; raw or log-transformed) | `beta` |
| Odds ratio (logistic, case-control) | `odds_ratio` |
| Hazard ratio (Cox proportional hazards) | `hazard_ratio` |
| Risk ratio / relative risk (cohort, RCT) | `risk_ratio` |
| Incidence rate ratio (Poisson, negative binomial) | `incidence_rate_ratio` |
| Correlation coefficient (Pearson r, Spearman rho) | `correlation_r` |
| Cohen's d (standardized mean difference) | `cohens_d` |
| η² / partial η² (variance-explained from ANOVA) | `eta_squared` |
| Generic ratio of counts (e.g., "9 nurses per emigrant") | `ratio` |
| Elasticity (% change in Y per % change in X) | `elasticity` |
| Semielasticity (% change in Y per unit change in X) | `semielasticity` |
| Percent change vs. counterfactual (e.g., "+148%") | `percent_change` |
| Percentage-point change on a 0–100 scale (e.g., "+12 pp") | `percentage_point_change` |
| dY/dX in natural units (e.g., MPC, marginal effect of price on quantity) | `marginal_effect` |
| Raw difference in means (unstandardized; e.g., "+\$35,000") | `mean_difference` |

### Common mistakes

- **Labeling an elasticity as `beta`** — A coefficient on a log-log regression is technically a beta, but the finding's meaning is an elasticity. If the paper reports "0.30 manufacturing-output elasticity", use `elasticity` so meta-engines can group with other elasticity findings rather than mixing with raw OLS betas.
- **Confusing `percent_change` with `percentage_point_change`** — "+148%" is a relative change (`percent_change`); "+12 pp on turnout" is an additive change on a probability scale (`percentage_point_change`). They are not interchangeable.
- **Using `mean_difference` for standardized differences** — `mean_difference` is the raw, unstandardized difference. If the effect has been divided by a pooled SD, use `cohens_d`.
- **Defaulting to `other`** — there is no `other` value here. If none of the values fit, leave `effect_size_type` null and put the kind in `effect_size` (text) so a future schema extension can capture it.

---

## Concept vs. Operationalization

Praxis distinguishes **conceptual constructs** (what you are trying to measure) from **operationalizations** (the specific coding rule used to measure it). Two papers that both measure "civil war onset" using different battle-death thresholds (UCDP's 25 vs. Fearon & Laitin 2003's 1000) are operationalizing the same concept differently — they should share a `canonical_id` but each declare its own `operationalization_id`.

### Why this matters

The `canonical_id` is the mechanism that enables cross-PAX bridges to work as **identity** rather than name-matching. Without it, two PAX that both define `civil_war_onset` in their own constructs.json files end up as two unrelated rows in the constructs table — bridges and pathway analysis cannot tell that they refer to the same concept. With it, both rows point at `concept:civil_war_onset` and Praxis can answer "what does the literature say about civil war onset?" by looking through every operationalization across every installed PAX.

### How to declare it

In `knowledge/constructs.json`, each construct entry can carry three additional fields:

```json
{
  "id": "civil_war_onset",
  "display_name": "Civil War Onset",
  "construct_type": "quantifiable",
  "definition": "...",
  "canonical_id": "concept:civil_war_onset",
  "operationalization_id": "op:civil_war_onset.fl2003_1000_deaths",
  "coding_rule": "First country-year with cumulative battle-related deaths >= 1000..."
}
```

**Rules:**

- If `canonical_id` is declared, the canonical must either already exist in `canonical_constructs` OR be declared in this PAX's `knowledge/canonical_constructs.json`.
- If `canonical_id` is declared and `operationalization_id` is **not**, the PAX **must** include a `coding_rule` field. The installer will synthesize `op:<canonical_id>.<pax_name>` and write a fresh `construct_operationalizations` row.
- If you omit `canonical_id` entirely, the construct is created without a canonical link (NULL). Sprint 9 governance is opt-in: existing constructs continue to work unchanged.

### Bootstrapping a new canonical

When you encounter a genuinely new concept that does not yet exist on `pax-market.com`, declare it inline in `knowledge/canonical_constructs.json`:

```json
[
  {
    "id": "concept:civil_war_onset",
    "display_name": "Civil War Onset",
    "kind": "outcome",
    "formal_definition": "The first year of an internal armed conflict between a state government and one or more organized armed groups...",
    "status": "provisional",
    "owner": "fearon-laitin-2003"
  }
]
```

The installer loads `canonical_constructs.json` **before** `constructs.json`, so foreign-key references resolve cleanly.

### Construct relations (the lattice)

Use `knowledge/construct_relations.json` to express the lattice of relationships between canonical concepts:

| relation_type | Semantics | Example |
|---------------|-----------|---------|
| `refines` | A refines B = A is **more specific** than B (A is a subtype of B). | `concept:civil_war_onset refines concept:armed_conflict_onset` (civil war is a subtype of armed conflict). |
| `subsumes` | A subsumes B = A is **more general** than B (A encompasses B). The inverse of `refines`. | `concept:armed_conflict_onset subsumes concept:civil_war_onset`. |
| `disjoint_from` | A and B name distinct, non-overlapping concepts. Bridges and pathways cannot traverse this edge. | `concept:civil_war_onset disjoint_from concept:terrorism_onset`. |
| `equivalent_to` | A and B refer to the same concept under different names. Treat as identity. | `concept:gdp_per_capita equivalent_to concept:income_per_capita`. |

Direction matters: `refines` and `subsumes` are inverses of each other. `disjoint_from` and `equivalent_to` are symmetric, but the underlying row still has a `from_id` and `to_id` — pick one direction and stick with it.

**Operational consequence of `disjoint_from`:** the lattice is enforced at traversal time, not just as documentation. Both `find_pathways` and `level_bridge` consult `construct_relations` while building their adjacency graphs and **refuse to cross any `disjoint_from` edge** between two canonicals. This means BFS over `find_pathways` will not return a path between two constructs whose canonicals are declared disjoint, and `level_bridge` will not surface a macro/micro bridge if the underlying canonical pair is disjoint. Use `disjoint_from` deliberately — it is a hard separator across the entire graph.

### Governance flow when registering a new construct

When an agent calls `praxis_skill_construct(display_name=..., definition=...)` **without** declaring a `canonical_id`, Praxis runs cosine similarity over `formal_definition` against all existing canonicals:

| Cosine to nearest canonical | Behavior |
|-----------------------------|----------|
| ≥ 0.80 | **Reject** with `status='rejected_high_similarity'` and the top 3 candidates. The agent must either (a) re-call with `canonical_id=<existing>` to operationalize the existing canonical, or (b) re-call with `force=True` and a `justification` to override. |
| 0.70 – 0.79 | Warn but allow. |
| < 0.70 | Allow. If `PRAXIS_ALLOW_PROVISIONAL_CANONICALS=true`, mint a provisional canonical; otherwise the construct is created with `canonical_id=NULL` (degrade-to-NULL — the default and recommended setting). |

`force=True` always requires a `justification` string. Justifications are written to the `governance_log` table for later audit.

These thresholds (0.80 reject / 0.70 warn) operate on the **canonical layer** only. The existing construct-layer dedup thresholds (0.65 warn / 0.82 auto-merge in `incorporate.py`) are unchanged and continue to govern construct identity within the constructs table.

---

## Validation Checklist

Before submitting your PAX, verify:

### Manifest (`pax.yaml`)
- [ ] `name` is kebab-case (e.g. `my-research-topic`)
- [ ] `version` is semver (e.g. `1.0.0`)
- [ ] `description` is 1-3 sentences
- [ ] `schema_version` is `"3.0"` (or `"2.0"` for legacy packages without canonical backbone)
- [ ] `pax_type` is one of: paper, topic, field, enterprise, engine
- [ ] `provides` lists all entity IDs from knowledge files

### Domain (`domain.json`)
- [ ] `id` is snake_case
- [ ] `description` is at least one sentence
- [ ] `level_of_analysis` is specified

### Constructs (`constructs.json`)
- [ ] Every construct has a unique snake_case `id`
- [ ] Every `definition` is at least one full sentence (≥10 characters)
- [ ] `construct_type` is one of: quantifiable, concept, process, composite, outcome
- [ ] At least one outcome-type construct exists
- [ ] `domain_ids` references the domain from domain.json
- [ ] Aliases included for common abbreviations/synonyms
- [ ] `measurement_level` specified (nominal/ordinal/interval/ratio)

### Sources (`sources.json`)
- [ ] Every source has a unique snake_case `id` (pattern: `author_year`)
- [ ] `methodology_summary` is filled in
- [ ] `sample_size` is specified
- [ ] `study_design` is one of the valid values

### Findings (`findings.json`)
- [ ] Every finding has `source_id` matching a source in sources.json
- [ ] Every finding has `domain_id` matching the domain
- [ ] Every finding has at least one `construct_id` from constructs.json
- [ ] `finding_text` is ≥20 characters and describes ONE specific claim
- [ ] Null findings included (direction="null") for non-significant results
- [ ] **Structured statistics populated** when available:
  - [ ] `effect_size_value` (the numeric coefficient)
  - [ ] `effect_size_se` (standard error)
  - [ ] `p_value`
  - [ ] `sample_size`
  - [ ] `effect_size_type` specified (beta, odds_ratio, etc.)
  - [ ] `model_specification` describes the full model
  - [ ] `covariates_controlled` lists control variables
- [ ] Fields set to `null` (not omitted) when not available

### Construct Relationships (`construct_relationships.json`)
- [ ] Every relationship references constructs from constructs.json
- [ ] `relationship_type` specified
- [ ] `mechanism` explains how/why

### Cross-File Consistency
- [ ] All `construct_ids` in findings exist in constructs.json
- [ ] All `source_id` values in findings exist in sources.json
- [ ] All construct IDs in relationships exist in constructs.json
- [ ] `provides` in pax.yaml lists all entity IDs

---

## ID Conventions

| Entity | Pattern | Examples |
|--------|---------|----------|
| PAX name | kebab-case | `democratic-peace`, `bartel-comp-materials` |
| Domain | snake_case | `transnational_repression`, `climate_economics` |
| Construct | snake_case | `gdp_per_capita`, `civil_war_onset` |
| Source | author_year | `fearon_laitin_2003`, `dukalskis_et_al_2024` |
| Proposition | snake_case descriptive | `poverty_increases_conflict_risk` |
| Playbook | snake_case | `quick_start`, `full_replication` |

---

## Common Mistakes

1. **Findings that summarize instead of claim.** Bad: "The paper studies X." Good: "X increases Y by β=0.34 (p<0.01, N=500)."
2. **Missing null findings.** If a regression coefficient is not significant, that IS a finding with direction="null".
3. **Constructs without operationalization.** Always say how it's measured, not just what it means.
4. **Effect sizes trapped in prose.** Put β=0.34 in `effect_size_value`, not just in `finding_text`.
5. **Missing covariates.** If the paper controls for GDP, population, etc., list them in `covariates_controlled`.
6. **Forgetting construct relationships.** If the paper tests A→B, create a relationship entry.

---

## Multi-Source Examples by PAX Type

### Topic PAX: Democratic Peace Theory

A topic PAX synthesizes multiple papers. The key challenge is **construct alignment** — different papers may measure the same concept differently.

```yaml
# pax.yaml
name: democratic-peace
pax_type: topic
description: "Why democracies rarely fight each other — regime type, economic interdependence, and international organizations."
```

**Sources:** 5 papers (Doyle 1986, Maoz & Russett 1993, Oneal & Russett 1999, Gartzke 2007, Hegre 2014)
**Constructs:** `joint_democracy` (quantifiable), `mid_onset` (outcome), `trade_interdependence` (quantifiable), `igo_membership_overlap` (quantifiable), `capitalist_peace` (concept)
**Findings:** 15 findings across 5 papers — some agree (democracy reduces MID), some contest (Gartzke: it's capitalism, not democracy)
**Propositions:** "Joint democracy reduces interstate conflict" with scope_conditions="post-1945 dyads"

**Key pattern:** The same construct (`joint_democracy`) appears in multiple sources with different operationalizations. Use `measures` to list them all and `aliases` for variant names.

### Field PAX: Computational Materials Science

A field PAX covers an entire research program. Expect sub-domains.

```json
// domain.json — primary domain
{
  "id": "bartel_comp_materials",
  "display_name": "Bartel Computational Materials Science",
  "description": "ML for property prediction, autonomous synthesis, perovskite stability, battery materials..."
}

// Additional domains with parent linkage:
[
  {"id": "perovskite_stability", "parent_domain_id": "bartel_comp_materials", ...},
  {"id": "battery_materials", "parent_domain_id": "bartel_comp_materials", ...},
  {"id": "autonomous_synthesis", "parent_domain_id": "bartel_comp_materials", ...}
]
```

**Key pattern:** Use `parent_domain_id` to organize sub-domains. Constructs and findings spread across sub-domains. The export system will collect all child domains automatically.

### Enterprise PAX: SaaS Churn

```yaml
name: saas-customer-churn
pax_type: enterprise
description: "Customer churn prediction and retention drivers for B2B SaaS."
```

```json
// constructs.json
[
  {
    "id": "monthly_churn_rate",
    "display_name": "Monthly Churn Rate",
    "construct_type": "outcome",
    "definition": "Percentage of paying customers who cancel or don't renew in a given month.",
    "operational_definition": "Churned customers / total active customers at month start × 100",
    "measurement_level": "ratio",
    "measures": ["Stripe subscription cancellation events", "Manual cancellation tracking in CRM"]
  },
  {
    "id": "feature_adoption_score",
    "display_name": "Feature Adoption Score",
    "construct_type": "quantifiable",
    "definition": "Composite score (0-100) measuring how many core product features a customer actively uses.",
    "operational_definition": "Count of distinct core features used in last 30 days / total core features × 100",
    "measurement_level": "ratio"
  }
]

// findings.json
[
  {
    "source_id": "internal_analysis_2026q1",
    "domain_id": "saas_customer_churn",
    "finding_text": "Feature adoption score > 60% reduces monthly churn by 40% compared to low-adoption cohort.",
    "construct_ids": ["feature_adoption_score", "monthly_churn_rate"],
    "direction": "negative",
    "confidence": "strong",
    "effect_size_value": 0.60,
    "effect_size_type": "odds_ratio",
    "sample_size": 5000,
    "p_value": 0.001,
    "model_specification": "logistic regression with cohort and tenure controls",
    "covariates_controlled": ["customer_tenure_months", "plan_tier", "company_size"]
  }
]
```

**Key pattern:** Enterprise PAX often has `dataset` or `manual` source types and findings from internal analyses rather than published papers.

---

## Packaging & Distribution Format

For sharing, archival, marketplace submission, or cross-machine transfer, a PAX is distributed as a single archive containing the PAX directory plus an integrity envelope (`manifest.json`).

### Accepted archive formats

| Format | Extension | Status | When to use |
|---|---|---|---|
| zip | `<pax_name>.zip` | **Canonical (preferred)** | All hand-authored submissions and modern releases. First-class on every desktop OS, browser-friendly. |
| gzip-tar | `<pax_name>.pax.tar.gz` | Legacy (still accepted) | Compatibility with v1 praxis releases. The marketplace continues to publish this alongside `.zip`. |

`submit.pax-market.com` and `praxis_install_pax` accept either format; the marketplace's `publish-artifacts` workflow ships both formats for each pack so legacy consumers keep working. **For new submissions, use `.zip`.**

### Archive layout

The archive flattens the PAX directory at its root and adds one file — `manifest.json` — at the top level:

```
<pax_name>.zip                      (or <pax_name>.pax.tar.gz)
├── manifest.json                   # Archive metadata + per-file sha256 + size
├── pax.yaml
├── knowledge/
│   ├── domain.json
│   ├── constructs.json
│   ├── sources.json
│   ├── findings.json
│   ├── propositions.json
│   ├── construct_relationships.json
│   ├── canonical_constructs.json   # v3
│   └── construct_relations.json    # v3
└── playbooks/
    └── quick_start.yaml
```

> **Note.** `manifest.json` (archive metadata) is distinct from `pax.yaml` (the PAX manifest). Both live at the archive root; only `pax.yaml` is authored by you. **Do not include README.md, image assets, or markdown documentation** — anything not listed in `manifest.json["files"]` will fail the integrity check.

### `manifest.json` schema

```json
{
  "pax_name": "dukalskis-et-al-2024-transnational-repression",
  "version": "1.0.0",
  "schema_version": "3.0",
  "exported_at": "2026-04-29T12:34:56Z",
  "exported_by": "praxis",
  "files": {
    "pax.yaml": { "sha256": "8a7b...e3", "size": 1284 },
    "knowledge/domain.json": { "sha256": "12cf...91", "size": 4102 },
    "knowledge/constructs.json": { "sha256": "44ee...0a", "size": 18733 },
    "knowledge/canonical_constructs.json": { "sha256": "9d10...77", "size": 2950 },
    "knowledge/construct_relations.json": { "sha256": "ab2c...41", "size": 612 }
  }
}
```

Every file shipped in the archive (except `manifest.json` itself) MUST appear in `files` keyed by its archive-relative path, with a `{ "sha256": "<hex>", "size": <int> }` value. `import_pax` recomputes each digest on receipt and refuses the archive on any mismatch — this is the integrity boundary between authoring and consumption.

> **Wire shape — pinned.** `files[<path>]` is always a JSON object with `sha256` and `size`. **Never a bare string.** If you see legacy archives shipping bare strings, treat that as a bug (issue #99); consumers should coerce defensively but producers must emit the dict shape.

### How to produce the archive

**Path A — Round-trip via Praxis (recommended if you have praxis available):**

```python
# Install your authored directory locally first
praxis_install_pax(source="/path/to/my-pax-name")

# Then export — canonical packaging (computes sha256s, builds manifest.json, zips)
praxis_export_pax(pax_name="my-pax-name", output_dir="/path/to/output")
```

`export_pax` always reconstructs the archive contents from the database, not the filesystem — any normalization, ID rewrites, or `extend_pax` additions made after install are reflected in the export.

**Path B — Self-contained Python script (no Praxis runtime):**

Save the snippet below as `build_pax.py` next to your PAX directory and run `python3 build_pax.py my-pax-name/`. It produces both `my-pax-name.zip` and (optionally) `my-pax-name.pax.tar.gz` with a valid `manifest.json` envelope. The marketplace's own registry generator uses the same logic; this snippet is the canonical reference implementation for submitters.

```python
import hashlib, json, sys, zipfile
from datetime import datetime, timezone
from pathlib import Path

def build_pax(pack_dir: Path, *, also_targz: bool = False, exported_by: str = "submitter") -> Path:
    if not (pack_dir / "pax.yaml").exists():
        sys.exit(f"missing pax.yaml under {pack_dir}")
    name = pack_dir.name

    # Collect files (skip dotfiles and __pycache__).
    pack_files = []
    for p in sorted(pack_dir.rglob("*")):
        if not p.is_file():
            continue
        arcname = str(p.relative_to(pack_dir))
        if arcname.startswith(".") or "__pycache__" in arcname:
            continue
        if arcname == "manifest.json":
            continue  # never shipped from source; we generate it
        pack_files.append((p, arcname))

    files = {
        arcname: {
            "sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
            "size": p.stat().st_size,
        }
        for p, arcname in pack_files
    }

    # Read schema_version + version out of pax.yaml without requiring PyYAML.
    import re
    text = (pack_dir / "pax.yaml").read_text()
    def field(k, default=""):
        m = re.search(rf'^\s*{k}\s*:\s*"?([^"\n]+)"?\s*$', text, re.M)
        return (m.group(1).strip() if m else default)

    manifest = {
        "pax_name": name,
        "version": field("version", "0.0.0"),
        "schema_version": field("schema_version", "3.0"),
        "exported_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "exported_by": exported_by,
        "files": files,
    }
    manifest_bytes = json.dumps(manifest, indent=2, sort_keys=True).encode()

    out = pack_dir.parent / f"{name}.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("manifest.json", manifest_bytes)
        for p, arcname in pack_files:
            zf.write(p, arcname=arcname)

    if also_targz:
        import io, tarfile
        targz = pack_dir.parent / f"{name}.pax.tar.gz"
        with tarfile.open(targz, "w:gz") as tar:
            info = tarfile.TarInfo("manifest.json")
            info.size = len(manifest_bytes)
            tar.addfile(info, io.BytesIO(manifest_bytes))
            for p, arcname in pack_files:
                tar.add(p, arcname=arcname)

    return out

if __name__ == "__main__":
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else sys.exit("usage: build_pax.py <pack-dir>")
    out = build_pax(target.resolve(), also_targz="--targz" in sys.argv)
    print(f"wrote {out}")
```

Or if you'd rather not run a script, `submit.pax-market.com` accepts a plain directory upload and runs the same logic server-side — you don't need to produce `manifest.json` yourself in that case.

**Path C — Reference shell snippet (zip only, manual digest pass):**

Useful when you specifically want to build the zip by hand. Requires `python3` (or any tool that produces SHA-256). The Path B script is preferred; this is here for transparency.

```bash
cd /path/to/my-pax-name
python3 - <<'PY'
import hashlib, json, zipfile
from datetime import datetime, timezone
from pathlib import Path
files = {}
for p in sorted(Path('.').rglob('*')):
    if not p.is_file(): continue
    arc = str(p)
    if arc.startswith('.') or arc == 'manifest.json' or '__pycache__' in arc: continue
    files[arc] = {"sha256": hashlib.sha256(p.read_bytes()).hexdigest(), "size": p.stat().st_size}
manifest = {
    "pax_name": Path('.').resolve().name,
    "schema_version": "3.0",
    "exported_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "exported_by": "submitter",
    "files": files,
}
Path('manifest.json').write_text(json.dumps(manifest, indent=2, sort_keys=True))
PY
zip -r "../$(basename $PWD).zip" manifest.json pax.yaml knowledge playbooks
rm manifest.json
```

### Archive integrity rules

- **Filename** — Must be `<pax_name>.zip` (canonical) or `<pax_name>.pax.tar.gz` (legacy). The leading segment must match `pax.yaml`'s `name` field.
- **No path traversal** — Entries with `..`, absolute paths, or symlinks are rejected by `import_pax`.
- **No extra files** — Anything not listed in `manifest.json["files"]` triggers a validation warning. `manifest.json` itself is excluded from the file map. **No README.md, no images, no markdown docs** in the archive.
- **Compression** — `.zip` (deflate or store) or `.pax.tar.gz` (gzip). No bzip2, no xz, no `.tar` without compression.
- **Size guidance** — Most paper PAXes are <100 KB compressed; field PAXes (50+ sources) typically 1–5 MB. Hard ceiling enforced by the marketplace upload service is 50 MB.

---

## What Happens Next

Once you have the files (and optionally the `.pax.tar.gz`):

1. **Validate offline** — Check against the checklist above
2. **Import into Praxis** — Use `praxis_import_pax` (archive) or `praxis_install_pax` (directory)
3. **Or publish** — Submit to the PAX marketplace at [pax-market.com](https://pax-market.com)
4. **Agents use it** — Any Praxis-connected agent can install the PAX and immediately run analyses

The PAX is the unit of portable expertise. Build it once, use it everywhere.

---

## Controlled Vocabularies Reference

These are the canonical enum values for all PAX fields. The Praxis codebase parses this section at runtime — changes here propagate automatically to validation, MCP tool schemas, and LLM extraction prompts.

<!-- PAX_SCHEMA_START — do not remove this marker -->

**pax_type values:** paper, topic, field, enterprise, engine

**source_type values:** academic_paper, journal_article, book, book_chapter, working_paper, report, dataset, manual, synthetic

**construct_type values:** quantifiable, concept, process, composite, outcome

**direction values:** positive, negative, null, conditional, unknown

**confidence values:** strong, moderate, weak, foundational, unknown

**finding_type values:** empirical, theoretical, normative, mechanism, methodological

**evidence_type values:** quantitative, qualitative, mixed, theoretical, exploratory

**finding_state values:** provisional, confirmed, contested, superseded, retracted

**level_of_analysis values:** micro, meso, macro, cross-level, dyadic

**measurement_level values:** nominal, ordinal, interval, ratio

**relationship_type values:** causal, correlational, mediating, moderating, compositional

**study_design values:** rct, quasi_experimental, observational_longitudinal, observational_cross_sectional, case_study, meta_analysis, review, theoretical

**effect_size_type values:** beta, odds_ratio, hazard_ratio, risk_ratio, incidence_rate_ratio, correlation_r, cohens_d, eta_squared, ratio, elasticity, semielasticity, percent_change, percentage_point_change, marginal_effect, mean_difference

**strength values:** strong, moderate, weak

**alias_type values:** synonym, abbreviation, operationalization

**unit_of_analysis values:** country-year, region-year, province-year, municipality-year, county-year, district-year, dyad-year, individual, household, firm, firm-year, firm-quarter, patient, patient-episode, site, site-year, event, conflict-episode, other

**relation_type values:** subsumes, refines, disjoint_from, equivalent_to

**operationalization_status values:** active, deprecated

**canonical_status values:** provisional, canonical, deprecated

**construct_kind values:** quantifiable, concept, process, composite, outcome

**dataset_format values:** csv, parquet, excel

**playbook_action values:** engine, ingest_dataset, data_quality_gate, register_dataset, derive_observations

<!-- PAX_SCHEMA_END — do not remove this marker -->

---

## Machine-Readable Field Manifest

This section is parsed at runtime by `pax_schema.get_entity_fields()`. It defines
required, recommended, and optional fields for each PAX knowledge entity.

<!-- PAX_FIELDS_START -->
```yaml
entities:
  pax_yaml:
    required: [name, version, description, schema_version, pax_type]
    recommended: [author, tags, provides, engines]
    optional: [dependencies, registry_url, domain_id]

  domain:
    required: [id, display_name, description]
    recommended: [temporal_scope, population, level_of_analysis]
    optional: [research_questions, parent_domain_id]

  source:
    required: [id, source_type, title]
    recommended:
      - {name: methodology_summary, type: text}
      - {name: sample_size, type: integer}
      - {name: population_description, type: text}
      - {name: study_design, type: enum, enum: STUDY_DESIGNS}
      - {name: key_limitations, type: text}
      - {name: replication_status, type: text}
      - {name: data_availability, type: text}
      - {name: journal, type: text}
      - {name: url, type: text}
    optional: [authors, year, doi, abstract]

  construct:
    required: [id, display_name, construct_type, definition]
    recommended:
      - {name: formal_definition, type: text}
      - {name: operational_definition, type: text}
      - {name: measurement_level, type: enum, enum: MEASUREMENT_LEVELS}
      - {name: aliases, type: list}
      - {name: measures, type: list}
      - {name: domain_ids, type: list}
    optional: [parent_construct_id, validity_notes, provenance_json, source_id, canonical_id, operationalization_id]

  finding:
    required: [source_id, domain_id, finding_text, construct_ids, direction]
    recommended:
      - {name: confidence, type: enum, enum: CONFIDENCE_VALUES}
      - {name: finding_type, type: enum, enum: FINDING_TYPES}
      - {name: evidence_type, type: enum, enum: EVIDENCE_TYPES}
      - {name: unit_of_analysis, type: enum, enum: UNIT_OF_ANALYSIS}
      - {name: scope_conditions, type: text}
      - {name: sample_n, type: integer}
      - {name: effect_size_value, type: number}
      - {name: effect_size_se, type: number}
      - {name: p_value, type: number}
      - {name: ci_lower, type: number}
      - {name: ci_upper, type: number}
      - {name: effect_size_type, type: enum, enum: EFFECT_SIZE_TYPES}
    optional: [method_used, sample_size, r_squared, model_specification, covariates_controlled, state]

  proposition:
    required: [id, proposition_text, construct_from, construct_to]
    recommended:
      - {name: direction, type: enum, enum: DIRECTION_VALUES}
      - {name: theoretical_basis, type: text}
      - {name: scope_conditions, type: text}
    optional: [domain_id, status, source_id]

  construct_relationship:
    required: [construct_from, construct_to, relationship_type]
    recommended:
      - {name: direction, type: enum, enum: DIRECTION_VALUES}
      - {name: strength, type: enum, enum: STRENGTH_VALUES}
      - {name: mechanism, type: text}
    optional: [source_id]

  construct_alias:
    required: [construct_id, alias]
    recommended:
      - {name: alias_type, type: enum, enum: ALIAS_TYPES}
      - {name: source_id, type: text}
      - {name: pax_name, type: text}
    optional: [added_at]

  construct_measure:
    required: [construct_id, measure_description]
    recommended:
      - {name: unit, type: text}
      - {name: scale_description, type: text}
      - {name: source_id, type: text}
      - {name: pax_name, type: text}
    optional: [added_at]

  construct_evidence:
    required: [construct_id, source_id, contribution_type]
    recommended:
      - {name: pax_name, type: text}
    optional: [added_at]

  dataset_variable:
    required: [source_id, column_name]
    recommended:
      - {name: construct_id, type: text}
      - {name: description, type: text}
      - {name: units, type: text}
      - {name: scale_type, type: text}
      - {name: table_name, type: text}
    optional: [notes, priority, operationalization_notes]

  canonical_construct:
    required: [id, display_name, kind, formal_definition]
    recommended:
      - {name: status, type: text}
      - {name: unit_kind, type: text}
      - {name: owner, type: text}
    optional: [superseded_by]

  construct_operationalization:
    required: [id, canonical_id, display_name, coding_rule]
    recommended:
      - {name: measurement_level, type: enum, enum: MEASUREMENT_LEVELS}
      - {name: source_id, type: text}
      - {name: status, type: text}
    optional: [threshold_json, unit]

  construct_relation:
    required: [from_id, to_id, relation_type]
    recommended:
      - {name: justification, type: text}
      - {name: source_id, type: text}
    optional: [pax_name]

  dataset:
    # v4 — raw data layer. Each entry under `provides.datasets[]` in pax.yaml
    # describes a Parquet/CSV/Excel dataset that ships with the PAX (or is
    # fetched at install time). The praxis runtime registers each entry in
    # DuckDB so playbooks can run `register_dataset` + `derive_observations`
    # against it.
    required:
      - {name: dataset_id, type: text}
      - {name: display_name, type: text}
      - {name: format, type: enum, enum: DATASET_FORMAT}
      - {name: unit_of_analysis, type: enum, enum: UNIT_OF_ANALYSIS}
    recommended:
      - {name: description, type: text}
      - {name: source_url, type: text}
      - {name: bundled, type: boolean}
      - {name: parquet_relpath, type: text}
      - {name: sha256, type: text}
    optional: [row_count, column_count, license]
```
<!-- PAX_FIELDS_END -->

---

## Version History

This document is the canonical PAX specification. All schema changes are recorded here.

| Version | Date | Changes |
|---------|------|---------|
| 4.0 | 2026-04-29 | Raw data layer: `provides.datasets[]` block on the manifest, `dataset` entity in PAX_FIELDS, `dataset_format` and `playbook_action` controlled vocabularies. Two new playbook actions (`register_dataset`, `derive_observations`) documented in `docs/PLAYBOOK_FORMAT.md`. Validator (`scripts/validate_pax.py`) enforces dataset registration when `provides.datasets[]` is non-empty (issue #106). v3 PAXes without a datasets block continue to validate unchanged. |
| 3.0 | 2026-04-28 | Canonical-construct backbone (`canonical_constructs.json`, `construct_relations.json`). Operationalization split — `constructs.json` entries gain `canonical_id`, `operationalization_id`, `operationalization_status`, `coding_rule`. Backbone `relation_type` controlled vocabulary (`subsumes`, `refines`, `disjoint_from`, `equivalent_to`). `unit_of_analysis` on findings (engine pooling/dedup). Minting governance — provisional → canonical promotion logged in `governance_log` with justification. `find_pathways` and `level_bridge` honor `disjoint_from` to block cross-cluster traversal. Sprints 7–9. |
| 2.0 | 2026-04-07 | Structured statistics on findings (effect_size_value, SE, p, N, CI, model_spec, covariates). Enriched source metadata (methodology, study_design, sample_size, limitations, replication). Construct provenance (formal/operational definitions, measurement_level, provenance chain). Construct relationships (causal/correlational with mechanism). Engine documentation (parameters, assumptions, diagnostics, interpretation). Playbook enhancements (data quality gates, conditional branching, parameter variants). Quality scoring adds statistical_richness, relationship_coverage, source_depth sub-scores. See ADR-007. |
| 1.0 | 2026-04-05 | Initial PAX format: manifest, domain, constructs (with aliases/measures), sources, findings, propositions, playbooks, engine registry, data sources. |

### v3.0.1 (2026-04-29 — clarifications, no schema change)
- Banner naming this doc as the source of truth over `pax-market.com/guide/` (issue #95).
- `author` field semantics by `pax_type` clarified — pack maintainer vs. paper authors (issue #98).
- Packaging section: `.zip` named canonical, `.pax.tar.gz` kept as legacy alias; both are accepted upload formats (issue #97).
- "How to produce manifest.json" now ships a self-contained Python script + shell snippet so submitters aren't blocked by the integrity envelope (issue #96).
- `manifest.json["files"]` shape pinned to `{sha256, size}` dict; bare-string shape called out as a producer-side bug (issue #99).

### Planned for v3.1
- Finding TTL/expiration for business metrics that decay
- Data freshness requirements on playbook steps
- KPI constructs with target_value and threshold fields
- Construct scope (org-specific vs. universal)
- Cross-PAX canonical reconciliation (auto-detect when two PAXes use different canonical IDs for the same concept)

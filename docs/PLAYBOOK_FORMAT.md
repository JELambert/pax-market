# PAX Playbook Format

> **Schema version:** 4.0 — Last updated: 2026-04-29
>
> Canonical reference for the playbook YAML format consumed by Praxis. The vocabulary of action types here is the source of truth — `pax_schema.py` parses the controlled vocabulary out of `PAX_CREATION_GUIDE.md`'s `PAX_SCHEMA_START` block (`playbook_action values:` line) at import time.

A playbook is a YAML file under a PAX's `playbooks/` directory. Each playbook describes a reproducible analysis workflow: the steps a praxis-connected agent runs to reproduce or extend the PAX's findings.

## Top-level shape

```yaml
id: quick_start                             # required, kebab-case, unique within the PAX
display_name: "Replicate Avant & Neu (2019) — Table 2"
description: >                              # what the playbook does, free text
  Three-step replication of ...
estimated_runtime: "1 minute"               # human-readable hint
requires_data: true                         # if true, runner expects a registered dataset before step 1
steps:                                      # required, ordered list
  - { ... }
  - { ... }
```

## Step shape

Every step is an object with at minimum:

```yaml
- step: 1                          # ordinal (informational; runner uses depends_on for ordering)
  id: register_psed_raw            # required, unique within the playbook
  display_name: "Register PSED raw data"
  action: register_dataset         # required, one of the values below
  depends_on: [previous_step_id]   # optional list of step ids that must complete first
  params:                          # action-specific parameter block (see per-action sections)
    ...
```

## Action vocabulary

The `action` field accepts one of the values in the `playbook_action values:` line of `PAX_CREATION_GUIDE.md`'s SCHEMA block. Currently:

| Action | Purpose | Writes to construct_observations? |
|---|---|---|
| `engine` | Run a registered statistical engine (cox_ph, ols, kmeans, etc.) | No (engine outputs go elsewhere) |
| `ingest_dataset` | Legacy: fetch CSV → aggregate → write `construct_observations` directly | Yes |
| `data_quality_gate` | Pre-flight assertion on dataset rows / coverage | No |
| `register_dataset` | **v4** Fetch raw data and store as Parquet in install dir | No |
| `derive_observations` | **v4** Run DuckDB SQL on a registered dataset to produce `construct_observations` | Yes |

`ingest_dataset` is preserved for backwards compatibility; new PAXes should prefer the v4 `register_dataset` + `derive_observations` pair, which separates raw-data registration from the SQL transformation that produces observations. The split makes the SQL inspectable, replayable, and testable in isolation.

## `engine` action

```yaml
- id: ar2013_baseline
  action: engine
  engine: cox_ph                   # required, must match a registered engine
  params:
    duration: civil_war_duration
    outcome: conflict_terminated
    predictors: [pmsc_competition, gdp_per_capita, ...]
  expected_results:                # optional KB regression hooks
    pmsc_competition:
      hazard_ratio: 1.294
      direction: positive
      p_threshold: 0.05
```

`expected_results` lets the playbook double as a KB regression test: when the engine returns numbers outside the declared envelope, praxis flags the divergence rather than silently accepting fresh data.

## `data_quality_gate` action

```yaml
- id: gate_panel_coverage
  action: data_quality_gate
  params:
    min_country_years: 800
    required_coverage_window: [1990, 2008]
```

Gates fail the playbook before any expensive engine step runs.

## `register_dataset` action (v4)

Fetches a raw dataset (or copies a bundled one) and stores it as Parquet in the PAX install directory at `<install_root>/<parquet_relpath>` (default `datasets/<dataset_id>.parquet`). Does **not** write to `construct_observations`.

```yaml
- id: register_psed_raw
  action: register_dataset
  params:
    dataset_id: psed_1990_2012     # required, must match an entry in pax.yaml provides.datasets[]
    source_url: "https://dataverse.harvard.edu/..."  # honored when bundled: false
    format: csv                    # csv | parquet | excel
    unit_of_analysis: event
    encoding: latin-1              # optional; default utf-8
    delimiter: ","                 # optional; default ","
```

**Behavior:**
- If the matching `provides.datasets` entry has `bundled: true`, the file is read from inside the archive and rewritten as Parquet.
- If `bundled: false`, the source is fetched from `source_url`. The fetch is content-addressed by `sha256` if the manifest entry provides one.
- After registration the dataset is exposed to subsequent steps as a DuckDB view named `dataset_<dataset_id>`. A bare alias `dataset` always resolves to the most recently registered dataset in the playbook (so a single-dataset playbook can write `FROM dataset`).

## `derive_observations` action (v4)

Runs a DuckDB SQL query against a registered dataset and inserts the result rows into `construct_observations`. This is the canonical v4 way to turn raw data into knowledge.

```yaml
- id: derive_event_counts
  action: derive_observations
  depends_on: [register_psed_raw]
  params:
    dataset_id: psed_1990_2012
    sql: |
      SELECT
        'pmsc_event_count' AS construct_id,
        country_code AS entity_id,
        year AS time_value,
        COUNT(*) AS value_numeric,
        'country-year' AS unit_of_analysis
      FROM dataset
      GROUP BY country_code, year
```

### SQL surface

- The dataset is exposed as the alias `dataset` (and as `dataset_<dataset_id>` if you want to be explicit). Both resolve to `read_parquet('<resolved path>')`.
- The query MUST be a single `SELECT` statement. No DDL, no DML, no `ATTACH`. Multi-statement queries are rejected.
- The result set MUST contain these columns (any extras are ignored):

  | Column | Type | Notes |
  |---|---|---|
  | `construct_id` | TEXT | Must reference a construct defined in this PAX or a dependency. Unknown ids are rejected and logged as `needs_construct_definition`. |
  | `entity_id` | TEXT | Praxis lower-cases entity_ids on insert; the SQL should emit the canonical form (e.g. ISO3 lowercase for country-year datasets). |
  | `time_value` | INT or DATE | Year for annual panels; use DATE for finer-grained data. |
  | `value_numeric` OR `value_text` | NUMERIC / TEXT | Exactly one must be non-null per row. |
  | `unit_of_analysis` | TEXT | Should match an entry in the `UNIT_OF_ANALYSIS` enum. Unknown values produce a warning, not a rejection. |

- Each row is inserted into `construct_observations` with `pax_name` stamped from the playbook context. Re-running the same playbook is idempotent: `(pax_name, construct_id, entity_id, time_value)` is the dedupe key.

### Failure modes

| Failure | Behavior |
|---|---|
| Unknown `construct_id` in result | Row rejected, playbook status `needs_construct_definition`, dangling id logged. |
| Unknown `unit_of_analysis` | Warning, row accepted. |
| Result missing required column | Step fails before any insert; transaction rolled back. |
| SQL is multi-statement or contains DDL/DML | Step fails with `unsafe_sql`; nothing inserted. |
| Source dataset hasn't been registered | Step fails with `dataset_not_registered`. Add the matching `register_dataset` step and re-run. |

## Validation

`scripts/validate_pax.py` checks the following at PR time:

- Each step has a unique `id` within the playbook.
- Each `action` is in the `playbook_action` enum.
- `derive_observations` steps have `depends_on` that includes at least one `register_dataset` step (or the dataset is bundled and pre-registered by the installer).
- `dataset_id` referenced by `register_dataset` and `derive_observations` is declared in `pax.yaml` `provides.datasets[]`.
- SQL strings are present and non-empty when the action requires them.

## Backwards compatibility

- Existing v3 PAXes using `engine`, `ingest_dataset`, or `data_quality_gate` continue to validate unchanged.
- `ingest_dataset` is **not** removed in v4. It remains a valid action; new PAXes should prefer the v4 split.
- Praxis runtime support for `register_dataset` and `derive_observations` is tracked in praxis's playbook-runner work; this document is the canonical spec the runner implements against.

## Version history

| Version | Date | Changes |
|---|---|---|
| 4.0 | 2026-04-29 | First standalone playbook spec doc. Adds `register_dataset` and `derive_observations` actions; SQL surface, failure modes, dataset alias resolution. |

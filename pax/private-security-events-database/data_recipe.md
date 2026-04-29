# PSED Data Recipe — event-level CSV → country-year constructs

The `quick_start` playbook in this PAX consumes country-year aggregates of the
Private Security Events Database (PSED, Avant & Neu 2019). The raw PSED file
distributed by Harvard Dataverse (doi:10.7910/DVN/ZKKOK7) is **event-level** —
77 columns, one row per private security event. This recipe is the canonical
mapping from that event-level file to the country-year constructs the playbook
expects, replicating Avant & Neu (2019) Table 2.

If you skip this preprocessing step, the playbook will fail with construct/
column mismatches.

## Source file quirks (read these first)

- **Filename.** Dataverse delivers the file with a `.tab` extension. It is
  **comma-delimited**, not tab-delimited. Treat it as CSV.
- **Encoding.** Latin-1 (`ISO-8859-1`). UTF-8 ingest fails on byte `0xCA`.
- **Country codes.** PSED uses ISO3 uppercase (`AGO`, `IRQ`). Praxis lower-
  cases entity_ids on import (`AGO` → `ago`). If your AR2013 panel uses
  uppercase ISO3, convert to lowercase before joining or the join will
  silently match nothing.
- **Year coverage.** PSED covers 1990–2012. Trim your AR2013 panel to that
  window before joining.

## Aggregation rules

Apply these in order, grouping by `(country_code, year)`:

### `pmsc_event_count`
```python
df_psed.groupby(["country_code", "year"]).size().rename("pmsc_event_count")
```
A simple row count. Drop any rows where `country_code` or `year` is null.

### `pmsc_government_event_count`
The construct counts events with **any** government client. PSED encodes client
type as three binary columns:

- `Client Types - Local Government`
- `Client Types - National Government`
- `Client Types - Foreign Government`

Avant & Neu (2019) Table 2 uses the union of all three:
```python
gov_mask = (
    df_psed["Client Types - Local Government"].fillna(0).astype(int)
    | df_psed["Client Types - National Government"].fillna(0).astype(int)
    | df_psed["Client Types - Foreign Government"].fillna(0).astype(int)
)
df_psed.loc[gov_mask.astype(bool)].groupby(
    ["country_code", "year"]
).size().rename("pmsc_government_event_count")
```

Reindex against the full country-year panel and fill missing with `0` (a
country-year with zero government events should record `0`, not `NaN`).

### `pmsc_abuse_allegation`
Country-year **count** of events where any abuse-allegation column is set. PSED
has multiple `Abuse - *` columns (e.g., `Abuse - Killing`, `Abuse - Sexual
Violence`). The Table 2 specification uses the count, not a binary
ever-happened flag:

```python
abuse_cols = [c for c in df_psed.columns if c.startswith("Abuse -")]
abuse_any = df_psed[abuse_cols].fillna(0).astype(int).any(axis=1)
df_psed.loc[abuse_any].groupby(
    ["country_code", "year"]
).size().rename("pmsc_abuse_allegation")
```

Reindex against the panel and fill missing with `0`.

### `pmsc_competition` (NOT from PSED)
This construct comes from **Avant & Neu's coded supplement to AR2013**, not
PSED. Source it from the AR2013 panel join, not from the event-level CSV. It
is documented in this PAX as a construct so the playbook can reference it; the
PSED data does not contain it.

### `civil_war_duration`, `conflict_episode`
These come from the AR2013 / UCDP-PRIO panel side of the join, not PSED.
Resolve them from your AR2013 source — the PAX expects them as inputs to the
join, not as outputs of PSED aggregation.

## End-to-end recipe

```python
import pandas as pd

raw = pd.read_csv(
    "PSED.tab",            # despite extension, comma-delimited
    encoding="latin-1",
    low_memory=False,
)

# Lowercase country codes to match praxis's normalized entity_ids.
raw["country_code"] = raw["country_code"].str.lower()

g = raw.groupby(["country_code", "year"])

# 1. event count
ec = g.size().rename("pmsc_event_count")

# 2. government event count (union of three client-type flags)
gov_mask = (
    raw["Client Types - Local Government"].fillna(0).astype(int)
    | raw["Client Types - National Government"].fillna(0).astype(int)
    | raw["Client Types - Foreign Government"].fillna(0).astype(int)
).astype(bool)
gec = (
    raw.loc[gov_mask]
       .groupby(["country_code", "year"])
       .size()
       .rename("pmsc_government_event_count")
)

# 3. abuse-allegation event count
abuse_cols = [c for c in raw.columns if c.startswith("Abuse -")]
abuse_mask = raw[abuse_cols].fillna(0).astype(int).any(axis=1)
aa = (
    raw.loc[abuse_mask]
       .groupby(["country_code", "year"])
       .size()
       .rename("pmsc_abuse_allegation")
)

panel = pd.concat([ec, gec, aa], axis=1).fillna(0).astype(int).reset_index()

# Trim to PSED's coverage window before joining AR2013.
panel = panel[(panel["year"] >= 1990) & (panel["year"] <= 2012)]
panel.to_csv("psed_country_year.csv", index=False)
```

The output `psed_country_year.csv` is the file the `quick_start` playbook
expects. Join it to your AR2013 panel on `(country_code, year)` (after
lowercasing country codes on both sides) before running the playbook.

## Column inventory in this recipe

| Construct in this PAX | Source | Aggregation |
|---|---|---|
| `pmsc_event_count` | PSED | `COUNT(*) GROUP BY country_code, year` |
| `pmsc_government_event_count` | PSED | `COUNT(*) WHERE any(Client Types - *Government) GROUP BY country_code, year` |
| `pmsc_abuse_allegation` | PSED | `COUNT(*) WHERE any(Abuse - *) GROUP BY country_code, year` |
| `pmsc_competition` | AR2013 supplement (not PSED) | n/a — sourced upstream |
| `civil_war_duration` | UCDP/PRIO via AR2013 | n/a — sourced upstream |
| `conflict_episode` | UCDP/PRIO via AR2013 | n/a — sourced upstream |

## Caveats

- Avant & Neu's exact column-name spellings (`Client Types - Foreign
  Government` etc.) are reproduced as they appear in the Dataverse file —
  including the spaces and the leading capital. Don't normalize them before
  the mask is computed.
- If a future Dataverse revision renames columns, this recipe will need
  updating; check the PSED codebook first.
- The Avant & Neu (2019) JCR article is the authoritative replication source
  for the exact specification — this recipe is the country-year roll-up they
  use, not their full event-level analysis.

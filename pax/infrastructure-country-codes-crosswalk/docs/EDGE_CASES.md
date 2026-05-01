# Edge Cases & Coding Choices

This document is required by the PAX v4 infrastructure PAX specification.
It records contested coding choices, time-varying code divergences, and
known limitations of the Thyne country-code crosswalk.

---

## 1. Non-State Entities (ccode = -999)

The do-file assigns `ccode = -999` to 60 dependencies, territories, and
non-recognized entities (e.g., Hong Kong, Puerto Rico, Kosovo pre-2008,
various colonial territories). These are preserved as -999 in the CSV.
**Filter these out for sovereign-state analyses.** Keeping them may cause
join failures or inflated entity counts.

## 2. Year-Conditional G&W Divergences

The Thyne do-file's G&W section contains only ccode-based, year-conditional
rules — not country-name-based rules. These cannot be represented as a flat
crosswalk without a year column:

| Rule | Interpretation |
|------|---------------|
| `ccode_gw=260 if ccode==255 & year>=1949` | West Germany uses G&W=260 for years from 1949 (reunification era) |
| `ccode_gw=340 if ccode==345 & year>=1878 & year<=1915` | Serbia uses G&W=340 for 1878–1915 |
| `ccode_gw=340 if ccode==345 & year>=2006` | Serbia post-2006 uses G&W=340 |
| `ccode_gw=815 if country=="Vietnam" & year>=1816 & year<=1893` | Pre-colonial Vietnam uses G&W=815 |

**Impact:** The CSV's `ccode_gw` column is empty for all rows. Users requiring
G&W codes must apply these ccode-based rules from the original do-file using
the year variable in their own dataset. The bundled CSV is sufficient for
country-name→COW matching; supplement with the raw do-file for full G&W support.

## 3. Kosovo

Kosovo's status is contested:
- In Thyne's do-file: `Kosovo` → `ccode=347` (the Serbia & Montenegro code),
  with a Polity override `ccode_polity=341`.
- In this PAX's ISO3 enrichment: COW 347 → `MNE` (Montenegro, as Serbia &
  Montenegro dissolved into Serbia+Montenegro in 2006). Kosovo's own ISO3 is
  `XKX` (user-assigned, not formally ISO 3166-1).
- **Recommendation:** For post-2008 analyses, treat Kosovo entries as a
  special case. The -999 COW code is also found in the do-file for Kosovo in
  some usages. Validate against your specific dataset.

## 4. Yugoslavia Successor States

Multiple country names map to Yugoslavia/Serbia COW codes (345, 347):
- `Yugoslavia` → 345 (pre-dissolution)
- `Serbia and Montenegro` → 345 or 347
- `Serbia & Montenegro` → 345
- `Kosovo` → 347 with Polity override 341
- `Montenegro` → 341 (COW uses 341 for Montenegro post-2006)

The COW and Polity systems diverge for these entities in the early 1990s.
Use the Polity override column and your dataset's year range to disambiguate.

## 5. Sudan / South Sudan

The do-file handles pre-/post-2011 Sudan via Polity overrides:
- `Sudan` → COW 625; `South Sudan` → COW 626
- Polity overrides: `South Sudan → 525`, `North Sudan → 626`
  (Polity uses different codes than COW for these entities post-2011)

For analyses crossing the 2011 independence date, apply the Polity override
for studies using Polity coding, and keep COW codes for COW-based datasets.

## 6. Vietnam

Three distinct coding strategies:
- `Vietnam` → COW 816; Polity override 818 (for years ≥ 1976)
- `South Vietnam` / `Vietnam, Republic of` → COW 817
- G&W override: COW 816 → G&W 815 for years 1816–1893 (pre-colonial)

Year-awareness is required for correct Vietnam coding.

## 7. Germany

- `Germany` → COW 255 (post-reunification)
- `West Germany` / `Federal Republic of Germany` → COW 255
- `East Germany` / `German Democratic Republic` → COW 265
- Polity override for Germany in 1990 (reunification year): ccode_polity=255
- G&W override: COW 255 → G&W 260 for years ≥ 1949

## 8. ISO3 Enrichment — Not Authoritative

The `iso3` column is a **best-effort** addition NOT present in the original
Thyne do-file. It was derived by mapping COW numeric codes to ISO 3166-1
alpha-3 via a static embedded lookup. Known limitations:

- Historical states (e.g., Bavaria, Hanover, Prussia, Baden, Wurttemberg,
  Austria-Hungary, Ottoman Empire) return NULL — no current ISO3 applies.
- Dependencies and non-states (ccode=-999) return NULL by design.
- Disputed territories (Kosovo, Taiwan, Western Sahara) return best-effort
  codes that may not be authoritative in all contexts.
- Coverage: 490 / 602 rows (81.4%). The remaining 18.6% returned NULL.

For authoritative ISO3 mapping, consult the ISO 3166 Maintenance Agency
or the UNSTATS M49 list directly.

## 9. Leading/Trailing Whitespace in Country Names

Some entries in the do-file have leading spaces, e.g.:
- `" Antigua & Barb."` (space before Antigua)
- `" Antigua & Barbuda"` (space before Antigua)

These are preserved verbatim in the CSV so that exact-match joins against
the original source datasets succeed. Be aware that `TRIM(country_name)`
will normalize these — apply TRIM if your join is failing on such entries.

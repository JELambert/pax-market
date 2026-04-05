---
title: "About Praxis Marketplace"
---

## What is Praxis?

[Praxis](https://github.com/praxis-research/praxis) is an open-source framework for creating agent-accessible empirical research infrastructure. It provides the analytical backbone that AI agents need to handle complex research tasks intelligently — structured context about concepts, literature, data, and analytical methods.

## What are PAX Packs?

**PAX** (Portable Analytical eXpertise) are composable, distributable packages of domain intelligence. Each pack bundles:

- **Constructs** — theoretically-grounded concepts that serve as universal keys linking theory, literature, data, and analysis
- **Findings** — empirical results with provenance, direction, effect sizes, and methods
- **Engines** — analytical methods (regression, survival analysis, causal inference, ML, and more)
- **Playbooks** — executable analysis recipes that agents can run step-by-step
- **Data Protocols** — acquisition configurations (APIs, file downloads) rather than raw data

## PAX Types

| Type | Scope | Example |
|------|-------|---------|
| **Paper** | Single paper, fully decomposed | `fearon-laitin-2003` |
| **Topic** | Research question / narrow domain | `happiness-economics` |
| **Field** | Entire research field | `intra-state-conflict` |
| **Engine** | Analytical method package | `survival-analysis` |
| **Enterprise** | Company-specific analytical domain | Private, not published |

## How to Use a Pack

1. **Browse** the marketplace to find packs relevant to your domain
2. **Download** the `.pax.tar.gz` archive
3. **Import** into your Praxis instance:
   ```
   praxis_import_pax("pack-name.pax.tar.gz", install=True)
   ```
4. **Run playbooks** for guided analysis, or explore constructs and findings directly

## Contributing

PAX packs are submitted via pull request. Export your pack using `praxis_export_pax()`, then open a PR with your pack files. See the [contribution guide](https://github.com/praxis-marketplace/praxis-marketplace) for details.

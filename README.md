# PAX Registry

The source of truth for [PAX](https://github.com/JELambert/praxis) (Portable Analytical eXpertise) packages — structured domain knowledge that gives AI assistants real analytical expertise.

**Browse at [pax-market.com](https://pax-market.com)** | **Submit at [submit.pax-market.com](https://submit.pax-market.com)**

## What is PAX?

A PAX pack is a portable knowledge package you can drop into any AI assistant (ChatGPT, Claude, Gemini, etc.) to give it structured expertise in a specific domain. Each pack bundles:

- **Constructs** — key concepts with precise definitions
- **Findings** — empirical results with structured statistics (effect sizes, p-values, methods)
- **Sources** — papers and datasets the findings trace back to
- **Playbooks** — reproducible analysis workflows

Packs cover domains from economics and public health to materials science and financial risk. Download one, paste it into your AI, and it can reason with real evidence instead of generic training data.

## Pack Structure

```
pax/<pack-name>/
  pax.yaml                  # Manifest — name, version, type, description
  knowledge/
    domain.json             # Domain metadata
    constructs.json         # Construct definitions
    findings.json           # Empirical findings with structured statistics
    sources.json            # Bibliographic references
    propositions.json       # Theoretical claims (optional)
    construct_relationships.json  # Causal/correlational links (optional)
  playbooks/
    quick_start.yaml        # Analysis workflow (optional)
```

## Contributing

Anyone can submit a pack.

### Option 1: Web Upload
1. Go to [submit.pax-market.com](https://submit.pax-market.com)
2. Sign in with GitHub
3. Upload your pack as a zip file
4. Validation runs automatically — you'll see errors immediately
5. After review, your pack goes live on pax-market.com

### Option 2: Pull Request
1. Fork this repo
2. Add your pack directory under `pax/<your-pack-name>/`
3. Open a PR — CI validates the pack structure
4. After review and merge, it's published

### Creation Guide
See the full [PAX Creation Guide](https://pax-market.com/guide/) for how to build a pack from scratch. You can also [download the spec](https://pax-market.com/PAX_CREATION_GUIDE.md) and feed it to any LLM along with your source material to generate a valid pack.

## Validation

PRs touching `pax/**` are validated automatically:

- Required manifest fields: `name`, `version`, `description`, `pax_type`, `schema_version`
- Valid `pax_type`: paper, topic, field, engine, enterprise
- Valid `schema_version`: 1.0, 2.0
- All JSON files must be valid
- At least one construct recommended

## How It Works

```
Pack added to pax/ → PR validated by CI → merged → publish-artifacts.yml runs
  → GitHub Release created with registry.json + full-catalog.json + tar.gz archives
  → pax-market.com fetches release → rebuilds → pack appears on the site
```

This repo is the **registry** — it contains pack data only. The website frontend lives in a [separate repo](https://github.com/JELambert/pax-website).

## Using Packs

### With any AI (no setup)
Download a pack from [pax-market.com](https://pax-market.com), extract the archive, and use the [PAX Usage Guide](https://pax-market.com/PAX_USAGE_GUIDE.md) to load it into your AI assistant.

### With Praxis (full system)
```python
praxis_install_remote("pack-name")  # fetches from registry
# or
praxis_import_pax("pack-name.pax.tar.gz", install=True)
```

## Related Repos

| Repo | Purpose |
|------|---------|
| [praxis](https://github.com/JELambert/praxis) | The framework — MCP server, engines, PAX system |
| [pax-website](https://github.com/JELambert/pax-website) | Frontend for pax-market.com (private) |

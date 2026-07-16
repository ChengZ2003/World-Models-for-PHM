# Resources

This directory curates supporting context without implying endorsement or completeness. [`../data/repositories.csv`](../data/repositories.csv) is the source of truth for structured repository records, and [`generated_related_repositories.md`](generated_related_repositories.md) is its generated verified-only view.

- [`related_repositories.md`](related_repositories.md): structured ecosystem map
- [`datasets.md`](datasets.md): dataset documentation fields and access cautions
- [`metrics.md`](metrics.md): task-specific evaluation concepts
- [`open_source_projects.md`](open_source_projects.md): verified implementations and infrastructure
- [`surveys_and_tutorials.md`](surveys_and_tutorials.md): verified background material
- [`venues.md`](venues.md): publication venues relevant to the search process

Unverified names and links should remain `TODO`; all structured repository and dataset records belong under [`../data/`](../data/README.md). Do not manually edit data rows in generated Markdown. Follow the standard workflow in [`../scripts/README.md`](../scripts/README.md) and commit source and generated changes together.

```bash
python3 scripts/validate_metadata.py
python3 scripts/generate_paper_tables.py
python3 scripts/generate_repository_table.py
git diff
```

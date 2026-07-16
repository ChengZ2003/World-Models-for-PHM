# Structured Data

These CSV files are the only sources of truth for structured records:

- `papers.csv`: bibliographic, scope, mechanism, evaluation, and verification fields
- `datasets.csv`: task, sequence, access, license, and verification fields
- `methods.csv`: method taxonomy and reproduction status
- `repositories.csv`: related-project landscape and verification fields

Use UTF-8 CSV with one header row. Comma-containing values must be quoted. Boolean values are lowercase `true` or `false`; unknown non-boolean content is `TODO` or an allowed `unknown` enum. Dates use `YYYY-MM-DD`. Example records must have obvious `EXAMPLE` labels and remain unverified.

Generated Markdown is a reviewable view, not a second database. Do not maintain data rows manually in `papers/generated/` or `resources/generated_related_repositories.md`.

```bash
python3 scripts/validate_metadata.py
python3 scripts/generate_paper_tables.py
python3 scripts/generate_repository_table.py
git diff
```

Edit a CSV, validate it, regenerate Markdown, review the diff, and commit both source and generated files. GitHub Actions runs the same scripts with `python`. No pandas dependency is used.

# Structured Data

CSV files are the canonical machine-readable metadata sources.

- `papers.csv`: bibliographic, scope, mechanism, evaluation, and verification fields
- `datasets.csv`: task, sequence, access, license, and verification fields
- `methods.csv`: method taxonomy and reproduction status
- `repositories.csv`: related-project landscape and verification fields

Use UTF-8 CSV with one header row. Comma-containing values must be quoted. Boolean values are lowercase `true` or `false`; unknown non-boolean content is `TODO` or an allowed `unknown` enum. Dates use `YYYY-MM-DD`. Example records must have obvious `EXAMPLE` labels and remain unverified.

Run `python scripts/validate_metadata.py` before committing changes.

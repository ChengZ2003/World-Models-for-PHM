# Structured Data

`vocabularies.json` is the source of truth for controlled values. The CSV files are the sources of truth for structured records and review provenance:

- `papers.csv`: bibliographic, scope, mechanism, evaluation, and verification fields
- `datasets.csv`: task, sequence, access, license, and verification fields
- `methods.csv`: method taxonomy and reproduction status
- `repositories.csv`: related-project landscape and verification fields
- `paper_reviews.csv`: independent seven-question classification reviews
- `search_runs.csv`: executed database queries and export provenance
- `screening.csv`: dual-review title/abstract and full-text decisions

The Phase 1A schema is treated as frozen for initial literature entry. Vocabulary or header changes require an explicit reviewed migration that updates validation, generators, documentation, and existing records together.

## Value Conventions

- Single-value structured fields use values from `vocabularies.json`.
- Multi-value structured fields use semicolons, for example `anomaly_detection;rul_prediction`.
- Controlled values use lowercase snake_case.
- Natural-language CSV values containing commas must be quoted.
- `verified` and `approved` are strict lowercase `true` or `false` values.
- Other boolean-like mechanism fields use `true`, `false`, or `unknown`.
- Dates use `YYYY-MM-DD`.
- An unverified paper year may be `TODO`; a verified paper year must be a valid four-digit year.
- Example records must contain an obvious `EXAMPLE` marker and must remain unverified or unapproved.

Known controlled multi-value paper fields are `tasks`, `transition_type`, `learning_objective`, `uncertainty_modeling`, and `application_domain`. Search-run references in `screening.csv` also use semicolons.

## Verification Semantics

A paper may be set to `verified=true` only after at least two different reviewers have submitted approved reviews in `paper_reviews.csv`, completed all seven questions, cited evidence locations, and agreed on the scope. Verification means that metadata and classification rationale were manually reviewed; it does not mean that experimental claims or results were reproduced.

## Survey Data Flow

1. Execute a search and add a row to `search_runs.csv`.
2. Record independent screening decisions in `screening.csv`.
3. Add candidate metadata to `papers.csv` with `verified=false`.
4. Add two independent seven-question reviews to `paper_reviews.csv`.
5. Resolve disagreements and align the paper scope with approved-review consensus.
6. Set `verified=true` only after validation requirements are satisfied.
7. Regenerate Markdown and inspect source/generated consistency.

Generated Markdown is a reviewable view, not a second database. Do not maintain data rows manually in `papers/generated/` or `resources/generated_related_repositories.md`.

```bash
python3 scripts/validate_metadata.py
python3 scripts/generate_paper_tables.py
python3 scripts/generate_repository_table.py
git diff
```

Edit structured data, validate it, regenerate Markdown, review the diff, and commit both source and generated files. GitHub Actions runs the same scripts with `python` and rejects both tracked differences and untracked generated files. No pandas dependency is used.

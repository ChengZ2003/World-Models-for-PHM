# Structured Data

`vocabularies.json` is the source of truth for controlled values. The CSV files are the sources of truth for structured records and review provenance:

- `papers.csv`: bibliographic, scope, mechanism, evaluation, and verification fields
- `datasets.csv`: task, sequence, access, license, and verification fields
- `methods.csv`: method taxonomy and reproduction status
- `repositories.csv`: related-project landscape and verification fields
- `paper_reviews.csv`: independent seven-question classification reviews
- `search_runs.csv`: executed database queries and export provenance
- `screening.csv`: dual-review title/abstract and full-text decisions

The current files are a **Phase 1A candidate schema** with **candidate controlled vocabularies**, pending validation through pilot papers. Formal schema freeze is planned only after 6–8 pilot papers exercise the review and extraction workflow. Until then, vocabulary or header changes still require an explicit reviewed migration that updates validation, generators, documentation, and existing records together.

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

`paper_reviews.csv` preserves independent reviewer judgments. `approved=true` means that one review is complete and has passed formal checks; it does not mean that its scope or confidence agrees with another review. Reviewer rows must not be overwritten to manufacture agreement, and a third or later review may remain as additional evidence.

`papers.csv` stores the final consensus classification in `world_model_scope` and `scope_confidence`, with `consensus_reached`, `consensus_date`, and `consensus_rationale` documenting resolution. A paper may be set to `verified=true` only after at least two different reviewers have approved reviews and the final consensus metadata is complete. When reviewer scope or confidence differs, the rationale must name the differing values and explain how they were resolved.

Verification means that metadata, independent reviews, and final classification were manually checked; it does not mean that experimental claims or results were reproduced.

## Screening Records

Each row in `screening.csv` has a globally unique `screening_id`. The pair `(candidate_id, stage)` is unique, so the same candidate may have one `title_abstract` row and one `full_text` row. DOI, source URL, external identifier, and semicolon-delimited search-run provenance support deduplication and audit.

A completed consensus requires two different reviewers with non-pending decisions. Exclusion requires a recorded reason. Pending rows may remain incomplete without being presented as consensus.

## Survey Data Flow

1. Execute a search and add a row to `search_runs.csv`.
2. Record independent screening decisions in `screening.csv`.
3. Add candidate metadata to `papers.csv` with `verified=false`.
4. Add two independent seven-question reviews to `paper_reviews.csv`.
5. Preserve reviewer disagreements and record their resolution in the paper consensus fields.
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

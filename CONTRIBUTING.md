# Contributing

Thank you for helping build a careful, verifiable resource on world models for PHM.

## Evidence Policy

- Do not submit fabricated citations, URLs, repositories, or results.
- Do not rely solely on model-generated metadata.
- Prefer official paper pages, proceedings, DOI records, dataset pages, and official repositories.
- Use `TODO` for unresolved fields and set `verified` to `false`.
- Explain classification using the actual dynamics mechanism, not only author terminology.
- Mark uncertain classification honestly and discuss taxonomy disagreements in the pull request description.
- Do not report unverified reproduction results or conceal protocol differences and failed experiments.

## Contribution Workflows

### Adding Papers

1. Record an executed query in [`data/search_runs.csv`](data/search_runs.csv).
2. Complete dual screening in [`data/screening.csv`](data/screening.csv).
3. Add a unique candidate to [`data/papers.csv`](data/papers.csv) with `verified=false`.
4. Use semicolons for multiple tasks and controlled values from [`data/vocabularies.json`](data/vocabularies.json).
5. Verify title, authors, year, venue, official URLs, tasks, datasets, mechanism, and classification evidence.
6. Use a paper note based on [`paper_notes/TEMPLATE.md`](paper_notes/TEMPLATE.md) when extended analysis is useful.

### Classification Review Process

1. One contributor enters candidate metadata with `verified=false`.
2. Two different reviewers independently add rows to [`data/paper_reviews.csv`](data/paper_reviews.csv).
3. Each reviewer answers all seven inclusion questions, proposes a scope, records confidence, writes a rationale, and identifies evidence locations.
4. `approved=true` means that the individual review is complete and formally valid; it does not mean that reviewers agree.
5. Preserve every original proposed scope and confidence, including disagreement and additional third-reviewer evidence.
6. Record the final scope, confidence, consensus date, and resolution rationale in `papers.csv`.
7. Set `verified=true` only when at least two different approved reviews and complete final-consensus metadata exist. Do not overwrite reviews to manufacture agreement.

> `verified=true` means that the metadata and classification rationale have been manually checked. It does not mean that the paper's claims or experimental results have been independently reproduced.

### Correcting Metadata or Classification

Identify the record and old/new values, cite supporting sources, and explain any proposed scope change. Classification changes should address state, transition, rollout, downstream use, and centrality of dynamics.

### Recording Screening Decisions

Use a unique `screening_id` for every row and at most one row per `(candidate_id, stage)`. A candidate may have separate `title_abstract` and `full_text` records. Two completed reviewers must be different people; non-pending consensus requires both non-pending decisions, and exclusion requires a reason.

### Adding Resources

- Related repositories go in [`data/repositories.csv`](data/repositories.csv).
- Datasets go in [`data/datasets.csv`](data/datasets.csv).
- Metrics and narrative context belong under [`resources/`](resources/README.md).
- Record a verified official URL, license/access constraints when known, and a last-checked date.

### Adding Reproduction Reports

Copy [`reproduction/REPRODUCTION_TEMPLATE.md`](reproduction/REPRODUCTION_TEMPLATE.md) into `reproduction/reports/`. Distinguish official from third-party implementations and document environments, data splits, metric definitions, deviations, failures, and missing details.

## Run Validation

```bash
python3 scripts/validate_metadata.py
python3 scripts/generate_paper_tables.py
python3 scripts/generate_repository_table.py
git diff
```

The vocabulary, entity CSVs, and review-provenance CSVs under `data/` are the structured sources of truth. After editing them, validate, regenerate Markdown, inspect the diff and status manually, and submit source and generated outputs together. Do not manually edit data rows in `papers/generated/` or `resources/generated_related_repositories.md`.

On macOS and some local systems, use `python3`. GitHub Actions configures Python 3.11 and invokes the same scripts with `python`. No pandas or other third-party package is required.

Every pull request automatically checks script syntax, vocabularies, metadata, review consensus, and generated-file consistency. A pull request fails when regeneration changes a tracked file or creates an untracked file.

## Pull Request Checklist

- [ ] Factual claims have reliable sources.
- [ ] No citation, link, or result is fabricated.
- [ ] Unresolved values are marked `TODO` and unverified.
- [ ] Classification rationale is documented where relevant.
- [ ] Search and screening provenance is recorded where relevant.
- [ ] Controlled values and semicolon-delimited multi-value fields follow `vocabularies.json`.
- [ ] CSV is treated as the source of truth.
- [ ] Validation scripts pass.
- [ ] Generated files were regenerated and included when structured data changed.
- [ ] I made no manual data edits to generated files.
- [ ] `verified=true` was set only after two different approved reviews and complete final-consensus metadata.
- [ ] Independent reviewer judgments were preserved rather than rewritten to match consensus.
- [ ] Reproduction claims disclose deviations and failures.
- [ ] I made no claim of successful reproduction without a reproduction report.

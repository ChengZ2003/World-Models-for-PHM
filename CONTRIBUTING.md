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

1. Apply the seven questions in [`taxonomy/inclusion_criteria.md`](taxonomy/inclusion_criteria.md).
2. Add a unique record to [`data/papers.csv`](data/papers.csv).
3. Verify the title, authors, year, venue, official paper URL, code URL, task, datasets, mechanism, and scope classification.
4. Explain borderline decisions in `notes` or a paper note based on [`paper_notes/TEMPLATE.md`](paper_notes/TEMPLATE.md).

### Classification Review Process

1. One contributor enters the metadata.
2. The contributor answers all seven inclusion questions.
3. The contributor proposes a scope classification.
4. The contributor writes a mechanism-based classification rationale.
5. The contributor records the scope confidence.
6. At least one other maintainer or reviewer checks the metadata and rationale before `verified=true` is set.
7. When disagreement remains, use `world_model_scope=uncertain` and `scope_confidence=low`; do not force a category through argument alone.

> `verified=true` means that the metadata and classification rationale have been manually checked. It does not mean that the paper's claims or experimental results have been independently reproduced.

### Correcting Metadata or Classification

Identify the record and old/new values, cite supporting sources, and explain any proposed scope change. Classification changes should address state, transition, rollout, downstream use, and centrality of dynamics.

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

The four files under `data/` are the structured sources of truth. After editing a CSV, validate it, regenerate Markdown, inspect the diff manually, and submit both the CSV and generated outputs. Do not manually edit data rows in `papers/generated/` or `resources/generated_related_repositories.md`.

On macOS and some local systems, use `python3`. GitHub Actions configures Python 3.11 and invokes the same scripts with `python`. No pandas or other third-party package is required.

Every pull request automatically checks script syntax, metadata, and generated-file consistency. A pull request fails when regeneration changes a committed generated file.

## Pull Request Checklist

- [ ] Factual claims have reliable sources.
- [ ] No citation, link, or result is fabricated.
- [ ] Unresolved values are marked `TODO` and unverified.
- [ ] Classification rationale is documented where relevant.
- [ ] CSV is treated as the source of truth.
- [ ] Validation scripts pass.
- [ ] Generated files were regenerated and included when structured data changed.
- [ ] I made no manual data edits to generated files.
- [ ] `verified=true` was set only after manual checking by another reviewer.
- [ ] Reproduction claims disclose deviations and failures.
- [ ] I made no claim of successful reproduction without a reproduction report.

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
python scripts/validate_metadata.py
python scripts/generate_paper_tables.py
python scripts/generate_repository_table.py
```

Generated paper tables contain only `verified=true` records. Review changed Markdown and relative links before submitting.

## Pull Request Checklist

- [ ] Factual claims have reliable sources.
- [ ] No citation, link, or result is fabricated.
- [ ] Unresolved values are marked `TODO` and unverified.
- [ ] Classification rationale is documented where relevant.
- [ ] Validation and generators pass.
- [ ] Generated changes are included when structured data changes.
- [ ] Reproduction claims disclose deviations and failures.

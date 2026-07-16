# Scripts

These tools use only the Python standard library and resolve default paths from the repository root.

```bash
python scripts/validate_metadata.py
python scripts/generate_paper_tables.py --input data/papers.csv --output-dir papers/generated
python scripts/generate_repository_table.py --input data/repositories.csv --output resources/generated_related_repositories.md
```

Validation returns a nonzero exit code for schema or record errors. Generators include only `verified=true` records and mark outputs as generated. They refuse to overwrite an existing file that lacks the generated marker.

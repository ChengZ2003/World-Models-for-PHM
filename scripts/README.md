# Scripts

These tools use only the Python standard library and resolve default paths from the repository root.

```bash
python3 scripts/validate_metadata.py
python3 scripts/generate_paper_tables.py
python3 scripts/generate_repository_table.py
git diff
```

Standard workflow:

1. Edit the relevant CSV under `data/`.
2. Run metadata validation.
3. Regenerate the Markdown views.
4. Inspect `git diff` manually.
5. Commit the CSV and generated files together.

Validation returns a nonzero exit code for schema or record errors. Generators include only `verified=true` records, produce deterministic output, and refuse to overwrite a Markdown file that lacks the generated marker.

Some local systems expose Python only as `python3`. GitHub Actions uses `python` after configuring Python 3.11. Both run the same standard-library scripts, and the project does not depend on pandas.

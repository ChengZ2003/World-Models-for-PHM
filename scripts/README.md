# Scripts

These tools use only the Python standard library and resolve default paths from the repository root.

```bash
python3 scripts/validate_metadata.py
python3 scripts/generate_paper_tables.py
python3 scripts/generate_repository_table.py
git diff
```

Standard workflow:

1. Record the search run and dual screening decisions.
2. Add candidate metadata with `verified=false`.
3. Add independent classification reviews without rewriting disagreements.
4. Record the final consensus fields in `papers.csv` and set `verified=true` only after validation requirements are met.
5. Run metadata validation and regenerate Markdown views.
6. Inspect `git diff` and `git status --short` manually.
7. Commit structured sources and generated files together.

Validation loads `data/vocabularies.json`, checks seven CSV schemas, validates controlled and semicolon-delimited values, checks review/search foreign keys, preserves independent reviews, and enforces explicit final-consensus metadata. It returns a nonzero exit code for errors and reports a per-file summary.

The paper generator supports multiple semicolon-delimited tasks. A paper appears in each relevant task page but is counted once by paper ID in the index. Generators include only `verified=true` records, produce deterministic output, and refuse to overwrite a Markdown file that lacks the generated marker.

Some local systems expose Python only as `python3`. GitHub Actions uses `python` after configuring Python 3.11. Both run the same standard-library scripts, and the project does not depend on pandas.

CI checks both `git diff --exit-code` and an empty `git status --porcelain`, so newly generated untracked files cannot bypass consistency validation.

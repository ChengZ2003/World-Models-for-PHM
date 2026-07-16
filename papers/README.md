# Papers

[`../data/papers.csv`](../data/papers.csv) is the source of truth for structured paper records and final consensus classification, while [`../data/paper_reviews.csv`](../data/paper_reviews.csv) preserves independent reviewer judgments. Generated tables under [`generated/`](generated/index.md) include only papers backed by two approved reviews, complete consensus metadata, and `verified=true`; generated files must not be edited manually.

Handwritten topic pages contain task definitions, scope notes, inclusion considerations, and survey observations. They link to the generated index rather than maintaining separate paper lists.

Phase 1B has prepared seven unverified pilot candidates and evidence notes to test the candidate taxonomy. They remain excluded from generated verified-paper pages. Two human reviewers should follow the [`pilot review guide`](../docs/PILOT_REVIEW_GUIDE.md) independently; review-dependent findings belong in [`PILOT_FINDINGS.md`](../docs/PILOT_FINDINGS.md).

| Page | Focus |
| --- | --- |
| [`general_world_models.md`](general_world_models.md) | General concepts relevant to dynamic-state modeling |
| [`anomaly_detection.md`](anomaly_detection.md) | Current-window abnormality detection |
| [`anomaly_prediction.md`](anomaly_prediction.md) | Future anomaly risk and early warning |
| [`fault_diagnosis.md`](fault_diagnosis.md) | Fault type, location, or cause |
| [`fault_prognosis.md`](fault_prognosis.md) | Future degradation or failure evolution |
| [`health_assessment.md`](health_assessment.md) | Health-state estimation |
| [`rul_prediction.md`](rul_prediction.md) | Remaining-life estimation |
| [`predictive_maintenance.md`](predictive_maintenance.md) | Maintenance planning from predicted evolution |
| [`foundation_models.md`](foundation_models.md) | Pretraining and transfer for PHM dynamics |

After changing paper metadata, run the standard validation and generation workflow documented in [`../scripts/README.md`](../scripts/README.md) and submit the generated changes with the CSV.

```bash
python3 scripts/validate_metadata.py
python3 scripts/generate_paper_tables.py
python3 scripts/generate_repository_table.py
git diff
```

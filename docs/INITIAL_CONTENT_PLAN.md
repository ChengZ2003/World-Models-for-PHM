# Initial Content Plan

## Goal

Move the repository from a structure-only foundation to a minimum useful public release through small, manually reviewed batches. Correctness remains more important than count.

## Batch A — Related Repository Landscape

Target 6–10 verified repositories spanning:

- General world models
- PHM frameworks
- Anomaly-detection benchmarks
- RUL resources
- Predictive-maintenance resources
- Time-series foundation-model resources

For every record, manually verify the repository URL, current README focus, relationship to this project, and last-checked date.

### Completion Checklist

- [ ] Each target category has been reviewed
- [ ] URLs and current README scope have been manually checked
- [ ] Relationships are specific and non-promotional
- [ ] Generated repository output matches the CSV

## Batch B — Seed Papers

Target 10–20 verified papers without attempting exhaustive coverage. Select records that exercise strict world model, world-model-like, related predictive model, and uncertain classifications.

### Completion Checklist

- [ ] Each paper answers all seven inclusion questions
- [ ] Official paper and code sources are checked where available
- [ ] Classification rationale and confidence are recorded
- [ ] A second reviewer checks each record before `verified=true`
- [ ] Generated task pages match `data/papers.csv`

## Batch C — Seed Datasets

Target 3–5 verified datasets spanning anomaly detection, early warning, RUL, run-to-failure sequences, and industrial multivariate sensing. A dataset may cover more than one target.

### Completion Checklist

- [ ] Official URL and access procedure are checked
- [ ] License and redistribution status are recorded without inference
- [ ] Task, labels, sequence properties, and operating conditions are documented
- [ ] Last-checked dates are present

## Batch D — Paper Notes

Choose 2–3 representative verified papers and complete the full paper-note template. Prefer different scope classifications so the notes demonstrate the boundary logic.

### Completion Checklist

- [ ] Metadata and mechanism sections are complete
- [ ] Author claims and repository classification are separated
- [ ] Experimental protocol and reproducibility limitations are documented
- [ ] No result is described as reproduced without evidence

## Batch E — First Taxonomy Check

Use the seed papers to test whether the taxonomy can be applied consistently, where boundaries remain ambiguous, whether CSV fields are sufficient, and whether any taxonomy dimension should be simplified.

### Completion Checklist

- [ ] Borderline cases and reviewer disagreements are recorded
- [ ] Scope labels can be justified from mechanisms
- [ ] Missing or redundant CSV fields are identified
- [ ] Taxonomy changes are synchronized with survey terminology
- [ ] The first review outcome is documented without overstating validation

## Overall Completion Criteria

- [ ] Recommended content targets have been reviewed, or deviations are explained
- [ ] All verified records have second-review evidence
- [ ] Validation and generation scripts pass
- [ ] Generated files match structured sources
- [ ] README status and content counts reflect the actual repository
- [ ] Publication checklist has been reviewed by maintainers

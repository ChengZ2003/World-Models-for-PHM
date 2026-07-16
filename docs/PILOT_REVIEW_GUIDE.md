# Pilot Paper Review Guide

This guide supports independent human review of the Phase 1B pilot candidates. Candidate metadata and Codex-prepared note drafts are aids, not verified classifications. Reviewers must inspect the primary paper themselves.

## Reviewer Workflow

1. Read the abstract, method, experiments, and relevant appendix.
2. Check title, authors, venue, links, datasets, and code against official sources.
3. Answer q1-q7 independently with `yes`, `partial`, `no`, or `unknown`.
4. Propose `world_model_scope` and `scope_confidence` independently.
5. Record concise mechanism-based reasoning and precise evidence locations.
6. Mark the review `approved=true` only when every required field is complete and formally checked.
7. Do not inspect the other reviewer's judgment before completing the first review.
8. Discuss disagreements only after both independent rows have been recorded.
9. Record the final classification and complete consensus metadata in `data/papers.csv`.
10. Preserve both original rows in `data/paper_reviews.csv` unchanged, including disagreements.

An approved review means one review is complete; it does not mean the two reviewers agree. A verified paper requires two approved reviews from different people, complete final-consensus metadata, and a final scope/confidence pair proposed by at least one approved reviewer. Verification does not imply experimental reproduction.

## Suggested Review Assignment

| Paper ID | Reviewer A | Reviewer B | Status |
| --- | --- | --- | --- |
| `wm-failure-autonomous-inspection-2026` |  |  | Pending |
| `foundational-wm-bimanual-failures-2026` |  |  | Pending |
| `omni-anomaly-2019` |  |  | Pending |
| `mtad-gat-2020` |  |  | Pending |
| `rul-end-to-end-representations-2021` |  |  | Pending |
| `ensemble-rul-2023` |  |  | Pending |
| `functional-rul-2019` |  |  | Pending |

Do not add names here unless the reviewers have explicitly agreed to the assignment. Enter completed judgments only in `data/paper_reviews.csv`.

## Calibration Questions

- Is an explicit state representation necessary, or can a recurrent hidden state be sufficient?
- Does one-step forecasting qualify as a transition model?
- When is future prediction central, and when is it merely an auxiliary loss?
- Is direct scalar RUL regression ever a world model?
- Does multi-step rollout materially change `world_model_like` into `strict_world_model`?
- Does action conditioning make a model more world-model-like when the prediction horizon is one step?
- How should physics-informed state-space models be classified?
- Does predictive uncertainty strengthen classification when no future state is generated?
- Are industrial inspection, server telemetry, and robotics maintenance all inside the intended PHM boundary?

## Review Record Checklist

For each reviewer row, confirm:

- the reviewer identity is real and distinct from the other reviewer;
- the full text was inspected;
- q1-q7 are all answered;
- proposed scope and confidence reflect the reviewer's own judgment;
- rationale describes the mechanism rather than repeating the title;
- evidence locations are precise enough for another person to find;
- no other review row was overwritten to manufacture agreement.

## Consensus Checklist

After both independent reviews are approved:

- compare q1-q7, proposed scope, and confidence;
- preserve all original review values;
- document every material disagreement and how it was resolved;
- select a final scope/confidence pair that appears in at least one approved review;
- set `consensus_reached=true` and record the date and rationale;
- set `verified=true` only after metadata and all consensus requirements pass validation;
- keep reproduction status separate from metadata/classification verification.

## Pilot Completion Criteria

The pilot is complete only when:

- all selected papers have two independent approved reviews;
- disagreements and their resolution are documented;
- final consensus fields are complete;
- the taxonomy has been tested on every selected mechanism type;
- schema and controlled-vocabulary limitations are documented;
- no original reviewer decision has been overwritten;
- the findings document records the decision on schema freeze and systematic search.

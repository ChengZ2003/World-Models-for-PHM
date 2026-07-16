# Pilot Findings

This is a template for findings that require two independent human reviews. Candidate counts and preparation facts may be recorded now; agreement rates, conclusions, and freeze decisions remain TODO until the review is complete.

## Pilot Paper Distribution

Prepared candidates: **7**. Verified papers: **0**.

| Preliminary candidate grouping | Count | Human-confirmed count |
| --- | ---: | ---: |
| `strict_world_model` | 2 | TODO |
| `world_model_like` | 2 | TODO |
| `related_predictive_model` | 2 | TODO |
| `uncertain` | 1 | TODO |

These values are initial cataloging proposals, not review outcomes.

## Classification Agreement

| Measure | Result | Notes |
| --- | --- | --- |
| Exact scope agreement | TODO | Compute only after all independent reviews are approved. |
| Exact confidence agreement | TODO | TODO |
| q1-q7 agreement | TODO | Report per question and overall. |

## Scope Disagreements

| Paper ID | Reviewer proposals | Final resolution | Rationale recorded |
| --- | --- | --- | --- |
| TODO | TODO | TODO | TODO |

## Confidence Disagreements

| Paper ID | Reviewer confidences | Final confidence | Resolution note |
| --- | --- | --- | --- |
| TODO | TODO | TODO | TODO |

## Difficult q1-q7 Questions

| Question | Difficult mechanism | Evidence from pilot | Proposed clarification |
| --- | --- | --- | --- |
| TODO | TODO | TODO | TODO |

## Missing Metadata Fields

| Candidate field | Example need | Blocking? | Proposed action |
| --- | --- | --- | --- |
| TODO | TODO | TODO | TODO |

## Redundant Metadata Fields

| Field | Evidence of redundancy | Proposed action |
| --- | --- | --- |
| TODO | TODO | TODO |

## Controlled-Vocabulary Gaps

| Vocabulary | Observed gap | Current non-blocking encoding | Decision needed |
| --- | --- | --- | --- |
| `learning_objectives` | Direct scalar RUL regression has no dedicated value. | `unknown`, with the actual objective explained in the note and rationale. | Decide after dual review whether `direct_regression` is needed. |
| `repository_categories` | The candidate schema has no general time-series-library category distinct from foundation-model resources. | Include only repositories that fit an existing category; do not force a generic library into the landscape. | Decide whether future landscape coverage requires a migration. |

No schema migration is proposed in Phase 1B. These gaps do not block the current pilot.

## Taxonomy Ambiguities

| Ambiguity | Relevant pilot IDs | Human finding | Proposed clarification |
| --- | --- | --- | --- |
| One-step latent prediction versus strict world-model status | `wm-failure-autonomous-inspection-2026`; `foundational-wm-bimanual-failures-2026` | TODO | TODO |
| Conditional reconstruction versus learned transition | `omni-anomaly-2019` | TODO | TODO |
| Joint one-step forecasting and reconstruction | `mtad-gat-2020` | TODO | TODO |
| Direct or probabilistic scalar RUL prediction | `rul-end-to-end-representations-2021`; `ensemble-rul-2023`; `functional-rul-2019` | TODO | TODO |

## Proposed Schema Changes

| Proposal | Evidence across pilot papers | Compatibility impact | Decision |
| --- | --- | --- | --- |
| Add `direct_regression` to learning objectives | TODO after review | Requires vocabulary and documentation migration | TODO |
| Add a general time-series-library repository category | TODO after landscape review | Requires vocabulary and generated-view migration | TODO |

Do not implement proposals until the pilot is complete and a migration is explicitly approved.

## Decision on Schema Freeze

**TODO after all 6-8 pilot papers receive two independent reviews.** The current schema remains a Phase 1A candidate schema pending pilot validation.

## Decision on Full Systematic Search

**TODO after pilot completion.** The searches recorded in `data/search_runs.csv` are exploratory `pilot_search` activity and are not exhaustive.

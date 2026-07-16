# Ensemble Neural Networks for Remaining Useful Life (RUL) Prediction

## Metadata

- Authors: Abhishek Srinivasan; Juan Carlos Andresen; Anders Holst
- Year: 2023
- Venue: 4th Asia Pacific Conference of the Prognostics and Health Management Society
- Official paper source: https://arxiv.org/abs/2309.12445
- Official code source: not confirmed
- Tasks: probabilistic RUL prediction
- Datasets: NASA C-MAPSS FD001-FD003
- Tentative scope: `uncertain`
- Tentative confidence: `low`
- Verification status: pilot boundary candidate; metadata and classification await dual human review

## Claimed World Model Definition

The authors do not use the term “world model.” They propose an ensemble of LSTM predictors that separates aleatoric and epistemic components of predictive RUL uncertainty.

## Our Preliminary Classification

`uncertain` keeps the boundary visible for human calibration. The method models degradation history and produces a predictive distribution useful for maintenance risk, but the predicted object is scalar RUL rather than a future state trajectory. `related_predictive_model` may be the more defensible final classification.

## State Representation

Sliding windows of normalized sensor readings enter two-layer LSTMs. Their hidden features are implicit representations rather than an explicitly identified physical or latent health state.

## Transition or Dynamics Model

Temporal dependence is embedded in each LSTM, but the paper does not expose a reusable state transition or learn a next-state target.

## Rollout Capability

None. The ensemble aggregates distributions over RUL predictions; it does not generate degradation rollouts or counterfactual futures.

## Learning Objective

Each model estimates a predictive distribution. Ensemble aggregation and entropy-based formulas separate aleatoric and epistemic uncertainty. The direct regression objective lacks a dedicated controlled value and is recorded as `unknown`.

## Downstream Use

The authors motivate uncertainty separation for maintenance risk interpretation and data acquisition. Experiments evaluate point and interval metrics on C-MAPSS.

## Inclusion Questions

| Question | Draft answer | Evidence |
| --- | --- | --- |
| q1 | partial | Section IV-B LSTM hidden representation |
| q2 | partial | sequential dependence is implicit only |
| q3 | no | output is a scalar RUL distribution |
| q4 | yes | introduction and Section IV-C connect RUL to maintenance |
| q5 | no | uncertainty-aware regression is central |
| q6 | partial | aleatoric and epistemic uncertainty are explicit; rollout is absent |
| q7 | unknown | human review should decide whether probabilistic degradation prediction is sufficient |

## Evidence Table

| Claim | Evidence location | Preliminary interpretation |
| --- | --- | --- |
| State representation | Section IV-A-B | Sensor windows feed implicit LSTM state. |
| Transition mechanism | Section IV-B | No separately accessible transition is defined. |
| Future prediction | Equations 2-5 | Ensemble predicts a distribution over remaining life. |
| Downstream PHM use | Introduction; Section IV-C | Uncertainty supports risk-aware maintenance interpretation. |
| Dynamics centrality | Table II | Evaluation centers on RUL and interval quality. |

## Open Questions

- Should probabilistic scalar RUL remain `uncertain` or become `related_predictive_model`?
- Is uncertainty modeling alone enough to strengthen world-model status when rollout is absent?
- Verify venue metadata and any official code release independently.

## Verification Status

- Metadata verified by two humans: no
- Two approved classification reviews: no
- Final consensus: no
- Results reproduced: no
- Last checked: 2026-07-16

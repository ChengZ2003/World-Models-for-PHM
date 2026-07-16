# Remaining Useful Life Estimation Using Functional Data Analysis

## Metadata

- Authors: Qiyao Wang; Shuai Zheng; Ahmed Farahat; Susumu Serita; Chetan Gupta
- Year: 2019
- Venue: 2019 IEEE International Conference on Prognostics and Health Management
- Official paper source: https://arxiv.org/abs/1904.06442
- Official code source: not confirmed
- Tasks: RUL prediction
- Datasets: NASA C-MAPSS
- Tentative scope: `related_predictive_model`
- Tentative confidence: `high`
- Verification status: pilot boundary candidate; metadata and classification await dual human review

## Claimed World Model Definition

The authors do not use the term “world model.” They formulate sensor histories as functional observations and learn a functional multilayer perceptron for direct RUL estimation.

## Our Preliminary Classification

`related_predictive_model` is proposed because continuous sensor curves encode degradation history, but the model maps those curves directly to scalar RUL. It has no explicit state-transition model and no future-state rollout.

## State Representation

Each sensor history is treated as a realization of an underlying continuous random process. Functional principal components and learned weight functions summarize within-equipment temporal correlation and across-equipment variation.

## Transition or Dynamics Model

No transition is learned. The covariance and basis functions describe correlations over the observed interval rather than a mechanism that advances state.

## Rollout Capability

None. For a newly observed time window, the functional MLP directly estimates RUL.

## Learning Objective

Functional-neuron weights and downstream numerical layers are optimized for RUL estimation. Because direct scalar regression is not a candidate controlled value, `learning_objective=unknown` is used pending pilot findings.

## Downstream Use

The scalar estimate supports RUL prognosis and predictive maintenance. Evaluation reports RMSE and the asymmetric PHM score on four C-MAPSS subsets.

## Inclusion Questions

| Question | Draft answer | Evidence |
| --- | --- | --- |
| q1 | yes | Section II-A represents sensors as continuous processes |
| q2 | partial | correlations are modeled but no transition operator is learned |
| q3 | no | model predicts scalar RUL rather than future system state |
| q4 | yes | Sections II-C and III evaluate RUL |
| q5 | no | functional regression is central |
| q6 | no | no rollout uncertainty or counterfactual mechanism |
| q7 | no | mechanism is functional regression rather than a world model |

## Evidence Table

| Claim | Evidence location | Preliminary interpretation |
| --- | --- | --- |
| State representation | Section II-A | Sensor histories are continuous functional observations. |
| Transition mechanism | Equations 3-5 | Covariance bases encode correlation but not state evolution. |
| Future prediction | Figure 2; Section II-C | Functional MLP outputs RUL directly. |
| Downstream PHM use | Table III | C-MAPSS RUL estimation is the sole downstream task. |
| Dynamics centrality | Figure 2 | Direct functional regression is central; rollout is absent. |

## Open Questions

- Confirm that this remains a boundary reference rather than a world-model-like method.
- Decide whether `direct_regression` should be added to learning objectives after pilot review.
- Confirm any official implementation or data-preparation code.

## Verification Status

- Metadata verified by two humans: no
- Two approved classification reviews: no
- Final consensus: no
- Results reproduced: no
- Last checked: 2026-07-16

# Learning Representations with End-to-End Models for Improved Remaining Useful Life Prognostic

## Metadata

- Authors: Alaaeddine Chaoub; Alexandre Voisin; Christophe Cerisara; Benoît Iung
- Year: 2021
- Venue: PHM Society European Conference
- Official paper source: https://papers.phmsociety.org/index.php/phme/article/view/2785
- Official code source: not confirmed
- Tasks: RUL prediction
- Datasets: NASA C-MAPSS FD001-FD004
- Tentative scope: `related_predictive_model`
- Tentative confidence: `high`
- Verification status: pilot boundary candidate; metadata and classification await dual human review

## Claimed World Model Definition

The authors do not use the term “world model.” The contribution is an end-to-end MLP-LSTM-MLP architecture for direct RUL regression.

## Our Preliminary Classification

`related_predictive_model` is proposed because the network learns degradation-related features and temporal smoothing, but its output is a scalar RUL at each observed time. It does not predict future system states or expose a transition model for rollout.

## State Representation

The first MLP maps each raw sensor frame to learned features. The paper shows that several features trend with degradation, while the LSTM smooths them through time.

## Transition or Dynamics Model

Temporal dependence is implicit in the LSTM hidden state. There is no separately trained state transition, physical degradation law, or next-state objective.

## Rollout Capability

None. A forward pass over observations returns current scalar RUL estimates; the model is not rolled forward to synthesize a degradation trajectory.

## Learning Objective

The final MLP directly regresses RUL. The present candidate vocabulary has no direct scalar-regression objective, so `learning_objective=unknown` is used without changing the schema.

## Downstream Use

Predicted RUL is intended to inform maintenance timing. Experiments report RMSE and the asymmetric PHM competition score on C-MAPSS.

## Inclusion Questions

| Question | Draft answer | Evidence |
| --- | --- | --- |
| q1 | partial | Figure 1 learned per-frame representation |
| q2 | partial | LSTM captures dependencies but no explicit transition is learned |
| q3 | no | output is direct scalar RUL rather than a future state |
| q4 | yes | Section 4.3 evaluates RUL prognosis |
| q5 | no | direct regression is central rather than dynamics rollout |
| q6 | no | no rollout uncertainty or counterfactual analysis |
| q7 | no | mechanism is best described as sequence-to-RUL regression |

## Evidence Table

| Claim | Evidence location | Preliminary interpretation |
| --- | --- | --- |
| State representation | Figure 1; Figures 5-6 | MLP features summarize sensor frames and degradation trends. |
| Transition mechanism | Section 3 | LSTM smooths history but is not exposed as a transition model. |
| Future prediction | Figure 1 caption | Each observed prefix maps directly to an RUL scalar. |
| Downstream PHM use | Sections 4.1 and 4.3 | RUL estimates are evaluated for turbofan prognosis. |
| Dynamics centrality | Section 3 | Regression performance rather than state evolution is central. |

## Open Questions

- Confirm that direct RUL regression remains a useful boundary example rather than an included world-model method.
- Decide whether the controlled vocabulary needs a `direct_regression` learning objective after the pilot.
- Confirm whether official code exists.

## Verification Status

- Metadata verified by two humans: no
- Two approved classification reviews: no
- Final consensus: no
- Results reproduced: no
- Last checked: 2026-07-16

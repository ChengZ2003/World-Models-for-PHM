# World Model Failure Classification and Anomaly Detection for Autonomous Inspection

## Metadata

- Authors: Michelle Ho; Muhammad Fadhil Ginting; Isaac R. Ward; Andrzej Reinke; Mykel J. Kochenderfer; Ali-akbar Agha-Mohammadi; Shayegan Omidshafiei
- Year: 2026
- Venue: arXiv preprint
- Official paper source: https://arxiv.org/abs/2602.16182
- Official code source: https://github.com/autoinspection-classification/GaugeFailClassification
- Tasks: anomaly detection (online or anticipatory failure detection during an evolving trajectory)
- Datasets: gauge-inspection videos collected in office and industrial environments
- Tentative scope: `strict_world_model`
- Tentative confidence: `low`
- Verification status: pilot candidate; metadata and classification await dual human review

## Claimed World Model Definition

The authors explicitly call the predictive backbone a world model. They describe a Cosmos encoder, a learned latent next-frame model, and a decoder that reconstructs the next video frame. The paper does not give a general PHM definition of a world model.

## Our Preliminary Classification

`strict_world_model` is a deliberately debatable pilot proposal. The method has an explicit compressed state and a learned temporal predictor whose residuals support online failure and OOD detection. It can detect a developing failure earlier than a human observer, but the paper does not define a separately labelled future gap or prediction horizon matching this repository's formal anomaly-prediction protocol. The demonstrated transition is one-step, action conditioning is absent, and no planning or counterfactual rollout is evaluated. Human reviewers should decide whether these limitations instead imply `world_model_like`.

## State Representation

The video frame is compressed and tokenized by the pretrained NVIDIA Cosmos tokenizer. Its latent tokens represent the inspection scene; the paper stores consecutive latent pairs for some conformal scores.

## Transition or Dynamics Model

A latent world model predicts the next latent from the current encoded frame. The decoded result is a next-frame reconstruction. Section III-E and Figure 3 present an explicit but one-step transition; the fixed robot pose means the model is not action conditioned.

## Rollout Capability

Only one-step next-frame prediction is demonstrated. The paper does not establish autoregressive multi-step simulation, multiple futures, counterfactuals, or planning support.

## Learning Objective

Equation 7 combines a weighted pixel reconstruction term, temporal-consistency regularization, perceptual similarity, and a weak center-region prior. Separate success and failure models are trained and their scores are calibrated with conformal thresholds.

## Downstream Use

Prediction and latent residual scores are used with two calibrated decision functions to classify an inspection trajectory as success, known failure, or OOD anomaly. The method provides online or anticipatory detection as evidence accumulates during an evolving operation and may detect failure before a human observer. This timing advantage is not treated as the separate `anomaly_prediction` task because the paper does not specify the repository's formal future-window mapping from an observed history to anomaly probability over a future gap and horizon.

## Inclusion Questions

| Question | Draft answer | Evidence |
| --- | --- | --- |
| q1: dynamic-system state representation | yes | Figure 3; Section III-E |
| q2: learned transition mechanism | yes | Section III-E; latent prediction `z[t+1]` |
| q3: future-state prediction or simulation | yes | next-frame prediction in Figure 3 |
| q4: future evolution used for PHM | partial | Table I; Section IV uses next-frame residuals for online failure/OOD detection, not a labelled future anomaly horizon |
| q5: dynamics central rather than auxiliary | yes | world-model scores drive classification |
| q6: rollout uncertainty or counterfactual support | partial | conformal calibration is present; multi-step and counterfactual rollout are absent |
| q7: mechanism meaningful without terminology | partial | predictive latent mechanism is substantive but strict status is debatable |

## Evidence Table

| Claim | Evidence location | Preliminary interpretation |
| --- | --- | --- |
| State representation | Figure 3; Section III-E | Cosmos tokens form the compressed scene state. |
| Transition mechanism | Figure 3; Section III-E | Learned latent predictor advances to the next frame. |
| Future prediction | Equation 7 | Training explicitly scores predicted against ground-truth next frames. |
| Downstream PHM use | Table I; Section IV | Prediction and latent deviations become online failure/OOD scores; earlier detection is not formal future-window anomaly prediction. |
| Dynamics centrality | Figure 5; Section III-F | Calibrated world-model scores are central to the decision rule. |

## Open Questions

- Should one-step visual prediction without actions satisfy the strict category?
- Decide whether a future repository category should distinguish anticipatory online detection from explicit future-window anomaly prediction.
- Review whether the industrial gauge task falls inside the repository's PHM boundary or is adjacent inspection reliability.
- Verify the released code and subset data independently; no reproduction is claimed.

## Verification Status

- Metadata verified by two humans: no
- Two approved classification reviews: no
- Final consensus: no
- Results reproduced: no
- Last checked: 2026-07-16

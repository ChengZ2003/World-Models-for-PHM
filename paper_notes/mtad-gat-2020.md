# Multivariate Time-Series Anomaly Detection via Graph Attention Network

## Metadata

- Authors: Hang Zhao; Yujing Wang; Juanyong Duan; Congrui Huang; Defu Cao; Yunhai Tong; Bixiong Xu; Jing Bai; Jie Tong; Qi Zhang
- Year: 2020
- Venue: 2020 IEEE International Conference on Data Mining
- Official paper source: https://arxiv.org/abs/2009.02040
- Official code source: not confirmed; known third-party implementations are not recorded as official code
- Tasks: multivariate time-series anomaly detection and diagnosis
- Datasets: SMAP; MSL; proprietary TSA dataset
- Tentative scope: `world_model_like`
- Tentative confidence: `low`
- Verification status: pilot candidate; metadata and classification await dual human review

## Claimed World Model Definition

The authors do not use the term “world model.” They describe a self-supervised anomaly-detection framework combining graph attention, recurrent encoding, next-timestamp forecasting, and reconstruction.

## Our Preliminary Classification

`world_model_like` is a low-confidence proposal because next-state prediction is explicit and feeds the anomaly score, while graph and recurrent features represent multivariate temporal state. The forecast is limited to one timestamp and is jointly optimized with reconstruction, making `related_predictive_model` a plausible alternative.

## State Representation

Feature-oriented and time-oriented graph attention layers encode cross-variable and within-window temporal dependencies. Their outputs are concatenated with convolved inputs and passed through a GRU.

## Transition or Dynamics Model

The GRU representation feeds a deterministic forecasting head that predicts the next multivariate timestamp. The paper does not define a standalone reusable transition operator.

## Rollout Capability

Only one-step prediction is shown. No autoregressive multi-step, probabilistic-future, counterfactual, or planning experiment is reported.

## Learning Objective

Section III-D jointly optimizes forecasting RMSE and sequence reconstruction error. At inference, forecast and reconstruction errors are combined into anomaly scores.

## Downstream Use

The combined errors detect anomalies; feature-level errors and attention structure support diagnosis. Experiments cover spacecraft telemetry and a proprietary service dataset.

## Inclusion Questions

| Question | Draft answer | Evidence |
| --- | --- | --- |
| q1 | partial | Figure 2 graph/GRU representation |
| q2 | yes | forecasting head predicts the next timestamp |
| q3 | yes | Section III-D one-step forecast |
| q4 | yes | Equations 7-8 anomaly inference score |
| q5 | partial | forecasting is one of two joint objectives |
| q6 | no | no multi-step uncertainty or counterfactual mechanism |
| q7 | partial | mechanism has dynamics but lacks simulation capability |

## Evidence Table

| Claim | Evidence location | Preliminary interpretation |
| --- | --- | --- |
| State representation | Figure 2; Section III-B | Graph attention and GRU encode multivariate history. |
| Transition mechanism | Section III-D | Forecasting head maps representation to the next timestamp. |
| Future prediction | Equation 5 | Objective directly trains next-step prediction. |
| Downstream PHM use | Equations 7-8; Table III | Forecast/reconstruction deviations form anomaly scores. |
| Dynamics centrality | Section III-D | Forecasting is central but shares weight with reconstruction. |

## Open Questions

- Should a one-step forecast used in a joint loss be world-model-like or merely related predictive modeling?
- Confirm whether Microsoft or the authors released official code.
- Review dataset relevance: SMAP and MSL are cyber-physical telemetry; TSA is proprietary.

## Verification Status

- Metadata verified by two humans: no
- Two approved classification reviews: no
- Final consensus: no
- Results reproduced: no
- Last checked: 2026-07-16

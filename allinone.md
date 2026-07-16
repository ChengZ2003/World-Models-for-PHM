# Phase 1B Pilot Paper Search Log

This log records the complete output of one exploratory multi-source query run on 2026-07-16. It is not a systematic-search result, does not establish inclusion, and must not be treated as a verified-paper list.

- Query: `world model latent dynamics anomaly detection prognostics remaining useful life industrial`
- Date range: 2024-2026
- Maximum returned per source: 5

Search warning: `open_alex` was unavailable because its client import failed with `unsupported operand type(s) for |: 'type' and 'NoneType'`. The local Python TLS stack also emitted a `NotOpenSSLWarning`, and the search service reported one rate-limit wait of three seconds.

## Semantic Scholar (5 papers)

| # | Title | Date | Venue | Citations |
| --- | --- | --- | --- | ---: |
| 1 | [Koopman-Informed Neural Network for Machinery's Nonlinear Dynamics Learning and Remaining Useful Life Prediction](https://www.semanticscholar.org/paper/8cba77290110a5c79c2d5c5b400a0a4495983600) | 2025 | IEEE Transactions on Instrumentation and Measurement | 6 |
| 2 | [Enhanced Remaining Useful Life Prediction for Turbofan Engines Using Spatiotemporal Koopman Dual-Branch Transformer](https://www.semanticscholar.org/paper/b931f85f55691deafacb2cbc4dc3931b3cdef5f2) | 2025 | IEEE Transactions on Instrumentation and Measurement | 3 |
| 3 | [Edge-Based Stochastic Koopman-Lyapunov Graph for Anomaly Detection and RUL Prediction in Turbofan Engines](https://www.semanticscholar.org/paper/1bdf811ed687b8b84c5c3a078f8d480f04e8bcce) | 2026 | Quality and Reliability Engineering International | 0 |
| 4 | [Predictive Maintenance of Sensors: A Machine Learning Approach for Proactive Anomaly Detection](https://www.semanticscholar.org/paper/0620dc6f4aa34426b4eda98948b602a372960edd) | 2025 | International Journal for Research in Applied Science and Engineering Technology | 0 |
| 5 | [Physically-Constrained Mamba-SDE for Remaining Useful Life Prediction under Irregular Observations](https://www.semanticscholar.org/paper/9fc8dd33d969c7539c835f6baa4b13e1d0c7dc24) | 2026 | Venue not returned | 0 |

## OpenAlex (0 papers)

No results were available because the source client failed before the query completed. No zero-result claim is made for OpenAlex.

## arXiv (5 papers)

| # | Title | Date | Venue | Citations |
| --- | --- | --- | --- | ---: |
| 1 | [Latent-Y: A Lab-Validated Autonomous Agent for De Novo Drug Design](http://arxiv.org/abs/2603.29727v2) | 2026 | arXiv | 0 |
| 2 | [Latent-X: An Atom-level Frontier Model for De Novo Protein Binder Design](http://arxiv.org/abs/2507.19375v1) | 2025 | arXiv | 0 |
| 3 | [Large Interferometer For Exoplanets (LIFE): XIII. The Value of Combining Thermal Emission and Reflected Light for the Characterization of Earth Twins](http://arxiv.org/abs/2406.13037v1) | 2024 | arXiv | 0 |
| 4 | [Multi-Flow: Multi-View-Enriched Normalizing Flows for Industrial Anomaly Detection](http://arxiv.org/abs/2504.03306v1) | 2025 | arXiv | 0 |
| 5 | [Drug-like antibodies with low immunogenicity in human panels designed with Latent-X2](http://arxiv.org/abs/2512.20263v1) | 2025 | arXiv | 0 |

## OpenReview (0 papers)

No matches were returned for this narrow query and date window.

## Crossref (5 papers)

| # | Title | Date | Venue | Citations |
| --- | --- | --- | --- | ---: |
| 1 | [Sequential Deep Learning Model Development for Battery Remaining Useful Life Forecasting and Anomaly Detection](https://doi.org/10.1109/iciea61579.2024.10664735) | 2024 | IEEE ICIEA | 1 |
| 2 | [Blade-Tip Vibration Informed Latent Physics Residual Prognostics for Fatigue Crack Growth and Remaining Useful Life Prediction](https://doi.org/10.2139/ssrn.7024553) | Date not returned | Venue not returned | 0 |
| 3 | [Continuous-Depth Latent State Modeling for Predicting Turbofan Engine Remaining Useful Life](https://doi.org/10.1109/icphm69567.2026.11585276) | 2026 | IEEE ICPHM | 0 |
| 4 | [Remaining Useful Life Estimation Based on the System Trajectory in a Latent Space Representation](https://doi.org/10.1109/phm61473.2024.00075) | 2024 | PHM Conference | 1 |
| 5 | [High-Precision Prognostics of PEMFC Remaining Useful Life via VMD-IASO-BiLSTM](https://doi.org/10.21203/rs.3.rs-7700778/v1) | Date not returned | Venue not returned | 0 |

## DBLP (0 papers)

No matches were returned for this narrow query and date window.

## Model Knowledge (0 papers)

No unverified model-recalled entries were added. Older pilot candidates were instead identified through targeted primary-source searches and snowballing recorded in `data/search_runs.csv`.

## Overview

The query returned 15 records from Semantic Scholar, arXiv, and Crossref. It had high lexical noise around “latent” and poor recall for established anomaly-detection and RUL work, so it was used only as a seed for targeted searches and full-text screening.

## Trends

The relevant results concentrate on RUL, Koopman representations, probabilistic degradation, and industrial anomaly detection. The arXiv results demonstrate substantial query drift, while Semantic Scholar and Crossref returned the most mechanism-relevant candidates.

## Key Themes

1. Koopman and latent dynamics for turbofan RUL: Semantic Scholar 1-3.
2. Probabilistic or physically constrained RUL: Semantic Scholar 3 and 5; Crossref 2-3.
3. Direct RUL forecasting and latent trajectory representations: Crossref 1 and 4-5.
4. Industrial anomaly detection: arXiv 4; Crossref 1; Semantic Scholar 4.
5. Query drift from generic “latent” terminology: arXiv 1-3 and 5.

## Keywords Frequency

Counts below are simple title-level counts across the 15 returned records.

| Keyword | Count |
| --- | ---: |
| Remaining useful life / RUL | 9 |
| Latent | 5 |
| Anomaly detection | 4 |
| Koopman | 3 |
| Prognostics | 2 |

## Most Cited by Accepted Paper

Citation counts are those returned by the search APIs and may lag publishers.

| Rank | Title | Year | Citations |
| ---: | --- | ---: | ---: |
| 1 | Koopman-Informed Neural Network for Machinery's Nonlinear Dynamics Learning and Remaining Useful Life Prediction | 2025 | 6 |
| 2 | Enhanced Remaining Useful Life Prediction for Turbofan Engines Using Spatiotemporal Koopman Dual-Branch Transformer | 2025 | 3 |
| 3 | Sequential Deep Learning Model Development for Battery Remaining Useful Life Forecasting and Anomaly Detection | 2024 | 1 |
| 4 | Remaining Useful Life Estimation Based on the System Trajectory in a Latent Space Representation | 2024 | 1 |
| 5 | Edge-Based Stochastic Koopman-Lyapunov Graph for Anomaly Detection and RUL Prediction in Turbofan Engines | 2026 | 0 |

## Most Cited by First Author

| Rank | Author | Papers in set | Total citations |
| ---: | --- | ---: | ---: |
| 1 | Enxiu Wang | 1 | 6 |
| 2 | Eden Kim | 1 | 3 |
| 3 | Manohara MM Pai | 1 | 1 |
| 4 | Adaiton Oliveira-Filho | 1 | 1 |
| 5 | Sasmita Pani | 1 | 0 |

## Recommendations for Reading

1. Koopman-Informed Neural Network for Machinery's Nonlinear Dynamics Learning and RUL Prediction - the closest returned match to explicit learned machinery dynamics.
2. Remaining Useful Life Estimation Based on the System Trajectory in a Latent Space Representation - useful for testing the latent-trajectory boundary.
3. Continuous-Depth Latent State Modeling for Predicting Turbofan Engine Remaining Useful Life - relevant to continuous-depth state evolution, subject to full-text availability.
4. Sequential Deep Learning Model Development for Battery Remaining Useful Life Forecasting and Anomaly Detection - bridges anomaly detection and RUL but may be primarily direct prediction.
5. Physically-Constrained Mamba-SDE for Remaining Useful Life Prediction under Irregular Observations - relevant to physics and stochastic dynamics, but too recent for inclusion without further source checking.

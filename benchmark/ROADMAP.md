# Benchmark Engineering Roadmap

The goal is not to replace full PHM platforms, but to provide a focused evaluation layer for world-model-oriented research questions. All versions below are plans unless a release explicitly documents completion.

## v0.1 — Protocol Documents

- Anomaly detection protocol
- Early-warning protocol
- RUL protocol
- Data-leakage checklist
- Result-reporting schema
- Reproducibility checklist

## v0.2 — Minimal Evaluation Utilities

- Window generation
- Point-to-event conversion
- Event-level metrics
- Lead-time metrics
- Recall@K and capacity-constrained recall
- RUL regression metrics
- Calibration metrics

## v0.3 — Framework Adapters

- Stable adapter interface
- Existing-framework integration
- Dataset path configuration
- Prediction export format
- Evaluation-only workflow

## v0.4 — Representative Baselines

Candidate baselines are logistic regression, LightGBM, GRU, observation forecasting, latent prediction, and probabilistic rollout. Listing a baseline is not an implementation or result claim.

## v1.0 — Focused Public Evaluation Layer

Release requires stable protocols, tested metrics, at least two verified dataset adapters, reproducible baseline configurations, a versioned result format, documentation, and a contribution guide.

## Data and Integration Principles

Dataset redistribution is not assumed. Users must follow the original dataset licenses and access procedures. Adapters should integrate with maintained ecosystems before new infrastructure is built. No public leaderboard claim should be made without versioned protocols and reproducible submissions.

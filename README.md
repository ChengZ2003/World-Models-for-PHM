# World Models for PHM

**A Survey and Resource Hub for World Models in Anomaly Detection, Prognostics, and Remaining Useful Life Prediction**

A survey companion repository for studying how learned system states and temporal dynamics support prognostics and health management (PHM).

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Validate Repository](https://github.com/ChengZ2003/World-Models-for-PHM/actions/workflows/validate.yml/badge.svg)](https://github.com/ChengZ2003/World-Models-for-PHM/actions/workflows/validate.yml)

> **Current stage:** Repository foundation, taxonomy development, and initial literature verification.
> No public benchmark implementation or validated leaderboard is available yet.

## Overview

This repository supports a survey of world-model principles in anomaly detection, fault prognosis, remaining useful life (RUL) prediction, and PHM. It asks:

- How should a world model be defined in PHM?
- How are dynamic system states represented?
- How are state transitions and degradation processes learned?
- How are future rollouts used for anomaly detection or prognosis?
- How are uncertainty and multiple futures modeled?
- How can anomaly detection, early warning, and RUL be connected under a common dynamics perspective?

We use the following operational definition:

> A world model learns a representation of a dynamic system and its temporal transition mechanisms, enabling the prediction, generation, or simulation of possible future system states for downstream tasks such as anomaly detection, early warning, health assessment, remaining useful life prediction, and maintenance decision-making.

This repository complements rather than replaces existing world-model collections, PHM frameworks, anomaly-detection benchmarks, and RUL paper lists.

Our focus is how world-model principles are used to represent industrial system states, learn temporal dynamics, simulate future evolution, detect anomalies, predict degradation, and estimate remaining useful life.

## Motivation

General world-model collections often emphasize robotics, autonomous driving, video generation, or embodied intelligence. PHM frameworks generally emphasize training and evaluation infrastructure; anomaly-detection benchmarks emphasize detection protocols; and RUL collections emphasize prognosis literature. To the best of our current review, relatively few resources systematically examine the intersection of world models and PHM. This repository provides a mechanism-centered taxonomy, verified metadata workflow, reproduction index, and a future lightweight protocol layer for that intersection.

## Scope

### Included

- Industrial and cyber-physical systems and multivariate sensor systems
- Observation-space, latent, probabilistic, graph-structured, multimodal, and hybrid physical-latent state representations
- Temporal transitions, degradation processes, multi-step rollout, and action-conditioned or physics-informed dynamics
- Anomaly detection, anomaly prediction, early warning, fault prognosis, health assessment, RUL prediction, and maintenance decision support

### Out of Scope

- General image or video generation unrelated to PHM
- Pure classification without temporal dynamics and static tabular fault classifiers
- LLM-based maintenance report generation without system-dynamics modeling
- Generic reinforcement-learning world models unrelated to industrial reliability
- Standard forecasting papers with no relevance to PHM methodology

## Key Distinctions

| Task | Operational meaning |
| --- | --- |
| Anomaly detection | Identifies abnormality in the current or observed interval. |
| Anomaly prediction / early warning | Estimates whether an anomaly will occur in a future horizon. |
| Fault diagnosis | Identifies a fault type, location, or cause. |
| Fault prognosis | Predicts future degradation or failure evolution. |
| RUL prediction | Estimates the time remaining before a defined failure condition. |
| Maintenance decision-making | Uses predicted system evolution to select interventions. |

## World-Model Scope

- **Strict World Model:** explicit state representation and central dynamics model, normally with multi-step rollout and a role in simulation, planning, counterfactual reasoning, or decisions.
- **World-Model-Like Dynamics Model:** learns observation-space or latent transitions for future prediction, degradation modeling, or uncertainty estimation, but may not support explicit planning or counterfactual simulation.
- **Related Predictive Model:** forecasting, reconstruction, representation learning, or direct RUL regression included only when it provides useful methodological or historical context.

Classification follows the modeling mechanism rather than the terminology used by a paper. See the [inclusion criteria](taxonomy/inclusion_criteria.md).

## Taxonomy at a Glance

| Dimension | Categories |
| --- | --- |
| Representation space | Observation space; continuous latent; discrete latent/token; hybrid physical-latent; graph-structured; multimodal |
| Transition modeling | Deterministic; probabilistic; stochastic latent variable; state-space; autoregressive; non-autoregressive; action-conditioned; physics-informed; retrieval-augmented; continuous-time |
| Learning objective | Reconstruction; one-step prediction; multi-step prediction; latent prediction; contrastive prediction; masked modeling; generative likelihood; diffusion; uncertainty estimation; multi-task learning |
| Downstream task | Detection; early warning; diagnosis; health assessment; prognosis; RUL; maintenance planning |

The detailed taxonomy is maintained in [`taxonomy/`](taxonomy/README.md).

## Repository Value

This is more than a paper list. The repository is designed around verified metadata, explicit inclusion criteria, reproducibility status, task and method taxonomies, survey figures and tables, links to related repositories, lightweight protocol definitions, and transparent reporting of uncertainty and disagreement.

## Source of Truth

- **Controlled values:** `data/vocabularies.json` defines the frozen vocabulary used by structured fields.
- **Entity metadata:** `data/papers.csv`, `data/datasets.csv`, `data/methods.csv`, and `data/repositories.csv` are the sources of truth for literature and resource entities.
- **Review provenance:** `data/paper_reviews.csv`, `data/search_runs.csv`, and `data/screening.csv` are the sources of truth for classification reviews, searches, and screening decisions.
- **Generated views:** `papers/generated/` and `resources/generated_related_repositories.md` contain verified-only Markdown generated from CSV. Do not edit their data rows manually.
- **Handwritten pages:** task and landscape pages define scope, selection principles, inclusion considerations, and survey observations. They link to generated views instead of duplicating records.

## Paper Index

Real paper records are maintained in [`data/papers.csv`](data/papers.csv), the structured source of truth. The [generated paper index](papers/generated/index.md) contains only manually verified records. Handwritten task pages define scope and inclusion considerations; they do not duplicate paper tables.

## Related Projects

This repository builds on and complements existing efforts in general world models, predictive maintenance, PHM benchmarking, multivariate anomaly detection, and RUL literature curation. The structured landscape and its verification policy are in [`resources/related_repositories.md`](resources/related_repositories.md).

## Current Status

| Component | Status | Notes |
| --- | --- | --- |
| Repository structure | Available | Initial structure and contribution workflow |
| Terminology | Draft | Subject to refinement |
| Inclusion criteria | Draft | Requires validation on real papers |
| Search and screening methodology | Draft | Protocol defined; no completed search claimed |
| Verified literature database | In progress | Initial manual verification pending |
| Reproduction index | Planned | No reproduced result claimed |
| Benchmark protocols | Draft | Documentation only |
| Benchmark implementation | Not available | Future work |

## Repository Map

- [`papers/`](papers/README.md): manually curated topic pages and generated verified-paper tables
- [`taxonomy/`](taxonomy/README.md): definitions, inclusion criteria, and method dimensions
- [`resources/`](resources/README.md): datasets, metrics, projects, venues, and related repositories
- [`data/`](data/README.md): machine-readable metadata
- [`survey/`](survey/README.md): draft search method, outline, research questions, terminology, and figure plan
- [`reproduction/`](reproduction/README.md): reproduction reports and status tracking
- [`benchmark/`](benchmark/README.md): future lightweight protocol and evaluation layer
- [`docs/ROADMAP.md`](docs/ROADMAP.md): staged project roadmap
- [`docs/INITIAL_CONTENT_PLAN.md`](docs/INITIAL_CONTENT_PLAN.md): minimum useful-content batches

## How to Contribute

Contributions may submit a missing paper, correct metadata, discuss a classification, add a related repository, dataset, or metric, submit a reproduction report, improve the taxonomy, or report a broken link. Every factual record should cite an official or otherwise reliable source and clearly mark uncertainty. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Validation

```bash
python3 scripts/validate_metadata.py
python3 scripts/generate_paper_tables.py
python3 scripts/generate_repository_table.py
git diff
```

All scripts use only the Python standard library; the project does not depend on pandas. Some local environments, including macOS, expose Python as `python3`, while GitHub Actions uses `python` after setting up Python 3.11. Both execute the same scripts.

Every pull request automatically runs Python syntax compilation, vocabulary and metadata validation, table generation, tracked-file diff checks, and untracked-file checks. After changing structured data, regenerate the Markdown outputs, inspect the diff, and commit the source and generated files together.

## Survey Review Workflow

1. Execute a reviewed search query and record the search run.
2. Perform dual title/abstract and full-text screening.
3. Add candidate metadata with `verified=false`.
4. Have two different reviewers answer the seven inclusion questions independently.
5. Resolve scope disagreement and record consensus evidence.
6. Set `verified=true` only after two approved reviews agree with the paper classification.
7. Regenerate Markdown and let CI check source/generated consistency.

See the draft [search strategy](survey/search_strategy.md) and [inclusion criteria](taxonomy/inclusion_criteria.md). Verification covers metadata and classification review; it does not imply independent reproduction of experimental results.

## Citation

Citation metadata is provided in [`CITATION.cff`](CITATION.cff).

> TODO: Replace this placeholder with the final survey citation after publication.

## Disclaimer

This is an early-stage research resource and its taxonomy may evolve. Inclusion does not imply endorsement. Classification can be debatable, and recorded metadata should be independently verified before reuse. No experimental result should be added without reproducible evidence. The repository does not claim that its future benchmark layer is complete.

## License

Released under the [MIT License](LICENSE).

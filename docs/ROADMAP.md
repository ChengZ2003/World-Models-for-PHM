# Project Roadmap

This roadmap separates completed repository foundations from planned research and engineering. Correctness before coverage.

## Phase 0 — Repository Foundation

### Goals

- Define scope and terminology
- Establish the metadata schema and contribution workflow
- Add validation scripts and a related-repository landscape

### Completion Criteria

- README is publication-ready
- No fabricated references are present
- Metadata schemas are documented
- A taxonomy draft exists
- Validation scripts pass
- A public-release checklist is available

## Phase 1 — Verified Literature Collection

Manually collect candidates, separate strict world models from related predictive models, and verify official paper/code links, tasks, datasets, objectives, transitions, uncertainty, and classification confidence.

Suggested review milestones are 20, 40, and 60 verified papers, followed by a survey-aligned release. These are coordination markers, not quality targets. **Correctness before coverage.** At minimum verify title, year, venue, official paper URL, code URL, task, dataset, modeling mechanism, and scope classification.

## Phase 2 — Taxonomy and Survey Support

Refine the definition and produce an inclusion flowchart, taxonomy figure, task-relationship figure, historical timeline, method-task mapping, and evidence-based research gaps.

Planned outputs: taxonomy diagram, inclusion decision tree, timeline, dataset-task matrix, metric-task matrix, research-gap table, and open-challenge summary.

## Phase 3 — Reproduction Index

Build credible status records instead of immediately rewriting every method. Record official and third-party implementations, environment, dataset and checkpoint availability, status, issues, metric compatibility, license, and last verification date.

Statuses: Not evaluated; Code available; Environment built; Partial reproduction; Reproduced; Failed reproduction; Blocked by unavailable data; Blocked by missing implementation details.

## Phase 4 — Representative Reproductions

Select a small, informative set across observation forecasting, reconstruction, latent dynamics, probabilistic state-space modeling, world-model-based anomaly detection, world-model-like RUL, action-conditioned dynamics, and physics-informed dynamics. The first roadmap does not commit to reproducing dozens of models.

## Phase 5 — Protocol Layer

Define task protocols, window construction, leakage prevention, event-level evaluation, early-warning evaluation, RUL evaluation, and result reporting. Protocol documents precede a full software framework.

## Phase 6 — Integration with Existing Ecosystems

Explore adapters for PHM frameworks, evaluation modules for anomaly-detection benchmarks, world-model baselines for existing loaders, standard metadata/result formats, and upstream contributions.

> Integrate before rebuilding.

## Phase 7 — Lightweight Research Benchmark

Only after earlier phases stabilize, consider minimal dataset adapters, unified window generation, representative baselines, event-level/early-warning/RUL metrics, configuration files, and reproducible reports.

> The goal is not to replace full PHM platforms, but to provide a focused evaluation layer for world-model-oriented research questions.

## Phase 8 — Unified World Models for PHM

```text
Historical observations
        ↓
Dynamic system state
        ↓
Transition / rollout model
        ↓
Possible future trajectories
        ↓
Anomaly risk / health state / RUL / maintenance decision
```

Long-term directions include shared latent dynamics, joint anomaly and RUL modeling, multi-task world models, probabilistic rollout, uncertainty calibration, action-conditioned and physics-informed transitions, retrieval-augmented trajectory modeling, cross-machine transfer, counterfactual maintenance simulation, multimodal sensor and maintenance records, and foundation models for PHM.

## Roadmap Principles

- Correctness before coverage
- Mechanism before terminology
- Reproducibility before leaderboard performance
- Integration before rebuilding
- Event-level evaluation before point-wise optimization
- Transparent reporting of failed reproduction
- No fabricated results
- No benchmark claim without reproducible protocols
- Keep the survey taxonomy and code implementation consistent
- Record uncertainty when paper classification is debatable

## Progress Checklist

- [x] Establish repository structure
- [x] Draft operational definition and inclusion criteria
- [x] Add metadata validation and generation tooling
- [ ] Approve maintainer and citation placeholders
- [ ] Add first manually verified literature records
- [ ] Review taxonomy with domain experts
- [ ] Publish survey figures from verified data
- [ ] Populate the reproduction index
- [ ] Stabilize protocol specifications
- [ ] Implement and test minimal evaluation utilities
- [ ] Add verified framework and dataset adapters

# Figure Plan

| Figure | Purpose | Main elements | Expected message | Required data | Status | Source files |
| --- | --- | --- | --- | --- | --- | --- |
| Scope and inclusion | Explain selection boundaries | Seven questions, decision outcomes | Mechanism determines inclusion | Verified classification notes | Planned | `taxonomy/inclusion_criteria.md`, `data/papers.csv` |
| Scope classes | Compare three scope levels | Strict, world-model-like, related | Categories differ by dynamics and rollout roles | Verified paper coding | Planned | `taxonomy/world_model_taxonomy.md` |
| Overall taxonomy | Organize method dimensions | Representation, transition, objective, task | World-model methods are multidimensional | Verified metadata | Planned | `taxonomy/`, `data/papers.csv` |
| Task relationships | Separate detection, warning, prognosis, RUL | Time axis, targets, outputs | Related tasks require different protocols | Protocol definitions | Planned | `taxonomy/task_taxonomy.md` |
| Representation comparison | Contrast observation and latent dynamics | Inputs, states, decoders | Representation affects interpretability and rollout | Method coding | Planned | `taxonomy/representation_taxonomy.md` |
| Rollout uncertainty | Compare deterministic and probabilistic futures | Single vs multiple trajectories | Multiple futures require calibration | Uncertainty metadata | Planned | `taxonomy/uncertainty_modeling.md` |
| Action conditioning | Show interventions affecting transitions | State, action, next state | Maintenance decisions need intervention-aware dynamics | Verified examples | Planned | `data/papers.csv` |
| Unified PHM dynamics | Connect shared state to tasks | History, state, rollout, outputs | One dynamics perspective can connect PHM tasks | Survey synthesis | Planned | Editable source TODO |
| Dataset-task map | Reveal evaluation coverage | Datasets by tasks | Coverage and comparability gaps become visible | Verified dataset-paper links | Planned | `data/papers.csv`, `data/datasets.csv` |
| Research gap map | Summarize open challenges | Method and evaluation gaps | Claims follow coded evidence | Survey extraction | Planned | Survey synthesis TODO |
| Ecosystem map | Position complementary projects | Collections, frameworks, benchmarks | This repository connects rather than replaces ecosystems | Verified repository metadata | Planned | `data/repositories.csv` |

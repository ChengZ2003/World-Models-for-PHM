# Inclusion Criteria

## Operational Definition

> A world model learns a representation of a dynamic system and its temporal transition mechanisms, enabling the prediction, generation, or simulation of possible future system states for downstream tasks such as anomaly detection, early warning, health assessment, remaining useful life prediction, and maintenance decision-making.

## Candidate Assessment

For each candidate paper, answer with **yes**, **partial**, **no**, or **unknown**, and cite the relevant method section:

1. Does the method represent the state of a dynamic system?
2. Does it learn an explicit or implicit transition mechanism?
3. Can it predict, generate, or simulate future states?
4. Is future evolution used for anomaly detection, prognosis, RUL, or maintenance?
5. Is the dynamics component central to the method rather than an auxiliary loss?
6. Does the method support multi-step rollout, uncertainty modeling, or counterfactual analysis?
7. Would the method still be meaningfully described as a world model without relying only on the authors' terminology?

## Decision Guidance

```text
State representation? ── no ──> related_predictive_model or exclude
        │ yes/partial
Transition learned? ─── no ──> related_predictive_model or exclude
        │ yes
Future states used for PHM? ── no ──> background only or exclude
        │ yes
Dynamics central and questions 1–5 mostly yes?
        ├── yes, meaningful rollout/simulation/decision role ──> strict_world_model candidate
        ├── yes, but rollout/planning limited ──> world_model_like candidate
        └── primarily forecasting/reconstruction/classification/regression ──> related_predictive_model
```

Use `uncertain` and explain the ambiguity when the paper does not support a defensible assignment. Question 6 strengthens a strict classification but is not sufficient by itself. Question 7 prevents category assignment based on branding alone.

> Classification should be based on the actual modeling mechanism, not solely on whether the paper uses the phrase “world model.”

## Exclusion and Verification

Exclude work with no substantive connection to PHM or industrial reliability, and do not treat generic temporal prediction as automatically in scope. A record may be collected with `verified=false`, but only verified records appear in generated public tables.

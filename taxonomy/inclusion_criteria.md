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

## Mechanism-Based Examples

These abstract examples illustrate classification logic and do not refer to unverified papers.

### Example A — Strict World Model

```text
Historical observations
→ state encoder
→ learned transition model
→ multi-step future rollout
→ anomaly risk, RUL, or maintenance decision
```

This mechanism represents system state, learns state transitions, supports multi-step rollout, and makes rollout central to downstream inference or decision-making.

### Example B — World-Model-Like Dynamics Model

```text
Historical observations
→ latent representation
→ future latent prediction
→ prediction deviation used for anomaly scoring
```

This mechanism learns dynamic evolution and uses future prediction centrally, but it may not support planning, counterfactual reasoning, or a complete simulation interface.

### Example C — Related Predictive Model

```text
Historical sensor sequence
→ end-to-end neural network
→ direct scalar RUL prediction
```

This mechanism can be useful for RUL, but it does not explicitly learn a reusable state transition or rollout. Predicting a future outcome alone does not make a method a world model.

### Example D — Uncertain Case

```text
Encoder
→ auxiliary future-prediction loss
→ main fault classifier
```

Future prediction may be only an auxiliary objective. Reviewers must determine whether dynamics are central to the method and record both `scope_confidence` and the classification rationale.

## Common Misclassification Risks

- Treating every forecasting model as a world model
- Treating every generative model as a world model
- Treating direct RUL regression as rollout
- Relying only on the authors' terminology
- Ignoring whether dynamics are central or auxiliary
- Confusing reconstruction with future simulation
- Confusing foundation-model pretraining with system-specific dynamics modeling

## Classification Review Process

1. Record the search run and dual-screening decision before classification.
2. One contributor enters candidate metadata with `verified=false`.
3. Two different reviewers independently answer all seven questions in `data/paper_reviews.csv` and cite evidence locations.
4. Each reviewer proposes a scope, writes a mechanism-based rationale, records confidence, and marks approval only after checking the full-text evidence.
5. The two approved reviews must agree on `proposed_scope`.
6. The paper's `world_model_scope` must match that consensus before `verified=true` is set.
7. If disagreement remains, retain the record as unverified or reach an explicit `uncertain`/low-confidence consensus instead of forcing a category.

> `verified=true` means that the metadata and classification rationale have been manually checked. It does not mean that the paper's claims or experimental results have been independently reproduced.

## Exclusion and Verification

Exclude work with no substantive connection to PHM or industrial reliability, and do not treat generic temporal prediction as automatically in scope. A record may be collected with `verified=false`, but only records backed by two approved, scope-consistent reviews appear in generated public tables.

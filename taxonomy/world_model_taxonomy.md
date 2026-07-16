# World-Model Scope Taxonomy

## Strict World Models

Typically include an explicit system-state representation, an explicit temporal transition or dynamics model, multi-step prediction or rollout, and a role in simulation, planning, counterfactual reasoning, or decision support. Dynamics modeling is central.

## World-Model-Like Dynamics Models

Learn observation-space or latent-space temporal transitions for future prediction, degradation modeling, or uncertainty estimation. Dynamics matter to anomaly or prognosis tasks, but explicit planning and counterfactual simulation may be absent.

## Related Predictive Models

Standard forecasting, reconstruction, representation learning, direct RUL regression, and related methods can provide methodological or historical context. They are not called world models by default.

## Uncertain

Use this status when available evidence cannot support a stable assignment. Record the competing interpretations and evidence needed to resolve them.

## Mechanism-Based Examples

### Strict World Model

```text
Historical observations → state encoder → learned transition model
→ multi-step future rollout → anomaly risk, RUL, or maintenance decision
```

The learned transition and rollout are reusable and central to inference or decisions.

### World-Model-Like Dynamics Model

```text
Historical observations → latent representation → future latent prediction
→ prediction deviation used for anomaly scoring
```

Dynamics and future prediction are central, but planning, counterfactual reasoning, or full simulation may be absent.

### Related Predictive Model

```text
Historical sensor sequence → end-to-end neural network → direct scalar RUL prediction
```

The method predicts a future outcome without necessarily learning a reusable transition or rollout.

### Uncertain Case

```text
Encoder → auxiliary future-prediction loss → main fault classifier
```

The classification depends on whether dynamics are a core mechanism or merely auxiliary. Record low confidence and rationale when evidence is insufficient.

## Common Misclassification Risks

- Equating all forecasting or generative models with world models
- Calling direct RUL regression a rollout
- Relying on author terminology without checking the mechanism
- Ignoring whether dynamics are central or auxiliary
- Confusing reconstruction with future simulation
- Treating foundation-model pretraining as system-specific dynamics by default

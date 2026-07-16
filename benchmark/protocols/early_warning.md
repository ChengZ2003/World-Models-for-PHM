# Early-Warning Protocol

## Task Definition

For observation length `L`, lead-time gap `g`, and prediction horizon `H`:

\[
X_{t-L+1:t}
\rightarrow
P(Y_{t+g+1:t+g+H}=1)
\]

- `L`: observation window available at prediction time
- `g`: lead-time gap between the latest observation and forecast target
- `H`: future prediction horizon

The event-label rule within the target horizon must be explicit. Detection at `g=0` should not be silently reported as advance warning.

## Leakage Prevention

Features, normalization, interpolation, labels, and engineered health indicators must use information available no later than `t`. Split assets or chronological episodes before constructing overlapping windows. Thresholds and horizon choices must not use test events.

## Recommended Metrics

- AUROC and AUPRC
- Event recall and event precision
- Mean and median lead time
- False alarms per hour
- Recall@K and Precision@K
- Capacity-constrained recall
- Performance across multiple gaps and horizons

Define how repeated alarms map to events, how missed events affect lead-time summaries, and whether ranking capacity is per hour, shift, asset, or dataset.

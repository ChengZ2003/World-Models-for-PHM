# Metrics

Metrics must match the task and label granularity.

- Detection: report point-level and event-level metrics separately, threshold selection, alarm merging, and any point adjustment.
- Early warning: report event recall/precision, lead time, false-alarm rate, ranking metrics, capacity constraints, and performance by horizon.
- RUL: report MAE/RMSE and, when applicable, asymmetric scoring, relative error, interval coverage, calibration, and sharpness.

Metric names alone are insufficient: every result should specify aggregation, units, censoring, threshold selection, and test protocol.

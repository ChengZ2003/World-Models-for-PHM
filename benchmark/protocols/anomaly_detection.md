# Anomaly Detection Protocol

## Task

Given observations available through time `t`, produce an abnormality score or label for the current point or observed window. Future information is unavailable at inference time.

## Labels and Events

Report whether labels are point-level, window-level, or event-level. Event construction must state adjacency rules, tolerance, minimum duration, and treatment of overlapping faults. Point-level and event-level results must not be mixed.

## Threshold Selection

Select thresholds using training or validation data only. Report whether one global, per-asset, per-channel, or adaptive threshold is used. Test-label-derived thresholds constitute leakage unless the explicitly declared protocol studies oracle thresholding.

## Alarm Merging

Document cooldown, hysteresis, and rules for merging adjacent alarms. Report both raw scores and the post-processing configuration when possible.

## Evaluation Leakage

Prevent test windows, test labels, future normalization statistics, and post-failure observations from influencing training, hyperparameters, thresholds, or feature construction. Overlapping windows must not cross split boundaries.

## Point Adjustment

Point adjustment can award an entire anomalous segment after a single detected point and may substantially change rankings. If used for comparison with prior work, report unadjusted results alongside it and specify the exact implementation.

## Recommended Reporting

- Dataset version, asset split, label granularity, and event conversion
- Observation window and stride
- Threshold-selection data and method
- Alarm-merging settings
- AUROC and AUPRC with their aggregation level
- Event precision, recall, F-score, detection delay, and false alarms per unit time
- Point-adjusted results only as an explicitly labeled secondary analysis

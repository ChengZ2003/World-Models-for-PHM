# RUL Prediction Protocol

## Supported Settings

- Run-to-failure sequences
- Truncated or right-censored sequences
- Direct regression
- Health-index-based estimation
- Rollout-based RUL estimation
- Point estimates and probabilistic predictions
- Evaluation across operating conditions and assets

Define the failure threshold, RUL label construction, truncation or capping, censoring assumptions, and prediction times. Split by physical unit when windows from one unit are dependent.

## Recommended Metrics

- MAE and RMSE
- NASA scoring function, with the exact formula and convention
- Relative error
- Calibration error
- Prediction-interval coverage
- Sharpness

Report aggregate and horizon/health-stage stratified performance. For probabilistic predictions, report coverage and sharpness together. Operating-condition adaptation must not use future test information.

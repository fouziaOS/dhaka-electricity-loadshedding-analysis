# Key Insights — Dhaka Electricity & Load-Shedding Analysis

- Dataset: 365 days of 2025.
- Worst month for load-shedding: **month 4** (average 2.1 hours per day).
- Total load-shedding in the year: **316 hours**.
- Correlation between temperature and load-shedding: **0.60** (hotter days, more shedding).
- Average daily demand: **1,184 MW** vs supply **1,141 MW**.

## Machine Learning — prediction model
Predict daily load-shedding hours from temperature, demand, supply and month.

| Model | R² / Accuracy | RMSE |
|---|---|---|
| Linear Regression | 0.790 | 0.42 hours |
| Random Forest | 0.725 | 0.48 hours |

**Best model: Linear Regression.** Linear Regression predicts daily load-shedding within about **0.42 hours (25 minutes)** on average (R² = 0.790).

Run it yourself: `python src/ml_model.py` (needs scikit-learn, already in `requirements.txt`).
Results are saved in `outputs/tables/model_results.csv`.

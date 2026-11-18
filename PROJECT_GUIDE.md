# PROJECT GUIDE — Dhaka Electricity & Load-Shedding Analysis

A complete explanation of this project for beginners: what it is, what every file
and column means, how the code works step by step, and how to explain it in a viva.

## 1. What is this project?
Analyzing 365 days of electricity demand, supply and load-shedding in Dhaka. It is a full data-analysis workflow: create data → clean and explore it →
group and summarize → draw charts → write honest insights. Dataset size: 365 days.

## 2. Files in this project
- `README.md` — project summary with the key results and chart images.
- `PROJECT_GUIDE.md` — this guide.
- `requirements.txt` — the Python libraries needed (pandas, numpy, matplotlib).
- `src/generate_dataset.py` — builds the dataset with NumPy random numbers (fixed seed = same data every run).
- `src/analysis.py` — the main analysis code.
- `src/ml_model.py` — the Machine Learning code (trains 2 models and compares them).
- `data/electricity_daily.csv` — the dataset (created by generate_dataset.py).
- `dhaka-electricity-loadshedding-analysis.ipynb` — the same analysis as a Jupyter notebook.
- `outputs/charts/` — chart images:
- `demand_vs_supply.png`
- `shed_by_month.png`
- `shed_distribution.png`
- `temp_vs_shed.png`
- `outputs/tables/` — summary tables (CSV):
- `correlation_matrix.csv`
- `monthly_summary.csv`
- `total_shed_by_month.csv`
- `outputs/insights.md` — the key findings in plain words.

## 3. Dataset columns explained
| Column | Meaning |
|---|---|
| date | Date |
| temperature_c | Average temperature (°C) |
| demand_mw | Electricity demand (MW) |
| supply_mw | Electricity supply (MW) |
| loadshedding_hours | Load-shedding hours that day |
| outage_count | Number of outages that day |

## 4. How to run it (step by step)
1. Open a terminal inside this project folder.
2. Install the libraries: `pip install -r requirements.txt`
3. Create the data: `python src/generate_dataset.py`
4. Run the analysis: `python src/analysis.py`
5. Look inside `outputs/` — charts, tables and insights are created there.
6. Or open `dhaka-electricity-loadshedding-analysis.ipynb` in Jupyter and run the cells one by one.

## 5. How the code works
**generate_dataset.py** — sets a fixed NumPy seed, chooses categories with realistic
probabilities, builds numeric columns from related formulas (so the data behaves like
real life), assembles a Pandas DataFrame and saves it as CSV.

**analysis.py** — loads the CSV with Pandas, then:
1. `groupby(...)` summaries → saved as tables in `outputs/tables/`.
2. A correlation matrix for the numeric columns.
3. Four Matplotlib charts → saved in `outputs/charts/`.
4. The most important numbers are written into `outputs/insights.md`.

## 6. Key results
# Key Insights — Dhaka Electricity & Load-Shedding Analysis

- Dataset: 365 days of 2025.
- Worst month for load-shedding: **month 4** (average 2.1 hours per day).
- Total load-shedding in the year: **316 hours**.
- Correlation between temperature and load-shedding: **0.60** (hotter days, more shedding).
- Average daily demand: **1,184 MW** vs supply **1,141 MW**.

## 6b. The Machine Learning model
Predict daily load-shedding hours from temperature, demand, supply and month.
The code splits the data into 80% training and 20% testing, trains both models,
and compares them honestly on the test part only:
| Model | R² / Accuracy | RMSE |
|---|---|---|
| Linear Regression | 0.790 | 0.42 hours |
| Random Forest | 0.725 | 0.48 hours |

Best model: **Linear Regression**. Linear Regression predicts daily load-shedding within about **0.42 hours (25 minutes)** on average (R² = 0.790).
Key ideas: features (inputs) vs target (what we predict); train/test split so the
model is judged on data it has never seen; R² (how much variation the model explains)
and RMSE (average prediction error, in the target's own unit).

## 7. How to read the charts
- **Bar charts** compare groups (which group is biggest / most expensive / slowest).
- **Line charts** show change over time or hour — look for peaks.
- **Histograms** show how values are spread (most common range, rare extremes).
- **Scatter plots** show relationships between two numbers — an upward or downward
  cloud means the two move together (check the correlation value in the tables).

## 8. Viva / interview questions
**Q: Why does load-shedding rise with temperature?**
A: Heat raises fan/AC use, so demand grows faster than supply and the gap becomes load-shedding.

**Q: Which chart best shows the yearly pattern?**
A: The demand vs supply line chart over the 365 days.

**Q: What is the difference between demand and supply here?**
A: Demand is what consumers need; supply is what the grid could deliver that day.

**Q: What does R² = 0.79 mean in plain words?**
A: The model explains about 79% of the day-to-day variation in load-shedding; the rest is random outages and unmeasured factors.

## 9. Honest note
The data is synthetic (computer-generated with realistic patterns), made for learning
and portfolio demonstration. The workflow, code and analysis method are exactly what
would be used with real data.

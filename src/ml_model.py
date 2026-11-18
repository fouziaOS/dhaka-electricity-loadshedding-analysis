"""Machine Learning: predict daily load-shedding hours.

Features: temperature, demand, supply and month.
Models compared: Linear Regression and Random Forest.
Run from the project root:  python src/ml_model.py
"""
import pandas as pd, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, root_mean_squared_error

df = pd.read_csv("data/electricity_daily.csv", parse_dates=["date"])
df["month"] = df["date"].dt.month
X = df[["temperature_c", "demand_mw", "supply_mw", "month"]]
y = df["loadshedding_hours"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rows = []; preds = {}
for name, model in [("Linear Regression", LinearRegression()),
                    ("Random Forest", RandomForestRegressor(n_estimators=200, random_state=42))]:
    model.fit(X_train, y_train)
    p = model.predict(X_test)
    preds[name] = p
    rows.append({"model": name, "R2": round(r2_score(y_test, p), 3),
                 "RMSE (hours)": round(root_mean_squared_error(y_test, p), 2)})
    print(name, "-> R2:", rows[-1]["R2"], "| RMSE:", rows[-1]["RMSE (hours)"], "hours")

pd.DataFrame(rows).to_csv("outputs/tables/model_results.csv", index=False)
plt.figure(figsize=(6.5, 6)); plt.scatter(y_test, preds["Random Forest"], alpha=0.45, color="#c55a11")
lims = [0, y_test.max()]; plt.plot(lims, lims, "r--")
plt.title("Actual vs Predicted Load-Shedding (Random Forest)"); plt.xlabel("Actual (hours)"); plt.ylabel("Predicted (hours)")
plt.tight_layout(); plt.savefig("outputs/charts/actual_vs_predicted_shed.png"); plt.close()
print("Saved outputs/tables/model_results.csv and outputs/charts/actual_vs_predicted_shed.png")

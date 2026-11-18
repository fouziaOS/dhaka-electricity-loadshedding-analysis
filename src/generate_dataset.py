"""Generate the dataset for this project (synthetic data, NumPy seed-based)."""
import numpy as np, pandas as pd, os
rng = np.random.default_rng(3)
os.makedirs("data", exist_ok=True)
dates = pd.date_range("2025-01-01", periods=365, freq="D")
doy = np.arange(365)
temp = 27 + 6.5 * np.sin((doy - 30) / 365 * 2 * np.pi) + rng.normal(0, 1.6, 365)
demand = 1180 + 26 * (temp - 27) + rng.normal(0, 35, 365)
supply = demand - np.maximum(0, (temp - 31) * 38) - rng.normal(15, 22, 365)
supply = np.minimum(supply, demand - rng.uniform(0, 25, 365))
gap = (demand - supply).clip(5, None)
shed = np.round((gap / 55 + rng.normal(0, 0.5, 365)).clip(0, 14), 1)
outages = np.round(shed * rng.uniform(0.7, 1.3, 365)).astype(int)
df = pd.DataFrame({"date": dates.date, "temperature_c": temp.round(1), "demand_mw": demand.round(1),
                   "supply_mw": supply.round(1), "loadshedding_hours": shed, "outage_count": outages})
df.to_csv("data/electricity_daily.csv", index=False)
print("Saved", len(df), "days")

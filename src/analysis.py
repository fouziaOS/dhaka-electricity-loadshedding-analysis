"""Main analysis: tables, charts and insights. Run from the project root: python src/analysis.py"""
import pandas as pd, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt, os
os.makedirs("outputs/charts", exist_ok=True); os.makedirs("outputs/tables", exist_ok=True)
df = pd.read_csv("data/electricity_daily.csv", parse_dates=["date"])
df["month"] = df["date"].dt.month
df.groupby("month")[["temperature_c", "demand_mw", "supply_mw", "loadshedding_hours"]].mean().round(2).to_csv("outputs/tables/monthly_summary.csv")
df.groupby("month")["loadshedding_hours"].sum().round(1).rename("total_shed_hours").to_csv("outputs/tables/total_shed_by_month.csv")
df[["temperature_c", "demand_mw", "supply_mw", "loadshedding_hours", "outage_count"]].corr().round(2).to_csv("outputs/tables/correlation_matrix.csv")
m = df.groupby("month")["loadshedding_hours"].mean()
plt.figure(figsize=(8, 4.5)); m.plot(kind="bar", color="#c55a11")
plt.title("Average Daily Load-Shedding Hours by Month"); plt.ylabel("Hours"); plt.tight_layout(); plt.savefig("outputs/charts/shed_by_month.png"); plt.close()
plt.figure(figsize=(9, 4.5)); plt.plot(df["date"], df["demand_mw"], label="Demand", color="#c00000"); plt.plot(df["date"], df["supply_mw"], label="Supply", color="#2e75b6")
plt.title("Electricity Demand vs Supply (2025)"); plt.ylabel("MW"); plt.legend(); plt.tight_layout(); plt.savefig("outputs/charts/demand_vs_supply.png"); plt.close()
plt.figure(figsize=(8, 4.5)); plt.scatter(df["temperature_c"], df["loadshedding_hours"], alpha=0.4, color="#7030a0")
plt.title("Temperature vs Load-Shedding"); plt.xlabel("°C"); plt.ylabel("Hours"); plt.tight_layout(); plt.savefig("outputs/charts/temp_vs_shed.png"); plt.close()
plt.figure(figsize=(8, 4.5)); plt.hist(df["loadshedding_hours"], bins=16, color="#548235")
plt.title("Distribution of Daily Load-Shedding Hours"); plt.xlabel("Hours"); plt.tight_layout(); plt.savefig("outputs/charts/shed_distribution.png"); plt.close()
worst = int(m.idxmax()); c = df["temperature_c"].corr(df["loadshedding_hours"])
ins = f"""# Key Insights — Dhaka Electricity & Load-Shedding Analysis

- Dataset: {len(df)} days of 2025.
- Worst month for load-shedding: **month {worst}** (average {m.max():.1f} hours per day).
- Total load-shedding in the year: **{df['loadshedding_hours'].sum():,.0f} hours**.
- Correlation between temperature and load-shedding: **{c:.2f}** (hotter days, more shedding).
- Average daily demand: **{df['demand_mw'].mean():,.0f} MW** vs supply **{df['supply_mw'].mean():,.0f} MW**.
"""
open("outputs/insights.md", "w").write(ins)
print(ins)

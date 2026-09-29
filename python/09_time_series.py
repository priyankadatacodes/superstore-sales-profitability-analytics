"""
09_time_series.py
Purpose: Look at how sales and profit change over time.
"""

import pandas as pd

df = pd.read_csv("data_final.csv")

# Monthly sales, profit, margin
monthly = df.groupby("Order Year-Month").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum")
).reset_index()
monthly["Profit Margin %"] = (monthly["Profit"] / monthly["Sales"] * 100).round(2)
monthly = monthly.sort_values("Order Year-Month")

print("Monthly Performance:")
print(monthly.to_string(index=False))
print("Monthly Performance:")
print(monthly)

# Yearly sales, profit, and YoY growth
yearly = df.groupby("Order Year").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum")
).reset_index()

yearly["Sales YoY Growth %"] = yearly["Sales"].pct_change().mul(100).round(2)
yearly["Profit YoY Growth %"] = yearly["Profit"].pct_change().mul(100).round(2)

print("\nYearly Performance & YoY Growth:")
print(yearly.to_string(index=False))
print("\nYearly Performance & YoY Growth:")
print(yearly)

# Seasonality - average sales by month name
month_order = ["January","February","March","April","May","June",
               "July","August","September","October","November","December"]

seasonality = df.groupby("Order Month Name")["Sales"].sum().reindex(month_order)

print("\nTotal Sales by Month (seasonality):")
print(seasonality)

strongest_month = seasonality.idxmax()
print("\nStrongest month by sales:", strongest_month, "-", round(seasonality.max(), 2))

monthly.to_csv("monthly_performance.csv", index=False)
yearly.to_csv("yearly_performance.csv", index=False)
seasonality.to_csv("seasonality.csv")
print("\nSaved monthly_performance.csv, yearly_performance.csv, seasonality.csv")

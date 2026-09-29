"""
04_feature_engineering.py
Purpose: Create new columns needed for analysis.
"""

import pandas as pd

df = pd.read_csv("data_cleaned.csv")
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Profit Margin %
df["Profit Margin %"] = (df["Profit"] / df["Sales"]) * 100

# Discount Bucket
def get_bucket(discount):
    pct = discount * 100
    if pct == 0:
        return "0%"
    elif pct <= 10:
        return "1-10%"
    elif pct <= 20:
        return "11-20%"
    elif pct <= 30:
        return "21-30%"
    elif pct <= 40:
        return "31-40%"
    elif pct <= 50:
        return "41-50%"
    else:
        return ">50%"

df["Discount Bucket"] = df["Discount"].apply(get_bucket)

# Date features
df["Order Year"] = df["Order Date"].dt.year
df["Order Quarter"] = df["Order Date"].dt.quarter
df["Order Month"] = df["Order Date"].dt.month
df["Order Month Name"] = df["Order Date"].dt.strftime("%B")
df["Order Year-Month"] = df["Order Date"].dt.strftime("%Y-%m")

# Order-level metrics
order_metrics = df.groupby("Order ID").agg(
    Order_Sales_Total=("Sales", "sum"),
    Order_Profit_Total=("Profit", "sum")
).reset_index()

df = df.merge(order_metrics, on="Order ID", how="left")

print(df.shape)

df.to_csv("data_final.csv", index=False)
print("Saved data_final.csv")

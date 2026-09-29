"""
07_profitability_analysis.py
Purpose: Calculate profit KPIs and breakdowns.
"""

import pandas as pd

df = pd.read_csv("data_final.csv")

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()

print("Total Profit:", round(total_profit, 2))
print("Overall Profit Margin %:", round(total_profit / total_sales * 100, 2))

# Profit by Category
profit_category = df.groupby("Category")["Profit"].sum().sort_values(ascending=False)
print("\nProfit by Category:")
print(profit_category)

# Profit by Sub-Category
profit_subcat = df.groupby("Sub-Category")["Profit"].sum().sort_values(ascending=False)
print("\nProfit by Sub-Category:")
print(profit_subcat)

# Loss-making sub-categories
print("\nLoss-making Sub-Categories:")
print(profit_subcat[profit_subcat < 0])

# Profit by Region
profit_region = df.groupby("Region")["Profit"].sum().sort_values(ascending=False)
print("\nProfit by Region:")
print(profit_region)

# Profit by Segment
profit_segment = df.groupby("Segment")["Profit"].sum().sort_values(ascending=False)
print("\nProfit by Segment:")
print(profit_segment)

profit_category.to_csv("profit_by_category.csv")
profit_subcat.to_csv("profit_by_subcategory.csv")
profit_region.to_csv("profit_by_region.csv")
profit_segment.to_csv("profit_by_segment.csv")
print("\nSaved all profit CSVs")

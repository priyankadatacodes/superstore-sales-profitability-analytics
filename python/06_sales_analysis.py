"""
06_sales_analysis.py
Purpose: Calculate sales KPIs and breakdowns.
"""

import pandas as pd

df = pd.read_csv("data_final.csv")

total_sales = df["Sales"].sum()
total_orders = df["Order ID"].nunique()

print("Total Sales:", round(total_sales, 2))
print("Total Orders:", total_orders)
print("Avg Order Value:", round(total_sales / total_orders, 2))

# Sales by Category
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
print("\nSales by Category:")
print(category_sales)

# Sales by Sub-Category
subcat_sales = df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False)
print("\nSales by Sub-Category:")
print(subcat_sales)

category_sales.to_csv("sales_by_category.csv")
subcat_sales.to_csv("sales_by_subcategory.csv")
print("\nSaved sales_by_category.csv and sales_by_subcategory.csv")

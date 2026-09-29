"""
08_discount_analysis.py
Purpose: Analyze how discounting affects profit.
"""

import pandas as pd

df = pd.read_csv("data_final.csv")

# Discount bucket summary
bucket_order = ["0%", "1-10%", "11-20%", "21-30%", "31-40%", "41-50%", ">50%"]

discount_summary = df.groupby("Discount Bucket").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum")
).reset_index()

discount_summary["Profit Margin %"] = (discount_summary["Profit"] / discount_summary["Sales"] * 100).round(2)
discount_summary["Discount Bucket"] = pd.Categorical(discount_summary["Discount Bucket"], categories=bucket_order, ordered=True)
discount_summary = discount_summary.sort_values("Discount Bucket")

print("Discount Bucket Summary:")
print(discount_summary)

# Discount by Category
discount_category = df.groupby("Category").agg(
    Avg_Discount=("Discount", "mean"),
    Profit=("Profit", "sum")
).reset_index()
discount_category["Avg Discount %"] = (discount_category["Avg_Discount"] * 100).round(2)

print("\nDiscount by Category:")
print(discount_category[["Category", "Avg Discount %", "Profit"]])

# Discount by Sub-Category (sorted by avg discount)
discount_subcat = df.groupby("Sub-Category").agg(
    Avg_Discount=("Discount", "mean"),
    Profit=("Profit", "sum")
).reset_index()
discount_subcat["Avg Discount %"] = (discount_subcat["Avg_Discount"] * 100).round(2)
discount_subcat = discount_subcat.sort_values("Avg Discount %", ascending=False)

print("\nDiscount by Sub-Category (highest discount first):")
print(discount_subcat[["Sub-Category", "Avg Discount %", "Profit"]])

# Correlation
correlation = df["Discount"].corr(df["Profit Margin %"])
print("\nCorrelation between Discount and Profit Margin %:", round(correlation, 3))

discount_summary.to_csv("discount_summary.csv", index=False)
discount_category.to_csv("discount_by_category.csv", index=False)
discount_subcat.to_csv("discount_by_subcategory.csv", index=False)
print("\nSaved discount CSVs")

"""
05_eda.py
Purpose: Create charts to explore the data.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_csv("data_final.csv")

os.makedirs("screenshots", exist_ok=True)

# Sales distribution
plt.figure(figsize=(8,5))
sns.histplot(df["Sales"], bins=50)
plt.title("Sales Distribution")
plt.savefig("screenshots/eda_sales_distribution.png")
plt.close()

# Profit distribution
plt.figure(figsize=(8,5))
sns.histplot(df["Profit"], bins=50, color="orange")
plt.axvline(0, color="red", linestyle="--")
plt.title("Profit Distribution")
plt.savefig("screenshots/eda_profit_distribution.png")
plt.close()

# Discount vs Profit
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x="Discount", y="Profit", alpha=0.4)
plt.axhline(0, color="red", linestyle="--")
plt.title("Discount vs Profit")
plt.savefig("screenshots/eda_discount_vs_profit.png")
plt.close()

# Sales by Category
df.groupby("Category")["Sales"].sum().sort_values(ascending=False).plot(kind="bar")
plt.title("Sales by Category")
plt.tight_layout()
plt.savefig("screenshots/eda_sales_by_category.png")
plt.close()

# Profit by Category
df.groupby("Category")["Profit"].sum().sort_values(ascending=False).plot(kind="bar", color="green")
plt.title("Profit by Category")
plt.tight_layout()
plt.savefig("screenshots/eda_profit_by_category.png")
plt.close()

# Sales by Region
df.groupby("Region")["Sales"].sum().sort_values(ascending=False).plot(kind="bar", color="orange")
plt.title("Sales by Region")
plt.tight_layout()
plt.savefig("screenshots/eda_sales_by_region.png")
plt.close()

print("Charts saved in screenshots folder")

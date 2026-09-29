"""
13_extended_analysis.py
Purpose: Fill in the analysis gaps — State-level, Product-level,
City-level, Shipping, Quantity, Correlations, and Outliers.
"""

import pandas as pd

df = pd.read_csv("data_final.csv")
df["Order Date"] = pd.to_datetime(df["Order Date"])

# =====================================================
# 1. STATE-LEVEL PROFIT/LOSS CLASSIFICATION
# =====================================================
print("=" * 60)
print("STATE-LEVEL ANALYSIS")
print("=" * 60)

state_summary = df.groupby("State").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum")
).reset_index()
state_summary["Profit Margin %"] = (state_summary["Profit"] / state_summary["Sales"] * 100).round(2)

median_sales = state_summary["Sales"].median()
median_profit = state_summary["Profit"].median()

def classify_state(row):
    high_sales = row["Sales"] >= median_sales
    high_profit = row["Profit"] >= median_profit
    if high_sales and high_profit:
        return "High Sales + High Profit"
    elif high_sales and not high_profit:
        return "High Sales + Low Profit"
    elif not high_sales and high_profit:
        return "Low Sales + High Profit"
    else:
        return "Low Sales + Low Profit"

state_summary["Quadrant"] = state_summary.apply(classify_state, axis=1)
state_summary = state_summary.sort_values("Sales", ascending=False)

print("\nTop 10 states by sales:")
print(state_summary.head(10).to_string(index=False))

print("\nLoss-making states:")
loss_states = state_summary[state_summary["Profit"] < 0]
print(loss_states.to_string(index=False) if len(loss_states) > 0 else "None")

print("\nHigh Sales + Low Profit states (biggest concern):")
print(state_summary[state_summary["Quadrant"] == "High Sales + Low Profit"].to_string(index=False))

state_summary.to_csv("state_analysis.csv", index=False)

# =====================================================
# 2. PRODUCT-LEVEL ANALYSIS (individual products, not sub-category)
# =====================================================
print("\n" + "=" * 60)
print("PRODUCT-LEVEL ANALYSIS")
print("=" * 60)

product_summary = df.groupby("Product Name").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum")
).reset_index()
product_summary["Profit Margin %"] = (product_summary["Profit"] / product_summary["Sales"] * 100).round(2)

print("\nTop 10 products by sales:")
print(product_summary.sort_values("Sales", ascending=False).head(10)[
    ["Product Name", "Sales", "Profit"]].to_string(index=False))

print("\nTop 10 worst products by profit (biggest losses):")
worst_products = product_summary.sort_values("Profit").head(10)
print(worst_products[["Product Name", "Sales", "Profit"]].to_string(index=False))

print("\nHigh sales but negative profit products (top 10 by sales among losers):")
high_sales_losers = product_summary[product_summary["Profit"] < 0].sort_values("Sales", ascending=False).head(10)
print(high_sales_losers[["Product Name", "Sales", "Profit"]].to_string(index=False))

product_summary.to_csv("product_analysis.csv", index=False)

# =====================================================
# 3. CITY-LEVEL ANALYSIS
# =====================================================
print("\n" + "=" * 60)
print("CITY-LEVEL ANALYSIS")
print("=" * 60)

city_summary = df.groupby(["City", "State"]).agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum")
).reset_index()

print("\nTop 10 cities by sales:")
print(city_summary.sort_values("Sales", ascending=False).head(10).to_string(index=False))

print("\nBottom 10 cities by profit (biggest losses):")
print(city_summary.sort_values("Profit").head(10).to_string(index=False))

city_summary.to_csv("city_analysis.csv", index=False)

# =====================================================
# 4. SHIPPING MODE ANALYSIS
# =====================================================
print("\n" + "=" * 60)
print("SHIPPING MODE ANALYSIS")
print("=" * 60)

ship_summary = df.groupby("Ship Mode").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Orders=("Order ID", "nunique")
).reset_index()
ship_summary["Profit Margin %"] = (ship_summary["Profit"] / ship_summary["Sales"] * 100).round(2)
ship_summary = ship_summary.sort_values("Sales", ascending=False)

print(ship_summary.to_string(index=False))

print("\nShip Mode preference by Segment:")
ship_by_segment = df.groupby(["Segment", "Ship Mode"])["Order ID"].nunique().reset_index()
ship_by_segment.columns = ["Segment", "Ship Mode", "Order Count"]
print(ship_by_segment.to_string(index=False))

ship_summary.to_csv("shipping_analysis.csv", index=False)

# =====================================================
# 5. QUANTITY ANALYSIS
# =====================================================
print("\n" + "=" * 60)
print("QUANTITY ANALYSIS")
print("=" * 60)

qty_by_product = df.groupby("Product Name").agg(
    Quantity=("Quantity", "sum"),
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum")
).reset_index()

print("\nTop 10 highest-quantity products:")
print(qty_by_product.sort_values("Quantity", ascending=False).head(10)[
    ["Product Name", "Quantity", "Sales", "Profit"]].to_string(index=False))

print("\nHigh quantity but low/negative profit (potential volume traps):")
high_qty_low_profit = qty_by_product[qty_by_product["Profit"] < 50].sort_values("Quantity", ascending=False).head(10)
print(high_qty_low_profit[["Product Name", "Quantity", "Sales", "Profit"]].to_string(index=False))

# =====================================================
# 6. CORRELATION ANALYSIS
# =====================================================
print("\n" + "=" * 60)
print("CORRELATION ANALYSIS")
print("=" * 60)

print("Sales vs Profit correlation:", round(df["Sales"].corr(df["Profit"]), 3))
print("Discount vs Profit correlation:", round(df["Discount"].corr(df["Profit"]), 3))
print("Quantity vs Profit correlation:", round(df["Quantity"].corr(df["Profit"]), 3))
print("Quantity vs Sales correlation:", round(df["Quantity"].corr(df["Sales"]), 3))

# =====================================================
# 7. OUTLIER ANALYSIS
# =====================================================
print("\n" + "=" * 60)
print("OUTLIER ANALYSIS")
print("=" * 60)

print("\nTop 5 largest single-order losses:")
print(df.nsmallest(5, "Profit")[
    ["Order ID", "Product Name", "Sales", "Discount", "Profit"]].to_string(index=False))

print("\nTop 5 largest single-order profits:")
print(df.nlargest(5, "Profit")[
    ["Order ID", "Product Name", "Sales", "Discount", "Profit"]].to_string(index=False))

print("\nTop 5 largest single-order sales:")
print(df.nlargest(5, "Sales")[
    ["Order ID", "Product Name", "Sales", "Discount", "Profit"]].to_string(index=False))

# =====================================================
# 8. SEGMENT x CATEGORY CROSS-ANALYSIS
# =====================================================
print("\n" + "=" * 60)
print("SEGMENT x CATEGORY ANALYSIS")
print("=" * 60)

segment_category = df.groupby(["Segment", "Category"]).agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum")
).reset_index()
segment_category = segment_category.sort_values(["Segment", "Profit"], ascending=[True, False])

print(segment_category.to_string(index=False))

segment_category.to_csv("segment_category_analysis.csv", index=False)

print("\n\nAll extended analysis CSVs saved: state_analysis.csv, product_analysis.csv, "
      "city_analysis.csv, shipping_analysis.csv, segment_category_analysis.csv")

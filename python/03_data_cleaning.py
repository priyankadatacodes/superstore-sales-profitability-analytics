"""
03_data_cleaning.py
Purpose: Clean the raw data.
"""

import pandas as pd

df = pd.read_csv("data_raw.csv")

# Remove duplicate rows
df = df.drop_duplicates()

# Drop rows missing critical fields
df = df.dropna(subset=["Sales", "Profit", "Order Date"])

# Fix data types
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# Validation rules
df = df[df["Quantity"] > 0]
df = df[df["Sales"] >= 0]
df = df[(df["Discount"] >= 0) & (df["Discount"] <= 1)]

print("Final rows:", df.shape[0])

df.to_csv("data_cleaned.csv", index=False)
print("Saved data_cleaned.csv")

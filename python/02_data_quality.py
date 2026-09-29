"""
02_data_quality.py
Purpose: Look at the raw data before cleaning it.
"""

import pandas as pd

df = pd.read_csv("data_raw.csv")

print(df.shape)
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
print("Duplicates:", df.duplicated().sum())
"""
01_data_ingestion.py
Purpose: Load the Superstore dataset from a local file on disk.
"""

import pandas as pd

# Load the file (cp1252 encoding needed)
df = pd.read_csv("Sample - Superstore.csv", encoding="cp1252")

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# Save a clean UTF-8 copy for every later script to use
df.to_csv("data_raw.csv", index=False, encoding="utf-8")
print("Saved data_raw.csv")

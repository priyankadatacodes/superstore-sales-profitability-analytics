"""
12_tableau_export.py
Purpose: Export data from MySQL views into CSVs for Tableau Public.
"""

from sqlalchemy import create_engine
import pandas as pd
import os

# Fill in your real MySQL password here (same as script 11)
engine = create_engine("mysql+pymysql://root:pricass00@localhost:3306/superstore")

os.makedirs("tableau", exist_ok=True)

# Main transaction table
main_df = pd.read_sql("SELECT * FROM superstore;", con=engine)
main_df.to_csv("tableau/tableau_main_export.csv", index=False)
print("Exported tableau_main_export.csv:", main_df.shape[0], "rows")

# RFM table
rfm_df = pd.read_sql("SELECT * FROM customer_rfm;", con=engine)
rfm_df.to_csv("tableau/tableau_rfm_export.csv", index=False)
print("Exported tableau_rfm_export.csv:", rfm_df.shape[0], "rows")

# Monthly performance (from view)
monthly_df = pd.read_sql("SELECT * FROM vw_monthly_performance ORDER BY `Order Year-Month`;", con=engine)
monthly_df.to_csv("tableau/tableau_monthly_export.csv", index=False)
print("Exported tableau_monthly_export.csv:", monthly_df.shape[0], "rows")

# Geographic performance (from view)
geo_df = pd.read_sql("SELECT * FROM vw_geographic_profitability;", con=engine)
geo_df.to_csv("tableau/tableau_geographic_export.csv", index=False)
print("Exported tableau_geographic_export.csv:", geo_df.shape[0], "rows")

print("\nAll Tableau CSVs saved in the tableau/ folder")

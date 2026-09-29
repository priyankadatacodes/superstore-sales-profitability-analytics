"""
11_mysql_upload.py
Purpose: Upload data into MySQL.
"""

from sqlalchemy import create_engine
import pandas as pd

# Fill in your real MySQL password here
engine = create_engine("mysql+pymysql://root:pricass00@localhost:3306/superstore")

df = pd.read_csv("data_final.csv")
df.to_sql("superstore", con=engine, if_exists="replace", index=False)
print("Uploaded superstore table:", df.shape[0], "rows")

rfm_df = pd.read_csv("customer_rfm.csv")
rfm_df.to_sql("customer_rfm", con=engine, if_exists="replace", index=False)
print("Uploaded customer_rfm table:", rfm_df.shape[0], "rows")

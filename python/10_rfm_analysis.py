"""
10_rfm_analysis.py
Purpose: Segment customers into Champions, Loyal, Recent, At Risk, Lost.
"""

import pandas as pd

df = pd.read_csv("data_final.csv")
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Snapshot date = 1 day after the last order in the dataset
snapshot_date = df["Order Date"].max() + pd.Timedelta(days=1)
print("Snapshot date:", snapshot_date.date())

# Calculate Recency, Frequency, Monetary per customer
rfm = df.groupby("Customer ID").agg(
    Recency=("Order Date", lambda x: (snapshot_date - x.max()).days),
    Frequency=("Order ID", "nunique"),
    Monetary=("Sales", "sum")
).reset_index()

print("Total customers:", rfm.shape[0])

# Score each dimension 1-5
rfm["R"] = pd.qcut(rfm["Recency"], q=5, labels=[5,4,3,2,1]).astype(int)
rfm["F"] = pd.qcut(rfm["Frequency"].rank(method="first"), q=5, labels=[1,2,3,4,5]).astype(int)
rfm["M"] = pd.qcut(rfm["Monetary"].rank(method="first"), q=5, labels=[1,2,3,4,5]).astype(int)

rfm["RFM Score"] = rfm["R"].astype(str) + rfm["F"].astype(str) + rfm["M"].astype(str)

# Assign segments
def assign_segment(row):
    r, f, m = row["R"], row["F"], row["M"]
    if r >= 4 and f >= 4 and m >= 4:
        return "Champions"
    elif f >= 4:
        return "Loyal"
    elif r >= 4 and f <= 2:
        return "Recent"
    elif r <= 2 and m >= 3:
        return "At Risk"
    else:
        return "Lost"

rfm["Segment"] = rfm.apply(assign_segment, axis=1)

# Segment summary
segment_summary = rfm.groupby("Segment").agg(
    Customer_Count=("Customer ID", "count"),
    Total_Monetary=("Monetary", "sum")
).reset_index()
segment_summary["% of Customers"] = (segment_summary["Customer_Count"] / segment_summary["Customer_Count"].sum() * 100).round(2)
segment_summary = segment_summary.sort_values("Total_Monetary", ascending=False)

print("\nSegment Summary:")
print(segment_summary.to_string(index=False))

# At-Risk total value
at_risk_value = rfm[rfm["Segment"] == "At Risk"]["Monetary"].sum()
print("\nTotal historical sales tied to At-Risk customers:", round(at_risk_value, 2))

rfm.to_csv("customer_rfm.csv", index=False)
segment_summary.to_csv("rfm_segment_summary.csv", index=False)
print("\nSaved customer_rfm.csv and rfm_segment_summary.csv")

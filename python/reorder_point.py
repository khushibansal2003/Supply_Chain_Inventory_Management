import pandas as pd
import os

print("=" * 70)
print("SUPPLY CHAIN & INVENTORY MANAGEMENT")
print("REORDER POINT ANALYSIS")
print("=" * 70)

# Load cleaned datasets
sales = pd.read_csv("data/cleaned/sales_cleaned.csv")
inventory = pd.read_csv("data/cleaned/inventory_cleaned.csv")
suppliers = pd.read_csv("data/cleaned/suppliers_cleaned.csv")

# ---------------------------------------------------------
# 1. CALCULATE AVERAGE DAILY DEMAND
# ---------------------------------------------------------

sales["Sale_Date"] = pd.to_datetime(sales["Sale_Date"])

total_days = (
    sales["Sale_Date"].max() - sales["Sale_Date"].min()
).days + 1

daily_demand = (
    sales.groupby("Product_ID")["Quantity_Sold"]
    .sum()
    / total_days
)

daily_demand = daily_demand.reset_index()
daily_demand.columns = ["Product_ID", "Average_Daily_Demand"]

# ---------------------------------------------------------
# 2. MERGE INVENTORY WITH DEMAND
# ---------------------------------------------------------

reorder = inventory.merge(
    daily_demand,
    on="Product_ID",
    how="left"
)

# ---------------------------------------------------------
# 3. ADD SUPPLIER LEAD TIME
# ---------------------------------------------------------

# Use the average supplier lead time for each product
supplier_lead_time = (
    suppliers.groupby("Product_ID")["Lead_Time (days)"]
    .mean()
    .reset_index()
)

reorder = reorder.merge(
    supplier_lead_time,
    on="Product_ID",
    how="left"
)

# ---------------------------------------------------------
# 4. REORDER POINT
# ---------------------------------------------------------

reorder["Reorder_Point"] = (
    reorder["Average_Daily_Demand"]
    * reorder["Lead_Time (days)"]
)

# ---------------------------------------------------------
# 5. STOCK STATUS
# ---------------------------------------------------------

reorder["Reorder_Status"] = reorder.apply(
    lambda row:
    "REORDER REQUIRED"
    if row["Stock_Level"] <= row["Reorder_Point"]
    else "Stock Sufficient",
    axis=1
)

# ---------------------------------------------------------
# 6. DISPLAY RESULTS
# ---------------------------------------------------------

print("\n[1] REORDER POINT ANALYSIS")

result_columns = [
    "Product_ID",
    "Store_ID",
    "Stock_Level",
    "Reorder_Level",
    "Average_Daily_Demand",
    "Lead_Time (days)",
    "Reorder_Point",
    "Reorder_Status"
]

print(
    reorder[result_columns]
    .round(2)
    .to_string(index=False)
)

# ---------------------------------------------------------
# 7. PRODUCTS REQUIRING REORDER
# ---------------------------------------------------------

reorder_required = reorder[
    reorder["Reorder_Status"] == "REORDER REQUIRED"
]

print("\n[2] PRODUCTS REQUIRING REORDER")
print("Number of records:", len(reorder_required))

print(
    reorder_required[result_columns]
    .round(2)
    .to_string(index=False)
)

# ---------------------------------------------------------
# 8. SAVE RESULTS
# ---------------------------------------------------------

output_path = "data/cleaned"
os.makedirs(output_path, exist_ok=True)

reorder.to_csv(
    os.path.join(output_path, "reorder_analysis.csv"),
    index=False
)

reorder_required.to_csv(
    os.path.join(output_path, "products_requiring_reorder.csv"),
    index=False
)

print("\n" + "=" * 70)
print("REORDER POINT ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 70)

print("\nFiles created:")
print("1. reorder_analysis.csv")
print("2. products_requiring_reorder.csv")
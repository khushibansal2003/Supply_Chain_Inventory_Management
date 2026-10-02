import pandas as pd
import os

print("=" * 70)
print("SUPPLY CHAIN & INVENTORY MANAGEMENT")
print("DATA CLEANING & PREPARATION")
print("=" * 70)

# ---------------------------------------------------------
# 1. LOAD DATASETS
# ---------------------------------------------------------

base_path = "data"

sales = pd.read_csv(os.path.join(base_path, "sales_data.csv"))
inventory = pd.read_csv(os.path.join(base_path, "inventory_data.csv"))
purchase_orders = pd.read_csv(
    os.path.join(base_path, "purchase_orders_data.csv")
)
suppliers = pd.read_csv(os.path.join(base_path, "suppliers_data.csv"))

print("\n[1] DATASETS LOADED")
print("Sales records          :", len(sales))
print("Inventory records      :", len(inventory))
print("Purchase order records:", len(purchase_orders))
print("Supplier records       :", len(suppliers))

# ---------------------------------------------------------
# 2. DISPLAY COLUMNS
# ---------------------------------------------------------

print("\n[2] DATASET COLUMNS")

print("\nSales:")
print(sales.columns.tolist())

print("\nInventory:")
print(inventory.columns.tolist())

print("\nPurchase Orders:")
print(purchase_orders.columns.tolist())

print("\nSuppliers:")
print(suppliers.columns.tolist())

# ---------------------------------------------------------
# 3. CHECK DUPLICATES
# ---------------------------------------------------------

print("\n[3] DUPLICATE CHECK")

print("Sales duplicates          :", sales.duplicated().sum())
print("Inventory duplicates      :", inventory.duplicated().sum())
print("Purchase order duplicates:", purchase_orders.duplicated().sum())
print("Supplier duplicates       :", suppliers.duplicated().sum())

# ---------------------------------------------------------
# 4. CHECK MISSING VALUES
# ---------------------------------------------------------

print("\n[4] MISSING VALUE CHECK")

print("Sales missing values:")
print(sales.isnull().sum())

print("\nInventory missing values:")
print(inventory.isnull().sum())

print("\nPurchase Orders missing values:")
print(purchase_orders.isnull().sum())

print("\nSuppliers missing values:")
print(suppliers.isnull().sum())

# ---------------------------------------------------------
# 5. DATE CONVERSION
# ---------------------------------------------------------

print("\n[5] CONVERTING DATE COLUMNS")

sales["Sale_Date"] = pd.to_datetime(sales["Sale_Date"])
inventory["Last_Updated"] = pd.to_datetime(inventory["Last_Updated"])
purchase_orders["Order_Date"] = pd.to_datetime(
    purchase_orders["Order_Date"]
)
purchase_orders["Arrival_Date"] = pd.to_datetime(
    purchase_orders["Arrival_Date"]
)

print("Date conversion completed.")

# ---------------------------------------------------------
# 6. PURCHASE ORDER LEAD TIME
# ---------------------------------------------------------

purchase_orders["Actual_Lead_Time"] = (
    purchase_orders["Arrival_Date"]
    - purchase_orders["Order_Date"]
).dt.days

print("\n[6] PURCHASE ORDER LEAD TIME CREATED")

print(
    purchase_orders[
        ["Order_ID", "Order_Date", "Arrival_Date", "Actual_Lead_Time"]
    ].head()
)

# ---------------------------------------------------------
# 7. INVENTORY STATUS
# ---------------------------------------------------------

inventory["Stock_Status"] = inventory.apply(
    lambda row:
    "Below Reorder Level"
    if row["Stock_Level"] < row["Reorder_Level"]
    else "Sufficient Stock",
    axis=1
)

print("\n[7] INVENTORY STATUS CREATED")

print(inventory["Stock_Status"].value_counts())

# ---------------------------------------------------------
# 8. SALES MONTH
# ---------------------------------------------------------

sales["Year"] = sales["Sale_Date"].dt.year
sales["Month"] = sales["Sale_Date"].dt.month
sales["Month_Name"] = sales["Sale_Date"].dt.strftime("%B")

print("\n[8] SALES TIME FEATURES CREATED")

print(
    sales[
        ["Sale_Date", "Year", "Month", "Month_Name"]
    ].head()
)

# ---------------------------------------------------------
# 9. DATA QUALITY CHECK
# ---------------------------------------------------------

print("\n[9] FINAL DATA QUALITY CHECK")

print("\nSales:")
print("Rows:", len(sales))
print("Columns:", len(sales.columns))
print("Missing values:", sales.isnull().sum().sum())

print("\nInventory:")
print("Rows:", len(inventory))
print("Columns:", len(inventory.columns))
print("Missing values:", inventory.isnull().sum().sum())

print("\nPurchase Orders:")
print("Rows:", len(purchase_orders))
print("Columns:", len(purchase_orders.columns))
print("Missing values:", purchase_orders.isnull().sum().sum())

print("\nSuppliers:")
print("Rows:", len(suppliers))
print("Columns:", len(suppliers.columns))
print("Missing values:", suppliers.isnull().sum().sum())

# ---------------------------------------------------------
# 10. SAVE CLEANED DATA
# ---------------------------------------------------------

cleaned_path = "data/cleaned"
os.makedirs(cleaned_path, exist_ok=True)

sales.to_csv(
    os.path.join(cleaned_path, "sales_cleaned.csv"),
    index=False
)

inventory.to_csv(
    os.path.join(cleaned_path, "inventory_cleaned.csv"),
    index=False
)

purchase_orders.to_csv(
    os.path.join(cleaned_path, "purchase_orders_cleaned.csv"),
    index=False
)

suppliers.to_csv(
    os.path.join(cleaned_path, "suppliers_cleaned.csv"),
    index=False
)

print("\n" + "=" * 70)
print("DATA CLEANING COMPLETED SUCCESSFULLY")
print("=" * 70)

print("\nCleaned files created:")
print("1. sales_cleaned.csv")
print("2. inventory_cleaned.csv")
print("3. purchase_orders_cleaned.csv")
print("4. suppliers_cleaned.csv")
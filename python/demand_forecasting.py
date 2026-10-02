import pandas as pd
import os

print("=" * 70)
print("SUPPLY CHAIN & INVENTORY MANAGEMENT")
print("DEMAND ANALYSIS & NEXT-MONTH FORECAST")
print("=" * 70)

# Load cleaned sales data
sales = pd.read_csv("data/cleaned/sales_cleaned.csv")
sales["Sale_Date"] = pd.to_datetime(sales["Sale_Date"])

# ---------------------------------------------------------
# 1. MONTHLY DEMAND
# ---------------------------------------------------------

monthly_demand = (
    sales.groupby(sales["Sale_Date"].dt.to_period("M"))
    ["Quantity_Sold"]
    .sum()
    .reset_index()
)

monthly_demand.columns = ["Month", "Total_Demand"]

print("\n[1] MONTHLY DEMAND")
print(monthly_demand.to_string(index=False))

# ---------------------------------------------------------
# 2. PRODUCT-WISE DEMAND
# ---------------------------------------------------------

product_demand = (
    sales.groupby("Product_ID")["Quantity_Sold"]
    .sum()
    .reset_index()
    .sort_values("Quantity_Sold", ascending=False)
)

print("\n[2] TOP 10 FAST-MOVING PRODUCTS")
print(product_demand.head(10).to_string(index=False))

# ---------------------------------------------------------
# 3. AVERAGE MONTHLY DEMAND
# ---------------------------------------------------------

average_monthly_demand = monthly_demand["Total_Demand"].mean()

print("\n[3] AVERAGE MONTHLY DEMAND")
print(f"Average monthly demand: {average_monthly_demand:.2f}")

# ---------------------------------------------------------
# 4. NEXT-MONTH FORECAST
# ---------------------------------------------------------

# Simple forecasting approach:
# average of the available monthly demand values

forecast_demand = average_monthly_demand

print("\n[4] NEXT-MONTH DEMAND FORECAST")
print(f"Forecast demand: {forecast_demand:.2f} units")

# ---------------------------------------------------------
# 5. SAVE FORECAST RESULTS
# ---------------------------------------------------------

output_path = "data/cleaned"
os.makedirs(output_path, exist_ok=True)

monthly_demand.to_csv(
    os.path.join(output_path, "monthly_demand.csv"),
    index=False
)

forecast_result = pd.DataFrame({
    "Forecast_Monthly_Demand": [round(forecast_demand, 2)]
})

forecast_result.to_csv(
    os.path.join(output_path, "demand_forecast.csv"),
    index=False
)

print("\n" + "=" * 70)
print("DEMAND ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 70)

print("\nFiles created:")
print("1. monthly_demand.csv")
print("2. demand_forecast.csv")
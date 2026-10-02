USE supply_chain_inventory;

-- 1. Inventory summary
SELECT
    Product_ID,
    COUNT(*) AS Records,
    ROUND(AVG(Inventory_Level), 2) AS Avg_Inventory,
    ROUND(AVG(Reorder_Level), 2) AS Avg_Reorder_Level
FROM inventory
GROUP BY Product_ID
ORDER BY Avg_Inventory ASC;


-- 2. Products below reorder level
SELECT
    Product_ID,
    Store_ID,
    Inventory_Level,
    Reorder_Level,
    Stock_Status
FROM inventory
WHERE Inventory_Level <= Reorder_Level
ORDER BY Inventory_Level ASC;


-- 3. Sales summary by product
SELECT
    Product_ID,
    SUM(Quantity_Sold) AS Total_Quantity_Sold,
    ROUND(SUM(Revenue), 2) AS Total_Revenue
FROM sales
GROUP BY Product_ID
ORDER BY Total_Quantity_Sold DESC;


-- 4. Monthly sales analysis
SELECT
    Year,
    Month,
    Month_Name,
    SUM(Quantity_Sold) AS Total_Quantity_Sold,
    ROUND(SUM(Revenue), 2) AS Total_Revenue
FROM sales
GROUP BY Year, Month, Month_Name
ORDER BY Year, Month;


-- 5. Supplier performance
SELECT
    Supplier_ID,
    Supplier_Name,
    ROUND(AVG(Lead_Time), 2) AS Avg_Lead_Time,
    ROUND(AVG(Reliability_Score), 2) AS Avg_Reliability
FROM suppliers
GROUP BY Supplier_ID, Supplier_Name
ORDER BY Avg_Reliability DESC;


-- 6. Purchase order status
SELECT
    Order_Status,
    COUNT(*) AS Order_Count,
    SUM(Quantity_Ordered) AS Total_Quantity
FROM purchase_orders
GROUP BY Order_Status
ORDER BY Order_Count DESC;


-- 7. Overall sales KPIs
SELECT
    COUNT(*) AS Total_Sales_Records,
    SUM(Quantity_Sold) AS Total_Units_Sold,
    ROUND(SUM(Revenue), 2) AS Total_Revenue,
    ROUND(AVG(Quantity_Sold), 2) AS Avg_Quantity_Per_Sale
FROM sales;
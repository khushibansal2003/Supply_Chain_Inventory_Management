CREATE DATABASE IF NOT EXISTS supply_chain_inventory;
USE supply_chain_inventory;

CREATE TABLE inventory (
    Product_ID VARCHAR(20),
    Store_ID VARCHAR(20),
    Inventory_Level INT,
    Reorder_Level INT,
    Unit_Cost DECIMAL(10,2),
    Supplier_Lead_Time DECIMAL(10,2),
    Stock_Status VARCHAR(30)
);

CREATE TABLE sales (
    Sale_ID VARCHAR(50),
    Product_ID VARCHAR(20),
    Store_ID VARCHAR(20),
    Sale_Date DATE,
    Quantity_Sold INT,
    Revenue DECIMAL(12,2),
    Year INT,
    Month INT,
    Month_Name VARCHAR(20)
);

CREATE TABLE purchase_orders (
    Purchase_Order_ID VARCHAR(50),
    Product_ID VARCHAR(20),
    Supplier_ID VARCHAR(20),
    Order_Date DATE,
    Quantity_Ordered INT,
    Expected_Delivery_Date DATE,
    Order_Status VARCHAR(30)
);

CREATE TABLE suppliers (
    Supplier_ID VARCHAR(20),
    Supplier_Name VARCHAR(100),
    Location VARCHAR(100),
    Lead_Time DECIMAL(10,2),
    Reliability_Score DECIMAL(10,2)
);
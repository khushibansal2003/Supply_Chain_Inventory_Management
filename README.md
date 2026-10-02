# Supply Chain & Inventory Management Analytics

## 📌 Project Overview

The Supply Chain & Inventory Management Analytics project is a data-driven solution designed to analyze sales, inventory, suppliers, purchase orders, demand patterns, and reorder requirements.

The project uses Python for data cleaning and analytical processing and MySQL for structured data storage and SQL-based business analysis.

The objective is to transform raw supply chain data into meaningful insights that can support inventory planning, demand forecasting, supplier management, and sales analysis.

---

## 🎯 Project Objectives

- Clean and prepare raw supply chain datasets.
- Analyze historical sales performance.
- Analyze inventory levels and reorder requirements.
- Identify products that require reordering.
- Analyze supplier lead times.
- Forecast future monthly demand.
- Calculate reorder points using demand and supplier lead-time information.
- Store cleaned data in a MySQL database.
- Perform business analysis using SQL queries.
- Generate structured analytical output files for further reporting.

---

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **MySQL**
- **SQL**
- **Git**
- **GitHub**
- **Visual Studio Code**

---

## 📂 Project Structure

```text
Supply_Chain_Inventory_Management/
│
├── data/
│   ├── cleaned/
│   │   ├── demand_forecast.csv
│   │   ├── inventory_cleaned.csv
│   │   ├── monthly_demand.csv
│   │   ├── products_requiring_reorder.csv
│   │   ├── purchase_orders_cleaned.csv
│   │   ├── reorder_analysis.csv
│   │   ├── sales_cleaned.csv
│   │   └── suppliers_cleaned.csv
│   │
│   ├── inventory_data.csv
│   ├── purchase_orders_data.csv
│   ├── sales_data.csv
│   └── suppliers_data.csv
│
├── python/
│   ├── data_cleaning.py
│   ├── demand_forecasting.py
│   └── reorder_point.py
│
├── sql/
│   ├── schema.sql
│   └── inventory_analysis.sql
│
└── README.md
# 🛒 Retail ML-Ready Synthetic Database

This repository provides a fully structured, **logically consistent**, and **clean synthetic dataset** designed for building and testing **retail analytics and machine learning** solutions using a relational database approach.

It includes realistic relationships between **Customers**, **Products**, **Purchases**, and **Payments**, with a special focus on:

- Churn Analysis
- Product Recommendation
- Customer Segmentation
- Anomaly/Fraud Detection

## 📦 Contents

- `Products_Final.csv` — Catalogue of retail products with pricing and categories.
- `Customers_Final.csv` — Customer demographics, location, and preferences.
- `Payments_Final.csv` — Detailed payment records with fraud-relevant fields.
- `Purchases_Final.csv` — Transactions linking customers, products, and payments with valid dates and amounts.

## 🧠 Use Cases

| Use Case              | Features Used                                                                 |
|-----------------------|-------------------------------------------------------------------------------|
| Churn Analysis        | Customer ID, gender, product, location, payment method, sales channel         |
| Product Recommendation| Customer ID, Product ID, Category, Purchase Date                              |
| Customer Segmentation | Demographics + Spend Behaviour (total, average, frequency)                    |
| Fraud Detection       | Payment Date, Amount, Channel, CVV, AVS, 3DS, Auth Response                   |

## 🧱 Schema Overview

```plaintext
Customers ─┬─▶ Purchases ─┬─▶ Products
           └──────────────┴─▶ Payments
           
```       
## 🧾 Purchase Structure

Each purchase has:

- ✅ A **customer**
- ✅ A **product**
- ✅ A **valid payment** (same **date** and **amount** as purchase)
- ✅ A **defined sales channel** (_Note: "Online" ≠ "Cash"_)

---

## 💡 Features Ensured

- **Timeliness**: Dates are recent and relevant (last 60 days)
- **Completeness**: No missing values in required fields
- **Accuracy**: `Payment amount = Purchase amount`
- **Validity**: Online purchases do **not** allow `"Cash"` as payment method
- **Consistency**: `purchase_date == payment_date`
- **Uniqueness**: Clean, conflict-free primary keys across all tables

---

## 🚀 Getting Started

### 📥 1. Clone this Repo

```bash
git clone https://github.com/ADEYEMIBolaji/Retail-ML-Ready-Synthetic-Database.git
cd Retail-ML-Ready-Synthetic-Database
```

### 🧑‍💻 2. Load the Data

You can use these datasets in:

- **PostgreSQL** (recommended): Create schemas and import the CSV files using SQL scripts or PgAdmin.
- **Power BI / Tableau**: Load the CSVs directly or connect to your hosted database.
- **Python / Pandas**: Use for ML workflows, data analysis, or visualisation.

---

### 📦 3. Requirements (if using Python)

```bash
pip install pandas numpy
```

> **Note:** No personal or sensitive data is included. Everything is fully synthetic and safe for public use.

---

### 🤝 Contributions

Feel free to fork this repository and contribute:

- 🛠️ SQL schema definitions  
- 📊 Jupyter notebooks for ML or EDA  
- 📈 Dashboards or interactive reports  

---

### 📄 License

This project is released under the **MIT License** — free for personal and commercial use.



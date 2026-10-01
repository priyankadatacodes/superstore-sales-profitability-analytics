# 📊 Superstore Sales & Profitability Analytics

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python\&logoColor=white)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0%2B-4479A1?logo=mysql\&logoColor=white)](https://www.mysql.com/)
[![SQL](https://img.shields.io/badge/SQL-Analytics-336791)](https://www.mysql.com/)
[![Tableau](https://img.shields.io/badge/Tableau-Public-E97627?logo=tableau\&logoColor=white)](https://public.tableau.com/)
[![Status](https://img.shields.io/badge/Status-Completed-success)](https://github.com/priyankadatacodes/superstore-sales-profitability-analytics)
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)

> **End-to-end retail analytics project focused on sales performance, profitability, discount impact, geographic performance, customer value, and growth trends.**

---

## 📌 Executive Summary

This project analyzes the **Sample Superstore** dataset to identify revenue drivers, profitability gaps, discount-related margin pressure, geographic performance differences, and customer-value segments.

The solution follows a complete analytics workflow:

**Python → MySQL → SQL → Tableau → Business Insights**

### Core Business Question

> **Where is the business making money, where is it losing money, and why?**

---

## 🎯 Business Problem

Retail performance cannot be evaluated through revenue alone. The analysis focuses on understanding the relationship between **sales, profit, discounts, customers, geography, and time**.

### Key Business Questions

* Where is the business generating revenue?
* Which products and categories are driving profitability?
* Where is profitability under pressure?
* Are higher discounts associated with weaker margins?
* Which regions and locations perform differently?
* Which customers are valuable, loyal, at risk, or lost?
* Is sales growth translating into profitable growth?

---

## 📊 Key Metrics

| Metric              |             Value |
| ------------------- | ----------------: |
| Analysis Period     |         2014–2017 |
| Total Orders        |             5,009 |
| Customers           |               793 |
| Total Sales         | **$2,297,200.86** |
| Total Profit        |   **$286,397.02** |
| Profit Margin       |        **12.47%** |
| Average Order Value |       **$458.61** |
| Dashboards          |                 5 |

---

## 🧩 Analytical Approach

### 1. Data Preparation

* Loaded raw Superstore data using Python/Pandas
* Handled Windows-1252 encoding
* Validated duplicates and null values
* Retained legitimate negative-profit transactions
* Created analytical features

### 2. Exploratory Analysis

Analyzed:

* Sales trends
* Profitability
* Product performance
* Discount impact
* Geographic performance
* Customer behavior

### 3. SQL Analytics

Built reusable SQL queries and analytical views using:

* Aggregations
* Joins
* `CASE`
* CTEs
* Window functions
* `RANK()`
* `LAG()`
* `SUM() OVER()`

### 4. Customer Analytics

Implemented RFM analysis using:

* Recency
* Frequency
* Monetary value

Customer segments:

`Champions` · `Loyal` · `Recent` · `At Risk` · `Lost`

### 5. Business Intelligence

Created five Tableau dashboards covering executive, product, discount, geographic, and customer perspectives.

---

## 🛠️ Tech Stack

| Category             | Tools                                           |
| -------------------- | ----------------------------------------------- |
| **Programming**      | Python, Pandas                                  |
| **Database**         | MySQL                                           |
| **Data Integration** | SQLAlchemy                                      |
| **Querying**         | SQL                                             |
| **Visualization**    | Tableau Public                                  |
| **EDA**              | Matplotlib, Seaborn                             |
| **Analytics**        | RFM, Correlation Analysis, Time-Series Analysis |

---

## 🔄 Analytics Workflow

```text
                    ┌───────────────┐
                    │   Raw CSV     │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │    Python     │
                    │               │
                    │ • Cleaning    │
                    │ • Validation  │
                    │ • Features    │
                    │ • EDA         │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │     MySQL     │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │      SQL      │
                    │               │
                    │ • Analysis    │
                    │ • CTEs        │
                    │ • Windows     │
                    │ • Views       │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │    Tableau    │
                    │  Dashboards   │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │   Business    │
                    │   Insights    │
                    └───────────────┘
```

---

## 📁 Repository Structure

```text
superstore-sales-profitability-analytics/
│
├── data/
│   ├── Sample - Superstore.csv
│   └── data_raw.csv
│
├── python/
│   ├── 01_data_ingestion.py
│   ├── 02_data_cleaning.py
│   ├── 03_feature_engineering.py
│   ├── 04_eda_category_analysis.py
│   ├── 05_eda_discount_analysis.py
│   ├── 06_eda_geographic_analysis.py
│   ├── 07_rfm_segmentation.py
│   ├── 08_time_series_analysis.py
│   ├── 09_mysql_upload.py
│   ├── 10_tableau_export.py
│   ├── 11_correlation_analysis.py
│   ├── 12_quadrant_data_prep.py
│   └── 13_extended_analysis.py
│
├── sql/
│   ├── 01_database_setup.sql
│   ├── 02_table_creation.sql
│   ├── 03_sales_performance_queries.sql
│   ├── 04_product_profitability_queries.sql
│   ├── 05_discount_analysis_queries.sql
│   ├── 06_geographic_queries.sql
│   ├── 07_customer_rfm_queries.sql
│   ├── 08_window_functions.sql
│   └── 09_create_views.sql
│
├── tableau/
│   ├── superstore_dashboard.twbx
│   └── exports/
│
├── docs/
│   ├── case_study.md
│   └── dashboard_screenshots/
│
└── README.md
```

---

## 🗃️ Dataset

### Source

**Sample Superstore Dataset**

| Attribute  | Details                 |
| ---------- | ----------------------- |
| Records    | 9,994                   |
| Columns    | 21                      |
| Date Range | 2014–2017               |
| Customers  | 793                     |
| Encoding   | Windows-1252 (`cp1252`) |

### Key Fields

```text
Order Date
Ship Date
Customer ID
Customer Name
Segment
Region
State
City
Category
Sub-Category
Product Name
Sales
Quantity
Discount
Profit
```

### Data Quality

* **0** duplicate records
* **0** null values found during validation
* Negative profit values retained as genuine business losses

### Limitation

The dataset does not contain product cost or shipping cost fields. Therefore, profitability analysis relies on the provided `Profit` column.

---

# 📈 Key Findings

## 1. Discount & Profitability

The analysis found a **Pearson correlation of -0.864** between discount and profit margin.

| Discount | Profit Margin |
| -------- | ------------: |
| 0%       |        29.51% |
| 21–30%   |      Negative |
| 50%+     |      -119.20% |

> **Note:** Correlation does not establish causation.

An important product-level observation is **Binders**, which had an average discount of **37.23%** while still generating **$30,221.76 profit**.

This indicates that discount level alone does not determine profitability.

---

## 2. Product Profitability

**Tables** generated:

| Metric           |           Value |
| ---------------- | --------------: |
| Sales            |     $206,965.53 |
| Profit           | **-$17,725.48** |
| Average Discount |          26.13% |

This identifies Tables as an area for further SKU-level profitability analysis.

---

## 3. Geographic Performance

| Region  |      Profit |
| ------- | ----------: |
| West    | $108,418.45 |
| Central |  $39,706.36 |

Sales-profit quadrant analysis was used to identify geographic areas with relatively high sales but weaker profitability.

---

## 4. Customer Value

RFM analysis was performed across **793 customers**.

| Segment | Customers | Historical Sales |
| ------- | --------: | ---------------: |
| Loyal   |       211 |      $716,805.46 |
| Lost    |       297 |      $550,543.60 |
| At Risk |        90 |      $309,501.64 |

The results show that customer count and customer economic value are not necessarily aligned.

---

## 5. Growth & Profitability

| Year | Profit Margin |
| ---- | ------------: |
| 2014 |        10.23% |
| 2016 |        13.43% |
| 2017 |        12.74% |

Sales increased **20.36% in 2017**, while AOV declined despite increased order volume.

---

# 💼 Business Recommendations

Based on the analysis:

1. Move from blanket discounting toward **product-specific discount limits**.
2. Investigate **Tables at SKU level** to identify drivers of negative profitability.
3. Investigate factors contributing to the **West vs. Central profitability gap**.
4. Develop targeted reactivation strategies for **At-Risk customers**.
5. Monitor **sales growth together with profit and margin**.

---

# 📊 Tableau Dashboards

Five dashboards were developed:

| Dashboard                       | Focus                                         |
| ------------------------------- | --------------------------------------------- |
| **Executive Overview**          | Overall sales, profit, orders, AOV and trends |
| **Product & Sales Performance** | Products, sub-categories, sales and profit    |
| **Discount & Margin**           | Discount levels and profitability             |
| **Geographic Performance**      | Region, state and city performance            |
| **Customer & Growth**           | RFM segments and customer value               |

### Dashboard File

```text
tableau/superstore_dashboard.twbx
```

### Tableau Public

**[View Interactive Dashboard](ADD_YOUR_TABLEAU_LINK_HERE)**

---

# ⚙️ Setup & Execution

## Prerequisites

* Python 3.9+
* MySQL 8.0+
* Tableau Public or Tableau Desktop

## Clone Repository

```bash
git clone https://github.com/priyankadatacodes/superstore-sales-profitability-analytics.git
cd superstore-sales-profitability-analytics
```

## Install Dependencies

```bash
pip install pandas sqlalchemy pymysql matplotlib seaborn
```

## Create Database

```sql
CREATE DATABASE superstore;
```

## Add Dataset

Place the dataset here:

```text
data/Sample - Superstore.csv
```

## Run Python Pipeline

```bash
python python/01_data_ingestion.py
python python/02_data_cleaning.py
python python/03_feature_engineering.py
python python/04_eda_category_analysis.py
python python/05_eda_discount_analysis.py
python python/06_eda_geographic_analysis.py
python python/07_rfm_segmentation.py
python python/08_time_series_analysis.py
python python/09_mysql_upload.py
python python/10_tableau_export.py
```

### Additional Analysis

```bash
python python/11_correlation_analysis.py
python python/12_quadrant_data_prep.py
python python/13_extended_analysis.py
```

## Run SQL

```sql
SOURCE sql/01_database_setup.sql;
SOURCE sql/02_table_creation.sql;
SOURCE sql/09_create_views.sql;
```

## Open Tableau

```text
tableau/superstore_dashboard.twbx
```

---

# 🧠 Skills Demonstrated

### Data Analysis

* Exploratory Data Analysis
* Profitability Analysis
* Trend Analysis
* Geographic Analysis
* Customer Segmentation
* Correlation Analysis

### Python

* Pandas
* Data Cleaning
* Data Validation
* Feature Engineering
* RFM Segmentation

### SQL

* Aggregations
* Joins
* CASE Statements
* CTEs
* Window Functions
* Analytical Views

### MySQL

* Database Setup
* Table Creation
* Data Loading
* SQLAlchemy Integration

### Tableau

* Interactive Dashboards
* Calculated Fields
* LOD Expressions
* Parameters
* Dashboard Actions
* Data Relationships

---

# ⚠️ Limitations

* No product cost or shipping cost fields
* Profitability analysis relies on the provided `Profit` column
* Discount-profit correlation does not prove causation
* RFM segmentation is descriptive, not predictive
* Tableau Public requires a CSV-extract workflow
* Dataset ends in 2017 and does not represent current business conditions

---

# 🔮 Future Improvements

* Cohort-based customer retention analysis
* Churn prediction
* Customer lifetime value analysis
* Product cost and shipping cost analysis
* Automated Python and SQL refresh
* A/B testing of discount caps
* Interactive discount scenario analysis

---

# 👩‍💻 Author

**Priyanka Lakra**
Data Analyst

🌐 **Portfolio:** [bloomindata.in](https://bloomindata.in/)

💻 **GitHub:** [priyankadatacodes](https://github.com/priyankadatacodes)

---

# 📄 License

This project is licensed under the **MIT License**.

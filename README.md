# Supermarket Sales Analysis

## Project Overview
This project analyzes **500 supermarket sales transactions** to identify useful patterns in products, branches, categories, customer types, payment methods, and customer ratings.

The project was completed as part of the **IBM SkillsBuild Data Analytics with AI Academic Internship Program conducted by BharatCares in association with AICTE**.

## Problem Statement
The objective is to transform supermarket transaction data into clear business insights that can support inventory planning, branch performance analysis, payment strategy, and customer-service decisions.

## Dataset
Google Sheets dataset:
https://docs.google.com/spreadsheets/d/1QIX__4VObHFMEXnRM2xJyXmB5JAB2peHrJcQ41_U9TE/edit?usp=sharing

The submitted Excel dataset contains 500 transactions and 13 original fields plus the calculated sales check field used during analysis.

## Main Columns
- Invoice ID
- Date
- Branch
- City
- Customer Type
- Gender
- Product
- Category
- Quantity
- Unit Price
- Payment
- Rating
- Sales

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook
- Excel / OpenPyXL

## Analysis Performed
1. Loaded the supermarket dataset.
2. Checked dimensions, missing values, duplicate rows, and data types.
3. Recalculated sales as `Quantity × Unit Price` and compared it with the supplied Sales column.
4. Calculated overall KPIs.
5. Grouped sales by product, branch, and category.
6. Counted payment-method usage.
7. Compared average transaction value for Member and Normal customers.
8. Calculated average customer rating.
9. Created charts for major findings.
10. Derived business recommendations from the results.

## Key Results
| Metric | Result |
|---|---:|
| Total sales | ₹244,411.08 |
| Average transaction value | ₹488.82 |
| Highest-selling product | Cheese — ₹27,906.30 |
| Best-performing branch | Branch C (Mumbai) — ₹72,469.45 |
| Highest-sales category | Beverages — ₹56,108.24 |
| Most-used payment method | UPI — 127 transactions |
| Member average transaction | ₹483.14 |
| Normal average transaction | ₹497.07 |
| Average customer rating | 3.99/5 |

## Business Decisions
- Keep adequate inventory for high-sales products and categories.
- Study the practices associated with the strong sales performance of Branch C in Mumbai.
- Continue supporting UPI while keeping alternative payment methods available.
- Monitor customer ratings and improve service where necessary.
- Use the Member vs Normal spending comparison when designing membership offers.

## Project Files
- `GVL_Sahithi_SupermarketSalesAnalysis.ipynb` — complete Jupyter Notebook.
- `GVL_Sahithi_SupermarketSalesAnalysis.py` — Python version of the analysis.
- `requirements.txt` — Python dependencies.
- `GVL_Sahithi_SupermarketSalesAnalysis_ProjectReport.docx` — project report.
- `SUPER MARKET DATA.xlsx` — dataset used for analysis.

## Setup and Run Instructions
1. Install Python 3.
2. Place the notebook/script and `SUPER MARKET DATA.xlsx` in the same folder.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Open the notebook:
   ```bash
   jupyter notebook GVL_Sahithi_SupermarketSalesAnalysis.ipynb
   ```
5. Run the cells from top to bottom.

## Conclusion
The project shows how basic data-cleaning, aggregation, KPI calculation, and visualization techniques can convert supermarket transaction data into actionable business information.

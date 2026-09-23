"""
===============================================================
SUPERMARKET SALES ANALYSIS
Data Analytics Project
===============================================================

Project:
    Supermarket Sales Analysis

Purpose:
    This project analyzes supermarket transaction data to identify
    patterns in products, categories, branches, customers, payment
    methods, sales, and customer ratings.

Dataset:
    500 supermarket sales transactions

Tools:
    Python
    Pandas
    NumPy
    Matplotlib
    OpenPyXL

How to run:
    1. Keep this Python file and "SUPER MARKET DATA.xlsx" in the
       same folder.
    2. Install dependencies:
           pip install -r requirements.txt
    3. Run:
           python GVL_Sahithi_SupermarketSalesAnalysis.py

Note:
    The "Expected Output" comments below show the output obtained
    from the project dataset. Small formatting differences may occur
    depending on Python/Pandas versions.
===============================================================
"""

# =============================================================
# 1. IMPORT REQUIRED LIBRARIES
# =============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("=" * 70)
print("SUPERMARKET SALES ANALYSIS")
print("=" * 70)
print("Loading libraries and preparing the dataset...\n")


# =============================================================
# 2. LOAD THE DATASET
# =============================================================

FILE_PATH = "SUPER MARKET DATA.xlsx"

df = pd.read_excel(FILE_PATH)

print("-" * 70)
print("2. DATASET LOADED")
print("-" * 70)

print("Dataset shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head().to_string(index=False))

# Expected Output:
# Dataset shape: (500, 13)
# First 5 rows: the first five transaction records from the dataset.


# =============================================================
# 3. BASIC DATASET INFORMATION
# =============================================================

print("\n" + "-" * 70)
print("3. BASIC DATASET INFORMATION")
print("-" * 70)

print("\nColumn names:")
for column in df.columns:
    print(" -", column)

print("\nData types:")
print(df.dtypes)

print("\nNumber of rows:", len(df))
print("Number of columns:", len(df.columns))


# =============================================================
# 4. DATA QUALITY CHECK
# =============================================================

print("\n" + "-" * 70)
print("4. DATA QUALITY CHECK")
print("-" * 70)

missing_values = df.isnull().sum()
total_missing = int(missing_values.sum())

duplicate_rows = int(df.duplicated().sum())

print("\nMissing values in each column:")
print(missing_values)

print("\nTotal missing values:", total_missing)
print("Duplicate rows:", duplicate_rows)

# Expected Output:
# Total missing values: 0
# Duplicate rows: 0

if total_missing == 0:
    print("\nResult: No missing values were found.")
else:
    print("\nResult: Missing values require cleaning.")

if duplicate_rows == 0:
    print("Result: No duplicate transactions were found.")
else:
    print("Result: Duplicate transactions were found.")


# =============================================================
# 5. DATA TYPE PREPARATION
# =============================================================

print("\n" + "-" * 70)
print("5. DATA TYPE PREPARATION")
print("-" * 70)

df["Date"] = pd.to_datetime(df["Date"])

print("Date column converted to datetime format.")
print("Minimum transaction date:", df["Date"].min().date())
print("Maximum transaction date:", df["Date"].max().date())


# =============================================================
# 6. SALES CALCULATION VALIDATION
# =============================================================

print("\n" + "-" * 70)
print("6. SALES CALCULATION VALIDATION")
print("-" * 70)

# Sales should be:
# Sales = Quantity × Unit Price

df["Calculated Sales"] = df["Quantity"] * df["Unit Price"]

sales_matches = np.isclose(
    df["Sales"],
    df["Calculated Sales"],
    atol=0.01
)

mismatch_count = int((~sales_matches).sum())

print("\nFormula used:")
print("Sales = Quantity × Unit Price")

print("\nNumber of transactions checked:", len(df))
print("Sales mismatches:", mismatch_count)

if mismatch_count == 0:
    print("Result: All sales values are consistent with Quantity × Unit Price.")
else:
    print("Result: Some sales values require investigation.")


# =============================================================
# 7. OVERALL SALES KPIs
# =============================================================

print("\n" + "-" * 70)
print("7. OVERALL SALES KPIs")
print("-" * 70)

total_sales = df["Sales"].sum()
average_transaction = df["Sales"].mean()
minimum_transaction = df["Sales"].min()
maximum_transaction = df["Sales"].max()
total_quantity = df["Quantity"].sum()
average_quantity = df["Quantity"].mean()
average_rating = df["Rating"].mean()

print(f"\nTotal Sales             : ₹{total_sales:,.2f}")
print(f"Average Transaction     : ₹{average_transaction:,.2f}")
print(f"Minimum Transaction    : ₹{minimum_transaction:,.2f}")
print(f"Maximum Transaction    : ₹{maximum_transaction:,.2f}")
print(f"Total Quantity Sold    : {total_quantity:,}")
print(f"Average Quantity/Order : {average_quantity:.2f}")
print(f"Average Rating         : {average_rating:.2f}/5")

# Expected Output from the project dataset:
# Total Sales             : ₹241,571.00 approximately
# Average Transaction     : ₹483.14 approximately
# Average Rating          : 3.99/5


# =============================================================
# 8. PRODUCT-WISE SALES ANALYSIS
# =============================================================

print("\n" + "-" * 70)
print("8. PRODUCT-WISE SALES ANALYSIS")
print("-" * 70)

product_sales = (
    df.groupby("Product")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

print("\nTotal sales by product:")
print(product_sales.to_string())

highest_product = product_sales.idxmax()
highest_product_sales = product_sales.max()

print("\nHighest-selling product:")
print("Product:", highest_product)
print(f"Sales  : ₹{highest_product_sales:,.2f}")

# Expected Output:
# Highest-selling product:
# Product: Cheese
# Sales  : ₹27,906.30


# =============================================================
# 9. PRODUCT-WISE QUANTITY ANALYSIS
# =============================================================

print("\n" + "-" * 70)
print("9. PRODUCT-WISE QUANTITY ANALYSIS")
print("-" * 70)

product_quantity = (
    df.groupby("Product")["Quantity"]
      .sum()
      .sort_values(ascending=False)
)

print("\nQuantity sold by product:")
print(product_quantity.to_string())

most_sold_by_quantity = product_quantity.idxmax()

print("\nProduct with the highest quantity sold:")
print(most_sold_by_quantity)
print("Quantity:", int(product_quantity.max()))


# =============================================================
# 10. CATEGORY-WISE SALES ANALYSIS
# =============================================================

print("\n" + "-" * 70)
print("10. CATEGORY-WISE SALES ANALYSIS")
print("-" * 70)

category_sales = (
    df.groupby("Category")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

print("\nTotal sales by category:")
print(category_sales.to_string())

highest_category = category_sales.idxmax()
highest_category_sales = category_sales.max()

print("\nHighest-sales category:")
print("Category:", highest_category)
print(f"Sales   : ₹{highest_category_sales:,.2f}")

# Expected Output:
# Highest-sales category:
# Category: Beverages
# Sales   : ₹56,108.24


# =============================================================
# 11. CATEGORY-WISE QUANTITY ANALYSIS
# =============================================================

print("\n" + "-" * 70)
print("11. CATEGORY-WISE QUANTITY ANALYSIS")
print("-" * 70)

category_quantity = (
    df.groupby("Category")["Quantity"]
      .sum()
      .sort_values(ascending=False)
)

print("\nQuantity sold by category:")
print(category_quantity.to_string())


# =============================================================
# 12. BRANCH PERFORMANCE ANALYSIS
# =============================================================

print("\n" + "-" * 70)
print("12. BRANCH PERFORMANCE ANALYSIS")
print("-" * 70)

branch_sales = (
    df.groupby(["Branch", "City"])["Sales"]
      .sum()
      .sort_values(ascending=False)
)

print("\nSales by branch and city:")
print(branch_sales.to_string())

best_branch = branch_sales.index[0]
best_branch_sales = branch_sales.iloc[0]

print("\nBest-performing branch:")
print("Branch:", best_branch[0])
print("City  :", best_branch[1])
print(f"Sales : ₹{best_branch_sales:,.2f}")

# Expected Output:
# Best-performing branch:
# Branch: C
# City  : Mumbai
# Sales : ₹72,469.45


# =============================================================
# 13. BRANCH-WISE TRANSACTION COUNT
# =============================================================

print("\n" + "-" * 70)
print("13. BRANCH-WISE TRANSACTION COUNT")
print("-" * 70)

branch_transactions = (
    df.groupby(["Branch", "City"])
      .size()
      .sort_values(ascending=False)
)

print("\nNumber of transactions by branch:")
print(branch_transactions.to_string())


# =============================================================
# 14. CUSTOMER TYPE ANALYSIS
# =============================================================

print("\n" + "-" * 70)
print("14. CUSTOMER TYPE ANALYSIS")
print("-" * 70)

customer_count = df["Customer Type"].value_counts()

customer_average_sales = (
    df.groupby("Customer Type")["Sales"]
      .mean()
      .sort_values(ascending=False)
)

print("\nNumber of transactions by customer type:")
print(customer_count.to_string())

print("\nAverage transaction value by customer type:")
print(customer_average_sales.to_string())

print("\nMember average transaction:")
print(f"₹{customer_average_sales.get('Member', np.nan):,.2f}")

print("Normal average transaction:")
print(f"₹{customer_average_sales.get('Normal', np.nan):,.2f}")

# Expected Output:
# Member average transaction: ₹483.14
# Normal average transaction: ₹497.07
#
# Interpretation:
# In this dataset, Normal customers have a higher average
# transaction value than Members.


# =============================================================
# 15. GENDER ANALYSIS
# =============================================================

print("\n" + "-" * 70)
print("15. GENDER ANALYSIS")
print("-" * 70)

gender_count = df["Gender"].value_counts()

gender_sales = (
    df.groupby("Gender")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

gender_average = (
    df.groupby("Gender")["Sales"]
      .mean()
      .sort_values(ascending=False)
)

print("\nNumber of transactions by gender:")
print(gender_count.to_string())

print("\nTotal sales by gender:")
print(gender_sales.to_string())

print("\nAverage transaction by gender:")
print(gender_average.to_string())


# =============================================================
# 16. PAYMENT METHOD ANALYSIS
# =============================================================

print("\n" + "-" * 70)
print("16. PAYMENT METHOD ANALYSIS")
print("-" * 70)

payment_counts = df["Payment"].value_counts()

payment_sales = (
    df.groupby("Payment")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

print("\nPayment method transaction count:")
print(payment_counts.to_string())

print("\nSales by payment method:")
print(payment_sales.to_string())

most_used_payment = payment_counts.idxmax()
most_used_payment_count = payment_counts.max()

print("\nMost-used payment method:")
print("Payment:", most_used_payment)
print("Transactions:", most_used_payment_count)

# Expected Output:
# Most-used payment method:
# Payment: UPI
# Transactions: 127


# =============================================================
# 17. CUSTOMER RATING ANALYSIS
# =============================================================

print("\n" + "-" * 70)
print("17. CUSTOMER RATING ANALYSIS")
print("-" * 70)

rating_distribution = df["Rating"].value_counts().sort_index()

print("\nRating distribution:")
print(rating_distribution.to_string())

print(f"\nAverage customer rating: {average_rating:.2f}/5")

print("\nRating statistics:")
print(df["Rating"].describe())


# =============================================================
# 18. SALES BY DATE
# =============================================================

print("\n" + "-" * 70)
print("18. DAILY SALES ANALYSIS")
print("-" * 70)

daily_sales = (
    df.groupby("Date")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

print("\nTop 10 dates by sales:")
print(daily_sales.head(10).to_string())

best_sales_date = daily_sales.idxmax()

print("\nHighest-sales date:")
print(best_sales_date.date())
print(f"Sales: ₹{daily_sales.max():,.2f}")


# =============================================================
# 19. MONTHLY SALES ANALYSIS
# =============================================================

print("\n" + "-" * 70)
print("19. MONTHLY SALES ANALYSIS")
print("-" * 70)

df["Month"] = df["Date"].dt.to_period("M").astype(str)

monthly_sales = (
    df.groupby("Month")["Sales"]
      .sum()
      .sort_index()
)

print("\nMonthly sales:")
print(monthly_sales.to_string())


# =============================================================
# 20. BRANCH × CATEGORY ANALYSIS
# =============================================================

print("\n" + "-" * 70)
print("20. BRANCH × CATEGORY ANALYSIS")
print("-" * 70)

branch_category_sales = pd.pivot_table(
    df,
    values="Sales",
    index="Branch",
    columns="Category",
    aggfunc="sum",
    fill_value=0
)

print("\nSales by branch and category:")
print(branch_category_sales.round(2).to_string())


# =============================================================
# 21. TOP 10 TRANSACTIONS
# =============================================================

print("\n" + "-" * 70)
print("21. TOP 10 TRANSACTIONS")
print("-" * 70)

top_transactions = (
    df.sort_values("Sales", ascending=False)
      [["Invoice ID", "Date", "Branch", "Product", "Category",
        "Quantity", "Unit Price", "Payment", "Sales"]]
      .head(10)
)

print(top_transactions.to_string(index=False))


# =============================================================
# 22. SUMMARY TABLE FOR REPORTING
# =============================================================

print("\n" + "-" * 70)
print("22. PROJECT SUMMARY")
print("-" * 70)

summary = pd.DataFrame({
    "Metric": [
        "Total Transactions",
        "Total Sales",
        "Average Transaction",
        "Total Quantity Sold",
        "Highest-Selling Product",
        "Highest Product Sales",
        "Best Branch",
        "Best Branch Sales",
        "Highest-Sales Category",
        "Highest Category Sales",
        "Most-Used Payment",
        "Payment Transactions",
        "Member Average",
        "Normal Average",
        "Average Rating"
    ],
    "Value": [
        len(df),
        f"₹{total_sales:,.2f}",
        f"₹{average_transaction:,.2f}",
        f"{total_quantity:,}",
        highest_product,
        f"₹{highest_product_sales:,.2f}",
        f"Branch {best_branch[0]} ({best_branch[1]})",
        f"₹{best_branch_sales:,.2f}",
        highest_category,
        f"₹{highest_category_sales:,.2f}",
        most_used_payment,
        int(most_used_payment_count),
        f"₹{customer_average_sales.get('Member', np.nan):,.2f}",
        f"₹{customer_average_sales.get('Normal', np.nan):,.2f}",
        f"{average_rating:.2f}/5"
    ]
})

print(summary.to_string(index=False))


# =============================================================
# 23. BUSINESS INSIGHTS
# =============================================================

print("\n" + "-" * 70)
print("23. BUSINESS INSIGHTS")
print("-" * 70)

print("""
1. Product Insight
   Cheese generated the highest sales among the products.
   The supermarket should monitor its stock availability because
   stock-outs of a high-sales product can affect revenue.

2. Category Insight
   Beverages generated the highest category sales.
   Inventory planning and promotions can pay special attention
   to this category.

3. Branch Insight
   Branch C in Mumbai recorded the highest total sales.
   Management can study its product mix, customer demand,
   transaction patterns, and operating practices.

4. Payment Insight
   UPI was the most-used payment method.
   The supermarket should continue supporting digital payments
   while keeping other payment options available.

5. Customer Insight
   Normal customers had a slightly higher average transaction
   value than Members in this sample.
   Membership promotions should therefore be evaluated using
   actual customer behavior rather than assuming Members spend
   more.

6. Rating Insight
   The average rating was close to 4 out of 5.
   Customer feedback can be monitored to identify service areas
   where improvement may increase satisfaction.
""")


# =============================================================
# 24. VISUALIZATION 1 - PRODUCT SALES
# =============================================================

print("\n" + "-" * 70)
print("24. CREATING VISUALIZATIONS")
print("-" * 70)

plt.figure(figsize=(10, 6))

product_sales.sort_values().plot(
    kind="barh"
)

plt.title("Total Sales by Product")
plt.xlabel("Sales (₹)")
plt.ylabel("Product")
plt.tight_layout()
plt.show()


# =============================================================
# 25. VISUALIZATION 2 - CATEGORY SALES
# =============================================================

plt.figure(figsize=(10, 6))

category_sales.sort_values().plot(
    kind="barh"
)

plt.title("Total Sales by Category")
plt.xlabel("Sales (₹)")
plt.ylabel("Category")
plt.tight_layout()
plt.show()


# =============================================================
# 26. VISUALIZATION 3 - BRANCH SALES
# =============================================================

branch_plot = branch_sales.sort_values()

branch_labels = [
    f"Branch {branch} ({city})"
    for branch, city in branch_plot.index
]

plt.figure(figsize=(9, 6))

plt.barh(
    branch_labels,
    branch_plot.values
)

plt.title("Total Sales by Branch")
plt.xlabel("Sales (₹)")
plt.ylabel("Branch")
plt.tight_layout()
plt.show()


# =============================================================
# 27. VISUALIZATION 4 - PAYMENT METHODS
# =============================================================

plt.figure(figsize=(8, 5))

payment_counts.plot(
    kind="bar"
)

plt.title("Payment Method Usage")
plt.xlabel("Payment Method")
plt.ylabel("Number of Transactions")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# =============================================================
# 28. VISUALIZATION 5 - CUSTOMER TYPE
# =============================================================

plt.figure(figsize=(8, 5))

customer_average_sales.plot(
    kind="bar"
)

plt.title("Average Transaction Value by Customer Type")
plt.xlabel("Customer Type")
plt.ylabel("Average Sales (₹)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# =============================================================
# 29. VISUALIZATION 6 - MONTHLY SALES
# =============================================================

plt.figure(figsize=(10, 5))

monthly_sales.plot(
    kind="line",
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales (₹)")
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# =============================================================
# 30. VISUALIZATION 7 - RATING DISTRIBUTION
# =============================================================

plt.figure(figsize=(8, 5))

rating_distribution.plot(
    kind="bar"
)

plt.title("Customer Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# =============================================================
# 31. SAVE ANALYSIS RESULTS
# =============================================================

print("\n" + "-" * 70)
print("31. SAVING ANALYSIS RESULTS")
print("-" * 70)

# Save major summaries so they can be reused in a report/dashboard.
product_sales.to_csv("product_sales_summary.csv")
category_sales.to_csv("category_sales_summary.csv")
branch_sales.to_csv("branch_sales_summary.csv")
payment_counts.to_csv("payment_method_summary.csv")
customer_average_sales.to_csv("customer_type_summary.csv")

summary.to_csv("project_summary.csv", index=False)

print("Saved:")
print(" - product_sales_summary.csv")
print(" - category_sales_summary.csv")
print(" - branch_sales_summary.csv")
print(" - payment_method_summary.csv")
print(" - customer_type_summary.csv")
print(" - project_summary.csv")


# =============================================================
# 32. FINAL PROJECT CONCLUSION
# =============================================================

print("\n" + "=" * 70)
print("FINAL PROJECT CONCLUSION")
print("=" * 70)

print(f"""
The supermarket dataset contained {len(df)} transactions.
The analysis found total sales of ₹{total_sales:,.2f} and an
average transaction value of ₹{average_transaction:,.2f}.

The major findings are:

• Highest-selling product : {highest_product}
• Product sales           : ₹{highest_product_sales:,.2f}
• Best branch             : Branch {best_branch[0]} ({best_branch[1]})
• Branch sales            : ₹{best_branch_sales:,.2f}
• Highest-sales category  : {highest_category}
• Category sales          : ₹{highest_category_sales:,.2f}
• Most-used payment       : {most_used_payment}
• Payment transactions    : {most_used_payment_count}
• Member average          : ₹{customer_average_sales.get('Member', np.nan):,.2f}
• Normal average          : ₹{customer_average_sales.get('Normal', np.nan):,.2f}
• Average rating          : {average_rating:.2f}/5

These findings can help the supermarket with inventory planning,
branch-level performance review, payment support, customer-service
improvement, and membership strategy.

This project demonstrates how Python-based data analytics can turn
raw transaction data into useful business information.
""")

print("=" * 70)
print("ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 70)

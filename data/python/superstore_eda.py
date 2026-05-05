import pandas as pd
import matplotlib.pyplot as plt
import os
from pathlib import Path

# ============================================================
# Load Dataset
# This block loads the Superstore dataset into a pandas DataFrame.
# latin1 encoding is used to avoid character decoding issues.
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent

csv_path = PROJECT_ROOT / "Sample - Superstore.csv"
df = pd.read_csv(csv_path, encoding="latin1")

# Finding:
# Python confirms the dataset loads successfully with 9,994 rows and 21 columns, matching the expected Superstore structure.
# Python also reveals the dataset contains 5,009 unique orders, 1,850 unique customers, and 1,849 unique products.
# This means the file is suitable for independently verifying the SQL analysis across orders, customers, products, regions, and categories.

# ============================================================
# Inspect Dataset Structure
# This block checks data types, missing values, and previews the first few rows.
# This helps confirm whether the dataset needs cleaning before analysis.
# ============================================================

print("\n--- Dataset Data Types ---")
print(df.dtypes)

print("\n--- Missing Values by Column ---")
print(df.isnull().sum())

print("\n--- First 5 Rows ---")
print(df.head())

# Finding:
# Python confirms the dataset has no missing values across the columns used in this analysis.
# Python also reveals that Order Date and Ship Date are stored as object columns before conversion.
# This means date columns must be converted into datetime format before analysis.

# ============================================================
# Category Sales, Profit, and Profit Margin Check
# This block groups the data by category and calculates total sales, total profit,
# and profit margin to verify the SQL category analysis.
# ============================================================
category_performance = (
    df.groupby('Category')
    .agg(
        total_sales=('Sales', 'sum'),
        total_profit=('Profit', 'sum')
    )
)

category_performance['profit_margin_pct'] = (
    category_performance['total_profit'] / category_performance['total_sales'] * 100
)

category_performance = (
    category_performance
    .round(2)
    .sort_values('total_sales', ascending=False)
)

print("\n--- Category Sales, Profit, and Profit Margin ---")
print(category_performance)

# Finding:
# Python confirms the SQL result that Technology is the top category with $836,154.03 in sales, $145,454.95 in profit, and a 17.40% profit margin.
# Python also reveals that Furniture generated $741,999.80 in sales but only $18,451.27 in profit, contributing far less profit than Technology and Office Supplies despite ranking second by revenue.
# This means Furniture appears strong by sales but weak by profitability, so it should be reviewed for discounts, costs, or pricing issues.

# ============================================================
# Regional Sales and Profit Check
# This block groups the data by region and calculates total sales, total profit,
# and profit margin to verify the regional SQL analysis.
# ============================================================

region_performance = (
    df.groupby('Region')
    .agg(
        total_sales=('Sales', 'sum'),
        total_profit=('Profit', 'sum')
    )
)

region_performance['profit_margin_pct'] = (
    region_performance['total_profit'] / region_performance['total_sales'] * 100
)

region_performance = (
    region_performance
    .round(2)
    .sort_values('total_sales', ascending=False)
)

print("\n--- Regional Sales and Profit Performance ---")
print(region_performance)

# Finding:
# Python confirms the SQL result that the West region leads with $725,457.82 in sales, $108,418.45 in profit, and a 14.94% profit margin.
# Python also reveals that Central generated higher sales than South, with $501,239.89 compared with $391,721.91, but Central had a weaker margin of 7.92% compared with South's 11.93%.
# This means Central has healthy revenue but weaker profitability, so it should be investigated further by discount level, category, and sub-category.

# ============================================================
# Central Region Sub-Category Profitability Check
# This block filters the dataset to the Central region and groups by sub-category.
# This verifies which sub-categories are causing weak Central profitability.
# ============================================================

central_subcategory = (
    df[df['Region'] == 'Central']
    .groupby('Sub-Category')
    .agg(
        total_sales=('Sales', 'sum'),
        total_profit=('Profit', 'sum')
    )
)

central_subcategory['profit_margin_pct'] = (
    central_subcategory['total_profit'] / central_subcategory['total_sales'] * 100
)

central_subcategory = (
    central_subcategory
    .round(2)
    .sort_values('total_profit', ascending=True)
)

print("\n--- Central Region Sub-Category Profitability ---")
print(central_subcategory)

# Finding:
# Python confirms the SQL result that Furnishings was the weakest Central sub-category, with $15,254.37 in sales, -$3,906.22 in profit, and a -25.61% profit margin.
# Python also reveals that 7 out of 17 Central sub-categories produced negative profit.
# This means Central's weak profitability is not caused by one product area only, but by multiple loss-making sub-categories.


# ============================================================
# Convert Date Columns
# This block converts Order Date and Ship Date into datetime format.
# It also creates Year and Month columns for monthly trend analysis.
# ============================================================

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month

print("\n--- Date Range ---")
print("Minimum Order Date:", df['Order Date'].min())
print("Maximum Order Date:", df['Order Date'].max())

# Finding:
# Python confirms the dataset covers orders from 2014-01-03 to 2017-12-30, matching the expected Superstore analysis period.
# Python also reveals that Year and Month can be extracted directly from the cleaned Order Date column.
# This means the dataset is ready for accurate monthly sales and profit trend analysis.


# ============================================================
# Monthly Sales and Profit Trend Check
# This block groups the data by year and month.
# It verifies the strongest and weakest monthly performance found in SQL.
# ============================================================

monthly_trend = (
    df.groupby(['Year', 'Month'])
    .agg(
        total_sales=('Sales', 'sum'),
        total_profit=('Profit', 'sum')
    )
    .round(2)
    .reset_index()
)

print("\n--- Monthly Sales and Profit Trend ---")
print(monthly_trend)

# Finding:
# Python confirms the SQL result that November 2017 had the highest sales at $118,447.83, while December 2016 had the highest profit at $17,885.31.
# Python also reveals that January 2015 was the weakest profit month, recording a loss of -$3,281.01.
# This means revenue and profit should be analysed separately because the highest sales month was not the same as the highest profit month.


# ============================================================
# Create Discount Groups
# This block converts raw discount values into readable discount categories.
# These categories allow Python to verify the SQL discount analysis.
# ============================================================

df['Discount Type'] = pd.cut(
    df['Discount'],
    bins=[-0.0001, 0, 0.2, 0.4, 1],
    labels=['No Discount', 'Low Discount', 'Medium Discount', 'High Discount'],
    include_lowest=True
)

print("\n--- Discount Type Categories ---")
print(df['Discount Type'].unique())

# Finding:
# Python confirms the SQL discount grouping by creating 4 discount categories: No Discount, Low Discount, Medium Discount, and High Discount.
# Python also reveals that discount values are stored as decimal percentages, so grouping them makes the results easier to interpret.
# This means the discount analysis can be presented clearly in business terms instead of raw decimal values.


# ============================================================
# Discount Impact on Profitability Check
# This block groups orders by discount type and calculates average profit,
# total profit, and number of orders to verify the SQL discount findings.
# ============================================================

discount_analysis = (
    df.groupby('Discount Type', observed=False)
    .agg(
        average_profit=('Profit', 'mean'),
        total_profit=('Profit', 'sum'),
        num_orders=('Profit', 'count')
    )
    .round(2)
)

print("\n--- Discount Impact on Profitability ---")
print(discount_analysis)

# Finding:
# Python confirms the SQL result that no-discount orders were the most profitable, with 4,798 orders, $66.90 average profit, and $320,987.60 total profit.
# Python also reveals that high-discount orders produced the largest total loss at -$99,558.59, with an average loss of -$106.71 per row.
# This means high discounting has a major negative impact on profitability and should be reviewed closely.


# ============================================================
# Top 10 Products by Sales Check
# This block ranks products by total sales and calculates total profit and units sold.
# It verifies whether the highest-selling products are also profitable.
# ============================================================

top_products = (
    df.groupby('Product Name')
    .agg(
        total_sales=('Sales', 'sum'),
        total_profit=('Profit', 'sum'),
        total_units=('Quantity', 'sum')
    )
    .round(2)
    .sort_values('total_sales', ascending=False)
    .head(10)
)

print("\n--- Top 10 Products by Sales ---")
print(top_products)

# Finding:
# Python confirms the SQL result that the Canon imageCLASS 2200 Advanced Copier was the highest-selling product, with $61,599.82 in sales, $25,199.93 in profit, and 20 units sold.
# Python also reveals that 3 of the top 10 products by sales had negative profit, while the GBC Ibimaster 500 Manual ProClick Binding System sold the most units at 48 but generated only $760.98 in profit.
# This means product performance should not be judged by sales alone because some high-sales or high-volume products may be weak from a profitability perspective.


# ============================================================
# Top 20 Customers by Revenue Check
# This block ranks customers by total revenue and calculates order count and total profit.
# It verifies whether high-revenue customers are also profitable.
# ============================================================

top_customers = (
    df.groupby('Customer Name')
    .agg(
        num_orders=('Order ID', 'nunique'),
        total_revenue=('Sales', 'sum'),
        total_profit=('Profit', 'sum')
    )
    .round(2)
    .sort_values('total_revenue', ascending=False)
    .head(20)
)

print("\n--- Top 20 Customers by Revenue ---")
print(top_customers)

# Finding:
# Python confirms the SQL result that Sean Miller was the highest-revenue customer, with $25,043.05 in revenue across 5 orders, but -$1,980.74 in profit.
# Python also reveals that Tamara Chand was more valuable from a profit perspective, generating $8,981.32 profit from $19,052.22 revenue across 5 orders.
# This means customer value should be measured using both revenue and profit, not revenue alone.

# ============================================================
# What correlation does Discount and profit have
# This block check if Higher discount relates to lower profit 
# Correlation helps measure the relationship between Discount and Profit
# ============================================================

discount_profit_corr = df['Discount'].corr(df['Profit'])

print("\n--- Discount and Profit Correlation ---")
print(round(discount_profit_corr, 3)) 

# Finding: 
# The correlation of -0.219 suggests that higher discounts are linked to lower profit, but the relationship is not very strong. 
# However, discount is not the only reason profit changes, because other factors such as product category, shipping cost, and region may also affect profit.
# This means discount alone should not be the focus of a profitability review
# However, medium and high discount orders generated almost $135,000 in total losses, even though most transactions had low or no discount.
# This means discounting is not a widespread issue across all orders, but discounts above 20% have a severe impact on profitability.

os.makedirs("visuals", exist_ok=True)

# ============================================================
# This block create a horizontal bar chart for category based on profit margin performance
# ============================================================

category_performance = category_performance.sort_values(by="profit_margin_pct")
plt.figure(figsize=(8, 5))

plt.barh(
    category_performance.index,
    category_performance["profit_margin_pct"]
)

plt.xlabel("Profit Margin %")
plt.ylabel("Category")
plt.title("Profit Margin by Category")

plt.tight_layout()
plt.savefig('visuals/01_category_performance_margin.png', dpi=150, bbox_inches='tight')

# ============================================================
# Line chart showing total profit by month over time
# ============================================================
# Convert year+month to a string 
monthly_trend["YearMonth"] = pd.to_datetime(
    monthly_trend["Year"].astype(str) + "-" + monthly_trend["Month"].astype(str),
    format="%Y-%m"
)
#sort so it display in orders of year and month 
monthly_trend = monthly_trend.sort_values("YearMonth")
plt.figure(figsize=(10, 5))
plt.plot(monthly_trend['YearMonth'], monthly_trend['total_profit'])
plt.xlabel("Month")
plt.ylabel("Total profit")
plt.title("Monthly Profit Trends")
plt.xticks(rotation=45)
plt.tight_layout()
# Draw a horizontal line at the 0 value, the colour of the line is black, and the width of line is 1 
plt.axhline(0, color='black', linewidth=1)
plt.savefig('visuals/monthy_trends.png', dpi=150, bbox_inches='tight')

# ============================================================
# Bar chart showing average profit by discount tier
# Green = profitable, red = loss-making
# ============================================================
#Discount vs profit 
plt.figure(figsize=(8, 5))
# add colour s
colors = [
    "green" if profit > 0 else "red"
    for profit in discount_analysis["average_profit"]
]
plt.bar(
    discount_analysis.index, 
    discount_analysis['average_profit'], 
    color = colors
)

# Draws a horizontal line at zero, so we can see which discount is profitable and which is losing money 
plt.xlabel('Discount tier')
plt.ylabel('Average profit')
plt.title('Average profit based on discount tier')
# Draws a horizontal line at zero, so we can see which discount is profitable and which is losing money 
plt.axhline(0, color="black", linewidth=1)
plt.savefig('visuals/average_profit_by_discount.png', dpi=150, bbox_inches='tight')

# ============================================================
# Scatter plot based on discount vs profit at indivual order level
# ============================================================

plt.figure(figsize=(8, 5))
plt.scatter(df["Discount"], df["Profit"], alpha=0.4)

plt.xlabel("Discount")
plt.ylabel("Profit")
plt.title("Discount vs Profit")

plt.axhline(0, color="black", linewidth=1)

plt.tight_layout()
plt.savefig('visuals/discount_vs_profit.png', dpi=150, bbox_inches='tight')

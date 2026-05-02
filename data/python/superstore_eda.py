
import pandas as pd


# ============================================================
# Load Dataset
# This block loads the Superstore dataset into a pandas DataFrame.
# latin1 encoding is used to avoid character decoding errors.
# ============================================================

df = pd.read_csv('Sample - Superstore.csv', encoding='latin1')

# ============================================================
# Inspect Dataset Structure
# This block checks data types, missing values, and a preview of the data.
# This helps confirm whether the dataset needs cleaning before analysis.
# ============================================================

print("\n--- Dataset Data Types ---")
print(df.dtypes)

print("\n--- Missing Values by Column ---")
print(df.isnull().sum())

print("\n--- First 5 Rows ---")
print(df.head())

# Finding:
# Initial inspection helps confirm column formats and data quality before analysis.

# ============================================================
# Regional Sales and Profit Check
# This block groups the data by region and calculates total sales and profit.
# It is used to validate the regional performance analysis done in SQL.
# ============================================================

region_performance = (
    df.groupby('Region')[['Sales', 'Profit']]
    .sum()
    .round(2)
    .sort_values('Sales', ascending=False)
)

print("\n--- Regional Sales and Profit Performance ---")
print(region_performance)

# Finding:
# This confirms which regions generate the most sales and profit.
# Central can be compared against other regions to check whether its profit is weak despite healthy sales.


# ============================================================
# Category Sales, Profit, and Profit Margin Check
# This block groups the data by category and calculates sales, profit, and profit margin.
# It helps validate whether the best-selling categories are also profitable.
# ============================================================

category_performance = df.groupby('Category')[['Sales', 'Profit']].sum()

category_performance['profit_margin_pct'] = (
    category_performance['Profit'] / category_performance['Sales'] * 100
).round(2)

category_performance = (
    category_performance
    .round(2)
    .sort_values('Sales', ascending=False)
)

print("\n--- Category Sales, Profit, and Profit Margin ---")
print(category_performance)

# Finding:
# This confirms category-level performance across sales, profit, and margin.
# The result should match the SQL category analysis.


# ============================================================
# Central Region Sub-Category Profitability Check
# This block filters the dataset to the Central region.
# It then groups by sub-category to identify which areas are reducing Central's profitability.
# ============================================================

central_subcategory = (
    df[df['Region'] == 'Central']
    .groupby('Sub-Category')[['Sales', 'Profit']]
    .sum()
)

central_subcategory['profit_margin_pct'] = (
    central_subcategory['Profit'] / central_subcategory['Sales'] * 100
).round(2)

central_subcategory = (
    central_subcategory
    .round(2)
    .sort_values('Profit', ascending=True)
)

print("\n--- Central Region Sub-Category Profitability ---")
print(central_subcategory)

# Finding:
# This helps confirm which Central sub-categories are loss-making.
# These results can support the SQL follow-up analysis on Central's weak profit margin.


# ============================================================
# Convert Date Columns
# This block converts Order Date and Ship Date into datetime format.
# It also creates Year and Month columns for monthly trend analysis.
# ============================================================

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month

# Finding:
# Date columns are now ready for time-based analysis.


# ============================================================
# Monthly Sales and Profit Trend Check
# This block groups the data by year and month.
# It calculates monthly sales and profit to validate the monthly trend analysis done in SQL.
# ============================================================

monthly_trend = (
    df.groupby(['Year', 'Month'])[['Sales', 'Profit']]
    .sum()
    .round(2)
)

print("\n--- Monthly Sales and Profit Trend ---")
print(monthly_trend)

# Finding:
# This confirms monthly sales and profit trends over time.
# The output can be sorted further to identify the highest sales month and highest profit month.


# ============================================================
# Create Discount Groups
# This block converts raw discount values into readable discount categories.
# These categories make it easier to compare profitability by discount level.
# ============================================================

df['Discount Type'] = pd.cut(
    df['Discount'],
    bins=[-0.1, 0, 0.2, 0.4, 1],
    labels=['No Discount', 'Low Discount', 'Medium Discount', 'High Discount']
)

print("\n--- Discount Type Categories ---")
print(df['Discount Type'].unique())

# Finding:
# Discount values have been grouped into clearer categories for analysis.


# ============================================================
# Discount Impact on Profitability Check
# This block groups orders by discount type.
# It calculates average profit, total profit, and order count for each discount group.
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
# This helps validate whether higher discount levels are linked to weaker profitability.
# The result can support the SQL discount analysis.


# ============================================================
# Top 10 Products by Sales
# This block ranks products by total sales.
# It also calculates units sold and total profit for each product.
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
# This checks whether the highest-selling products are also profitable.
# It can support the SQL product analysis where high sales did not always mean high profit.


# ============================================================
# Top 20 Customers by Revenue
# This block ranks customers by total revenue.
# It also calculates number of orders and total profit for each customer.
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
# This checks whether high-revenue customers are also profitable.
# It supports the customer segmentation analysis from SQL.

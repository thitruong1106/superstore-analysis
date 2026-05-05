SELECT
    `Customer Name`,
    COUNT(DISTINCT `Order ID`) AS num_orders,
    ROUND(SUM(Sales), 2) AS total_revenue,
    ROUND(SUM(Profit), 2) AS total_profit,
    CASE
        WHEN SUM(Sales) > 5000 THEN 'High value'
        WHEN SUM(Sales) > 1000 THEN 'Mid value'
        ELSE 'Low value'
    END AS customer_tier
FROM orders
GROUP BY `Customer Name`
ORDER BY total_revenue DESC
LIMIT 20;

/*
Analysis: Customer Segmentation by Revenue and Profitability

Insights: 
The customer segmentation analysis shows that the highest-revenue customer was Sean Miller, generating $25,043.05 in total revenue across 5 orders. However, this customer recorded a negative profit of -$1,980.74, which shows that high revenue does not always translate into high customer value.

In contrast, Tamara Chand was the second-highest revenue customer, generating $19,052.22 from 5 orders, but also produced a strong profit of $8,981.32. This makes Tamara a more valuable customer from a profitability perspective compared to Sean Miller.

Most of the top 20 revenue customers placed fewer than 13 orders, which suggests their high revenue may come from larger or higher-priced purchases rather than frequent transactions.

Business Recommendation: 
the key insight is that customers should not be assessed by revenue alone. A more useful customer segmentation would compare both revenue and profit to separate genuinely profitable high-value customers from high-revenue but loss-making customers.
*/

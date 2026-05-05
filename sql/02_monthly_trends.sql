SELECT 
	YEAR(order_date_clean) as year,
	MONTH(order_date_clean) as month, 
	ROUND(SUM(Sales),2) as total_sale, 
	ROUND(SUM(Profit),2) as total_profit
FROM orders
GROUP BY YEAR(order_date_clean), MONTH(order_date_clean)
ORDER BY YEAR(order_date_clean), MONTH(order_date_clean); 

/*
Analysis: Monthly Sales and profit performance over time. 

Insight: 
The highest sales month was November 2017, generating $118,447.83 in total sales and $9,690.10 in profit. However, the most profitable month was December 2016, which generated $17,885.31 in profit from $96,999.04 in sales. This shows that higher sales do not always mean higher profit.

The weakest month was January 2015, which recorded a loss of -$3,281.01 despite generating $18,174.08 in sales. This should be investigated further, as the loss may be linked to discounting, returns, high costs, or low-margin products.

Business Recommendation:
Overall, the key insight is that November 2017 drove the most revenue, while December 2016 delivered the strongest profitability. The business should investigate what made December 2016 more profitable and why January 2015 produced a negative result.
 */

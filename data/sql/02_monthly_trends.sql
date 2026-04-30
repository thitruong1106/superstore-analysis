SELECT 
	YEAR(order_date_clean) as year,
	MONTH(order_date_clean) as month, 
	ROUND(SUM(Sales),2) as total_sale, 
	ROUND(SUM(Profit),2) as total_profit
FROM orders
GROUP BY YEAR(order_date_clean), MONTH(order_date_clean)
ORDER BY YEAR(order_date_clean), MONTH(order_date_clean); 

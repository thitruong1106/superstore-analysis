SELECT 
	YEAR(order_date_clean) as year,
	MONTH(order_date_clean) as month, 
	SUM(Sales) as total_sale
FROM orders
GROUP BY YEAR(order_date_clean), MONTH(order_date_clean)
ORDER BY YEAR(order_date_clean), MONTH(order_date_clean); 

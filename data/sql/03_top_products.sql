SELECT 
	`Product Name`, 
	SUM(Sales) as total_sale, 
	SUM(Quantity) as total_units, 
	ROUND(SUM(Profit),2) as total_profit,
	RANK() OVER (ORDER BY SUM(Sales)DESC) as sales_rank
FROM orders 
GROUP BY `Product Name` 
ORDER BY SUM(Sales) DESC
LIMIT 10; 

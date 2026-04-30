SELECT 
	Category, 
	ROUND(SUM(Sales),2) as total_sales,
	ROUND(SUM(Profit),2) as total_profit, 
	ROUND((SUM(Profit) / NULLIF(SUM(Sales),0)) * 100, 2) as profit_margin_pct, 
	RANK() OVER (ORDER BY SUM(Sales)DESC) as sales_rank
FROM orders 
GROUP BY  Category;

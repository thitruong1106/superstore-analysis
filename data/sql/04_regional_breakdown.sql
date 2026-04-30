SELECT
	Region, 
	ROUND(SUM(Sales),2) as total_sales, 
	ROUND(SUM(Profit),2) as total_profit,
	ROUND((SUM(Profit) / NULLIF(SUM(Sales), 0)) * 100, 2) AS profit_margin_pct
FROM orders 
GROUP BY Region 
ORDER BY SUM(Sales) DESC; 

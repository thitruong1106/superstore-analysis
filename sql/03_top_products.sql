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

/*
Analysis:
Rank products by total sales to identify the top 10 revenue-generating products.

Insight: 
In the Top 10 products by sales, the Canon imageCLASS 2200 Advanced Copier was the strongest-performing product, generating $61,599.82 in sales from only 20 units sold, while producing $25,199.93 in profit. This indicates that the product is a major driver in terms of both revenue and profitability.

However, not all high-sales products were profitable. Three products in the Top 10 recorded negative profit, showing that high revenue does not always translate into strong business performance. The Cisco TelePresence System EX90 Videoconferencing Unit generated $22,638.48 in sales but recorded a loss of -$1,811.08. Similarly, the GBC DocuBind P400 Electric Binding System generated $17,965.07 in sales but lost -$1,878.17, while the High Speed Automatic Electric Letter Opener generated $17,030.31 in sales but lost -$262.00.

The product with the highest unit volume was the GBC Ibimaster 500 Manual ProClick Binding System, with 48 units sold. However, it generated only $760.98 in profit, which suggests that strong sales volume does not necessarily lead to strong profitability. This product may have lower margins or may be affected by discounting or higher costs.

Business Recommendation: 
Overall, the key insight is that product performance should not be judged by sales alone. The business should prioritise products that generate both strong sales and strong profit, while reviewing high-sales products that are either low-margin or loss-making.
*/

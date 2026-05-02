SELECT 
    Category, 
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit, 
    ROUND((SUM(Profit) / NULLIF(SUM(Sales), 0)) * 100, 2) AS profit_margin_pct, 
    RANK() OVER (ORDER BY SUM(Sales) DESC) AS sales_rank
FROM orders 
GROUP BY Category
ORDER BY sales_rank;

/*
Question:
Which product categories perform best in terms of sales, profit, and profit margin?

Analysis:
Group products by category to compare total sales, total profit, and profit margin.

Insight:
The store has three main product categories: Technology, Furniture, and Office Supplies.

Technology is the strongest-performing category, generating the highest total sales at $836,154.03 and maintaining a strong profit margin of 17.40%.
This suggests that Technology is not only driving sales, but also contributing efficiently to profit.

Furniture ranks second in sales with $741,999.80, but its profit margin is much lower at 2.49%.
This indicates that while Furniture generates strong revenue, it may not be converting sales into profit efficiently.
Possible reasons could include higher costs, discounting, or weaker pricing power.

Office Supplies ranks third by sales at $719,047.03, but it also achieves a strong profit margin of 17.04%.
Although its revenue is slightly lower than Furniture, it appears to be a more profitable category overall.

Business recommendation:
Technology appears to be the best-performing category overall.
Furniture should be investigated further because it has strong sales but a weak profit margin.
*/

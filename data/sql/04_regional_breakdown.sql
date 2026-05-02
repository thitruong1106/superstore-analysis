SELECT
	Region, 
	ROUND(SUM(Sales),2) as total_sales, 
	ROUND(SUM(Profit),2) as total_profit,
	ROUND((SUM(Profit) / NULLIF(SUM(Sales), 0)) * 100, 2) AS profit_margin_pct
FROM orders 
GROUP BY Region 
ORDER BY SUM(Sales) DESC; 

/* 
Analysis: 
Comparing Region in terms of total sales, profit and profit margin. 

Insight: 
The West region is the strongest-performing region overall, generating the highest total sales of $725,457.82 and the highest total profit of $108,418.45. It also has the strongest profit margin at 14.94%, suggesting that the West is performing well in both revenue generation and profitability.

The East region ranks second, with $678,781.24 in sales and $91,522.78 in profit. Its profit margin of 13.48% is also strong, making it another healthy-performing region.

The Central region generated $501,239.89 in sales, which is higher than the South region’s $391,721.91. However, Central produced the lowest profit at $39,706.36 and the weakest profit margin at 7.92%. This suggests that Central may be facing margin pressure despite reasonable sales volume.

The South region had the lowest sales at $391,721.91, but its profit margin of 11.93% was stronger than Central’s. This shows that South is converting sales into profit more effectively than Central.

Business Recommendation: 
The key insight is that Central should be investigated further, because it has higher sales than South but weaker profitability. Possible causes could include heavy discounting, higher shipping costs, product mix, or lower-margin products.
*/

SELECT 
	Region,
	`Sub-Category`, 
	ROUND(SUM(Sales),2) as total_sales,
	ROUND(SUM(Profit),2) as total_profit, 
	ROUND((SUM(Profit) / NULLIF(SUM(Sales),0)) * 100, 2) as profit_margin_pct 
FROM orders 
WHERE Region = 'Central'
GROUP BY Region, `Sub-Category`
ORDER BY SUM(Profit) ASC;

/*
Analysis: Investigation on the central region based on ealier findings. 

Insight: 
Earlier, I found that the Central region had healthy sales of $501,239.89, but only generated $39,706.36 in profit, resulting in a weak profit margin of 7.92%. To investigate this further, I broke Central’s performance down by sub-category.

The analysis shows that 7 sub-categories recorded negative profit in the Central region: Furnishings, Tables, Appliances, Bookcases, Machines, Binders, and Supplies. This explains why Central’s overall profitability is weaker compared to other regions.

The weakest-performing sub-category was Furnishings, which generated $15,254.37 in sales but recorded a loss of -$3,906.22, resulting in a profit margin of -25.61%. This suggests that Furnishings may be affected by heavy discounting, high costs, or low-margin sales in the Central region.

Other major loss-making sub-categories include Tables with -$3,559.65 profit and Appliances with -$2,638.62 profit. These areas should be reviewed because they are reducing the overall profitability of the Central region.

Business Recommendation: 
Central’s weak profit margin appears to be driven by multiple loss-making sub-categories, especially Furnishings, Tables, and Appliances. A useful next step would be to investigate discount levels, shipping costs, and product-level performance within these sub-categories.
*/ 

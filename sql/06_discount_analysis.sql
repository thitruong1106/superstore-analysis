SELECT 
	MAX(Discount),
	MIN(Discount)
FROM Orders; 

SELECT 
	CASE
		WHEN Discount = 0 THEN 'No Discount'
		WHEN Discount <= 0.2 THEN '(LOW: 0-20% Discount)'
		WHEN Discount <= 0.4 THEN '(MED: 20-40% Discount)'
		ELSE 'High (+40% Discount)'
	END AS Discount_Type,
	COUNT(*) AS Num_of_order,
	ROUND(AVG(Profit),2) as average_profit,
	ROUND(SUM(Profit),2) as total_profit 
FROM orders
GROUP BY Discount_Type
ORDER BY average_profit;

/* 
Analysis: 
Discount analysis, does discount level relate to profitability. 

Insight: 
The discount analysis shows a clear relationship between discount level and profitability. Orders with no discount performed the best, with 4,798 transactions, an average profit of $66.90, and total profit of $320,987.60.

Low-discount orders between 0–20% were still profitable, generating an average profit of $26.50 and total profit of $100,785.47 across 3,803 transactions. However, profitability drops sharply once discounts move above 20%.

Medium discounts between 20–40% recorded an average loss of -$77.86 per order and total losses of -$35,817.47. High discounts above 40% performed the worst, with an average loss of -$106.71 per order and total losses of -$99,558.59.

Business Recommendation: 
The data suggests that discounting is a major driver of profit loss. Discounts below 20% can still remain profitable, but discounts above 20% appear to push orders into negative profitability. The business should review its discount strategy, especially for products or regions where medium and high discounts are frequently used.

*/

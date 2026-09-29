USE superstore;

-- Overall profit and margin
SELECT
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS Profit_Margin_Pct
FROM superstore;

-- Profit by Category
SELECT Category, ROUND(SUM(Profit), 2) AS Profit
FROM superstore
GROUP BY Category
ORDER BY Profit DESC;

-- Loss-making sub-categories (using HAVING)
SELECT `Sub-Category`, ROUND(SUM(Profit), 2) AS Profit
FROM superstore
GROUP BY `Sub-Category`
HAVING SUM(Profit) < 0
ORDER BY Profit ASC;
USE superstore;

-- Profit by Region
SELECT Region, ROUND(SUM(Sales), 2) AS Sales, ROUND(SUM(Profit), 2) AS Profit
FROM superstore
GROUP BY Region
ORDER BY Profit DESC;

-- Top 10 states by sales
SELECT State, ROUND(SUM(Sales), 2) AS Sales, ROUND(SUM(Profit), 2) AS Profit
FROM superstore
GROUP BY State
ORDER BY Sales DESC
LIMIT 10;
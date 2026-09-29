USE superstore;

-- Discount bucket summary
SELECT
    `Discount Bucket`,
    ROUND(SUM(Sales), 2) AS Sales,
    ROUND(SUM(Profit), 2) AS Profit,
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS Profit_Margin_Pct
FROM superstore
GROUP BY `Discount Bucket`;

-- Discount by Sub-Category
SELECT
    `Sub-Category`,
    ROUND(AVG(Discount) * 100, 2) AS Avg_Discount_Pct,
    ROUND(SUM(Profit), 2) AS Profit
FROM superstore
GROUP BY `Sub-Category`
ORDER BY Avg_Discount_Pct DESC;
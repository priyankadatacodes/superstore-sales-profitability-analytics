USE superstore;

SELECT
    Segment,
    ROUND(SUM(Sales), 2) AS Sales,
    ROUND(SUM(Profit), 2) AS Profit,
    ROUND(AVG(Discount) * 100, 2) AS Avg_Discount_Pct
FROM superstore
GROUP BY Segment
ORDER BY Profit DESC;
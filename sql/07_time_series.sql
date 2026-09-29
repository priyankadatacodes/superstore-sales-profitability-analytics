USE superstore;

-- Monthly sales and profit
SELECT
    `Order Year-Month`,
    ROUND(SUM(Sales), 2) AS Sales,
    ROUND(SUM(Profit), 2) AS Profit
FROM superstore
GROUP BY `Order Year-Month`
ORDER BY `Order Year-Month`;

-- Year-over-year growth using a window function (LAG)
WITH yearly AS (
    SELECT `Order Year`, SUM(Sales) AS Sales, SUM(Profit) AS Profit
    FROM superstore
    GROUP BY `Order Year`
)
SELECT
    `Order Year`,
    ROUND(Sales, 2) AS Sales,
    ROUND((Sales - LAG(Sales) OVER (ORDER BY `Order Year`)) / LAG(Sales) OVER (ORDER BY `Order Year`) * 100, 2) AS Sales_YoY_Pct,
    ROUND((Profit - LAG(Profit) OVER (ORDER BY `Order Year`)) / LAG(Profit) OVER (ORDER BY `Order Year`) * 100, 2) AS Profit_YoY_Pct
FROM yearly
ORDER BY `Order Year`;
USE superstore;

-- Overall KPIs
SELECT
    ROUND(SUM(Sales), 2) AS Total_Sales,
    COUNT(DISTINCT `Order ID`) AS Total_Orders
FROM superstore;

-- Sales by Category
SELECT Category, ROUND(SUM(Sales), 2) AS Total_Sales
FROM superstore
GROUP BY Category
ORDER BY Total_Sales DESC;

-- Sales by Sub-Category
SELECT `Sub-Category`, ROUND(SUM(Sales), 2) AS Total_Sales
FROM superstore
GROUP BY `Sub-Category`
ORDER BY Total_Sales DESC;
USE superstore;

-- Segment summary
SELECT
    Segment,
    COUNT(`Customer ID`) AS Customer_Count,
    ROUND(SUM(Monetary), 2) AS Total_Monetary
FROM customer_rfm
GROUP BY Segment
ORDER BY Total_Monetary DESC;

-- Join RFM back to transactions 
SELECT
    r.Segment,
    s.Category,
    ROUND(SUM(s.Sales), 2) AS Sales
FROM superstore s
JOIN customer_rfm r ON s.`Customer ID` = r.`Customer ID`
GROUP BY r.Segment, s.Category
ORDER BY r.Segment, Sales DESC;
USE superstore;

CREATE OR REPLACE VIEW vw_sales_performance AS
SELECT Category, `Sub-Category`, Region, Segment, `Order Year`,
       SUM(Sales) AS Total_Sales, COUNT(DISTINCT `Order ID`) AS Total_Orders
FROM superstore
GROUP BY Category, `Sub-Category`, Region, Segment, `Order Year`;

CREATE OR REPLACE VIEW vw_product_profitability AS
SELECT Category, `Sub-Category`,
       ROUND(SUM(Sales), 2) AS Sales, ROUND(SUM(Profit), 2) AS Profit
FROM superstore
GROUP BY Category, `Sub-Category`;

CREATE OR REPLACE VIEW vw_discount_analysis AS
SELECT `Discount Bucket`, Category,
       ROUND(SUM(Sales), 2) AS Sales, ROUND(SUM(Profit), 2) AS Profit
FROM superstore
GROUP BY `Discount Bucket`, Category;

CREATE OR REPLACE VIEW vw_geographic_profitability AS
SELECT Region, State, City,
       ROUND(SUM(Sales), 2) AS Sales, ROUND(SUM(Profit), 2) AS Profit
FROM superstore
GROUP BY Region, State, City;

CREATE OR REPLACE VIEW vw_monthly_performance AS
SELECT `Order Year-Month`,
       ROUND(SUM(Sales), 2) AS Sales, ROUND(SUM(Profit), 2) AS Profit
FROM superstore
GROUP BY `Order Year-Month`;

CREATE OR REPLACE VIEW vw_customer_rfm AS
SELECT `Customer ID`, Recency, Frequency, Monetary, Segment
FROM customer_rfm;

-- Confirm views were created
SHOW FULL TABLES WHERE Table_type = 'VIEW';
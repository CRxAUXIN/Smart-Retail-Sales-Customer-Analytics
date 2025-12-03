
-- Top Selling Products
SELECT product_id, SUM(quantity) AS total_sold
FROM sales
GROUP BY product_id
ORDER BY total_sold DESC
LIMIT 10;

-- Overstock Items
SELECT product_id, store, current_stock - reorder_level AS overstock
FROM inventory
WHERE current_stock > reorder_level;

-- Region-wise Revenue
SELECT c.region, SUM(s.quantity * s.price) AS revenue
FROM sales s
JOIN customers c ON s.customer_id = c.customer_id
GROUP BY c.region;

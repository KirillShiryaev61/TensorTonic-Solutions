-- Write your SQL query here
SELECT name, 
       price,
       price - (SELECT AVG(price) FROM products) AS vs_avg
FROM products
WHERE id IN (SELECT DISTINCT product_id FROM sales)
ORDER BY vs_avg DESC, 
         name ASC
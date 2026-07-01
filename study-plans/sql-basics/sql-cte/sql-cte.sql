-- Write your SQL query here
WITH main_table AS (

SELECT customer, 
       COUNT(id) AS order_count, 
       SUM(amount) AS total_spent
FROM orders
GROUP BY customer
)

SELECT *
FROM main_table
WHERE order_count > 1
ORDER BY total_spent DESC,
         customer ASC
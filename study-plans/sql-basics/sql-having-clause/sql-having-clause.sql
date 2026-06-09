-- Write your SQL query here
SELECT customer,
       COUNT(id) AS total_orders,
       SUM(amount) AS total_spent
FROM orders
GROUP BY customer
HAVING COUNT(id) >= 2
ORDER BY total_spent DESC
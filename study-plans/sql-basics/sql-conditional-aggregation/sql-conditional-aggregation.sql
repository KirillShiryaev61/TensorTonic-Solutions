-- Write your SQL query here
SELECT department,
       COUNT(status) AS total_tickets,
       COUNT(CASE WHEN status = 'open' THEN 1 END) AS open_count,
       COUNT(CASE WHEN status = 'in_progress' THEN 1 END) AS in_progress_count,
       COUNT(CASE WHEN status = 'closed' THEN 1 END) AS closed_count
FROM tickets
GROUP BY department
ORDER BY total_tickets DESC,
         department ASC
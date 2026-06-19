-- Write your SQL query here
SELECT 
    name, 
    COALESCE(email, 'N/A') AS display_email,
    CASE 
        WHEN deactivated_at IS NOT NULL 
        THEN 'inactive'
        ELSE 'active' 
    END AS status
FROM customers
WHERE phone IS NOT NULL
ORDER BY name ASC
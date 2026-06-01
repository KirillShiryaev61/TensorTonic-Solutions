-- Write your SQL query here
SELECT u1.username, 
       COALESCE(u2.username, 'organic') AS referrer_name
FROM user_referrals u1
LEFT JOIN user_referrals u2 ON u1.referred_by = u2.id
ORDER BY u1.username ASC
       
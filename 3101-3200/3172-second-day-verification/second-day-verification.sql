# Write your MySQL query statement below
SELECT user_id 
FROM texts AS A
JOIN emails AS B 
USING(email_id)
WHERE DATE(action_date) = DATE(signup_date + INTERVAL 1 DAY)
AND signup_action = 'Verified'
ORDER BY user_id;
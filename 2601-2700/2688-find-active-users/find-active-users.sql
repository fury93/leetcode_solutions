# Write your MySQL query statement below
SELECT DISTINCT user_id 
FROM (
    SELECT
        user_id, 
        created_at - LAG(created_at, 1) OVER (
            PARTITION BY user_id ORDER BY created_at
        ) AS diff
    FROM Users
) a 
WHERE diff <= 7
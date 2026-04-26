# Write your MySQL query statement below
SELECT u.user_id, 
       u.name,
       IFNULL(SUM(distance), 0) AS 'traveled distance'
FROM Users AS u
LEFT JOIN Rides AS r
ON u.user_id = r.user_id
GROUP BY user_id, name
ORDER BY user_id 
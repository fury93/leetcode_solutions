# Write your MySQL query statement below
# Approach 1: NOT IN/EXISTS​
-- WITH user_by_activity AS
--     (
--     SELECT activity, COUNT(DISTINCT id) AS user_cnts
--     FROM Friends
--     GROUP BY activity
--     )
-- SELECT activity
-- FROM user_by_activity
-- WHERE user_cnts NOT IN (SELECT MAX(user_cnts) FROM user_by_activity)
-- AND user_cnts NOT IN (SELECT MIN(user_cnts) FROM user_by_activity)

# Approach 2: Using RANK() to Identify the Maximum and Minimum
-- SELECT activity 
-- FROM 
--     (
--     SELECT activity, 
--         RANK () OVER (ORDER BY(COUNT(id))) AS rank_asc,
--         RANK () OVER (ORDER BY(COUNT(id))DESC) AS rank_desc
--     FROM Friends
--     GROUP BY activity
--     )t0
-- WHERE rank_asc != 1 AND rank_desc != 1

# Approach 3: Remove the Matching Records Using LEFT JOIN
WITH user_by_activity AS 
    (
    SELECT activity, COUNT(DISTINCT id) AS user_cnts
    FROM Friends
    GROUP BY activity
    )
SELECT activity
FROM user_by_activity u
LEFT JOIN 
    (SELECT MAX(user_cnts) AS user_cnts 
    FROM user_by_activity
    UNION
    SELECT MIN(user_cnts) AS user_cnts 
    FROM user_by_activity
    )m
ON u.user_cnts = m.user_cnts
WHERE m.user_cnts IS NULL

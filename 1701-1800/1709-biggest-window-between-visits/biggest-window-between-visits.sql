# Write your MySQL query statement below

# Approach 1: Find Next Using LEAD() + Append Value Using IFNULL()
SELECT user_id, MAX(w) AS biggest_window
  FROM(
SELECT 
    user_id, 
    visit_date,
    DATEDIFF(IFNULL(LEAD(visit_date, 1) OVER(PARTITION BY user_id ORDER BY visit_date), '2021-01-01'), visit_date) AS w
FROM UserVisits) AS a
GROUP BY user_id

# Approach 2: Find the Next Visit Using RANK()
-- WITH all_dates AS(
--     SELECT user_id, visit_date
--     FROM UserVisits
--     UNION
--     SELECT user_id, '2021-01-01' AS 'visit_date'
--     FROM UserVisits)
-- , rnk AS(
--     SELECT *, 
--         RANK()OVER(PARTITION BY user_id ORDER BY visit_date) AS date_rnk
--     FROM all_dates
-- )
-- SELECT a.user_id, MAX(DATEDIFF(b.visit_date, a.visit_date)) AS biggest_window
-- FROM rnk a, rnk b
-- WHERE a.user_id = b.user_id
-- AND b.date_rnk = a.date_rnk + 1
-- GROUP BY a.user_id
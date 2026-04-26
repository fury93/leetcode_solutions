# Write your MySQL query statement below
WITH CTE AS (
    SELECT *,
        MAX(height) OVER(ORDER BY id ASC) AS left_highest_bar,
        MAX(height) OVER(ORDER BY id DESC) AS right_highest_bar
    FROM Heights
)
SELECT SUM(LEAST(left_highest_bar, right_highest_bar) - height) AS total_trapped_water -- MIN() get smallest in a column, LEAST() get smallest among X values put in the function
FROM CTE
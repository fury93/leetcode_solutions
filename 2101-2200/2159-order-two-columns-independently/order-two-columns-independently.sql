# Write your MySQL query statement below
SELECT first_col, second_col
FROM (
    SELECT 
    first_col,
    ROW_NUMBER() OVER(ORDER BY first_col ASC) AS r
    FROM Data
) a
JOIN (
    SELECT 
    second_col,
    ROW_NUMBER() OVER(ORDER BY second_col DESC) AS r
    FROM Data
) b
ON a.r = b.r
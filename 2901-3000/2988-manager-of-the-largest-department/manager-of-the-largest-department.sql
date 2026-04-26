# Write your MySQL query statement below
WITH t AS (
SELECT dep_id, RANK() OVER(ORDER BY COUNT(emp_id) DESC) AS rnk
FROM Employees
GROUP BY dep_id)

SELECT emp_name AS manager_name, dep_id
FROM Employees
WHERE position = "Manager" AND dep_id IN (SELECT dep_id
FROM t
WHERE rnk = 1)
ORDER BY dep_id
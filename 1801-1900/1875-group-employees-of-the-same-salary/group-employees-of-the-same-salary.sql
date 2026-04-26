# Write your MySQL query statement below
SELECT *,
    DENSE_RANK() OVER(ORDER BY salary) team_id
FROM Employees
WHERE salary NOT IN(
			SELECT salary
			FROM Employees
			GROUP BY salary
			HAVING COUNT(*) = 1)
ORDER BY team_id, employee_id
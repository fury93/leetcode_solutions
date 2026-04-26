# Write your MySQL query statement below
WITH RECURSIVE t AS (
    SELECT employee_id, employee_name, 0 AS hierarchy_level, salary
    FROM Employees
    WHERE manager_id IS NULL
    UNION ALL
    SELECT e.employee_id, e.employee_name, hierarchy_level + 1, e.salary - (SELECT salary FROM Employees WHERE manager_id IS NULL)
    FROM Employees e
    JOIN t
    ON t.employee_id = e.manager_id
)

SELECT employee_id AS subordinate_id, employee_name AS subordinate_name, hierarchy_level, salary AS salary_difference
FROM t
WHERE hierarchy_level > 0
ORDER BY 3, 1
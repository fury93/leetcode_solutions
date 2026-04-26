# Write your MySQL query statement below
SELECT project_id, employee_id
FROM (
    SELECT p.project_id, 
           p.employee_id, 
           RANK()OVER(PARTITION BY project_id ORDER BY experience_years DESC) AS rnk
    FROM Project p
    JOIN Employee e
    ON p.employee_id = e.employee_id
)a
WHERE rnk = 1
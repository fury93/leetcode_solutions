# Write your MySQL query statement below
WITH salary_ranker AS (
    SELECT
        *,
        SUM(salary) OVER(
            PARTITION BY experience ORDER BY salary
        ) AS running_sum
    FROM candidates
)
, seniors AS(
    SELECT 
        employee_id, 
        running_sum 
    FROM salary_ranker 
    where experience="senior" and running_sum <= 70000
)
, juniors AS(
    SELECT 
        employee_id, 
        running_sum
    FROM salary_ranker 
    WHERE running_sum <= 70000 - (
        SELECT IFNULL(MAX(running_sum), 0)
        FROM seniors
    )
)
SELECT employee_id FROM seniors
UNION
SELECT employee_id FROM juniors
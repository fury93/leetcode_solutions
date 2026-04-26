# Write your MySQL query statement below
select max(salary) as SecondHighestSalary
from employee
where salary not in (select max(salary) from employee)

-- SELECT
--     IFNULL(
--       (SELECT DISTINCT Salary
--        FROM Employee
--        ORDER BY Salary DESC
--         LIMIT 1 OFFSET 1),
--     NULL) AS SecondHighestSalary

-- SELECT max(Salary) AS SecondHighestSalary
-- FROM Employee
-- WHERE Salary < (SELECT max(Salary) FROM Employee)

-- SELECT Salary AS NthHighest
-- FROM Employee
-- ORDER BY Salary DESC
-- LIMIT N-1,1

-- to retrieve Nth highest
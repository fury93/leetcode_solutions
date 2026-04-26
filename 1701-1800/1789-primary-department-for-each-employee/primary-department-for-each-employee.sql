# Write your MySQL query statement below
# Approach 1: UNION
-- Retrieving employees with primary_flag set to 'Y'
-- SELECT 
--   employee_id, 
--   department_id 
-- FROM 
--   Employee 
-- WHERE 
--   primary_flag = 'Y' 
-- UNION 
-- -- Retrieving employees that appear exactly once in the Employee table
-- SELECT 
--   employee_id, 
--   department_id 
-- FROM 
--   Employee 
-- GROUP BY 
--   employee_id 
-- HAVING 
--   COUNT(employee_id) = 1;


# Approach 2: Window Function (COUNT)
SELECT 
  employee_id, 
  department_id 
FROM 
  (
    SELECT 
      *, 
      COUNT(employee_id) OVER(PARTITION BY employee_id) AS EmployeeCount
    FROM 
      Employee
  ) EmployeePartition 
WHERE 
  EmployeeCount = 1 
  OR primary_flag = 'Y';

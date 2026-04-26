# Write your MySQL query statement below
SELECT 
  employee_id 
FROM 
  Employees 
WHERE 
  employee_id NOT IN (
    SELECT 
      employee_id 
    FROM 
      Salaries
  ) 
UNION 
SELECT 
  employee_id 
FROM 
  Salaries 
WHERE 
  employee_id NOT IN (
    SELECT 
      employee_id 
    FROM 
      Employees
  ) 
ORDER BY 
  employee_id ASC
  
-- select e.employee_id
-- from (
--     select * from employees left join salaries using(employee_id)
--     union
--     select * from employees right join salaries using(employee_id)
--     ) as e
-- where e.name IS NULL or e.salary IS NULL
-- order by e.employee_id
# Write your MySQL query statement below
select 
    e.employee_id, 
    e.name, 
    count(*) as reports_count, 
    ROUND(AVG(r.age)) as average_age
from employees e join Employees r on e.employee_id = r.reports_to
group by employee_id
order by employee_id

# Write your MySQL query statement below
with cte as(
select 
employee_id,
project_id,
name,
workload,
avg(workload) over(partition by team) as total_avg
from project left join employees 
using(employee_id)
)
select 
employee_id as EMPLOYEE_ID,
project_id AS PROJECT_ID,
name AS EMPLOYEE_NAME,
workload AS PROJECT_WORKLOAD
from cte 
where total_avg < workload
order by 1, 2
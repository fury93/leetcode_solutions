# Write your MySQL query statement below

#Approach 1 using if statement
#select employee_id,
#if(employee_id%2 and name not like 'M%', salary, 0) as bonus
#from employees
#order by employee_id

#Approach 2 using case statement
#select employee_id,
#case
#  when employee_id%2 and name not like 'M%' then salary
#  else 0
#end as bonus
#from employees
#order by employee_id

#Approach 3 tricky
select employee_id,
salary * (employee_id%2) * (name not like 'M%') as bonus
from employees
order by employee_id
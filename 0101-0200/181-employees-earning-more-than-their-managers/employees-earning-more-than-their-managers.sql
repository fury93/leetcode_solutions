# Write your MySQL query statement below
#Approach 1 using join
#select name as `Employee` 
#from Employee e1
#where salary > (select salary from Employee e2 where e2.id = e1.managerid)

select e1.name as `Employee` 
from Employee e1, Employee e2
where e2.id = e1.managerid and e1.salary > e2.salary
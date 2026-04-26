# Write your MySQL query statement below
select distinct email 
from person
group by email
having count(email) > 1
# Write your MySQL query statement below
select 
    a.driver_id, 
    ifnull(count(distinct b.ride_id), 0) as cnt
from Rides a 
left join Rides b 
on a.driver_id = b.passenger_id
group by a.driver_id
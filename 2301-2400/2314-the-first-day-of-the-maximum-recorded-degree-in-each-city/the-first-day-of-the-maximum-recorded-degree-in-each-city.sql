# Write your MySQL query statement below
select city_id, day, degree from(
select *, rank() over 
    (partition by city_id
     order by degree desc, day asc) as r
from Weather) tmp
where r = 1
;
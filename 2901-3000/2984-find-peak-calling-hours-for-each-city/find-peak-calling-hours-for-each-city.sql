# Write your MySQL query statement below
with t as 
(select city,hour(call_time) as hr, count(*) as cnt
from calls
group by city,hour(call_time)
)
, t1 as (select *, dense_rank()
over (partition by city order by cnt desc) rnk from t)
select city, hr as peak_calling_hour, cnt as number_of_calls
from t1
where rnk=1
order by peak_calling_hour desc, city desc
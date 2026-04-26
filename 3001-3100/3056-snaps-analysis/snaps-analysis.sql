# Write your MySQL query statement below
with cte as (
    select age_bucket, 
    round(sum(case when activity_type = 'send' then time_spent else 0 end)*100/sum(time_spent),2) as send_perc,
    round(sum(case when activity_type = 'open' then time_spent else 0 end)*100/sum(time_spent),2) as open_perc
    from age u
    left join activities a on u.user_id = a.user_id
    group by 1
)
select*
from cte
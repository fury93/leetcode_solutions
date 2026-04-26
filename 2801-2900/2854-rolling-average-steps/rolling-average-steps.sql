# Write your MySQL query statement below
select user_id, steps_date, rolling_average
from (
    select user_id, steps_date,
    round(avg(steps_count) over (partition by user_id order by steps_date rows between 2 preceding and current row), 2) as rolling_average,
    lag(steps_date, 2) over (partition by user_id order by steps_date) as two_dates_before
    from steps
) tmp
where datediff(steps_date, two_dates_before) = 2
order by 1, 2
;
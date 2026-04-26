# Write your MySQL query statement below
-- SELECT ifnull(ROUND(COUNT(DISTINCT session_id)/COUNT(DISTINCT user_id), 2),0.00) 
-- AS average_sessions_per_user
-- FROM Activity 
-- WHERE activity_date >= '2019-06-28' and activity_date <= '2019-07-27';  

select ifnull(round(avg(cnt),2),0) as average_sessions_per_user
from( 
    select user_id, count(distinct session_id) as cnt 
    from activity 
    where activity_date between date_sub('2019-07-27', interval 29 day) and '2019-07-27'
    group by user_id) count_session
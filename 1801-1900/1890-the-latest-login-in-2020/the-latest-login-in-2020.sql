# Write your MySQL query statement below
select user_id, MAX(time_stamp) as last_stamp
from logins
where YEAR(time_stamp) = 2020
group by user_id

-- SELECT
--     DISTINCT user_id,
--     FIRST_VALUE(time_stamp)OVER(PARTITION BY user_id ORDER BY time_stamp DESC) AS last_stamp
-- FROM
--     Logins
-- WHERE EXTRACT(Year FROM time_stamp) = 2020;
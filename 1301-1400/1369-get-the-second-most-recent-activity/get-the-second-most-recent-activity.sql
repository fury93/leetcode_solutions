# Write your MySQL query statement below
select username, activity, startDate, endDate from (
select
    username,
    activity,
    startDate,
    endDate,
    row_number() over (partition by username order by startDate desc) as ranks,
    count(username) over (partition by username) as counts
from UserActivity) as t
where counts = 1 or ranks = 2;
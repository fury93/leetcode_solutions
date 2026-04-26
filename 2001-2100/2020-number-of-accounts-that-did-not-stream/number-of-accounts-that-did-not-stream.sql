# Write your MySQL query statement below
select count(t.account_id) accounts_count
from subscriptions s
left join streams t
on s.account_id = t.account_id 
and year(t.stream_date) <> 2021 
and year(s.end_date) = 2021
where t.account_id is not null
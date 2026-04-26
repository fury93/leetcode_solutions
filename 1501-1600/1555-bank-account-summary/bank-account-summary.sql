# Write your MySQL query statement below
SELECT user_id,user_name,
IFNULL(SUM(CASE WHEN a.user_id=b.paid_by THEN -amount ELSE amount END),0)+a.credit as credit,
CASE WHEN IFNULL(SUM(CASE WHEN a.user_id=b.paid_by THEN -amount ELSE amount END),0)>=-a.credit THEN "No" ELSE "Yes" END as credit_limit_breached
FROM Users as a
LEFT JOIN Transactions as b
ON a.user_id=b.paid_by OR a.user_id=b.paid_to
GROUP BY a.user_id;

-- with CTE as 
-- (Select user_id, credit from Users
-- union ALL
-- Select paid_by as user_id, -1*amount as credit from Transactions
-- union all
-- Select paid_to as user_id, amount as credit from Transactions)

-- Select a.user_id, b.user_name, sum(a.credit) as credit,
-- case when sum(a.credit) >= 0 then "No"
-- else "Yes"
-- end as credit_limit_breached from CTE a join Users b using(user_id)
-- group by user_id
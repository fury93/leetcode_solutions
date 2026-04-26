# Write your MySQL query statement below
SELECT 
    account_id, 
    day, 
    sum(
        case when type = 'Deposit' 
        then amount 
        else -amount end
    ) over(
        partition by account_id 
        order by day asc
    ) as balance 
FROM transactions
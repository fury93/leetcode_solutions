# Write your MySQL query statement below
with recursive all_id as
(
    select 
        1 as ids
    union all
    select 
        ids+1 
    from all_id 
        where ids<(select max(customer_id) from Customers)
)
select 
ids
from all_id
where ids not in (select customer_id  from Customers)
order by 1

-- WITH RECURSIVE id_seq AS (
--     SELECT 1 as continued_id
--     UNION 
--     SELECT continued_id + 1
--     FROM id_seq
--     WHERE continued_id < (
--         SELECT MAX(customer_id) 
--         FROM Customers
--     ) 
-- )

-- SELECT continued_id AS ids
-- FROM id_seq
-- WHERE continued_id NOT IN (SELECT customer_id FROM Customers)  

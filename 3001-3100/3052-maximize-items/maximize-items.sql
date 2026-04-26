# Write your MySQL query statement below

with a as (
    select 
    item_type,
    sum(square_footage) as total_footage,
    count(item_id) as item_cnt
    from inventory
    group by 1
)

select 
item_type,
item_cnt*floor(500000/total_footage) as item_count
from a 
where item_type = 'prime_eligible'
union all
select 
item_type,
item_cnt*floor((500000%(select total_footage from a where item_type = 'prime_eligible'))/total_footage) as item_count
from a 
where item_type = 'not_prime'
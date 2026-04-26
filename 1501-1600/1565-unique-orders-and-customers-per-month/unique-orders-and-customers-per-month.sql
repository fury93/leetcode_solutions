# Write your MySQL query statement below
select 
 SUBSTRING(order_date, 1, 7) as month,
 count(distinct order_id) as order_count,
 count(distinct customer_id) as customer_count
from
Orders
where invoice > 20
group by
SUBSTRING(order_date, 1, 7)

-- select left(order_date, 7) month, count(distinct order_id) order_count, count(distinct customer_id) customer_count
-- from orders
-- where invoice > 20
-- group by 1;
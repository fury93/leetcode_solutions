# Write your MySQL query statement below
-- purchase of each customer by year
with yearly as
(select customer_id, year(max(order_date)) year, sum(price) price
from orders
group by year(order_date),customer_id)
-- "left" join each year with its +1 year, and has strictly bigger purchase on +1 year.
select y1.customer_id
from yearly y1
left join yearly y2 on y1.customer_id=y2.customer_id and y1.year+1=y2.year and y1.price<y2.price
group by y1.customer_id
having count(*)-count(y2.customer_id)=1
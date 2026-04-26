# Write your MySQL query statement below
select product_name, sum(unit) unit
from products p
left join orders o using(product_id)
where YEAR(order_date) = 2020 AND MONTH(order_date) = 2
group by product_name
having unit >=100
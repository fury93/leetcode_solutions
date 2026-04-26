# Write your MySQL query statement below
SELECT
    customer_number
FROM
    orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1
;

-- select customer_number
-- from `orders`
-- group by customer_number
-- having count(*) = (
--     select max(cnt) from(
--         select count(*) cnt
--         from `orders`
--         group by customer_number
--     ) as q
-- )
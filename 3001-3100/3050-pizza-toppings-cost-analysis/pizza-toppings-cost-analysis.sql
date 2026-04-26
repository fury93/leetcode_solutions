# Write your MySQL query statement below
-- select 
--     concat(
--         t1.topping_name, ',' ,
--         t2.topping_name, ',' ,
--         t3.topping_name
--     )
--     as pizza, 
--     t1.cost + t2.cost + t3.cost as total_cost 
-- from toppings t1 inner join toppings t2 
-- on t1.topping_name < t2.topping_name 
-- inner join toppings t3
-- on t2.topping_name < t3.topping_name
-- order by total_cost desc, pizza

WITH TEMP AS (
    SELECT TOPPING_NAME, COST, 
        ROW_NUMBER() OVER (ORDER BY TOPPING_NAME) AS RANK1
    FROM TOPPINGS
    ORDER BY TOPPING_NAME)

SELECT 
    CONCAT(A.TOPPING_NAME, ',', B.TOPPING_NAME, ',', C.TOPPING_NAME) AS 'PIZZA', 
    ROUND((A.COST + B.COST + C.COST), 2) AS 'TOTAL_COST'
FROM TEMP AS A
JOIN TEMP AS B ON A.RANK1 < B.RANK1
JOIN TEMP AS C ON B.RANK1 < C.RANK1
ORDER BY TOTAL_COST DESC, PIZZA
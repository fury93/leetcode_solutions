# Write your MySQL query statement below

SELECT DISTINCT d.product_id FROM
(SELECT product_id, 
 YEAR(purchase_date) AS curr_year,
 LEAD(YEAR(purchase_date)) 
 OVER(
    PARTITION BY product_id 
    ORDER BY YEAR(purchase_date)
) AS next_year
 FROM orders
 GROUP BY curr_year, product_id
 HAVING COUNT(order_id) >= 3) d
 WHERE d.next_year=d.curr_year+1

--  WITH cte as(SELECT product_id, 
--  year(purchase_date) AS purchase_year
--  FROM orders
--  GROUP BY purchase_year, product_id
--  HAVING COUNT(order_id) >= 3)
 
-- SELECT DISTINCT c1.product_id FROM
-- cte c1 JOIN cte c2
-- ON c1.product_id=c2.product_id AND c1.purchase_year=c2.purchase_year+1
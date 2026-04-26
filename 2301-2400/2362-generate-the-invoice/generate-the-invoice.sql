# Write your MySQL query statement below
with temp as (
    select invoice_id, SUM(quantity*price) as 'price2'
    FROM Purchases a 
    left join Products 
    ON a.product_id=Products.product_id
    GROUP BY 1 
    ORDER BY 2 DESC, 1 ASC
    limit 1
)

SELECT a.product_id, quantity, quantity*b.price as 'price'
FROM Purchases a 
LEFT JOIN Products b 
ON a.product_id=b.product_id
WHERE invoice_id = (select invoice_id from temp)

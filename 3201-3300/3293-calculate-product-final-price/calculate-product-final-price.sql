# Write your MySQL query statement below

SELECT 
    product_id,
    IFNULL(price * (1-discount/100), price) AS final_price,
    p.category
FROM Products p 
LEFT JOIN Discounts d 
ON p.category = d.category
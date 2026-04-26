# Write your MySQL query statement below

SELECT 
    DISTINCT p.product_name,
    p.product_id,
    o.order_id,
    o.order_date
FROM 
    Products p 
JOIN 
    Orders o
ON 
    p.product_id = o.product_id
JOIN
    (
    SELECT 
        DISTINCT product_id, 
        MAX(order_date) AS order_date
    FROM 
        Orders
    GROUP BY 1
    )a
ON 
    o.product_id = a.product_id
AND 
    o.order_date = a.order_date
ORDER BY p.product_name,
    p.product_id,
    o.order_id

# Approach 2: Using RANK() to Find the Most Recent Order
-- SELECT 
--     DISTINCT p.product_name,
--     p.product_id,
--     o.order_id,
--     o.order_date
-- FROM 
--     Products p
-- JOIN 
--     (
--     SELECT 
--         order_id, 
--         order_date, 
--         product_id,
--         RANK() OVER (PARTITION BY product_id ORDER BY order_date DESC) AS rnk
--     FROM Orders
-- )o
-- ON 
--     p.product_id = o.product_id
-- AND 
--     rnk = 1
-- ORDER BY p.product_name,
--     p.product_id,
--     o.order_id

# Write your MySQL query statement below
-- SELECT 
--     user_id, 
--     product_id
-- FROM (SELECT 
--         user_id, 
--         product_id, 
--         RANK() OVER (
--             PARTITION BY user_id 
--             ORDER BY SUM(price * quantity) DESC
--         ) AS rnk 
--       FROM Sales JOIN Product USING (product_id) 
--       GROUP BY 1, 2) a 
-- WHERE rnk = 1

-- Step 1: Calculate the total count of each product per user
WITH user_product_count AS (
  
  SELECT user_id, product_id, SUM(quantity) as total_quantity
  FROM Sales
  GROUP BY user_id, product_id
),

-- Step 2: Rank the user purchases based on total amount spent on each product
user_spent AS (
  
  SELECT user_id, product_id,
    RANK() OVER (PARTITION BY user_id ORDER BY total_quantity * price DESC) as rk
  FROM user_product_count s INNER JOIN Product p USING(product_id)
)

-- Step 3: Filter the Products user spend the most money
SELECT user_id, product_id
FROM user_spent
WHERE rk = 1
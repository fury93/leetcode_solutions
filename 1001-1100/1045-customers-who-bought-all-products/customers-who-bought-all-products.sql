# Write your MySQL query statement below
# Approach 1: Count how many products each customer bought
SELECT
  customer_id
FROM
  Customer
GROUP BY
  customer_id
HAVING
  COUNT(DISTINCT product_key) = (
    SELECT
      COUNT(product_key)
    FROM
      Product
  );

# Approach 2: Use nested subquery with Cartesian Product - Alternative
-- SELECT DISTINCT
--   customer_id
-- FROM
--   Customer
-- WHERE
--   customer_id NOT IN (
--     SELECT
--       customer_id
--     FROM
--       (
--         SELECT DISTINCT
--           Customer.customer_id,
--           Product.product_key
--         FROM
--           Customer,
--           Product
--       ) AS AllPossibleCases
--     WHERE
--       (customer_id, product_key) NOT IN (
--         SELECT
--           customer_id,
--           product_key
--         FROM
--           Customer
--       )
--   );
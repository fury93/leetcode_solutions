# Write your MySQL query statement below
 SELECT v.customer_id, COUNT(DISTINCT v.visit_id) as count_no_trans 
 FROM Visits v LEFT JOIN Transactions t ON v.visit_id = t.visit_id
 WHERE t.transaction_id IS NULL
 GROUP BY v.customer_id ;
 
# Approach 1: Removing Records Using NOT IN/EXISTS
-- SELECT 
--   customer_id, 
--   COUNT(visit_id) AS count_no_trans 
-- FROM 
--   Visits 
-- WHERE 
--   visit_id NOT IN (
--     SELECT 
--       visit_id 
--     FROM 
--       Transactions
--   ) 
-- GROUP BY 
--   customer_id

# Approach 2: Removing Records Using LEFT JOIN and IS NULL
-- SELECT 
--   customer_id, 
--   COUNT(*) AS count_no_trans 
-- FROM 
--   Visits AS v 
--   LEFT JOIN Transactions AS t ON v.visit_id = t.visit_id 
-- WHERE 
--   t.visit_id IS NULL 
-- GROUP BY 
--   customer_id


# Write your MySQL query statement below
# Approach 1: Aliases or SELF JOIN
SELECT 
    a.sale_date, a.sold_num-b.sold_num AS diff
FROM
    Sales a, Sales b
WHERE 
    a.fruit IN ('apples') AND b.fruit IN ('oranges')
    AND a.sale_date = b.sale_date
GROUP BY 1
ORDER BY 1 

-- SELECT 
--     a.sale_date, a.sold_num-b.sold_num AS diff
-- FROM
--     Sales a
-- JOIN
--     Sales b
-- ON 
--     a.sale_date = b.sale_date
-- AND 
--     a.fruit IN ('apples') AND b.fruit IN ('oranges')
-- GROUP BY 1
-- ORDER BY 1 

# Approach 2: Create Two Separate Tables and Columns First
-- SELECT 
--     a.sale_date, a.sold_num-b.sold_num AS diff
-- FROM 
--     (SELECT sale_date, sold_num FROM Sales WHERE fruit IN ('apples'))a
-- JOIN
--     (SELECT sale_date, sold_num FROM Sales WHERE fruit IN ('oranges'))b
-- ON 
--     a.sale_date = b.sale_date
-- GROUP BY 1
-- ORDER BY 1

# Approach 3: Calculate With SUM(CASE WHEN)
-- SELECT 
--     sale_date,
--     SUM(CASE WHEN fruit IN ('apples') THEN sold_num 
--              WHEN fruit IN ('oranges') THEN (sold_num)*-1 
--         END) AS diff
-- FROM 
--     Sales
-- GROUP BY 1
-- ORDER BY 1
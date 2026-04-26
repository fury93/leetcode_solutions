# Write your MySQL query statement below
# Approach 1: Not in/Exists in the Subquery
SELECT 
    seller_name
FROM 
    Seller s
WHERE 
    s.seller_id NOT IN (
        SELECT DISTINCT seller_id
        FROM 
            Orders
        WHERE 
            YEAR(sale_date) = 2020
    )
ORDER BY 1 ASC

# Approach 2: Left Join then Exclude the Matching Record.
-- SELECT 
--     seller_name
-- FROM 
--     Seller a
-- LEFT JOIN 
--     (SELECT 
--         DISTINCT seller_id
--     FROM 
--         Orders
--     WHERE 
--         YEAR(sale_date) = 2020) b
-- ON 
--     a.seller_id = b.seller_id
-- WHERE 
--     b.seller_id IS NULL 
-- ORDER BY 1 ASC

# Approach 3: Flag Records by HAVING or CASE WHEN
-- SELECT 
--     seller_name
-- FROM (
--     SELECT 
--         seller_name, 
--         SUM(CASE WHEN YEAR(sale_date) ='2020' THEN 1 ELSE 0 END) AS flag
--     FROM 
--         Seller s
--     LEFT JOIN 
--         Orders o
--     ON 
--         s.seller_id = o.seller_id
--     GROUP BY 
--         s.seller_id
-- )t0
-- WHERE 
--     flag=0
-- ORDER BY 1 ASC
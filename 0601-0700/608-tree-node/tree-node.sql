# Write your MySQL query statement below
# Approach 1: Using UNION
-- SELECT
--     id, 'Root' AS Type
-- FROM
--     tree
-- WHERE
--     p_id IS NULL

-- UNION
-- SELECT
--     id, 'Leaf' AS Type
-- FROM
--     tree
-- WHERE
--     id NOT IN (SELECT DISTINCT
--             p_id
--         FROM
--             tree
--         WHERE
--             p_id IS NOT NULL)
--         AND p_id IS NOT NULL
-- UNION
-- SELECT
--     id, 'Inner' AS Type
-- FROM
--     tree
-- WHERE
--     id IN (SELECT DISTINCT
--             p_id
--         FROM
--             tree
--         WHERE
--             p_id IS NOT NULL)
--         AND p_id IS NOT NULL
-- ORDER BY id;

# Approach 2: Using flow control statement CASE
-- SELECT
--     id AS `Id`,
--     CASE
--         WHEN tree.id = (SELECT atree.id FROM tree atree WHERE atree.p_id IS NULL)
--           THEN 'Root'
--         WHEN tree.id IN (SELECT atree.p_id FROM tree atree)
--           THEN 'Inner'
--         ELSE 'Leaf'
--     END AS Type
-- FROM
--     tree
-- ORDER BY `Id`
-- ;

# Approach 3: Using IF function
SELECT
    atree.id,
    IF(ISNULL(atree.p_id),
        'Root',
        IF(atree.id IN (SELECT p_id FROM tree), 'Inner','Leaf')) Type
FROM
    tree atree
ORDER BY atree.id
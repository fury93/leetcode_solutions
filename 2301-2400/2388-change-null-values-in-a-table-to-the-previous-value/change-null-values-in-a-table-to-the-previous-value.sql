# Write your MySQL query statement below
WITH RECURSIVE WithRowNum (row_num, id, drink) AS (
    SELECT
        ROW_NUMBER() OVER() AS row_num,
        id,
        drink
    FROM CoffeeShop
), Result (row_num, id, drink) AS (
    SELECT
        row_num,
        id,
        drink
    FROM WithRowNum
    WHERE row_num = 1
    UNION ALL
    SELECT
        WithRowNum.row_num,
        WithRowNum.id,
        IFNULL(WithRowNum.drink, Result.drink) AS drink
    FROM Result
    JOIN WithRowNum
    ON Result.row_num = WithRowNum.row_num - 1
)

SELECT id, drink
FROM Result;
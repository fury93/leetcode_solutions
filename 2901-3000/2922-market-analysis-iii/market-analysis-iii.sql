# Write your MySQL query statement below
WITH Sellers AS
(
    SELECT
        U.seller_id,
        COUNT(DISTINCT I.item_id) AS num_items
    FROM Users U
    LEFT JOIN Orders O ON U.seller_id = O.seller_id
    LEFT JOIN Items I ON O.item_id = I.item_id
    WHERE U.favorite_brand != I.item_brand
    GROUP BY U.seller_id
),
RankNums AS
(
    SELECT
        *,
        DENSE_RANK() OVER(ORDER BY num_items DESC) AS rank_num
    FROM Sellers
)
SELECT
    seller_id,
    num_items
FROM RankNums
WHERE rank_num = 1
ORDER BY seller_id;
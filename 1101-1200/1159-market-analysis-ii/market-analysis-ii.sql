# Write your MySQL query statement below
SELECT u.user_id AS seller_id, 
       CASE WHEN u.favorite_brand = b.item_brand THEN 'yes' ELSE 'no' END AS 2nd_item_fav_brand
FROM Users u
LEFT JOIN(
    SELECT a.seller_id, a.item_id, i.item_brand
    FROM (
        SELECT seller_id, 
               item_id,
               RANK() OVER (PARTITION BY seller_id ORDER BY order_date ASC) AS rnk
        FROM Orders) a
    JOIN Items i
    ON a.item_id = i.item_id
    WHERE a.rnk = 2) b
ON u.user_id = b.seller_id 
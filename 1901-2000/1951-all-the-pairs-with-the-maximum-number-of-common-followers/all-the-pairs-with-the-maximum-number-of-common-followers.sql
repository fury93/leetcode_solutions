# Write your MySQL query statement below

WITH CTE AS (
    SELECT
        r1.user_id AS user1_id,
        r2.user_id AS user2_id,
        RANK() OVER(ORDER BY COUNT(r1.follower_id) DESC) as rnk
    FROM Relations AS r1
    JOIN Relations AS r2 ON r1.user_id < r2.user_id
    WHERE r1.follower_id = r2.follower_id
    GROUP BY user1_id, user2_id
)
SELECT user1_id, user2_id
FROM CTE
WHERE rnk = 1

-- select user1_id, user2_id
-- from
-- (
--     select 
--     r1.user_id as user1_id,
--     r2.user_id as user2_id,
--     dense_rank() over(
--         order by count(r1.follower_id) desc
--     ) as rk
-- from Relations r1, Relations r2
-- where r1.user_id < r2.user_id 
-- and r1.follower_id = r2.follower_id 
-- group by r1.user_id, r2.user_id) temp
-- where rk = 1
# Write your MySQL query statement below
SELECT player_id,
       Min(event_date) first_login
FROM   activity
GROUP  BY player_id  

-- SELECT
--   X.player_id,
--   X.event_date AS first_login
-- FROM
--   (
--     SELECT
--       A.player_id,
--       A.event_date,
--       RANK() OVER (
--         PARTITION BY
--           A.player_id
--         ORDER BY
--           A.event_date
--       ) AS rnk
--     FROM
--       Activity A
--   ) X
-- WHERE
--   X.rnk = 1;

-- select player_id, device_id
-- from `activity`
-- group by player_id
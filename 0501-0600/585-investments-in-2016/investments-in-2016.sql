# Write your MySQL query statement below
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM (
   SELECT *,
       COUNT(*)OVER(PARTITION BY tiv_2015) AS tiv_2015_cnt,
       COUNT(*)OVER(PARTITION BY lat, lon) AS loc_cnt
   FROM Insurance
   )t0
WHERE tiv_2015_cnt > 1
AND loc_cnt = 1

-- SELECT
--     ROUND(SUM(insurance.TIV_2016),2) AS TIV_2016
-- FROM
--     insurance
-- WHERE
--     insurance.TIV_2015 IN
--     (
--       SELECT
--         TIV_2015
--       FROM
--         insurance
--       GROUP BY TIV_2015
--       HAVING COUNT(*) > 1
--     )
--     AND CONCAT(LAT, LON) IN
--     (
--       SELECT
--         CONCAT(LAT, LON)
--       FROM
--         insurance
--       GROUP BY LAT , LON
--       HAVING COUNT(*) = 1
--     )
-- ;
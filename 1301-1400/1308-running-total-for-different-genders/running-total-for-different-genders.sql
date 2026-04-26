# Write your MySQL query statement below

SELECT 
    gender, 
    day, 
    SUM(score_points)
         OVER(PARTITION BY gender ORDER BY day) AS total
FROM Scores

-- SELECT s1.gender, s1.day, SUM(s2.score_points) AS total
-- FROM Scores AS s1,
--      Scores AS s2
-- WHERE s1.gender = s2.gender AND s2.day <= s1.day
-- GROUP BY s1.gender, s1.day
-- ORDER BY s1.gender, s1.day
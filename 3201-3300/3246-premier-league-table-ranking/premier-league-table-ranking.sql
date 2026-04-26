# Write your MySQL query statement below
SELECT
    team_id,
    team_name,
    points,
    RANK() OVER (ORDER BY points DESC) AS position
FROM 
(SELECT 
    team_id,
    team_name,
    3*wins + 1*draws AS points
FROM TeamStats
)t
ORDER BY
    3 DESC,
    2 ASC
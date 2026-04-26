# Write your MySQL query statement below
WITH DATA_WITH_START_AND_END_TIME AS (
    SELECT *,
        LEAD(status_time, 1) OVER(PARTITION BY server_id ORDER BY status_time ASC, session_status ASC) AS status_time2
    FROM Servers
),
DURATION AS (
    SELECT TIMESTAMPDIFF(SECOND, status_time, status_time2) AS duration
    FROM DATA_WITH_START_AND_END_TIME
    WHERE session_status = 'start'
)
SELECT FLOOR(SUM(duration)/(24 * 60 * 60)) AS total_uptime_days
FROM DURATION
# Write your MySQL query statement below
SELECT ROUND(AVG(daily_rate)*100, 2) AS average_daily_percent
FROM (
    SELECT action_date, 
        COUNT(DISTINCT CASE WHEN a.post_id = r.post_id THEN r.post_id END) / COUNT(DISTINCT a.post_id) AS daily_rate
    FROM Actions a
    LEFT JOIN Removals r
    ON a.post_id = r.post_id
    WHERE a.extra = 'spam'
    GROUP BY action_date
    )t0
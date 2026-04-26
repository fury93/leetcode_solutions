# Write your MySQL query statement below
WITH new_event_start AS (
  SELECT
  	IFNULL(start_day > MAX(end_day) OVER pw, 1) AS is_new_event_start,
  	hall_id,
    start_day,
  	end_day
  FROM
  	HallEvents
  WINDOW
  	pw AS (
      PARTITION BY hall_id 
      ORDER BY start_day ASC, end_day DESC
      ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING
    )
),
event_id AS (
  SELECT
  	SUM(is_new_event_start) OVER w AS event_id,
    hall_id,
    start_day,
    end_day
  FROM
  	new_event_start
  WINDOW
  	w AS (
      PARTITION BY hall_id
      ORDER BY start_day ASC, end_day DESC
    )
)
SELECT
	hall_id,
    min(start_day) AS start_day,
    max(end_day) As end_day    
FROM
	event_id
GROUP BY hall_id, event_id
  
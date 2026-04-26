# Write your MySQL query statement below
# Approach 1: Transform Values with CASE WHEN and then Calculate
-- SELECT 
--     machine_id,
--     ROUND(SUM(CASE WHEN activity_type='start' THEN timestamp*-1 ELSE timestamp END)*1.0
--     / (SELECT COUNT(DISTINCT process_id)),3) AS processing_time
-- FROM 
--     Activity
-- GROUP BY machine_id

# Approach 2: Calling the original Table twice and Calculate as two columns
SELECT a.machine_id, 
       ROUND(AVG(b.timestamp - a.timestamp), 3) AS processing_time
FROM Activity a, 
     Activity b
WHERE 
    a.machine_id = b.machine_id
AND 
    a.process_id = b.process_id
AND 
    a.activity_type = 'start'
AND 
    b.activity_type = 'end'
GROUP BY machine_id

-- select 
--  s.machine_id,
--  ROUND(AVG(e.timestamp - s.timestamp),3) as processing_time
-- from activity s join activity e on
--     s.machine_id = e.machine_id and
--     s.process_id = e.process_id and
--     s.activity_type = 'start' and
--     e.activity_type = 'end'
-- group by s.machine_id
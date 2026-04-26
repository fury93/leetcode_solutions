# Write your MySQL query statement below

# Approach 1: Using the Aggregate Function
-- SELECT 
--   e.business_id 
-- FROM 
--   Events e 
--   JOIN (
--     SELECT 
--       event_type, 
--       AVG(occurrences) AS avg 
--     FROM 
--       Events 
--     GROUP BY 
--       event_type
--   ) t0 ON e.event_type = t0.event_type 
--   AND e.occurrences > t0.avg 
-- GROUP BY 
--   e.business_id 
-- HAVING 
--   COUNT(*) > 1

# Approach 2: Using the Window Function
SELECT 
  business_id 
FROM 
  (
    SELECT 
      business_id, 
      event_type, 
      occurrences, 
      AVG(occurrences) OVER (PARTITION BY event_type) AS avg 
    FROM 
      Events
  ) t0 
WHERE 
  occurrences > avg 
GROUP BY 
  business_id 
HAVING 
  COUNT(*) > 1
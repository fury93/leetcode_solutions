# Write your MySQL query statement below
# Approach 1: Combining Tables Using UNION ALL and Finding the Top Values Using ORDER BY + LIMIT
-- WITH all_ids AS (
--    SELECT requester_id AS id 
--    FROM RequestAccepted
--    UNION ALL
--    SELECT accepter_id AS id
--    FROM RequestAccepted)
-- SELECT id, 
--    COUNT(id) AS num
-- FROM all_ids
-- GROUP BY id
-- ORDER BY COUNT(id) DESC
-- LIMIT 1

#Approach 2: Combining Tables Using UNION ALL and Finding Top Values Using RANK()
WITH all_ids AS (
   SELECT requester_id AS id 
   FROM RequestAccepted
   UNION ALL
   SELECT accepter_id AS id
   FROM RequestAccepted)
SELECT id, num
FROM 
   (
   SELECT id, 
      COUNT(id) AS num, 
      RANK () OVER(ORDER BY COUNT(id) DESC) AS rnk
   FROM all_ids
   GROUP BY id
   )t0
WHERE rnk=1


-- select requester_id as id,
--     (select count(*) from RequestAccepted  where (requester_id = id or accepter_id = id)) as num
-- from RequestAccepted
-- group by requester_id
-- union 
-- select accepter_id as id,
--     (select count(*) from RequestAccepted  where (requester_id = id or accepter_id = id)) as num
-- from RequestAccepted
-- group by accepter_id
-- order by num desc limit 1; 
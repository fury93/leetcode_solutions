# Write your MySQL query statement below

# Approach 1: Groupby with Having
SELECT 
  DISTINCT viewer_id as id 
FROM 
  Views 
GROUP BY 
  viewer_id, 
  view_date 
HAVING 
  COUNT(DISTINCT article_id) > 1 
ORDER BY 
  viewer_id;

# Approach 2: Self-Join
-- SELECT 
--   DISTINCT v1.viewer_id AS id 
-- FROM 
--   Views v1 
--   JOIN Views v2 ON v1.viewer_id = v2.viewer_id 
--   AND v1.view_date = v2.view_date 
--   AND v1.article_id < v2.article_id 
-- ORDER BY 
--   v1.viewer_id;
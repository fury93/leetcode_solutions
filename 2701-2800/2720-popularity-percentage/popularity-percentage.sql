# Write your MySQL query statement below
WITH FriendshipsExpanded AS (
  -- Expanding friendships to account for both user1 and user2 as primary users
  SELECT 
    user1, 
    user2 
  FROM 
    Friends 
  UNION
  SELECT 
    user2, 
    user1 
  FROM 
    Friends
) 
SELECT 
  user1, 
  ROUND(
    -- Calculating the percentage popularity
    100 * COUNT(DISTINCT user2) / COUNT(user1) OVER (), 
    2
  ) AS percentage_popularity 
FROM 
  FriendshipsExpanded 
GROUP BY 
  user1 -- Grouping results by primary user
ORDER BY 
  user1;
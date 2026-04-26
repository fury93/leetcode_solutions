# Write your MySQL query statement below
-- Common Table Expression for Consolidating Scores
WITH PlayerScores AS (
  -- Combine scores where player is the first player
  SELECT 
    first_player AS player_id, 
    first_score AS score 
  FROM 
    matches 
  UNION ALL 
    -- Combine scores where player is the second player
  SELECT 
    second_player AS player_id, 
    second_score AS score 
  FROM 
    matches
), 
TotalScores AS (
  -- Aggregate Total Scores for Each Player
  SELECT 
    player_id, 
    SUM(score) AS total_score 
  FROM 
    PlayerScores 
  GROUP BY 
    player_id
) -- Select the Winner in Each Group
SELECT 
  DISTINCT group_id, 
  -- Use window function to determine the player with the highest score in each group
  -- In case of a tie, the player with the lowest player_id is chosen
  FIRST_VALUE(TotalScores.player_id) OVER (
    PARTITION BY group_id 
    ORDER BY 
      total_score DESC, 
      TotalScores.player_id
  ) AS player_id -- Winner player_id
FROM 
  TotalScores -- Join with Players table to get group information
  LEFT JOIN players ON TotalScores.player_id = players.player_id
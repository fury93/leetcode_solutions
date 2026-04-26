# Write your MySQL query statement below
WITH RankedMatches AS (
  SELECT 
    player_id, 
    match_day, 
    result, 
    CASE WHEN result = 'Win' THEN 0 ELSE 1 END AS is_not_win, 
    ROW_NUMBER() OVER (
      PARTITION BY player_id 
      ORDER BY 
        match_day
    ) - ROW_NUMBER() OVER (
      PARTITION BY player_id, 
      result 
      ORDER BY 
        match_day
    ) AS streak_group 
  FROM 
    Matches
), 
Streaks AS (
  SELECT 
    player_id, 
    SUM(1 - is_not_win) OVER (
      PARTITION BY player_id, 
      streak_group 
      ORDER BY 
        match_day
    ) AS streak_length, 
    is_not_win 
  FROM 
    RankedMatches
) 
SELECT 
  player_id, 
  MAX(
    CASE WHEN is_not_win = 0 THEN streak_length ELSE 0 END
  ) AS longest_streak 
FROM 
  Streaks 
GROUP BY 
  player_id;
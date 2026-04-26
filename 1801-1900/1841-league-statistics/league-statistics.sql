# Write your MySQL query statement below
SELECT 
  t.team_name, 
  COUNT(*) AS matches_played, 
  SUM(
    CASE WHEN (
      m.home_team_id = t.team_id 
      AND m.home_team_goals > m.away_team_goals
    ) 
    OR (
      m.away_team_id = t.team_id 
      AND m.away_team_goals > m.home_team_goals
    ) THEN 3 WHEN m.home_team_goals = m.away_team_goals THEN 1 ELSE 0 END
  ) AS points, 
  SUM(
    CASE WHEN m.home_team_id = t.team_id THEN m.home_team_goals ELSE m.away_team_goals END
  ) AS goal_for, 
  SUM(
    CASE WHEN m.home_team_id = t.team_id THEN m.away_team_goals ELSE m.home_team_goals END
  ) AS goal_against, 
  SUM(
    CASE WHEN m.home_team_id = t.team_id THEN m.home_team_goals - m.away_team_goals ELSE m.away_team_goals - m.home_team_goals END
  ) AS goal_diff 
FROM 
  Teams t 
  JOIN Matches m ON m.home_team_id = t.team_id 
  OR m.away_team_id = t.team_id 
GROUP BY 
  t.team_id, 
  t.team_name 
ORDER BY 
  points DESC, 
  goal_diff DESC, 
  team_name;
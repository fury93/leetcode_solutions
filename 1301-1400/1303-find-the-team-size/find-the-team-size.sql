# Write your MySQL query statement below
-- select e.employee_id, 
--     (select count(team_id) 
-- from Employee 
-- where e.team_id = team_id) as team_size
-- from Employee e

SELECT employee_id, team_size
FROM Employee AS e
LEFT JOIN (
      SELECT team_id, COUNT(DISTINCT employee_id) AS team_size
      FROM Employee
      GROUP BY team_id
) AS teams
ON e.team_id = teams.team_id
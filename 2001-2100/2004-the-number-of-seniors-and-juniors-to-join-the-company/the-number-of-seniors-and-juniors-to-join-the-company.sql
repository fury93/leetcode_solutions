# Write your MySQL query statement below
WITH SeniorCandidates AS (
  SELECT 
    *, 
    SUM(salary) OVER (
      ORDER BY 
        salary
    ) AS cumulative_salary 
  FROM 
    Candidates 
  WHERE 
    experience = 'Senior'
), 
HiredSeniors AS (
  SELECT 
    COUNT(*) AS count 
  FROM 
    SeniorCandidates 
  WHERE 
    cumulative_salary <= 70000
), 
RemainingBudget AS (
  SELECT 
    70000 - COALESCE(
      (
        SELECT 
          cumulative_salary 
        FROM 
          SeniorCandidates 
        WHERE 
          cumulative_salary <= 70000 
        ORDER BY 
          cumulative_salary DESC 
        LIMIT 
          1
      ), 0
    ) AS budget
), 
JuniorCandidates AS (
  SELECT 
    *, 
    SUM(salary) OVER (
      ORDER BY 
        salary
    ) AS cumulative_salary 
  FROM 
    Candidates 
  WHERE 
    experience = 'Junior'
), 
HiredJuniors AS (
  SELECT 
    COUNT(*) AS count 
  FROM 
    JuniorCandidates, 
    RemainingBudget 
  WHERE 
    JuniorCandidates.cumulative_salary <= RemainingBudget.budget
) 
SELECT 
  'Senior' AS experience, 
  (
    SELECT 
      count 
    FROM 
      HiredSeniors
  ) AS accepted_candidates 
UNION 
SELECT 
  'Junior' AS experience, 
  (
    SELECT 
      count 
    FROM 
      HiredJuniors
  ) AS accepted_candidates;
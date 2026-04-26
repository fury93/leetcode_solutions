# Write your MySQL query statement below
SELECT 
  c.name 
FROM 
  Candidate AS c 
  JOIN (
    SELECT 
      candidateId, 
      COUNT(*) AS vote_count 
    FROM 
      Vote 
    GROUP BY 
      candidateId 
    ORDER BY 
      COUNT(*) DESC 
    LIMIT 
      1
  ) AS v 
  ON c.id = v.candidateId;

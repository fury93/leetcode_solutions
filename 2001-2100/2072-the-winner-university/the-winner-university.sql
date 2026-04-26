# Write your MySQL query statement below
SELECT 
  CASE 
    WHEN NY.excellent_students > CA.excellent_students THEN 'New York University'
    WHEN NY.excellent_students < CA.excellent_students THEN 'California University'
    ELSE 'No Winner'
  END AS winner
FROM 
  (
    SELECT 
      COUNT(*) as excellent_students 
    FROM 
      NewYork 
    WHERE 
      score >= 90
  ) NY, 
  (
    SELECT 
      COUNT(*) as excellent_students 
    FROM 
      California 
    WHERE 
      score >= 90
  ) CA;
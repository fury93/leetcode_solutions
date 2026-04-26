# Write your MySQL query statement below
WITH CTE AS (
  SELECT 
    airport_id, 
    RANK() OVER(ORDER BY SUM(flights_count) DESC) AS RN
  FROM ( 
    SELECT departure_airport AS airport_id, flights_count FROM Flights
           UNION ALL
       SELECT arrival_airport AS airport_id, flights_count FROM Flights ) T
  GROUP BY airport_id )

SELECT airport_id FROM CTE WHERE RN = 1
# Write your MySQL query statement below
SELECT 
  f.flight_id, 
  LEAST(
    f.capacity, 
    COUNT(p.passenger_id)
  ) AS booked_cnt, 
  GREATEST(
    0, 
    COUNT(p.passenger_id) - f.capacity
  ) AS waitlist_cnt 
FROM 
  Flights f 
  LEFT JOIN Passengers p ON f.flight_id = p.flight_id 
GROUP BY 
  f.flight_id 
ORDER BY 
  f.flight_id;
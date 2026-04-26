# Write your MySQL query statement below
WITH OrderedBusArrivals AS (
  -- Joining buses with passengers who arrived on or before each bus's arrival.
  -- Counting the number of passengers eligible to board each bus.
  SELECT 
    bus_id, 
    b.arrival_time, 
    capacity, 
    COUNT(passenger_id) AS eligible_passengers 
  FROM 
    Buses b 
    LEFT JOIN Passengers p ON p.arrival_time <= b.arrival_time 
  WHERE 
    bus_id IS NOT NULL 
  GROUP BY 
    bus_id 
  ORDER BY 
    b.arrival_time
) 
SELECT 
  bus_id, 
  passengers_cnt 
FROM 
  (
    SELECT 
      bus_id, 
      capacity, 
      eligible_passengers, 
      -- Calculating the number of passengers that can board the bus.
      -- Limited by either the bus's capacity or the remaining passengers after previous buses.
      @boarded_passengers := LEAST(
        capacity, eligible_passengers - @accumulated_boarding
      ) AS passengers_cnt, 
      -- Updating the total number of passengers who have boarded buses so far.
      @accumulated_boarding := @accumulated_boarding + @boarded_passengers 
    FROM 
      OrderedBusArrivals, 
      (
        SELECT 
          @accumulated_boarding := 0, 
          @boarded_passengers := 0
      ) AS Initialization
  ) AS FinalResult 
ORDER BY 
  bus_id;
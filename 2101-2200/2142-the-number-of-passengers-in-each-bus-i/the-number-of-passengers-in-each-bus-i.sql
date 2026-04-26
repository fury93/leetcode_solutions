# Write your MySQL query statement below
# Get each passenger's boarding time
WITH t AS
(
    SELECT passenger_id, MIN(b.arrival_time) AS arrival_time
    FROM Passengers p
    INNER JOIN Buses b
    ON p.arrival_time <= b.arrival_time
    GROUP BY passenger_id
)

# Boarding time and bus id have 1 to 1 correspondence
SELECT bus_id, COUNT(t.arrival_time) AS passengers_cnt
FROM Buses b
LEFT JOIN t
ON b.arrival_time = t.arrival_time
GROUP BY bus_id
ORDER BY bus_id
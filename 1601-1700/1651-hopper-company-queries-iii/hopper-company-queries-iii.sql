# Write your MySQL query statement below

# create 12 month table
WITH RECURSIVE month AS (
    SELECT 1 AS month
    UNION
    SELECT month+1 AS month
    FROM month where month <12
),

# create monthly rides
month_rides AS (
    SELECT Month(r.requested_at) AS month,
    SUM(a.ride_distance) AS ride_distance,
    SUM(a.ride_duration) AS ride_duration
    FROM Rides r
    LEFT JOIN AcceptedRides a
    ON r.ride_id = a.ride_id
    WHERE YEAR(requested_at) = '2020'
    GROUP BY month
),

# create 12 month monthly rides
every_month_ride AS (
    SELECT m.month,
    IFNULL(r.ride_distance,0) AS ride_distance,
    IFNULL(r.ride_duration,0) AS ride_duration
    FROM month m LEFT JOIN month_rides r
    ON m.month = r.month
    )

    SELECT month,
    ROUND(AVG(ride_distance) OVER(ORDER BY month ROWS BETWEEN CURRENT ROW AND 2 FOLLOWING), 2) AS average_ride_distance,
    ROUND(AVG(ride_duration) OVER(ORDER BY month ROWS BETWEEN CURRENT ROW AND 2 FOLLOWING), 2) AS average_ride_duration
    FROM every_month_ride
    ORDER BY month
    LIMIT 10
# Write your MySQL query statement below
WITH RECURSIVE Months AS (
    SELECT 
        1 AS month
    UNION ALL
    SELECT 
        month + 1
    FROM 
        Months
    WHERE 
        month < 12
), Driver AS (
    SELECT 
        driver_id, 
	    (CASE WHEN YEAR(join_date) = 2019 THEN '1' ELSE MONTH(join_date) END) AS month
	FROM 
        Drivers 
	WHERE 
        YEAR(join_date) <= 2020
), Ride AS (
    SELECT 
        MONTH(requested_at) AS month, 
        a.ride_id
    FROM 
        AcceptedRides AS a 
    INNER JOIN 
        Rides r
    ON 
        r.ride_id = a.ride_id
    WHERE 
        YEAR(requested_at) = 2020
)

SELECT
    m.month, 
    COUNT(DISTINCT d.driver_id) AS active_drivers,
    COUNT(DISTINCT r.ride_id) AS accepted_rides 
FROM
    Months AS m
LEFT JOIN
    Driver AS d
ON 
    d.month <= m.month
LEFT JOIN
    Ride AS r
ON 
    m.month = r.month
GROUP BY 
    m.month 
ORDER BY 
    m.month 
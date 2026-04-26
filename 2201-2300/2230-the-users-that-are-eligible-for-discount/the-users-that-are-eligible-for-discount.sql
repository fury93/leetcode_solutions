CREATE PROCEDURE getUserIDs(
    startDate DATE, endDate DATE, minAmount INT
)
BEGIN
	# Write your MySQL query statement below.
    SELECT DISTINCT user_id AS user_id
    FROM Purchases
    WHERE (
        DATE(time_stamp) BETWEEN startDate 
        AND DATE_SUB(endDate, INTERVAL 1 DAY)
        AND
        amount >= minAmount
    )
    ORDER BY user_id;
END
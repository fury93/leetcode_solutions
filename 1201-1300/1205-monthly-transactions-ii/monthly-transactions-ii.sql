# Write your MySQL query statement below
SELECT t0.month,
    t0.country,
    SUM(approved_count) AS approved_count,
    SUM(approved_amount) AS approved_amount,
    SUM(chargeback_count) AS chargeback_count,
    SUM(chargeback_amount) AS chargeback_amount
FROM (
    SELECT DATE_FORMAT(c.trans_date, '%Y-%m') AS month,
        t.country,
        0 AS approved_count,
        0 AS approved_amount,
        COUNT(DISTINCT c.trans_id) AS chargeback_count,
        SUM(amount) AS chargeback_amount
    FROM Chargebacks c
    JOIN Transactions t
    ON c.trans_id = t.id
    GROUP BY month, country
    UNION ALL
    SELECT DATE_FORMAT(trans_date, '%Y-%m') AS month,
       country,
       COUNT(DISTINCT id) AS approved_count,
       SUM(amount) AS approved_amount,
       0 AS chargeback_count,
       0 AS chargeback_amount
    FROM Transactions t
    WHERE state = 'approved'
    GROUP BY month, country) AS t0
GROUP BY month, country
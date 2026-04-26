# Write your MySQL query statement below
SELECT '[0-5>' AS 'bin', SUM(duration/60 < 5) AS 'total'
FROM Sessions
UNION
SELECT '[5-10>' AS 'bin',
 SUM(duration/60 >= 5 AND duration/60 < 10) AS 'total'
FROM Sessions
UNION
SELECT '[10-15>' AS 'bin',
 SUM(duration/60 >= 10 AND duration/60 < 15) AS 'total'
FROM Sessions
UNION
SELECT '15 or more' AS 'bin',
 SUM(duration/60 >= 15) AS 'total'
FROM Sessions
# Write your MySQL query statement below
-- select w2.id 
-- from weather w1, weather w2
-- where w2.temperature > w1.temperature and datediff(w2.recorddate, w1.recorddate) = 1

SELECT w1.id
FROM Weather w1
JOIN Weather w2 ON DATE(w1.recordDate) = DATE(w2.recordDate) + INTERVAL 1 DAY
WHERE w1.temperature > w2.temperature;
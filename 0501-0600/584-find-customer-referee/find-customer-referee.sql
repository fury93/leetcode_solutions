# Write your MySQL query statement below
SELECT name FROM customer WHERE referee_id <> 2 OR referee_id IS NULL;
-- select name
-- from Customer
-- where COALESCE(referee_id, 0) <> 2
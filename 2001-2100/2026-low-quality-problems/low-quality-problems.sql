# Write your MySQL query statement below
SELECT a.problem_id 
FROM Problems AS a 
Where a.likes*2<a.dislikes*3 
ORDER BY a.problem_id ASC;


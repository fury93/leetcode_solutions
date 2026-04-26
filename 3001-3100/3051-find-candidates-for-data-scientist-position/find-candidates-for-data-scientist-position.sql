# Write your MySQL query statement below
-- SELECT candidate_id
-- FROM Candidates
-- GROUP BY candidate_id
-- HAVING SUM(IF(skill = 'Python', 1, 0)) + SUM(IF(skill = 'Tableau', 1, 0)) + SUM(IF(skill = 'PostgreSQL', 1, 0)) = 3
-- ORDER BY candidate_id ASC

# Write your MySQL query statement below
select candidate_id
from candidates
where skill IN ('Python','Tableau','PostgreSQL')
group by 1
having count(skill)=3
order by 1 asc
# Write your MySQL query statement below
WITH vote_count AS (SELECT voter, COUNT(*) AS vote_count FROM Votes GROUP BY voter),

votes AS (
SELECT candidate, SUM(1. / vote_count) AS votes FROM Votes a, vote_count b WHERE a.voter = b.voter AND a.candidate IS NOT NULL GROUP BY candidate
)

SELECT candidate FROM votes WHERE votes = (SELECT MAX(votes) FROM votes) ORDER BY candidate

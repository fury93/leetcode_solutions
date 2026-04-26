# Write your MySQL query statement below
SELECT DISTINCT a.user_id AS user1_id, b.user_id AS user2_id # 1) Find distinct combos
FROM Listens a, Listens b
WHERE a.day = b.day
	AND a.song_id = b.song_id
	AND a.user_id != b.user_id
	AND (a.user_id, b.user_id) IN (
        SELECT * FROM Friendship
    ) # 2) They are also in Friendship table
	
GROUP BY a.user_id, b.user_id, b.day
HAVING COUNT(DISTINCT a.song_id) >= 3 # 3) There are >= 3 overlaps
# Write your MySQL query statement below
SELECT user1_id as user_id,page_id,COUNT(user_id) as friends_likes
FROM
(
    SELECT a.user1_id,b.user_id,b.page_id # user, all user friends, page_id
    FROM Friendship as a
    JOIN Likes as b
    ON a.user2_id=b.user_id
    UNION SELECT a.user2_id,b.user_id,b.page_id
    FROM Friendship as a
    JOIN Likes as b
    ON a.user1_id=b.user_id
) a
WHERE CONCAT(user1_id,",",page_id) NOT IN
(SELECT CONCAT(user_id,",",page_id) FROM Likes)
GROUP BY user1_id,page_id;
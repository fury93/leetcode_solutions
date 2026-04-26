# Write your MySQL query statement below
WITH A AS(
    SELECT *, 
    RANK() OVER(
        PARTITION BY gender ORDER BY user_id
    ) AS rnk,
    IF(gender='female', 0, IF(gender='other', 1,  2))
     AS rnk2 FROM Genders
)
SELECT user_id, gender FROM A ORDER BY rnk, rnk2;
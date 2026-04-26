# Write your MySQL query statement below
WITH CALLS_RANK AS (
    SELECT CONTACT_ID, TYPE, DURATION,
        RANK() OVER (
            PARTITION BY TYPE ORDER BY DURATION DESC
        ) AS RANK1
    FROM CALLS)

SELECT B.FIRST_NAME, A.TYPE, 
    CONCAT( 
        LPAD(FLOOR(DURATION /3600), 2, '0'), ':',
        LPAD(FLOOR((DURATION%3600)/60), 2, '0'), ':', 
        LPAD(FLOOR((DURATION%3600)%60), 2, '0')) AS DURATION_FORMATTED
FROM CALLS_RANK AS A 
JOIN CONTACTS AS B ON A.CONTACT_ID = B.ID AND A.RANK1 <= 3
ORDER BY A.TYPE DESC, DURATION_FORMATTED DESC, B.FIRST_NAME DESC

-- with cte as(select first_name,c.contact_id, type,duration,
-- dense_rank() over(partition by type order by duration desc)as rn
-- from calls c
-- inner join contacts co
-- on co.id=c.contact_id)

-- select first_name,type,date_format(sec_to_time(duration), '%H:%i:%s') as duration_formatted
-- from cte
-- where type='incoming'
-- and rn between 1 and 3
-- union
-- select  first_name,type,date_format(sec_to_time(duration), '%H:%i:%s') as duration_formatted
-- from cte
-- where type='outgoing'
-- and rn between 1 and 3
-- order by 2 desc, 3 desc, 1 desc
# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below
-- delete p1
-- from person p1, person p2
-- where p1.id > p2.id and p1.email = p2.email

DELETE FROM `Person`
WHERE `id` NOT IN (
    SELECT * FROM (
        SELECT MIN(`id`) AS `id` FROM `Person` #store the minimum id's so that one stays
        GROUP BY `email`
    ) AS `keep_ids`
);
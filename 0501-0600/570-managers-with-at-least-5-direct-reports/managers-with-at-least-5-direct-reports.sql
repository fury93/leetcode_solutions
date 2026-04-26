# Write your MySQL query statement below
SELECT
    Name
FROM
    Employee AS t1 
JOIN
    (SELECT 
        ManagerId
    FROM 
        Employee
    GROUP BY ManagerId
    HAVING COUNT(ManagerId) >= 5) AS t2
ON 
    t1.Id = t2.ManagerId
;

-- SELECT
--     name
-- FROM
--     employee
-- WHERE
--     id IN (
--         SELECT
--             managerId
--         FROM
--             employee
--         GROUP BY
--             managerId
--         HAVING COUNT(*) >= 5
--     );

-- select m.name
-- from employee e join employee m on e.managerid = m.id
-- group by e.managerid
-- having count(*) >=5
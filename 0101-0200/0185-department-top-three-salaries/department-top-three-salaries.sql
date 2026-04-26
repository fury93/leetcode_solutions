# Write your MySQL query statement below
-- SELECT
--     d.Name AS 'Department', e1.Name AS 'Employee', e1.Salary
-- FROM
--     Employee e1
--         JOIN
--     Department d ON e1.DepartmentId = d.Id
-- WHERE
--     3 > (SELECT
--             COUNT(DISTINCT e2.Salary)
--         FROM
--             Employee e2
--         WHERE
--             e2.Salary > e1.Salary
--                 AND e1.DepartmentId = e2.DepartmentId
--         )
-- ;

select Department, Employee, Salary 
    from (
    select 
    dense_rank() over w as top,
    e.name as Employee, salary as Salary, departmentId, d.name as Department from Employee e
    join Department d
    on e.departmentId = d.id 
    window w as (
    partition by departmentId
    order by salary desc
    )
) x
where top < 4
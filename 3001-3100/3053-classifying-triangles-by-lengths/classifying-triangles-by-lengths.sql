# Write your MySQL query statement below
select case when a+b<=c or b+c<=a or a+c<=b then 'Not A Triangle'
when a=b and b=c then 'Equilateral'
when a=b or b=c or a=c then 'Isosceles'
else 'Scalene'
end as triangle_type
from Triangles;
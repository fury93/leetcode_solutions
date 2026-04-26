# Write your MySQL query statement below
-- select 
-- a.symbol as metal,
-- b.symbol as nonmetal
-- from 
-- Elements as a,
-- Elements as b
-- where a.type= "Metal" and b.type="Nonmetal"

with metals as (
select * from Elements
where type in ('Metal')
)
, nonmetals as (
select * from Elements
where type in ('Nonmetal')    
)

select m.symbol as metal
, n.symbol as nonmetal 
from metals m cross join nonmetals n
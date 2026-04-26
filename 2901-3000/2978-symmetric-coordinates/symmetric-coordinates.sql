# Write your MySQL query statement below
with cte as (
    select X as X, Y as Y 
    from Coordinates where X <> Y group by X, Y
    union all
    select Y as X, X as Y 
    from Coordinates where X <> Y group by Y, X
    union all
    select X as X, Y as Y 
    from Coordinates where X = Y
)
select
    X,
    Y
from
    cte
group by
    X,
    Y
having
    count(*) > 1
    and
    X <= Y
order by
    X,
    Y
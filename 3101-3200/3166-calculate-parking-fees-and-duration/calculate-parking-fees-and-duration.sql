# Write your MySQL query statement below
# Write your MySQL query statement below

with tmp as(
    select  lot_id,
    car_id,
    sum(TIMESTAMPDIFF(minute,entry_time, exit_time)/60) as hours,
    sum(fee_paid) as fee_paid
from ParkingTransactions
group by lot_id, car_id)

select 
    t1.car_id, 
    total_fee_paid, 
    avg_hourly_fee, 
    t2.lot_id as most_time_lot 
from (select car_id, 
        round(sum(fee_paid),2) as total_fee_paid, 
        round(sum(fee_paid)/sum(hours),2) as avg_hourly_fee
from tmp
group by car_id) t1
left join (
    select car_id, lot_id
    from 
        (
        select 
            car_id, 
            lot_id, 
            rank() over(
                partition by car_id order by hours desc
            ) as rk 
        from tmp 
        order by car_id, hours desc
        ) t3
    where rk=1
) t2
using(car_id)
order by t1.car_id

-- with a as (
-- select
-- lot_id,car_id,
-- sum(fee_paid) over (partition by car_id) as total_fee_paid,
-- sum(timestampdiff(SECOND,entry_time,exit_time)) over (partition by car_id) as hours_spent,
-- sum(timestampdiff(SECOND,entry_time,exit_time)) over (partition by car_id,lot_id) as hours_spent_lot
-- from parkingtransactions
-- )

-- select distinct car_id,total_fee_paid, round(total_fee_paid/(hours_spent/(60*60)),2) as avg_hourly_fee,lot_id as most_time_lot from a
-- where (car_id,hours_spent_lot) in (select car_id,max(hours_spent_lot) from a group by 1)
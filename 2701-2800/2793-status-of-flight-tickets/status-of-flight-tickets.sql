# Write your MySQL query statement below
select passenger_id, if(idx <= capacity, "Confirmed", "Waitlist") Status
from
(
    select passenger_id, rank() over(partition by p.flight_id order by booking_time) idx, f.capacity
    from passengers p
    left join
    flights f
    on f.flight_id = p.flight_id
) t
order by passenger_id
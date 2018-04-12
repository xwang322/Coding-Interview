# Write your MySQL query statement below
select c1.seat_id 
from cinema c1 
where c1.free=1 and
(   c1.seat_id+1 in (select seat_id from cinema where free=1)
    or
    c1.seat_id-1 in (select seat_id from cinema where free=1)
)
order by c1.seat_id
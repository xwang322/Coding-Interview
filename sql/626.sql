# Write your MySQL query statement below
select a.id,  
case when b.student is null then a.student else b.student end
as student 
from seat a left join seat b
on (case when a.id&1 then a.id+1=b.id else a.id-1=b.id end)
order by a.id
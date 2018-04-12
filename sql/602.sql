# Write your MySQL query statement below
select t.id as id, count(t.id) as num
from (select r1.requester_id as id from request_accepted r1 union all select r2.accepter_id as id from request_accepted r2) as t
group by t.id 
order by count(t.id) desc limit 1
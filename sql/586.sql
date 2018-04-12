# Write your MySQL query statement below
select customer_number
from (select customer_number, count(*) as counts from orders group by customer_number order by counts desc) t
limit 1
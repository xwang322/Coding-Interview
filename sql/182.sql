# Write your MySQL query statement below
select distinct p1.Email
from Person p1 
group by p1.Email having count(*)>1
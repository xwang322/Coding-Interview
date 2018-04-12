# Write your MySQL query statement below
select E1.Id, E1.Month, (ifnull(E1.Salary,0) + ifnull(E2.Salary,0) + ifnull(E3.Salary,0)) as Salary 
from  (select id, max(Month) as month from Employee group by id having count(*)>1) as maxmonth
left join Employee E1 on (maxmonth.id=E1.id and maxmonth.month>E1.month)
left join Employee E2 on (E1.id=E2.id and E1.month=E2.month+1)
left join Employee E3 on (E1.id=E3.id and E1.month=E3.month+2)
order by Id asc, Month desc
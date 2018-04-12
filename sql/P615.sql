# Write your MySQL query statement below
select A.pay_m as pay_month, A.department_id, if(A.amt=B.amt, 'same', if(A.amt>B.amt, 'higher', 'lower')) as comparison
from (select pay_m, department_id, avg(amount) as amt from (select *, left(pay_date, 7) as pay_m from salary) S
join employee E on S.employee_id=E.employee_id group by pay_m, department_id) as A
join (select pay_m, avg(amount) as amt from (select *, left(pay_date,7) as pay_m from salary) as T1 group by pay_m) as B
on A.pay_m=B.pay_m
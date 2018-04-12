# Write your MySQL query statement below
select name
from salesperson 
where not exists (
    select * 
    from orders join company on orders.com_id=company.com_id and company.name='RED'
    where salesperson.sales_id=orders.sales_id
)
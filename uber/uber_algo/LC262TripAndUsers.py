# Write your MySQL query statement below
select Trips.Request_at as Day, round (sum(if (status != 'completed', 1, 0)) / sum(1), 2) as 'Cancellation Rate'
from Trips
join Users
on Trips.Client_Id = Users.Users_Id
where Users.Banned = 'No'
and Trips.Request_at between '2013-10-01' and '2013-10-03'
Group by Trips.Request_at

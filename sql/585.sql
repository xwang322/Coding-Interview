# Write your MySQL query statement below
select round(sum(i1.TIV_2016), 2) as TIV_2016
from insurance i1
where exists (select * from insurance i2 where i1.PID!=i2.PID and i1.TIV_2015=i2.TIV_2015)
      and not exists (select * from insurance i3 where i1.PID!=i3.PID and i1.LAT=i3.LAT and i1.LON=i3.LON)
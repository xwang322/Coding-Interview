# Write your MySQL query statement below
select Score, (select count(*) from (select distinct Score dis from Scores)t where dis>=Score) Rank
from Scores
order by Score desc;
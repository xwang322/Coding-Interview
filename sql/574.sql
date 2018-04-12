# Write your MySQL query statement below
select Name 
from Candidate
where id = (select CandidateId from Vote group by CandidateId order by count(CandidateId) desc limit 1)
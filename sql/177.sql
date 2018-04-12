CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
declare m int;
set m = n-1;
  RETURN (
      select distinct Salary from Employee order by Salary DESC limit m, 1
  );
END
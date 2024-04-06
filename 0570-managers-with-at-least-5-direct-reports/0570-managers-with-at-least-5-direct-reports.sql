# Write your MySQL query statement below
select name from employee where id in
(select e1.managerId
from employee e1
group by e1.managerId
having count(*)>=5);
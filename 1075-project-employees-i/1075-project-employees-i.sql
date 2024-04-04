# Write your MySQL query statement below
select p.project_id, round(avg(experience_years),2) as average_years
from employee e, project p
where p.employee_id = e.employee_id
group by p.project_id;
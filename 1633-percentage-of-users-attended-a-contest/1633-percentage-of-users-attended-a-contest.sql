# Write your MySQL query statement below
select r.contest_id, round((count(*)/(select count(*) from users))*100,2) as percentage
from register r, users u
where u.user_id = r.user_id
group by r.contest_id
order by percentage desc, r.contest_id asc
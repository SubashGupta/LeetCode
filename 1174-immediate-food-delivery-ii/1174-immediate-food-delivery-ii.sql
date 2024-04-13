# Write your MySQL query statement below
select round(sum(if (order_Date = customer_pref_delivery_date, 1,0))*100/(select count(distinct customer_id)from delivery),2) as immediate_percentage
from delivery d
where (customer_id,order_date) in (select customer_id, min(order_date) from delivery group by customer_id);
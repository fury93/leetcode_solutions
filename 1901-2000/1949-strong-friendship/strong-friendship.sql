# Write your MySQL query statement below
with cte as(select user1_id,user2_id from friendship
            union 
            select user2_id,user1_id from friendship)
            
select c1.user1_id
      ,c2.user1_id as user2_id
	  ,count(*) as common_friend 
from cte as c1 
     join 
	 cte as c2
on c1.user1_id<c2.user1_id 
   and 
   c1.user2_id=c2.user2_id
where (c1.user1_id,c2.user1_id) 
in (select * from friendship)
group by 1,2
having count(*)>=3
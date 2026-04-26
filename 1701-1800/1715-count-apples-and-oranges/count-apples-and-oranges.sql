# Write your MySQL query statement below
select 
sum(boxes.apple_count + COALESCE(Chests.apple_count, 0)) as apple_count,
sum(boxes.orange_count + COALESCE(Chests.orange_count, 0)) as orange_count
from boxes left join Chests
on boxes.chest_id = chests.chest_id
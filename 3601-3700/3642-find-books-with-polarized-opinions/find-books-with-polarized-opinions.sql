# Write your MySQL query statement below
select 
b.book_id as book_id,
title,
author,
genre,
pages,
max(session_rating) - min(session_rating) as rating_spread,
round(sum(case when session_rating <= 2 or session_rating >= 4 then 1 else 0 end)/count(1), 2) as polarization_score
from
books b join reading_sessions r on b.book_id = r.book_id
group by b.book_id
having count(*) >= 5 and min(session_rating) <= 2 and max(session_rating) >= 4
order by polarization_score desc, title desc
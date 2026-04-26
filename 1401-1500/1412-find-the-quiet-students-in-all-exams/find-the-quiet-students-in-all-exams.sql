# Write your MySQL query statement below
Select e.student_id, s.student_name from 
Exam e, student s,
(Select max(score) as high, min(score) as low, exam_id from Exam
group by exam_id) r
where 
	e.student_id = s.student_id 
	and e.exam_id = r.exam_id 
group by e.student_id, s.student_name
having sum(Case when e.score = r.high then 1 else 0 end) =0 and
sum(Case when e.score = r.low then 1 else 0 end)= 0 
order by e.student_id
# Write your MySQL query statement below
# Approach 1: Window Function
-- SELECT 
--   student_id, 
--   course_id, 
--   grade 
-- FROM 
--   (
--     SELECT 
--       student_id, 
--       course_id, 
--       grade, 
--       DENSE_RANK() OVER (
--         PARTITION BY student_id 
--         ORDER BY 
--           grade DESC, 
--           course_id ASC
--       ) AS rnk 
--     FROM 
--       Enrollments
--   ) AS ranked 
-- WHERE 
--   rnk = 1 
-- ORDER BY 
--   student_id;

# Approach 2: Aggregation & Self-Join
-- SELECT 
--   e1.student_id, 
--   MIN(e1.course_id) AS course_id, 
--   e1.grade 
-- FROM 
--   Enrollments e1 
--   JOIN (
--     SELECT 
--       student_id, 
--       MAX(grade) AS max_grade 
--     FROM 
--       Enrollments 
--     GROUP BY 
--       student_id
--   ) e2 ON e1.student_id = e2.student_id 
--   AND e1.grade = e2.max_grade 
-- GROUP BY 
--   e1.student_id, 
--   e1.grade 
-- ORDER BY 
--   e1.student_id;

# Approach 3: Subquery with Aggregation
SELECT 
  student_id, 
  MIN(course_id) AS course_id, 
  grade 
FROM 
  Enrollments 
WHERE 
  (student_id, grade) IN (
    SELECT 
      student_id, 
      MAX(grade) 
    FROM 
      Enrollments 
    GROUP BY 
      student_id
  ) 
GROUP BY 
  student_id, 
  grade 
ORDER BY 
  student_id;
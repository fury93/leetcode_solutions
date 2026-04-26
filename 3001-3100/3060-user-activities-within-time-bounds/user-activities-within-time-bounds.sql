# Write your MySQL query statement below
SELECT 
  DISTINCT a.user_id 
FROM 
  (
    SELECT 
      s1.user_id, 
      s1.session_type, 
      s1.session_end, 
      LEAD(s1.session_start) OVER(
        PARTITION BY s1.user_id, 
        s1.session_type 
        ORDER BY 
          s1.session_start
      ) AS next_session_start 
    FROM 
      Sessions s1
  ) a 
WHERE 
  a.next_session_start IS NOT NULL 
  AND TIMESTAMPDIFF(
    HOUR, a.session_end, a.next_session_start
  ) <= 12;
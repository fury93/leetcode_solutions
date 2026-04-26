# Write your MySQL query statement below
WITH cte AS (
SELECT user_id, COUNT(prompt) OVER(partition by user_id) prompt_count, ROUND(AVG(tokens) OVER(partition by user_id),2) avg_tokens,
MAX(tokens) OVER(partition by user_id) max_tokens
FROM prompts)
SELECT DISTINCT user_id, prompt_count, avg_tokens
FROM cte
WHERE prompt_count > 2 AND max_tokens > avg_tokens
ORDER BY avg_tokens DESC, user_id;
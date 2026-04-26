# Write your MySQL query statement below

WITH RECURSIVE content_sep_words AS (
    SELECT
        content_id,
        content_text,
        SUBSTRING_INDEX(content_text, ' ', 1) AS word,
        SUBSTRING(content_text, INSTR(content_text, ' ') + 1, 1000) AS remaining,
        1 AS level
        from user_content
    UNION ALL
    SELECT 
        content_id,
        content_text,
        SUBSTRING_INDEX(remaining, ' ', 1),
        IF(INSTR(remaining, ' ') = 0, '', SUBSTRING(remaining, INSTR(remaining, ' ') + 1, 1000)),
        level + 1
    FROM content_sep_words
    WHERE remaining != ''
),
content_sep_words_capitalized as (
    select content_id,
    content_text,
    level as word_seq,
    word,
    CONCAT(upper(substring(WORD, 1, 1)), lower(substring(WORD, 2, 1000))) as formatted_word
    from content_sep_words
)
select
content_id,
content_text as original_text,
group_concat(formatted_word order by word_seq separator ' ') as converted_text
from content_sep_words_capitalized
group by 1, 2
order by 1
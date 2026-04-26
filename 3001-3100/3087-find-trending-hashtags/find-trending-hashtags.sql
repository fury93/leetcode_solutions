# Write your MySQL query statement below
SELECT REGEXP_SUBSTR(tweet,'\#[a-zA-Z]+') HASHTAG,COUNT(*) HASHTAG_COUNT FROM Tweets
WHERE DATE_FORMAT(tweet_date,'%Y-%m')='2024-02'
GROUP BY 1
ORDER BY 2 DESC,1 DESC
LIMIT 3
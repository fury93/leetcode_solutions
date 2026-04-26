# Write your MySQL query statement below
-- Common Table Expression (CTE) to calculate monthly income and compare with max_income
WITH MonthlyIncome AS (
  SELECT 
    t.account_id, 
    DATE_FORMAT(t.day, '%Y%m') AS income_month, 
    -- Format transaction date to 'YYYYMM'
    SUM(t.amount) AS monthly_income, 
    -- Calculate total income for the month
    a.max_income -- Include max_income from Accounts table
  FROM 
    Transactions t 
    LEFT JOIN Accounts a ON a.account_id = t.account_id -- Join with Accounts table
  WHERE 
    t.type = 'Creditor' -- Consider only 'Creditor' transactions
  GROUP BY 
    t.account_id, 
    income_month 
  HAVING 
    SUM(t.amount) > a.max_income -- Filter months where income exceeds max_income
    ) -- Final query to find accounts with excessive income for two consecutive months
SELECT 
  Income1.account_id 
FROM 
  MonthlyIncome Income1, 
  MonthlyIncome Income2 
WHERE 
  Income1.account_id = Income2.account_id -- Compare the same account
  AND PERIOD_DIFF(
    Income1.income_month, Income2.income_month
  ) = 1 -- Check for consecutive months
GROUP BY 
  Income1.account_id 
ORDER BY 
  Income1.account_id;
# Write your MySQL query statement below
WITH CTE AS(
    SELECT user_id, COUNT(contact_email) AS contacts_cnt,
            SUM(IF(contact_email IN (SELECT email FROM Customers), 1, 0)) AS trusted_contacts_cnt
    FROM Contacts
    GROUP BY user_id)

SELECT invoice_id, cs.customer_name, price, 
        IFNULL(contacts_cnt, 0) AS contacts_cnt, 
        IFNULL(trusted_contacts_cnt, 0) AS trusted_contacts_cnt
FROM Invoices i 
LEFT JOIN CTE c ON i.user_id = c.user_id
LEFT JOIN Customers cs ON i.user_id = cs.customer_id
ORDER BY invoice_id
-- SELECT 
--   I.invoice_id, 
--   Cust.customer_name, 
--   I.price, 
--   COUNT(DISTINCT C.contact_name) AS contacts_cnt, 
--   COUNT(DISTINCT Nme.customer_name) AS trusted_contacts_cnt 
-- FROM 
--   Invoices I 
--   LEFT JOIN Customers Cust ON I.user_id = Cust.customer_id 
--   LEFT JOIN Contacts C ON C.user_id = Cust.customer_id 
--   LEFT JOIN Customers Nme ON Nme.customer_name = C.contact_name 
-- GROUP BY 
--   I.invoice_id
# Write your MySQL query statement below
SELECT 
    a.name as customer_name,a.customer_id,
    b.order_id,
    b.order_date
FROM Customers as a
JOIN Orders as b
ON a.customer_id=b.customer_id
JOIN Orders as c
ON b.customer_id=c.customer_id AND b.order_date<=c.order_date
GROUP BY a.customer_id,b.order_id
HAVING COUNT(c.order_date)<=3
ORDER BY customer_name,customer_id,order_date DESC;
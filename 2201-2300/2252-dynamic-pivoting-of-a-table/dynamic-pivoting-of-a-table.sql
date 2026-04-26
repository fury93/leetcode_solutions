CREATE PROCEDURE PivotProducts()
BEGIN

#Override GROUP_CONCAT length which has a default limit of 1024
SET SESSION group_concat_max_len = 1000000;

#Store case statement for dynamically generated columns in a variable ie case_stmt
SET @case_stmt = NULL;
SELECT GROUP_CONCAT(DISTINCT CONCAT('SUM(CASE WHEN store = "', store, '" THEN price END) AS ', store))
INTO @case_stmt
FROM products;
 
#Insert above statement (@case_stmt) in the following main query to frame final query 
SET @sql_query = CONCAT('SELECT product_id, ', @case_stmt, ' FROM products GROUP BY product_id');

#Execute final query
PREPARE final_sql_query FROM @sql_query;
EXECUTE final_sql_query;
DEALLOCATE PREPARE final_sql_query;

END
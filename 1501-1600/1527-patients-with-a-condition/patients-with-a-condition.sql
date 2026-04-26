# Write your MySQL query statement below
# Approach 1: Using Regular Expression Word Boundaries or Spaces
SELECT patient_id, patient_name, conditions
FROM Patients
WHERE conditions REGEXP '(^|[[:space:]])DIAB1';

# Approach 2: Without Using Regular Expressions
-- SELECT patient_id, patient_name, conditions
-- FROM Patients
-- WHERE conditions LIKE 'DIAB1%' OR conditions LIKE '% DIAB1%';
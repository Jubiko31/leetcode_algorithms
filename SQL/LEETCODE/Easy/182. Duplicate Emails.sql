--- Write an SQL query to report all the duplicate emails. Note that it's guaranteed that the email field is not NULL.

/* Write your PL/SQL query statement below */
SELECT email
FROM Person 
GROUP BY email
HAVING COUNT(*) > 1;

-- Runtime: 39.90% | Memory: 100.00%
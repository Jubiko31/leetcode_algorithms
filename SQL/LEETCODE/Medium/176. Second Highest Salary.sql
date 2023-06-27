-- Find the second highest salary from the Employee table. If there is no second highest salary, return null.

/* Write your T-SQL query statement below */
SELECT 
    CASE
        WHEN (SELECT COUNT(*) FROM Employee) < 2 THEN NULL
        WHEN (SELECT COUNT(DISTINCT salary) FROM Employee) = 1 THEN NULL
        ELSE 
            (SELECT MIN(salary)
             FROM (SELECT DISTINCT TOP 2 salary
                   FROM Employee
                   ORDER BY salary DESC) AS SecondHighestSalary)
    END AS SecondHighestSalary;


-- Runtime: 38.34% | Memory: 100.00%
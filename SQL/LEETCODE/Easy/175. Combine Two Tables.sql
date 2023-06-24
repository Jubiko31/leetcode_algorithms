-- Write an SQL query to report the first name, last name, city, and state of each person in the Person table. If the address of a personId is not present in the Address table, report null instead.

SELECT Person.lastName, Person.firstName, Address.city, Address.state
FROM Person
LEFT JOIN Address ON Person.personId = Address.personId



-- Runtime: 33.62% | Memory: 100.00%
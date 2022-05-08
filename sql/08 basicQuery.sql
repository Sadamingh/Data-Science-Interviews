-- https://www.hackerrank.com/challenges/revising-the-select-query/problem?isFullScreen=true

SELECT *
FROM CITY
WHERE population > 100000
AND CountryCode = 'USA';

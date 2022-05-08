/*
https://www.hackerrank.com/challenges/weather-observation-station-8/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
*/

SELECT DISTINCT CITY
FROM STATION
WHERE LEFT(CITY, 1) IN ("a", "e", "i", "o", "u")
AND RIGHT(CITY, 1) IN ("a", "e", "i", "o", "u")

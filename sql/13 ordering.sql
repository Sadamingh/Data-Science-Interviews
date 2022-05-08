/*
https://www.hackerrank.com/challenges/weather-observation-station-5/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
*/

SELECT CITY, LENGTH(CITY) as len
FROM STATION
ORDER BY len, CITY
LIMIT 1;

SELECT CITY, LENGTH(CITY) as len
FROM STATION
ORDER BY len DESC
LIMIT 1;

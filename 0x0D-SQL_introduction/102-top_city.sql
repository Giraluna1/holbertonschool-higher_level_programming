-- this script display the top 3 of cities temperature
-- during July and Agust ordered Decending
SELECT city, AVG(value) 'avg_temp' FROM temperatures
WHERE month
BETWEEN 7
AND 8
GROUP BY city
ORDER BY avg_temp DESC LIMIT 3;

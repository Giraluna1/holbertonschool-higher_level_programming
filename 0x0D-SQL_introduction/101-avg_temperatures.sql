-- This script display the average temperature
-- (Farenheit) by city ordered by temperature decresing
SELECT city, AVG(value) 'avg_temp'
FROM temperatures
GROUP BY city
ORDER by avg_temp DESC;

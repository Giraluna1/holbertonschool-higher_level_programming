-- This script display the max temperatue of each state
-- order by state name
SELECT state, MAX(value) 'max_value' FROM temperatures
GROUP BY state
ORDER BY state;

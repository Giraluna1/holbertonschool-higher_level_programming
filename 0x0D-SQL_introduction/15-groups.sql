-- This script lists the numbes of records with
-- the same score in the scond table
SELECT score COUNT(score) 'number', score
FROM second_table
GROUP BY score
ORDER BY score DESC;

-- This script lists the numbes of records with
-- the same score in the scond table
SELECT score AS "score",
    COUNT(score) AS 'number'
FROM second_table
GROUP BY score
ORDER BY score DESC;

-- This script lists all records with score >= 10
-- in the secon table, ordered by score
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
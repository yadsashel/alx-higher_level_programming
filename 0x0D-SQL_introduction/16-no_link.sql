-- Script to list all records with a name value in second_table

-- List all records with a name value, ordered by descending score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;


-- Script to list all records with a score >= 10 from second_table

-- List all records with score >= 10 ordered by score (top first)
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;


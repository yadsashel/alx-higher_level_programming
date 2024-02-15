-- Use the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Retrieve the id of California from the states table
SET @california_id := (SELECT id FROM states WHERE name = 'California');

-- Query to select all cities of California
SELECT * 
FROM cities 
WHERE state_id = @california_id
ORDER BY id ASC;

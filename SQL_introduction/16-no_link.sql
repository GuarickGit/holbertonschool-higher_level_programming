-- Script that lists all records of the table second_table with non-empty names
-- List score and name from second_table where name is not null or empty, ordered by score descending
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;

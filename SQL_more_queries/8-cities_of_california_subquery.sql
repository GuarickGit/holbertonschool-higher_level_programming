-- Script that lists all the cities of California from the database hbtn_0d_usa
-- Retrieves cities where the state is California, sorted by cities.id

SELECT id, name FROM cities
WHERE state_id = (
    SELECT id FROM states WHERE name = 'California'
)
ORDER BY id ASC;

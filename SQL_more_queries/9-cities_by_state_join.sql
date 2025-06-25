-- Lists all cities along with their state name
-- Using a JOIN to match each city with its corresponding state
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;

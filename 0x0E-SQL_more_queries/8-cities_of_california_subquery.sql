-- 8-list_cities_of_california.sql
-- Script to list all cities of California from the database

-- Select cities where the state_id matches the id of California in the states table
SELECT cities.id, cities.name
FROM cities, states
WHERE states.name = 'California' AND cities.state_id = states.id
ORDER BY cities.id ASC;


-- 9-list_all_cities.sql
-- Script to list all cities with their state names from the database

-- Select cities.id, cities.name, and states.name, sorting by cities.id
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;


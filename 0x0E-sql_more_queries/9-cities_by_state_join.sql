-- a script to select data from 2 databases using join
SELECT cities.id, cities.name, states.name FROM cities JOIN states ON (states.id=cities.state_id)
ORDER BY cities.id ASC;
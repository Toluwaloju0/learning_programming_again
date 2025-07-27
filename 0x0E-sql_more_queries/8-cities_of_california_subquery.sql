-- A script to select id and names from a database
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE states.name LIKE  'California');
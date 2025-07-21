-- a script to select rows with names from a database table
SELECT score, name FROM second_table WHERE name NOT LIKE '' OR name IS NOT NULL;
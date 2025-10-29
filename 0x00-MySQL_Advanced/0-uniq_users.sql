-- A script to create a new table in any database
CREATE TABLE IF NOT EXISTS users (
    id INTEGER NOT NULL AUTO INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);

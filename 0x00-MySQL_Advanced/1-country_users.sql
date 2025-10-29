-- a script to create a table called users
CREATE TABLE IF NOT EXITS users (
    id INT NOT NULL AUTO INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM("US", "CO", "TN") NOT NULL DEFAULT "US"
);

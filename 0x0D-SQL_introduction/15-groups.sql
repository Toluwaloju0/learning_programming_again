-- a script to get the count of scores in a database table
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score;
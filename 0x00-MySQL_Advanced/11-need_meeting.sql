-- a script to create a view

CREATE VIEW need_meeting AS SELECT name from students WHERE students.score < 80 AND (DATEDIFF(NOW(), students.last_meeting) >= 30 OR students.last_meeting IS NULL);
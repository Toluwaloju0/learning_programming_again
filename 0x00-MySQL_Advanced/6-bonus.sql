-- a script to create a stored procedure
DELIMITER //
CREATE PROCEDURE addBonus (user_id INT, project_name VARCHAR(255), score INT) BEGIN
    SET @project_id = (SELECT id FROM projects WHERE projects.name = project_name);
     if @project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET @project_id = LAST_INSERT_ID();
        INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, @project_id, score);
    ELSE
        UPDATE corrections SET score = score WHERE user_id = user_id AND project_id = @project_id;
    END IF;
END //

DELIMITER ;

-- a function to compute the average score of a user

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser (user_id INT) BEGIN
    UPDATE users SET average_score = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = user_id) WHERE users.id = user_id;
END //
DELIMITER ;
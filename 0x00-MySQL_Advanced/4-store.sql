-- a script to create a trigger

DELIMITER //
CREATE TRIGGER IF NOT EXISTS quantity_add AFTER INSERT ON orders FOR EACH ROW
BEGIN
    UPDATE items SET items.quantity = items.quantity - NEW.number WHERE items.name = NEW.item_name;
END //
DELIMITER ;
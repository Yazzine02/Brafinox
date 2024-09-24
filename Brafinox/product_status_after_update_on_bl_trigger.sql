DELIMITER //
CREATE TRIGGER update_product_status_after_bl_update
AFTER UPDATE ON inventory_bl
FOR EACH ROW
BEGIN
    IF NEW.amount_paid >= NEW.total_price THEN
        UPDATE inventory_sell
        SET status = 'completed'
        WHERE bl_id = NEW.bl_code;
    END IF;
END;
//
DELIMITER ;

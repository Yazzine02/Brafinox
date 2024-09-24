delimiter //
create trigger update_bl_on_payment
after insert on inventory_payment
for each row
begin
update inventory_bl
set amount_paid = amount_paid + NEW.amount, payment_status = IF(amount_paid >= total_price, 'completed', 'pending')
where bl_code = NEW.bl_id;
end;
//
delimiter ;
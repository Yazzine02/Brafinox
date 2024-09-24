delimiter //
create trigger update_stock_on_sale
after insert on inventory_sell
for each row
begin
declare current_stock int;
select stock_unit into current_stock from inventory_product where id =NEW.product_id;
if current_stock < NEW.quantity then
signal SQLSTATE '45000'
set MESSAGE_TEXT = 'Stock insuffisant pour cette vente';
else
update inventory_product
set stock_unit = stock_unit - NEW.quantity
where id = NEW.product_id;
end if;
end;
//
delimiter ;
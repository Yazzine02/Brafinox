delimiter //
create trigger update_stock_on_buy
after insert on inventory_buy
for each row
begin
update inventory_product
set stock_unit = stock_unit + NEW.quantity
where id = NEW.product_id;
end;
//
delimiter ;
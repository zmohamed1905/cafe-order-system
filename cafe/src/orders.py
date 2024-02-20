from colorama import Fore,Back,Style
from products import get_drinks_from_db
from couriers import get_couriers_list_from_db

def add_order_to_db(curr,connection_v):
    customer_name = input("What is the Customer name?\n")
    customer_address = input("What is the customer's address?\n")
    customer_num = input("What is the customers number?\n")
    get_couriers_list_from_db(curr)
    courier_num = int(input("What is the courier number?\n"))
    order_status = 1
    get_drinks_from_db(curr)
    items = int(input("What product item number would you like?\n"))
    sql = "INSERT INTO `orders` (`customer_name`, `customer_address`, `customer_phone`, `courier`, `order_status`, `items`) VALUES (%s, %s, %s, %s, %s, %s)"
    curr.execute(sql, (customer_name, customer_address, customer_num, courier_num, order_status, items))
    connection_v.commit() 
    
def get_orders_list_from_db(curr):
    sql = "SELECT * FROM orders"
    curr.execute(sql)
    result = curr.fetchall()
    for row in result:
        print(f'Order ID: {row[0]}, Customer Name: {row[1]}, Customer Address: {row[2]}, Customer Number: {row[3]}, Courier: {row[4]}, Order Status: {row[5]}, Items: {row[6]}\n')
        
def delete_order_from_db(curr,connection_v):
    order_to_delete = int(input("What order number would you like to delete?\n"))
    sql = "DELETE FROM orders WHERE order_id=%s"
    curr.execute(sql, (order_to_delete))
    connection_v.commit()
    
def update_order_in_db(curr,connection_v):
    try:
        order_to_update = int(input("What order number would you like to update?\n"))
        customer_name = input("\nWhat would you like to change the customer name to? (Space + Enter to skip)\n")
        if customer_name != ' ':
            sql = "UPDATE orders SET customer_name=%s WHERE order_id=%s"
            curr.execute(sql,(customer_name,order_to_update))
            connection_v.commit()
        
        customer_address = input("\nWhat would you like to change the customer address to? (Space + Enter to skip)\n")
        if customer_address != ' ':
            sql = "UPDATE orders SET customer_address=%s WHERE order_id=%s"
            curr.execute(sql,(customer_address,order_to_update))
            connection_v.commit()
            
        customer_phone = input("\nWhat would you like to change the customer phone number to? (Space + Enter to skip)\n")
        if customer_phone != ' ':
            sql = "UPDATE orders SET customer_phone=%s WHERE order_id=%s"
            curr.execute(sql,(customer_phone,order_to_update))
            connection_v.commit()
            
        courier = input("\nWhat would you like to change the courier number to? (Space + Enter to skip)\n")
        if courier != ' ':
            sql = "UPDATE orders SET courier=%s WHERE order_id=%s"
            curr.execute(sql,(courier,order_to_update))
            connection_v.commit()
        
        item = int(input("\nWhat would you like to chage the order item to? (0 to skip)\n"))
        if item != 0:
            sql = "UPDATE orders SET items=%s WHERE order_id=%s"
            curr.execute(sql,(item,order_to_update))
            connection_v.commit()
    
    except ValueError as ve:
        print(Fore.RED + f"Please Enter a Valid Input: {ve}")
        print(Style.RESET_ALL)
        
        
def update_order_status(curr,connection_v):
    try:
        order_status_to_update = int(input("What order number would you like to update?\n"))
        print('1: preparing\n2: out for delivery\n3: delivered\n')
        
        what_to_change_to = int(input("What would you like to change the order status number to?\n"))
        sql = "UPDATE orders SET order_status=%s WHERE order_id=%s"
        curr.execute(sql,(what_to_change_to,order_status_to_update))
        connection_v.commit()
    
    except ValueError as ve:
        print(Fore.RED + f"Please Enter a Valid Input: {ve}")
        print(Style.RESET_ALL)
    
    
def get_order_info(curr):
    sql = "SELECT orders.order_id,orders.customer_name,order_status.order_status FROM orders INNER JOIN order_status ON orders.order_status = order_status.order_status_id ORDER BY orders.order_id ASC"
    curr.execute(sql)
    result = curr.fetchall()
    for row in result:
        print(f'Order ID: {row[0]}, Order Name: {row[1]}, Order Status: {row[2]}\n')
    
def get_order_status(curr):
    sql = "SELECT * FROM order_status"
    curr.execute(sql)
    result = curr.fetchall()
    for row in result:
        print(f'{row[0]}, {row[1]}\n')
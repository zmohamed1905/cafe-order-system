from colorama import Fore,Back,Style

def add_courier_to_db(curr,connection_v):
    to_insert = input("What courier would you like to add?\n")
    courier_num = input("What is the courier number?\n")
    sql = "INSERT INTO `couriers` (`courier_name`, `courier_number`) VALUES (%s, %s)"
    curr.execute(sql, (to_insert, courier_num))
    connection_v.commit() 
    
def get_couriers_list_from_db(curr):
    sql = "SELECT * FROM couriers"
    curr.execute(sql)
    result = curr.fetchall()
    for row in result:
        print(f'Courier ID: {row[0]}, Courier Name: {row[1]}, Courier Number: {row[2]}\n')
        
def delete_courier_from_db(curr,connection_v):
    courier_to_delete = int(input("What courier number would you like to delete?\n"))
    sql = "DELETE FROM couriers WHERE courier_id=%s"
    curr.execute(sql, (courier_to_delete))
    connection_v.commit()
    
    
def update_courier_in_db(curr,connection_v):
    try:
        courier_to_update = int(input("What courier number would you like to update?\n"))
        courier_name = input("\nWhat would you like to change the courier name to? (Space + Enter to skip)\n") 
        if courier_name != ' ':
            sql = "UPDATE couriers SET courier_name=%s WHERE courier_id=%s"
            curr.execute(sql,(courier_name,courier_to_update))
            connection_v.commit()
        
        courier_number = input("\nWhat would you like to change the courier number to? (Space + Enter to skip)\n")
        if courier_number != ' ':
            sql = "UPDATE couriers SET courier_number=%s WHERE courier_id=%s"
            curr.execute(sql,(courier_number, courier_to_update))
            connection_v.commit()
        
    except ValueError as ve:
        print(Fore.RED + f"Please Enter a Valid Input: {ve}")
        print(Style.RESET_ALL)
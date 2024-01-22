orders = []

orders_status = []


menu = ['Americano','Hot Chocolate','Green Tea','Coke','Fanta','Water']


main_menu = {
                '0':'Exit App',
                '1':'Show Products Menu Options',
                '2':'Show Orders Menu Options',
                '3':'Show Couriers Menu Options',
}

options_menu = {
                    '0':'Return to Main Menu',
                    '1':'Print Products List',
                    '2':'Create New Product',
                    '3':'Update Existing Product',
                    '4':'Delete Product'
    
}


products_options ={
                    '0':'Return to Main Menu',
                    '1':'Print Orders List',
                    '2':'Create New Order',
                    '3':'Update Existing Order Status',
                    '4':'Update Existing Order',
                    '5':'Delete Order'
    
}


couriers_options ={
                    '0':'Return to Main Menu',
                    '1':'Print Couriers List',
                    '2':'Create New Courier',
                    '3':'Update Existing Courier',
                    '4':'Delete Courier',
    
}


def greeting() -> str:
    print("\nWelcome to Zak's Cafe!\n")
    
def show_main_menu():
    for key,value in main_menu.items():
        print(key,value)   

def show_options_menu():
    for key,value in options_menu.items():
        print(key,value)
        
        
def show_orders_options():
    for key,value in products_options.items():
        print(key,value)

def show_menu():
    for item in menu:
        print(item)
        
def show_couriers_menu():
    for key,value in couriers_options.items():
        print(key,value) 
        
def add_item(item_to_add):
    menu.append(item_to_add)
    
def update_item():
    update_product = int(input("What item number you like to update?\n"))
    new_item = input("What would you like to update it to?\n")
    menu[update_product] = new_item
    print(menu)
    
    
def delete_item():
    item_to_delete = input("\nWhat item would you like to delete from the menu?\n")
    menu.remove(item_to_delete)
    
    
def show_drinks_with_index():
    for index, drink in enumerate(menu):
        print(index,drink)
        
def show_orders_with_index():
    for index, order in enumerate(orders):
        print(index,order)
        

def create_new_customer():
    new_customer = {}
    new_customer["customer_name"] = input("\nEnter customer name: ")
    new_customer["customer_address"] = input("\nEnter customer address: ")
    new_customer["customer_number"] = input("\nEnter customer number: ")
    new_customer["order_status"] = 'PREPARING'
    
    return new_customer

def update_existing_order():
    show_orders_with_index()
    to_update = int(input("What order number would you like to change?\n"))
    user_key = input("What would you like to change in this order?\n")
    user_val = input("What would you like to change this to?\n")

    try :
        orders[to_update][user_key] = user_val
        
    except KeyError as ke:
        print(f"{ke}: Please enter a valid key!")
    

def update_existing_order_status():
    show_orders_with_index()
    user_index = int(input("What order number would you like to update?\n"))
    new_status = input("What status would you like to set this to?\n")
    orders[user_index]['order_status'] = new_status
    
    

def delete_existing_order():
    user_index = int(input("What order number would you like to delete?\n"))
    orders.pop(user_index)
    
    
def get_couriers_list():
    couriers_list = []
    with open('couriers.txt', 'r') as file:
        data = file.readlines()
        for line in data:
            couriers_list.append(line.strip())
            
    print(couriers_list)
    
    
def create_new_courier():
    new_courier = input("What courier would you like to add?\n")
    with open('couriers.txt', 'a') as file:
        file.write('\n'+ new_courier)
        
        
def get_products_list():
    products_list = []
    with open('products.txt', 'r') as file:
        data = file.readlines()
        for line in data:
            products_list.append(line.strip())
            
    print(products_list)
             
    
def welcome():
    greeting()
    show_main_menu()
    

while True:
    welcome()
    user_choice = str(input("\nWhat option number would you like?\n"))
    if user_choice == '0':
        exit()
        
    elif user_choice == '1':
        show_options_menu()
        user_option = input("\nWhat option would you like?\n")
        
        if user_option == '0':
            show_main_menu()
        
        elif user_option == '1':
            # show_menu()
            get_products_list()
            
        elif user_option == '2':
            new_product=input("What would you like to add to the menu?\n")
            add_item(item_to_add=new_product)
            print(menu)
            
        elif user_option == '3':
            show_drinks_with_index()
            update_item()
        

        elif user_option == '4':
            show_drinks_with_index()
            delete_item()
            
    
    elif user_choice == '2':
        show_orders_options()
        new_user_choice = input("\nWhat option would you like next?\n")
        if new_user_choice == '0':
            show_main_menu()
            
        elif new_user_choice == '1':
            print(orders)
            
        elif new_user_choice == '2':
            entry = create_new_customer()
            orders.append(entry)
            print(orders)
            
        elif new_user_choice == '3':
            update_existing_order_status()
            
            
        elif new_user_choice == '4':
            update_existing_order()
        
            
        elif new_user_choice == '5':
            show_orders_with_index()
            delete_existing_order()
            
            
    elif user_choice == '3':
        show_couriers_menu()
        new_user_choice = input("\nWhat option number would you like?\n")
        
        if new_user_choice == '0':
            show_main_menu()
            
        elif new_user_choice == '1':
            get_couriers_list()
            
        elif new_user_choice == '2':
            create_new_courier()
            get_couriers_list()
            
        elif new_user_choice == '3':
            pass
            
            
        elif new_user_choice == '4':
            pass
        
    else:
        print("Please Enter a valid option number!")
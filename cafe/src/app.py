import os
from dotenv import load_dotenv
import pymysql
from products import *
from couriers import *
from orders import *


load_dotenv()
host_name = os.environ.get("mysql_host")
database_name = os.environ.get("mysql_db")
user_name = os.environ.get("mysql_user")
user_password = os.environ.get("mysql_pass")

connection_v = pymysql.connect(
            host = host_name,
            database = database_name,
            user = user_name,
            password = user_password
        )
curr = connection_v.cursor()

orders = []

orders_status = []

products_list = []

couriers_list = []


main_menu = {
                '0':'Exit App',
                '1':'Show Products Menu Options',
                '2':'Show Orders Menu Options',
                '3':'Show Couriers Menu Options',
}

product_menu = {
                    '0':'Return to Main Menu',
                    '1':'Print Products List',
                    '2':'Create New Product',
                    '3':'Update Existing Product',
                    '4':'Delete Product'
    
}


order_menu ={
                    '0':'Return to Main Menu',
                    '1':'Print Orders List',
                    '2':'Create New Order',
                    '3':'Update Existing Order Status',
                    '4':'Update Existing Order',
                    '5':'Delete Order'
    
}


couriers_menu ={
                    '0':'Return to Main Menu',
                    '1':'Print Couriers List',
                    '2':'Create New Courier',
                    '3':'Update Existing Courier',
                    '4':'Delete Courier',
    
}


def greeting() -> str:
    print("\nWelcome to Zak's Cafe!\n")
    
def show_menu(menu):
    for key,value in menu.items():
        print(key,value)
        
        

def welcome():
    greeting()
    show_menu(main_menu)
    
    
while True:
    welcome()
    user_choice = str(input("\nWhat option number would you like?\n"))
    if user_choice == '0':
        print("Thanks for visiting Zak's Cafe!")
        curr.close()
        exit()
        
    elif user_choice == '1':
        while True:
            show_menu(product_menu)
            user_option = input("\nWhat option would you like?\n")
            
            if user_option == '0':
                break
            
            elif user_option == '1':
                get_prod_list_from_db(curr)
                  
                
            elif user_option == '2':
                get_prod_list_from_db(curr)
                add_product_to_db(curr,connection_v)

                
                
            elif user_option == '3':
                get_prod_list_from_db(curr)
                update_product_in_db(curr, connection_v)
            

            elif user_option == '4':
                delete_product_from_db(curr,connection_v)
            
    
    elif user_choice == '2':
        while True:
            show_menu(order_menu)
            new_user_choice = input("\nWhat option would you like next?\n")
            if new_user_choice == '0':
                break
                
            elif new_user_choice == '1':
                get_orders_list_from_db(curr)
                     
                
            elif new_user_choice == '2':
                add_order_to_db(curr, connection_v)
                
            elif new_user_choice == '3':
                get_order_info(curr)
                update_order_status(curr,connection_v)
                
                
            elif new_user_choice == '4':
                 get_orders_list_from_db(curr)
                 update_order_in_db(curr,connection_v)
            
                
            elif new_user_choice == '5':
                get_orders_list_from_db(curr)
                delete_order_from_db(curr,connection_v)
            
            
    elif user_choice == '3':
        while True:
            show_menu(couriers_menu)
            new_user_choice = input("\nWhat option number would you like?\n")
            
            if new_user_choice == '0':
                break
                
            elif new_user_choice == '1': 
                get_couriers_list_from_db(curr)

              
            elif new_user_choice == '2':
                get_couriers_list_from_db(curr)
                add_courier_to_db(curr,connection_v)
                
            elif new_user_choice == '3':
                get_couriers_list_from_db(curr)
                update_courier_in_db(curr,connection_v)
                
                
            elif new_user_choice == '4':
               get_couriers_list_from_db(curr)
               delete_courier_from_db(curr,connection_v)
            
    else:
        print("Please Enter a valid option number!")
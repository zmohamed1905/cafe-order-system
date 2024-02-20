from colorama import Fore,Back,Style

def add_product_to_db(curr,connection_v):
    to_insert = input("What product would you like to add?\n")
    prod_price = float(input("What is the price of the new prodcut?\n"))
    sql = "INSERT INTO `products` (`product_name`, `product_price`) VALUES (%s, %s)"
    curr.execute(sql, (to_insert, prod_price))
    connection_v.commit()
    
def get_prod_list_from_db(curr):
    sql = "SELECT * FROM products"
    curr.execute(sql)
    result = curr.fetchall()
    for row in result:
        print(f'Product ID: {row[0]}, Product Name: {row[1]}, Product Price {row[2]}\n')
        
def get_drinks_from_db(curr):
    sql = "SELECT product_id, product_name FROM products"
    curr.execute(sql)
    result = curr.fetchall()
    for row in result:
        print(f'{row[0]}: {row[1]}\n')
    
def delete_product_from_db(curr,connection_v):
    product_to_delete = int(input("What product number would you like to delete?\n"))
    sql = "DELETE FROM products WHERE product_id=%s"
    curr.execute(sql, (product_to_delete))
    connection_v.commit()
    
def update_product_in_db(curr,connection_v):
    try:
        product_to_update = int(input("What product number would you like to update?\n"))
        product_name = input("\nWhat would you like to change the product name to? (Space + Enter to skip)\n")
        if product_name != ' ':
            sql = "UPDATE products SET product_name=%s WHERE product_id=%s"
            curr.execute(sql,(product_name,product_to_update))
            connection_v.commit()
        
        product_price= float(input("\nWhat would you like to change the product price to? (0 to skip)\n"))
        if product_price != 0:
            sql = "UPDATE products SET product_price=%s WHERE product_id=%s"
            curr.execute(sql,(product_price,product_to_update))
            connection_v.commit()
    except ValueError as ve:
        print(Fore.RED + f"Please Enter a Valid Input: {ve}")
        print(Style.RESET_ALL)
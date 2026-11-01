from database import connection
# database connection established

connection()

from customers import Customers
from sales import Sales
from products import Products


def main_menu():
    while True:
        print("1. Customer Management")
        print("2. Product Management")
        print("3. Sales Management")
        print("4. Exit Application")
        choice=input("Enter your choice: ")

        if choice=='1':
            Customers().customer_menu()
        elif choice=='2':
            Products().product_menu()
        elif choice=='3':
            Sales().sale_menu()
        elif choice=='4':
            print("Exiting Application...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__=="__main__":
    main_menu()
    
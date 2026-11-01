import psycopg2
from database import connection


conn=connection()
class Customers:
    def __init__(self):
        pass# self.name = name
        # self.contact = contact
    @staticmethod
    def create_table():
        cur=conn.cursor()
        cur.execute(
            """CREATE TABLE IF NOT EXISTS customer(
            id serial primary key,
            name varchar(100) not null,
            contact varchar(15) not null
            )"""
        )
        conn.commit()
        cur.close()
    @staticmethod
    def insert_customer(name,contact):
        
        cur=conn.cursor()
        cur.execute(
            """INSERT INTO customer (name,contact)
            values(%s,%s)""",(name,contact),
              )
              
        conn.commit()
        cur.close()
    @staticmethod
    def update_customer(customer_id,name=None,contact=None):
        
        cur=conn.cursor()
        cur.execute("SELECT * FROM CUSTOMER WHERE id=%s",(customer_id,))
        customer=cur.fetchone()
        if not customer:
            print(">>>>>>Customer not found !")
            cur.close()
            return
        update_fields=[]
        params=[]
        if name not in (None,''):
            update_fields.append("name=%s")
            params.append(name)
        if contact not in (None,''):
            update_fields.append("contact=%s")
            params.append(contact)
        if not update_fields:
            cur.close()
            return
        params.append(customer_id)
        update_query=f"UPDATE customer SET {','.join(update_fields)} WHERE id=%s"
        cur.execute(update_query,params)
        conn.commit()
        cur.close()
    @staticmethod
    def delete_customer(customer_id):
        
        cur=conn.cursor()
        cur.execute(
            "DELETE FROM CUSTOMER WHERE id =%s",(customer_id,)
        )
        conn.commit()
        cur.close()
    @staticmethod
    def get_all_customers():
        
        cur=conn.cursor()
        cur.execute(
           "select * from customer")
        customers=cur.fetchall()

        cur.close()
        return customers
    @staticmethod
    def customer_menu():
        
        while True:
            print("1. Create Table")
            print("2. Insert customer")
            print("3. Update customer")
            print("4. Delete customer")
            print("5. View customers")
            print("6. Exit customer menu")
            choice=input("Enter your choice: ")
            if choice=='1':
                Customers().create_table()
                print(">>>>>Table created successfully !")
            elif choice=='2':
                name=input("enter customer name: ")
                contact=input("enter customer contact: ")
                Customers().insert_customer(name,contact)
                print(">>>>>Customer inserted successfully !")
            elif choice=='3':
                customer_id=input("Enter customer id:")
                name=input("enter customer name: ")
                contact=input("enter customer contact: ")
                Customers().update_customer(customer_id,name,contact)
                print(">>>>>Customer updated successfully !")
            elif choice=='4':
                customer_id=input("Enter customer id: ")
                Customers().delete_customer(customer_id)
                print(">>>>>Customer deleted successfully !")
            elif choice=='5':
                customers=Customers().get_all_customers()
                print(customers)
            elif choice=='6':
                break   
            else:
                print("Invalid choice,Please try again !")


#Customers().customer_menu()
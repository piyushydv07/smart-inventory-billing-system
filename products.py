from database import connection
conn=connection()

class Products:
    def __init__(self):
        pass
    # self.name = name
        # self.contact = contact
    @staticmethod
    def create_table():
        
        cur=conn.cursor()
        cur.execute(
            """CREATE TABLE IF NOT EXISTs products(
            id serial primary key,
            name varchar(100) not null,
            description text not null,
            price decimal(10,2) not null,
            quantity int not null
            )"""
        )
        conn.commit()
        cur.close()
    @staticmethod
    def insert_product(name,description,price,quantity):
        
        cur=conn.cursor()
        cur.execute(
            """INSERT INTO products (name,description,price,quantity)
            values(%s,%s,%s,%s)""",(name,description,price,quantity),
              )
              
        conn.commit()
        cur.close()


    @staticmethod
    def update_product(product_id,name=None,description=None,price=None,quantity=None):
        
        cur=conn.cursor()
        cur.execute("SELECT * FROM products WHERE id=%s",(product_id,))
        products=cur.fetchone()
        if not products:
            print(">>>>>>product not found !")
            cur.close()
            return products
        update_fields=[]
        params=[]
        if name not in (None,''):
            update_fields.append("name=%s")
            params.append(name)
        if description not in (None,''):
            update_fields.append("description=%s")
            params.append(description)
        if price not in (None,''):
            update_fields.append("price=%s")
            params.append(price)
        # 0 is a valid quantity (last unit sold), so only skip None and blank input
        if quantity not in (None,''):
            update_fields.append("quantity=%s")
            params.append(quantity)
        if not update_fields:
            cur.close()
            return
        params.append(product_id)
        update_query=f"UPDATE products SET {','.join(update_fields)} WHERE id=%s"
        cur.execute(update_query,params)
        conn.commit()
        cur.close()
    @staticmethod
    def delete_product(product_id):
        
        cur=conn.cursor()
        cur.execute(
            "DELETE FROM products WHERE id =%s",(product_id,)
        )
        conn.commit()
        cur.close()
    @staticmethod
    def get_all_products():
        
            cur=conn.cursor()
            cur.execute(
               "select * from products")
            products=cur.fetchall()

            cur.close()
            return products

    @staticmethod
    def get_all_products_id(product_id):
        
            cur=conn.cursor()
            cur.execute(
                "select * from products where id=%s",(product_id,))
            products=cur.fetchone()
    
            cur.close()
            return products
    @staticmethod
    def product_menu():
        
        while True:
            print("1. Create Table")
            print("2. Insert product")
            print("3. Update product")
            print("4. Delete product")
            print("5. View product")
            print("6. View all products")
            print("7. Exit product menu")
            choice=input("Enter your choice: ")
            if choice=='1':
                Products().create_table()
                print(">>>>>Table created successfully !")
            elif choice=='2':
                name=input("enter products name: ")
                description=input("enter products description: ")
                price=input("enter products price: ")
                quantity=input("enter products quantity: ")
                Products().insert_product(name,description,price,quantity)
                print(">>>>>products inserted successfully !")
            elif choice=='3':
                products_id=input("Enter products id:")
                name=input("enter products name: ")
                description=input("enter products description: ")
                price=input("enter products price: ")
                quantity=input("enter products quantity: ")
                Products().update_product(products_id,name,description,price,quantity)
                print(">>>>>products updated successfully !")
            elif choice=='4':
                products_id=input("Enter products id: ")
                Products().delete_product(products_id)
                print(">>>>>products deleted successfully !")
            elif choice=='5':
                products_id=input("Enter products id: ")
                product=Products().get_all_products_id(products_id)
                print(product)
            elif choice=='6':
                products=Products().get_all_products()
                print(products)
            elif choice=='7':
                break   
            else:
                print("Invalid choice,Please try again !")


#Products().product_menu()
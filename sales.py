from database import connection
conn=connection()
class Sales:
    def __init__(self):
        pass
    # self.name = name
        # self.contact = contact
    @staticmethod
    def create_table():
        
        cur=conn.cursor()
        cur.execute(
            """CREATE TABLE IF NOT EXISTs sales(
            id serial primary key,
            customer_id integer not null,
            date date not null,
            total_amount decimal(10,2) not null,
            constraint fk_sales_customer foreign key (customer_id) references customer(id) on delete cascade
            )"""
        )
        conn.commit()
        cur.close()
    @staticmethod
    def insert_sale(customer_id,date,total_amount):
        cur=conn.cursor()
        cur.execute(
            """INSERT INTO sales (customer_id,date,total_amount)
            values(%s,%s,%s)""",(customer_id,date,total_amount),
              )
              
        conn.commit()
        cur.close()


    @staticmethod
    def update_sale(sale_id,customer_id=None,date=None,total_amount=None):
        
        cur=conn.cursor()
        cur.execute("SELECT * FROM sales WHERE id=%s",(sale_id,))
        sales=cur.fetchone()
        if not sales:
            print(">>>>>>sale not found !")
            cur.close()
            return sales
        update_fields=[]
        params=[]
        if customer_id not in (None,''):
            update_fields.append("customer_id=%s")
            params.append(customer_id)
        if date not in (None,''):
            update_fields.append("date=%s")
            params.append(date)
        if total_amount not in (None,''):
            update_fields.append("total_amount=%s")
            params.append(total_amount)
        if not update_fields:
            cur.close()
            return
        params.append(sale_id)
        update_query=f"UPDATE sales SET {','.join(update_fields)} WHERE id=%s"
        cur.execute(update_query,params)
        conn.commit()
        cur.close()
    @staticmethod
    def delete_sale(sale_id):
        
        cur=conn.cursor()
        cur.execute(
            "DELETE FROM sales WHERE id =%s",(sale_id,)
        )
        conn.commit()
        cur.close()
    @staticmethod
    def get_all_sales():
        
            cur=conn.cursor()
            cur.execute(
               "select * from sales")
            sales=cur.fetchall()

            cur.close()
            return sales
    @staticmethod
    def get_all_sales_id(sale_id):
        
            cur=conn.cursor()
            cur.execute(
               "select * from sales where id=%s",(sale_id,))
            sales=cur.fetchall()

            cur.close()
            return sales

    @staticmethod
    def generate_bill(sale_id):
        
            cur=conn.cursor()
            cur.execute(
                "select * from sales where id=%s",(sale_id,))
            res=cur.fetchone()
            if res:
                return res[3]
            else:
                return 0
            cur.close()
            return total_amount
#  Analytical query
    @staticmethod
    def get_total_sales_by_date(start_date,end_date):
        
        cor=conn.cursor()
        cor.execute(
             "select sum(total_amount) from sales where date between %s and %s",(start_date,end_date,)
         )
        total_sales=cor.fetchone()
        cor.close()
        return total_sales
    @staticmethod
    def get_top_selling_products():
        
        cor=conn.cursor()
        cor.execute(
             """select product_id,sum(quantity) as total_quantity from salesitem
               group by product_id
               order by total_quantity desc
               limit 5""",
        )
        total_products=cor.fetchall()
        cor.close()
        return total_products
    @staticmethod
    def get_sales_by_customer(customer_id):
        
        cor=conn.cursor()
        cor.execute(
             "select * from sales where customer_id=%s",(customer_id,)
         )
        sales=cor.fetchall()
        cor.close()
        return sales


    @staticmethod
    def sale_menu():
        
        while True:
            
            print("1. Create Table")
            print("2. Insert sale")
            print("3. Update sale")
            print("4. Delete sale")
            print("5. View sale")
            print("6. View all sales")
            print("7. Generate bill")
            print("8. total sales by date")
            print("9. top 5 selling products")
            print("10. sales by customer")
            print("11. Exit sale menu")
            choice=input("Enter your choice: ")
            
            if choice=='1':
                Sales().create_table()
                print(">>>>>Table created successfully !")
            
            elif choice=='2':
                customer_id=input("enter customer id: ")
                date=input("enter Sale date: ")
                total_amount=input("enter sale total amount: ")
                Sales().insert_sale(customer_id,date,total_amount)
                print(">>>>>sales inserted successfully !")
            
            elif choice=='3':
                sales_id=input("Enter sales id:")
                customer_id=input("enter customer id: ")
                date=input("enter sale date: ")
                total_amount=input("enter sale total amount: ")
                Sales().update_sale(sales_id,customer_id,date,total_amount)
                print(">>>>>sales updated successfully !")
            
            elif choice=='4':
                sales_id=input("Enter sales id: ")
                Sales().delete_sale(sales_id)
                print(">>>>>sales deleted successfully !")
            
            elif choice=='5':
                sales_id=input("Enter sales id: ")
                saless=Sales().get_all_sales_id(sales_id)
                print(saless)
            
            elif choice=='6':
                salesss=Sales().get_all_sales()
                print(salesss)
            
            elif choice=='7':
                sales_id=input("Enter sales id: ")
                total_amount=Sales().generate_bill(sales_id)
                print(f"Total amount for sale id {sales_id} is {total_amount}")
            
            elif choice=='8':
                start_date=input("Enter start date(YYYY-MM-DD): ")
                end_date=input("Enter end date (YYYY-MM-DD): ")
                salessss=Sales().get_total_sales_by_date(start_date,end_date)
                print(salessss)
            
            elif choice=='9':
                top=Sales().get_top_selling_products()
                print(top)
            
            elif choice=='10':
                customer_id=input("Enter customer id: ")
                sales=Sales().get_sales_by_customer(customer_id)
                print(sales)
            
            elif choice=='11':
                break   
            else:
                print("Invalid choice,Please try again !")


#Sales().sale_menu()
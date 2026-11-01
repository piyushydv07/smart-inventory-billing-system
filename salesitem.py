from database import connection 
con=connection()

class salesitem():
    @staticmethod
    def create_table():
        cur=con.cursor()
        cur.execute(
            """create table if not exists salesitem(
            id serial primary key,
            sale_id integer  not null,
            product_id integer not null,
            quantity integer not null check(quantity>0),
            price decimal(10,2) not null check(price>=0),
            CONSTRAINT fk_salesitems_sales FOREIGN KEY (sale_id) REFERENCES sales(id) ON DELETE CASCADE,
            CONSTRAINT k_salesitems_products FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE


            )"""

        )
        con.commit()
        cur.close()
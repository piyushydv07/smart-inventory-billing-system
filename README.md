# Smart Inventory and Billing System

A Python and PostgreSQL application for managing customers, products and sales, with billing and sales reports. It comes with a Streamlit web interface and a command-line menu version.

<!-- Add screenshots here, for example docs/dashboard.png and docs/bill.png -->

## Features

- **Customers:** add, view, update and delete customers.
- **Products:** add, view, update and delete products, with price and stock quantity.
- **Sales:** create a sale for a customer, add items to it, and finish it to calculate the total. Adding an item reduces the product's stock.
- **Billing:** generate an itemised bill for any sale.
- **Analytics and reports** (Streamlit app):
  - Sales summary with a daily sales trend chart
  - Sales by date range
  - Top selling products (bar chart)
  - Low stock alert (products with fewer than 10 units)
  - Customer purchase history

## Tech stack

- Python 3
- PostgreSQL, accessed with `psycopg2`
- Streamlit for the web interface

## Setup

1. Install PostgreSQL and create a database:

   ```sql
   CREATE DATABASE ecommerce;
   ```

2. Clone the repo and install the dependencies:

   ```bash
   git clone https://github.com/piyushydv07/smart-inventory-billing-system.git
   cd smart-inventory-billing-system
   python -m venv venv
   source venv/bin/activate        # on Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Configure the database connection. Copy `.env.example` to `.env` and put in your own PostgreSQL password:

   ```bash
   cp .env.example .env
   ```

4. Run the web app. It creates all the tables on first run:

   ```bash
   streamlit run app.py
   ```

   Or use the command-line version:

   ```bash
   python main.py
   ```

   Run the Streamlit app at least once first, because it is what creates the `salesitem` table that the billing and top-products reports use.

## Project structure

```
app.py          Streamlit web interface (dashboard, management pages, reports)
main.py         Command-line menu version
database.py     PostgreSQL connection (reads settings from environment variables)
customers.py    Customer table and operations
products.py     Product table and operations
sales.py        Sales table, operations and report queries
salesitem.py    Line items of each sale
```

## Database tables

| Table | Columns |
| --- | --- |
| `customer` | id, name, contact |
| `products` | id, name, description, price, quantity |
| `sales` | id, customer_id (FK), date, total_amount |
| `salesitem` | id, sale_id (FK), product_id (FK), quantity, price |

## Known limitations

- No login or user roles.
- No automated tests yet.
- The modules share one database connection each, which a larger version would replace with a connection pool.

## Author

Piyush Yadav, B.Tech CSE (AIML), J.C. Bose University of Science and Technology, YMCA.

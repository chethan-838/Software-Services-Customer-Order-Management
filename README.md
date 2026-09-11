# Software Services Customer Order Management Control

**Technology:** Python 3.13/3.14 + MySQL 8  
**Database:** `Sales_customers_database_management`

This project implements all programs listed in the supplied Python Project 1 specification:
1. Add 10 salespeople through Python
2. Add 7 customers through Python
3. Display all salespeople
4. Increase salesperson incentive/commission by Rs. 1500.55
5. Display all customers
6. Display customers in London, Bengaluru, Paris or Mumbai
7. Store 9 orders
8. Display all orders
9. Simple calculator using user-defined Python functions

## Setup

1. Install MySQL 8 and create/start the MySQL server.
2. Open `src/db_config.py` and enter your MySQL username/password.
3. Install the Python dependency:
   ```bash
   pip install -r requirements.txt
   ```
4. Run `sql/schema.sql` in MySQL Workbench or MySQL Shell.
5. Run the scripts from the project root, for example:
   ```bash
   python src/01_add_salespeople.py
   python src/02_add_customers.py
   python src/03_display_salespeople.py
   python src/04_increase_incentive.py
   python src/05_display_customers.py
   python src/06_filter_customers.py
   python src/07_add_orders.py
   python src/08_display_orders.py
   python src/09_calculator.py
   ```

## Important
The scripts use parameterized SQL queries and commit database changes. Running an insert script more than once may cause duplicate primary-key errors. If you want a clean run, recreate the database using `sql/schema.sql`.

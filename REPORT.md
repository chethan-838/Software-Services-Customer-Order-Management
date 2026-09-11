# PROJECT REPORT
## Software Services Customer Order Management Control Project

### 1. Purpose of the Project

The purpose of this project is to develop a Python and MySQL based customer order management system for a software services company. The system maintains salesperson, customer and order information in a relational database and provides Python scripts for inserting, updating, filtering and displaying records.

### 2. Advantage of the Project for the Company

- Centralizes salesperson, customer and order information.
- Reduces manual data-entry work.
- Makes customer and order information easier to retrieve.
- Maintains relationships between salespeople, customers and orders.
- Supports basic reporting through Python scripts.
- Uses MySQL for structured and persistent data storage.
- Uses Python automation for database operations.
- Foreign keys help maintain data consistency.

### 3. Software Used

- Python 3.13 / 3.14
- MySQL 8
- MySQL Workbench or MySQL Shell
- VS Code / another Python IDE
- `mysql-connector-python`

### 4. Database

Database name:

`Sales_customers_database_management`

### 5. Tables

#### Salespeople — Master Table

| Column | Type | Key | Description |
|---|---|---|---|
| Snum | INT | Primary Key | Salesperson number |
| sname | VARCHAR(100) | | Salesperson name |
| city | VARCHAR(100) | | Salesperson city |
| comm | DECIMAL(10,2) | | Incentive/commission |

#### Customer — Child Table

| Column | Type | Key | Description |
|---|---|---|---|
| cnum | INT | Primary Key | Customer number |
| cname | VARCHAR(100) | | Customer name |
| city | VARCHAR(100) | | Customer city |
| snum | INT | Foreign Key | Assigned salesperson |

#### Order — Child Table

| Column | Type | Key | Description |
|---|---|---|---|
| onum | INT | Primary Key | Order number |
| odate | DATE | | Order date |
| oamount | DECIMAL(12,2) | | Order amount |
| cnum | INT | Foreign Key | Customer number |
| snum | INT | Foreign Key | Salesperson number |

### 6. Python Programs

**Q1:** `01_add_salespeople.py` adds 10 salesperson records.

**Q2:** `02_add_customers.py` adds 7 customer records.

**Q3:** `03_display_salespeople.py` displays all salespeople.

**Q4:** `04_increase_incentive.py` increases the incentive/commission by Rs. 1500.55.

**Q5:** `05_display_customers.py` displays all customers.

**Q6:** `06_filter_customers.py` displays customers staying in London, Bengaluru, Paris or Mumbai.

**Q7:** `07_add_orders.py` stores 9 customer orders.

**Q8:** `08_display_orders.py` displays all orders.

**Q9:** `09_calculator.py` implements a simple calculator using user-defined functions.

### 7. Conclusion

The project demonstrates practical use of Python database programming with MySQL. It covers database creation, relational tables, primary and foreign keys, insert operations, update operations, filtering, joins and a function-based Python calculator.

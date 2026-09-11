Software Services Customer Order Management System

A Python and MySQL based customer order management project designed to manage salespeople, customers, and orders efficiently.

📌 Project Overview

The Software Services Customer Order Management System is developed using Python and MySQL.

The project manages:

- Salespeople
- Customers
- Customer orders
- Salesperson incentives
- Customer location filtering
- Basic calculations

The Python programs connect to a MySQL database to insert, update, retrieve, and display business data.

🎯 Purpose of the Project

The purpose of this project is to develop a simple database-driven application for managing salespeople, customers, and customer orders.

It demonstrates how Python can be integrated with MySQL to perform database operations in a real-world business scenario.

🚀 Features

- Add 10 salespeople
- Add 7 customers
- Display all salespeople
- Increase salesperson incentive by ₹1500.55
- Display all customers
- Filter customers by city
- Add 9 customer orders
- Display all orders
- Simple calculator using user-defined Python functions
- MySQL database connectivity using Python

🛠️ Technologies Used

- Python 3.12
- MySQL 8
- mysql-connector-python
- MySQL Workbench
- Python IDLE
- Git
- GitHub

🗄️ Database

Database name:

Sales_customers_database_management

Tables

1. "Salespeople"
2. "customer"
3. "order"

Salespeople Table

Stores salesperson information such as:

- Salesperson number
- Name
- City
- Incentive/commission

Customer Table

Stores customer information such as:

- Customer number
- Customer name
- City
- Salesperson number

Order Table

Stores order information such as:

- Order number
- Order date
- Order amount
- Customer number
- Salesperson number

📂 Project Structure

Software_Services_Customer_Order_Management/
│
├── README.md
├── REPORT.md
├── requirements.txt
│
├── sql/
│   └── schema.sql
│
└── src/
    ├── db_config.py
    ├── common.py
    ├── 01_add_salespeople.py
    ├── 02_add_customers.py
    ├── 03_display_salespeople.py
    ├── 04_increase_incentive.py
    ├── 05_display_customers.py
    ├── 06_filter_customers.py
    ├── 07_add_orders.py
    ├── 08_display_orders.py
    └── 09_calculator.py

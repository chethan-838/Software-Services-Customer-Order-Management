from common import get_connection, close_connection

salespeople = [
    (101, "Arun", "Bengaluru", 5000.00),
    (102, "Priya", "Mumbai", 5500.00),
    (103, "Rahul", "Delhi", 6000.00),
    (104, "Sneha", "London", 6500.00),
    (105, "Vikram", "Paris", 5200.00),
    (106, "Anjali", "Bengaluru", 5800.00),
    (107, "Kiran", "Mumbai", 6200.00),
    (108, "Meena", "Chennai", 5400.00),
    (109, "Ravi", "Hyderabad", 5700.00),
    (110, "Neha", "Pune", 6100.00),
]

connection = cursor = None
try:
    connection = get_connection()
    cursor = connection.cursor()
    sql = """
        INSERT INTO Salespeople (Snum, sname, city, comm)
        VALUES (%s, %s, %s, %s)
    """
    cursor.executemany(sql, salespeople)
    connection.commit()
    print(f"{cursor.rowcount} salespeople records inserted successfully.")
except mysql.connector.Error as e:
    if connection:
        connection.rollback()
    print("Database error:", e)
finally:
    close_connection(cursor, connection)

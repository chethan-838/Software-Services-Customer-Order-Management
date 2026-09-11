from common import get_connection, close_connection

customers = [
    (201, "Amit", "London", 104),
    (202, "Divya", "Bengaluru", 101),
    (203, "John", "Paris", 105),
    (204, "Rohan", "Mumbai", 102),
    (205, "Kavya", "Chennai", 108),
    (206, "Daniel", "London", 104),
    (207, "Pooja", "Bengaluru", 106),
]

connection = cursor = None
try:
    connection = get_connection()
    cursor = connection.cursor()
    sql = """
        INSERT INTO customer (cnum, cname, city, snum)
        VALUES (%s, %s, %s, %s)
    """
    cursor.executemany(sql, customers)
    connection.commit()
    print(f"{cursor.rowcount} customers inserted successfully.")
except mysql.connector.Error as e:
    if connection:
        connection.rollback()
    print("Database error:", e)
finally:
    close_connection(cursor, connection)

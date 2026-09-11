from common import get_connection, close_connection

orders = [
    (301, "2026-07-01", 12500.00, 201, 104),
    (302, "2026-07-02", 18500.50, 202, 101),
    (303, "2026-07-03", 22000.00, 203, 105),
    (304, "2026-07-04", 15750.75, 204, 102),
    (305, "2026-07-05", 9900.00, 205, 108),
    (306, "2026-07-06", 27500.25, 206, 104),
    (307, "2026-07-07", 16400.00, 207, 106),
    (308, "2026-07-08", 31200.00, 202, 101),
    (309, "2026-07-09", 11800.00, 204, 102),
]

connection = cursor = None
try:
    connection = get_connection()
    cursor = connection.cursor()
    sql = """
        INSERT INTO `order` (onum, odate, oamount, cnum, snum)
        VALUES (%s, %s, %s, %s, %s)
    """
    cursor.executemany(sql, orders)
    connection.commit()
    print(f"{cursor.rowcount} orders inserted successfully.")
except mysql.connector.Error as e:
    if connection:
        connection.rollback()
    print("Database error:", e)
finally:
    close_connection(cursor, connection)

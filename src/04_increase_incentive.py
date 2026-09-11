from common import get_connection, close_connection

INCREASE = 1500.55

connection = cursor = None
try:
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE Salespeople SET comm = comm + %s",
        (INCREASE,)
    )
    connection.commit()
    print(f"Incentive increased by Rs. {INCREASE:.2f} for {cursor.rowcount} salespeople.")
except Exception as e:
    if connection:
        connection.rollback()
    print("Database error:", e)
finally:
    close_connection(cursor, connection)

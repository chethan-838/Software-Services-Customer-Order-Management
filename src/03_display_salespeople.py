from common import get_connection, close_connection

connection = cursor = None
try:
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT Snum, sname, city, comm FROM Salespeople ORDER BY Snum")
    rows = cursor.fetchall()

    print("\n--- ALL SALESPEOPLE ---")
    print(f"{'Snum':<8}{'Name':<15}{'City':<15}{'Incentive':>12}")
    print("-" * 50)
    for row in rows:
        print(f"{row[0]:<8}{row[1]:<15}{row[2]:<15}{float(row[3]):>12.2f}")
finally:
    close_connection(cursor, connection)

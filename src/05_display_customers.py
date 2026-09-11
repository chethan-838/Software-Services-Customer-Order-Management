from common import get_connection, close_connection

connection = cursor = None
try:
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT c.cnum, c.cname, c.city, c.snum, s.sname
        FROM customer c
        JOIN Salespeople s ON c.snum = s.Snum
        ORDER BY c.cnum
    """)
    rows = cursor.fetchall()

    print("\n--- ALL CUSTOMERS ---")
    print(f"{'Cnum':<8}{'Name':<15}{'City':<15}{'Snum':<8}{'Salesperson':<15}")
    print("-" * 65)
    for r in rows:
        print(f"{r[0]:<8}{r[1]:<15}{r[2]:<15}{r[3]:<8}{r[4]:<15}")
finally:
    close_connection(cursor, connection)

from common import get_connection, close_connection

connection = cursor = None
try:
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT o.onum, o.odate, o.oamount,
               c.cname, s.sname
        FROM `order` o
        JOIN customer c ON o.cnum = c.cnum
        JOIN Salespeople s ON o.snum = s.Snum
        ORDER BY o.onum
    """)
    rows = cursor.fetchall()

    print("\n--- ALL ORDERS ---")
    print(f"{'Order':<8}{'Date':<13}{'Amount':>12}  {'Customer':<15}{'Salesperson':<15}")
    print("-" * 68)
    for r in rows:
        print(f"{r[0]:<8}{str(r[1]):<13}{float(r[2]):>12.2f}  {r[3]:<15}{r[4]:<15}")
finally:
    close_connection(cursor, connection)

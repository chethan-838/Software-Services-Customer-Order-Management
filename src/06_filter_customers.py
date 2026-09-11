from common import get_connection, close_connection

cities = ("London", "Bengaluru", "Paris", "Mumbai")

connection = cursor = None
try:
    connection = get_connection()
    cursor = connection.cursor()
    placeholders = ", ".join(["%s"] * len(cities))
    query = f"""
        SELECT cnum, cname, city, snum
        FROM customer
        WHERE city IN ({placeholders})
        ORDER BY city, cnum
    """
    cursor.execute(query, cities)
    rows = cursor.fetchall()

    print("\n--- CUSTOMERS IN LONDON / BENGALURU / PARIS / MUMBAI ---")
    for r in rows:
        print(f"Cnum: {r[0]}, Name: {r[1]}, City: {r[2]}, Salesperson No: {r[3]}")
finally:
    close_connection(cursor, connection)

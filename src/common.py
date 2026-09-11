import mysql.connector
from db_config import DB_CONFIG

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

def close_connection(cursor=None, connection=None):
    if cursor is not None:
        cursor.close()
    if connection is not None and connection.is_connected():
        connection.close()

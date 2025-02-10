import pymysql

try:
    print("Attempting to connect to MySQL with PyMySQL...")
    conn = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="root"
    )
    if conn.open:
        print("Connection successful!")
    else:
        print("Connection failed!")
except pymysql.MySQLError as err:
    print(f"MySQL Error: {err}")
except Exception as e:
    print(f"General Error: {e}")
finally:
    if 'conn' in locals() and conn.open:
        print("Closing connection...")
        conn.close()
    else:
        print("No connection to close.")
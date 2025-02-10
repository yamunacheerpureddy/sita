import pymysql

# Establishing the connection
conn = pymysql.connect(
    host='localhost',
    user='root',            # Use your MySQL username
    password='root',        # Use your MySQL password
)

# Check if the connection is successful
if conn.open:
    print("Connection successful!")
else:
    print("Connection failed!")

# Close the connection
conn.close()
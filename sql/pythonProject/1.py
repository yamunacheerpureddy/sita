#Program for Demonstrating How to obtain Connection from mySQL
#MySQLConnTestEx1.p
# -connector-python
import pymysql

try:
    # Connect to the database
    con = pymysql.connect(host='localhost',
                          user='root',
                          password='root')  # Use your actual password here

    print("Python Program Obtains Connection from MySQL")

    # Remember to close the connection when done
    con.close()

except pymysql.MySQLError as e:
    print("Problem in MySQL:", e)

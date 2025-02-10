#Program for Demonstrating How to obtain Connection from mySQL
#MySQLConnTestEx1.py
import mysql.connector
try:
    con=mysql.connector.connect(host="localhost",
                                user="root",
                                passwd="root",
                                auth_plugin='mysql_native_password')
    print("Python Program Obtains Connection from MySQL")
except mysql.connector.DatabaseError as d:
    print("Problem in MySQL :",d)
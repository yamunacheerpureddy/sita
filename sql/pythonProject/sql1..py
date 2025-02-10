import pymysql

try:
    conn = pymysql.connect(
        host="localhost",
        user="root",
        passwd="root"  # This should match the password you set
    )
    print("Python Program Obtains Connection from MySQL")
except pymysql.DatabaseError as d:
    print("Problem in MySQL:", d)

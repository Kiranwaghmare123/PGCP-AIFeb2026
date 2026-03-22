import mysql.connector

print("connection imported" )

conn = mysql.connector.connect(
    host="localhost",      # MySQL server name
    user="root",           # MySQL username
    password="cdac",    # MySQL password
    database="test_db"  # Database name
)

if conn.is_connected():
    print("Success....")
    
cursor = conn.cursor()

query = "update customer set course = %s where name=%s"
values = ("Java", "Ashi")

cursor.execute(query, values)
conn.commit()

conn.commit()


print("Data updated")

cursor.close()
conn.close()



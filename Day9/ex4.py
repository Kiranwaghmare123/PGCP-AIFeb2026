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

query = "delete from customer where name = %s"
values = ("Ashi",)

cursor.execute(query, values)
conn.commit()

print("Data deleted")

cursor.close()
conn.close()



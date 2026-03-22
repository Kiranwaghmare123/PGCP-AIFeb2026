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

query = "select * from customer"

cursor.execute(query)
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.commit()


print("Data displayed")

cursor.close()
conn.close()



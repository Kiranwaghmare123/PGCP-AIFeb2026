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

query = "insert into customer (name,age,course) values (%s, %s, %s)"

values = ("Ashi", 22, "Bigdata")

cursor.execute(query,values)
conn.commit()


print("Data inserted")

cursor.close()
conn.close()



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

query = """
CREATE TABLE IF NOT EXISTS customer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    course VARCHAR(100)
)

"""

cursor.execute(query)


print("Table created")

cursor.close()
conn.close()



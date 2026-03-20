import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="cdac",
    database="test_db"
)

cursor =conn.cursor()

query = """ 
CREATE TABLE IF NOT EXISTS employee (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    course VARCHAR(100)
)

"""
cursor.execute(query)

cursor.close()
conn.close()


print("Test data")
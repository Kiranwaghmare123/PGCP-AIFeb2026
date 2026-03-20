import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="cdac",
    database="test_db"
)

cursor = conn.cursor()

query = "INSERT INTO EMPLOYEE (NAME, AGE, COURSE) VALUES (%s, %s, %s)"

Values = ("Sahil", 27, "Python")

cursor.execute(query, Values)

conn.commit()

print("Record inserted successfully")


cursor.close()
conn.close()
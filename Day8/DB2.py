import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="cdac",
    database="test_db"
)

print("Test data")
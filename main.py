import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Yogi@2006",
    database="inventory_db"
)

print("Database Connected Successfully!")

conn.close()
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Yogi@2006",
    database="inventory_db"
)

cursor = conn.cursor()

print("PRODUCTS")
cursor.execute("SELECT * FROM products")
for row in cursor.fetchall():
    print(row)

print("\nTRANSACTIONS")
cursor.execute("SELECT * FROM stock_transactions")
for row in cursor.fetchall():
    print(row)

conn.close()
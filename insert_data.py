import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Yogi@2006",
    database="inventory_db"
)

cursor = conn.cursor()

sql = """
INSERT INTO stock_transactions
(product_id, transaction_date, transaction_type, quantity, supplier_id)
VALUES
(1, CURDATE(), 'IN', 20, 1),
(2, CURDATE(), 'IN', 50, 2),
(2, CURDATE(), 'OUT', 5, NULL)
"""

cursor.execute(sql)
conn.commit()

print("Data inserted successfully!")

conn.close()
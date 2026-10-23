import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Yogi@2006",
    database="inventory_db"
)

query = """
SELECT
    p.product_name,
    SUM(
        CASE
            WHEN s.transaction_type='IN'
            THEN s.quantity
            ELSE -s.quantity
        END
    ) AS current_stock
FROM products p
JOIN stock_transactions s
ON p.product_id=s.product_id
GROUP BY p.product_name
"""

df = pd.read_sql(query, conn)

plt.figure(figsize=(8,5))
plt.bar(df["product_name"], df["current_stock"])

plt.title("Current Stock Levels")
plt.xlabel("Product")
plt.ylabel("Quantity")

plt.show()

conn.close()
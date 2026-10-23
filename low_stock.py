import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Yogi@2006",
    database="inventory_db"
)

query = """
SELECT
    p.product_name,
    p.reorder_level,
    COALESCE(
        SUM(
            CASE
                WHEN s.transaction_type='IN'
                THEN s.quantity
                ELSE -s.quantity
            END
        ),0
    ) AS current_stock
FROM products p
LEFT JOIN stock_transactions s
ON p.product_id=s.product_id
GROUP BY p.product_id
"""

df = pd.read_sql(query, conn)

low_stock = df[df["current_stock"] < df["reorder_level"]]

print("\nLOW STOCK ITEMS\n")
print(low_stock)

conn.close()
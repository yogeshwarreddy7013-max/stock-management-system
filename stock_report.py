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
    p.product_id,
    p.product_name,
    p.unit_cost,
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
GROUP BY p.product_id,p.product_name,p.unit_cost
"""

df = pd.read_sql(query, conn)

df["inventory_value"] = df["current_stock"] * df["unit_cost"]

print("\nCURRENT STOCK REPORT\n")
print(df)

print("\nTOTAL INVENTORY VALUE:")
print(df["inventory_value"].sum())

conn.close()
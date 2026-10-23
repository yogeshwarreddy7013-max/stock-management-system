import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Yogi@2006",
    database="inventory_db"
)

cursor = conn.cursor()

# Clear tables
cursor.execute("DELETE FROM stock_transactions")
cursor.execute("DELETE FROM suppliers")
cursor.execute("DELETE FROM products")

# Reset auto increment
cursor.execute("ALTER TABLE stock_transactions AUTO_INCREMENT = 1")
cursor.execute("ALTER TABLE suppliers AUTO_INCREMENT = 1")
cursor.execute("ALTER TABLE products AUTO_INCREMENT = 1")

# Insert products
cursor.execute("""
INSERT INTO products
(sku, product_name, category, reorder_level, unit_cost)
VALUES
('P001','Laptop','Electronics',5,50000),
('P002','Mouse','Accessories',10,500)
""")

# Insert suppliers
cursor.execute("""
INSERT INTO suppliers (supplier_name)
VALUES
('TechSupplier'),
('OfficeMart')
""")

# Insert transactions
cursor.execute("""
INSERT INTO stock_transactions
(product_id, transaction_date, transaction_type, quantity, supplier_id)
VALUES
(1,CURDATE(),'IN',20,1),
(2,CURDATE(),'IN',50,2),
(2,CURDATE(),'OUT',5,NULL)
""")

conn.commit()

print("Database Reset Successfully!")

conn.close()
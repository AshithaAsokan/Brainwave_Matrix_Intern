import sqlite3

# Database connection
conn = sqlite3.connect('inventory.db')
cursor = conn.cursor()

# Create Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        quantity INTEGER NOT NULL
    )
''')
conn.commit()

# Function to Add Product
def add_product(name, quantity):
    cursor.execute('INSERT INTO products (name, quantity) VALUES (?, ?)', (name, quantity))
    conn.commit()
    return "Product added successfully"

# Function to Fetch All Products
def get_products():
    cursor.execute('SELECT * FROM products')
    return cursor.fetchall()

# Function to Update Product Quantity
def update_product(product_id, quantity):
    cursor.execute('UPDATE products SET quantity = ? WHERE id = ?', (quantity, product_id))
    conn.commit()
    return "Product updated successfully"

# Function to Delete Product
def delete_product(product_id):
    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
    conn.commit()
    return "Product deleted successfully"

# Close connection when done (if needed)
def close_connection():
    conn.close()

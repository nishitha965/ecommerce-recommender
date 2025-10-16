import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("ecommerce.db")
c = conn.cursor()

# Create products table
c.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT,
    price REAL
)
''')

# Create user behavior table
c.execute('''
CREATE TABLE IF NOT EXISTS user_behavior (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    product_id INTEGER,
    action TEXT  -- e.g., view, purchase, like
)
''')

conn.commit()
conn.close()
print("Database and tables created.")

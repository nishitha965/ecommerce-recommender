import sqlite3

conn = sqlite3.connect("ecommerce.db")
c = conn.cursor()

# Sample products
products = [
    (1, "Wireless Mouse", "Electronics", 25.0),
    (2, "Bluetooth Headphones", "Electronics", 50.0),
    (3, "Coffee Mug", "Kitchen", 10.0),
    (4, "Notebook", "Stationery", 5.0),
    (5, "Desk Lamp", "Electronics", 20.0),
    (6, "Water Bottle", "Kitchen", 15.0),
    (7, "Pen Set", "Stationery", 8.0),
    (8, "Smartphone Stand", "Electronics", 18.0)
]

c.executemany("INSERT OR IGNORE INTO products VALUES (?, ?, ?, ?)", products)

# Sample user behavior
user_behavior = [
    # User 1
    (1, 1, 1, "view"),
    (2, 1, 2, "purchase"),
    (3, 1, 4, "view"),

    # User 2
    (4, 2, 3, "view"),
    (5, 2, 4, "purchase"),
    (6, 2, 6, "view"),

    # User 3
    (7, 3, 2, "view"),
    (8, 3, 5, "purchase"),
    (9, 3, 8, "view")
]

c.executemany("INSERT OR IGNORE INTO user_behavior VALUES (?, ?, ?, ?)", user_behavior)

conn.commit()
conn.close()
print("Sample data for multiple users added.")

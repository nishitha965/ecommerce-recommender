import sqlite3

def recommend_products(user_id, top_n=3):
    conn = sqlite3.connect("ecommerce.db")
    c = conn.cursor()

    # Get favorite category of the user
    c.execute('''
        SELECT p.category, COUNT(*) as cnt
        FROM user_behavior ub
        JOIN products p ON ub.product_id = p.id
        WHERE ub.user_id = ?
        GROUP BY p.category
        ORDER BY cnt DESC
        LIMIT 1
    ''', (user_id,))
    result = c.fetchone()

    if result:
        favorite_category = result[0]
        # Recommend top products from that category
        c.execute('''
            SELECT id, name, category, price 
            FROM products
            WHERE category = ? 
            LIMIT ?
        ''', (favorite_category, top_n))
        recommendations = c.fetchall()
    else:
        # Fallback: recommend top products overall if user has no history
        c.execute('''
            SELECT id, name, category, price
            FROM products
            LIMIT ?
        ''', (top_n,))
        recommendations = c.fetchall()

    conn.close()
    return recommendations

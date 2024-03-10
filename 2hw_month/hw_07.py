import sqlite3

conn = sqlite3.connect("product.db")
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS product(
            id INTEGER PRIMARY KEY,
            product_title VARCHAR(200),
            price FLOAT NOT NULL DEFAULT 0.0,
            quantity INTEGER  NOT NULL DEFAULT 0
)''')

conn.commit()

into = 'INSERT INTO product (product_title,price, quantity) VALUES (?, ?, ?)'

values = ('Банан', 2.99, 10)

cur.execute(into, values)
conn.commit()
conn.close()
import sqlite3


def create_database():
    """Creates a SQLite database and populates it with sample product data."""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS Products (
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   category TEXT NOT NULL,
                   price REAL NOT NULL
                   )
                ''')

    cursor.execute('''
                   INSERT INTO Products (id, name, category, price)
                   VALUES
                   (1, 'Laptop', 'Electronics', 999.99),
                   (2, 'Smartphone', 'Electronics', 499.99)
                   ''')
    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_database()

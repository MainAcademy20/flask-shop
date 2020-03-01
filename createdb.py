import sqlite3

conn = sqlite3.connect('shop.db')

def create_product_table():
    query = """
    CREATE TABLE product (
        name VARCHAR(30),
        price DECIMAL)
    """
    conn.execute(query)
    conn.commit()


def create_user():
    query = """
    CREATE TABLE user (
        username VARCHAR(20),
        password_hash TEXT
    )
    """
    conn.execute(query)
    conn.commit()


if __name__ == '__main__':
    create_product_table()

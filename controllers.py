import sqlite3
from hashlib import sha256


def get_all_products():
    query = """
    SELECT name, price
    FROM product
    """
    conn = sqlite3.connect('shop.db')
    cursor = conn.execute(query)
    return cursor.fetchall()


def insert_item(item_name, item_price):
    query = """
    INSERT INTO product
    VALUES (?, ?)
    """
    conn = sqlite3.connect('shop.db')
    conn.execute(query, (item_name, item_price))
    conn.commit()


def exists_user(user):
    query = """
        SELECT 1
        FROM user
        WHERE username = ?
    """
    conn = sqlite3.connect('shop.db')
    cursor = conn.execute(query, (user, ))
    return bool(cursor.fetchall())


def register_user(user, password):
    sha = sha256()
    sha.update(password.encode('utf-8'))
    password_hash = sha.hexdigest()

    query = """
    INSERT INTO user
    VALUES (?, ?)
    """
    conn = sqlite3.connect('shop.db')
    conn.execute(query, (user, password_hash))
    conn.commit()

import sqlite3
from hashlib import sha256

from models import Product, User


def get_all_products():
    return Product.select()


def insert_item(item_name, item_price):
    Product.create(name=item_name, price=item_price)


def exists_user(user):
    return bool(User.get_or_none(username=user))


# def register_user(user, password):
#     sha = sha256()
#     sha.update(password.encode('utf-8'))
#     password_hash = sha.hexdigest()
#
#     query = """
#     INSERT INTO user
#     VALUES (?, ?)
#     """
#     conn = sqlite3.connect('shop.db')
#     conn.execute(query, (user, password_hash))
#     conn.commit()

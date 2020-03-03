from flask_login import UserMixin
from peewee import SqliteDatabase, Model, CharField, IntegerField

db = SqliteDatabase('shop.db')


class BaseModel(Model):
    class Meta:
        database = db


class Product(BaseModel):
    name = CharField()
    price = IntegerField()


class User(BaseModel, UserMixin):
    username = CharField(unique=True)
    password = CharField()
    def __repr__(self):
        return 'User <{}>'.format(self.username)
    def __str__(self):
        return 'User <{}>'.format(self.username)


if __name__ == '__main__':
    db.create_tables([Product, User])




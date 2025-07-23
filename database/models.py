from peewee import *

db = SqliteDatabase('database.db')

class BaseModel(Model):
    class Meta:
        database = db

class Client(BaseModel):
    id = PrimaryKeyField(default=1)
    name = CharField()
    phone = CharField()
    service = CharField()
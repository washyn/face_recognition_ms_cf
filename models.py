from global_variables import sqliteDbFileName
from peewee import *
import datetime
import uuid

from models import *

db = SqliteDatabase(sqliteDbFileName)


class BaseModel(Model):
    class Meta:
        database = db

# class User(BaseModel):
#     username = CharField(unique=True)

# class Tweet(BaseModel):
#     user = ForeignKeyField(User, backref='tweets')
#     message = TextField()
#     created_date = DateTimeField(default=datetime.datetime.now)
#     is_published = BooleanField(default=True)

class Student(BaseModel):
    fullName = CharField(unique=True)
    # personGuid = UUIDField()
    personGuid = CharField(unique=False)
    folderGuid = CharField(unique=False)

    # faceIdentifier = CharField(unique=False)
from global_variables import *
from peewee import *
import datetime
import uuid


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
    code = CharField(unique=True)
    personGuid = CharField(unique=False)
    folderGuid = CharField(unique=False)

    # personGuid = UUIDField()

    # faceIdentifier = CharField(unique=False)

    def __str__(self):
        return f"Full name:{self.fullName}\nCode:{self.code}\nPerson guid:{self.personGuid}\nFolder guid:{self.folderGuid}"
import datetime
from peewee import *
import sqlite3

DATABASE=SqliteDatabase('courses.sqlite')


class Course(Model):
    title = CharField()
    url = CharField(unique=True)
    created_at=DateTimeField(default=datetime.datetime.now)

    class meta:
        database = DATABASE

class Review(Model):
    course=ForeignKeyField(Course,related_name='review_set')
    rating=IntegerField()
    comment=TextField(default='')
    created_at=DateTimeField(datetime.datetime.now)

    class meta :
        database = DATABASE

def initalize():
    DATABASE.connect()
    DATABASE.create_tables([Course,Review],safe=True)
    DATABASE.close()
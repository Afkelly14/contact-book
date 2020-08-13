from peewee import *
from datetime import date

db = PostgresqlDatabase('contacts', user='postgres', password='',
                        host='localhost', port=5432)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Person(BaseModel):
    first_name = CharField()
    last_name = CharField()
    birthday = DateField()
    number = CharField()


db.create_tables([Person])

alex = Person(first_name='Alex', last_name='Kelly', birthday=date(1992, 6, 10), number='571-215-0235')
alex.save()

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


db.drop_tables([Person])
db.create_tables([Person])

# adding to the database
alex = Person(first_name='Alex', last_name='Kelly',
              birthday=date(1992, 6, 10), number='571-215-0235')
alex.save()

jeremiah = Person(first_name='Jeremiah', last_name='Scott',
                  birthday=date(1997, 9, 18), number='410-530-2569')
jeremiah.save()

michael = Person(first_name='Michael', last_name='Hall',
                 birthday=date(1985, 2, 20), number='616-308-2555')
michael.save()

wayne = Person(first_name='Wayne', last_name='Kelly',
               birthday=date(1955, 7, 16), number='571-214-0234')
wayne.save()

maggie = Person(first_name='Maggie', last_name='Kelly',
                birthday=date(1957, 6, 2), number='703-812-0909')
maggie.save()

sam = Person(first_name='Sam', last_name='Kelly',
             birthday=date(2018, 7, 4), number='703-281-3989')
sam.save()

harry = Person(first_name='Harry', last_name='Kelly',
               birthday=date(2018, 7, 4), number='703-281-3989')
harry.save()


def book():
    print(' 1: Contacts \n 2: Make Contact \n 3: Update Contact \n 4: Delete Contact \n 5: Exit')
    selection = int(input('enter category: '))
    if selection == 1:
        showContacts()
    elif selection == 2:
        createContact()
    elif selection == 3:
        updateContact()
    elif selection == 4:
        deleteContact()
    else:
        exit()

# show all the contacts
def showContacts():
    contacts = Person.select()
    for contact in contacts:
        print(
            f'Full Name: {contact.first_name} {contact.last_name} \n Birthday: {contact.birthday} \n Phone Number: {contact.number}')


book()

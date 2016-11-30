# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


# def test_add_Contact(app):
#     old_contact = app.contact.get_Contact_list()
#     addContact = BookContact(firstname="Алексей", middlename="Иларионовна", lastname="Баранцев", work="суперпрепод", address="Не дом и не улица", mobile='8915223344')
#     app.contact.add_Contact(addContact)
#     assert len(old_contact) + 1 == app.contact.count()
#     old_contact.append(addContact)
#     new_Contact = app.contact.get_Contact_list()
#     assert sorted(old_contact, key=BookContact.id_or_max) == sorted(new_Contact, key=BookContact.id_or_max)

def random_string(prefix, maxlen):
    #symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname=firstname, \
                    middlename=random_string("", 10), \
                    work=random_string("", 10), \
                    mobile=random_string("", 10), \
                    address=random_string("", 10), \
                    lastname=random_string("", 10))
            for firstname in ["", random_string("", 10)]
            for address in ["", random_string("", 10)]
]

#testdata = [Contact(firstname=" Mdz k", lastname="zCQ ")]

# testdata = [Contact(firstname="Алексей", \
#                     middlename="Иларионовна", \
#                     lastname="Баранцев", \
#                     work="суперпрепод", \
#                     address="Не дом и не улица", \
#                     mobile='8915223344')]


@pytest.mark.parametrize("add_contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contacts(app, add_contact):
    old_contact = app.contact.get_contact_list()
    app.contact.add_contact(add_contact)
    assert len(old_contact) + 1 == app.contact.count()
    old_contact.append(add_contact)
    new_contact = app.contact.get_contact_list()
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)

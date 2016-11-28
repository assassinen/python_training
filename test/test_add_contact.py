# -*- coding: utf-8 -*-
from model.contact import Contact


# def test_add_Contact(app):
#     old_contact = app.contact.get_Contact_list()
#     addContact = BookContact(firstname="Алексей", middlename="Иларионовна", lastname="Баранцев", work="суперпрепод", address="Не дом и не улица", mobile='8915223344')
#     app.contact.add_Contact(addContact)
#     assert len(old_contact) + 1 == app.contact.count()
#     old_contact.append(addContact)
#     new_Contact = app.contact.get_Contact_list()
#     assert sorted(old_contact, key=BookContact.id_or_max) == sorted(new_Contact, key=BookContact.id_or_max)

def test_add_contacts(app):
    for i in range (1, 6):
        old_contact = app.contact.get_contact_list()
        add_contact = Contact(firstname="Алексей"+str(i), \
                             middlename="Иларионовна"+str(i), \
                             lastname="Баранцев"+str(i), \
                             work="суперпрепод"+str(i), \
                             address="Не дом и не улица"+str(i), \
                             mobile='8915223344'+str(i))
        app.contact.add_contact(add_contact)
        assert len(old_contact) + 1 == app.contact.count()
        old_contact.append(add_contact)
    new_contact = app.contact.get_contact_list()
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)

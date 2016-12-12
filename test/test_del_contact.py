# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_delete_some_contact(app, db, data_contacts, chech_ui):
    if app.contact.count() == 0:
        add_contact = data_contacts
        app.contact.add_contact(add_contact)
    old_contact = db.get_contact_list()
    contact = random.choice(old_contact)
    app.contact.delete_contact_by_id(contact.paramentr['id'])
    assert len(old_contact) - 1 == app.contact.count()
    old_contact.remove(contact)
    new_contact = db.get_contact_list()
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
    if chech_ui:
        assert sorted(app.contact.get_contact_list(), key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


# def test_delete_all_contact(app, db, chech_ui):
#     #old_contact = app.contact.get_contact_list()
#     old_contact = db.get_contact_list()
#     while len(db.get_contact_list()):
#         app.contact.delete_first_contact()
#         assert len(old_contact) - 1 == app.contact.count()
#         old_contact[0:1] = []
#     #new_contact = app.contact.get_contact_list()
#     new_contact = db.get_contact_list()
#     if chech_ui:
#         assert old_contact == new_contact
#         assert 0 == len(new_contact)
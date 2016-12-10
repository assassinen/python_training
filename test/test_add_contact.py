# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contacts(app, json_contacts, chech_ui):
    add_contact = json_contacts
    old_contact = app.contact.get_contact_list()
    app.contact.add_contact(add_contact)
    assert len(old_contact) + 1 == app.contact.count()
    old_contact.append(add_contact)
    new_contact = app.contact.get_contact_list()
    if chech_ui:
        assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)

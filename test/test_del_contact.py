# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_delete_some_contact(app):
    if app.contact.count() == 0:
        add_contact = Contact(firstname="Алексей", middlename="Иларионовна", lastname="Баранцев", work="суперпрепод", address="Не дом и не улица", mobile='8915223344')
        app.contact.add_contact(add_contact)
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    app.contact.delete_contact_by_index(index)
    assert len(old_contact) - 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact[index:index+1] = []
    assert old_contact == new_contact


def test_delete_all_contact(app):
    old_contact = app.contact.get_contact_list()
    while len(app.contact.get_contact_list()):
        app.contact.delete_first_contact()
        assert len(old_contact) - 1 == app.contact.count()
        old_contact[0:1] = []
    new_contact = app.contact.get_contact_list()
    assert old_contact == new_contact
    assert 0 == len(new_contact)
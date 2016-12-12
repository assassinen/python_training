# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_edit_contact(app, db, data_contacts, chech_ui):
    if app.contact.count() == 0:
        add_contact = data_contacts
        app.contact.add_contact(add_contact)
    #получаем список контактов с web-страницы
    old_contact = db.get_contact_list()
    contact = random.choice(old_contact)
    #формируем контакт с изменениями, который хотим внести
    add_contact = Contact(mobile='8915223344', middlename="Иванович")
    #запоминаем id изменяемого контакта и дополняем им созданные вышу контакт
    add_contact.paramentr['id'] = contact.paramentr['id']
    if add_contact.paramentr['lastname'] is None:
        add_contact.paramentr['lastname'] = contact.paramentr['lastname']
    if add_contact.paramentr['firstname'] is None:
        add_contact.paramentr['firstname'] = contact.paramentr['firstname']
    #изменяем полученный список в соответсвии с выполненными изменениями
    #old_contact.id = add_contact
    old_contact.remove(contact)
    old_contact.append(add_contact)
    #вносим изменения
    app.contact.edit_contact_by_id(contact.paramentr['id'], add_contact)
    #сравниваем количество записей до и после именений
    assert len(old_contact) == app.contact.count()
    #получаем список контактов с web-страницы после изменения
    new_contact = db.get_contact_list()
    #сравниваем списко контактов до и после изменений
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
    if chech_ui:
        assert sorted(app.contact.get_contact_list(), key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)

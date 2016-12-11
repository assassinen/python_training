# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_edit_contact(app, data_contacts, chech_ui):
    if app.contact.count() == 0:
        add_contact = data_contacts
        app.contact.add_contact(add_contact)
    #получаем список контактов с web-страницы
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    #формируем контакт с изменениями, который хотим внести
    add_contact = Contact(mobile='8915223344', middlename="Иванович")
    #запоминаем id изменяемого контакта и дополняем им созданные вышу контакт
    add_contact.paramentr['id'] = old_contact[index].paramentr['id']
    if add_contact.paramentr['lastname'] is None:
        add_contact.paramentr['lastname'] = old_contact[index].paramentr['lastname']
    if add_contact.paramentr['firstname'] is None:
        add_contact.paramentr['firstname'] = old_contact[index].paramentr['firstname']
    #изменяем полученный список в соответсвии с выполненными изменениями
    old_contact[index] = add_contact
    #вносим изменения
    app.contact.edit_contact_by_index(index, add_contact)
    #app.contact.open_contact_to_edit_by_index(index)
    #сравниваем количество записей до и после именений
    assert len(old_contact) == app.contact.count()
    #получаем список контактов с web-страницы после изменения
    new_contact = app.contact.get_contact_list()
    #сравниваем списко контактов до и после изменений
    if chech_ui:
        assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)

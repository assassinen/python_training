__author__ = 'NovikovII'

from model.contact import Contact
import random


def test_add_contact_to_group(app, orm, data_contacts, data_groups):
    # создаем группу если список групп пуст
    if app.group.count() == 0:
        app.group.create(data_groups)
    all_groups = orm.get_group_list()
    group = random.choice(all_groups)
    # создаем контакт если список контактов пуст или нет контакта, который не находится в заданной группе
    contacts = orm.get_contacts_not_in_group(group)
    if len(contacts) == 0:
        add_contact = data_contacts
        app.contact.add_contact(add_contact)
        contacts = orm.get_contacts_not_in_group(group)
    contact = random.choice(contacts)
    old_contacts = orm.get_contacts_in_group(group)
    app.contact.add_to_group(contact, group)
    new_contacts = orm.get_contacts_in_group(group)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
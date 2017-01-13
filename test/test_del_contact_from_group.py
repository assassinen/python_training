__author__ = 'NovikovII'

from model.contact import Contact
from model.group import Group
import random


def test_del_contact_from_group(app, orm, data_contacts, data_groups):
    all_groups = orm.get_group_list()
    all_contacts = orm.get_contact_list()
    # получаем список групп в которых есть контакты
    groups = list(filter(lambda x: len(orm.get_contacts_in_group(x)) > 0, all_groups))
    if len(groups) == 0:
        if len(all_groups) == 0:
            app.group.create(data_groups)
            all_groups = orm.get_group_list()
        group = random.choice(all_groups)
        if len(all_contacts) == 0:
            add_contact = data_contacts
            app.contact.add_contact(add_contact)
            all_contacts = orm.get_contacts_not_in_group(group)
        contact = random.choice(all_contacts)
        app.contact.add_to_group(contact, group)
    groups = list(filter(lambda x: len(orm.get_contacts_in_group(x)) > 0, all_groups))
    # выбор группы и контакта из группы, который следует исключить
    group = random.choice(groups)

    old_contacts = orm.get_contacts_in_group(group)
    contact = random.choice(old_contacts)
    app.contact.del_from_group(contact, group)
    new_contacts = orm.get_contacts_in_group(group)
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

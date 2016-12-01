__author__ = 'NovikovII'

import re
import random
from model.contact import Contact

def random_contact(app):
    count = app.contact.count()
    return random.randint(0, count-1)

def test_phones_on_home_page(app):
    if app.contact.count() == 0:
        add_contact = Contact(firstname="Алексей", middlename="Иларионовна", lastname="Баранцев", work="суперпрепод", address="Не дом и не улица", mobile='8(915)223344')
        app.contact.add_contact(add_contact)
    #получаем список контактов с web-страницы
    edit_contact = random_contact(app)
    contact_from_home_page = app.contact.get_contact_list()[edit_contact]
    contact_from_edit_page = app.contact.get_contact_list_info_from_edit_page(edit_contact)
    assert contact_from_home_page.parament['all_phone_from_home_page'] == merge_phone_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.parament['all_emal_from_home_page'] == merge_email_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.parament['lastname'] == contact_from_edit_page.parament['lastname']
    assert contact_from_home_page.parament['firstname'] == contact_from_edit_page.parament['firstname']
    assert contact_from_home_page.parament['address'] == contact_from_edit_page.parament['address']


def test_phones_on_contact_view_page(app):
    if app.contact.count() == 0:
        add_contact = Contact(firstname="Алексей", middlename="Иларионовна", lastname="Баранцев", work="суперпрепод", address="Не дом и не улица", mobile='8(915)223344')
        app.contact.add_contact(add_contact)
    #получаем список контактов с web-страницы
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_list_info_from_edit_page(0)
    assert contact_from_view_page.parament['mobile'] == contact_from_edit_page.parament['mobile']

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phone_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.parament['home'], contact.parament['mobile'], contact.parament['work'], contact.parament['phone2']]))))

def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                  [contact.parament['email'], contact.parament['email2'], contact.parament['email3']])))

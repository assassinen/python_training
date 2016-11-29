__author__ = 'NovikovII'

import re
from model.contact import Contact

def test_phones_on_home_page(app):
    if app.contact.count() == 0:
        add_contact = Contact(firstname="Алексей", middlename="Иларионовна", lastname="Баранцев", work="суперпрепод", address="Не дом и не улица", mobile='8(915)223344')
        app.contact.add_contact(add_contact)
    #получаем список контактов с web-страницы
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_list_info_from_edit_page(0)
    assert contact_from_home_page.parament['mobile'] == clear(contact_from_edit_page.parament['mobile'])

def clear(s):
    return re.sub("[() -]", "", s)
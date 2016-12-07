__author__ = 'NovikovII'

import re
import random
from model.contact import Contact

def random_contact(app):
    count = app.contact.count()
    return random.randint(0, count-1)

def test_phones_on_home_page(app, data_contacts):
    if app.contact.count() == 0:
        app.contact.add_contact(data_contacts)
    #получаем список контактов с web-страницы
    edit_contact = random_contact(app)
    contact_from_home_page = app.contact.get_contact_list()[edit_contact]
    contact_from_edit_page = app.contact.get_contact_list_info_from_edit_page(edit_contact)
    assert contact_from_home_page.paramentr['all_phone_from_home_page'] == merge_phone_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.paramentr['all_emal_from_home_page'] == merge_email_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.paramentr['lastname'] == contact_from_edit_page.paramentr['lastname']
    assert contact_from_home_page.paramentr['firstname'] == contact_from_edit_page.paramentr['firstname']
    assert contact_from_home_page.paramentr['address'] == contact_from_edit_page.paramentr['address']


def test_phones_on_contact_view_page(app, data_contacts):
    if app.contact.count() == 0:
        app.contact.add_contact(data_contacts)
    #получаем список контактов с web-страницы
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_list_info_from_edit_page(0)
    assert contact_from_view_page.paramentr['mobile'] == contact_from_edit_page.paramentr['mobile']

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phone_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.paramentr['home'], contact.paramentr['mobile'], contact.paramentr['work'], contact.paramentr['phone2']]))))

def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                  [contact.paramentr['email'], contact.paramentr['email2'], contact.paramentr['email3']])))

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
    print(123)
    print(contact_from_home_page)
    assert False
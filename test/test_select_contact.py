__author__ = 'NovikovII'
from model.contact import Contact
import time


def test_select_contact(app):
    add_contact = Contact(mobile='8915223344', middlename="Иванович")
    if add_contact.paramentr['lastname'] is None:
        add_contact.paramentr['lastname'] = contact.paramentr['lastname']
    if add_contact.paramentr['firstname'] is None:
        add_contact.paramentr['firstname'] = contact.paramentr['firstname']
    app.contact.edit_contact_by_id(755, add_contact)
    #app.contact.edit_contact_by_index(2, add_contact)
    time.sleep(2)

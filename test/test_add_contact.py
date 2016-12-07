# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
from data.add_contact import constant as testdata
from data.add_contact import err_date as testdata
from data.add_contact import testdata as testdata



@pytest.mark.parametrize("add_contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contacts(app, add_contact):
    old_contact = app.contact.get_contact_list()
    app.contact.add_contact(add_contact)
    assert len(old_contact) + 1 == app.contact.count()
    old_contact.append(add_contact)
    new_contact = app.contact.get_contact_list()
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)

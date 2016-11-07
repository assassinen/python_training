# -*- coding: utf-8 -*-
import pytest
from book_entry import BookEntry
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_test_add_entry(app):
    app.login(username="admin", password="secret")
    addEntry = BookEntry(firstname="Алексей", middlename="Иларионовна", lastname="Баранцев", work="суперпрепод", address="Не дом и не улица", mobile='8915223344')
    app.add_book_entry(addEntry)
    app.logout()

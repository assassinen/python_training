# -*- coding: utf-8 -*-
import pytest
from model.book import BookEntry
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_entry(app):
    app.session.login(username="admin", password="secret")
    addEntry = BookEntry(firstname="Алексей", middlename="Иларионовна", lastname="Баранцев", work="суперпрепод", address="Не дом и не улица", mobile='8915223344')
    app.book.add_entry(addEntry)
    app.session.logout()

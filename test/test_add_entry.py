# -*- coding: utf-8 -*-
from model.book import BookEntry


def test_add_entry(app):
    addEntry = BookEntry(firstname="Алексей", middlename="Иларионовна", lastname="Баранцев", work="суперпрепод", address="Не дом и не улица", mobile='8915223344')
    app.book.add_entry(addEntry)
    app.book.add_entry(addEntry)

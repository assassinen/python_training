# -*- coding: utf-8 -*-
from model.book import BookEntry


def test_edit_entry(app):
    if app.book.count() == 0:
        addEntry = BookEntry(firstname="Алексей", middlename="Иларионовна", lastname="Баранцев", work="суперпрепод", address="Не дом и не улица", mobile='8915223344')
        app.book.add_entry(addEntry)
    addEntry = BookEntry(firstname="Алексей", middlename="Иванович", lastname="Баранцев", work="суперпрепод", address="Не дом и не улица", mobile='8915223344')
    app.book.edit_first_entry(addEntry)


# -*- coding: utf-8 -*-
from model.book import BookEntry


def test_edit_entry(app):
    addEntry = BookEntry(firstname="Алексей", middlename="Иванович", lastname="Баранцев", work="суперпрепод", address="Не дом и не улица", mobile='8915223344')
    app.book.edit_first_entry(addEntry)


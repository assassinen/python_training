# -*- coding: utf-8 -*-
from model.book import BookEntry


def test_delete_first_entry(app):
    if app.book.count() == 0:
        addEntry = BookEntry(firstname="Алексей", middlename="Иларионовна", lastname="Баранцев", work="суперпрепод", address="Не дом и не улица", mobile='8915223344')
        app.book.add_entry(addEntry)
    old_entry = app.book.get_entry_list()
    app.book.delete_first_entry()
    new_entry = app.book.get_entry_list()
    assert len(old_entry) - 1 == len(new_entry)

# def test_delete_all_entry(app):
#     while len(app.book.get_entry_list()):
#         app.book.delete_first_entry()
#     new_entry = app.book.get_entry_list()
#     assert 0 == len(new_entry)
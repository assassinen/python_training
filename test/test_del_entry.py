# -*- coding: utf-8 -*-
from model.book import BookEntry
from random import randrange


def test_delete_some_entry(app):
    if app.book.count() == 0:
        addEntry = BookEntry(firstname="Алексей", middlename="Иларионовна", lastname="Баранцев", work="суперпрепод", address="Не дом и не улица", mobile='8915223344')
        app.book.add_entry(addEntry)
    old_entry = app.book.get_entry_list()
    index = randrange(len(old_entry))
    app.book.delete_entry_by_index(index)
    assert len(old_entry) - 1 == app.book.count()
    new_entry = app.book.get_entry_list()
    old_entry[index:index+1] = []
    assert old_entry == new_entry

def test_delete_all_entry(app):
    old_entry = app.book.get_entry_list()
    while len(app.book.get_entry_list()):
        app.book.delete_first_entry()
        assert len(old_entry) - 1 == app.book.count()
        old_entry[0:1] = []
    new_entry = app.book.get_entry_list()
    assert old_entry == new_entry
    assert 0 == len(new_entry)
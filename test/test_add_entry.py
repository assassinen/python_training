# -*- coding: utf-8 -*-
from model.book import BookEntry


# def test_add_entry(app):
#     old_entry = app.book.get_entry_list()
#     addEntry = BookEntry(firstname="Алексей", middlename="Иларионовна", lastname="Баранцев", work="суперпрепод", address="Не дом и не улица", mobile='8915223344')
#     app.book.add_entry(addEntry)
#     assert len(old_entry) + 1 == app.book.count()
#     old_entry.append(addEntry)
#     new_entry = app.book.get_entry_list()
#     assert sorted(old_entry, key=BookEntry.id_or_max) == sorted(new_entry, key=BookEntry.id_or_max)

def test_add_entrys(app):
    for i in range (1, 6):
        old_entry = app.book.get_entry_list()
        addEntry = BookEntry(firstname="Алексей"+str(i), \
                             middlename="Иларионовна"+str(i), \
                             lastname="Баранцев"+str(i), \
                             work="суперпрепод"+str(i), \
                             address="Не дом и не улица"+str(i), \
                             mobile='8915223344'+str(i))
        app.book.add_entry(addEntry)
        assert len(old_entry) + 1 == app.book.count()
        old_entry.append(addEntry)
    new_entry = app.book.get_entry_list()
    assert sorted(old_entry, key=BookEntry.id_or_max) == sorted(new_entry, key=BookEntry.id_or_max)

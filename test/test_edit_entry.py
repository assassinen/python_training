# -*- coding: utf-8 -*-
from model.book import BookEntry


def test_edit_entry(app):
    if app.book.count() == 0:
        addEntry = BookEntry(firstname="Алексей", middlename="Иларионовна", lastname="Баранцев", work="суперпрепод", address="Не дом и не улица", mobile='8915223344')
        app.book.add_entry(addEntry)
    #получаем список контактов с web-страницы
    old_entry = app.book.get_entry_list()
    #формируем контакт с изменениями, который хотим внести
    addEntry = BookEntry(firstname="Алексей", middlename="Иванович", lastname="Баранцев", work="суперпрепод", address="Не дом и не улица", mobile='8915223344')
    #запоминаем id изменяемого контакта и дополняем им созданные вышу контакт
    addEntry.parament['id'] = old_entry[0].parament['id']
    #изменяем полученный список в соответсвии с выполненными изменениями
    old_entry[0] = addEntry
    #вносим изменения
    app.book.edit_first_entry(addEntry)
    #получаем список контактов с web-страницы после изменения
    new_entry = app.book.get_entry_list()
    #сравниваем списко контактов до и после изменений
    assert sorted(old_entry, key=BookEntry.id_or_max) == sorted(new_entry, key=BookEntry.id_or_max)
    #сравниваем количество записей до и после именений
    assert len(old_entry) == len(new_entry)

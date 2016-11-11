# -*- coding: utf-8 -*-
from model.book import BookEntry


def test_delete_first_entry(app):
    app.book.delete_first_entry()

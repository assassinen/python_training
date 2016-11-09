# -*- coding: utf-8 -*-
from model.book import BookEntry


def test_delete_first_entry(app):
    app.session.login(username="admin", password="secret")
    app.book.delete_first_entry()
    app.session.logout()

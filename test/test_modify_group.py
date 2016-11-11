__author__ = 'NovikovII'

# -*- coding: utf-8 -*-
from model.group import Group

def test_modify_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify(Group(name="modify_name"))
    app.session.logout()

def test_modify_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.modify(Group(header="modify_header"))
    app.session.logout()
__author__ = 'NovikovII'

# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.group.create(Group(name="test", header="test", footer="test"))
    #app.session.logout()

def test_add_empty_group(app):
    for i in range (1, 6):
        app.group.create(Group(name="test"+str(i), header="test"+str(i), footer="test"+str(i)))


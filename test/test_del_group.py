__author__ = 'NovikovII'

# -*- coding: utf-8 -*-
from model.group import Group


def test_delele_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test", footer="test"))
    app.group.delete_first_group()


def test_delele_all_group(app):
    if app.group.count() == 0:
        for i in range (1, 6):
            app.group.create(Group(name="test"+str(i), header="test"+str(i), footer="test"+str(i)))
    app.group.delete_all_group()

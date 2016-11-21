__author__ = 'NovikovII'

# -*- coding: utf-8 -*-
from model.group import Group

def test_add_empty_group(app):
    for i in range (1, 6):
        app.group.create(Group(name="test"+str(i), header="test"+str(i), footer="test"+str(i)))
    app.session.logout()


def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="test", header="test", footer="test"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


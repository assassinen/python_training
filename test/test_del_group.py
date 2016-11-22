__author__ = 'NovikovII'

# -*- coding: utf-8 -*-
from model.group import Group


def test_delele_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test", footer="test"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0:1] = []
    assert old_groups == new_groups


def test_delele_all_group(app):
    if app.group.count() == 0:
        for i in range(1, 2):
            app.group.create(Group(name="test"+str(i), header="test"+str(i), footer="test"+str(i)))
    app.group.delete_all_group()
    assert 0 == app.group.count()



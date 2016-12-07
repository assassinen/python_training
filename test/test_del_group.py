__author__ = 'NovikovII'

# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_delele_some_group(app, data_groups):
    if app.group.count() == 0:
        app.group.create(data_groups)
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index:index+1] = []
    assert old_groups == new_groups


def test_delele_all_group(app, json_groups):
    if app.group.count() == 0:
        app.group.create(json_groups)
    app.group.delete_all_group()
    assert 0 == app.group.count()



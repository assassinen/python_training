__author__ = 'NovikovII'

# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_modify_group_name(app, data_groups):
    if app.group.count() == 0:
        app.group.create(data_groups)
    old_groups = app.group.get_group_list()

    index = randrange(len(old_groups))
    group = Group(name="modify_name")
    group.id = old_groups[index].id
    app.group.modify(index, group)

    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(data_groups)
    old_groups = app.group.get_group_list()

    group = Group(header="modify_header")
    group.id = old_groups[0].id
    app.group.modify(0, group)

    assert len(old_groups) == app.group.count()
    # new_groups = app.group.get_group_list()
    # old_groups[0] = group
    # assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
